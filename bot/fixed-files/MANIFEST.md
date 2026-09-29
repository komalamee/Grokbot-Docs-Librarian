# Fixed files manifest: Docs Librarian

This repository is public, so both files below are fetched at setup rather than embedded in a skill. Each URL is pinned to the tag `fixed-files-v1`, never to a branch, so an install always gets the exact bytes that were tested, and the checksum below lets anyone confirm it. The tag is separate from the bot's release tags (`v0.1.0` and later), so the fixed files and the marketplace version move independently.

Neither file holds personal data. The skill asks the owner before it creates anything.

| File | What it is | Installed where | By which skill, when |
|---|---|---|---|
| `index-sheet-layout.json` | The index Sheet: name, two tabs, headers, order and date format | The owner's Google Sheet | `docs-librarian-getting-started`, right after message 2 and before any search |
| `folder-set.json` | The folder set: policies, receipts and payments, deadlines | The owner's chosen storage: their computer or Drive | `docs-librarian-getting-started`, during setup |

## Pinned URLs and checksums (tag `fixed-files-v1`)

| File | URL | SHA-256 |
|---|---|---|
| `index-sheet-layout.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v1/bot/fixed-files/index-sheet-layout.json` | `c0b80212165376444f781190afd179874fb87c73ad805a5468a2586bc06a5540` |
| `folder-set.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v1/bot/fixed-files/folder-set.json` | `f8d83eb14b39354594023d783e1b5262630165de6421700f152cfa57a6bfe455` |

Check a file with `sha256sum <file>` (or `shasum -a 256 <file>`) and compare it with the line above.

## When one of these files changes
1. Edit the file and rerun the checksum.
2. Update the checksum here, and the version inside the file.
3. Cut the next tag in the series (`fixed-files-v2`, and so on), and change the tag in both URLs here and in `docs-librarian-getting-started`.
4. Tell existing owners before their setup starts using the new one. An install never follows a branch, so nothing changes under a live user until the skill points at the new tag.

If a fetch fails, the skill says so in one line and falls back to the columns written out in `docs-librarian-library`.
