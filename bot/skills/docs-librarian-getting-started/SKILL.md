---
name: docs-librarian-getting-started
description: "Docs Librarian first conversation: PLACEHOLDER, not written yet. It will be used when Docs Librarian has just been installed and is talking to its new owner for the first time, or when they say \"set me up\" or \"start again\"."
---
# PLACEHOLDER: Docs Librarian getting started

**Nothing here is bot behaviour yet.** This file exists so the repo layout, `bot.json` and the build are in place. The skill itself is written at gate ④ of `playbook/PLAYBOOK.md`, from `docs/SPEC.md` only.

## What this skill will cover (all of it already agreed in `docs/SPEC.md`)
- Message 1 and message 2, word for word from SPEC Appendix A: where to keep documents, then search or send (SPEC §4.1–4.2).
- Creating the empty index Sheet right after message 2, before any search, and sending its link (SPEC §4.3, §5).
- Setting up the folder set: policies, receipts and payments, deadlines (SPEC §4.4).
- Progress updates while searching, about one per 10 documents, and the end-of-search summary (SPEC §4.5–4.6).
- The first result: review the routines, remind the owner what the library holds, suggest questions, ask how often to check the inbox, with the token warning (SPEC §4.7).
- The routines question: every routine starts off and is switched on one at a time, only after the owner says yes (SPEC §9).
- Installing the fixed files listed in `fixed-files/MANIFEST.md`, after the owner says yes, then one line saying what went where (SPEC §13).

## Not decided yet
The open questions in `docs/SPEC.md` (Sheet and tab names, renewals columns, routine times, how each fixed file reaches the user) are settled with the owner before this skill is written.

Skeleton to write it from: the getting-started skill in `grokbot-template` v0.1 (`bot-skeleton/skills/`).
