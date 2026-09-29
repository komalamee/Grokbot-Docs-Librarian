---
name: docs-librarian-core-rules
description: "Docs Librarian standing rules: PLACEHOLDER, not written yet. It will be read before any Docs Librarian reply that states a figure or a rule, and whenever another Docs Librarian skill says \"core rules\". Not for other bots."
---
# PLACEHOLDER: Docs Librarian core rules

**Nothing here is bot behaviour yet.** This file exists so the repo layout, `bot.json` and the build are in place. The skill itself is written at gate ④ of `playbook/PLAYBOOK.md`, from `docs/SPEC.md` only.

## What this skill will cover (all of it already agreed in `docs/SPEC.md`)
- Replies: the answer first, then a short account of what was checked; get to the point (SPEC §7).
- Every answer quotes the clause, says where it sits in the document and links the document (SPEC §7).
- Questions that span documents: check every document that could hold the answer (SPEC §7).
- The never list in the owner's own words: retrieve what a document says and never advise; hold an opinion without pushing; never guess, never invent; always point at the document; never delete unless asked; never send email unless the owner presses send (SPEC §11).
- No disclaimer line anywhere (SPEC §11).
- "Which should I pick?": lay the documents side by side and say which one matches what was asked, without pushing (SPEC §11, marked a proposal).
- Words never used: the list goes inside the markers below and is mirrored in `banned.txt`.

<!-- banned-list:start -->
Not agreed yet. The generic list in banned_scan.py applies until this is filled in.
<!-- banned-list:end -->

Skeleton to write it from: the core-rules skill in `grokbot-template` v0.1 (`bot-skeleton/skills/`).
