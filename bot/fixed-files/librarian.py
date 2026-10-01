#!/usr/bin/env python3
"""The Librarian reading store: a private text copy of the owner's documents, searchable locally.

  librarian.py add --id ID --file PATH [--name N] [--type T] [--provider P] [--start D] [--ends D]
                   [--link URL] [--card PATH]
  librarian.py index ...                      same as add; run it again to refresh one document
  librarian.py find "excess OR deductible" [--type insurance] [--limit 8]
  librarian.py verify --id ID --quote "the exact words from the document"
  librarian.py catalog [--type insurance] [--json]
  librarian.py rebuild

Store: $DOCS_LIBRARIAN_HOME, or ~/.docs-librarian, created mode 700. It holds text/<id>.txt,
cards/<id>.md, catalog.jsonl and index.db (SQLite FTS5, ranked with BM25). It is a cache and
nothing else: the owner's mail, their filed copies and their Sheet stay the record. Nothing in it is
shared, uploaded or committed, and it is deleted only when the owner asks.

Standard library only: sqlite3, subprocess (pdftotext), zipfile (.docx).
"""
from __future__ import annotations
import argparse, json, os, re, sqlite3, subprocess, sys, unicodedata, zipfile
from contextlib import closing
from pathlib import Path

SCHEMA = "CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(" \
         "docid UNINDEXED, doctype UNINDEXED, kind UNINDEXED, loc UNINDEXED, body)"
QUOTE_MAP = {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
             "\u2013": "-", "\u2014": "-", "\u00a0": " "}
MIN_PER_PAGE = 50       # a PDF page with fewer real characters than this carries no text layer


def store() -> Path:
    root = Path(os.environ.get("DOCS_LIBRARIAN_HOME", Path.home() / ".docs-librarian"))
    root.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(root, 0o700)
    for sub in ("text", "cards"):
        (root / sub).mkdir(mode=0o700, exist_ok=True)
    return root


def safe(docid: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "_", docid)[:120]


def norm_light(s: str) -> str:
    """Unicode, punctuation and soft-hyphen normalisation. Keeps line and page breaks."""
    s = unicodedata.normalize("NFKC", s)
    for k, v in QUOTE_MAP.items():
        s = s.replace(k, v)
    return s.replace("\u00ad", "")


def norm_raw(s: str, keep_hyphen: bool = False) -> str:
    """norm_light, then join a word split by a hyphen at a line end ("reimburse-/ment").
    keep_hyphen=True keeps the hyphen instead, for real hyphens at a line end ("third-/party")."""
    return re.sub(r"-\s*\n\s*", "-" if keep_hyphen else "", norm_light(s))


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", norm_raw(s)).strip()


def prepare_text(text: str, keep_hyphen: bool = False) -> str:
    """Normalise a full document (or passage) before indexing or verifying."""
    return re.sub(r"\s+", " ", norm_raw(text, keep_hyphen)).strip()


def extract(path: Path) -> str:
    """Plain text of a PDF, .docx or text file. Empty string when nothing can be read."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            out = subprocess.run(["pdftotext", "-layout", str(path), "-"],
                                 capture_output=True, timeout=120)
            return out.stdout.decode("utf-8", "replace")
        except (OSError, subprocess.SubprocessError):
            return ""
    if suffix == ".docx":
        try:
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml").decode("utf-8", "replace")
        except (OSError, KeyError, zipfile.BadZipFile):
            return ""
        xml = re.sub(r"</w:p>", "\n\n", xml)
        xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
        return re.sub(r"<[^>]+>", "", xml)
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def passages(text: str, size: int = 900):
    """(label, passage) pairs. PDF page breaks become page numbers; anything else is numbered parts."""
    paged = "\f" in text
    blocks = text.split("\f") if paged else [text]
    part = 0
    for pageno, block in enumerate(blocks, 1):
        buf = ""
        for line in block.splitlines(keepends=True):
            if buf and len(buf) + len(line) > size:
                part += 1
                yield (f"page {pageno}" if paged else f"part {part}"), buf
                buf = ""
            buf += line
        if buf.strip():
            part += 1
            yield (f"page {pageno}" if paged else f"part {part}"), buf


def verify_in_document(raw_text: str, quote: str) -> str | None:
    """If quote appears in the normalised document, return starting loc; else None."""
    want = norm(quote)
    if not want:
        return None
    for keep in (False, True):                  # hyphen dropped, then hyphen kept, at line-end joins
        full = prepare_text(raw_text, keep)
        if want in full:
            break
    else:
        return None
    idx = full.find(want)
    pos = 0
    chunks = [(loc, prepare_text(body, keep)) for loc, body in passages(norm_light(raw_text))]
    chunks = [(loc, c) for loc, c in chunks if c]
    for i, (loc, chunk) in enumerate(chunks):
        end = pos + len(chunk)
        if pos <= idx < end:
            return loc
        pos = end
        if i + 1 < len(chunks):
            pos += 1
    return chunks[0][0] if chunks else None


def db(root: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(root / "index.db")
    conn.execute(SCHEMA)
    os.chmod(root / "index.db", 0o600)
    return conn


def read_catalog(root: Path) -> dict:
    path, out = root / "catalog.jsonl", {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                row = json.loads(line)
                out[row["id"]] = row
    return out


def write_catalog(root: Path, rows: dict) -> None:
    body = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows.values())
    (root / "catalog.jsonl").write_text(body, encoding="utf-8")
    os.chmod(root / "catalog.jsonl", 0o600)


def canon_type(t: str | None) -> str:
    return (t or "other").lower()


def index_one(conn, docid: str, doctype: str, text: str, card: str) -> int:
    conn.execute("DELETE FROM chunks WHERE docid = ?", (docid,))
    rows = [(docid, canon_type(doctype), "text", loc, prepare_text(body))
            for loc, body in passages(norm_light(text)) if body.strip()]
    rows += [(docid, canon_type(doctype), "card", "card", line.strip())
             for line in card.splitlines() if len(line.strip()) > 3]
    conn.executemany("INSERT INTO chunks(docid, doctype, kind, loc, body) VALUES (?,?,?,?,?)", rows)
    conn.commit()
    return len(rows)


def cmd_add(a) -> int:
    root = store()
    source = Path(a.file).expanduser()
    if not source.exists():
        print(f"MISSING: {source}")
        return 1
    text = extract(source)
    chars = len(text)
    real = len(re.sub(r"\s", "", text))
    pages = max(1, text.count("\f") or 1)
    scanned = source.suffix.lower() == ".pdf" and real < MIN_PER_PAGE * pages
    (root / "text" / f"{safe(a.id)}.txt").write_text(text, encoding="utf-8")
    os.chmod(root / "text" / f"{safe(a.id)}.txt", 0o600)
    card, card_path = "", root / "cards" / f"{safe(a.id)}.md"
    if getattr(a, "card", None):
        card = Path(a.card).expanduser().read_text(encoding="utf-8")
        card_path.write_text(card, encoding="utf-8")
        os.chmod(card_path, 0o600)
    elif card_path.exists():                    # re-add without --card keeps the saved card indexed
        card = card_path.read_text(encoding="utf-8")
    rows = read_catalog(root)
    prev = rows.get(a.id, {})
    row = {"id": a.id}
    row["name"] = a.name if hasattr(a, "name") else (prev.get("name") or source.name)
    row["type"] = canon_type(a.type if hasattr(a, "type") else prev.get("type"))
    row["provider"] = a.provider if hasattr(a, "provider") else prev.get("provider", "")
    row["start"] = a.start if hasattr(a, "start") else prev.get("start", "")
    row["ends"] = a.ends if hasattr(a, "ends") else prev.get("ends", "")
    row["link"] = a.link if hasattr(a, "link") else prev.get("link", "")
    row["scanned"] = scanned
    row["chars"] = chars
    rows[a.id] = row
    write_catalog(root, rows)
    if scanned:
        print(f"SCANNED {a.id}: no text layer, nothing indexed. Read this document directly.")
        return 0
    with closing(db(root)) as conn:
        n = index_one(conn, a.id, row["type"], text, card)
    print(f"ADDED {a.id}: {chars} characters, {n} passages indexed.")
    return 0


def cmd_find(a) -> int:
    root = store()
    sql = ("SELECT docid, doctype, kind, loc, snippet(chunks, 4, '[', ']', ' … ', 20), "
           "bm25(chunks) FROM chunks WHERE chunks MATCH ?")
    args: list = [a.query]
    if a.type:
        sql += " AND lower(doctype) = ?"
        args.append(a.type.lower())
    sql += " ORDER BY bm25(chunks) LIMIT ?"
    args.append(a.limit)
    with closing(db(root)) as conn:
        try:
            hits = conn.execute(sql, args).fetchall()
        except sqlite3.OperationalError:                  # bad FTS5 syntax: treat it as a phrase
            args[0] = '"' + a.query.replace('"', "") + '"'
            hits = conn.execute(sql, args).fetchall()
    if not hits:
        print("NO MATCH")
        return 1
    for i, (docid, doctype, kind, loc, snip, score) in enumerate(hits, 1):
        print(f"{i}. {docid} [{doctype}] {loc} ({kind}): {norm(snip)}")
    return 0


def cmd_verify(a) -> int:
    root = store()
    path = root / "text" / f"{safe(a.id)}.txt"
    if not path.exists():
        print(f"NO TEXT for {a.id}: add it first, or read the document directly.")
        return 1
    raw = path.read_text(encoding="utf-8")
    loc = verify_in_document(raw, a.quote)
    if loc:
        print(f"OK {a.id}: found on {loc}.")
        return 0
    print(f"MISMATCH {a.id}: those words are not in the text. Do not quote them.")
    return 1


def cmd_catalog(a) -> int:
    filt = a.type.lower() if a.type else None
    rows = [r for r in read_catalog(store()).values()
            if not filt or r.get("type", "").lower() == filt]
    for row in rows:
        if a.json:
            print(json.dumps(row, ensure_ascii=False))
        else:
            bits = [row.get("id", ""), row.get("name", ""), row.get("type", ""),
                    row.get("provider", ""), row.get("start", ""), row.get("ends", ""),
                    row.get("link", ""), str(row.get("chars", "")), str(row.get("scanned", ""))]
            print("\t".join(bits))
    print(f"{len(rows)} document(s).")
    return 0


def cmd_rebuild(a) -> int:
    root = store()
    total = 0
    with closing(db(root)) as conn:
        conn.execute("DELETE FROM chunks")
        conn.commit()
        for docid, row in read_catalog(root).items():
            text_path = root / "text" / f"{safe(docid)}.txt"
            card_path = root / "cards" / f"{safe(docid)}.md"
            if not text_path.exists() or row.get("scanned"):
                continue
            total += index_one(conn, docid, row.get("type", "other"),
                               text_path.read_text(encoding="utf-8"),
                               card_path.read_text(encoding="utf-8") if card_path.exists() else "")
    print(f"REBUILT: {total} passages from {len(read_catalog(root))} document(s).")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The Librarian reading store")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("add", "index"):
        p = sub.add_parser(name)
        p.add_argument("--id", required=True)
        p.add_argument("--file", required=True)
        for opt in ("name", "type", "provider", "start", "ends", "link", "card"):
            p.add_argument(f"--{opt}", action="store", default=argparse.SUPPRESS)
        p.set_defaults(fn=cmd_add)
    p = sub.add_parser("find")
    p.add_argument("query")
    p.add_argument("--type")
    p.add_argument("--limit", type=int, default=8)
    p.set_defaults(fn=cmd_find)
    p = sub.add_parser("verify")
    p.add_argument("--id", required=True)
    p.add_argument("--quote", required=True)
    p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("catalog")
    p.add_argument("--type")
    p.add_argument("--json", action="store_true", help="full JSON per document")
    p.set_defaults(fn=cmd_catalog)
    sub.add_parser("rebuild").set_defaults(fn=cmd_rebuild)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
