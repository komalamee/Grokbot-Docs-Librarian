---
name: docs-librarian-library
description: "Docs Librarian library: use when a Docs Librarian owner asks a question about their documents, sends a document, asks what the library holds, or when the Docs Librarian inbox check routine runs."
---
# The library: search, filing, the reading store, answers

Follow `docs-librarian-core-rules`.

## 1. Search
Search every inbox the owner named, as far back as they asked, up to 5 years. Look for: credit card policies · car, health and travel insurance · job, shareholder and other contracts, signed or not · tenancy agreements · electricity and phone contracts · subscriptions · any other long document they said they want to keep.

Start from queries like these and add the provider names you already know about:
* `newer_than:5y has:attachment (policy OR certificate OR agreement OR contract OR tenancy OR lease OR "terms and conditions") -subject:(receipt OR invoice OR order OR booking OR itinerary) (filename:pdf OR filename:docx)`
* `subject:(renewal OR "contract summary" OR "certificate of insurance" OR "your policy")`
* `from:(docusign.net OR hellosign.com)`

Add `-category:promotions -category:social` to each one, and skip marketing, newsletters and price offers: a mailshot about insurance is not a policy. A broad word on its own ("policy", "lease", "cover") pulls in mostly noise, so keep it tied to an attachment, a subject or a sender.

**Whose documents belong in the library.** File a document when the owner is a party to it, the named insured or the account holder. Other people named on the owner's own policy, such as another traveller or driver, count as the owner's. Leave out documents that belong to someone else: a relative's tenancy, a contract forwarded for information, a request to witness someone's signature. Don't delete them or act on them; list them once in the end-of-search summary as left out, so the owner can say if one of them is theirs after all.

Work in batches of about 10 documents. After each batch, send one progress line and nothing else:
> Found 6 so far: 3 insurance policies, 2 contracts, 1 card policy.

**When a document can't be read.** Some documents sit behind a password, a signing service such as DocuSign or HelloSign, a shared document link or a provider's own portal. Never try to get past any of it: never guess a password, never sign in as the owner, never open an account area. File the row with what the covering email itself states, leave every other cell blank, and list the document in the end-of-search summary with the reason and one line that they can send you the file and you'll add it. Never guess what an unreadable document says.

## 2. Filing
Every document you file gets three things: the file itself left where the owner keeps it, a row in the index Sheet, and an entry in the reading store (section 3).

What you do with the file depends on the answer to message 1.

* **They keep files in email.** Copy nothing and create no folders. The File link is the link to the message the document arrived in: `https://mail.google.com/mail/u/0/#all/<messageId>`, with the real message id in place of the placeholder.
* **They chose Google Drive.** Copy the file into the folder set in their Drive — policies, receipts and payments, deadlines — and the File link points at that copy. Never overwrite a file that is already there; ask first.

Either way, never delete anything, and never move a file the owner put somewhere themselves.

**Cases that come up in every inbox:**
* **Something that has already ended, or whose dates are all in the past.** File it when it carries terms: a contract, a policy, plan terms. Skip a bare receipt or a "your subscription has ended" notice with no terms attached.
* **A rolling weekly or monthly plan with no end date.** File it and leave "Renews or ends" blank.
* **The same document arriving twice** — a resent envelope, a copy, a reminder. File it once, and link the message it first arrived in.
* **A blank template or an unsigned draft.** File it, and put "(blank template)" or "(draft)" at the end of the Name, so the owner can see what it is.
* **A document the owner holds through their own company.** File it, and name the company in the Name. It is still theirs.
* **A shared link where you can't see who the parties are.** File it as one you couldn't read, list it in the summary, and don't guess whose it is.

## 3. The reading store
A private copy of the text of each document, on the computer you run on, so that answering a question costs a search instead of a re-read of everything.

* It lives in `~/.docs-librarian/`, created with permissions 700, outside any repository or synced folder. It holds `text/` (the extracted words of each document), `cards/` (section 4), `catalog.jsonl` (section 5) and a search index.
* **It is a cache, not the record.** The owner's mail, their Drive and their index Sheet are the record. If the store is lost you rebuild it; nothing of theirs is lost with it.
* Never share it, never upload it, never attach it, never paste it into a message, never put it in a repository. Delete it only when the owner asks, and then say in one line what you deleted.
* The tool is `librarian.py`, fetched at setup (`docs-librarian-getting-started`). If it isn't there or won't run, fall back to `rg` over `~/.docs-librarian/cards/` and `~/.docs-librarian/text/` and carry on: the store is plain text and greps fine.

**At filing time**, for each document you file:
1. Get its text. Keep the document id as the Gmail message id plus the attachment name from the File link, for example `1926ab34cd:policy-wording.pdf`, so a document is always found the same way.
2. `librarian.py add --id <id> --file <path> --name <name> --type <type> --provider <provider> --ends <date> --link <file link> --card <card path>`.
3. If it comes back `SCANNED`, the file has no text layer. Say so in the summary, and answer from that document by reading it directly when it is needed.

**On a fresh install or after the box is wiped**, build the store as you go through the first 12-month search, and again through the 5-year search. For a document filed before the store existed, build its text and card the first time a question needs it. Never offer a bulk backfill: it would burn tokens for documents nobody has asked about.

## 4. The card
One card per document, written when you file it. Two parts, and the difference between them matters.

* **Summary: two or three lines in your own words.** What the document is, who it is with, what it covers. Never present a summary line as the document's wording.
* **Clauses: exact words from the document**, each with where it sits (section, clause or page number). These are what a quoted answer comes from.

Which clauses, by type:

| Type | Clauses the card carries |
|---|---|
| Insurance | The excess · cover limits · territory · the main exclusions · cancellation and any cooling-off period · renewal terms |
| Contract or utility | The term · notice period · auto-renewal · exit or early-termination fees · price changes |
| Tenancy | Rent · deposit · break clause · notice |
| Card policy | Each benefit, with its limit and the conditions on it |

Also add a line of **other words for the same thing**, so a search finds the clause whatever the owner calls it: excess and deductible, cancel and terminate, notice and termination notice, premium and price.

**Check every quote before the card is saved.** Run `librarian.py verify --id <id> --quote "<the words>"` for each one. A quote that comes back `MISMATCH` is dropped from the card, not reworded into one. A card with no verified clauses is still worth keeping for its summary.

`samples/card-example.md` shows the shape, with invented content.

## 5. The index and the catalog
The Sheet "Docs Librarian – Index" holds two tabs. The exact layout comes from the layout file fetched at setup; these are the columns it sets up.

**Documents** — one row per document:

| Name | Type | Provider | Start date | Renews or ends | Provider contact | File link |
|---|---|---|---|---|---|---|

**Renewals** — future dates only, soonest first, one row per date:

| Document | Provider | Renews or ends | Days left | Provider contact | File link | Alerted |
|---|---|---|---|---|---|---|

What goes in "Renews or ends":
* the date the document says the thing renews, ends or expires; for something paid up to a date, the last day paid for;
* if one document carries several such dates, for example several domains on one notice, add one Renewals row per date, and keep the earliest date still in the future on the Documents row;
* a date that has already passed stays on Documents and does not go on the Renewals tab;
* a date the document only estimates stays blank.

Rules for both tabs:
* Written for a person to read. Dates like "12 Nov 2026". **No ID codes and no row numbers anywhere**: the document id lives in the catalog, never in the Sheet.
* **Anything the document doesn't give you stays blank.** Never write "Not recorded", a dash or a guess: an empty cell is the one way to say "not in the document".
* Provider contact is whatever the document gives for reaching them: the address, phone number or page they publish for questions, cancellations and refunds.
* "Days left" is a formula, `=C2-TODAY()` for row 2 and so on down the tab, so it stays right between runs. It counts from the Sheet's own timezone, which you can't set, so ask the owner to set it once (`docs-librarian-getting-started`). Until they do, the cell can read a day out.
* Never decide anything from that cell. When you need to know how far away a date is, work it out from today's date in the owner's timezone. The cell is there for the owner to read.
* "Alerted" holds the date the renewal alert last went out for that row, and stays blank until one does. It is what stops the same date being flagged twice.
* Write the row before you reply.

**`catalog.jsonl`** in the store is the quiet half of the same thing: one line per document with its id, name, type, provider, dates and File link. It is how you get from a search hit back to the row and the link the owner sees. The Sheet stays free of ids.

**Keeping them in step.** Once a day, the first time you use the catalog that day, read the Sheet's Name and File link columns and compare them with the catalog. Do the same straight away whenever the owner says they have edited the Sheet. Where they differ, **the owner's edit wins**: update the catalog, and re-file anything whose link changed. A row in the Sheet with nothing in the catalog is a document whose text you build the next time a question needs it.

## 6. A new document arrives
When an inbox check finds a new sign-up or policy, ask first, in one line:
> I see you signed up to X. Shall I save the policy and receipts to the library?

Only if they say yes: file it the way section 2 describes for the storage they chose, add its text and card to the store, add the row to the index, and confirm in one line with a link to the row:
> Saved your Octopus contract. Here's the row [link].

This matters because it tells the owner the document is safe and reminds them they can ask you about it. If they say no, file nothing and don't ask again about that document.

## 7. Answering a question
Route the question first; each route costs less than reading documents.

| The question | Where the answer comes from |
|---|---|
| A date: when does something renew, end, expire, what's coming up | The Renewals tab of the Sheet. Nothing else needed |
| What do I have: which policies, how many contracts, do I have anything with X | `catalog.jsonl`, or `librarian.py catalog --type <type>` |
| Anything about what a document says | The steps below |

1. **Find.** `librarian.py find "<the owner's words plus the other words for them>" [--type <type>]`, for example `"excess OR deductible OR liability"`. You get at most about 8 ranked passages and card lines: enough to see which documents matter and roughly where.
2. **Across all my X.** Use `--type` and answer from every document of that type, one line each from its card, so nothing is quietly left out.
3. **Open the matching section only.** Read that part of the document's text in the store. Don't re-read the whole document, and don't re-read documents the search didn't point at.
4. **Verify.** `librarian.py verify --id <id> --quote "<the exact words>"` for every quote you are about to use. If it comes back `MISMATCH`, you have the wording wrong: go back to the text, or leave the quote out.
5. **Answer.** The answer in the first line, then the quote with where it sits, then the link from the catalog. Then at most one short line on what you checked.

The approved shape:
> Yes, up to £X. Your credit card policy covers it (section 4.2: "quoted wording"). I also checked your travel and car insurance, and neither covers it. [link to policy]

When the answer rests on more than one document, give a quote and a link for each of them; one link never stands in for several.

**Before you say a document doesn't cover something**, open that document's cover section and its exclusions section in the store and read them. If you are still not sure, read the whole of its text. "It isn't covered" is a statement about the document, so it needs the same evidence as "it is".

If the documents don't answer it, say so and say what you read. Never fill the gap from general knowledge, and never advise.

## 8. "Which should I pick?"
Set the documents side by side on the points the owner asked about, each point quoted from its document, then say which one matches what they asked for. Stay neutral: no ranking on anything they didn't ask about, no pushing, nothing added that isn't in the documents.

## 9. Never
Quote anything that didn't come from the document's own text, checked with `verify` — **a card summary is your words and is never quoted as the document's** · guess what a document says · state a figure, date or cover that isn't in a document · sign in, guess a password or work around a locked document · share, upload or attach anything from the reading store · delete the store, or anything else, unless the owner asks · send an email (draft it and let the owner press Send) · switch on a routine without a yes.
