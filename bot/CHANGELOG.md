# Changelog: Docs Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL right after Koko presses Publish.

## v0.1.0 (not published) · 29 Sep 2026
- Made from grokbot-template v0.1.
- Repo set up: `bot-skeleton/` became `bot/`, `mybot` / `MyBot` became `docs-librarian` / `Docs Librarian`.
- Four skills written: `docs-librarian-getting-started` (the first conversation, the index Sheet, the folder set, the routines question), `docs-librarian-core-rules` (reply shape and the never list), `docs-librarian-library` (search, filing, the index, answers) and `docs-librarian-renewals` (the 30-day flag and the opt-in price comparison).
- `routines.json`: the inbox check, the renewal alert and the monthly look-ahead. Every one `"enabled": false`, each silent when there is nothing to report.
- `bot.json`: profile, the four connections (Gmail, Google Sheets, Google Drive, Google Calendar) and the bot's memories.
- Fixed files: `index-sheet-layout.json` and `folder-set.json`, fetched at setup from this public repo. Pinned to the release tag `v0.1.0` rather than a branch, with SHA-256 checksums recorded in `fixed-files/MANIFEST.md`, following the repo standard on pinned installs.
- `listing/LISTING.md`: a draft; the wording still needs the owner's approval.
- The routines question and the banned-phrase list in `banned.txt` and the core-rules skill are approved as written.
- The repository is public and holds the bot's files only. The intake notes and the build plan are kept privately by the owner and are not in this repo.
- Build and scan run clean; `args/create_bot_share_json.args.json` is a pre-test build, not a release.

**Before the bot can fetch its fixed files, the tag `v0.1.0` has to exist on `main`.** The pinned URLs return 404 until it does.
