# Playbook: shipping a Grok Bot template

Version 0.1 (29 Sep 2026). Adapted from Bot Studio's playbook (28 Sep 2026, updated 29 Sep 2026) so this repo stands on its own.
Owner: Komal Amin (Koko). Builder: Bot Studio. One bot at a time through 11 gates. **At most two bots in Build at once.**

```
Idea → Goal and intake → Spec → Build → Test → Package → Pre-publish check → Publish → Post-launch → Learn → Retire/replace
 ①          ②             ③      ④       ⑤       ⑥            ⑦               ⑧          ⑨           ⑩          ⑪
```
Each gate needs Koko's OK to move on.

## Who does what
| Who | Does | Never |
|---|---|---|
| **Koko** | Picks ideas, joins the intake, approves each gate, **merges PRs**, checks the staged card, **presses Publish**, OKs every outside message | — |
| **Bot Studio** | Runs the intake, writes the spec, builds, tests, packages, stages, drafts the listing and comparison, keeps the repo and board | Publish, merge, message outsiders, post, delete a bot |
| **Brandy P** | X/social drafts and scheduling, after Koko's OK | Post before the card is live and final |
| **Chief** | Website page, **Nomad Pro only** | Other bots' pages |
| **Hermes** (Koko's) | Website pages for **every other bot** | — (Bot Studio writes a handoff doc; **Koko passes it on**) |

**Hard rule:** nothing is published, posted, pushed public or sent to anyone outside without Koko's say-so for that exact thing.
**Open:** whether Bot Studio may merge after Koko says yes in chat is still undecided. Until Koko decides, Koko merges.

## The rules that apply to every gate
- **Goal first, intake second, spec third.** Never fill a gap with a guess, and never copy another bot's choices (Nomad Pro included) without asking.
- **Disclaimers are opt-in.** Default: none. Add one only if the bot's own subject needs it (e.g. health, money, law) and Koko agrees in intake.
- **Routines start OFF.** The bot asks during setup which ones to switch on, and switches each on only with the user's yes (every run uses tokens).
- **Never state facts, places, dates or statuses the user hasn't given.** Never embellish in first-person copy.
- **Proof before release.** Screenshots and test-run evidence in `proof/`. A full like-for-like comparison before any republish.
- **Every lesson goes back into this template** (`LEARNINGS.md` + the file it affects), by PR.

---

## ① Idea
- **Entry:** an idea on the board.
- **Steps:** one line: who, the one job, the pain, first result, connections, effort (S/M/L). Quick saturation check (say it's not market research). Drop anything that repeats a live bot.
- **"Worse without it" test (Andy):** would going back to a plain Grok chat make the user's workflow noticeably worse? Is it more than one prompt? Does it use 2+ of: routines, connected tools, repeated context, background work, memory? If not, drop it or rethink it.
- **Exit:** Koko picks it **and** fewer than 2 bots are in Build.

## ② Goal and intake
- **Entry:** Koko picked the idea.
- **Steps:**
  1. Agree a one-line goal with Koko: who it's for and the one outcome.
  2. Run the intake conversation with `INTAKE-GUIDE.md`: 13 topics, one per message, plain words. Listen more than propose. Label my ideas "My suggestion".
  3. After each topic, play back what I understood in 1–3 lines. Koko corrects it.
- **Output:** `docs/INTAKE.md` (from `templates/INTAKE.md`), in Koko's words, open points marked.
- **Exit:** Koko confirms `docs/INTAKE.md`.

## ③ Spec
- **Entry:** intake confirmed.
- **Steps:** make the private repo from this template (with Koko's OK). Fill `docs/SPEC.md` from `templates/SPEC.md`, **from the intake**. Every choice traces to intake or is marked as my suggestion and approved. Approved wording goes word for word into the appendix.
- **Exit:** Koko approves the spec. First result by message 2. A reason to come back each week.

## ④ Build
- **Entry:** approved spec.
- **Steps:**
  1. Create the source bot. **Set its avatar shape and colour now** (not white).
  2. Write skills from the skeletons: `<bot>-getting-started`, `<bot>-core-rules`, one job skill, then only what the job needs. Prefix every slug and description with the bot name.
  3. Design the data Sheet for a human reader first (`SPEC.md` §5). **Show Koko a screenshot mock-up** with fake data before building it, and before any later layout change.
  4. Write `routines.json`: the one source for slugs, schedules, cron and job text. **Every routine `"enabled": false`.**
  5. List every connection the skills mention in `bot.json`.
  6. Put anything that must be installed on import in `fixed-files/`, with setup steps inside the bot (e.g. in getting-started or an `<bot>-setup` skill). Same for anything else that won't transfer (MCP servers, scripts, an engine).
  7. Copy skills to the live folder only from the repo; back up the live copy first.
- **Exit:** `python3 build.py` runs clean.

## ⑤ Test
- **Entry:** clean build.
- **Steps:** in a **clean agent** (no other skills visible): "hi", the main job, an off-scope ask, the routines question in setup, a dry run of each routine (incl. the quiet case), no connections at all. Time to first result. Check each routine's cron fires at the agreed minute. Only if intake agreed advice limits: one ask that tests them.
- **Output:** `docs/RETEST.md` (from `templates/RETEST.md`) with pass/fail per case, and the evidence in `proof/` (screenshots, transcripts, test-run logs).
- **Exit:** all pass; first result by message 2; behaves as `docs/INTAKE.md` describes. Redo the retest after every change round.

## ⑥ Package
- **Entry:** tests pass.
- **Steps:** `python3 build.py --check-live <live skills folder> --private-terms <file outside the repo>` → args JSON. `python3 banned_scan.py skills listing args --banned banned.txt`. Write `listing/LISTING.md`. For a republish, write the like-for-like comparison (`templates/COMPARE.md`).
- **Exit:** ≤ 92 KB, 0 banned, 0 private, 0 body diffs, comparison clean.

## ⑦ Pre-publish check
- **Entry:** package ready.
- **Steps:** tick every item in `PUBLISH-CHECKLIST.md`. Review the share draft line by line: instructions, memories, skills, routines, plugins; no keys, internal URLs or client data (Andy). Open a PR with the exact files; **Koko merges**. Draft launch content now (see ⑨): ready, not posted. Stage from **inside the source bot** (for an update: the bot that owns the live listing).
- **Exit:** Koko has seen the staged card: **right icon, all connections visible**. Any icon or skill change after staging = restage.

## ⑧ Publish
- **Entry:** checklist all ticked, PR merged.
- **Steps:** **Koko presses Publish.** Check the link: `x.ai/bot/` + 21 characters, opens the right card. Tag the repo `vX.Y.Z`; add the link to `CHANGELOG.md`.
- **Exit:** the live page shows name, author "Komal Amin", icon and description as staged.

## ⑨ Post-launch
- Links: URL in the repo README, listing file and board.
- Marketplace: listed there as well as shared on X (Andy).
- Social: hand Brandy P the final link, icon, 3–4 example first messages and visuals. Koko OKs each post. Formats (Andy): pain point line · screen recording of the output · walkthrough article · workflow article. No "paid partnership" label (Koko isn't in the rewards programme).
- Website: Nomad Pro → Chief. Any other bot → `docs/WEBSITE-HANDOFF.md`, **Koko passes it to Hermes**.
- Any later link or icon change → restage, Koko rechecks the card, Brandy P rechecks every scheduled asset, the site is updated.
- **Exit:** every public asset points to the live link and current icon.

## ⑩ Learn
- **Entry:** live for 1–2 weeks, or feedback arrives.
- **Steps:** gather installs, repeat use, feedback, errors (never invent numbers). **Write each lesson into this template's `LEARNINGS.md` and the file it affects, by PR.** Plan the next version as a spec change.
- **Exit:** Koko picks: improve (back to ③), keep, or retire.

## ⑪ Retire / replace
- **Retire the listing first** (point it to the replacement, or unpublish). Keep the source bot; archive it, never delete it while any listing uses it. Update social links and the website. Tag the repo `retired-vX.Y.Z`.
- **Exit:** no public link points to a dead bot.

---

## Updating a live bot (republish)
Gates ④–⑧ again, plus: same source bot · like-for-like comparison against the live version · version bump · fresh proof · Koko checks the card again · social assets rechecked. Published routine slugs never change (list them in `bot.json` `legacy_routine_slugs`).

## Decisions log
- **28 Sep 2026:** Nomad Pro keeps its published slug `calendar-review` (published in v6). New bots use the `<bot>-` prefix.
- **28 Sep 2026:** website for other bots = Hermes, via a handoff doc Koko passes on. Chief keeps Nomad Pro.
- **29 Sep 2026 (Koko):** goal and intake gate added; disclaimers no longer a default.
- **29 Sep 2026 (Koko):** routines start OFF and are switched on only with the user's yes. Replaces "on by default where Koko agreed".
- **29 Sep 2026 (Koko):** every bot has its own private repo with its latest version; fixed files ship from the repo and install on import.
- **29 Sep 2026 (Koko):** Sheets designed for a human reader; no record-ID codes or "source rows" anywhere. Replaces the old "outputs name source rows" rule.
- Andy's rewards-programme items don't apply (Koko doesn't qualify).
