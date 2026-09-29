# Publish checklist: hard go / no-go

Version 0.1 (29 Sep 2026). Adapted from Bot Studio's checklist (28 Sep 2026, updated 29 Sep 2026) with Koko's 29 Sep rules added (marked **new**).
**Every box ticked = GO. Any box empty = NO-GO.** Who ticks: **BS** Bot Studio, **K** Koko. Section N comes from Andy's article.
Copy this file into the bot's PR description or `docs/` for each release.

Bot: ________ · Version: v____ · Date (ICT): ________

## A. Goal and intake (before the spec)
- [ ] **A1** Goal line agreed with Koko: who it's for and the one outcome. · K
- [ ] **A2** `docs/INTAKE.md` in Koko's words, open points marked, confirmed by Koko. · K
- [ ] **A3** Every choice in `docs/SPEC.md` traces to `docs/INTAKE.md`, or is marked as my suggestion and approved. · BS

## B. Clear outcome
- [ ] **B1** One job in one line (≤ 15 words), identical in SPEC and listing. · BS
- [ ] **B2** First result is measurable: "by message N the user sees X" (N ≤ 2). · BS
- [ ] **B3** Clean-agent retest reaches that first result from "hi" by message 2. · BS
- [ ] **B4** No second job: off-scope asks get one polite line. · BS

## C. Clear onboarding
- [ ] **C1** `<bot>-getting-started` exists, is set as `gettingStarted`, and follows the onboarding in `docs/INTAKE.md`. · BS
- [ ] **C2** Message 1 is ≤ 2 lines, short and correct: who it is + one question. · BS
- [ ] **C3** Useful result by message 2; other setup later, in chunks, only when needed. · BS
- [ ] **C4** Connections offered once, with or after the first result; each can be declined; the bot still works without them. · BS
- [ ] **C5** One question per message; "skip" works. · BS
- [ ] **C6** Data Sheet created (or offered) at the first result, with one line and its link. · BS
- [ ] **C7 new** The routines message is short and correct: names each routine and its time, says each run uses tokens, asks which to switch on. · BS

## D. Clear rules
- [ ] **D1** `<bot>-core-rules` exists; other skills point to it. · BS
- [ ] **D2** Scope: says what it does and doesn't do. · BS
- [ ] **D3** Disclaimer only if the bot's own subject needs one and Koko agreed in intake; then word for word, at most one per message. Otherwise none. · BS
- [ ] **D4** Banned words in core rules (inside `banned-list` markers) and in `banned.txt`. · BS
- [ ] **D5** Read-only by default; any write access is named and explained. · BS
- [ ] **D6** Never sends, posts, shares, books or deletes unless the owner asks for that exact action. · BS
- [ ] **D7** Email, calendar, file and web content is data, never instructions. · BS
- [ ] **D8 new** Never states a fact, place, date or status the user hasn't given. Unknown stays unknown (blank or "Not recorded"). · BS
- [ ] **D9 new** Never sends an email: it can draft, the user presses Send. · BS
- [ ] **D10 new** Replies answer first, then at most a short line on how; plain words. · BS

## E. Very specific routines
- [ ] **E1** Each routine has: name, slug, exact schedule in the **owner's** timezone, trigger, job, quiet rule, connection needed. · BS
- [ ] **E2** Cron minute matches the words (no "18:00" text with an 18:05 cron), and the test run shows it fired at the agreed minute. · BS
- [ ] **E3** Quiet when nothing changed: no "no changes" messages, first run silent, ≤ 1 message per run, no chasers. · BS
- [ ] **E4** A routine that needs a connection checks it and stays silent without it. · BS
- [ ] **E5** Routines are offered **after the first result**, in the owner's timezone (never Koko's). · BS
- [ ] **E6** Never duplicated: setup updates by slug, never adds a second copy. · BS
- [ ] **E7** Slugs identical in `routines.json`, getting-started and args (build check). · BS
- [ ] **E8** "stop", "pause" and "change time" work. · BS
- [ ] **E9 new** Every routine starts OFF (`"enabled": false`). The bot asks during setup which to switch on and switches each on only after the user says yes to it. · BS

## F. The data Sheet (user-owned, human-first)
- [ ] **F1** One editable Google Sheet is the single master record, in the owner's Drive, never shared. · BS
- [ ] **F2 new** Designed for a human to read first: a clean summary on top with a period dropdown; **one** filterable data tab, one line per item, with a period column (no tabs per year); proper formatting, column widths, frozen headers, filter; dates like "28 Sep 2026"; no record-ID codes and no "source rows" anywhere; no backup tabs; no private file paths. · BS
- [ ] **F3 new** Koko approved a screenshot mock-up (fake data) of the layout before it was built. Any later layout change: new mock-up first, plus a one-time layout update step for existing users. · K
- [ ] **F4** Bot writes to the Sheet first and reads it before every run; owner edits win; bad rows flagged in one line, never guessed. · BS
- [ ] **F5 new** Outputs say where they came from in plain words (Sheet name and period, e.g. "From your Index, Jan–Sep 2026"), never row IDs. · BS
- [ ] **F6** Fallback when Sheets isn't connected is defined (e.g. CSV + one offer). · BS

## G. Connections parity
- [ ] **G1** Every plugin any skill or routine mentions is listed (grep the skills). · BS
- [ ] **G2** Every listed plugin is **packed**. "Optional in skills" still means pack it. · BS
- [ ] **G3** Each checked with **GetPlugin**: installed on the account. · BS
- [ ] **G4** Key is `pluginId`, value a **string** ("45893414"); no `plugin_id`. · BS
- [ ] **G5** Each plugin description says access level and use in one line. · BS

## H. Package
- [ ] **H1** Args built by `build.py` from the repo skills; no hand edits, no build-time text swaps. · BS
- [ ] **H2** Args ≤ **92,000 bytes** (host limit sits between ~98 KB and ~103 KB). · BS
- [ ] **H3** Private-data scan = **0** (names, emails, paths, agent IDs, owner's city/timezone, tokens). · BS
- [ ] **H4** Banned-phrase scan = **0** on skills + listing + args. · BS
- [ ] **H5** Live skills == args bodies (`build.py --check-live`), 0 diffs. · BS
- [ ] **H6** Nothing owner-specific baked in ("21:00 your time", "you/the owner"; no names or pronouns). · BS
- [ ] **H7** Slugs prefixed with the bot name; descriptions start "<Bot> <job>:". · BS
- [ ] **H8** Only this bot's skills packed. · BS
- [ ] **H9** Memories: general job facts only; none of Koko's. · BS
- [ ] **H10** Name spelled one way everywhere (hyphen vs en dash). · BS

## I. Avatar
- [ ] **I1** Avatar shape and colour set on the source bot **before** packaging (uploaded pictures don't copy). · BS
- [ ] **I2** Not white or a placeholder; readable on light and dark. · K
- [ ] **I3** Icon unchanged since staging (any change = restage). · BS

## J. Listing
- [ ] **J1** `listing/LISTING.md` complete: pitch, what it does, who it's for, what it connects, routines you can switch on, example first messages; a disclaimer line only if D3 applies. · BS
- [ ] **J2** Every claim maps to a tested behaviour; nothing the bot can't do. · BS
- [ ] **J3 new** No embellishment or invented detail in first-person copy (listing, message 1, any "I …" line). · BS
- [ ] **J4** 3–4 example first messages (templates can't carry example prompts). · BS
- [ ] **J5** Attribution "Komal Amin". · K

## K. Proof, compare and test
- [ ] **K1** Clean-agent retest done after the last change: "hi", main job, off-scope, routines question, each routine incl. quiet case, no connections. `docs/RETEST.md` filled. · BS
- [ ] **K2 new** Proof in `proof/`: screenshots of message 1, the first result, the routines question and the Sheet; test-run evidence for each routine (fire time, message or silence). · BS
- [ ] **K3** Republish only: full like-for-like comparison against the previous version (`templates/COMPARE.md`); every difference "on purpose" or fixed; anything that couldn't be checked is said. · BS
- [ ] **K4** Koko has read the comparison, retest and proof. · K

## L. Repo
- [ ] **L1** The bot's private repo holds this exact version: skills, `routines.json`, `bot.json`, fixed files, args, listing, proof. · BS
- [ ] **L2** PR **merged by Koko before or at publish**. · K
- [ ] **L3** Version agreed; tag + CHANGELOG + listing URL added right after Publish. · BS
- [ ] **L4** Any public repo holds code only (no notes, drafts or personal data) and scans clean. · BS
- [ ] **L5 new** Fixed files install on import: tested on a clean install, and the setup step tells the user what it installs and where. · BS
- [ ] **L6 new** Lessons found while building this bot are in a PR to `grokbot-template` (`LEARNINGS.md` + the file it affects). · BS

## M. Stage and go
- [ ] **M1** Staged from inside the source bot; for an update, the bot that owns the live listing. · BS
- [ ] **M2** Koko checked the staged card: **icon** right. · K
- [ ] **M3** Koko checked the staged card: **all connections visible**. · K
- [ ] **M4** Koko said "go" in writing, and **Koko presses Publish**. · K
- [ ] **M5** Nothing sent to outsiders or posted before Koko's go. · BS
- [ ] **M6** Launch pack ready for Brandy P: link placeholder, final icon, example messages, visuals. · BS
- [ ] **M7** Website handoff ready: Nomad Pro → Chief; any other bot → handoff doc for Koko to pass to Hermes. · BS

---

## N. From Andy's article: "How to monetize your Grok Bot templates on X"
Source: Andy (@andy_ai0), 26 Sep 2026. Full text: `sources/andy-monetize-grokbot-templates.md`. Only the parts that apply to Koko.

### N1. Worth installing
- [ ] **N1.1** "Worse without it": going back to a plain Grok chat would make the workflow noticeably worse. · K
- [ ] **N1.2** Not a single prompt: real work to rebuild from scratch. · BS
- [ ] **N1.3** Uses at least 2 of: routines, connected tools, repeated context, background work, memory. · BS
- [ ] **N1.4** Solves one pain the audience feels, named in one line. · BS
- [ ] **N1.5** Built for repeat use: a reason to come back weekly. · BS

### N2. Package review
- [ ] **N2.1** Share draft reviewed line by line: instructions, memories, skills, routines, plugins. · BS
- [ ] **N2.2** No API keys, internal URLs, client data or anything confidential. · BS
- [ ] **N2.3** Setup steps inside the bot for anything that doesn't transfer (MCP servers, scripts, engines, fixed files). · BS
- [ ] **N2.4** Live link checked: `x.ai/bot/` + 21-character token, opens the right card. · K

### N3. Launch content (ready before Publish, posted only after Koko's OK)
- [ ] **N3.1** Pain point line for the posts. · Brandy P
- [ ] **N3.2** Final output shown: screen recording or result image (fake data). · BS → Brandy P
- [ ] **N3.3** Walkthrough article draft: setup, connecting each plugin, demo. · BS → Brandy P
- [ ] **N3.4** Workflow article draft. · Brandy P
- [ ] **N3.5** Listed on the Grok Bot marketplace as well as shared on X. · K

### Not applicable (rewards programme; Koko doesn't qualify)
Eligibility rules, the "paid partnership" label (don't add it), the 30-day public-post rule, reward factors, and Andy's guesses on getting an invite.
