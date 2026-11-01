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

## 008 (2026-10-31): Discontinued Apple entries are replaced by current-generation successors, user-confirmed

- Decision: The open item left by decision 006 is closed: discontinued
  Apple entries are replaced by their current-generation successors
  (9 replaced, 3 kept; see BUILD_LOG 011 for the full list), rather than
  tracked as clearance items.
- Why: The eval set's purpose is comparing what a buyer can buy new
  today; carrying retired generations would measure clearance pricing,
  not the mainstream new-unit market the project claims to cover.
- Nuance, user-confirmed: the MacBook Pro 14 M6 base (MHWT4LL/A) counts
  as the current model even though it is pre-order until its 2026-11-06
  release, because the M5 base it replaces is already discontinued; its
  entry stays pending (no UPC yet) and cannot enter the matched ranking
  until a retailer listing states the UPC.

## 009 (2026-10-31): Discontinued Galaxy Buds2 Pro replaced by Galaxy Buds4 Pro White, user-confirmed

- Decision: The Galaxy Buds2 Pro entry (samsung-buds2-pro-white) is retired
  and replaced by Galaxy Buds4 Pro White, US version (SM-R640NZWAXAR),
  under the new key samsung-buds4-pro-white. The old key is retired, never
  reused, and no Buds2 Pro quote is carried over.
- Why: The Buds2 Pro US white model is discontinued as new (B&H: "no
  longer available"; no current US listing found 2026-10-31). The user
  chose Buds4 Pro over Buds3 Pro and over dropping the entry. Buds4 Pro
  (released 2026-03-11, MSRP $249.99) is the current generation.
- Identifier: UPC 198957273582 for SM-R640NZWAXAR, agreed by Best Buy
  spec, a distributor catalog (GTIN 0198957273582), and T-Mobile's URL
  sku. The Amazon SM-R640NZWFXAR / 198957273568 listing is a different
  variant and was excluded, as were MEA and Latino Americana suffixes.

## 010 (2026-10-31): Superlight 2 US identifier corrected from 910-006630 to 910-006628

- Correction, not a new model: the eval entry for the G Pro X Superlight 2
  Black changes MPN from 910-006630 to 910-006628 and identifier from EAN
  5099206104525 to UPC 097855177797. The key
  (logitech-g-pro-x-superlight-2-black) does not change, and the two
  $159.99 quotes already collected (Logitech G direct, Sweetwater) stand:
  the Logitech G direct URL already showed 910-006628, so the correction
  makes the entry agree with its own quote instead of contradicting it.
- Why: the 910-006630 pinning came from European retailer listings. Four
  further sources agree 910-006628 is the North American black unit: Abt
  (US) lists Model 910-006628 with UPC 097855177797 and Color Black;
  DirectDial agrees on MFG part and UPC (0097855177797, the same code in
  GTIN-13 form); Best Buy Canada lists Model 910-006628, Black; the
  Logitech G US store URL carries 910-006628. The old 910-006630 / EAN
  5099206104525 reference is recorded here as superseded, not erased:
  it remains a valid European reference for the same mouse.
- Rule applied: an eval set for the US market pins the US identifier;
  a regional identifier is not silently kept once US sources disagree.

## 011 (2026-10-31): Electronics selection references brands' official current-sale catalogs; old-model and secondhand hunting deferred

- Decision: for electronics, the main product selection is built from
  each brand's official current-sale catalog. Hunting old models and
  secondhand units is a later-phase goal, not current work.
- Why: the official catalog is ground truth for what is actually
  current, and it is the most efficient source — the 737, Buds2 Pro,
  and M4-Apple rounds all burned effort on models that had already
  left the official catalog. Old-model and secondhand sourcing needs
  different machinery (marketplace condition grading, regional
  variants, refurbished-vs-new disambiguation) and belongs in its own
  phase, not mixed into the in-sale-new comparison.
- Scope: this confirms and extends DECISIONS 006 (in-sale new only,
  no secondhand/refurbished). It also retroactively justifies
  excluding the 736 Nano II 100W as a 737 successor: it is the 737's
  own generation (2022), not a current-catalog model. Current
  entries that remain in a brand's official catalog (e.g. DualSense
  White, still sold by PlayStation Direct) are unaffected.
