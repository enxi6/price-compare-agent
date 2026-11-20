# Track F — samsung.com sweep (batch-6 rework, 2026-11-20)

- **Date:** 2026-11-20
- **Scope:** samsung.com current mainstream lineup, ONLY in categories the catalog already carries (no TVs, appliances, SSDs). Site order: lenovo.com → samsung.com → asus.com; Samsung is the second site.
- **Catalog state:** 450 models in `price_agent/catalog.py` (21 Samsung). Batch-6 draft (`data/candidates_batch6_500.md`) already carries 4 Samsung: SmartTag 2, HW-Q800F, HW-QS700F, Odyssey G5 G55H 27".
- **Method:** `browser.search` / `browser.open` text fetch only. Every candidate checked by key, model name, MPN, and UPC against the 450-model catalog. US-market only; seller-direct or retailer-direct only; no Amazon as a source in any form; no eBay; no marketplace/third-party sellers. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant/config. Qualifying: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, CDW spec, Newegg spec, Best Buy spec panel, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators, price-tag photos, Q&A pages, search snippets alone.
- **Result: 9 Samsung picks carried + 1 weaker 10th pick.** Three picks have BOTH MPN and UPC VERIFIED (HW-Q600F, HW-S60D, Galaxy Buds3 Silver) — the strongest identifier evidence in the batch-6 rework so far. The other picks have MPN VERIFIED with UPC pending, except the G5 32" (both pending) and the Watch7 44mm (10th pick, weakest).
- **Prices are Black Friday-season snapshots (2026-11-20).** Best Buy Black Friday deals end Nov 28, 2026; Samsung.com Black Friday sale runs through Nov 30, 2026. Re-verify every price/stock state at add time.

## Picks carried (10)

### F1. Samsung HW-Q600F — Black (Q-series 3.1.2ch, 2025)
- **Key:** `samsung-hw-q600f-black`
- **Category:** soundbars
- **Variant pinned:** Black, Titan Black, HW-Q600F/ZA
- **Membership:** NOT in catalog (catalog has HW-Q990F only; HW-Q800F and HW-QS700F are in the batch-6 draft, distinct models). No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung 2025 Q-series soundbar; Best Buy direct Black Friday row + B&H in-stock row + samsung.com InStock.
- **Identifiers:**
  - MPN HW-Q600F/ZA — **VERIFIED** (Best Buy model field + B&H product page + samsung.com listing).
  - UPC 887276936895 — **VERIFIED** (B&H spec page + Walts TV spec page + Worldwide Stereo spec page + ChannelOnline distributor spec, all agree). NOTE: Amazon lists a CONFLICTING UPC 887276835426 for this model — Amazon is non-qualifying and the value is disregarded; do not use it.
- **Price / stock:** Best Buy $399.99 Black Friday (comp $699.99), sold by Best Buy; B&H $397.99 In Stock (was $697.99); samsung.com $699.99 InStock.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Strongest pick in this sweep (both identifiers verified, three live direct rows).

### F2. Samsung HW-S60D — Black (S-series 5.0ch all-in-one, 2024)
- **Key:** `samsung-hw-s60d-black`
- **Category:** soundbars
- **Variant pinned:** Black, HW-S60D/ZA
- **Membership:** NOT in catalog. No key/MPN/UPC collision. (Note: HW-LS60D Music Frame is a different model already in the catalog — do not mix; the S60D is the all-in-one soundbar, the LS60D is the Music Frame speaker.)
- **Why it qualifies:** Mainstream Samsung all-in-one Dolby Atmos soundbar; Best Buy direct Black Friday row + B&H row.
- **Identifiers:**
  - MPN HW-S60D/ZA — **VERIFIED** (Best Buy model field HW-S60D + B&H product page HW-S60D/ZA + Samsung official spec sheet).
  - UPC 887276823935 — **VERIFIED** (B&H spec page + Samsung official HW-S60D spec sheet, UPC CODE: 887276823935, agree). (Canadian /ZC variant has a different UPC 887276824543 — pin the US /ZA only.)
- **Price / stock:** Best Buy $279.99 Black Friday (comp $399.99; some crawls show $330.00), sold by Best Buy, Add to cart; Slickdeals confirms Best Buy $279.99 (2026-11-05).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Joint-strongest pick (both identifiers verified).

### F3. Samsung Galaxy Buds3 — Silver
- **Key:** `samsung-galaxy-buds3-silver`
- **Category:** earbuds
- **Variant pinned:** Silver, SM-R530NZAAXAR
- **Membership:** NOT in catalog (catalog has Buds3 Pro Silver, Buds3 FE Black, Buds4, Buds4 Pro — the base Buds3 is distinct). No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung earbuds (2024, still current); Best Buy direct new row + B&H in-stock row.
- **Identifiers:**
  - MPN SM-R530NZAAXAR — **VERIFIED** (Best Buy model field + B&H product page + Micro Center spec Mfr Part # + Abt page, all agree).
  - UPC 887276868059 — **VERIFIED** (B&H spec page + Micro Center spec + Abt page, all agree). NOTE: Swappa ties a DIFFERENT UPC 887276880938 to MPN SM-R530NZAWXAR (W-variant) — different variant code, disregarded for this pin; eBay also shows 887276880990 for White — eBay is non-qualifying.
- **Price / stock:** Best Buy $109.95 InStock (new, SKU 12901715; earlier crawl $109); B&H $124.95 In Stock (was $174.95); Micro Center $49.99 but OutOfStock (do not use as the row).
- **Flag:** Best Buy also lists a refurbished Excellent unit ($84.99, sold by Elite Tech LLC, marketplace) under a different SKU — pin the new SKU 12901715 only and confirm sold-by-Best-Buy at add time. Joint-strongest pick (both identifiers verified).

### F4. Samsung Galaxy Watch7 40mm BT — Cream
- **Key:** `samsung-galaxy-watch7-40mm-cream`
- **Category:** wearables
- **Variant pinned:** Cream, 40mm BT, SM-L300NZEAXAA
- **Membership:** NOT in catalog (catalog has Watch8, Watch8 Classic, Watch9, Watch Ultra2 — no Watch7). No key/MPN/UPC collision.
- **Why it qualifies:** Prior-generation Samsung watch, still current at retail; Best Buy direct Black Friday row.
- **Identifiers:**
  - MPN SM-L300NZEAXAA — **VERIFIED** (Best Buy model field + Samsung official Wearables MSRP Price Lists, Mar/Jun/Jul/Sep 2026 editions, all agree).
  - UPC 887276868912 — PENDING (strong lead: Samsung official Wearables MSRP Price Lists, Mar/Jun/Jul/Sep 2026 editions, all agree SM-L300NZEAXAA = Galaxy Watch7 BT 40mm Cream, UPC 887276868912, MSRP $249.99 — but that is one publisher; a second qualifying source, e.g. a B&H/Abt retailer spec page printing the same UPC, was NOT found in-session. Do not mark VERIFIED until that second source is found.)
- **Price / stock:** Best Buy $149.99 Black Friday (list $249.99), sold by Best Buy in the Green-variant crawl; Cream crawl shows $149.99 Black Friday Deal. Re-verify seller + stock at add time.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Prior generation (2024) superseded by Watch8/Watch9, but still sold new by Best Buy — not clearance (no clearance tag on the new row).

### F5. Samsung Galaxy Book5 15.6" — Silver (Core Ultra 7, 16GB, 512GB)
- **Key:** `samsung-galaxy-book5-15-6-ultra-7-512gb-silver`
- **Category:** laptops
- **Variant pinned:** Silver, 15.6" FHD IPS, Core Ultra 7 255U, 16GB, 512GB, NP750XHD-KB1US
- **Membership:** NOT in catalog (no Samsung laptop in the catalog at all). No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung laptop (2025); Best Buy direct Black Friday row.
- **Identifiers:**
  - MPN NP750XHD-KB1US — **VERIFIED** (Best Buy model field + Newegg spec page Model Number, agree).
  - UPC PENDING, no qualifying lead — eBay shows 198957212345 for this MPN, but eBay is non-qualifying; treat only as an unverified lead, never as verified.
- **Price / stock:** Best Buy $799.99 Black Friday (comp $1,299.99), sold by Best Buy. Newegg lists the same model at $1,228.99 but sold by DemProductSales (marketplace — not usable as a row).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. First Samsung laptop in the set if added. Do NOT confuse with Galaxy Book5 360 NP750QHA-KA1US (touch AMOLED 2-in-1, different model — see backlog/skipped).

### F6. Samsung Odyssey G7 G70D 32" — Black (4K UHD IPS, 144Hz)
- **Key:** `samsung-odyssey-g7-g70d-32-black`
- **Category:** monitors
- **Variant pinned:** Black, 32", LS32DG702ENXZA
- **Membership:** NOT in catalog (catalog has Odyssey G70F 27" and G9 G91F 49" — different models). No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung 4K gaming monitor; Best Buy direct row.
- **Identifiers:**
  - MPN LS32DG702ENXZA — **VERIFIED** (Best Buy model field + Samsung official monitor-offer Terms & Conditions Exhibit A: "LS32DG702ENXZA 32 Inch Odyssey G7 G70D", agree).
  - UPC PENDING, no lead found.
- **Price / stock:** Best Buy $799.99 new, sold by Best Buy (open-box $703.99–$731.99 also listed). samsung.com lists $599.99 but OutOfStock — do not use as the row.
- **Flag:** samsung.com is OOS, so the row is Best Buy only. Price $799.99 is list-ish, not a Black Friday deal — re-check at add time.

### F7. Samsung Odyssey OLED G7 G73SH 32" — Black (Dual Mode 4K 165Hz / FHD 330Hz, 2026)
- **Key:** `samsung-odyssey-oled-g7-g73sh-32-black`
- **Category:** monitors
- **Variant pinned:** Black, 32", LS32HG732SNXZA
- **Membership:** NOT in catalog (catalog has Odyssey G70F 27" and G9 G91F 49" — different models; distinct from F6 G70D IPS). No key/MPN/UPC collision.
- **Why it qualifies:** New 2026 Samsung OLED gaming monitor; Best Buy direct row + Newegg spec row.
- **Identifiers:**
  - MPN LS32HG732SNXZA — **VERIFIED** (Best Buy model field + Newegg spec page + Samsung official monitor-offer Terms & Conditions Exhibit A: "LS32HG732SNXZA 32 Inch Odyssey OLED G73SH", agree).
  - UPC PENDING, no lead found.
- **Price / stock:** Best Buy $699.99, Add to cart; Walmart $699.99 (sold by Walmart per listing). Macy's also $699.99 per a deal post.
- **Flag:** 2026 model, first discount cycle — price may move. Do not confuse with the G70D (F6, IPS) or the G80SD/G8 (clearance — see skipped).

### F8. Samsung HW-QS750F — Titan Black (Q-series 5.1.2ch, sub + rears, 2025)
- **Key:** `samsung-hw-qs750f-black`
- **Category:** soundbars
- **Variant pinned:** Titan Black, HW-QS750F/ZA
- **Membership:** NOT in catalog (catalog has HW-Q990F; HW-QS700F is in the batch-6 draft — the QS750F is the 5.1.2ch version with rear speakers, the QS700F is 3.1.2ch without rears; distinct models). No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung 2025 soundbar; Best Buy direct row.
- **Identifiers:**
  - MPN HW-QS750F/ZA — **VERIFIED** (Best Buy model field + Samsung official Simple User Guide for HW-QS700F / HW-QS750F naming the model, agree on the model code; /ZA suffix from Best Buy only).
  - UPC PENDING — only Canadian sources found: Canex lists HW-QS750F/ZC with UPC 887276955315; McNain TV same. The US /ZA UPC was NOT confirmed by two qualifying sources. Do not carry the /ZC UPC as the US value.
- **Price / stock:** Best Buy $599.99 (Titan Black). An older Best Buy crawl (261 days) showed $1,399.99 — price has dropped sharply; re-verify at add time.
- **Flag:** Price history is steep ($1,399.99 → $599.99); re-check at add time. UPC pending.

### F9. Samsung Odyssey G5 G55H 32" — Black (QHD, 180Hz, curved)
- **Key:** `samsung-odyssey-g5-g55h-32-black`
- **Category:** monitors
- **Variant pinned:** Black, 32", LS32HG554ENXZA
- **Membership:** NOT in catalog; distinct from the batch-6 draft's Odyssey G5 G55H 27" (LS27HG552ENXZA, entry 29) — different size and different model code. No key/MPN/UPC collision.
- **Why it qualifies:** Mainstream Samsung curved gaming monitor; Best Buy direct Black Friday row.
- **Identifiers:**
  - MPN LS32HG554ENXZA — PENDING (single source, Best Buy model field). NOTE: LS32HG552ENXZA is NOT this model — 552 is the 27" (LS27HG552ENXZA); the 32" is LS32HG554ENXZA. Do not mix.
  - UPC PENDING, no lead found.
- **Price / stock:** Best Buy $189.99 Black Friday (comp $289.99), sold by Best Buy; Slickdeals confirms Best Buy $189.99 (2026-11-09).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Identifier pending (both). Weakest of the strong picks, but a clean direct row at a mainstream price.

### F10. Samsung Galaxy Watch7 44mm BT — Green (weakest pick, sibling size)
- **Key:** `samsung-galaxy-watch7-44mm-green`
- **Category:** wearables
- **Variant pinned:** Green, 44mm BT, SM-L310NZGAXAA
- **Membership:** NOT in catalog. No key/MPN/UPC collision. Sibling size of F4 (40mm Cream) — different model code, different size, distinct entry.
- **Why it qualifies:** Same family as F4; Best Buy direct row, sold by Best Buy.
- **Identifiers:**
  - MPN SM-L310NZGAXAA — PENDING (single source, Best Buy model field; Samsung MSRP list presumably carries it but the 44mm UPC/MPN row was NOT captured in-session — do not upgrade without a second source).
  - UPC PENDING, no lead captured in-session.
- **Price / stock:** Best Buy $279.99 new, sold by Best Buy (some crawls show $249.00/$249.99 — price varies; re-check at add time).
- **Flag:** Weakest pick: both identifiers pending and a sibling-size duplicate of F4. Carry ONLY if a 10th Samsung slot is needed; first to drop if the batch needs trimming. If dropped, move to the backlog.

## QUEUED SAMSUNG BACKLOG (verified or well-evidenced, not carried — cap / slot reasons)

### B1. Samsung Galaxy Watch7 40mm BT — Green (SM-L300NZGAXAA)
- Sibling color of F4. Best Buy $249.99, sold by Best Buy. MPN from Best Buy model field; UPC 887276868905 per Samsung official Wearables MSRP Price Lists (Mar/Jun/Jul/Sep 2026 editions agree) — same single-publisher caveat as F4, needs a retailer spec second source. Strongest backlog item.

### B2. Samsung Galaxy Book5 360 15.6" — Gray (NP750QHA-KA1US)
- Touch AMOLED 2-in-1, Core Ultra 7 256V, 16GB, 512GB. Best Buy model NP750QHA-KA1US confirmed. Price signals conflicted across crawls ($358.99 Q&A page, $1,349.99 comp, one crawl "Unavailable") — no clean price captured in-session. MPN single-source. Backlog until a clean Best Buy direct price is captured.

### B3. Samsung Smart Monitor M7 M70F 32" — White (LS32FM703UNXZA)
- 2026 model, 4K Smart Monitor with Vision AI. Abt $299.99 (Abt is a qualifying retailer). No Best Buy row found in-session; MPN single-source (Abt); UPC not found. Backlog until a second identifier source and a Best Buy row are confirmed. Do NOT confuse with M70B (older, Best Buy $399.99 Sold Out) or M70D (LS32DM702UNXGO, Amazon-heavy signals).

### B4. Samsung Odyssey OLED G6 G60SD 27" — Silver (LS27DG602SNXZA)
- Best Buy model confirmed; new row $639.99 but the same listing shows "Clearance $179.99, Save $720, Comp. Value $899.99" — clearance signals are contradictory with the $639.99 new price and the model looks to be clearing out. Held out of the picks on the clearance rule; backlog only if the clearance signal resolves to a clean new row.

### B5. Samsung Odyssey OLED G8 G80SD 32" — Silver (LS32DG802SNXZA)
- Best Buy model confirmed, sold by Best Buy, $1,169.99 — but tagged Clearance in repeated crawls (was $1,399.99, open-box $608.99–$689.99). Clearance-only signal; fails the rule for batch 6. Backlog only if a clean non-clearance row appears.

### B6. Samsung HW-B650/ZA — Black (3.1ch, 2022)
- Best Buy model HW-B650/ZA, SKU 6505155, sold by Best Buy, $359.99 — but the new price is tagged "Clearance" in repeated crawls; 2022 model. Clearance-only signal; fails the rule. Backlog only if a clean non-clearance row appears.

### B7. Samsung Galaxy Watch Ultra (gen 1, SM-L705) — Titanium Silver/Gray
- NOT researched in-session beyond noting the catalog carries the Watch Ultra2 (SM-L715). The gen-1 Ultra (2024, $649.99 list) is plausibly still at retail, but no Best Buy row or identifier check was run. Backlog as an unresearched lead, not an evidenced find.

### B8. Samsung Galaxy Buds2 Pro — (SM-R510)
- NOT researched in-session. Older (2022) model, likely clearance/discontinued signals. Backlog as an unresearched lead only.

### B9. Samsung Galaxy Tab S10 FE 256GB — Gray (SM-X520 8+256GB)
- NOT researched in-session. The 128GB (SM-X520NZAAXAR) is in the catalog; the 256GB config is a plausible distinct config variant, but no retailer row or identifier check was run. Backlog as an unresearched lead only.

## Checked and skipped (with reasons)

- **Galaxy Buds4 / Buds4 Pro / Buds3 FE** — already in catalog (verified). Skipped.
- **Galaxy Buds3 Pro Silver** — already in catalog. Skipped.
- **Galaxy Watch8 40mm / 44mm Graphite** — already in catalog (verified). Skipped.
- **Galaxy Watch8 Classic 46mm Black (SM-L500NZKAXAA)** — already in catalog (verified). Skipped.
- **Galaxy Watch9 40mm / 44mm Graphite** — already in catalog (verified). Skipped.
- **Galaxy Watch Ultra2 47mm Titanium Silver** — already in catalog. Skipped.
- **Galaxy Tab S11 128GB Gray (SM-X730NZAAXAR)** — already in catalog (exact key). Skipped.
- **Galaxy Tab S11 Ultra 256GB Gray** — already in catalog. Skipped.
- **Galaxy Tab S10 FE 128GB Gray / S10 FE+ 128GB Gray / S10 Lite 128GB Gray** — already in catalog. Skipped.
- **Galaxy Tab A11+ 128GB Gray** — already in catalog. Skipped.
- **Galaxy Ring Size 9 Titanium Black** — already in catalog. Skipped.
- **Samsung Music Frame (HW-LS60D)** — already in catalog. Skipped (do not confuse with HW-S60D, pick F2).
- **Samsung HW-Q990F** — already in catalog. Skipped.
- **Samsung Odyssey G70F 27"** — already in catalog. Skipped.
- **Samsung Odyssey G9 G91F 49"** — already in catalog. Skipped.
- **Samsung Galaxy SmartTag 2 — Black** — already in the batch-6 draft (entry 26). Skipped per brief.
- **Samsung HW-Q800F** — already in the batch-6 draft (entry 27). Skipped.
- **Samsung HW-QS700F** — already in the batch-6 draft (entry 28). Skipped.
- **Samsung Odyssey G5 G55H 27" (LS27HG552ENXZA)** — already in the batch-6 draft (entry 29). Skipped; the 32" sibling is pick F9.
- **Samsung HW-Q700F** — not a real model: searches return HW-QS700F (already in draft) and HW-QS750F (pick F8). No HW-Q700F listing found. Skipped.
- **Samsung HW-C450/ZA** — discontinued signals: Abt "no longer available"; only refurb/open-box/eBay/woot reconditioned rows. No clean US retailer-direct new row. Skipped.
- **Samsung HW-B650/ZA** — clearance-only at Best Buy ($359.99 tagged Clearance, 2022 model). Skipped (see backlog B6).
- **Samsung Galaxy Watch FE (SM-R861)** — EOL: Samsung's March 2025 US MSRP file marks the FE models EOL; no Best Buy US row found (only Best Buy Canada). Skipped.
- **Samsung Galaxy Tab A9+ (SM-X210)** — EOL: Samsung's December 2025 US MSRP document lists A9+ configs as end of life; Best Buy rows are clearance/open-box ("no longer available in new condition" for Navy 64GB). Superseded by Tab A11+ in catalog. Skipped.
- **Samsung Smart Monitor M8 M80D 32" (LS32DM801UNXZA)** — clearance-only: Best Buy standalone listing shows "Clearance $191.99, Save $508, Comp. Value $699.99" + Unavailable. Skipped. (Note: a 2026 M80F exists per 9to5Toys at $400, but no Best Buy row was verified in-session.)
- **Samsung Smart Monitor M7 M70B 32" (LS32BM703UNXZA)** — Best Buy $399.99 Sold Out. Skipped; the 2026 M70F is backlog B3.
- **Samsung Odyssey OLED G6 G60SD 27" (LS27DG602SNXZA)** — clearance signals ($639.99 new vs "Clearance $179.99"). Skipped (see backlog B4).
- **Samsung Odyssey OLED G8 G80SD 32" (LS32DG802SNXZA)** — clearance-only ($1,169.99 tagged Clearance). Skipped (see backlog B5).
- **Samsung Galaxy Book5 360 (NP750QHA-KA1US)** — price signals conflicted/unavailable; no clean row captured. Skipped (see backlog B2).

## Counts
- Models researched in-session: 20 (Buds3, Watch7 40mm, Watch7 44mm, Watch FE, Tab A9+, HW-Q600F, HW-B650, HW-S60D, HW-C450, HW-Q700F, HW-QS750F, G6 G60SD, G7 G70D, G7 OLED G73SH, G8 G80SD, G5 G55H 32", M7, M8 M80D, Book5, Book5 360).
- Already-in-catalog or already-in-draft, identified by membership check: 20.
- Total models checked: ~40.
- Picks carried: 10 (3 with both MPN and UPC VERIFIED; 5 with MPN VERIFIED / UPC pending; 1 with both pending; 1 weakest sibling pick).
- Backlog: 9 items (B1–B9), strongest: Watch7 40mm Green, Book5 360, Smart Monitor M70F.
