# Batch 6 draft — 50 candidates (450 → 500)

- **Date:** 2026-11-20 (first draft); reworked 2026-11-20 (see "Rework 2026-11-20 — site-by-site" below).
- **Catalog state at draft time:** 450 models in `price_agent/catalog.py`, verified identifiers 194 / pending 256, ranking 148, matched 164. Repo HEAD `04ed2bc` (`feat: batch 5 — add 50 models (400 → 450), verified 173 → 194 (DECISIONS 084)`).
- **This batch:** 50 candidates, catalog 450 → 500. Final batch to the user's 500 target.
- **Identifier tally (REWORKED, as approved 2026-11-20): MPN VERIFIED 47 / 50. UPC/EAN VERIFIED 18 / 50 (36%). UPC PENDING 32 / 50.** Before the rework: MPN VERIFIED 1 / 50, UPC verified 0 / 50. Catalog "verified" = UPC/EAN verified (confirmed against the live catalog: all 194 verified models carry a UPC/EAN; 0 verified models lack one; 0 pending models carry one) — so this batch lifts verified identifiers 194 → 212 as approved. (Rework draft said 19/50; the user approved with the TUF M4 Air UPC downgraded to PENDING — see entry 50 — so 18/50.)
- **Brand counts (50):** Sony 4, Logitech 5, JBL 4, Razer 3, Samsung 6, Apple 2, Anker 2, Garmin 4, Lenovo 4, ASUS 7, Dell 1, HP 1, Meta 1, Google 1, HyperX 2, Microsoft 2, Corsair 1. (Bose, Keychron, Alienware: 0 — all three lost their only entries in the rework; see Swaps.)

## Rework 2026-11-20 — site-by-site

**What happened:** the first draft (VERIFIED 1 / PENDING 49, UPC verified 0) was sent back by the user ("打回重做"). The rework ran as 7 parallel research tracks, findings in `data/rework6/` (`trackA.md` Sony/Logitech/JBL re-probes, `trackB.md` Razer/Anker/Garmin re-probes, `trackC.md` Samsung/Apple/ASUS/HP/Dell/Microsoft/Meta/Google/Keychron/HyperX/Corsair/Bose re-probes, `trackD.md` alternates, `trackE_lenovo.md` lenovo.com sweep, `trackF_samsung.md` samsung.com sweep, `trackG_asus.md` asus.com sweep). The method reversed the first draft's mistake: instead of picking 50 models then hunting identifiers, each site was swept and only what verifies was taken. Site order: lenovo.com → samsung.com → asus.com, pivoting as soon as a site stopped yielding verifiable candidates; the batch was filled with the best-verified models across the easiest sites, not padded with brand-direct-only entries.

**Before / after:** MPN VERIFIED 1/50 → **47/50**. UPC/EAN VERIFIED 0/50 → **19/50 (38%)**. That is just short of the ~40% target (batches 4–5: 46% / 42%) — reported honestly, not dressed up. The remaining gap is structural, not effort: after 450 models, UPCs for the next tier of mainstream models are rarely printed on two qualifying spec pages. The lenovo.com sweep yielded **0 UPC-verified** across ~35 models; the 12 UPC-verified swap-ins below were the entire available supply from the three site sweeps plus the alternates track. No rule was loosened to reach 20/50.

**Lenovo.com sweep (track E):** ~35 models/configs checked. The catalog holds only 11 Lenovo keys, all tablets/handhelds — no Lenovo laptop, monitor, or accessory is in the catalog, so every candidate was new by membership. Yield: **7 picks** (4 MPN-VERIFIED: T14 Gen 5 21MC000CUS, Legion Pro 5 Gen 10 83LT000MUS, T16 Gen 4 21QN005XUS, E16 Gen 3 21ST0008US; 2 MPN-PENDING with direct rows: Legion 5i 83LY0000US, IdeaPad 5 83GH000AUS; 1 flagged lenovo.com-only: X1 Carbon 21NS0012US). **UPC verified: 0** — every UPC found is single-source or no-lead. Carried into the batch: 3 new picks (T14 Gen 5, Legion Pro 5 Gen 10, T16 Gen 4) + X1 Carbon kept = 4 Lenovo in the batch. The other 3 picks (E16 Gen 3, Legion 5i, IdeaPad 5) go to the queued Lenovo backlog — Samsung/ASUS verified better and took the slots, per the user's site-order refinement. ThinkVision monitors and docks yielded nothing pickable: every Best Buy ThinkVision listing is marketplace-only. Draft corrections from the sweep: entry 39 (Legion Pro 5 16IRX9) DROPPED — its Best Buy row is now dead ("no longer available in new condition"); entry 40 (T14 Gen 6) moved to backlog — MPN now VERIFIED (CDW + Best Buy) but still no usable direct price row; do NOT attach B&H's UPC 199272842804 to it (belongs to a different config, 21QDS2VV00). X1 Carbon: do NOT attach B&H's UPC 828143670351 (belongs to config 21NTSB8E00).

**Samsung.com sweep (track F):** ~40 models checked. 10 picks carried (3 with both MPN and UPC VERIFIED: HW-Q600F, HW-S60D, Galaxy Buds3 Silver; 5 MPN-VERIFIED / UPC-pending; 1 both-pending; 1 weakest sibling pick). Carried into the batch: the 3 both-verified picks only. Backlog: 9 (strongest: Watch7 40mm Green, Book5 360, Smart Monitor M70F).

**ASUS / ROG sweep (track G):** 65 models checked. 10 picks carried (6 VERIFIED, 4 PENDING). Carried into the batch: the 6 UPC-verified picks (PG32UCDM, RT-BE86U, RT-BE92U, ZenWiFi BT8 2-pack, ZenWiFi BT10 2-pack, TUF M4 Air). Backlog: 13 (strongest: ROG Strix G16 G614PR, XG27UCG, XG27UCSR).

**Alternates (track D):** 3 carried, all with fully VERIFIED MPN+UPC pairs — Surface Laptop 13" (2025), Garmin Fenix 8 Solar, Logitech Signature Slim K950. ULT Tower 10 (MPN VERIFIED, BB $799.99 direct) was not carried — the slots went to UPC-verified picks and the Lenovo 1:1 replacements; it is the strongest non-carried alternate. Alienware 16 Aurora (both identifiers VERIFIED via distributors) is on HOLD — no clean retailer-direct price row exists (all three Best Buy SKUs are marketplace sellers); do not add until a direct row confirms.

**Verification decisions (coordinator's calls, recorded here so they can be re-judged):**
- Distributor second sources ACCEPTED where they match the batch-5 Erikson precedent (retailer + distributor): HW-Q800F / HW-QS700F UPC (B&H + ADI Global Distribution), Nest Hub UPC (Ferguson + Zoro), K950 UPC (B&H + Tech-America distributor — caveat: Tech-America shares a data feed with PC-Canada), ZenWiFi BT10 UPC (B&H + CompSource distributor — caveat: weakest VERIFIED call; confirm on the Best Buy spec panel for SKU 11870821 at add time or downgrade to PENDING), Fenix 8 Solar UPC (Garmin price-list PDF + CompSource), TUF M4 Air UPC (SHI + Zoro).
- Brio 100 UPC 097855188588 ACCEPTED as VERIFIED (B&H + Logitech's own datasheet PDF — the content is verbatim Logitech, though the PDF is hosted on Zoro's static CMS rather than logitech.com; caveat recorded in the entry).
- Venu 3S UPC 753759314774 stays PENDING: Petra + CompSource are both distributors. Distributor + distributor is a step beyond the batch-5 precedent (distributor + retailer), so no upgrade. If the catalog owner accepts distributor + distributor, it becomes VERIFIED.
- Huntsman V3 Pro Mini stays PENDING on both identifiers: the Micro Center leg exists only as a truncated search snippet (MPN) / snippet-only UPC print, and snippets alone are not qualifying. A clean re-fetch of the Micro Center page (id 670527) at add time would likely verify both.
- Kiyo Pro Ultra UPC conflict stays UNRESOLVED: 840272900376 is tied to the Ultra by Amazon/Snapklik and to the Kiyo Pro (RZ19-03640100-R3U1) by eBay listings — no qualifying spec page ties it to either model. Entry dropped.
- Odyssey G5 G55H 27" MPN conflict stays UNRESOLVED: Samsung.com says LS27HG550ENXZA, Best Buy says LS27HG552ENXZA. Entry dropped.
- Oakley Vanguard MPN conflict stays UNRESOLVED: Abt OW8001800105 vs Best Buy 0OW8001 3928 46 vs EU consensus OW8001-05 52. Entry dropped.

**Swaps (15 out / 15 in):**

| Slot | Dropped model | Reason | Replacement | Why it's stronger |
|---|---|---|---|---|
| 1 | Bose Solo Soundbar Series II | MPN single-source, UPC no lead; 2 batches without progress | Samsung HW-Q600F | Both identifiers VERIFIED (B&H + Walts/Worldwide Stereo) |
| 2 | Razer Kiyo Pro Ultra 4K | MPN single-source, UPC conflict unresolved, Best Buy row is 6ave marketplace (not direct) | Lenovo ThinkPad T14 Gen 5 (21MC000CUS) | MPN VERIFIED (B&H + CDW); B&H $1,499 InStock |
| 16 | Razer Kiyo V2 Pro | No qualifying MPN/UPC lead at all; no retailer-direct row | Lenovo Legion Pro 5 Gen 10 (83LT000MUS) | MPN VERIFIED (lenovo.com + Best Buy); replaces dead 16IRX9 with its successor |
| 20 | Anker Soundcore Boom 2 Plus | MPN single-source, UPC no lead, Best Buy row Sold Out | Lenovo ThinkPad T16 Gen 4 (21QN005XUS) | MPN VERIFIED (CDW + Newegg); CDW $1,483.99 InStock |
| 29 | Samsung Odyssey G5 G55H 27" | MPN suffix conflict 550 vs 552 unresolved | Microsoft Surface Laptop 13" (2025) Ocean 512GB | Both identifiers VERIFIED (B&H + Abt); BB $1,149.99 direct |
| 32 | Apple Magic Keyboard (M2) | No retailer-direct new row (Best Buy new = HHGregg marketplace); Apple.com price not captured; MPN is the older keyboard, not M2-exclusive | Garmin Fenix 8 Solar Sapphire 47mm | Both identifiers VERIFIED (Garmin PDF + CompSource); BB $749.99 direct |
| 33 | ASUS ROG Falchion Ace HFX | MPN ASUS-only, UPC no lead | Logitech Signature Slim K950 | Both identifiers VERIFIED (B&H + Logitech datasheet / Tech-America); B&H $69.99 |
| 35 | Dell XPS 14 9440 | Pinned config not available new at Best Buy; price only from a Q&A page | Samsung HW-S60D | Both identifiers VERIFIED (B&H + Samsung spec sheet); BB $279.99 BF |
| 38 | HP 430 Multi-Device Mouse | MPN rests on same-family corroboration only; UPC datasheet-only | Samsung Galaxy Buds3 Silver | Both identifiers VERIFIED (B&H + Micro Center + Abt); BB $109.95 |
| 39 | Lenovo Legion Pro 5 16IRX9 | Best Buy row now dead ("no longer available in new condition"); no second source | ASUS ROG Swift OLED PG32UCDM | Both identifiers VERIFIED (B&H + Micro Center); B&H $1,229 InStock |
| 40 | Lenovo ThinkPad T14 Gen 6 | MPN now VERIFIED but still no usable direct price row (Best Buy marketplace/refurb only) → backlog | ASUS RT-BE86U | UPC VERIFIED (B&H + Micro Center); B&H $239.99 InStock |
| 42 | Meta Oakley Vanguard | MPN format conflict unresolved (Abt vs Best Buy vs EU) | ASUS RT-BE92U | UPC VERIFIED (B&H + Micro Center); BB $265.51 InStock |
| 45 | Keychron K11 Max | Likely discontinued (successor K15 Max); no retailer-direct row; MPN Keychron-family only, UPC no lead | ASUS ZenWiFi BT8 2-pack | Both identifiers VERIFIED (B&H + Micro Center); B&H $449.99 InStock |
| 46 | Keychron Q0 Max | Brand-direct-only; MPN Keychron-family only, UPC no lead | ASUS ZenWiFi BT10 2-pack | UPC VERIFIED (B&H + CompSource, caveat — confirm at add time); B&H $629.99 |
| 50 | Alienware 18 Area-51 | MPN single-source, UPC no lead | ASUS TUF Gaming M4 Air | MPN VERIFIED, UPC DOWNGRADED to PENDING at add time (SHI + Zoro, distributor + distributor — same shape as Venu 3S; user-approved); BB $57.99 |

**Queued backlogs (for later batches — do not force into this one):**
- Lenovo (track E, 7): B1 Legion Pro 7 Gen 10 AMD 83RU0002US (lenovo.com-only $2,799.99, single-source MPN — strongest backlog item); B2 Yoga Slim 7x 83QR000AUS (Best Buy direct $649.99 Holiday Deal, MPN single-source — one second source away from a pick); B3 T14 Gen 6 21QJ00CSUS (MPN VERIFIED, needs a direct price row); B4 T16 Gen 4 21QN0045US (MPN VERIFIED, sibling of the carried T16); B5 LOQ 83VA001PUS (Best Buy direct $1,049.99, single-source MPN + unresolved "2K" vs FHD spec conflict); B6 T14 Gen 5 Gray 21MC000NUS (single-source identifiers, supplier stock); B7 ThinkVision P27u-20 (weak, stale B&H price). Plus the 3 sweep picks not carried: E16 Gen 3 21ST0008US (MPN VERIFIED, CDW $1,212.99 InStock), Legion 5i 83LY0000US (MPN PENDING — needs a direct Walmart check), IdeaPad 5 83GH000AUS (MPN PENDING — Staples question).
- Samsung (track F, 9): B1 Watch7 40mm Green SM-L300NZGAXAA; B2 Book5 360 NP750QHA-KA1US (price signals conflicted); B3 Smart Monitor M70F LS32FM703UNXZA (Abt $299.99); B4 G6 G60SD, B5 G8 G80SD, B6 HW-B650 (all clearance-flagged); B7 Watch Ultra gen 1, B8 Buds2 Pro, B9 Tab S10 FE 256GB (unresearched leads).
- ASUS (track G, 13): strongest — ROG Strix G16 G614PR (Best Buy $1,749.99 BF, no UPC lead), XG27UCG (MPN VERIFIED, UPC single-source, Micro Center in-store-only), XG27UCSR (UPC conflicted). Remainder: XG27UCG Gen2, Delta II White, Keris II Ace White, Scope II 96 White (same-model color variants), BT8 3-pack, BT10 1-pack (pack-size siblings), VG27AQ1A, VG279QM5F (ASUS-direct-only), TUF M3 Gen II (conflicting stock signals), Vivobook S 14 Q423SA (config soup).
- Alternates (track D, not carried): Sony ULT Tower 10 (MPN VERIFIED SRSULT1000, BB $799.99 direct — strongest non-carried alternate); ASUS Zenbook A14 UX3407QA-PS76 (MPN/UPC pending, BB $1,199.99 direct); HP OmniBook 3 14 hz0788dx (MPN/UPC pending, BB $599.99 BF direct); ASUS ROG Zephyrus G14 2025 GA403UM (MPN pending, UPC no lead, BB $2,299.99 — seller/stock unconfirmed); HP OMEN Transcend 14 2025 (MPN/UPC pending, BB $2,824.99 — price volatile); Alienware 16 Aurora (both identifiers VERIFIED, HOLD — no direct price row).

**Membership check (rework):** script `/tmp/batch6_rework_membership.py` vs `/tmp/catalog_ref_450.tsv` (450 rows built from `price_agent/catalog.py`, 2026-11-20). Checks every candidate by exact key, model-name substring (normalized, both directions), MPN, and UPC (including pending leads), plus intra-batch duplicates. **Result: 0 true collisions; intra-batch duplicate keys / MPNs / UPCs: none.** The 4 raw hits are adjudicated siblings / false positives, not duplicates:
- `logitech-signature-m650-l-graphite` vs in-catalog Signature M650 (non-L): M650 L is the larger full-size version, distinct model.
- `razer-huntsman-v3-pro-mini-black` vs in-catalog Huntsman V3 Pro: 60% Mini vs full-size, distinct.
- `garmin-venu-3s-pebble-gray` vs in-catalog Venu 3: 3S is 41mm, Venu 3 is 45mm, distinct.
- `hyperx-cloud-iii-wireless-black` vs in-catalog Cloud II: false positive — "cloud ii" is a substring of "cloud iii" in the normalized match; different generation.
- Track-level sibling adjudications (no script hit, recorded from the findings files): Fenix 8 Solar 010-02906-10 vs catalog Fenix 8 AMOLED Sapphire 010-02904-20 (Solar MIP display vs AMOLED); Surface Laptop 13" 2025 EP2-33432 vs catalog Surface Laptop 13.8" 8th Edition EP2-59028 (different size, chip generation, MPN); Galaxy Buds3 SM-R530NZAAXAR vs catalog Buds3 Pro / Buds3 FE / Buds4 (base Buds3 is distinct); PG32UCDM vs catalog PG32UCWM / PG27UCDM (different panel/size); T14 Gen 5 21MC000CUS vs backlog T14 Gen 6 21QJ00CSUS (different generation); Legion Pro 5 Gen 10 83LT000MUS vs dropped 16IRX9 83DF00A8US (different generation/config); BlackShark V3 vs in-catalog BlackShark V3 Pro (standard vs Pro); Cobra vs in-catalog Cobra Pro (wired vs wireless Pro).

## Method note (read before add time)

- **First draft research was done directly in-session** (2026-11-20, via `browser.search` / `browser.open`). The task brief asked to fan out to parallel child agents, but this session runs at depth 2/2 with `can_spawn=no`, so no children could be spawned. Every per-model detail below traces to the batch-5 draft (`data/candidates_batch5_450.md`), or a search run directly in this session on 2026-11-20. No identifier, price, or SKU was reconstructed from memory or from a compacted summary.
- **Rework research (2026-11-20):** 7 parallel child tracks (A–G above), each writing findings to `data/rework6/track*.md`. Every per-model detail in the reworked entries traces to the first draft, one of those seven findings files (read verbatim), or a search run in this session. No identifier, price, or SKU was reconstructed from a compacted summary.
- **Black Friday direction (added 2026-11-20, applied to this draft):** prefer models with live Black Friday pricing at brand-direct or retailer-direct channels; flag each promo price with its expiry where known. Best Buy Black Friday deals end **Nov 28, 2026** (per Best Buy banners in crawls); Samsung.com's Black Friday sale runs through **Nov 30, 2026** (per dealnews). No rule was relaxed for BF: still US-market, seller-direct only, no Amazon source in any form, no marketplace rows, identifiers VERIFIED only with two qualifying sources.
- **Samsung.com sweep (2026-11-20, first draft):** samsung.com wearables page (JSON-LD, 1 day old) lists Galaxy Watch8 Classic 46mm Black Wi-Fi/Bluetooth $499.99 InStock and Galaxy Watch8 40/44mm $299.99/$329.99 — all already in the catalog (Watch8 Classic verified, SM-L500NZKAXAA; Watch8 40/44mm verified; Watch9 40/44mm also in catalog). Galaxy Buds4 / Buds4 Pro / Buds3 FE already in catalog. Galaxy Tab S11 128GB Gray already in catalog — the exact-key duplicate the membership check caught (see below). Soundbar sweep: samsung.com CA lists HW-QS700F; the US row is Best Buy $347.99 Black Friday (ends Nov 28). HW-QS700F is carried as the Tab S11 replacement (entry 28).
- **Lenovo.com sweep (2026-11-20, first draft):** Legion Go Gen 2 (83N0000AUS; entry $1,099.99, top config $3,081.99) already in catalog (83N0000BUS, pending). Legion Go S SteamOS already in catalog. Legion Pro 7 Gen 10 AMD (83RU0002US, RTX 5070 Ti, $2,799.99 — 39% off est. value $4,562.99, lenovo.com) is NOT in the catalog — swept, not carried: Lenovo-direct-only (DECISIONS 015 concern) and the batch already carries three Lenovo picks; the open slot went to the cleaner Best Buy Black Friday row (HW-QS700F). Legion Pro 7 Gen 10 AMD is the strongest Lenovo-sweep alternate — see "Not carried".
- **Held items from batch 5 — carried 3, dropped 3 (all re-checked 2026-11-20, first draft):**
  - CARRY — Bose Solo Soundbar Series II: Bose.com $199.00 new; Costco $212.99 InStock same-day. Still no retailer spec page for the UPC (batch-5 blocker unresolved) — carried as PENDING. (Rework: DROPPED — see Swaps, slot 1.)
  - CARRY — Razer Kiyo Pro Ultra 4K: Best Buy $429.95. UPC lead 840272900376 still conflicted; successor Kiyo V2 Pro announced 2026-09-24 at $299.99. Carried as PENDING with flags. (Rework: DROPPED — see Swaps, slot 2.)
  - CARRY — Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition: Lenovo.com direct prices confirmed (pin 21NS0012US $1,248.99). Carried as PENDING; Lenovo-direct only, DECISIONS 015 concern. (Rework: KEPT — slot 3, MPN now two-sourced.)
  - DROP — HP 930 Creator Wireless Mouse: HP Malaysia page says Discontinued; Staples OOS everywhere. Confirmed discontinued/OOS.
  - DROP — ASUS ROG Strix XG27ACS: ASUS US $229 OutOfStock still; Newegg $283.99 seller unconfirmed; Walmart $229 seller unknown. No clean US retailer-direct in-stock row.
  - DROP — Corsair NIGHTSABRE Wireless: Corsair.com now OutOfStock at $149.99; worse than batch 5.
- **Membership check (first draft):** script `/tmp/batch6_membership.py` vs `/tmp/catalog_ref_450.tsv` (450 rows built from `price_agent/catalog.py`, 2026-11-20). Checks every candidate by exact key, model-name substring (normalized, both directions), MPN, and UPC. **Final run (after the Tab S11 → HW-QS700F swap): 0 true collisions; intra-batch duplicate keys: none.** The first run caught one true collision — `samsung-galaxy-tab-s11-128gb-gray` matched a catalog row on exact KEY (the Galaxy Tab S11 128GB Gray, SM-X730NZAAXAR, is already in the catalog). It was dropped and replaced with HW-QS700F, and the script was re-run. The 7 remaining hits are adjudicated siblings / false positives, not duplicates:
  - `logitech-signature-m650-l-graphite` vs in-catalog Signature M650 (non-L): M650 L is the larger full-size version, distinct model.
  - `razer-blackshark-v3-black` vs in-catalog BlackShark V3 Pro: standard vs Pro, distinct.
  - `razer-cobra-black` vs in-catalog Cobra Pro: wired vs wireless Pro, distinct.
  - `razer-huntsman-v3-pro-mini-black` vs in-catalog Huntsman V3 Pro: 60% Mini vs full-size, distinct.
  - `anker-soundcore-boom-2-plus-black` vs in-catalog Soundcore Boom 2: Plus vs base, distinct.
  - `garmin-venu-3s-pebble-gray` vs in-catalog Venu 3: 3S is 41mm, Venu 3 is 45mm, distinct.
  - `hyperx-cloud-iii-wireless-black` vs in-catalog Cloud II: false positive — "cloud ii" is a substring of "cloud iii" in the normalized match; different generation.
- **Prices are Black Friday-season snapshots (2026-11-20).** Most Best Buy rows are Black Friday deals ending Nov 28. Re-verify every price and stock state at add time; promo prices will move. Entries flag each promo price and its expiry where known.

## Candidates

### 1. Samsung HW-Q600F — Black [REWORK SWAP-IN — replaces Bose Solo Soundbar Series II]
- **Key:** `samsung-hw-q600f-black`
- **Category:** soundbars
- **Variant pinned:** Black, Titan Black, HW-Q600F/ZA (Q-series 3.1.2ch, 2025)
- **Why it qualifies:** Mainstream Samsung 2025 Q-series soundbar; Best Buy direct Black Friday row + B&H in-stock row + samsung.com InStock. Strongest pick in the Samsung sweep — both identifiers VERIFIED.
- **Identifiers:** MPN HW-Q600F/ZA — **VERIFIED** (Best Buy model field + B&H product page + samsung.com listing). UPC 887276936895 — **VERIFIED** (B&H spec page + Walts TV spec page + Worldwide Stereo spec page + ChannelOnline distributor spec, all agree).
- **Price / stock:** Best Buy $399.99 Black Friday (comp $699.99), sold by Best Buy; B&H $397.99 In Stock (was $697.99); samsung.com $699.99 InStock.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon lists a CONFLICTING UPC 887276835426 for this model — Amazon is non-qualifying and the value is disregarded; do not use it.

### 2. Lenovo ThinkPad T14 Gen 5 — Black (21MC000CUS) [REWORK SWAP-IN — replaces Razer Kiyo Pro Ultra 4K]
- **Key:** `lenovo-thinkpad-t14-gen-5-black`
- **Category:** laptops
- **Variant pinned:** Black, 21MC000CUS — AMD Ryzen 7 PRO 8840U, 16GB DDR5, 512GB SSD, 14" WUXGA 1920x1200 IPS non-touch, Win 11 Pro
- **Why it qualifies:** Strongest pick in the Lenovo sweep. B&H direct in-stock row + CDW in-stock row. Distinct from the backlog T14 Gen 6 (21QJ00CSUS, different generation/config) and from the 21ML0053US touchscreen config (no clean row).
- **Identifiers:** MPN 21MC000CUS — **VERIFIED** (B&H spec page, opened 2026-11-20 + CDW spec page: "MFG#: 21MC000CUS | CDW#: 7941798", same config). UPC 198153286874 — PENDING + lead (B&H only).
- **Price / stock:** B&H $1,499.00 In Stock (direct open, 2026-11-20). CDW In Stock, $1,486.99 advertised (27-day crawl) / $1,811.99 (225-day crawl) — price varies across crawls, re-check at add time. Best Buy has only "Upgraded" IST Computers listings — not usable.
- **Flag:** UPC single-source (B&H only). CDW price needs re-check at add time.

### 3. Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition
- **Key:** `lenovo-thinkpad-x1-carbon-gen-13-aura-edition`
- **Category:** laptops
- **Variant pinned:** 21NS0012US — Intel Core Ultra 7 258V, 32GB LPDDR5X-8533, 1TB SSD, 14" 2.8K OLED 120Hz, Win 11 Pro, Eclipse Black
- **Why it qualifies:** Held from batch 5 (dropped there for marketplace-only Best Buy rows); re-checked 2026-11-20. Lenovo.com direct prices confirmed. **The single flagged DECISIONS 015 brand-direct-only pick in the reworked batch.**
- **Identifiers:** MPN 21NS0012US — **VERIFIED with caveat** (lenovo.com product page, title "… | 21NS0012US", $1,248.99 InStock + Newegg listing page naming 21NS0012US with the same config, search-fetch — the Newegg direct open hit the bot wall, so the leg is one step weaker than a direct open; if a direct-open second source is required, this drops to PENDING + strong lead). UPC PENDING, no qualifying lead — B&H prints UPC 828143670351, but that is for a DIFFERENT config (21NTSB8E00, $2,099.00) — do NOT attach it to 21NS0012US.
- **Price / stock:** Lenovo.com $1,248.99 InStock (JSON-LD, 1-day crawl). Best Buy has only an IST Computers "Upgraded" listing (Model 21NS-Upgraded, $2,399.99) — not a direct row.
- **Flag:** Lenovo-direct only, no clean retailer row found — DECISIONS 015 concern. No retailer-direct row; UPC has no qualifying lead. Carried because the MPN is two-sourced and the lenovo.com price/stock is confirmed live — if the batch prefers zero brand-direct-only entries, drop this one first and fill the slot from the Samsung/ASUS backlogs.

### 4. Sony WF-C700N — Black
- **Key:** `sony-wf-c700n-black`
- **Category:** earbuds
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony noise-cancelling earbuds; Best Buy live Black Friday row.
- **Identifiers:** MPN WFC700N/B — **VERIFIED** (Best Buy model field + Crutchfield "MFR # WFC700N/B" + Abt "Model # WFC700N/B"). UPC 027242925625 — PENDING + lead (Abt only; Amazon agrees but is non-qualifying).
- **Price / stock:** Best Buy $79.99 Black Friday (comp $118) / $119.99 list. B&H page shows "No Longer Available", $118.00, Discontinued — B&H is a source only, not the row.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 5. Sony INZONE H3 — White
- **Key:** `sony-inzone-h3-white`
- **Category:** headphones
- **Variant pinned:** White
- **Why it qualifies:** Mainstream Sony gaming headset; Best Buy White listing exists.
- **Identifiers:** MPN MDR-G300 (rendered MDRG300/W) — **VERIFIED** (Best Buy model field MDRG300/W, SKU 6510365 + B&H "MFR # MDRG300/W" + Crutchfield "MFR # MDRG300/W"). UPC 027242923546 — PENDING + lead (B&H specs page only; Amazon agrees, non-qualifying).
- **Price / stock:** Best Buy $69.99, sold by Best Buy, SKU 6510365 (crawls 3–7 days old; older crawls $79.99 / $119.99). B&H $68.00 In Stock (was $118.00, Holiday Savings $50.00), Add to Cart.
- **Flag:** Price now captured in-session (was missing in the first draft). Conflict noted and ignored: Kawartha TV (Canadian, non-qualifying) lists UPC 027242923522 for MDRG300/W — B&H + Amazon agree on …546.

### 6. Sony HT-A5000 — Black
- **Key:** `sony-ht-a5000-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony 5.1.2 Dolby Atmos soundbar; Best Buy in-stock direct row.
- **Identifiers:** MPN HT-A5000 (rendered HTA5000 by retailers) — **VERIFIED** (Best Buy model field HTA5000 + Crutchfield "MFR # HTA5000"). UPC 656942665540 — PENDING, lead is non-qualifying only (manuals.plus). B&H no longer carries it (replacement page for the HT-A8000).
- **Price / stock:** Best Buy shows two SKUs/prices — $499.99 (SKU 6467455, 10-day crawl) vs $699.99 (SKU 10917148, 3-day crawl). Draft had $499.99 InStock.
- **Flag:** Price conflict — re-check at add time.

### 7. Sony HT-S400 — Black
- **Key:** `sony-ht-s400-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony 2.1ch soundbar; Best Buy in-stock Black Friday row.
- **Identifiers:** MPN HT-S400 (rendered HTS400) — **VERIFIED** (Best Buy model field HTS400 + B&H "MFR # HTS400"). UPC 027242923942 — PENDING, lead is non-qualifying only (Amazon; a Best Buy-spec mirror site also shows it, not qualifying).
- **Price / stock:** Best Buy $199.99 InStock, Model HTS400, SKU 6498905 (1-day crawl). B&H $298.00 In Stock (older crawl).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 8. Logitech G435 — Black
- **Key:** `logitech-g435-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Logitech wireless gaming headset; Best Buy listing live.
- **Identifiers:** MPN 981-001049 — **VERIFIED** (Best Buy model field, SKU 6478273 + Abt "Model # 981-001049"). UPC 097855165763 — **VERIFIED** (Abt "UPC # 097855165763" + Best Buy spec page "Model Number: 981-001049 … UPC: 097855165763").
- **Price / stock:** Best Buy $49.99 (crawls 1 day and 8 days old), Black Friday banner ends Nov 28, 2026. In-stock wording was NOT explicitly captured in the snippets — re-check at add time. Abt's own listing says "no longer available" — Abt is a source only, not the row.
- **Flag:** Price now captured in-session (was missing in the first draft). In-stock wording needs re-check at add time.

### 9. Logitech Brio 100 — Graphite
- **Key:** `logitech-brio-100-graphite`
- **Category:** webcams
- **Variant pinned:** Graphite
- **Why it qualifies:** Mainstream Logitech 1080p webcam; Best Buy direct row.
- **Identifiers:** MPN 960-001580 — **VERIFIED** (Best Buy model field, SKU 6550199 + B&H page slug/title `logitech_960_001580_brio_100_full_hd`). UPC 097855188588 — **VERIFIED with caveat** (B&H spec page "UPC: 097855188588" + Logitech's own datasheet PDF, © 2023 Logitech: "Part # 960-001580 … Bar code 097855188588 (EAN-13)" — the datasheet is hosted on Zoro's static CMS, not logitech.com; the content is verbatim Logitech. If the strictest reading is applied, downgrade to PENDING + lead (B&H)).
- **Price / stock:** Best Buy $39.99, sold by Best Buy, InStock, SKU 6550199. B&H $24.99 In Stock (was $39.99, Holiday Savings $15.00).
- **Flag:** UPC caveat — see Identifiers.

### 10. Logitech Signature M650 L — Graphite
- **Key:** `logitech-signature-m650-l-graphite`
- **Category:** mice
- **Variant pinned:** Graphite, consumer (full-size L)
- **Why it qualifies:** Mainstream Logitech full-size wireless mouse; Best Buy direct Black Friday row. Distinct from in-catalog Signature M650 (non-L, standard size).
- **Identifiers:** MPN 910-006231 — **VERIFIED** (Best Buy model field, SKU 6491142 + Newegg "Model # 910-006231" + NeweggBusiness "Mfr. Part #: 910-006231"). UPC 097855167583 — PENDING + lead (B&H only; Adorama agrees but is not on the qualifying list).
- **Price / stock:** Best Buy $24.99 Black Friday, sold by Best Buy, SKU 6491142, InStock (1-day crawl; another crawl $29.99; list $39.99). Ignore marketplace SKU 13197120 (Gamzi Digital, $90.99) and SKU 10735960 (Electronic Express, $43.99). B&H $29.99 In Stock (was $39.99).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Do not mix: 910-006347 is the for-Business Off-White variant.

### 11. Logitech Zone Vibe 125 — Graphite
- **Key:** `logitech-zone-vibe-125-graphite`
- **Category:** headphones
- **Variant pinned:** Graphite
- **Why it qualifies:** Mainstream Logitech wireless headset; Best Buy direct row. Distinct from in-catalog Zone Vibe 100.
- **Identifiers:** MPN 981-001166 — **VERIFIED** (Best Buy model field + B&H page title "Logitech Zone Vibe 125 Wireless Headphones 981-001166"). UPC 097855175113 — PENDING + lead (Logitech datasheet PDF: "Part # 981-001166 … UPC 097855175113"; Amazon agrees, non-qualifying).
- **Price / stock:** Best Buy $129.99; B&H "No Longer Available", $129.99, Discontinued.
- **Flag:** Zone Vibe Wireless Teams listing (981-001440) is a different model — pin 125 only. Conflict noted and ignored: Snapklik lists UPC 657768069680 for this part number (non-qualifying aggregator, conflicts with datasheet + Amazon).

### 12. JBL Authentics 200 — Black
- **Key:** `jbl-authentics-200-black`
- **Category:** speakers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream JBL home speaker; Best Buy direct Black Friday row.
- **Identifiers:** MPN JBLAUTH200BLKAM — **VERIFIED** (JBL.com "Item#: JBLAUTH200BLKAM" + B&H title + Crutchfield "MFR # JBLAUTH200BLKAM"). UPC 050036396219 — PENDING + lead (B&H specs page only; Amazon/manuals.plus/Snapklik agree, all non-qualifying).
- **Price / stock:** B&H $189.95 In Stock (was $379.95, Holiday Savings $190.00). Abt $189.95, InStock (manufacturer rebate ends 12/05/2026, comp. value $379.95). JBL.com $189.95. Best Buy $189.95 Black Friday (comp $379.95).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 13. JBL PartyBox Encore Essential 2 — Black
- **Key:** `jbl-partybox-encore-essential-2-black`
- **Category:** speakers
- **Variant pinned:** Black, Essential 2
- **Why it qualifies:** Mainstream JBL party speaker; Best Buy direct row plus B&H/Abt rows.
- **Identifiers:** MPN JBLPBENCOREESS2AM — **VERIFIED** (B&H "MFR # JBLPBENCOREESS2AM" + Best Buy model field, SKU 6644260 + Abt title + Dell "Manufacturer Part Number, JBLPBENCOREESS2AM"). UPC 050036411059 — PENDING + lead (B&H only; Walts/NFM agree, not qualifying).
- **Price / stock:** B&H $199.95 In Stock (was $329.95, Holiday Savings $130.00). Best Buy $199.95 InStock, sold by Best Buy, **SKU 6644260** (supersedes the draft's SKU 10209209 @ $329.99). Abt $199.95 InStock (rebate ends 12/05/2026). Crutchfield still shows $329.95 (14-day-old crawl — stale).
- **Flag:** Draft SKU superseded — use SKU 6644260 @ $199.95. Do NOT use Best Buy SKU 12942222 — a bundle with EASYSING mic, sold/shipped by Electronics Expo (marketplace), $329.90. Premium Encore 2 with 2 mics is a different $400 model (JBLPBENCORE22MICAM) — pin Essential 2 only.

### 14. JBL Bar 500 — Black
- **Key:** `jbl-bar-500-black`
- **Category:** soundbars
- **Variant pinned:** Black, original Bar 500
- **Why it qualifies:** Mainstream JBL 5.1ch Dolby Atmos soundbar; Best Buy direct row.
- **Identifiers:** MPN **CORRECTION** — the draft's "BAR-500" is a shortened display name, not the full MPN. Full MPN JBLBAR500PROBLKAM — **VERIFIED** (JBL.com "Item#: JBLBAR500PROBLKAM" + Crutchfield "MFR # JBLBAR500PROBLKAM" + Best Buy model field, SKU 11113238). UPC 050036387743 — PENDING, lead is non-qualifying only (Amazon / Walts / Zoro agree; none is qualifying).
- **Price / stock:** Best Buy $399.95 InStock, SKU 11113238. JBL.com $399.95 in one crawl, $349.95 OutOfStock in a later crawl (2026-11-20).
- **Flag:** JBL.com price flipped $399.95 → $349.95 OutOfStock same day — re-check at add time. Note the JBL.com `-Z` variant (BAR500PROBLKAM-Z) seen on a different JBL.com URL variant. BAR500MK2 / JBLBAR500M2BLKAM is the newer model — pin the original Bar 500. Conflict noted and ignored: manuals.plus lists UPC 094148727882 (non-qualifying, conflicts with the Amazon/Walts/Zoro agreement).

### 15. JBL Tune 520BT — Black
- **Key:** `jbl-tune-520bt-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream JBL on-ear Bluetooth headphones; JBL.com direct row plus Walmart-direct row. Replaces the discontinued Tune 510BT (see "Not carried"). **The first draft's only VERIFIED identifier (MPN).**
- **Identifiers:** MPN JBLT520BTBLKAM — **VERIFIED** (JBL.com manufacturer item# + Best Buy Canada model field, two independent sources; re-confirmed 2026-11-20). UPC 050036394925 — PENDING, lead is non-qualifying only (BJ's Wholesale; Amazon agrees, non-qualifying).
- **Price / stock:** JBL.com $34.95 InStock (Item# JBLT520BTBLKAM); Walmart $34.95 (was $59.95); Target $59.99 OutOfStock.
- **Flag:** Promo price $34.95 vs $59.95 list. Do not mix with the personalized variant T520BTBLKAMCSTM (different item).

### 16. Lenovo Legion Pro 5 Gen 10 — Eclipse Black (83LT000MUS) [REWORK SWAP-IN — replaces Razer Kiyo V2 Pro]
- **Key:** `lenovo-legion-pro-5-gen-10-eclipse-black`
- **Category:** laptops
- **Variant pinned:** Eclipse Black, 83LT000MUS — AMD Ryzen 7 8745HX, RTX 5060 8GB, 32GB DDR5, 1TB SSD, 16" WQXGA 2560x1600 OLED 165Hz
- **Why it qualifies:** Successor to the dropped Legion Pro 5 16IRX9 (entry 39 in the first draft — its Best Buy row is now dead). Best Buy direct row + lenovo.com row. Distinct from Legion Pro 7 (83RU0002US, backlog).
- **Identifiers:** MPN 83LT000MUS — **VERIFIED** (lenovo.com product page, title "… | 83LT000MUS", $2,360.15 InStock + Best Buy model field: Model 83LT000MUS, SKU 6619246, Sold by Best Buy). UPC PENDING, no lead found.
- **Price / stock:** Best Buy direct SKU 6619246, Sold by Best Buy — **price must be re-checked at add time** ($1,179.99 Slickdeals figure is stale, Feb 2026; recent crawls $1,579.99 on this SKU, $1,774.99/$2,449 on sibling SKUs; some sibling SKUs now read "no longer available in new condition"). lenovo.com $2,360.15 InStock as the non-promo reference.
- **Flag:** Best Buy price unstable across crawls — re-check at add time; do not carry $1,179.99. Do not mix with the kelaptop listing that mislabels the CPU as Ryzen 9 7845HX (non-qualifying, wrong CPU — Best Buy + lenovo.com agree on Ryzen 7 8745HX).

### 17. Razer BlackShark V3 — Black (PC version)
- **Key:** `razer-blackshark-v3-black`
- **Category:** headphones
- **Variant pinned:** Black, PC version
- **Why it qualifies:** Mainstream Razer wireless gaming headset; Best Buy direct Black Friday row. Distinct from in-catalog BlackShark V3 Pro.
- **Identifiers:** MPN RZ04-05410100-R3U1 — **VERIFIED** (Best Buy model field, SKU 12588192 + Newegg "Model # RZ04-05410100-R3U1", Item # 9SIA1CZKVW4952). UPC NO LEAD (qualifying) — 840272919606 appears only on Amazon / eBay / HeadphoneTune (non-qualifying).
- **Price / stock:** Best Buy $129.99 InStock — currently sold & shipped by Electronic Express (marketplace); an older crawl said "Sold by Best Buy". Not currently a direct row at Best Buy. Newegg $129.99; Razer.com $149.99 InStock.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Do not mix: V3 Pro is RZ04-05400100-R3U1 (PC) / RZ04-04530100-R3U1 (Xbox); V3 X HyperSpeed is RZ04-05420100-R3U1; EU variant RZ04-05410100-R3M1.

### 18. Razer Cobra (wired) — Black
- **Key:** `razer-cobra-black`
- **Category:** mice
- **Variant pinned:** Black, wired
- **Why it qualifies:** Mainstream Razer wired gaming mouse; Best Buy direct Black Friday row. Distinct from in-catalog Cobra Pro (wireless).
- **Identifiers:** MPN RZ01-04650100-R3U1 — **VERIFIED** (Best Buy model field + B&H spec page "MFR # RZ01-04650100-R3U1"). UPC 840272903049 — PENDING + lead (ChannelOnline distributor listing only; eBay / Desertcart agree, non-qualifying; B&H spec page prints no UPC).
- **Price / stock:** B&H $29.99 live (snippets $34.95–$34.99 with In Stock / BackOrder varying across crawls). Best Buy $29.99 Black Friday (comp $39.99), sold by Best Buy (per 109-day-old crawl).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Pokémon edition RZ01-04650400-R3M1 ($44.99) is different — do not mix.

### 19. Razer Huntsman V3 Pro Mini 60% — Black
- **Key:** `razer-huntsman-v3-pro-mini-black`
- **Category:** keyboards
- **Variant pinned:** Black, 60% Mini (standard, not 8KHz)
- **Why it qualifies:** Mainstream Razer 60% analog-optical keyboard; Best Buy direct row. Distinct from in-catalog Huntsman V3 Pro (full-size).
- **Identifiers:** MPN RZ03-04990200-R3U1 — PENDING + lead (Best Buy full print, SKU 6558755; Micro Center snippet corroborates the MPN prefix but truncated as "RZ03-04990200-R" — a truncated snippet cannot carry a VERIFIED verdict). UPC 840272909409 — PENDING + lead (Micro Center snippet only as the qualifying source; eBay / PayMore / Ubuy / Desertcart agree, non-qualifying).
- **Price / stock:** Best Buy $124.99 Black Friday (comp $179.99), Sold by Best Buy, InStock. Micro Center $139.99 InStoreOnly.
- **Flag:** A clean re-fetch of the Micro Center product page (id 670527) at add time would likely verify both identifiers — the direct open on 2026-11-20 returned only return-policy text + JSON-LD, so the spec panel did not reproduce. A newer "8KHz" version is being promoted by Razer (posts Oct 2026) — pin the standard Mini.

### 20. Lenovo ThinkPad T16 Gen 4 — Black (21QN005XUS) [REWORK SWAP-IN — replaces Anker Soundcore Boom 2 Plus]
- **Key:** `lenovo-thinkpad-t16-gen-4-black`
- **Category:** laptops
- **Variant pinned:** Black, 21QN005XUS — AMD Ryzen AI 7 PRO 350, 16GB DDR5, 512GB SSD, 16" WUXGA 1920x1200, Win 11 Pro
- **Why it qualifies:** Lenovo sweep pick. CDW in-stock direct row. Distinct from the 21QN0045US config (Ryzen AI 5 PRO 340, 256GB — backlog sibling).
- **Identifiers:** MPN 21QN005XUS — **VERIFIED** (CDW spec page: "MFG#: 21QN005XUS | CDW#: 8436800" + Newegg listing page naming 21QN005XUS, search-fetch — the Newegg direct open hit the bot wall; corroborated by SHI distributor listing: "Mfr Part #: 21QN005XUS", stock 955). UPC PENDING, no lead found.
- **Price / stock:** CDW In Stock, $1,483.99 advertised (search-result crawl of the CDW page — re-check at add time). Adorama $1,649.00, "Ships from Manufacturer" (not on the strict qualifying list; corroboration only). Newegg listings $1,162.02–$1,257.93 (seller attribution unclear — do not use as the row). Best Buy has only "Upgraded" PCOnline/IST listings — not usable.
- **Flag:** Newegg leg is search-fetch only (bot wall). CDW price from search crawl — re-check at add time.

### 21. Anker Soundcore AeroFit 2 — Black
- **Key:** `anker-soundcore-aerofit-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, base model
- **Why it qualifies:** Mainstream Anker open-ear earbuds (launched 2026-11-02 per hifiverdict); Best Buy direct row.
- **Identifiers:** MPN A3874Z11 — **VERIFIED** (B&H spec page + Crutchfield "MFR # A3874Z11"). UPC 194644036393 — PENDING + lead (B&H only; Micro Center Black page fetch returned a support page with no Mfr Part # / UPC).
- **Price / stock:** B&H $79.99 InStock; Micro Center $69.99 InStock; soundcore.com $129.99 list. Best Buy $79.99 (retail $99.99; launched $129.99).
- **Flag:** AI Assistant version is a different listing at $109.99 (list $129.99, model A3874Z12 Obsidian Black) — pin base Black only (A3874Z11). Do not mix: Micro Center Green variant is A3874Z61 (different color).

### 22. Anker Prime 67W GaN Wall Charger (3 Ports)
- **Key:** `anker-prime-67w-gan-charger`
- **Category:** chargers
- **Variant pinned:** 67W, 3-port GaN
- **Why it qualifies:** Mainstream Anker GaN charger; Anker.com direct row plus Newegg row.
- **Identifiers:** MPN A2669 — **VERIFIED** (Anker.com "Model Number: A2669" + Newegg spec page "Model Number A2669" — caveat: the Newegg leg rests on the search fetch of its spec page, not a direct open; the direct open hit the Newegg bot wall on 2026-11-20). UPC NO LEAD (qualifying) — 194644137373 appears only on Amazon / eBay / Ubuy (non-qualifying); the Rakuten product URL digits 00194644137373 are NOT a verified identifier.
- **Price / stock:** Anker.com $49.99 InStock; AnkerDirect via Best Buy $34.99 (Slickdeals 2026-11-02); Newegg $49.99.
- **Flag:** Promo price $34.99 vs $49.99 list. Correction: the brief's "65W A2698" was wrong — the current model is the 67W GaN Wall Charger (3 Ports), model A2669.

### 23. Garmin Venu 3S — Pebble Gray
- **Key:** `garmin-venu-3s-pebble-gray`
- **Category:** wearables
- **Variant pinned:** Pebble Gray, 41mm
- **Why it qualifies:** Mainstream Garmin smartwatch; Best Buy direct row. Distinct from in-catalog Venu 3 (45mm; 3S is 41mm).
- **Identifiers:** MPN 010-02785-00 — **VERIFIED** (Best Buy model field, SKU 6551502 + Crutchfield "Venu 3S 010-02785-00"). UPC 753759314774 — PENDING + lead (Petra + CompSource distributors agree — see the Rework section: distributor + distributor is beyond the batch-5 precedent, so no upgrade; if the catalog owner accepts them as authorized distributors, the UPC becomes VERIFIED).
- **Price / stock:** Best Buy $299.99 InStock, Sold by Best Buy (comp $449.99). Sportsman's $449.99; Petra retail $449.99; CompSource $494.99.
- **Flag:** Identifier pending (UPC). Do not mix: Venu 3 45mm is a different model (e.g. 010-02784-00 / 010-02784-01).

### 24. Garmin Approach S44 — Black
- **Key:** `garmin-approach-s44-black`
- **Category:** wearables
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Garmin golf smartwatch; Best Buy direct row.
- **Identifiers:** MPN 010-03009-00 — **VERIFIED** (Abt "Model # 010-03009-00" + Garmin.com product page pn/010-03009-00). UPC 753759350666 — PENDING + lead (Abt only; Crutchfield search returned only the Twilight variant 010-03009-01; B&H search returned no listing).
- **Price / stock:** $249.99 at several retailers (HeartRateMonitorsUSA, Kohl's, PlayBetter) vs $299.99 list; Staples $316.79 LimitedAvailability. Best Buy $249.99 (comp $299.99), sold by Best Buy.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Do not mix: Twilight variant is 010-03009-01, UPC 753759350673 — different model.

### 25. Garmin Edge 1040 Solar — Black
- **Key:** `garmin-edge-1040-solar-black`
- **Category:** cycling-computers
- **Variant pinned:** Black, Solar
- **Why it qualifies:** Mainstream Garmin bike computer; Garmin.com direct row. Replaces the non-Solar Edge 1040, whose Best Buy listing says "no longer available in new condition". Distinct from in-catalog Edge 1050.
- **Identifiers:** MPN 010-02503-20 — **VERIFIED** (Best Buy model field, SKU 13144387 + buy.garmin.com cart page "Edge 1040 Solar, Device Only, 010-02503-20"). UPC NO LEAD (qualifying) — 753759279752 appears only at bike shops / Summit Racing / Snapklik (non-qualifying).
- **Price / stock:** Garmin.com $649.99 (ships in 2–3 weeks). Best Buy $599.99 InStock — sold & shipped by FrontRow Tech, an Authorized Dealer marketplace seller (not a direct row). MSRP $699.99.
- **Flag:** Pin Solar only. Identifier pending (UPC). Do not mix: non-Solar Edge 1040 is 010-02503-00 — different listing.

### 26. Samsung Galaxy SmartTag 2 — Black
- **Key:** `samsung-galaxy-smarttag-2-black`
- **Category:** trackers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Samsung Bluetooth tracker; Best Buy direct row.
- **Identifiers:** MPN EI-T5600BBEGUS — **VERIFIED** (Best Buy model field + Micro Center spec page "Mfr Part# EI-T5600BBEGUS"). UPC 887276765358 — PENDING + lead (Micro Center only qualifying; NFM agrees but is outside the qualifying list).
- **Price / stock:** Best Buy $25.00 (comp $29.99), sold by Best Buy. Price fluctuates $25–$26.93 across crawls (promo).
- **Flag:** Promo-sensitive price — re-check at add time.

### 27. Samsung HW-Q800F — Black
- **Key:** `samsung-hw-q800f-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Samsung 5.1.2 Dolby Atmos soundbar (2025); Best Buy direct list row. Distinct from in-catalog HW-Q990F.
- **Identifiers:** MPN HW-Q800F/ZA — **VERIFIED** (Crutchfield "MFR # HW-Q800F/ZA" + B&H, plus Best Buy model field). UPC 887276934242 — **VERIFIED** (B&H spec page + ADI Global Distribution distributor spec — second source is a distributor listing, not a core retailer; see the Rework section).
- **Price / stock:** $1,097.99 (B&H, Crutchfield, In Stock); Best Buy list $1,099.99. Some crawls show $537.99 marketplace rows / "Sold Out" flags — not usable.
- **Flag:** Best Buy direct row $1,099.99 needs re-check at add time — marketplace rows at $537.99 are not usable.

### 28. Samsung HW-QS700F — Black
- **Key:** `samsung-hw-qs700f-black`
- **Category:** soundbars
- **Variant pinned:** Black, 3.1.2ch convertible
- **Why it qualifies:** Mainstream Samsung 2025 soundbar (Convertible Flip design, Wireless Dolby Atmos, SpaceFit Sound Pro, Q-Symphony); Best Buy direct Black Friday row plus Crutchfield in-stock row. **Replacement for the Galaxy Tab S11 128GB Gray, which the membership check found already in the catalog (exact-key duplicate).** Found via the Samsung soundbar sweep: samsung.com CA lists the model; the US price row is Best Buy. Distinct from in-catalog HW-Q990F and in-batch HW-Q800F.
- **Identifiers:** MPN HW-QS700F/ZA — **VERIFIED** (B&H "MFR # HW-QS700F/ZA" + Abt + SHI distributor "Mfr Part # HW-QS700F/ZA"). UPC 887276934273 — **VERIFIED** (B&H spec page + ADI Global Distribution distributor spec — second source is a distributor listing, not a core retailer; see the Rework section).
- **Price / stock:** $597.99 (B&H, Abt, InStock); Best Buy $347.99 Black Friday (list $699.99); Crutchfield $597.99 (list $697.99), InStock, free shipping. Abt notes a manufacturer rebate ending 11/22/2026.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Crutchfield $597.99 is the non-promo reference; re-check both at add time.

### 29. Microsoft Surface Laptop 13" (2025) — Ocean, 512GB [REWORK SWAP-IN — replaces Samsung Odyssey G5 G55H 27"]
- **Key:** `microsoft-surface-laptop-13-2025-ocean-512gb`
- **Category:** laptops
- **Variant pinned:** Ocean, 512GB, Snapdragon X Plus, EP2-33432
- **Why it qualifies:** Named alternate from the first draft, now fully verified. Best Buy direct in-stock row. Cleanest verified pair in the alternates track. Distinct from in-catalog Surface Laptop 13.8" 8th Edition (EP2-59028, Snapdragon X2 Plus, 13.8") and 15" 8th Edition (EP2-60128) — different MPN, size, and chip generation.
- **Identifiers:** MPN EP2-33432 — **VERIFIED** (B&H "MFR # EP2-33432" + Abt "Model # EP2-33432"; Best Buy model field agrees). UPC 196388548231 — **VERIFIED** (B&H spec page UPC + Abt UPC # 196388548231).
- **Price / stock:** Best Buy Ocean 512GB $1,149.99 (comp $1,249.99), Add to cart, InStock, SKU 10148535 (page opened fresh 2026-11-20). Black Friday ends Nov 28. Abt lists this config as "no longer available" — Best Buy is the row. Other configs (NOT the pinned row): Platinum 512GB EP2-33462, Violet 512GB EP2-33426, Platinum 256GB EP2-36981.
- **Flag:** Target calls this model "8th Edition," which is confusing; do not conflate with the in-catalog 13.8" 8th Edition.

### 30. Apple 140W USB-C Power Adapter — White
- **Key:** `apple-140w-usb-c-power-adapter-white`
- **Category:** chargers
- **Variant pinned:** White, new model
- **Why it qualifies:** Mainstream Apple charger; Best Buy direct row.
- **Identifiers:** MPN MKFQ4AM/A — **VERIFIED** (Best Buy model field, SKU 6530838 + B&H "MFR # MKFQ4AM/A" + Apple.com shop product MKFQ4AM/A). UPC NO LEAD for MKFQ4AM/A — no qualifying source prints a UPC for this part.
- **Price / stock:** $99.00 (Apple.com, B&H, InStock); Adorama $129.00.
- **Flag:** Two Best Buy SKUs exist (old 6485370 vs new MKFQ4AM/A 6530838); pin the new MKFQ4AM/A. Do NOT confuse with MW2M3AM/A (B&H lists it as a 140W adapter with UPC 195949376955 — a different, newer part) or old MLYU3AM/A (UPC 194252750629).

### 31. Apple 35W Dual USB-C Port Compact Power Adapter — White
- **Key:** `apple-35w-dual-usb-c-compact-power-adapter-white`
- **Category:** chargers
- **Variant pinned:** White, compact
- **Why it qualifies:** Mainstream Apple dual-port charger; Best Buy direct row.
- **Identifiers:** MPN MW2H3AM/A — **VERIFIED** (B&H "MFR # MW2H3AM/A" + Apple.com shop product MW2H3AM/A + Micro Center "Mfr Part# MW2H3AM/A") — supersedes the first draft's single non-qualifying source (an in-store price-tag photo on Instagram). UPC 195949376535 — PENDING + lead (Micro Center only qualifying; NFM + Datavision agree but are outside the qualifying list).
- **Price / stock:** $59.00 (Apple.com, InStock); $59.99 (B&H). Some crawls show $49.99 (promo-sensitive).
- **Flag:** Promo-sensitive price ($49.99 vs $59.00 list). **UPC split — do not cross:** compact MW2H3AM/A = 195949376535; non-compact MW2K3AM/A = 195949376573. MW2K3AM/A is the larger non-compact version — pin compact only. (Earlier US part MNWM3AM/A is the legacy compact part number.)

### 32. Garmin Fenix 8 Solar Sapphire 47mm — Carbon Gray [REWORK SWAP-IN — replaces Apple Magic Keyboard (M2)]
- **Key:** `garmin-fenix-8-solar-sapphire-47mm-carbon-gray`
- **Category:** wearables
- **Variant pinned:** Carbon Gray DLC Titanium with Black/Pebble Gray silicone band, 010-02906-10
- **Why it qualifies:** Named alternate from the first draft, now fully verified. Best Buy direct in-stock row. Distinct from in-catalog Fenix 8 AMOLED Sapphire 47mm (010-02904-20) — Solar MIP display vs AMOLED — and from Fenix 9 47mm (010-04762-00).
- **Identifiers:** MPN 010-02906-10 — **VERIFIED** (Garmin official FĒNIX 8 SERIES price list PDF + CompSource distributor spec; Best Buy model field agrees). UPC 753759339326 — **VERIFIED** (same two sources: Garmin price list PDF + CompSource "UPC EAN CODE: 753759339326").
- **Price / stock:** Best Buy $749.99 (comp $999.99, Save $250), Sold by Best Buy, Add to cart, InStock, SKU 6594318 (page opened fresh 2026-11-20). Garmin price list MRP $1,099.99. Garmin.com $749.99 (for the sibling 010-02906-20 variant). Kohl's $749.99 lists both 010-02906-10 and 010-02906-20.
- **Flag:** Correction recorded 2026-11-20: the initial guess 010-02904-00 was WRONG — that is the AMOLED Slate Gray. Solar 47mm = 010-02906-10 (Carbon Gray) and 010-02906-20 (Titanium/Amp Yellow).

### 33. Logitech Signature Slim K950 — Graphite [REWORK SWAP-IN — replaces ASUS ROG Falchion Ace HFX]
- **Key:** `logitech-signature-slim-k950-graphite`
- **Category:** keyboards
- **Variant pinned:** Graphite, US layout
- **Why it qualifies:** Named alternate from the first draft, now fully verified. B&H direct in-stock row. Distinct from in-catalog Signature M650 mouse — only other Signature item.
- **Identifiers:** MPN 920-012424 — **VERIFIED** (B&H "MFR # 920-012424" + Logitech official datasheet, 1worldsync PDF: "GRAPHITE US Part #: 920-012424"; Off-White US is 920-012429, different; Best Buy model field agrees). UPC 097855192974 — **VERIFIED with caveat** (B&H product page "UPC: 097855192974" + Tech-America distributor spec — caveat: Tech-America and PC-Canada share the same data feed, so the second source is a distributor listing, not a second major retailer).
- **Price / stock:** B&H $69.99 InStock (was $89.99, Holiday Savings $20) — the clean row (opened fresh 2026-11-20). Staples $69.99 InStock. Best Buy $89.99, but one listing (SKU 10201839) is "Sold & shipped by EP Holdings Inc - Logitech Authorized Store" (marketplace — do not use); another Best Buy SKU 12804402 shows $89.99 InStock.
- **Flag:** Use the B&H $69.99 row. Do not mix with K980 Solar+ or MK950 combo (different models).

### 34. ASUS ZenWiFi AXE7800 Tri-Band Mesh Wi-Fi 6E System (3-Pack) — White
- **Key:** `asus-zenwifi-axe7800-3-pack-white`
- **Category:** networking (reconcile to `routers` at add time — the catalog's RT-BE58U is `routers`; the ASUS sweep used `routers` for all networking picks)
- **Variant pinned:** White, 3-pack
- **Why it qualifies:** Mainstream ASUS tri-band Wi-Fi 6E mesh system; ASUS direct in-stock row. Replaces the standalone RT-AXE7800 router (no current direct price — see "Not carried"). Different product from the standalone router.
- **Identifiers:** MPN ZenWiFi AXE7800 (model name AXE7800 (W-3-PK)) — **VERIFIED** (ASUS official + Newegg spec page "Part Number 90IG07D0-MA1A2V, Model # ZenWiFi AXE7800, 3-Pack"). UPC NO LEAD (qualifying); eBay GTIN 0197105421790 is not qualifying.
- **Price / stock:** ASUS $299.99 InStock; Newegg $329.99. **Best Buy row dead:** the current Best Buy listing is sold/shipped by Newegg Official (marketplace) at $356.49 — NOT Best Buy direct. The first draft's $302.49 Best Buy-direct row no longer holds.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. B&H carries the ZenWiFi XT9 (different model, 2-pack, No Longer Available) and RT-AXE7800 (different model, No Longer Available) — do not mix. The hardware is also sold as ZenWiFi ET9 — the retail 3-pack is AXE7800 (W-3-PK).

### 35. Samsung HW-S60D — Black [REWORK SWAP-IN — replaces Dell XPS 14 9440]
- **Key:** `samsung-hw-s60d-black`
- **Category:** soundbars
- **Variant pinned:** Black, HW-S60D/ZA (S-series 5.0ch all-in-one, 2024)
- **Why it qualifies:** Mainstream Samsung all-in-one Dolby Atmos soundbar; Best Buy direct Black Friday row + B&H row. Both identifiers VERIFIED — joint-strongest pick in the Samsung sweep. Distinct from the in-catalog HW-LS60D Music Frame (different model — the S60D is the all-in-one soundbar, the LS60D is the Music Frame speaker).
- **Identifiers:** MPN HW-S60D/ZA — **VERIFIED** (Best Buy model field HW-S60D + B&H product page HW-S60D/ZA + Samsung official spec sheet). UPC 887276823935 — **VERIFIED** (B&H spec page + Samsung official HW-S60D spec sheet, "UPC CODE: 887276823935", agree).
- **Price / stock:** Best Buy $279.99 Black Friday (comp $399.99; some crawls show $330.00), sold by Best Buy, Add to cart; Slickdeals confirms Best Buy $279.99 (2026-11-05).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Canadian /ZC variant has a different UPC 887276824543 — pin the US /ZA only.

### 36. Dell G16 7630 — Gray
- **Key:** `dell-g16-7630-gray`
- **Category:** laptops
- **Variant pinned:** Gray, RTX 4070 / i9-13900HX / 32GB / 1TB (Dell-direct config)
- **Why it qualifies:** Mainstream Dell gaming laptop; Dell-direct row. Best Buy only shows an "Upgraded" third-party config (not usable).
- **Identifiers:** MPN PENDING + lead (Dell order codes useghbto7630glmf / useghbto7630fwmg — no single MPN; two order codes seen for the same spec, likely differing in minor config options; Icecat CN76154 is a different code format and not a second source for the same code). UPC NO LEAD.
- **Price / stock:** Dell.com $1,949.99–$1,959.99 (crawls 88 and 135 days old — stale, re-verify the current price at add time). Tech Specs on both order codes: 13th Gen Intel Core i9-13900HX, NVIDIA GeForce RTX 4070 8GB GDDR6, 32 GB (2 x 16 GB) DDR5 4800 MT/s, 1 TB SSD, 16" QHD+ — the exact pinned config. Best Buy only shows an "Upgraded" third-party config at $2,879 (model G16-7630-Upgraded) — not usable.
- **Flag:** **Correction to the first draft: Dell.com DOES still list this config; the "discontinued at Dell" conclusion is withdrawn.** Dell-direct only (DECISIONS 015 concern — the second flagged brand-direct-only pick alongside the X1 Carbon). Color naming unverified: Icecat shows Black ("Zwart") vs the draft's Gray (G16's dark finish is Metallic Night). Stale prices — re-verify at add time.

### 37. HP Victus 15 (15-fb3093dx) — Mica Silver
- **Key:** `hp-victus-15-fb3093dx-mica-silver`
- **Category:** laptops
- **Variant pinned:** Mica Silver, 15-fb3093dx (Ryzen 7 7445HS, RTX 4050, 16GB, 512GB)
- **Why it qualifies:** Mainstream HP gaming laptop; Best Buy direct Holiday Deal row.
- **Identifiers:** MPN 15-fb3093dx / BM4X8UA#ABA — **VERIFIED** (Best Buy model field, SKU 6623881 + HP datasheet "Victus by HP 15.6 inch Gaming Laptop PC 15-fb3093dx", Product number BM4X8UA#ABA). UPC 199251266874 — PENDING + lead (HP datasheet only — needs a second qualifying source; eBay also prints it, does not count).
- **Price / stock:** Best Buy $949.99 (Holiday Deal). One snippet mentions $639.99 for the same specs (possibly an older deal price).
- **Flag:** Price volatility ($639.99 vs $949.99) — re-check at add time.

### 38. Samsung Galaxy Buds3 — Silver [REWORK SWAP-IN — replaces HP 430 Multi-Device Wireless Mouse]
- **Key:** `samsung-galaxy-buds3-silver`
- **Category:** earbuds
- **Variant pinned:** Silver, SM-R530NZAAXAR
- **Why it qualifies:** Mainstream Samsung earbuds (2024, still current); Best Buy direct new row + B&H in-stock row. Both identifiers VERIFIED — joint-strongest pick in the Samsung sweep. Distinct from in-catalog Buds3 Pro Silver, Buds3 FE Black, Buds4, Buds4 Pro — the base Buds3 is distinct.
- **Identifiers:** MPN SM-R530NZAAXAR — **VERIFIED** (Best Buy model field + B&H product page + Micro Center spec Mfr Part # + Abt page, all agree). UPC 887276868059 — **VERIFIED** (B&H spec page + Micro Center spec + Abt page, all agree).
- **Price / stock:** Best Buy $109.95 InStock (new, SKU 12901715; earlier crawl $109); B&H $124.95 In Stock (was $174.95); Micro Center $49.99 but OutOfStock (do not use as the row).
- **Flag:** Best Buy also lists a refurbished Excellent unit ($84.99, sold by Elite Tech LLC, marketplace) under a different SKU — pin the new SKU 12901715 only and confirm sold-by-Best-Buy at add time. Swappa ties a DIFFERENT UPC 887276880938 to MPN SM-R530NZAWXAR (W-variant) — different variant code, disregarded for this pin.

### 39. ASUS ROG Swift OLED PG32UCDM 32" 4K 240Hz — Black [REWORK SWAP-IN — replaces Lenovo Legion Pro 5 16IRX9]
- **Key:** `asus-rog-swift-oled-pg32ucdm-black`
- **Category:** monitors
- **Variant pinned:** Black, original PG32UCDM (QD-OLED, 240Hz)
- **Why it qualifies:** Flagship 32-inch 4K QD-OLED ROG monitor; two retailer-direct in-stock rows. Distinct from in-catalog PG32UCWM (Tandem RGB OLED flagship, different model) and PG27UCDM (27-inch).
- **Identifiers:** MPN PG32UCDM — **VERIFIED** (B&H spec page "MFR # PG32UCDM" + Micro Center spec "Mfr Part# PG32UCDM", SKU 668913). UPC 197105413726 — **VERIFIED** (same two sources agree).
- **Price / stock:** B&H $1,229.00 InStock (retailer-direct row). Micro Center also lists it (price not captured in-session; B&H is the row).
- **Flag:** Do NOT mix with PG32UCDM3 Gen3 (UPC 199291274662, B&H $1,278.70) or PG32UCDMR (UPC 199291033863, B&H $899 Holiday / $1,299.99 list) — distinct variants with their own UPCs. Pin original PG32UCDM only.

### 40. ASUS RT-BE86U BE6800 Dual-Band Wi-Fi 7 Router — Black [REWORK SWAP-IN — replaces Lenovo ThinkPad T14 Gen 6]
- **Key:** `asus-rt-be86u-black`
- **Category:** routers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Wi-Fi 7 router (successor to RT-AX86U); Best Buy + B&H + Micro Center rows. Distinct from in-catalog RT-BE58U (the catalog's only router).
- **Identifiers:** MPN RT-BE86U — **VERIFIED** (Micro Center spec "Mfr Part# RT-BE86U" + Best Buy model field, SKU 6594279, sold by Best Buy). UPC 197105581432 — **VERIFIED** (B&H spec page + Micro Center spec, SKU 792663, agree).
- **Price / stock:** B&H $239.99 InStock (row). Best Buy $255.99–$269.99, sold by Best Buy (price varies across crawls; one crawl showed $179.99 — likely open-box/clearance confusion, do not use). ASUS list $249.99 (ChannelOnline MSRP).
- **Flag:** Re-check Best Buy price at add time; use B&H $239.99 as the row unless Best Buy direct is lower and confirmed.

### 41. Microsoft Surface Thunderbolt 4 Dock — Black
- **Key:** `microsoft-surface-thunderbolt-4-dock-black`
- **Category:** docks
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Microsoft dock; Best Buy direct row. Replaces the Surface Dock 2 (clearance-only — see "Not carried").
- **Identifiers:** MPN T8I-00001 — **VERIFIED** (B&H + Newegg spec page "Part Number T8I-00001" + Best Buy model field, SKU 11149146 / 12476006). UPC 196388142200 — **VERIFIED** (B&H + Zoro distributor spec "Mfr # T8I-00001, UPC # 196388142200"; Target Plus partner-supplied listing also prints it).
- **Price / stock:** Best Buy $299.99 (one crawl $214.99 — promo-sensitive), sold by Best Buy, Add to cart; Newegg ~$251.99; Zoro $272.99.
- **Flag:** Promo-sensitive price — varies $214.99–$299.99 across crawls; use $299.99, re-check at add time.

### 42. ASUS RT-BE92U BE9700 Tri-Band Wi-Fi 7 Router — Black [REWORK SWAP-IN — replaces Meta Oakley Vanguard]
- **Key:** `asus-rt-be92u-black`
- **Category:** routers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream tri-band Wi-Fi 7 router with 10G port; Best Buy + B&H + ASUS rows. Distinct from RT-BE86U (dual-band BE6800) and RT-BE58U (in catalog).
- **Identifiers:** MPN RT-BE92U — **VERIFIED** (Micro Center spec "Mfr Part# RT-BE92U" + Best Buy model field, SKU 6594276 / 11124612). UPC 197105580633 — **VERIFIED** (B&H spec page + Micro Center spec, SKU 800631, agree).
- **Price / stock:** Best Buy $265.51 InStock (1-day crawl; list $289.99) — retailer-direct row. B&H $285.99; ASUS US $289.99 InStock.
- **Flag:** Best Buy price is promo-sensitive ($265.51 vs $289.99 list across crawls) — re-verify at add time. Refurbished RT-BE92U-RB (SKU 12760801, $166.24) is a different listing — do not mix.

### 43. Meta Ray-Ban Meta Skyler (Gen 2) (Green lenses) — Shiny Black
- **Key:** `meta-ray-ban-skyler-gen-2-green-shiny-black`
- **Category:** smart-glasses
- **Variant pinned:** Shiny Black, Green lenses
- **Why it qualifies:** Mainstream Meta smart glasses (Ray-Ban line, Gen 2); Best Buy direct row, meta.com also $379.
- **Identifiers:** MPN 0RW4014_601/7152 — PENDING + lead (Best Buy product page, SKU 6642578, "Model: 0RW4014_601/7152", Sold by Best Buy — upgraded from Q&A-only in the first draft, but still a single qualifying source; meta.com does not print the code). UPC NO LEAD.
- **Price / stock:** Best Buy $379.00 InStock, Sold by Best Buy; meta.com $379 InStock.
- **Flag:** Transitions variants $459 — pin Green only. The Transitions Green variant is a DIFFERENT model: Best Buy Model 0RW4014_601/1M52, SKU 6642596, Sold by Best Buy, $459.00. Abt carries only the Transitions variant (RW4014-6011M52, $459).

### 44. Google Nest Hub (2nd Gen) — Charcoal
- **Key:** `google-nest-hub-2nd-gen-charcoal`
- **Category:** smart-home
- **Variant pinned:** Charcoal
- **Why it qualifies:** Mainstream Google smart display; Best Buy direct list row.
- **Identifiers:** MPN GA01892-US — **VERIFIED** (Best Buy model field + Abt + Ferguson distributor spec + Zoro distributor spec). UPC 193575009223 — **VERIFIED** (Ferguson distributor spec + Zoro distributor spec — both UPC sources are distributor specs; no core retailer (B&H/Abt/Newegg/Crutchfield) printed the UPC; see the Rework section).
- **Price / stock:** Google Store $99.99; Ferguson $105.90 OutOfStock. Best Buy $99.99 list. One crawl showed Chalk "Sold Out" — Charcoal listing $99.99 live.
- **Flag:** 2021 hardware (5 years old), frequently discounted to $49.99–$59.99; $99.99 is list. Not discontinued, but age noted.

### 45. ASUS ZenWiFi BT8 BE14000 Tri-Band Wi-Fi 7 Mesh System (2-Pack) — White [REWORK SWAP-IN — replaces Keychron K11 Max]
- **Key:** `asus-zenwifi-bt8-2-pack-white`
- **Category:** routers
- **Variant pinned:** White, 2-pack BT8(W-2-PK)
- **Why it qualifies:** Current mainstream Wi-Fi 7 mesh; B&H + Micro Center + ASUS rows. Distinct from the in-batch ZenWiFi AXE7800 3-pack (different product/generation).
- **Identifiers:** MPN BT8(W-2-PK) — **VERIFIED** (B&H spec page "MFR # BT8(W-2-PK)" + Micro Center spec "Mfr Part# BT8(W-2-PK)", SKU 800656; ASUS tech-spec page confirms model names BT8(W-1-PK) / BT8(W-2-PK) / BT8(W-3-PK)). UPC 197105532045 — **VERIFIED** (same two sources agree).
- **Price / stock:** B&H $449.99 InStock, Holiday Savings $130 off (was $579.99) — retailer-direct row. Micro Center $599.99 InStoreOnly (not the row). ASUS 2-pack list $599.99.
- **Flag:** Promo price — Holiday Savings, re-verify at add time. 1-pack (UPC 197105531987, B&H $329.99, currently OutOfStock) and 3-pack (UPC 197105532090, B&H $699.99) are different pack sizes with different UPCs — pin 2-pack only. A Target refurbished 3-pack listing shows UPC 724129265927 — a refurb/Target-specific code, ignore; do not treat as a conflict.

### 46. ASUS ZenWiFi BT10 BE18000 Tri-Band Wi-Fi 7 Mesh System (2-Pack) — White [REWORK SWAP-IN — replaces Keychron Q0 Max]
- **Key:** `asus-zenwifi-bt10-2-pack-white`
- **Category:** routers
- **Variant pinned:** White, 2-pack BT10(W-2-PK)
- **Why it qualifies:** Premium current Wi-Fi 7 mesh; B&H + Best Buy rows. Distinct from BT8 (BE14000 vs BE18000, 2.5G vs 10G ports).
- **Identifiers:** MPN BT10(W-2-PK) — **VERIFIED** (B&H spec page "MFR # BT10(W-2-PK)" + Best Buy model field "BT10 (W-2-PK)", SKU 11870821). UPC 197105429895 — **PENDING (DOWNGRADED at add time 2026-11-20)** — was VERIFIED with caveat (B&H spec page + CompSource distributor spec); the Best Buy spec panel for SKU 11870821 as fetched shows no UPC field at all, so the confirm-or-downgrade check did not confirm it. The $760.69 Best Buy listing is marketplace (Beach Audio Inc), not Best Buy direct.
- **Price / stock:** B&H $629.99 (row). Best Buy $760.69 (seller not confirmed in-session — do not use as the row without a fresh seller check).
- **Flag:** At add time, confirm the UPC on the Best Buy spec panel for SKU 11870821; if it does not agree, downgrade to PENDING. Do NOT use the 3-pack: Best Buy 3-pack (SKU 6578611) is Clearance $849.99 and "no longer available in new condition" — clearance-only fails the rule. 1-pack (B&H UPC 197105429833, $346.00 InStock) is a different pack size — see backlog.

### 47. HyperX Cloud III Wireless — Black
- **Key:** `hyperx-cloud-iii-wireless-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream HyperX wireless gaming headset; Best Buy direct row. Distinct from in-catalog Cloud III S Wireless.
- **Identifiers:** MPN 77Z45AA — **VERIFIED** (Best Buy model field + HyperX.com press release "Part Number 77Z45AA Black, 77Z46AA Black-Red"). UPC 197029611727 — PENDING + lead (no qualifying source at all yet; printed with MPN 77Z45AA by shipfreedefense, shop.vb.net, PB Tech NZ, Desertcart — none qualifying; eBay prints a conflicting UPC 786513757593 — ignore, eBay, likely a different bundle).
- **Price / stock:** HyperX US shop: "Discontinued! Shop HyperX Cloud III S Wireless Headset Instead", $149.99, OutOfStock. Best Buy $149.99 (one crawl $174.49 — price varies), 1-day and 8-day crawls; Best Buy price/stock not re-verified this round.
- **Flag:** Discontinued at the HyperX US shop — Best Buy may be the only live row. Promo-sensitive price ($149.99 vs $174.49 across crawls) — re-check at add time.

### 48. HyperX Alloy Origins 60 — Black
- **Key:** `hyperx-alloy-origins-60-black`
- **Category:** keyboards
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream HyperX 60% gaming keyboard; Best Buy direct row. Distinct from in-catalog Alloy Origins 65.
- **Identifiers:** MPN 4P5N4AA#ABA — **VERIFIED** (Best Buy model field + Newegg spec page "Model 4P5N4AA; MPN 4P5N4AA#ABA" + HP.com "Product # 4P5N4AA#ABA"). UPC 196188048948 — **VERIFIED** (Newegg spec page + HP datasheet, via Icecat hosting — "HyperX Alloy Origins 60 (4P5N4AA), UPC 196188048948").
- **Price / stock:** HP.com $114.99 InStock; Best Buy $77.99–$86.99 (comp $114.99). Newegg $69.99–$114.99 (sold by Official HP Store).
- **Flag:** Promo-sensitive price (varies $77.99–$114.99 across crawls) — re-check at add time. The draft's alternate model HKBO1S-RB-US/G is Amazon-derived — do not use as the lead. HP datasheet also lists 196188048955 / 5704174946502 for other variants — do not mix.

### 49. Corsair K65 PRO MINI — Black (OPX)
- **Key:** `corsair-k65-pro-mini-black`
- **Category:** keyboards
- **Variant pinned:** Black, OPX optical switches
- **Why it qualifies:** Mainstream Corsair 60% keyboard; Corsair direct + Best Buy promo rows. Distinct from in-catalog K65 Plus Wireless (wired optical OPX vs wireless).
- **Identifiers:** MPN CH-91A401A-NA — **VERIFIED** (Best Buy model field, SKU 6547466 + Newegg "Part Number CH-91A401A-NA"). UPC 840006698432 — PENDING + lead (no qualifying source yet; aio.lv prints "MPN CH-91A401A-NA, EAN 840006698432"; camelcamelcamel / Desertcart agree — none qualifying).
- **Price / stock:** Best Buy $72.98 promo / $149.99 list; Newegg $109.99+; Corsair direct $79.99 per pricertoday. Pin $79.99 (Corsair direct / Best Buy promo).
- **Flag:** Promo price — list $149.99, promo ~$73–$80. Correct US code is CH-91A401A-NA (NA layout) — the guessed code CH-9199114 was wrong, do NOT use it. CH-91A401A-ND is the Nordics layout, a different variant.

### 50. ASUS TUF Gaming M4 Air Wired Gaming Mouse — Black [REWORK SWAP-IN — replaces Alienware 18 Area-51]
- **Key:** `asus-tuf-gaming-m4-air-black`
- **Category:** mice
- **Variant pinned:** Black (P307 TUF GAMING M4 AIR)
- **Why it qualifies:** Mainstream ultralight TUF mouse (47g, 16,000 DPI); Best Buy + ASUS rows. No TUF mouse is in the catalog.
- **Identifiers:** MPN P307 TUF GAMING M4 AIR — **VERIFIED** (SHI distributor spec + Zoro spec, both "Mfr Part # P307 TUF GAMING M4 AIR"; CompSource and OfficeCrave print the same UPC; Best Buy model field reads P307-TUF-GAMING-M4-AIR, SKU 11145905). UPC 195553335454 — **PENDING (DOWNGRADED at add time 2026-11-20, user-approved)** — was VERIFIED (SHI + Zoro agree); downgraded because both sources are distributors, the same shape as the Venu 3S UPC (Petra + CompSource) that stays pending — counting one and not the other would be inconsistent. If the catalog owner accepts distributor + distributor, it becomes VERIFIED.
- **Price / stock:** Best Buy $57.99 (8-day crawl, Add to cart) — retailer-direct row; older crawls $44.99. ASUS US $49.99.
- **Flag:** Price moves ($44.99–$57.99) — re-verify at add time. UPC conflict noted and set aside: a Target marketplace listing (sold by Ideal sales, not qualifying) shows UPC 196384006247 for the same model name — marketplace-sourced, do not treat as a competing verified code.

## Not carried

### Dropped in the rework (2026-11-20) — 15 entries, replaced per the Swaps table above
- **Bose Solo Soundbar Series II (845194-2100)** — MPN single-source (batch-5 draft), UPC no qualifying lead; two batches without progress. Bose.com $199.00 new; Costco $212.99 InStock. Dropped for the HW-Q600F (both identifiers VERIFIED).
- **Razer Kiyo Pro Ultra 4K (RZ19-04420100-R3U1)** — MPN single-source (Best Buy only); UPC 840272900376 conflict unresolved (no qualifying spec page ties it to either model); Best Buy $429.95 row is sold & shipped by 6ave Electronics (marketplace, not direct). Dropped for the ThinkPad T14 Gen 5.
- **Razer Kiyo V2 Pro** — No qualifying MPN/UPC lead at all (non-qualifying: RZ19-05360100-R3U1 / 840272918661); no Best Buy direct row; Razer.com $299.99 InStock, page prints no MPN/UPC. Too new for retailer spec pages as of 2026-11-20; re-probe B&H / Best Buy in a later sweep. Dropped for the Legion Pro 5 Gen 10.
- **Anker Soundcore Boom 2 Plus (A3134012)** — MPN single-source (Best Buy only); UPC no qualifying lead (3 conflicting Ubuy values); Best Buy $249.99 Sold Out; soundcore.com $159.99 sale. A Newegg spec-page fetch is the next probe (Klarna indicates Newegg carries it). Dropped for the ThinkPad T16 Gen 4.
- **Samsung Odyssey G5 G55H 27" (LS27HG552ENXZA)** — MPN suffix conflict unresolved (Samsung.com LS27HG550ENXZA vs Best Buy LS27HG552ENXZA); UPC no lead. Best Buy $149.99 Black Friday. Dropped for the Surface Laptop 13" (2025). The 32" sibling (LS32HG554ENXZA, Best Buy $189.99 BF) is MPN-pending single-source and was not carried either.
- **Apple Magic Keyboard for iPad Air 11" (M2) (MJQJ3LL/A)** — No retailer-direct new row (Best Buy new = HHGregg marketplace; refurb $149.99; clearance $119.99 seller unverified); Apple.com price/stock not captured; MPN is the older keyboard (Pro 11" 1st–4th gen / Air 4th–5th gen), not M2-exclusive. Dropped for the Fenix 8 Solar.
- **ASUS ROG Falchion Ace HFX (M605 / 90MP03VE-BKAA23)** — MPN ASUS-only; UPC no lead. ASUS $199.99; Newegg $129.99 (spec table not captured). Dropped for the Signature Slim K950.
- **Dell XPS 14 9440 (XPS9440-7816SLV-PUS)** — MPN now VERIFIED (Best Buy + Dell datasheet via Icecat), UPC pending (Dell datasheet only) — but the pinned config is not available new at Best Buy; price only from a Q&A page ($1,199.99). Dropped for the HW-S60D.
- **HP 430 Multi-Device Wireless Mouse (3B4Q2AA)** — MPN rests on same-family corroboration only (HP datasheet + hp.com); UPC 195908246565 #ABL datasheet-only. HP.com $48.99; Best Buy via HP Inc $28.99. Dropped for the Galaxy Buds3.
- **Lenovo Legion Pro 5 16IRX9 (83DF00A8US)** — Best Buy row now dead ("no longer available in new condition"); no second identifier source. Dropped for the Legion Pro 5 Gen 10 (its successor). See track E.
- **Lenovo ThinkPad T14 Gen 6 (21QJ00CSUS)** — MPN now VERIFIED (CDW + Best Buy) but still no usable direct price row (Best Buy marketplace/refurb only; CDW price not shown). Moved to the queued Lenovo backlog (B3), not dropped outright. Do NOT attach B&H's UPC 199272842804 (different config 21QDS2VV00). Replaced in the batch by the RT-BE86U.
- **Meta Oakley Vanguard** — MPN format conflict unresolved (Abt OW8001800105 vs Best Buy 0OW8001 3928 46 vs EU OW8001-05 52); UPC pending (Abt only). Meta.com $499 / $424.15 BF; Best Buy $424.00 BF. Dropped for the RT-BE92U.
- **Keychron K11 Max (K11M-A1)** — Likely discontinued (successor K15 Max); Keychron.com $89.99 sold-out header; in-stock Black variants $49.99/$59.99; MPN Keychron-family only; UPC no lead; no retailer-direct row. Dropped for the ZenWiFi BT8 2-pack.
- **Keychron Q0 Max (Q0M-M1)** — Brand-direct-only; MPN Keychron-family only; UPC no lead; no US retailer direct row. Keychron.com $113.99, Carbon Black/Red Available. It is a NUMBER PAD, not a keyboard. Dropped for the ZenWiFi BT10 2-pack.
- **Alienware 18 Area-51 (LAA18250-9444BLU-PUS)** — MPN single-source (Best Buy model field), SKU 12741185; UPC no lead. Best Buy $3,949.00 (price varies $3,369.99–$3,999 across crawls). Dropped for the TUF Gaming M4 Air. (The Alienware 16 Aurora, both identifiers VERIFIED via distributors, is on HOLD for no direct price row — see the Rework section.)

### Held items, dropped on re-check (2026-11-20, first draft)
- **HP 930 Creator Wireless Mouse (1D0K9AA)** — HP Malaysia page says Discontinued; Staples OOS everywhere. Confirmed discontinued/OOS — do not carry.
- **ASUS ROG Strix XG27ACS** — ASUS US $229 OutOfStock still; Newegg $283.99 seller unconfirmed; Walmart $229 seller unknown. No clean US retailer-direct in-stock row — drop again.
- **Corsair NIGHTSABRE Wireless (CH-931B011-NA)** — Corsair.com now OutOfStock at $149.99; worse than batch 5.

### Duplicate found by the membership check (2026-11-20, first draft)
- **Samsung Galaxy Tab S11 128GB Gray (SM-X730NZAAXAR)** — already in the catalog (exact key `samsung-galaxy-tab-s11-128gb-gray`). Was the planned 50th model; dropped and replaced with HW-QS700F (entry 28). Best Buy $699.99 Black Friday (list $999.99) was the row — do not re-add.

### Samsung / Lenovo sweep — already in the catalog (2026-11-20, first draft)
- **Samsung Galaxy Watch8 Classic 46mm Black (SM-L500NZKAXAA)** — already in catalog (verified). samsung.com $499.99 InStock.
- **Samsung Galaxy Watch8 40mm / 44mm Graphite** — already in catalog (verified). samsung.com $299.99 / $329.99.
- **Samsung Galaxy Watch9 40mm / 44mm Graphite** — already in catalog (verified).
- **Samsung Galaxy Buds4 / Buds4 Pro / Buds3 FE** — already in catalog (verified).
- **Lenovo Legion Go 2 32GB/1TB Eclipse Black (83N0000BUS)** — already in catalog (pending). lenovo.com entry $1,099.99; top config $3,081.99.
- **Lenovo Legion Go S (SteamOS)** — already in catalog (verified).

### Samsung / Lenovo sweep — passed checks, not carried (strongest alternate, first draft)
- **Lenovo Legion Pro 7 Gen 10 AMD (83RU0002US, RTX 5070 Ti, 16")** — lenovo.com $2,799.99 (39% off est. value $4,562.99). NOT in the catalog. Not carried: Lenovo-direct-only (DECISIONS 015 concern), promo-sensitive est-value price, and the batch already carries three Lenovo picks. Strongest alternate if a slot opens at add time. (Rework: now queued Lenovo backlog B1 — see the Rework section.)

### Fresh picks, dropped on research (2026-11-20, first draft)
- **Sony WH-CH710N** — Best Buy shows "Clearance $142.99" (comp $149.99). Clearance-only — fails the rule.
- **Sony SRS-XB13** — Abt "no longer available"; speakerranking calls it discontinued; Newegg $98.99 seller unclear; Best Buy only a bundle listing. Discontinued signals.
- **Sony WH-XB910N** — Best Buy $120.61 "Unavailable" (3-day crawl); other crawls $199.99 list. Stock unclear — too weak.
- **JBL Tune 510BT White** — Best Buy "no longer available in new condition" (18-day crawl); refurbished $39.99 listings dominate. Replaced by Tune 520BT (entry 15).
- **Samsung Galaxy Tab S11 FE** — Not a real product: "Rumoured", expected release April 20, 2026, unofficial; no Best Buy listing. Search results showed Tab S11 non-FE instead.
- **ASUS RT-AXE7800 (standalone router)** — Best Buy standalone listing exists (SKU 6520863) but NO current price captured — last price $265.99 (64-day-old Q&A page); Big Apple Buddy says retail $279.99, OutOfStock. Replaced by the ZenWiFi AXE7800 3-pack (entry 34), a different product.
- **Microsoft Surface Dock 2 (SVS-00001)** — Best Buy shows "Clearance $73.99 (comp $259.99)" and marketplace rows $478.67. Clearance-only — fails the rule. Replaced by Surface Thunderbolt 4 Dock (entry 41).
- **Microsoft Modern Webcam (8L3-00001)** — Best Buy "Clearance $55.99 (comp $69.99), Unavailable". Clearance + unavailable — fails the rule.
- **Fitbit Versa 4 (FB523SRAG-US)** — Best Buy Platinum $159.95 Black Friday (comp $199.95), sold by Best Buy — but Sam's Club clearance $139 and a reviewer report says "being discontinued by Fitbit"; 2022 model superseded by the Pixel Watch line. Discontinuation signals — drop.
- **Bose Soundbar 550 (873984-1100)** — No Best Buy standalone listing found — only bundles/packages and the Smart Ultra. Klarna shows "$417.99, 1 store" (store unnamed). eBay $439.99/$324.99 (not usable), ShopAbunda used $269.99 (not usable), OfferUp $325 out of stock (not usable). No clean US retailer-direct row. Model 873984-1100 seen on eBay only — do not carry as verified.
- **Logitech G713** — No clean Best Buy row; Klarna aggregator $142.99 (3 stores), Compsource OOS $203.20, BuyDig White 920-010413 with no price shown.
- **Logitech G Pro X TKL Rapid** — Best Buy $189.99, SKU 13283045 / 6599038, but stock/seller signals mixed: one crawl shows "Sold Out / Sold & shipped by Walts TV" (marketplace seller). MPN not captured. Not carried.

### Alternates investigated and dropped in the rework (track D, 2026-11-20)
- **Alienware 16 Aurora (LAC16250-7469BLU-PUS)** — MPN VERIFIED (Newegg + D&H distributor spec); UPC 884116430469 VERIFIED (D&H + New Age distributor spec sheets). **HOLD — no clean retailer-direct price row:** Best Buy's three SKUs are all marketplace sellers (CompVoy $1,707.70, PC Heaven $1,649.00, antonline $2,195.01); Newegg seller unclear; antonline.com direct $2,149.99 does not show the model code. Do NOT add until a Sold-by-Best-Buy, sold-by-Newegg, or dell.com direct row is confirmed at add time.
- **HP OMEN Max 16 (2025)** — sold out at Best Buy in both configs (16-ah0043dx/B7HV2UA#ABA, $4,019.99; 16-ah0033dx/B69J2UA#ABA, $2,564.99); third config is PC Heaven marketplace, sold out.
- **ASUS Vivobook S14 S3407QA** — no clean US direct retail row: ASUS US page offers availability alerts, not a price; $799 was a January 2025 launch starting price, not a current quote.
- **Razer Blade 14 (2025) (RZ09-05305ES3-R3U1)** — no second qualifying MPN source; UPC 840272915042 only via camelcamelcamel (Amazon-derived, not qualifying); Best Buy availability ambiguous.
- **HP OmniBook Ultra 14" (Snapdragon X2 Elite, Stone Blue)** — no model number captured on the Best Buy page; Best Buy row $2,399.99 is "Sold & shipped by HP Inc" (brand store via Best Buy, not Sold by Best Buy).
- **Lenovo Legion Pro 7 Gen 10 AMD (83RU0002US) and Lenovo Yoga Slim 7x 2026** — dropped from track D by the method pivot; the dedicated Lenovo.com sweep owns them (see the Rework section — Pro 7 is queued Lenovo backlog B1; Yoga Slim 7x 83QR000AUS is queued backlog B2).

### Passed checks but cut to hold the batch at exactly 50 (first draft — SUPERSEDED by the rework)
- **Sony ULT Tower 10 Black (SRSULT1000)** — first draft: Best Buy $799.99 (comp $1,199.99), sold by Best Buy, SKU 6577679; MPN SRSULT1000 single source (Best Buy) — PENDING. **Rework: MPN now VERIFIED (B&H + Crutchfield); UPC 027242928978 PENDING (Adorama only). Not carried — the slots went to UPC-verified picks and the Lenovo 1:1 replacements; strongest non-carried alternate, see the Rework section.**
- **Logitech Signature Slim K950 Graphite** — first draft: Best Buy $89.99 (was $99.99), Add to cart. MPN PENDING, no lead. **Rework: CARRIED as entry 33 — both identifiers VERIFIED (see entry 33).**
- **Microsoft Surface Laptop 13" (2025) Snapdragon X Plus** — first draft: Best Buy Ocean 512GB $1,149.99 Black Friday (comp $1,249.99), Add to cart; Platinum 256GB $979.00 at Best Buy per Klarna. MPN PENDING, no lead. **Rework: CARRIED as entry 29 — both identifiers VERIFIED (see entry 29).**

### Batch-5 do-not-carry items (no genuinely new evidence, 2026-11-20)
- **Samsung Galaxy Buds Core** — not a US-market product.
- **Corsair K70 MAX RGB / Dell S2725H / Sony HT-S2000 / Sony SRS-XG300 / Razer Leviathan V2 Pro / Razer Kiyo Pro / Sony SRS-XG500 / Sony LinkBuds S** — discontinued or clearance-only.
- **Garmin Epix Pro Gen 2** — suspicious above-MSRP row.

---
*Draft only — do not modify `price_agent/catalog.py`, `DECISIONS.md`, `BUILD_LOG.md`, `CHANGELOG.md`, snapshots, or site files from this document. Add-time session: re-verify every price/stock state (Black Friday pricing ends Nov 28, 2026 at Best Buy), re-check the two flagged DECISIONS 015 brand-direct-only entries (slot 3 X1 Carbon — lenovo.com-only; slot 36 G16 7630 — Dell-direct, stale prices), confirm the ZenWiFi BT10 UPC on the Best Buy spec panel for SKU 11870821 (downgrade to PENDING if it does not agree), re-fetch the Micro Center Huntsman page (id 670527) for a clean MPN + UPC print, and confirm identifiers against two qualifying sources before marking anything VERIFIED. Research files: `data/rework6/trackA.md` … `trackG_asus.md`.*
