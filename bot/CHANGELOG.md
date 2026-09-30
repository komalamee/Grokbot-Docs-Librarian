# Changelog: Docs Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL once the bot is published.

## v0.1.1 (not published) · 30 Sep 2026
Sixteen fixes from the first live test run. Behaviour only; no new job.

Onboarding
- Message 1 is one short question and offers the two storage options the bot can actually serve: leave the files in email, or copy them to Google Drive. The "your computer" option is gone, because the bot cannot reach a laptop.
- Message 2 is one question, and it now carries the first result: the index Sheet is created and a quick 12-month search runs first, so message 2 opens with a count of real documents and the link before it asks about going back 5 years.
- The email branch is written out: nothing is copied, no folders are made, and the file link is the link to the message the document arrived in.
- The contradiction about asking before creating things in Drive is settled: the index Sheet is part of setup, anything else in Drive is asked about first.
- The calendar offer and the reply when the owner wants no routines are now scripted word for word.

Renewals
- The alert fires when a date is 30 days away **or less**, so something already close when the owner sets up is not missed.
- Each document and date is flagged once: the Renewals tab records the date it was alerted, and the cell is cleared only if the date itself changes.
- The price comparison is out of the alert. It stays opt-in, offered only when the owner asks or as its own message after they answer the renew-or-cancel question.
- The end-of-search summary flags anything already 30 days or less away, since the alert routine starts off.

The index and the documents
- The date column is now "Renews or ends" and covers renewals, endings, expiries and the last day of a paid period, with rules for a document that carries several dates, for past dates and for dates a document only estimates.
- "Days left" is a formula, so it no longer goes stale between runs, and the Sheet's timezone is set to the owner's.
- A missing value is always a blank cell. "Not recorded" is gone.
- Documents behind a password, a signing service, a shared link or a provider portal are never broken into: the row is filed from the covering email, the rest stays blank, and the summary says what could not be read and offers to add it if the owner sends the file.
- Only the owner's own documents are filed. Someone else's document is left out and listed once in the summary.
- The search has starter queries and a rule to skip marketing and newsletters, so broad words don't pull in noise.

Files and tooling
- Fixed files: new layout `index-sheet-layout-v2.json`, and `folder-set.json` updated for Drive-only folders. Both pinned to the tag **`fixed-files-v2`**, with new checksums in `fixed-files/MANIFEST.md`. `index-sheet-layout.json` and the tag `fixed-files-v1` are untouched, so anything pinned there keeps working.
- `allow.txt` now allows the public raw-URL prefix and the GitHub handle inside it, so a standard private-terms run passes on the bot's own fetch URLs.
- Dead references removed from `docs/README.md` and `fixed-files/README.md`.

**`fixed-files-v2` has to exist on `main` before the bot can fetch its fixed files.** It is cut after this change is merged; until then the URLs return 404 and the skill falls back to the columns in `docs-librarian-library`.

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
