# Fixed files manifest: Docs Librarian

This repository is public, so the files below are fetched at setup rather than embedded in a skill. Each URL is pinned to the tag `fixed-files-v3`, never to a branch, so an install always gets the exact bytes that were tested, and the checksums here let anyone confirm it. These tags are separate from the bot's release tags (`v0.1.0` and later), so the fixed files and the marketplace version move independently.

**`fixed-files-v3` is not cut yet.** It is created once the change that carries it is merged. Until then the v3 URLs return 404, the skill says so in one line and falls back: the columns written out in `docs-librarian-library` in place of the layout, and `rg` over the reading store in place of the tool.

None of these files holds personal data. The skill asks the owner before it creates anything, apart from the index Sheet itself and its own private reading store, which are part of setup.

| File | What it is | Installed where | By which skill, when |
|---|---|---|---|
| `index-sheet-layout-v2.json` | The index Sheet: name, two tabs, headers, order, date rules and date format | The owner's Google Sheet | `docs-librarian-getting-started`, before the first search |
| `folder-set.json` | The folder set: policies, receipts and payments, deadlines | The owner's Google Drive, only when they choose to copy files there | `docs-librarian-getting-started`, during setup |
| `librarian.py` | The reading store: extracts a document's text, indexes it for search (SQLite FTS5, BM25), and checks a quote against the text | `~/.docs-librarian/` on the computer the bot runs on, never the owner's Drive | `docs-librarian-getting-started`, during setup; used at every filing and every question |

## Pinned URLs and checksums (tag `fixed-files-v3`)

| File | URL | SHA-256 |
|---|---|---|
| `index-sheet-layout-v2.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v3/bot/fixed-files/index-sheet-layout-v2.json` | `dcf1fe97a4162dd6e21b501342e2642ce41800cad2ce05b35ad36998a9ba186d` |
| `folder-set.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v3/bot/fixed-files/folder-set.json` | `9599881a8c094fcf945a8bfd0020e832b5996fb4ebff328b867c9592e055aca0` |
| `librarian.py` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v3/bot/fixed-files/librarian.py` | `f788a49467ae3f0f733b92a6ec194b2ffb22f188818163e7fd53182c69498320` |

Check a file with `sha256sum <file>` (or `shasum -a 256 <file>`) and compare it with the line above. **`librarian.py` is checked before it is run**: the setup skill fetches this manifest at the same tag, compares the value, and falls back to `rg` over the reading store rather than running a file that doesn't match.

## The earlier versions

Nothing from an earlier tag was moved or deleted, so anything already pinned keeps working.

* `fixed-files-v1` serves `index-sheet-layout.json` (`c0b80212165376444f781190afd179874fb87c73ad805a5468a2586bc06a5540`) and the first `folder-set.json`.
* `fixed-files-v2` serves the layout and folder set as they were on commit `7e7fd80`.

What changed in v3: `librarian.py` is new, and the layout's timezone rule now says to ask the owner to set the spreadsheet's timezone, because the bot has no way to set it. The tabs, columns, headers and formats are exactly as they were in v2, so an index built under v2 needs no change.

## When one of these files changes
1. Edit the file and rerun the checksum.
2. Update the checksum here, and the version inside the file.
3. Cut the next tag in the series (`fixed-files-v4`, and so on), and change the tag in every URL here and in `docs-librarian-getting-started`.
4. Tell existing owners before their setup starts using the new one. An install never follows a branch, so nothing changes under a live user until the skill points at the new tag.
