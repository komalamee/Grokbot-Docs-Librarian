# Repo standard: one private GitHub repo per bot

Version 0.1 (29 Sep 2026). Adapted from Bot Studio's repo standard (28 Sep 2026).

## The rules
- **Every bot has its own PRIVATE repo**, `grokbot-<bot>`, made from `grokbot-template` (Koko, 29 Sep 2026).
- **The repo holds the bot's latest version** (Koko's rule): merged to `main` **before or at** Publish.
- **Fixed files ship from the repo and install on import** (Koko, 29 Sep 2026): anything the bot needs on the user's side (folder sets, Sheet layouts, scripts) lives in `bot/fixed-files/`, and the bot's setup step installs it.
- Creating repos, pushing and merging happen only with Koko's OK. **Koko merges.**

**Be honest about what "private" protects.** Anyone who installs a published template can read its skills. A private repo protects notes, drafts, history, tests and private terms, not the prompts.

## Layout
```
grokbot-<bot>/                    (private, made from grokbot-template)
├─ README.md                      one line + live link + current version
├─ LEARNINGS.md  CHANGELOG.md     template's files (lessons go back upstream by PR)
├─ playbook/  templates/          the rules this bot was built with
└─ bot/                           (was bot-skeleton/)
   ├─ README.md                   the bot in one line, version, live link
   ├─ CHANGELOG.md                one entry per bot version, with listing URL
   ├─ bot.json                    profile, plugins (pluginId strings), memory, gettingStarted
   ├─ routines.json               the ONE source for routine slugs, schedules, cron, job text; every routine "enabled": false
   ├─ skills/<bot>-<name>/SKILL.md
   ├─ fixed-files/                files installed on import + MANIFEST.md
   ├─ docs/                       INTAKE.md, SPEC.md, RETEST.md, COMPARE-vX-vY.md, WEBSITE-HANDOFF.md
   ├─ listing/                    LISTING.md, images/
   ├─ proof/                      screenshots/, test-runs/ (evidence for each release)
   ├─ samples/                    fake data only (Sheet mock-ups, sample xlsx)
   ├─ args/                       create_bot_share_json.args.json (generated; committed per release)
   ├─ build.py  banned_scan.py  banned.txt
   └─ .gitignore                  private-terms.txt, *.local.*
```
`private-terms.txt` (real names, emails, cities) stays **outside** the repo or gitignored.

## Versioning
- `v2.0.0` = new card or big change · `v2.1.0` = new behaviour · `v2.0.1` = wording fix.
- **Repo tag = marketplace card version.** Tag after Koko presses Publish; the CHANGELOG entry carries the listing URL.
- One version = one args file = one tag = one set of proof. Never republish from untagged work.
- Retired: tag `retired-vX.Y.Z` and note the replacement link.

## Branches and PRs
- `main` = what's live. Work on `v<next>` branches; open a PR; **Koko merges**.
- The PR description holds the checklist result, the like-for-like comparison and links to the proof.
- If a PR can't be opened from where I am, hand off the exact files with SHA-256 checksums and apply scripts that check each change matches once (Nomad Pro: `pr-handoff-template-updates/`). The PR opens as a draft.

## Lessons go upstream
Any lesson learned in a bot repo goes to `grokbot-template` by PR: `LEARNINGS.md` + the file it affects + a CHANGELOG line. Then pull the template update into bots still in Build.

## When a public repo is needed
Only when something must be **fetchable at runtime by an installed bot**, e.g. an engine installed with `curl` (Nomad Pro's engine).
- Split it: **public repo** (code, tests, README, licence) + **private bot repo** (skills, notes, history).
- Public repo: no notes, drafts, transcripts, personal data or owner paths. Run `banned_scan.py` with private terms before each push.
- Bots install **tagged releases** (pinned, with a checksum) and tell the user before updating; never auto-pull `main`.
- **Open point:** a bot installed on someone else's account can't be expected to read Koko's private repo. Fixed files that install on import must either be small enough to live inside a skill, or come from a public, code-only location. Decide per bot in the spec.
