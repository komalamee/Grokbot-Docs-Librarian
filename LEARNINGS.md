# LEARNINGS

Every rule we've learned building Grok Bots, dated, in plain English. Newest first.
**How to add one (by PR):** date · the rule in one line · why (what happened) · source · where it landed (the template file you changed in the same PR). Then add a CHANGELOG line. Koko merges.
The organised rulebook is `playbook/GUARDRAILS.md`; this file is the dated log.

---

## 29 Sep 2026: from Koko

**K1. Routines always start OFF.** During setup the bot asks which ones to switch on, and switches each on only when the user says yes. Every run burns tokens.
- Source: Koko, 29 Sep 2026 (Docs Librarian intake, 17:19 and 17:38). Backed up by Nomad Pro: a weekly HMRC re-crawl of 143 pages per user was flagged as heavy once it was on for every install (`CHANGES-2026-09-28.md`, Issues).
- Landed: `bot-skeleton/routines.json` (`"enabled": false`), `build.py` (fails otherwise), getting-started skill (Message 3), `templates/SPEC.md` §8, `templates/INTAKE.md` §8, checklist C7 + E9.

**K2. Every bot has its own private GitHub repo holding its latest version. Fixed files ship from the repo and install on import.**
- Source: Koko, 29 Sep 2026; Docs Librarian `docs/INTAKE.md` "GitHub repo (Koko)" (review the whole process end to end; fixed files installed on the user's computer on import).
- Landed: `README.md`, `playbook/REPO-STANDARD.md`, `bot-skeleton/fixed-files/`, checklist L1 + L5.

**K3. A clear one-line goal plus a thorough intake conversation with Koko is the key.** Nothing is built until Koko agrees the goal line and confirms the intake.
- Source: Koko, 29 Sep 2026; pipeline skill "The two things that matter most".
- Landed: `README.md`, `playbook/PLAYBOOK.md` gate ②, `playbook/INTAKE-GUIDE.md`, `templates/INTAKE.md`.

**K4. Disclaimers are opt-in, never default.** Nomad Pro's disclaimers and advice limits are specific to its tax and residency subject.
- Source: Koko, 29 Sep 2026. Docs Librarian agreed "no disclaimer at all" (intake update 17:46).
- Landed: `templates/SPEC.md` §11 (default none), core-rules skill §6 (optional), checklist D3.

**K5. Google Sheets are designed for a human to read first.** A clean summary with a period dropdown; one line per item; proper formatting and column widths; human-readable dates ("28 Sep 2026"); no record-ID codes or "source rows" anywhere; one filterable data tab with a period column, not a tab per year.
- Source: Koko, 29 Sep 2026. Backed up by Nomad Pro's approved Sheet layout v2: readable dates, no country codes, a Summary dropdown, "no per-year or backup tabs", filter on Tax year; older Sheets with Row IDs, codes and per-year tabs needed a layout update (`COMPARE-sheet-layout.md`; export skill "Layout").
- Landed: `templates/SPEC.md` §5, `bot-skeleton/fixed-files/sheet-layout.example.json`, core-rules skill §5, checklist F2 + F5.

**K6. Show a screenshot mock-up before changing any template Sheet layout.**
- Source: Koko, 29 Sep 2026. Nomad Pro's layout v2 was built from "the Sheet layout Koko approved on the mock-up" (`COMPARE-sheet-layout.md`).
- Landed: `playbook/PLAYBOOK.md` gate ④, `templates/SPEC.md` §5, checklist F3.

**K7. Never state facts, places, dates or statuses the user hasn't given.** Unknown stays unknown.
- Source: Koko, 29 Sep 2026. Nomad Pro rules: unknown place = "Not recorded"; a trip is "Booked" only with a booking for the stay (a flight alone = "Planned") (`COMPARE-sheet-layout.md`, export skill "Trips"). Docs Librarian: "Never guess. Never lie. Never hallucinate." (intake 17:07).
- Landed: core-rules skill §3, checklist D8.

**K8. Never embellish or invent in first-person copy** (the listing, message 1, any "I …" line).
- Source: Koko, 29 Sep 2026.
- Landed: core-rules skill §3.4, `listing/LISTING.md` check line, checklist J3.

**K9. Full like-for-like comparison against the previous version before any republish.**
- Source: Koko, 29 Sep 2026. Nomad Pro did this for each change (`V1-V2-COMPARISON.md`, `COMPARE-row-links.md`, `COMPARE-overseas-work.md`, `COMPARE-sheet-layout.md`).
- Landed: `templates/COMPARE.md`, checklist K3.

**K10. Concrete proof before any release:** screenshots and test-run evidence.
- Source: Koko, 29 Sep 2026.
- Landed: `bot-skeleton/proof/`, `templates/RETEST.md`, checklist K1 + K2.

**K11. Koko presses Publish and merges PRs.** Bot Studio does neither.
- Source: Koko, 29 Sep 2026; playbook roles.
- Landed: `playbook/PLAYBOOK.md` roles, `playbook/REPO-STANDARD.md`, checklist L2 + M4.

**K12. Messages to users answer first, short and plain.**
- Source: Koko, 29 Sep 2026. Docs Librarian (17:18): "Get to the point … answer first, followed by a brief account of the process."
- Landed: core-rules skill §1, main-job skill "Reply shape", checklist D10.

**K13. Routine crons fire at the exact agreed minute.** Nomad Pro's calendar review said "Sunday 18:00" but its cron was `5 18 * * 0`, so it ran 5 minutes late.
- Source: Koko, 29 Sep 2026; `CHANGES-2026-09-28.md` (Issues); `V1-V2-COMPARISON.md` §3.
- Landed: `build.py` (time vs cron check), checklist E2 (now also checked in the test run), `templates/RETEST.md` case e.

**K14. The first message and the routines message must be short and correct.**
- Source: Koko, 29 Sep 2026.
- Landed: getting-started skill (Message 1, Message 3), `templates/SPEC.md` Appendix A, checklist C2 + C7.

**K15. Never send email unless the user presses Send.**
- Source: Koko, 29 Sep 2026. Docs Librarian (17:07): "Never send emails on behalf of the user unless the user expressly clicks send."
- Landed: core-rules skill §4, `bot.json` memory, checklist D9.

---

## 29 Sep 2026: from the Nomad Pro v2 drafts (27–29 Sep 2026)

**N1. One figure, one label, everywhere.** Chat, Sheet, dashboard and files must show the same number against the same line.
- Why: for the same log on the same day, chat showed "20 / 46" and the dashboard "20 / 182"; the summary said "before 183" and the card "before 182".
- Source: `FIXLIST-engine.md` §1–2. Landed: `playbook/GUARDRAILS.md` 41.

**N2. Quote numbers from the tool; the bot never redoes the arithmetic.**
- Why: the bot's own 16 − 15 said "1 day of room" where the engine said 0; a heads-up said "2" where it should be 1.
- Source: `CHANGES-2026-09-28.md` (Engine v0.1.4 follow-up); `RETEST.md` (i). Landed: core-rules skill §3.3, GUARDRAILS 42.

**N3. Mock-ups, samples and examples use fictional data only.**
- Why: the engine's figure mismatches (N1) were found while making article mock-ups from a fictional log; skill examples were checked so no place, date or count from Koko's own log appears.
- Source: `FIXLIST-engine.md`; `COMPARE-sheet-layout.md` "Real-data check". Landed: `bot-skeleton/proof/README.md`, `samples/`, GUARDRAILS 43.

**N4. The data Sheet needs the Google Sheets connection with edit access.** Drive alone can't edit cells.
- Why: with only Drive, the bot had to upload a fresh copy each refresh, piling up versions, and the Sheet link changed.
- Source: `CHANGES-2026-09-28.md` ("In-place edits need a Sheets connector"; "Google Sheets as the main path"). Landed: `bot-skeleton/bot.json` plugins, `templates/SPEC.md` §9, GUARDRAILS 44.

**N5. A layout change on a live Sheet needs a one-time update step for existing users:** with their OK, back up, build the new tabs, check every cell, log one change, read back with zero changed rows.
- Source: `COMPARE-sheet-layout.md`; Nomad Pro export skill "Layout update". Landed: checklist F3, GUARDRAILS 45.

**N6. Engine or script updates reach every live install.** Pin tagged releases and tell the user before updating; never auto-pull `main`.
- Why: Nomad Pro installs self-updated weekly from `main`, so merging an engine patch would change behaviour for every live user at once.
- Source: `CHANGES.md` open question 1. Landed: `playbook/REPO-STANDARD.md`, GUARDRAILS 46.

**N7. A comparison says what it could not check.**
- Why: nobody could prove what v1 packed; the overseas-work comparison could not be checked against the live listing itself.
- Source: `V1-V2-COMPARISON.md` "Still unverified"; `COMPARE-overseas-work.md` baseline note. Landed: `templates/COMPARE.md` "Could not check", GUARDRAILS 47.

**N8. When a PR can't be opened from here, hand off the exact files with SHA-256 checksums** and apply scripts that check each change matches exactly once. The PR opens as a draft; Koko merges.
- Source: `COMPARE-row-links.md` "GitHub PR"; `pr-handoff-template-updates/CLOUD-AGENT-PROMPT.md`. Landed: `playbook/REPO-STANDARD.md`, GUARDRAILS 48.

**N9. Redo the clean-agent retest after every change round.**
- Why: after the 28 Sep pass, the six routines and the Sheet flow were live in the drafts but untested in a clean agent.
- Source: `CHANGES-2026-09-28.md` ("RETEST.md and skills.diff were not redone for this pass"). Landed: `playbook/PLAYBOOK.md` gate ⑤, checklist K1, GUARDRAILS 49.

**N10. If a connection's tools can't be inspected before install, write skills that name the actions** (create spreadsheet, read range, append rows), not guessed tool names.
- Source: `CHANGES-2026-09-28.md` ("The Sheets connector's schema couldn't be inspected without installing it"). Landed: GUARDRAILS 50.

---

## 28 Sep 2026: Nomad Pro guardrails (full text and sources in `playbook/GUARDRAILS.md` 1–25)
G1 Never delete a bot with a live listing; retire the listing first. · G2 Update a live template only from the bot that owns its listing. · G3 "Optional" still means pack the plugin. · G4 Key `pluginId`, string value; check with GetPlugin. · G5 Keep every share call's args in the repo. · G6 Args ≤ 92 KB. · G7 Trim wording, never behaviour; keep a preservation table. · G8 Set avatar shape and colour before packaging; icon change = restage. · G9 No white or placeholder icon. · G10 One source for routine slugs; never rename a published slug. · G11 Live skills = args bodies; no build-time swaps. · G12 No owner names, pronouns, city or timezone in skills. · G13 Cron matches the words. · G14 Private-data hits fail the build. · G15 Build from the repo, not the shared live folder. · G16 Prefix slugs and descriptions with the bot name. · G17 Back up the live copy before every overwrite. · G18 First result by message 2. · G19 Routines silent unless something changed; ≤ 1 message per run. · G20 Tool output obeys the banned list. · G21 Nomad Pro only: records, never verdicts. · G22 Social only after the card is final and live. · G23 Bot repo private; public repos hold code only. · G24 Never guess the marketplace link. · G25 One spelling of the bot name.

---

## Nomad Pro-only choices: don't copy without asking Koko
These are right for Nomad Pro and were approved for it. A new bot gets them only if Koko says so in its intake.
- Tax and residency disclaimers, "records, not verdicts", its banned words (e.g. "non-resident"). *(Koko, 29 Sep 2026)*
- Routines on by default (Koko approved for Nomad Pro on 28 Sep 2026; new bots start with every routine off, K1).
- The legacy routine slug `calendar-review`. *(decision, 28 Sep 2026)*
- Row numbers in chat replies ("Rows 905–908") and greyed "Bot ref (ignore)" ID columns in its Sheet. *(COMPARE-row-links.md, COMPARE-sheet-layout.md; see K5 and the open questions in CHANGELOG v0.1)*
- One-tap check-in, quiet hours 22:00–08:00, heads-up bands. *(CHANGES-2026-09-28.md)*
