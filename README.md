# Grokbot-Docs-Librarian

**Docs Librarian** — a library for your contracts, policies and any long document you might need to look back at. It files them straight from your email, keeps them organised, tracks your renewals, and gives you an instant answer to anything you ask about them.

Live link: not published yet · Current version: none (written, not tested yet)

Public repo. It holds the bot's own files and nothing else; the working notes behind the bot are kept privately by the owner. Built from the master template grokbot-template v0.1, with the upgraded rules in v0.2.

| Folder / file | What |
|---|---|
| `bot/` | The bot: skills, routines, connections, fixed files, listing, docs, proof, build and scan scripts |

## Where things are
- The three routines, all switched off: `bot/routines.json`.
- Profile, connections and memories: `bot/bot.json`.
- Skills: `bot/skills/` — `docs-librarian-getting-started`, `-core-rules`, `-library` and `-renewals`.
- Fixed files: `bot/fixed-files/` — the index Sheet layout and the folder set, fetched at setup from this public repo, pinned to the tag `fixed-files-v2`, with their checksums in `bot/fixed-files/MANIFEST.md`.

## Build and scan
From `bot/`:

```bash
python3 build.py --allow allow.txt --private-terms ../private-terms.txt
python3 banned_scan.py skills listing args --banned banned.txt --private-terms ../private-terms.txt
```

`private-terms.txt` holds the owner's real names, handles and places. It never gets committed: keep it outside the checkout, or at the repo root, where `.gitignore` covers it. `bot/private-terms.example.txt` shows the shape.

## Tags
- `fixed-files-v2` — what the bot fetches its fixed files from. Pinned so an install always gets the exact bytes that were tested. Cut once the current change is merged; `fixed-files-v1` stays where it is for anything pinned to it.
- `v0.1.0` and later — the published releases, one tag per marketplace version.

## Never
Nothing is published, posted, shared outside or merged without the owner saying yes to that exact thing. The owner merges, and the owner presses Publish.
