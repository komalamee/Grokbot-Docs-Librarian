# Fixed files

Files the bot needs on the user's side, shipped from this repo and installed on import (Koko, 29 Sep 2026).
Examples from the Docs Librarian spec: the folder set (policies, receipts/payments, deadlines) and the index Sheet layout, so every install builds the same Sheet.

## Rules
- List every file in `MANIFEST.md`: what it is, where it goes, which skill installs it, when.
- The setup step lives inside the bot (`<bot>-getting-started` or a `<bot>-setup` skill). It asks first, installs, then tells the user in one line what went where.
- Never overwrite a user's existing file without asking. Back up first.
- No private data, keys, owner paths or real names in these files. They pass `banned_scan.py`.
- Test on a clean install before release; keep the evidence in `proof/`.
- **Open point:** a bot installed on someone else's account can't be expected to read this private repo. Decide per bot in the spec how each file reaches the user: written out by a skill (small files), or fetched from a public, code-only location (pinned version + checksum).

`sheet-layout.example.json` shows the human-first Sheet design. Copy and adapt it, or delete it if the bot has no Sheet.
