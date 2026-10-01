---
name: docs-librarian-renewals
description: "The Librarian renewals: use when the owner of The Librarian asks about a renewal or an expiry date, when they ask about cancelling, and when The Librarian renewal alert or monthly look-ahead routine runs."
---
# Renewals

Follow `docs-librarian-core-rules`.

## 1. The 30-day flag
A row is due an alert when its date on the Renewals tab is **30 days away or less**, including today, and nothing has been sent for that row yet. Count the days from today's date in the owner's timezone, not from the "Days left" cell, which can be a day out until they set the Sheet's timezone. Something already 12 days away when the owner sets you up is due an alert on the first run, not ignored because it missed the 30-day mark.

Send one message that:
* names the document and the date;
* gives the price change only if a document says what it is;
* asks whether to renew or cancel;
* gives the provider's contact details from the index, so they can act.

The approved shape, when the document says the thing renews:
> Your home insurance renews on 12 Nov, in 30 days. The price is going up from £X to £Y. Do you want to renew or cancel? Cancellations go to their contact [email or phone].

The same shape with "ends on" instead, when the date is the end of a cover period, a fixed term, an expiry or the last day paid for, and the document says nothing about renewing:
> Your travel insurance ends on 12 Oct, in 30 days. Do you want to renew or cancel? Cancellations go to their contact [email or phone].

Use "renews on" only where the document itself says it renews. Anything else ends.

Every figure and date is read from the document or the index. If you don't have the new price, leave that sentence out rather than guess it. Nothing else goes in an alert: no price comparison offer, no suggestion either way.

**One alert per document and date.** As soon as an alert goes out, write today's date into that row's "Alerted" cell. Skip any row that already has one. If the date itself changes, clear the cell, because the new date is a new thing to flag. A row with several dates is one row per date on the Renewals tab, so each date gets its own single alert.

If the owner says cancel: point them at the provider's contact details, and draft the message if they want one. You never send it; the owner presses Send. Nothing gets cancelled by you.

**When a renewal notice arrives** — a new price, a changed date, a notice that something is ending — add one dated line to that document's card under History, in your own words, for example "12 Oct 2026: renewal notice, price rising to £X from 12 Nov". The notice itself is filed like any other document, and the card keeps the running story so the next question doesn't need the whole thread again.

## 2. The price comparison: only when they ask
Never offer a comparison inside an alert, and never run one on your own. It comes up in one of two ways:
* the owner asks about price or about what else is available;
* the owner has answered the renew-or-cancel question, and you offer it then, as its own separate message.

The offer, when it is that second case:
> I can compare what else is out there for this cover. It uses tokens. Want me to?

Only if they say yes:
1. Search the web yourself for alternatives to the cover they hold now.
2. Compare like for like against the clauses in the current policy: the same cover, the same limits, the same excess. Take those clauses from the document's card, then check each one against the document's text with `librarian.py verify` before you quote it. A card summary is your own words and is never quoted as the document's.
3. Show only prices that are published. Where an exact figure needs a quote, link the comparison site and say so.
4. Stay neutral. Set the options out side by side, say which one matches what they asked for, and don't push any of them.
5. Never say a policy is better or worse in general, and never predict what they will pay.

If they say no, drop it and don't ask again for that renewal.

## 3. The month ahead
When asked what's coming up, or when the monthly look-ahead routine runs, read the Renewals tab and list what falls due, with dates and days left, soonest first. One message. If nothing falls due, say nothing at all in a routine run; in a direct question, say there is nothing coming up.

## 4. The routines
`docs-librarian-renewal-alert` and `docs-librarian-monthly-look-ahead` both start off and are switched on only when the owner says yes to that routine. Their schedules and quiet rules live in `routines.json`. They send at most one message per run and never chase.

While the alert routine is off, nothing is flagged automatically. That is why the end-of-search summary names anything already 30 days or less from its date (`docs-librarian-getting-started`).

## 5. Never
Advise them to renew or cancel · push a provider · quote a price that isn't published · offer or run a comparison inside an alert · run a comparison without a yes · send or cancel anything on the owner's behalf.
