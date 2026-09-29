---
name: docs-librarian-renewals
description: "Docs Librarian renewals: PLACEHOLDER, not written yet. It will be used when a Docs Librarian owner asks about a renewal or an expiry date, and when the Docs Librarian renewal alert or monthly look-ahead routine runs."
---
# PLACEHOLDER: Docs Librarian renewals

**Nothing here is bot behaviour yet.** This file exists so the repo layout, `bot.json` and the build are in place. The skill itself is written at gate ④ of `playbook/PLAYBOOK.md`, from `docs/SPEC.md` only.

## What this skill will cover (all of it already agreed in `docs/SPEC.md`)
- Flagging a renewal or expiry 30 days ahead and asking whether to renew or cancel, with the provider's contact details (SPEC §8, Appendix A example 3).
- The price comparison: offered, never run on its own, with a warning that it uses tokens (SPEC §8).
- If the owner says yes: compare cover like for like against the clauses in the current document, show only published prices, link comparison sites for exact quotes, stay neutral (SPEC §8).
- The two renewal routines and their quiet rules live in `routines.json`; both start switched off (SPEC §9).

Skeleton to write it from: the job skill in `grokbot-template` v0.1 (`bot-skeleton/skills/`).
