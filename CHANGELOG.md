# Changelog: grokbot-template

One entry per template version. Every entry says what changed and which lesson (LEARNINGS ID) caused it.
Versions: `v0.x` while drafting · minor bump for a new rule or file · patch bump for a wording fix.

## v0.1 · 29 Sep 2026 (draft, not yet a repo)
First version, built by Bot Studio from:
- the `grok-bot-template-pipeline` skill and Bot Studio's playbook (28–29 Sep 2026: 11 gates incl. Goal and intake, 13 intake topics, publish checklist, 25 guardrails, repo standard, templates, Andy's article);
- the Docs Librarian drafts (the worked example of INTAKE → SPEC → skeleton);
- the Nomad Pro v2 drafts (lessons N1–N10).

Added:
- `README.md`: purpose, how to start a new bot, and the rule that every lesson comes back here by PR.
- `playbook/`: quick reference, the 11 gates, intake guide, publish checklist, guardrails (1–50), repo standard, Andy's article.
- `templates/`: INTAKE (13 topics, one at a time), SPEC (goal line to approved-wording appendix), RETEST, COMPARE.
- `bot-skeleton/`: skills (getting-started, core-rules, main-job), `routines.json` (every routine `"enabled": false`), `bot.json`, `fixed-files/`, `docs/`, `listing/`, `proof/`, `samples/`, `args/`, `build.py`, `banned_scan.py`, `banned.txt`, CHANGELOG.
- `LEARNINGS.md`: Koko's 15 rules of 29 Sep 2026 (K1–K15), 10 Nomad Pro lessons (N1–N10), the 25 guardrails of 28 Sep (G1–G25), and the Nomad Pro-only list.

Changed from the playbook it was copied from:
- Routines: "on by default where Koko agreed" → start OFF, switched on only with the user's yes (K1). `build.py` now fails any routine that isn't `"enabled": false` and adds "Starts off" to each routine's packed text.
- Data Sheet: "outputs name source rows" and Row ID columns → human-first Sheet, no ID codes or source rows, one data tab with a period column, summary dropdown (K5). Screenshot mock-up before any layout change (K6).
- New checklist items: C7, D8–D10, E9 (rewritten), F2, F3, F5, J3, K2, L5, L6.
- Repo layout: `bot/` folder (from `bot-skeleton/`) with `fixed-files/` and `proof/`; `playbook/` and `templates/` travel with each bot.
- Merging: Koko merges (K11).

Open questions for Koko:
1. Nomad Pro still has routines on by default, row numbers in chat ("Rows 905–908", which you asked for on 29 Sep), greyed "Bot ref" ID columns and a "Source rows"-style trail. Do the new rules (K1, K5) apply to Nomad Pro too, or only to new bots?
2. Fixed files "install on import", but a bot installed on someone else's account can't read a private repo. Per bot: written out by a skill, or fetched from a public code-only location?
3. Can the share format carry a routine as switched off? Unverified. For now each routine's text says it starts off, and getting-started switches it on only after a yes.
4. Can Bot Studio merge after your yes in chat? Still undecided; until then you merge.
