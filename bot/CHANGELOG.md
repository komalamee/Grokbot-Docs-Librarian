# Changelog: Docs Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL once the bot is published.

## v0.1.2 (not published) · 30 Sep 2026
Ten fixes from the clean-agent retest of v0.1.1. Wording and tooling only; the fixed files are unchanged, so the tag `fixed-files-v2` still serves them.

The bot
- Setup now asks the owner to set the index Sheet's timezone by hand, in its own message, because no connector tool can set it. Until they do, nothing depends on the "Days left" cell: the bot works out how far away a date is from today's date in the owner's timezone, and the cell is there for the owner to read.
- A renewal alert says "ends on" for a cover period, a fixed term, an expiry or the last day paid for, and "renews on" only where the document itself says it renews. Both lines are scripted.
- An answer that rests on more than one document quotes and links each of them, rather than one link standing in for several.
- Filing rules for the cases that come up in every inbox: something already ended (file it only if it carries terms), a rolling plan with no end date (file it, date blank), the same document arriving twice (file it once), a blank template or unsigned draft (file it, marked in the Name), a document held through the owner's own company (file it, company named), and a shared link whose parties can't be seen (filed as one that couldn't be read).
- The first starter search query excludes receipts, invoices, orders, bookings and itineraries, and asks for a PDF or Word attachment, so it stops dragging in noise.
- The message 2 example uses the index's own types instead of "receipts", which was never one.
- Core rules say a banned word may appear only inside a verbatim quote from a document.

Tooling
- `allow.txt` no longer carries a bare handle, which was hiding any email address that started with it. It now holds only the exact pinned raw-URL prefixes and the repository URL.
- `banned_scan.py` applies `--allow` to private-data hits as well as banned phrases, with the same literal, exact-match semantics, so the bot's own public fetch URLs stop showing up as leaks. Its scope is documented: it reads the bot's own wording, not text the bot quotes back from a document.
- `MANIFEST.md`, the changelog and the repo README no longer say the `fixed-files-v2` tag is still to be cut. It is live on commit `7e7fd80`.

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

The tag `fixed-files-v2` went live on commit `7e7fd80` once this change was merged, and both pinned URLs serve the files.

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
