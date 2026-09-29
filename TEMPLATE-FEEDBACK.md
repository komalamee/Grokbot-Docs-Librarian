# Feedback for `grokbot-template` v0.1

What was unclear, wrong or missing while following the template's own "How to start a new bot" steps to set up this repo (29 Sep 2026, Docs Librarian, the first real use of the template).

Nothing here changes Docs Librarian's agreed behaviour. Per `playbook/PUBLISH-CHECKLIST.md` L6 and the template's "one rule that makes this work", each item below belongs in a PR to `grokbot-template` (`LEARNINGS.md` + the file it affects + a CHANGELOG line). **Koko reviews and merges.**

## 1. `build.py` reads a long routine slug as a secret (blocks the build)
The private-data pattern `\b[A-Za-z0-9_-]{32,}\b` ("token-like string") matches any kebab-case slug of 32 characters or more. SPEC §9's `docs-librarian-monthly-look-ahead` is 33, so the documented build command fails:
`FAIL private data (token-like string): ... "slug": "docs-librarian-monthly-look-ahead"`.
Worked around with a one-line `bot/allow.txt` and `--allow allow.txt`, which means the build command in `bot-skeleton/README.md` is not the one that works.
**Suggested fix:** in `build.py`, skip strings that contain a hyphen (or auto-allow every slug already declared in `bot.json` and `routines.json`), and add `--allow allow.txt` to the documented build line.

## 2. The owner's name is required in the listing and forbidden by the private scan
`bot-skeleton/private-terms.example.txt` says private terms include "Owner and builder names", but checklist J5 requires `listing/LISTING.md` to carry "Made by Komal Amin". With the owner's name in `private-terms.txt`, the documented scan fails: `listing/LISTING.md: [komal amin] Komal Amin`.
**Suggested fix:** decide one way — either the scan runs over `skills args` with the listing checked separately, or the attribution line goes in `allow.txt` by default, or the example file tells the owner to leave the published author name out.

## 3. The documented path for `private-terms.txt` is not gitignored
`bot-skeleton/README.md` says `--private-terms ../private-terms.txt`, which is the **repo root**, but the only `.gitignore` is `bot/.gitignore` and it covers `bot/private-terms.txt`. Following the documented command puts a file of the owner's real names one `git add -A` away from being committed.
**Suggested fix:** ship a root `.gitignore` in the template (`private-terms.txt`, `*.local.*`, `.env*`, `__pycache__/`). Added in this repo already.

## 4. Nothing says what to do with the master template's own root `README.md`
Step 2 covers `bot-skeleton/` and `mybot`, so a literal reading leaves the bot repo's front page saying "The master template for every Grok Bot that Bot Studio builds" and "press Use this template". `playbook/REPO-STANDARD.md` gives the root README the same one-line brief as `bot/README.md`, so it is also unclear what each of the two should hold.
**Suggested fix:** add a step "replace the root README with the bot repo README", and ship a root `README.template.md` whose brief differs from `bot/README.md` (repo map and where the docs live, versus the bot's own files).

## 5. Two CHANGELOGs, one rule
The root `CHANGELOG.md` is the template's own history; `bot/CHANGELOG.md` is the bot's versions. `REPO-STANDARD.md` lists the root one under "template's files" but never says whether to freeze it at the version the bot started from or keep adding to it. Frozen here, with the version recorded in `bot/CHANGELOG.md`.
**Suggested fix:** one line in `REPO-STANDARD.md`.

## 6. The skeleton's skills don't match the skill list a spec produces
`bot-skeleton/` ships `getting-started`, `core-rules` and `main-job`, while this spec (SPEC §13) needs `getting-started`, `core-rules`, `library` and `renewals`. Step 2 only talks about renaming `mybot`, not about adding or renaming skills, and `bot.json`'s `skills` array has to be edited to match. Renamed `main-job` to `docs-librarian-library` and added `docs-librarian-renewals`.
**Suggested fix:** say in step 2 that the spec's skill list wins, `bot.json` `skills[]` is the single source, and `main-job` is a skeleton to copy per job skill.

## 7. `mybot` isn't the only placeholder
A find-and-replace of `mybot` / `MyBot` still leaves `<Bot name>`, `<bot>`, `<one job>` and `<date>` in `README.md`, `CHANGELOG.md`, `fixed-files/MANIFEST.md`, `listing/LISTING.md` and `docs/WEBSITE-HANDOFF.md`.
**Suggested fix:** list every placeholder token in step 2, or add a tiny `init.py` that does the rename and prints what is left to fill in by hand.

## 8. Every routine has to be given a clock time, even an event-driven one
`build.py` requires `cron` for every routine and a `schedule` whose time matches it. SPEC §8's renewal alert is date-driven ("30 days before a renewal or expiry"), so it had to be written as a daily 09:00 check that stays quiet unless something is 30 days away. That is a reasonable convention, but the template never states it.
**Suggested fix:** document the "daily check, quiet unless due" convention in `templates/SPEC.md` §8 and `routines.json`, or allow a `trigger: "date"` routine without a clock time.

## 9. No convention for a repo that is set up before the skills exist
The template assumes the repo is made and the bot built in one go, so there is no guidance on what a set-up-only repo should contain: what a placeholder skill looks like, whether `listing/`, `fixed-files/` and `docs/WEBSITE-HANDOFF.md` get filled or left blank, and whether a pre-release `args/create_bot_share_json.args.json` should be committed (`.gitignore` only excludes `*.FAILED.json`, and `REPO-STANDARD.md` says "committed per release"). Marked every unwritten file `PLACEHOLDER` here and committed the setup-only args, labelled as such in `bot/CHANGELOG.md`.
**Suggested fix:** a short "repo set up, skills not written yet" state in `PLAYBOOK.md` gate ③, with a placeholder skill skeleton.

## 10. The template's open point on fixed files now has a worked answer, and it contradicts another rule
`REPO-STANDARD.md` and `fixed-files/README.md` both leave open how a fixed file reaches a user, since an installed bot can't read a private repo. Docs Librarian answers it by making the repo public and fetching the two small JSON files from `raw.githubusercontent.com` on `main`. That works, but `REPO-STANDARD.md` also says installs should pin **tagged releases with a checksum** and "never auto-pull `main`" (lesson N6), which is the opposite of what fetching from `main` does. Two rules, no way to follow both.
**Suggested fix:** close the open point with the public-repo pattern written out, and say plainly which files may track `main` (small, generic, layout-only) and which have to be pinned to a tag with a checksum (anything executable). A public bot repo also needs a line about what may live in it: this repo's `docs/INTAKE.md` and `docs/SPEC.md` are now world-readable, which `REPO-STANDARD.md` ("public repos hold code only, no notes or drafts") would not allow.

## 11. Small things
- `bot-skeleton/fixed-files/README.md` uses Docs Librarian as its worked example, so that text now travels into every other bot's repo. Move the example into the master template's docs, or make it generic.
- `bot-skeleton/fixed-files/MANIFEST.md` still points its example row at `mybot-getting-started`, which a `mybot` rename silently turns into a row the bot may not have.
- README step 1 asks for `grokbot-<bot>` (`grokbot-docs-librarian`); this repo is `Grokbot-Docs-Librarian`. Worth saying whether the exact spelling matters.
- SPEC Appendix B says to check each plugin ID with `GetPlugin` before the build. That can't be done from the repo, so the four IDs in `bot/bot.json` are unverified and need checking at gate ④.
