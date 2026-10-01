# Changelog: The Librarian

One entry per version. Repo tag = marketplace card version. Add the listing URL once the bot is published.

## v0.2.4 (not published) · 1 Oct 2026
The bot is renamed The Librarian, setup offers four storage choices instead of two, and the description loses "instant". This folds in v0.2.3, which was never merged.

The rename
- Every name a user sees is now **The Librarian**: the profile, the memories, the skill descriptions and text ("Hi, I'm The Librarian…", "You are **The Librarian**"), the routine names, the listing, the READMEs and the website handoff. The index Sheet is now "The Librarian – Index".
- Unchanged: the skill and routine slugs (`docs-librarian-*`), the repository name, the reading store `~/.docs-librarian`, fixed-file paths and URLs, and code identifiers.
- The fixed files carry the new name too: the layout's Sheet name, the folder set's root folder and the tool's help text (see below).
- `banned.txt` now lists the old name, so `banned_scan.py` fails if it comes back into the visible text.

Four storage choices
- **Message 1** now offers: leave files in email, copy them to Google Drive, save them to a folder on the owner's own computer, or somewhere else they name. Still one question.
- **Email and Drive** work as before. The email line "Nothing was copied to your Drive. I keep a private text copy on my own computer so answers are quick." is unchanged and used for the email choice only.
- **A folder on their computer.** The bot lists the owner's registered computers (one line and the other choices if none is connected), asks which one and which folder, checks the folder exists, and asks before creating it or the folder set inside it. Each save goes through their computer and asks for their approval there, which setup says in one line. The File link holds the path on their computer as plain text, then the link to the message.
- **Somewhere else.** The bot searches the plugin marketplace for that service each time. If its connection can save files, it offers once to connect it and files there the same way as Drive; if not, it says so in one line and offers the other three. No service is hard-coded and no plugin is added to the bundle.
- Every choice keeps the reading store in `~/.docs-librarian`, the index Sheet as the master record, and never overwriting or deleting without asking. Core rules, the library skill, the inbox-check routine, the storage memory line and the listing's connections section say so.

Description
- "gives you an instant answer to anything you ask about them" is now "answers anything you ask about them", in the profile and the root README, and the opening line of the core rules matches it ("answer anything they ask about them").

Fixed files and build
- Pinned tag moves to **`fixed-files-v6`**, cut on the merge commit. Wording only: `index-sheet-layout-v2.json` (0.3) names the Sheet "The Librarian – Index" and its File link description covers all four places; `folder-set.json` (0.3) has the root folder "The Librarian" and a description naming all four places; `librarian.py` changes only its opening comment and help text. Tabs, columns, folders and the tool's behaviour are unchanged. New checksums in `fixed-files/MANIFEST.md`, URLs in `docs-librarian-getting-started`, and `allow.txt` adds the v6 URL prefix. `index-sheet-layout.json` (v1) is left as it is for installs pinned to `fixed-files-v1`.
- Args rebuilt with `build.py --allow allow.txt`; `banned_scan.py` clean. All routines stay `"enabled": false`.

## v0.2.2 (not published) · 30 Sep 2026
Three fixes in `fixed-files/librarian.py` (standard library only), each with a unit test that fails on v0.2.1.

- **Pages are back in search.** v0.2.1 collapsed every line and page break before splitting a document into passages, so each document became one passage called "part 1". Passages are now cut from the lightly normalised text (page breaks and lines kept) and each passage is normalised on its own, so `find` reports "page N" again.
- **`verify` accepts a real hyphen at a line end.** A quote now matches if either the hyphen-dropped form ("reimburse-/ment" = "reimbursement") or the hyphen-kept form ("third-/party" = "third-party") is in the text.
- **Re-adding without `--card` keeps the card indexed.** The saved `cards/<id>.md` is loaded and indexed again, instead of dropping out of search until `rebuild`.
- Database connections are closed after every command (no more ResourceWarnings in the tests).

Fixed files and build
- Pinned tag moves to **`fixed-files-v5`** (new `librarian.py` checksum in `fixed-files/MANIFEST.md` and URLs in `docs-librarian-getting-started`; layout and folder set unchanged). `allow.txt` adds the v5 URL prefix. The manifest's stale "until then the URLs return 404" note is gone.
- Args rebuilt with `build.py --allow allow.txt`; `banned_scan.py` clean. All routines stay `"enabled": false`.

## v0.2.1 (not published) · 30 Sep 2026
Six fixes in `fixed-files/librarian.py` (standard library only), with a unit test for each.

The tool
- **`verify`** now matches against the whole normalised document text, not a single ~900-character passage, so a real quote that crosses a passage boundary is accepted; the message still names the page (or part) where the quote starts.
- Re-running **`add`** / **`index`** on an existing id keeps catalog metadata unless a field is passed again; type no longer resets to `other` and name, provider, dates and link are not cleared on a bare refresh.
- **`--type`** on `find` and `catalog` is case-insensitive; types are stored lowercase in the catalog and index.
- Text normalisation before indexing and verifying: soft hyphens, words split across a line break with a hyphen, and collapsed whitespace.
- **`catalog`** prints one compact tab-separated line per document by default; **`--json`** keeps the old full-JSON lines.
- **`chars`** in the catalog counts every character including whitespace.

Fixed files and build
- Pinned tag moves to **`fixed-files-v4`** (`librarian.py` checksum updated in `fixed-files/MANIFEST.md`; layout and folder set unchanged). `allow.txt` adds the v4 URL prefix. The manifest no longer says the tag is uncut; it is cut after merge.
- Unit tests extended in `bot/tests/test_librarian.py`; `banned_scan.py` and `build.py` run clean. All routines stay `"enabled": false`.

## v0.2.0 (not published) · 30 Sep 2026
A new way of answering: a private reading store, a card per document and a local search, so a question costs a search instead of a re-read of everything.

The reading store
- At filing time the bot now saves each document's text to `~/.docs-librarian/` (permissions 700, on its own computer, outside any repo) and writes a card for it. The store is a cache: the owner's mail, Drive and Sheet stay the record. It is never shared, uploaded or committed, and it is deleted only when the owner asks.
- A card is two or three lines of summary in the bot's own words, then the clauses that matter as exact quotes with their section or page: excess, limits, territory, exclusions, cancellation and renewal for insurance; term, notice, auto-renewal, exit fees and price changes for a contract or utility; rent, deposit, break clause and notice for a tenancy; each benefit with its limit and conditions for a card policy. Every quote is checked against the document's text before the card is saved, and one that doesn't match is dropped rather than reworded.
- `catalog.jsonl` carries one line per document — name, type, provider, dates, file link — keyed by the Gmail message id plus the attachment name from the File link. The Sheet keeps no ids and its layout is unchanged.
- The catalog is checked against the Sheet's Name and File link columns once a day, and as soon as the owner says they edited the Sheet. Their edits win.

Answering
- Date questions are answered from the Renewals tab, "what do I have" questions from the catalog, and everything else by searching the store: about eight ranked passages and card lines, then only the matching section of the text is opened, every quote is verified against that text, and the answer carries the link. "Across all my X" uses the type filter so no document of that type is quietly missed.
- Before saying a document doesn't cover something, the bot now opens that document's cover and exclusions sections, and reads the whole text if it is still unsure.
- A new rule: a quote comes only from verified document text. A card summary is the bot's own words and is never quoted as the document's.

The tool
- `fixed-files/librarian.py`: standard library only, with `add`/`index`, `find`, `verify`, `catalog` and `rebuild`. It extracts text with `pdftotext` or from a `.docx`, indexes passages in SQLite FTS5 ranked with BM25, and checks a quote word for word. A PDF with no text layer is marked, not indexed, and the bot reads that document directly. If the tool can't be fetched or run, the bot falls back to `rg` over the store.
- Unit tests in `bot/tests/test_librarian.py` cover adding, finding, the type filter, a made-up quote being caught, a scanned PDF with no text, a `.docx`, and rebuilding. The tool was also run against public policy PDFs.
- Fixed files move to the tag **`fixed-files-v3`**, which adds `librarian.py` with its checksum in `fixed-files/MANIFEST.md`; the setup skill checks that checksum before running it. The layout's timezone rule now says to ask the owner to set the spreadsheet timezone, which was the wording left over from v0.1.2. Tabs, columns, headers and formats are untouched, so an index built under v2 needs no change.
- `allow.txt` gains the v3 URL prefix, and `.gitignore` guards against a reading store ever being committed.

Elsewhere
- Setup creates the store, fetches the tool and says what "start again" does to it; the line for owners who keep files in email now reads "Nothing was copied to your Drive. I keep a private text copy on my own computer so answers are quick."
- The inbox-check routine saves the text copy and card along with the row. All three routines stay `"enabled": false`.
- A price comparison matches the card's clauses and then verifies them in the text; a renewal notice adds a dated line to the card's history.
- `listing/LISTING.md` carries the owner's approved "What it does" wording, and says in the connections section that the bot keeps a private text copy and what it can't read.
- `samples/card-example.md` shows the card format with invented content.

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
