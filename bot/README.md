# The Librarian (Grok Bot template)

A library for your contracts, policies and any long document you might need to look back at · Live link: not published yet · Current version: none (written, not tested yet)

| Folder / file | What |
|---|---|
| `bot.json` | Profile, connections (`pluginId` strings), memories, getting-started skill |
| `routines.json` | The one source for routines. Every routine `"enabled": false` |
| `skills/` | `docs-librarian-getting-started`, `docs-librarian-core-rules`, `docs-librarian-library`, `docs-librarian-renewals` |
| `fixed-files/` | The index Sheet layout and the folder set, fetched at setup from this public repo, pinned to the tag `fixed-files-v2`; URLs and checksums in `MANIFEST.md` |
| `docs/` | Website handoff, and the test results once there are some. Working notes are kept privately by the owner, not here |
| `listing/` | Marketplace listing copy and images (a draft for the owner to approve; finalised before publishing) |
| `proof/` | Screenshots and test-run evidence for each release (empty; nothing tested yet) |
| `samples/` | Fake data only: Sheet mock-ups, sample files |
| `args/` | Generated share args (by `build.py`; never hand-edited) |
| `build.py` · `banned_scan.py` · `banned.txt` · `allow.txt` | Build with hard checks; banned-word and private-data scan |

Build: `python3 build.py --allow allow.txt --private-terms ../private-terms.txt` (add `--check-live <live skills folder>` before release).
Scan: `python3 banned_scan.py skills listing args --banned banned.txt --allow allow.txt --private-terms ../private-terms.txt`.

`private-terms.txt` is the owner's own file and never lives in this repo: keep it outside the checkout, or at the repo root where `.gitignore` covers it.

`allow.txt` is the other half of that: exact public strings that both scans skip, namely this bot's 33-character routine slug, the two pinned raw-URL prefixes and the repository URL. Both `build.py` and `banned_scan.py` now apply it to private-data hits as well as banned phrases, so a private-terms file may list the owner's handle without the bot's own fetch URLs failing the run. Every line is matched literally and only excuses itself, so never put a bare name or handle in it: that would also hide every email address and path built from it. The published author name in the listing is the one thing to leave out of `private-terms.txt` altogether.

**What the scan covers.** It reads the bot's own wording: the skills, the listing and the packed args. It is not a test of what the bot quotes back: the core rules require quoting a clause word for word, so a banned word can legitimately appear inside quotation marks in a reply. Scanning a transcript of real bot output is useful, but read each hit before calling it a failure — inside a verbatim quote it is allowed, in the bot's own words it is not.
