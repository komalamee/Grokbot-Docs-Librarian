---
name: docs-librarian-library
description: "Docs Librarian library: PLACEHOLDER, not written yet. It will be used when a Docs Librarian owner asks a question about their documents, sends a new document, or when the Docs Librarian inbox check routine runs."
---
# PLACEHOLDER: Docs Librarian library (search, filing, the index, answers)

**Nothing here is bot behaviour yet.** This file exists so the repo layout, `bot.json` and the build are in place. The skill itself is written at gate ④ of `playbook/PLAYBOOK.md`, from `docs/SPEC.md` only.

## What this skill will cover (all of it already agreed in `docs/SPEC.md`)
- What the library holds: card policies, insurance, contracts of any kind including before signing, tenancy agreements, utility and phone contracts with their small print and the owner's rights, provider contact details, and subscriptions (SPEC §3).
- Searching the inboxes and folders the owner named, up to five years back, and filing what it finds (SPEC §4).
- The index Sheet: a documents tab, one row per document, and a renewals tab sorted by date (SPEC §5).
- New documents: ask before saving, then save the files, add the row and confirm in one line with the link to the row (SPEC §6).
- Answering: the answer first, then what was checked, with the clause quoted, its place in the document named and the document linked (SPEC §7).

## Not decided yet
Sheet and tab names, the renewals columns and how the fixed files reach the owner are open questions in `docs/SPEC.md`.

Skeleton to write it from: the job skill in `grokbot-template` v0.1 (`bot-skeleton/skills/`).
