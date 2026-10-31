# Decision Log

One line per key trade-off: what was decided, why, and why the alternative was not chosen.
New decisions are appended at the top; old decisions are never quietly changed — a change is
written as "superseded by" with the original text kept.

## 001 (2026-10-31): Serve the buyer only; ranking is decoupled from revenue

- Decision: Ranking factors contain buyer interests only (total price, delivery, reputation);
  affiliate commissions and ad revenue are disclosed truthfully and never enter ranking.
- Why: The core of Collison's post is "which side the agent is on". Once ranking can be
  influenced by payment, this project turns from a buyer tool into just another ad slot.
- Alternative (not chosen): A composite value score — opaque, unauditable by users. Rejected.

## 002 (2026-10-31): The same-product key is the identifier, not title similarity

- Decision: Only matching UPC / EAN / MPN / official SKU counts as the same product;
  similar titles go to the "suspected same product" appendix table.
- Why: Title similarity will inevitably fail on variants, refurbished units, and regional
  versions; one failure can make someone buy the wrong thing.
- Alternative (not chosen): Pure title / image matching — high recall but uncontrollable
  precision. Rejected.

## 003 (2026-10-31): Compare first, do not order yet; ordering needs a separate approval round

- Decision: Phases 1–2 compare prices and send alerts only; Phase 3 ordering requires a
  separate approval, with the constraints file written first.
- Why: Spending money is irreversible; get comparison right and earn trust first, then
  talk about ordering.
- Alternative (not chosen): Building ordering from day one — too much risk and compliance
  cost. Rejected.

## 004 (2026-10-31): Data sources follow the tier "official API > catalog > structured data > browser verification"

- Decision: A channel that is blocked or prohibited by ToS stops there — no bypassing
  verification, no fake identity.
- Why: Adversarial scraping would kill the project on legal and ban risk; an open-source
  project must above all withstand scrutiny.
- Alternative (not chosen): Scraping everything — higher short-term coverage, unsustainable
  long-term. Rejected.

## 005 (2026-10-31): Default market is the United States; first category is standardized electronics models

- Decision: Shipping, tax, and merchant lists follow US conventions first; the first category
  is model-based products whose identifiers are easiest to align.
- Why: A narrower scope is the only way to get same-product accuracy up; spread too thin and
  the first version compares nothing accurately.
- Status: Pending user confirmation — changing market or category takes one sentence.
- 2026-10-31 note: The user said "start" without changing the defaults, so Phase 1 has
  proceeded on these defaults (US market, standardized electronics models).

## 006 (2026-10-31): Phase 1 covers currently-selling mainstream new products only; no secondhand tracking for now

- Decision: The Phase 1 eval set is limited to mainstream new products
  currently on sale. Used, refurbished, and open-box markets are
  explicitly out of scope for Phase 1; they may be revisited later as
  a separate decision, not silently added.
- Why: Secondhand pricing is far more complex (condition grading,
  seller variance, no stable SKU identity), and mixing it into new-unit
  rankings would corrupt the "same product" guarantee before it is proven.
- Consequence: Entries that stop being sold new at major retailers
  (e.g. MacBook Air 13 M4, confirmed discontinued-new at Best Buy and
  B&H on 2026-10-31) are flagged for review against this criterion;
  whether they are replaced by current-generation successors is a
  separate user decision, not an automatic substitution.

## 007 (2026-10-31): Repository language is English only; market is the United States

- Decision: All repository content (docs, code comments, CLI output,
  snapshot metadata) is written in English, targeting US consumers.
  This confirms and closes the open item in decision 005: the market
  is the United States and the language is English.
- Why: The product and its future service target US consumers; a
  single-language public repository avoids mixed-language drift and
  keeps every claim auditable by its audience.
- Consequence: Existing Chinese text in docs and code is translated
  to English in one pass; new content must be written in English.
