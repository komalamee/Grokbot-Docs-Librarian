# Quick reference

Version 0.1 (29 Sep 2026). Adapted from the `grok-bot-template-pipeline` skill. Detail lives in the other playbook files.

## The two things that matter most
1. **A clear goal.** One line: who the bot is for and the one outcome. Nothing is built until Koko agrees it.
2. **A thorough intake with Koko.** One topic per message, before any spec. Never fill gaps with my own guesses or copy another bot's choices (Nomad Pro included) without asking.

## Never
- Publish, post, push public, or message anyone outside without Koko's OK for that exact thing. **Koko presses Publish. Koko merges.**
- Delete a bot with a live listing. Retire the listing first; archive, don't delete.
- Hand-edit the args or swap text at build time.
- Switch a routine on by default. Routines start OFF; the user says yes to each.
- Send an email for a user. The user presses Send.
- State a fact, place, date or status the user hasn't given. Embellish first-person copy.
- Carry over Nomad Pro's disclaimers, "records, not verdicts" wording or advice limits by default.

## Roles
Koko approves each gate, merges, checks the staged card and presses Publish. Bot Studio builds. Brandy P does social after Koko's OK. Website: Chief for Nomad Pro; every other bot gets a handoff doc that Koko passes to Hermes.

## Gates
Idea → Goal and intake → Spec → Build → Test → Package → Pre-publish check → Publish → Post-launch → Learn → Retire/replace. Max 2 bots in Build. Each gate needs Koko's OK.

## Build steps (short)
1. Make a **private** repo `grokbot-<bot>` from this template (Koko's OK). Rename `bot-skeleton/` → `bot/` and `mybot` → the bot's name.
2. `docs/INTAKE.md` (confirmed) → `docs/SPEC.md`.
3. Create the source bot; **set avatar shape and colour first** (not white).
4. Skills: `<bot>-getting-started`, `<bot>-core-rules`, one job skill. Prefix every slug and description with the bot name.
5. `routines.json`: the only source for routine slugs, schedules, cron, quiet rule and needs. Every routine `"enabled": false`.
6. `bot.json`: profile, plugins (`pluginId` digit strings), general memories, gettingStarted.
7. `fixed-files/` + setup steps inside the bot for anything that won't transfer.
8. Sheet: screenshot mock-up with fake data → Koko's OK → build.
9. Copy to the live skills folder only from the repo; back up the live copy first.
10. Clean-agent retest → `docs/RETEST.md` + evidence in `proof/`.
11. `python3 build.py --check-live <live dir> --private-terms <outside file>` then `python3 banned_scan.py skills listing args --banned banned.txt`.
12. Republish: like-for-like comparison. PR → Koko merges → stage from inside the source bot → Koko checks the card → **Koko presses Publish** → check the link → tag + CHANGELOG → launch pack to Brandy P → website handoff.
13. Lessons → `grokbot-template` by PR.

## Published slugs never change
List them in `bot.json` `legacy_routine_slugs` (e.g. Nomad Pro's `calendar-review`).
