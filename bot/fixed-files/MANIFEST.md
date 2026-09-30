# Fixed files manifest: Docs Librarian

This repository is public, so both files below are fetched at setup rather than embedded in a skill. Each URL is pinned to the tag `fixed-files-v2`, never to a branch, so an install always gets the exact bytes that were tested, and the checksum below lets anyone confirm it. The tag is separate from the bot's release tags (`v0.1.0` and later), so the fixed files and the marketplace version move independently.

**`fixed-files-v2` does not exist yet.** It is cut once this change is merged. Until then the URLs return 404 and the skill falls back to the columns written out in `docs-librarian-library`.

Neither file holds personal data. The skill asks the owner before it creates anything, apart from the index Sheet itself, which is part of setup.

| File | What it is | Installed where | By which skill, when |
|---|---|---|---|
| `index-sheet-layout-v2.json` | The index Sheet: name, two tabs, headers, order, date rules and date format | The owner's Google Sheet | `docs-librarian-getting-started`, before the first search |
| `folder-set.json` | The folder set: policies, receipts and payments, deadlines | The owner's Google Drive, only when they choose to copy files there | `docs-librarian-getting-started`, during setup |

## Pinned URLs and checksums (tag `fixed-files-v2`)

| File | URL | SHA-256 |
|---|---|---|
| `index-sheet-layout-v2.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v2/bot/fixed-files/index-sheet-layout-v2.json` | `34f4149ceb50c7fc41cec93badb3ec61e9ec237eaafb2b971eccbda4d5cad75b` |
| `folder-set.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v2/bot/fixed-files/folder-set.json` | `9599881a8c094fcf945a8bfd0020e832b5996fb4ebff328b867c9592e055aca0` |

Check a file with `sha256sum <file>` (or `shasum -a 256 <file>`) and compare it with the line above.

## The earlier version

`index-sheet-layout.json` is the v1 layout and is left exactly as it was, checksum `c0b80212165376444f781190afd179874fb87c73ad805a5468a2586bc06a5540`. The tag `fixed-files-v1` still points at the old commit and still serves both v1 files, so anything already pinned there keeps working. Nothing about v1 was moved or deleted.

What changed in v2: the date column is now "Renews or ends" and covers endings, expiries and paid-up-to dates, with rules for a document that carries several dates; "Days left" is a formula rather than a number that goes stale; the Renewals tab has an "Alerted" column so a date is flagged once; a missing value is always a blank cell; and the folder set is Drive-only, since files can also simply stay in the owner's email.

## When one of these files changes
1. Edit the file and rerun the checksum.
2. Update the checksum here, and the version inside the file.
3. Cut the next tag in the series (`fixed-files-v3`, and so on), and change the tag in both URLs here and in `docs-librarian-getting-started`.
4. Tell existing owners before their setup starts using the new one. An install never follows a branch, so nothing changes under a live user until the skill points at the new tag.

If a fetch fails, the skill says so in one line and falls back to the columns written out in `docs-librarian-library`.
