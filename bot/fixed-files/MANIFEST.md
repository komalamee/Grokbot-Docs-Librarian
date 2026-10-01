# Fixed files manifest: The Librarian

This repository is public, so the files below are fetched at setup rather than embedded in a skill. Each URL is pinned to the tag `fixed-files-v6`, never to a branch, so an install always gets the exact bytes that were tested, and the checksums here let anyone confirm it. These tags are separate from the bot's release tags (`v0.1.0` and later), so the fixed files and the marketplace version move independently.

**If a file can't be fetched or its checksum doesn't match**, the skill says so in one line and falls back: the columns written out in `docs-librarian-library` in place of the layout, and `rg` over the reading store in place of the tool.

None of these files holds personal data. The skill asks the owner before it creates anything, apart from the index Sheet itself and its own private reading store, which are part of setup.

| File | What it is | Installed where | By which skill, when |
|---|---|---|---|
| `index-sheet-layout-v2.json` | The index Sheet: name, two tabs, headers, order, date rules and date format | The owner's Google Sheet | `docs-librarian-getting-started`, before the first search |
| `folder-set.json` | The folder set: policies, receipts and payments, deadlines | Where the owner chose to copy files: their Google Drive, a folder on their own computer, or another service they connected. Never when they leave files in email | `docs-librarian-getting-started`, during setup |
| `librarian.py` | The reading store: extracts a document's text, indexes it for search (SQLite FTS5, BM25), and checks a quote against the text | `~/.docs-librarian/` on the computer the bot runs on, never the owner's Drive | `docs-librarian-getting-started`, during setup; used at every filing and every question |

## Pinned URLs and checksums (tag `fixed-files-v6`)

| File | URL | SHA-256 |
|---|---|---|
| `index-sheet-layout-v2.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v6/bot/fixed-files/index-sheet-layout-v2.json` | `ac6dd3dab56c3322ca3330196aaf470b2491a5c79504dcb471d10c1f042bb3f6` |
| `folder-set.json` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v6/bot/fixed-files/folder-set.json` | `dcc7d83ed5e033e69706c50f1c52f0af111d07b44f6fb83b5304e46a199d0588` |
| `librarian.py` | `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/fixed-files-v6/bot/fixed-files/librarian.py` | `3942a36731a956084826d4d8db7113eecf32ac735b0738f98bdd51f60acc42d2` |

Check a file with `sha256sum <file>` (or `shasum -a 256 <file>`) and compare it with the line above. **`librarian.py` is checked before it is run**: the setup skill fetches this manifest at the same tag, compares the value, and falls back to `rg` over the reading store rather than running a file that doesn't match.

## The earlier versions

Nothing from an earlier tag was moved or deleted, so anything already pinned keeps working.

* `fixed-files-v1` serves `index-sheet-layout.json` (`c0b80212165376444f781190afd179874fb87c73ad805a5468a2586bc06a5540`) and the first `folder-set.json`.
* `fixed-files-v2` serves the layout and folder set as they were on commit `7e7fd80`.
* `fixed-files-v3` serves the same layout and folder set as v2, plus the first `librarian.py`.
* `fixed-files-v4` serves the same layout and folder set, plus `librarian.py` v0.2.1 (`6087dc55b5143b414a4793c4b862fdd61b252254098bcac370bed38080bc18ac`).
* `fixed-files-v5` serves the layout (`dcf1fe97a4162dd6e21b501342e2642ce41800cad2ce05b35ad36998a9ba186d`), the folder set (`9599881a8c094fcf945a8bfd0020e832b5996fb4ebff328b867c9592e055aca0`) and `librarian.py` v0.2.2 (`3860317d613e65e5414ed9e417fcd246c452bb9d91bf8f51e17d52df96329912`), all under the bot's earlier name.

What changed in v4: `librarian.py` fixes verify (whole normalised text, page where the quote starts), metadata on re-index, case-insensitive types stored lowercase, text normalisation before index and verify, compact `catalog` by default with `--json`, and character counts that include whitespace. The layout and folder set are unchanged from v3.

What changed in v5: `librarian.py` indexes each page (or part) as its own passages again, so `find` reports pages; `verify` accepts a real hyphen that falls at a line end ("third-/party") as well as a word split by one ("reimburse-/ment"); re-adding a document without `--card` keeps its saved card indexed; database connections are closed. The layout and folder set are unchanged.

What changed in v6: wording only, for the rename to The Librarian and the four storage choices. The layout names the Sheet "The Librarian – Index" and its File link description covers a copy in another service and a path on the owner's computer (version 0.3). The folder set's root folder is "The Librarian" and its description names all four places (version 0.3). `librarian.py` changes only its opening comment and help text, so it behaves exactly as in v5. Tabs, columns, headers, formats and the folders themselves are unchanged.

## When one of these files changes
1. Edit the file and rerun the checksum.
2. Update the checksum here, and the version inside the file.
3. Cut the next tag in the series (`fixed-files-v7`, and so on), and change the tag in every URL here and in `docs-librarian-getting-started`.
4. Tell existing owners before their setup starts using the new one. An install never follows a branch, so nothing changes under a live user until the skill points at the new tag.
