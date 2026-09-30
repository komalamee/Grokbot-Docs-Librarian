# Example card (invented, for reference only)

Nothing here is real. It shows the shape of a card in `~/.docs-librarian/cards/`: a summary in the
bot's own words, then clauses in the document's words, each checked with `librarian.py verify`.

```markdown
# Sunrise Travel Cover 2026 — Sunrise Insurance (example)
id: 1900example11:sunrise-policy-wording.pdf · type: insurance · filed: 30 Sep 2026
link: https://mail.google.com/mail/u/0/#all/1900example11

Summary (my words, not the document's)
A single-trip travel policy for one adult, bought for a trip to Spain in June 2026.
It covers medical costs, cancellation and baggage, and the paid period ends 30 Jun 2026.
The certificate names one traveller and one under-18.

Clauses (the document's words, verified)
- Excess: "An excess of £75 applies to each claim under Section 2." (Section 2, page 4)
- Cover limit: "We will pay up to £5,000,000 for emergency medical treatment." (Section 2.1, page 4)
- Territory: "This policy covers travel within Europe, including Spain." (Definitions, page 3)
- Exclusion: "We do not cover claims arising from winter sports." (Section 9, page 11)
- Cancellation: "You may cancel within 14 days of purchase for a full refund." (Section 12, page 14)
- Renewal: "This is a single-trip policy and does not renew." (Section 12, page 14)

Also called
excess = deductible · cancel = terminate · cover limit = sum insured · territory = area of cover

History
- 30 Sep 2026: filed from the purchase email.
```
