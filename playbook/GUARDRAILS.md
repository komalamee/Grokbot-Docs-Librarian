# Guardrails

Version 0.1 (29 Sep 2026). Each item: **Rule** · *Why* (what happened) · source.
Items 1–25: Bot Studio's Nomad Pro lessons (28 Sep 2026; item 21 updated 29 Sep). Items 26 on: added 29 Sep 2026. The dated log of every lesson, with IDs, is `../LEARNINGS.md`.
Sources named "Nomad Pro:" are Bot Studio's Nomad Pro v2 drafts. "(brief)" = from Bot Studio's brief, no file evidence.

## Listings and bots
1. **Never delete a bot that has a live listing. Retire the listing first, then archive the bot.**
   *Why:* deleting the source bot locked its live listing from updates. *(brief; deleted-agents record)*
2. **Update a live template only from the bot that owns its listing.**
   *Why:* a copy can't update the original listing; you get a second listing. *(follows from 1)*

## Connections
3. **"Optional in skills" still means "pack it". Pack every plugin any skill or routine mentions.**
   *Why:* v2 dropped Gmail, Calendar and Drive by reading "optional" as "don't pack". *(Nomad Pro: V1-V2-COMPARISON §1)*
4. **Key is `pluginId`, value is a string. Check each with GetPlugin before staging.**
   *Why:* `plugin_id` got mixed up with `pluginId`; a wrong key silently packs no connections. *(brief; build.py; TRIM-LOG)*
5. **Keep a copy of every share call's args in the repo.**
   *Why:* nobody could prove what v1 actually packed. *(Nomad Pro: V1-V2-COMPARISON "Still unverified")*

## Size
6. **Args ≤ 92 KB. The build fails above it.**
   *Why:* 103,056 bytes was rejected; 98.0 KB staged. Trimming 11.7 KB cost a whole pass. *(Nomad Pro: TRIM-LOG)*
7. **Trim wording, never behaviour; keep a behaviour-preservation table.**
   *Why:* the trim kept all 30+ behaviours only because each was checked off after. *(Nomad Pro: TRIM-LOG, COMPARE-overseas-work §4)*

## Icon
8. **Set the avatar shape and colour before packaging. Any icon change after staging = restage.**
   *Why:* the staged card showed the old icon. Templates copy only shape and colour, not an uploaded picture. *(brief)*
9. **Never ship a white or placeholder icon. Koko checks the icon on the staged card.**
   *Why:* a white placeholder icon reached the card. *(brief)*

## Building the args
10. **One source for routine slugs (`routines.json`); the build checks them. Never rename a published slug.**
    *Why:* slugs drifted across files; a mismatch can create duplicate routines on update. Nomad Pro keeps `calendar-review`. *(Nomad Pro: build.py vs V1-V2-COMPARISON §3)*
11. **Live skill files must equal the args bodies. No text swaps at build time.**
    *Why:* build.py swapped "21:00 Bangkok time" for "21:00 your time" in the args only. *(Nomad Pro: build.py)*
12. **No owner-specific words in skills: no names, pronouns, city or timezone.**
    *Why:* Koko's timezone and the wrong pronoun were baked into skills every installer gets. *(Nomad Pro: RETEST.md, prev-round getting-started)*
13. **Cron must match the words, to the minute.**
    *Why:* Nomad Pro's calendar review said "Sunday 18:00" but its cron was `5 18 * * 0`, so it ran 5 minutes late. *(Nomad Pro: CHANGES-2026-09-28)*
14. **Private-data hits fail the build, with an explicit allow-list.**
    *Why:* printing hits without failing lets real leaks hide in the noise. *(Nomad Pro: build.py output)*
15. **Build from the repo, never from the shared live folder.**
    *Why:* another desk's `getting-started` would have been packed and hijacked a new user's first message. *(Nomad Pro: PACKAGING "Exclude")*
16. **Prefix every slug and description with the bot name.**
    *Why:* generic triggers ("a backup", "where do I stand") pull other bots' skills in. *(Nomad Pro: PACKAGING "Collision risk")*
17. **Back up the live copy before every overwrite.**
    *Why:* six rounds in one day were only safe because each had a dated backup. *(Nomad Pro: backups)*

## Behaviour
18. **First useful result by message 2.**
    *Why:* v1 asked 25–35 questions before any value. *(Nomad Pro: review; V1-V2-COMPARISON §7)*
19. **Routines stay silent unless something changed; ≤ 1 message per run.**
    *Why:* "no changes" messages train people to mute the bot. *(Nomad Pro: CHANGES-2026-09-28 §3)*
20. **Engine and tool output must obey the banned list too.**
    *Why:* the engine printed a banned word after the skills banned it. *(Nomad Pro: CHANGES-2026-09-28)*
21. **Nomad Pro only: records, never verdicts.** Not a rule for every bot. Other bots get disclaimers or advice limits only when their subject needs them and Koko agrees in intake.
    *Why:* Nomad Pro's tax and residency limits. Koko, 29 Sep 2026: those disclaimers were Nomad Pro-specific. *(board, review; Koko)*

## Launch and public assets
22. **Schedule social only after the card is final and live. Any link or icon change → Brandy P rechecks every scheduled asset.**
    *Why:* scheduled assets went stale. *(brief)*
23. **Bot repo private. A public repo (e.g. an engine) holds code only. Scan before every push.**
    *Why:* a public repo exposed working notes. *(brief)*
24. **Never guess the marketplace link in public copy; use `[MARKETPLACE LINK]` until Koko sends it.**
    *Why:* the website handoff already works this way. *(Nomad Pro website doc)*
25. **One spelling of the bot name.**
    *Why:* the live name used a hyphen and the drafts an en dash. *(Nomad Pro: CHANGES.md Q8)*

## Added 29 Sep 2026: Koko's rules (see LEARNINGS K1–K15)
26. **Routines start OFF.** The bot asks during setup which to switch on and switches each on only with the user's yes (token burn). *(K1)*
27. **Every bot has its own private GitHub repo with its latest version. Fixed files ship from the repo and install on import.** *(K2)*
28. **A clear one-line goal and a thorough intake with Koko come before anything else.** *(K3)*
29. **Disclaimers are opt-in, never default.** *(K4)*
30. **Sheets are designed for a human reader first:** clean summary with a period dropdown, one line per item, proper formatting and widths, readable dates, one filterable data tab with a period column, no record-ID codes or "source rows". *(K5)*
31. **Show a screenshot mock-up before changing any template Sheet layout.** *(K6)*
32. **Never state facts, places, dates or statuses the user hasn't given.** *(K7)*
33. **Never embellish or invent in first-person copy.** *(K8)*
34. **Full like-for-like comparison against the previous version before any republish.** *(K9)*
35. **Concrete proof (screenshots, test-run evidence) before any release.** *(K10)*
36. **Koko presses Publish and merges PRs.** *(K11)*
37. **Messages answer first, short and plain.** *(K12)*
38. **Routine crons fire at the exact agreed minute.** *(K13)*
39. **The first message and the routines message are short and correct.** *(K14)*
40. **Never send email unless the user presses Send.** *(K15)*

## Added 29 Sep 2026: from the Nomad Pro drafts (see LEARNINGS N1–N10)
41. **One figure, one label, everywhere** (chat, Sheet, dashboard, files). *(N1)*
42. **Quote numbers from the tool; the bot never does its own arithmetic on them.** *(N2)*
43. **Mock-ups, samples and examples use fictional data only.** *(N3)*
44. **The data Sheet needs the Google Sheets connection with edit access.** *(N4)*
45. **A layout change on a live Sheet needs a one-time update step for existing users.** *(N5)*
46. **Engine updates reach every live install: pin tagged releases and tell the user before updating.** *(N6)*
47. **A comparison says what it could not check.** *(N7)*
48. **When a PR can't be opened from here, hand off exact files with checksums. Koko merges.** *(N8)*
49. **Redo the clean-agent retest after every change round.** *(N9)*
50. **If a connection's tools can't be inspected before install, name the actions, not guessed tool names.** *(N10)*
