# Grokbot-Docs-Librarian

**Docs Librarian** — a library for your contracts, policies and any long document you might need to look back at. It files them straight from your email, keeps them organised, tracks your renewals, and gives you an instant answer to anything you ask about them.

Live link: not published yet · Current version: none · Status: gate ④ (skills, routines and fixed files written from the spec; not tested yet).

Public repo, made from `grokbot-template` v0.1 (see `CHANGELOG.md` and `LEARNINGS.md`, which travel with the bot and record the rules it was built under).

| Folder / file | What |
|---|---|
| `bot/` | The bot itself (was `bot-skeleton/`): skills, routines, connections, docs, listing, proof, build and scan scripts |
| `playbook/` | The 11 gates, intake guide, publish checklist, guardrails, repo standard — the version of the rules this bot is built with |
| `templates/` | The fill-in documents: INTAKE, SPEC, RETEST, COMPARE |
| `LEARNINGS.md` · `CHANGELOG.md` | The master template's files. Lessons go back upstream by PR |
| `TEMPLATE-FEEDBACK.md` | What was unclear, wrong or missing in `grokbot-template` v0.1 while setting this repo up |

## Where things are
- Approved intake and spec: `bot/docs/INTAKE.md`, `bot/docs/SPEC.md` (unchanged wording; approved first messages and example chats are in SPEC Appendix A).
- The three routines, all switched off: `bot/routines.json`.
- Profile, connections and memories: `bot/bot.json`.
- Skills: `bot/skills/` — `docs-librarian-getting-started`, `-core-rules`, `-library` and `-renewals`, all written from the spec.
- Fixed files: `bot/fixed-files/` — the index Sheet layout and the folder set, fetched at setup from this public repo (raw URLs on `main`).

## Build and scan
From `bot/`:

```bash
python3 build.py --allow allow.txt --private-terms ../private-terms.txt
python3 banned_scan.py skills listing args --banned banned.txt --private-terms ../private-terms.txt
```

`private-terms.txt` holds the owner's real names, handles and places. It never gets committed: keep it outside the checkout, or at the repo root, where `.gitignore` covers it. `bot/private-terms.example.txt` shows the shape.

## Never
Publish, post, push anything public or message anyone outside without Koko's OK for that exact thing. **Koko merges the PR and Koko presses Publish.**
