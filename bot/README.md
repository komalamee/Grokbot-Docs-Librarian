# Docs Librarian (Grok Bot template)

A library for your contracts, policies and any long document you might need to look back at · Live link: not published yet · Current version: none (built from the spec, not tested yet)

| Folder / file | What |
|---|---|
| `bot.json` | Profile, connections (`pluginId` strings), memories, getting-started skill |
| `routines.json` | The one source for routines. Every routine `"enabled": false` |
| `skills/` | `docs-librarian-getting-started`, `docs-librarian-core-rules`, `docs-librarian-library`, `docs-librarian-renewals`, all written from `docs/SPEC.md` |
| `fixed-files/` | The index Sheet layout and the folder set, fetched at setup from this public repo (raw URLs on `main`); listed in `MANIFEST.md` |
| `docs/` | `INTAKE.md`, `SPEC.md` (both approved, unchanged), `RETEST.md` later, website handoff |
| `listing/` | Marketplace listing copy and images (a draft for the owner to approve; finalised at gate ⑥) |
| `proof/` | Screenshots and test-run evidence for each release (empty; nothing tested yet) |
| `samples/` | Fake data only: Sheet mock-ups, sample files |
| `args/` | Generated share args (by `build.py`; never hand-edited) |
| `build.py` · `banned_scan.py` · `banned.txt` · `allow.txt` | Build with hard checks; banned-word and private-data scan |

Build: `python3 build.py --allow allow.txt --private-terms ../private-terms.txt` (add `--check-live <live skills folder>` before release).
Scan: `python3 banned_scan.py skills listing args --banned banned.txt --private-terms ../private-terms.txt`.

`private-terms.txt` is the owner's own file and never lives in this repo: keep it outside the checkout, or at the repo root where `.gitignore` covers it. `allow.txt` holds one entry: this bot's 33-character routine slug, which `build.py` would otherwise read as a token (see `../TEMPLATE-FEEDBACK.md`).
