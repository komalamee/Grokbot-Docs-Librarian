# Changelog: Docs Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL once the bot is published.

## v0.1.0 (not published) · 29 Sep 2026
- Built from the master template grokbot-template v0.1, with the upgraded rules in v0.2.
- Four skills written: `docs-librarian-getting-started` (the first conversation, the index Sheet, the folder set, the routines question), `docs-librarian-core-rules` (reply shape and the never list), `docs-librarian-library` (search, filing, the index, answers) and `docs-librarian-renewals` (the 30-day flag and the opt-in price comparison).
- `routines.json`: the inbox check, the renewal alert and the monthly look-ahead. Every one `"enabled": false`, each silent when there is nothing to report.
- `bot.json`: profile, the four connections (Gmail, Google Sheets, Google Drive, Google Calendar) and the bot's memories.
- Fixed files: `index-sheet-layout.json` and `folder-set.json`, fetched at setup from this public repo. Pinned to the tag `fixed-files-v1` rather than a branch, with SHA-256 checksums recorded in `fixed-files/MANIFEST.md`, so an install always gets the exact bytes that were tested.
- `listing/LISTING.md`: a draft; the wording still needs the owner's approval.
- The routines question and the banned-phrase list in `banned.txt` and the core-rules skill are approved as written.
- The repository is public and holds the bot's files only. The working notes behind the bot are kept privately by the owner.
- Build and scan run clean; `args/create_bot_share_json.args.json` is a pre-test build, not a release.

**Before the bot can fetch its fixed files, the tag `fixed-files-v1` has to exist on `main`.** The pinned URLs return 404 until it does. `v0.1.0` stays reserved for the published release.
