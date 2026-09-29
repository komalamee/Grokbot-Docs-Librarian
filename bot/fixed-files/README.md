# Fixed files

Files the bot needs on the user's side, shipped from this repo and installed on import (Koko, 29 Sep 2026).
Examples from the Docs Librarian spec: the folder set (policies, receipts/payments, deadlines) and the index Sheet layout, so every install builds the same Sheet.

## Rules
- List every file in `MANIFEST.md`: what it is, where it goes, which skill installs it, when.
- The setup step lives inside the bot (`<bot>-getting-started` or a `<bot>-setup` skill). It asks first, installs, then tells the user in one line what went where.
- Never overwrite a user's existing file without asking. Back up first.
- No private data, keys, owner paths or real names in these files. They pass `banned_scan.py`.
- Test on a clean install before release; keep the evidence in `proof/`.
- **How these reach the user here:** this repository is public, so each file is fetched from it at setup, pinned to a release tag and never to a branch, with its checksum recorded in `MANIFEST.md`. An install therefore gets the exact bytes that were tested, and nothing changes under a live user until the skill points at a new tag.

`sheet-layout.example.json` shows the human-first Sheet design. Copy and adapt it, or delete it if the bot has no Sheet.
