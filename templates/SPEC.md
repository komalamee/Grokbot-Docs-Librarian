# SPEC: <Bot name>

<!-- Copy to bot/docs/SPEC.md. Fill it FROM docs/INTAKE.md, never from memory or from another bot.
     Everything traces to the intake. Anything I add is marked (proposal) and needs Koko's OK.
     Undecided items go under Open questions. Plain English, short. -->

Version: v0.1 draft · Date: ____ · Owner: Komal Amin · Builder: Bot Studio · Status: for Koko's review
Source: `docs/INTAKE.md`, confirmed by Koko on ____ (updates up to ____).

## 1. Goal line (agreed)
Agreed with Koko on ____:
> <one line: who it's for and the one outcome>

## 2. Who it's for
Who installs it and their situation, in Koko's words. The pain, in one line. Who it's **not** for.

## 3. What it holds
The things the bot keeps or tracks, as a short list.

## 4. Onboarding (one question per message)
1. **Message 1** (≤ 2 lines, wording in Appendix A): who it is + one question.
2. **Message 2** = the first result (wording in Appendix A).
3. **Data Sheet**: when it's created and the one line that gives the link.
4. **Connections**: offered once, with or after the first result; each can be declined.
5. **Routines question**: after the first result. Short: names each routine and its time, says each run uses tokens, asks which to switch on (§8).
6. Later questions, only when needed: ____

## 5. Data Sheet
Designed for a human to read first. Koko OKd the screenshot mock-up (fake data) on ____; it is in `samples/`.
- Name: "<Bot> – <Record>" · in the owner's Drive · never shared.
- **Summary tab**: a clean summary on top. A period dropdown (month / year / tax year: ____) that updates every number below it.
- **<Data> tab**: one line per item. A **Period** column instead of tabs per year. Filter on. Columns: ____
- Every tab: row 1 a short plain note, row 2 headers, both frozen; editable columns shaded; set column widths; dates like "28 Sep 2026".
- Never: record-ID codes, "source rows", backup tabs, private file paths, codes a person has to decode.
- Unknown values stay blank or "Not recorded". Never guessed.
- The bot writes to the Sheet first and reads it before every run. The owner's edits win; a bad row is flagged in one line.
- Without Sheets: ____ (e.g. CSV + one offer).

## 6. Flows
The main things the bot does, one short paragraph each (e.g. "New document found", "Renewal coming up"). For each: what starts it, what the bot does, what it says (≤ 2 lines), what it writes to the Sheet.

## 7. Answers
- Answer first, then at most one short line on what it checked.
- Only facts from the user or their data. Never a fact, place, date or status the user hasn't given.
- Where it points to a source, it says it in plain words (document name, section, link), never an ID.
- Tone in Koko's words: ____

## 8. Routines
All routines start **OFF** (`"enabled": false` in `routines.json`). During setup the bot asks which to switch on and switches each on only with the user's yes. The cron fires at the exact minute in the words. Quiet when nothing changed; ≤ 1 message per run.
| Routine | Slug | When (owner's timezone) + cron | Stay quiet when | Needs | Suggested at setup? |
|---|---|---|---|---|---|
| | `<bot>-…` | e.g. Daily 09:00 · `0 9 * * *` | | | |

## 9. Connections
| Connection | pluginId (string) | Must / nice | Access | Why | Without it |
|---|---|---|---|---|---|
| Google Sheets | "45893414" | | edit | the data Sheet | |
| Google Drive | "45893413" | | own folder | | |
| Gmail | "45893410" | | read-only (drafts only; the user presses Send) | | |
| Google Calendar | "45893411" | | read-only | | |
Every connection any skill or routine mentions gets packed. Check each with GetPlugin before build.
**Fixed files installed on import:** what, where they go, how the bot installs them (→ `fixed-files/MANIFEST.md`).

## 10. Never
In Koko's words from the intake, plus the standing rules: never send email (the user presses Send) · never delete unless asked for that exact thing · never guess · never state facts the user hasn't given · never embellish.

## 11. Disclaimer
**None** (default). Only if the intake says the subject needs one: why, and the exact words (then word for word, at most one per message).

## 12. Test plan: what "working" means
Koko's definition from the intake, as numbered checks. Plus the standard retest (`templates/RETEST.md`): "hi" → first result by message 2 · main job · off-scope · routines question · each routine incl. quiet case and fire time · no connections. Evidence goes in `proof/`.

## 13. What gets built
- **Skills**: `<bot>-getting-started` (§4) · `<bot>-core-rules` (§7, §10, §11) · `<bot>-<job>` (§6) · others only if needed.
- **Routines**: `routines.json`, every one off (§8).
- **Fixed files**: `fixed-files/` (§9).
- **Sheet**: layout from §5 (in `fixed-files/` if every install must build the same Sheet).
- **Listing**: `listing/LISTING.md`.

## Open questions
1. <question> · who decides · by when

---
## Appendix A: approved wording (word for word, with the date and time Koko approved it)
**Message 1** (approved ____): "…"
**Message 2** (approved ____): "…"
**Routines question** (approved ____): "…"
**Example chat 1** (approved ____): …
**Example chat 2** (approved ____): …
**Example chat 3** (approved ____): …
