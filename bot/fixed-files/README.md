# Fixed files

Files the bot needs on the user's side, shipped from this repo and installed at setup: the folder set (policies, receipts and payments, deadlines) and the index Sheet layout, so every install builds the same Sheet.

## Rules
- List every file in `MANIFEST.md`: what it is, where it goes, which skill installs it, when.
- The setup step lives inside the bot (`<bot>-getting-started` or a `<bot>-setup` skill). It asks first, installs, then tells the user in one line what went where.
- Never overwrite a user's existing file without asking. Back up first.
- No private data, keys, owner paths or real names in these files. They pass `banned_scan.py`.
- Test on a clean install before release; keep the evidence in `proof/`.
- **How these reach the user here:** this repository is public, so each file is fetched from it at setup, pinned to a release tag and never to a branch, with its checksum recorded in `MANIFEST.md`. An install therefore gets the exact bytes that were tested, and nothing changes under a live user until the skill points at a new tag.

The files themselves: `index-sheet-layout-v2.json` is the Sheet the bot builds, `folder-set.json` is the Drive folder set, and `index-sheet-layout.json` is the earlier layout, kept so installs pinned to `fixed-files-v1` keep working.
