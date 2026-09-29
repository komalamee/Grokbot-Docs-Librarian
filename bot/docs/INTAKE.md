# INTAKE: The Librarian (working title; name undecided, see Open points)

Date: 29 Sep 2026 (in progress) · Talked through with: Koko · Written by: Bot Studio · Confirmed by Koko: not yet
In Koko's words where possible. My own ideas are marked *(my suggestion)*; keep them only if Koko said yes.

## 1. Goal line
> Not agreed yet. Koko's words so far: it's for everybody; it files the user's important documents in an organised way so they can query them like a database; it tracks what's up for renewal and what insurance covers.

## 2. Who uses it
- "For everybody", especially people who don't like filing things away, want them filed in an organised way, and then want to query them like a database.
- The struggle today: people never read their policies. Koko: "that's a really important part."
- Koko's own setup: she uses Obsidian and keeps all her finance documents and policies there.

## 3. A normal day or week with the bot
- The user asks questions about their documents any time, e.g. what their credit cards cover or what their travel insurance says.
- On its own, the bot checks the inbox (how often: open), notices new sign-ups and policies, and offers to save them to the library.
- It warns before a renewal and asks whether to renew or cancel.
- Documents it holds:
  - Credit card policies.
  - Insurance: car, health, travel.
  - Job contracts, shareholder contracts, any contract (including before signing).
  - Tenancy agreements.
  - Electricity and phone provider contracts: pull out the small print and extract the user's rights.
  - Subscriptions can go in, but they're not the focus.
- It keeps provider contact details so the user can ask about a policy, cancel, or ask for a refund.

## 4. First result (by message 2)
What makes it feel like it's working (Koko):
- Review the scheduled routines with the user.
- Suggest questions it can answer.
- Remind them of the documents it already holds.
- Ask how often to check the inbox.
How this fits into message 2: open (see Open points).

## 5. Must never do
- Advise. "It isn't advising; it retrieves wording."
- (Nothing else discussed yet.)

## 6. Replies: tone, length, look
Tone: not discussed · Length: not discussed · Look: not discussed (default: simple, short, visual first)
- Every answer shows where the clause came from in the document and links to where the document is kept. *(my suggestion; Koko agreed)*

## 7. Onboarding
Message 1: not written yet.
Message 2 (first result): see section 4.
Questions Koko listed (order and timing still open):
1. Where to save documents: locally on the computer, or in the cloud (Google Drive; maybe iCloud, unverified).
2. How to do the intake: the user hands over all documents, or the bot searches.
3. If it searches:
   - Ask permission to search the inbox or inboxes, and the device (laptop).
   - Ask for the folder paths where documents are kept.
   - Ask the user what to look for.
   - It may need to go back about 5 years (feasibility unknown).
4. It sets up folders for policies, receipts/payments, and deadlines (renewal or expiry dates).

## 8. Routines
| What | Exact time (owner's time) | Stay quiet when | On by default? |
|---|---|---|---|
| Inbox check for new documents and policies. When it spots one (e.g. travel health insurance signed up yesterday), it says: "I see you signed up to this. Do you want me to save the policy, receipts and all that to the library?" | Open. *(my suggestion: daily; Koko hasn't decided)* | *(my suggestion: message only when something is found; Koko hasn't decided)* | Open |
| Renewal warning: notifies before a renewal and asks whether to renew or cancel | Open (how far ahead: not discussed) | Open | Open |

Why the new-document message matters (Koko): the user knows it's saved and remembers they can query it.

## 9. Data Sheet
| Tab | What's in it | User edits it? |
|---|---|---|
| | | |
Not discussed. Koko described folders instead: policies, receipts/payments, deadlines (renewal or expiry dates), plus provider contact details. Whether there is also a Sheet: open.

## 10. Connections
| Connection | Why it's needed | Required or optional |
|---|---|---|
| Email (inbox or inboxes) | Search for documents; spot new sign-ups and policies | Open (asked with permission at onboarding) |
| Device / laptop folders | Search the folder paths the user gives | Open (asked with permission at onboarding) |
| Google Drive | Place to save documents (cloud option) | Open |
| iCloud | Place to save documents (cloud option) | Open; support unverified |
| Local Obsidian Markdown | Koko keeps her finance documents and policies in Obsidian | Open |

## 11. Disclaimer
Needed? Not decided. Koko: "It isn't advising; it retrieves wording." Whether that needs a disclaimer line, and its exact words: open.

## 12. What "working" means
- The routines have been reviewed with the user.
- The user has been shown questions it can answer.
- The user has been reminded which documents it already holds.
- The user has said how often to check the inbox.
- New documents get noticed and saved, so the user knows they're in the library and can query them.

## 13. Example conversations
**1.** User: "If I use my Revolut credit card, will it give me car rental insurance?" → Bot: quotes the clause, says where it is in the document and links to the document. (Exact reply not written yet.)
**2.** User: "Talk me through exactly what car rental insurance I've got across all my credit cards." → Bot: same pattern, across every card policy it holds. (Exact reply not written yet.)
**3.** User: "What do I need to know about my travel insurance policy?" → Bot: same pattern. (Exact reply not written yet.)
**4.** Bot (after an inbox check): "I see you signed up to this. Do you want me to save the policy, receipts and all that to the library?"

## GitHub repo (Koko)
- Lets Koko review the whole process end to end.
- Holds fixed files that must be installed on the user's computer when the bot is imported.

## Open points
- [ ] Name. "Librarian" is taken (Librarian by Shane, https://x.ai/bot/suKVjDAR-hSr_PTBxgdRw). *(my suggestions: Small Print (my favourite), Fine Print, The Archivist, Policy Keeper, Clause, Paper Trail)*. Undecided · Koko decides.
- [ ] Goal line (one line: who, the one outcome) · Koko agrees.
- [ ] How often to check the inbox. *(my suggestion: daily, message only when something is found)*. Not agreed · Koko decides.
- [ ] iCloud support: unverified · Bot Studio to check.
- [ ] Searching back about 5 years: feasibility unknown · Bot Studio to check.
- [ ] How far ahead of a renewal to notify · Koko decides.
- [ ] Onboarding message 1 wording, and which items land in message 2 · Koko decides.
- [ ] Tone, length and look of replies · Koko decides.
- [ ] Anything else it must never do · Koko decides.
- [ ] Data Sheet: whether there is one alongside the folders, and what's in it · Koko decides.
- [ ] Which connections are required and which optional · Koko decides.
- [ ] Disclaimer: needed or not, and its words · Koko decides.
- [ ] Which fixed files go in the repo to install on the user's computer · to work out in spec.

## Intake updates (29 Sep 2026, 17:07–17:08, Koko)
- Name: Docs Librarian (Koko chose between "Librarian" and "Docs Librarian"; "Librarian" is taken on the marketplace). Working name, final after a marketplace check.
- Inbox check frequency: deferred to the user at onboarding; the bot explains each check burns tokens; suggest daily as a default.
- Must never do (Koko's words): Always retrieve what the policy says but never advise. Have an opinion but don't push any one way or the other; act in the user's best interest. Never guess. Never lie. Never hallucinate. Always reference the documentation. Never delete unless the user expressly asks. Never send emails on behalf of the user unless the user expressly clicks send.
- Tone and length (Koko, 17:18): Get to the point; always focus on getting the user their answer in a clear, succinct way. For a question like "does any credit card policy cover car hire insurance?", check every policy that could possibly contain it, then reply with the answer first, followed by a brief account of the process (e.g. "I reviewed these policies …").
- Routines (Koko, 17:19): all routines start OFF. The bot always asks the user which ones they want on and turns each on only with their approval, to avoid token burn. Suggested set (mine, not yet confirmed): inbox check (user-chosen frequency), renewal alert 30 days before renewal/expiry, monthly look-ahead (only if something is coming up).

## Update 29 Sep 2026, 17:38
- Routines: all start OFF; bot asks during setup which to switch on, and switches each on only with user approval (token burn).
- Sheet layout AGREED: Google Sheet index, one row per document (name, type, provider, start date, renewal date, provider contact, file link) + Renewals tab sorted by date. Files stay in the user's chosen folder.
- Connections AGREED (17:45): must-have Gmail + Google Sheets; Google Drive must-have only if user picks cloud storage; Google Calendar nice-to-have (renewal dates).
- Disclaimer AGREED (17:46): none at all. No disclaimer line anywhere.
- "Working" AGREED (17:46): (1) finds every policy/contract in a real inbox back 5 years, files each with a Sheet row; (2) every answer quotes the clause + links the document; (3) flags renewal 30 days ahead and asks renew or cancel.
- Example chats: 3 drafts sent 17:46 (car hire cover, new signup save, renewal alert); awaiting Koko's OK.
- NEW (20:30) Koko idea: at renewal, offer to compare what else is out there for a better price. Proposed: offer only (never automatic, token warning); bot checks alternatives itself via web search, compares cover like-for-like against current policy clauses, shows published prices where available, links comparison sites for exact quotes; neutral, no pushing. Pending Koko confirm.
- Example chats AGREED (20:37): all 3 drafts approved as written.
- Messages 1 & 2 AGREED (20:38) as drafted. Renewal comparison treated as agreed (Koko "Yes this is great" answering both questions); flagged to her to correct if not.
- INTAKE COMPLETE 29 Sep 2026 20:38. Next: spec, name check, repo, build.
- (20:39) Koko asked when the index is created and how user is told. Proposed: create empty Sheet during setup right after message 2 (before search), send link; fill as docs found with progress updates in batches; end-of-search summary with counts by type + next renewals + link; each later new doc confirmed in one line with row link. Pending confirm.
- Index timing AGREED (20:40) as proposed above.
- Exact approved text of messages 1–2 and example chats 1–3 recorded in SPEC.md Appendix A (20:45).
- Goal line AGREED (21:22, Koko's words): "It's a library that organises your documents including contracts, policies, and any long form document you may need to reference or review in the future. Instantly query these documents." Scope widened: any long-form document.
- Goal line FINAL (21:23): "A library for your contracts, policies and any long document you might need to look back at. It files them straight from your email, keeps them organised, tracks your renewals, and gives you an instant answer to anything you ask about them."
