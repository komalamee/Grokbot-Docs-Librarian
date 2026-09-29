---
name: docs-librarian-renewals
description: "Docs Librarian renewals: use when a Docs Librarian owner asks about a renewal or an expiry date, when they ask about cancelling, and when the Docs Librarian renewal alert or monthly look-ahead routine runs."
---
# Renewals

Follow `docs-librarian-core-rules`.

## 1. The 30-day flag
30 days before a renewal or expiry date on the Renewals tab of the index, send one message that:
* names the document and the date;
* gives the price change only if a document says what it is;
* asks whether to renew or cancel;
* gives the provider's contact details from the index, so they can act.

The approved shape:
> Your home insurance renews on 12 Nov, in 30 days. The price is going up from £X to £Y. Do you want to renew or cancel? Cancellations go to their contact [email or phone].

Every figure and date is read from the document or the index. If you don't have the new price, leave that sentence out rather than guess it.

If the owner says cancel: point them at the provider's contact details, and draft the message if they want one. You never send it; the owner presses Send. Nothing gets cancelled by you.

## 2. The price comparison: only if they ask for it
Offer a comparison, and never run one on your own. Say what it costs before they decide:
> I can compare what else is out there for this cover. It uses tokens. Want me to?

Only if they say yes:
1. Search the web yourself for alternatives to the cover they hold now.
2. Compare like for like against the clauses in the current policy: the same cover, the same limits, the same excess. Quote the clause you are matching against.
3. Show only prices that are published. Where an exact figure needs a quote, link the comparison site and say so.
4. Stay neutral. Set the options out side by side, say which one matches what they asked for, and don't push any of them.
5. Never say a policy is better or worse in general, and never predict what they will pay.

If they say no, drop it and don't ask again for that renewal.

## 3. The month ahead
When asked what's coming up, or when the monthly look-ahead routine runs, read the Renewals tab and list what falls due, with dates and days left, soonest first. One message. If nothing falls due, say nothing at all in a routine run; in a direct question, say there is nothing coming up.

## 4. The routines
`docs-librarian-renewal-alert` and `docs-librarian-monthly-look-ahead` both start off and are switched on only when the owner says yes to that routine. Their schedules and quiet rules live in `routines.json`. They send at most one message per run and never chase.

## 5. Never
Advise them to renew or cancel · push a provider · quote a price that isn't published · run a comparison without a yes · send or cancel anything on the owner's behalf.
