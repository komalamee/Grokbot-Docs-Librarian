#!/usr/bin/env python3
"""Tests for fixed-files/librarian.py. Fake documents and public text only; no one's real data.

  python3 -m unittest discover -s bot/tests -v
"""
import importlib.util, io, os, shutil, sys, tempfile, unittest, zipfile
from contextlib import redirect_stdout
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "fixed-files" / "librarian.py"
spec = importlib.util.spec_from_file_location("librarian", TOOL)
librarian = importlib.util.module_from_spec(spec)
spec.loader.exec_module(librarian)

POLICY = """TRAVEL COVER POLICY WORDING
Section 1 Cover
The excess payable on each claim is 100 pounds.
Cover applies in Europe only.

Section 2 Exclusions
We do not cover winter sports.

Section 3 Cancellation
You may cancel within 14 days of the start date and get a full refund.
"""

CONTRACT = """SERVICE AGREEMENT
Clause 4 Term and notice
The term is 12 months and either party may give 30 days notice to end it.
"""


def docx(path: Path, text: str) -> None:
    """A .docx with one paragraph, built the way Word lays one out."""
    body = f"<w:document xmlns:w='x'><w:body><w:p><w:r><w:t>{text}</w:t></w:r></w:p></w:body></w:document>"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("[Content_Types].xml", "<Types/>")
        z.writestr("word/document.xml", body)


def pdf(path: Path, lines: list[str] | None) -> None:
    """A one-page PDF. lines=None leaves the page empty, which is what a scan without OCR looks like."""
    content = ""
    for i, line in enumerate(lines or []):
        content += f"BT /F1 12 Tf 72 {720 - i * 16} Td ({line}) Tj ET\n"
    objs = [
        "<< /Type /Catalog /Pages 2 0 R >>",
        "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        "/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        f"<< /Length {len(content)} >>\nstream\n{content}\nendstream",
        "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = "%PDF-1.4\n"
    for i, obj in enumerate(objs, 1):
        out += f"{i} 0 obj\n{obj}\nendobj\n"
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\n%%EOF\n"
    path.write_bytes(out.encode("latin-1"))


def pdf_pages(path: Path, pages: list[list[str]]) -> None:
    """A PDF with one page per list of lines, so pdftotext puts a form feed between pages."""
    n = len(pages)
    objs = ["<< /Type /Catalog /Pages 2 0 R >>",
            "<< /Type /Pages /Kids [" + " ".join(f"{3 + 2 * i} 0 R" for i in range(n)) + f"] /Count {n} >>"]
    for i, lines in enumerate(pages):
        content = "".join(f"BT /F1 12 Tf 72 {720 - j * 16} Td ({line}) Tj ET\n" for j, line in enumerate(lines))
        objs.append("<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
                    f"/Resources << /Font << /F1 {3 + 2 * n} 0 R >> >> /Contents {4 + 2 * i} 0 R >>")
        objs.append(f"<< /Length {len(content)} >>\nstream\n{content}\nendstream")
    objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    out = "%PDF-1.4\n"
    for i, obj in enumerate(objs, 1):
        out += f"{i} 0 obj\n{obj}\nendobj\n"
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\n%%EOF\n"
    path.write_bytes(out.encode("latin-1"))


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        os.environ["DOCS_LIBRARIAN_HOME"] = str(self.tmp / "store")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.addCleanup(os.environ.pop, "DOCS_LIBRARIAN_HOME", None)

    def run_tool(self, *argv):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = librarian.main(list(argv))
        return code, buf.getvalue()

    def write(self, name, text):
        path = self.tmp / name
        path.write_text(text, encoding="utf-8")
        return str(path)

    def add_policy(self, docid="msg1:policy.txt", doctype="insurance"):
        card = self.write("card.md", "Summary: a made-up travel policy for testing.\n"
                                     '- Excess: "The excess payable on each claim is 100 pounds." (Section 1)\n')
        return self.run_tool("add", "--id", docid, "--file", self.write("policy.txt", POLICY),
                             "--name", "Test travel policy", "--type", doctype,
                             "--provider", "Test Insurer", "--link", "https://example.invalid/1",
                             "--card", card)

    # add ------------------------------------------------------------------
    def test_add_writes_text_card_and_catalog(self):
        code, out = self.add_policy()
        self.assertEqual(code, 0)
        self.assertIn("ADDED", out)
        store = Path(os.environ["DOCS_LIBRARIAN_HOME"])
        self.assertTrue((store / "text" / "msg1_policy.txt.txt").exists())
        self.assertTrue((store / "cards" / "msg1_policy.txt.md").exists())
        self.assertEqual(oct(store.stat().st_mode)[-3:], "700")
        code, out = self.run_tool("catalog", "--json")
        self.assertIn('"provider": "Test Insurer"', out)
        self.assertIn("1 document(s).", out)

    # find -----------------------------------------------------------------
    def test_find_ranks_matching_passages(self):
        self.add_policy()
        code, out = self.run_tool("find", "excess OR deductible")
        self.assertEqual(code, 0)
        self.assertIn("payable on each claim", out.lower())
        self.assertIn("msg1:policy.txt", out)

    def test_find_reports_no_match(self):
        self.add_policy()
        code, out = self.run_tool("find", "helicopter")
        self.assertEqual(code, 1)
        self.assertIn("NO MATCH", out)

    def test_find_respects_the_type_filter(self):
        self.add_policy()
        self.run_tool("add", "--id", "msg2:contract.txt", "--type", "contract",
                      "--file", self.write("contract.txt", CONTRACT))
        code, out = self.run_tool("find", "notice OR excess", "--type", "contract")
        self.assertEqual(code, 0)
        self.assertIn("msg2:contract.txt", out)
        self.assertNotIn("msg1:policy.txt", out)

    # verify ---------------------------------------------------------------
    def test_verify_accepts_a_real_quote(self):
        self.add_policy()
        code, out = self.run_tool("verify", "--id", "msg1:policy.txt",
                                  "--quote", "The excess payable on each claim is 100 pounds.")
        self.assertEqual(code, 0)
        self.assertIn("OK", out)

    def test_verify_catches_a_made_up_quote(self):
        self.add_policy()
        code, out = self.run_tool("verify", "--id", "msg1:policy.txt",
                                  "--quote", "The excess payable on each claim is 50 pounds.")
        self.assertEqual(code, 1)
        self.assertIn("MISMATCH", out)

    def test_verify_needs_the_text_first(self):
        code, out = self.run_tool("verify", "--id", "never-added", "--quote", "anything")
        self.assertEqual(code, 1)
        self.assertIn("NO TEXT", out)

    # file types -----------------------------------------------------------
    def test_docx_is_read(self):
        path = self.tmp / "terms.docx"
        docx(path, "Clause 9 Exit fee: the exit fee is 75 pounds.")
        code, out = self.run_tool("add", "--id", "msg3:terms.docx", "--type", "contract",
                                  "--file", str(path))
        self.assertEqual(code, 0)
        self.assertIn("ADDED", out)
        code, out = self.run_tool("find", "exit fee")
        self.assertIn("msg3:terms.docx", out)
        code, _ = self.run_tool("verify", "--id", "msg3:terms.docx",
                                "--quote", "the exit fee is 75 pounds")
        self.assertEqual(code, 0)

    def test_scanned_pdf_with_no_text_is_marked_not_indexed(self):
        path = self.tmp / "scan.pdf"
        pdf(path, None)
        code, out = self.run_tool("add", "--id", "msg4:scan.pdf", "--type", "other",
                                  "--file", str(path))
        self.assertEqual(code, 0)
        self.assertIn("SCANNED", out)
        self.assertIn("Read this document directly", out)
        _, cat = self.run_tool("catalog", "--json")
        self.assertIn('"scanned": true', cat)
        code, out = self.run_tool("find", "anything")
        self.assertEqual(code, 1)

    @unittest.skipIf(shutil.which("pdftotext") is None, "pdftotext not installed")
    def test_pdf_with_a_text_layer_is_read(self):
        path = self.tmp / "wording.pdf"
        pdf(path, ["Section 1 Cover",
                   "The excess payable on each claim is 100 pounds",
                   "Cover applies in Europe only and the policy runs for twelve months",
                   "Section 2 Exclusions",
                   "We do not cover winter sports or any claim made after the policy ends"])
        code, out = self.run_tool("add", "--id", "msg5:wording.pdf", "--type", "insurance",
                                  "--file", str(path))
        self.assertEqual(code, 0)
        self.assertIn("ADDED", out)
        code, _ = self.run_tool("verify", "--id", "msg5:wording.pdf",
                                "--quote", "The excess payable on each claim is 100 pounds")
        self.assertEqual(code, 0)

    # housekeeping ---------------------------------------------------------
    def test_rebuild_restores_the_index(self):
        self.add_policy()
        store = Path(os.environ["DOCS_LIBRARIAN_HOME"])
        (store / "index.db").unlink()
        code, out = self.run_tool("rebuild")
        self.assertEqual(code, 0)
        self.assertIn("REBUILT", out)
        code, out = self.run_tool("find", "winter sports")
        self.assertEqual(code, 0)
        self.assertIn("msg1:policy.txt", out)

    def test_missing_file_is_reported(self):
        code, out = self.run_tool("add", "--id", "nope", "--file", str(self.tmp / "gone.pdf"))
        self.assertEqual(code, 1)
        self.assertIn("MISSING", out)

    def test_verify_across_passage_boundary(self):
        """A quote spanning two ~900-char passages must still verify; page is where it starts."""
        pad = "word " * 430
        text = pad + "Alpha start " + ("fill " * 80) + "end beta finish."
        self.run_tool("add", "--id", "wide:doc.txt", "--file", self.write("wide.txt", text))
        quote = "Alpha start " + "fill " * 80 + "end beta"
        code, out = self.run_tool("verify", "--id", "wide:doc.txt", "--quote", quote)
        self.assertEqual(code, 0, out)
        self.assertIn("OK", out)
        self.assertRegex(out.lower(), r"(page|part) \d+")

    def test_reindex_keeps_metadata_unless_overwritten(self):
        self.add_policy()
        code, _ = self.run_tool("index", "--id", "msg1:policy.txt",
                                "--file", self.write("policy.txt", POLICY))
        self.assertEqual(code, 0)
        _, cat = self.run_tool("catalog", "--json")
        self.assertIn('"type": "insurance"', cat)
        self.assertIn('"provider": "Test Insurer"', cat)
        self.assertIn('"name": "Test travel policy"', cat)

    def test_type_filter_is_case_insensitive(self):
        self.add_policy(doctype="Insurance")
        _, cat = self.run_tool("catalog", "--json")
        self.assertIn('"type": "insurance"', cat)
        code, out = self.run_tool("find", "excess", "--type", "Insurance")
        self.assertEqual(code, 0)
        self.assertIn("msg1:policy.txt", out)
        code, out = self.run_tool("catalog", "--type", "Insurance")
        self.assertIn("msg1:policy.txt", out.split("\t")[0])

    def test_normalise_soft_hyphens_and_line_break_hyphens(self):
        text = "The excess pay\u00adable on each claim is one hun\u00addred pounds.\n"
        self.run_tool("add", "--id", "hyp:doc.txt", "--file", self.write("hyp.txt", text))
        code, out = self.run_tool("verify", "--id", "hyp:doc.txt",
                                  "--quote", "The excess payable on each claim is one hundred pounds.")
        self.assertEqual(code, 0, out)
        broken = "The total deduct\u00adible is fifty pounds unless the policy says other-\nwise here."
        self.run_tool("add", "--id", "hyp2:doc.txt", "--file", self.write("hyp2.txt", broken))
        code, out = self.run_tool("verify", "--id", "hyp2:doc.txt",
                                  "--quote", "the policy says otherwise here.")
        self.assertEqual(code, 0, out)

    def test_catalog_default_is_compact_and_json_flag(self):
        self.add_policy()
        _, compact = self.run_tool("catalog")
        self.assertNotIn('"provider"', compact)
        self.assertIn("Test Insurer", compact)
        self.assertIn("\t", compact)
        _, full = self.run_tool("catalog", "--json")
        self.assertIn('"provider": "Test Insurer"', full)

    def test_character_count_includes_whitespace(self):
        text = "  hello  world  \n"
        self.run_tool("add", "--id", "sp:doc.txt", "--file", self.write("sp.txt", text))
        _, cat = self.run_tool("catalog", "--json")
        self.assertIn('"chars": 17', cat)


    # v0.2.2 ---------------------------------------------------------------
    @unittest.skipIf(shutil.which("pdftotext") is None, "pdftotext not installed")
    def test_multipage_pdf_is_indexed_page_by_page(self):
        path = self.tmp / "three-pages.pdf"
        pdf_pages(path, [["Section 1 Cover", "The excess payable on each claim is 100 pounds"],
                         ["Section 2 Exclusions", "We do not cover zebra rides or winter sports"],
                         ["Section 3 Cancellation", "You may cancel within 14 days for a yak refund"]])
        code, out = self.run_tool("add", "--id", "msg6:three.pdf", "--type", "insurance", "--file", str(path))
        self.assertEqual(code, 0, out)
        self.assertIn("3 passages indexed", out)
        _, out = self.run_tool("find", "zebra")
        self.assertIn("page 2 (text)", out)
        _, out = self.run_tool("find", "yak")
        self.assertIn("page 3 (text)", out)
        _, out = self.run_tool("verify", "--id", "msg6:three.pdf", "--quote", "You may cancel within 14 days")
        self.assertIn("found on page 3", out)

    def test_long_multi_paragraph_text_gives_several_parts(self):
        paras = [f"Paragraph {i}. " + "This clause sets out ordinary terms for the agreement. " * 3 for i in range(40)]
        paras[-1] += "The quokka clause ends here."
        self.run_tool("add", "--id", "long:doc.txt", "--file", self.write("long.txt", "\n\n".join(paras)))
        store = Path(os.environ["DOCS_LIBRARIAN_HOME"])
        import sqlite3
        with sqlite3.connect(store / "index.db") as conn:
            locs = [r[0] for r in conn.execute("SELECT loc FROM chunks WHERE kind = 'text'")]
        conn.close()
        self.assertGreater(len(locs), 5)
        self.assertEqual(len(locs), len(set(locs)))
        _, out = self.run_tool("find", "quokka")
        self.assertRegex(out, r"part (\d+) \(text\)")
        self.assertNotIn("part 1 (text)", out)

    def test_verify_real_hyphen_split_at_a_line_end(self):
        text = ("We are required to register all third-\nparty claims with the board.\n"
                "The excess reimburse-\nment limit is 500.\n")
        self.run_tool("add", "--id", "hy:doc.txt", "--file", self.write("hy.txt", text))
        for quote in ("register all third-party claims with the board.",
                      "The excess reimbursement limit is 500."):
            code, out = self.run_tool("verify", "--id", "hy:doc.txt", "--quote", quote)
            self.assertEqual(code, 0, quote + " -> " + out)
        code, _ = self.run_tool("verify", "--id", "hy:doc.txt", "--quote", "register all fourth-party claims")
        self.assertEqual(code, 1)

    def test_readd_without_card_keeps_the_card_indexed(self):
        _, first = self.add_policy()
        code, again = self.run_tool("add", "--id", "msg1:policy.txt", "--file", self.write("policy.txt", POLICY))
        self.assertEqual(code, 0)
        self.assertEqual(first.split(": ", 1)[1], again.split(": ", 1)[1])
        code, out = self.run_tool("find", "testing")
        self.assertEqual(code, 0)
        self.assertIn("(card)", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
