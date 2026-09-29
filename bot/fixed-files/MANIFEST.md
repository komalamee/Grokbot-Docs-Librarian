# Fixed files manifest: Docs Librarian

This repository is public, so both files below are fetched at setup from `raw.githubusercontent.com` on `main`. Nothing is embedded in a skill and nothing here holds personal data. The skill asks the owner before it creates anything.

| File | What it is | Installed where | By which skill, when | How it reaches the user |
|---|---|---|---|---|
| `index-sheet-layout.json` | The index Sheet: name, two tabs, headers, order and date format (SPEC §5) | The owner's Google Sheet | `docs-librarian-getting-started`, right after message 2 and before any search | Fetched from `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/main/bot/fixed-files/index-sheet-layout.json` |
| `folder-set.json` | The folder set: policies, receipts and payments, deadlines (SPEC §4) | The owner's chosen storage: their computer or Drive | `docs-librarian-getting-started`, during setup | Fetched from `https://raw.githubusercontent.com/komalamee/Grokbot-Docs-Librarian/main/bot/fixed-files/folder-set.json` |

If a fetch fails, the skill says so in one line and falls back to the columns written out in `docs-librarian-library`.
