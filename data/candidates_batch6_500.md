# Batch 6 draft — 50 candidates (450 → 500)

- **Date:** 2026-11-20
- **Catalog state at draft time:** 450 models in `price_agent/catalog.py`, verified identifiers 194 / pending 256, ranking 148, matched 164. Repo HEAD `04ed2bc` (`feat: batch 5 — add 50 models (400 → 450), verified 173 → 194 (DECISIONS 084)`).
- **This batch:** 50 candidates, catalog 450 → 500. Final batch to the user's 500 target.
- **Identifier tally: VERIFIED 1 / PENDING 49. UPC verified: 0.** The single VERIFIED identifier is the JBL Tune 520BT MPN (JBLT520BTBLKAM — JBL.com item# + Best Buy Canada model field, two independent sources). Every other MPN/UPC in this batch is PENDING: most are single-source retailer model fields; several have no lead at all. Nothing here was upgraded on one source alone.
- **Brand counts (50):** Sony 4, Logitech 4, JBL 4, Razer 4, Samsung 4, Apple 3, Anker 3, Garmin 3, Lenovo 3, ASUS 2, Dell 2, HP 2, Meta 2, Keychron 2, HyperX 2, Microsoft 1, Google 1, Corsair 1, Bose 1, Alienware 1.

## Method note (read before add time)

- **Research was done directly in-session** (2026-11-20, via `browser.search` / `browser.open`). The task brief asked to fan out to parallel child agents, but this session runs at depth 2/2 with `can_spawn=no`, so no children could be spawned. Every per-model detail below traces to the batch-5 draft (`data/candidates_batch5_450.md`), or a search run directly in this session on 2026-11-20. No identifier, price, or SKU was reconstructed from memory or from a compacted summary.
- **Black Friday direction (added 2026-11-20, applied to this draft):** prefer models with live Black Friday pricing at brand-direct or retailer-direct channels; flag each promo price with its expiry where known. Best Buy Black Friday deals end **Nov 28, 2026** (per Best Buy banners in crawls); Samsung.com's Black Friday sale runs through **Nov 30, 2026** (per dealnews). No rule was relaxed for BF: still US-market, seller-direct only, no Amazon source in any form, no marketplace rows, identifiers VERIFIED only with two qualifying sources.
- **Samsung.com sweep (2026-11-20):** samsung.com wearables page (JSON-LD, 1 day old) lists Galaxy Watch8 Classic 46mm Black Wi-Fi/Bluetooth $499.99 InStock and Galaxy Watch8 40/44mm $299.99/$329.99 — all already in the catalog (Watch8 Classic verified, SM-L500NZKAXAA; Watch8 40/44mm verified; Watch9 40/44mm also in catalog). Galaxy Buds4 / Buds4 Pro / Buds3 FE already in catalog. Galaxy Tab S11 128GB Gray already in catalog — the exact-key duplicate the membership check caught (see below). Soundbar sweep: samsung.com CA lists HW-QS700F; the US row is Best Buy $347.99 Black Friday (ends Nov 28). HW-QS700F is carried as the Tab S11 replacement (entry 28).
- **Lenovo.com sweep (2026-11-20):** Legion Go Gen 2 (83N0000AUS; entry $1,099.99, top config $3,081.99) already in catalog (83N0000BUS, pending). Legion Go S SteamOS already in catalog. Legion Pro 7 Gen 10 AMD (83RU0002US, RTX 5070 Ti, $2,799.99 — 39% off est. value $4,562.99, lenovo.com) is NOT in the catalog — swept, not carried: Lenovo-direct-only (DECISIONS 015 concern) and the batch already carries three Lenovo picks; the open slot went to the cleaner Best Buy Black Friday row (HW-QS700F). Legion Pro 7 Gen 10 AMD is the strongest Lenovo-sweep alternate — see "Not carried".
- **Held items from batch 5 — carried 3, dropped 3 (all re-checked 2026-11-20):**
  - CARRY — Bose Solo Soundbar Series II: Bose.com $199.00 new; Costco $212.99 InStock same-day. Still no retailer spec page for the UPC (batch-5 blocker unresolved) — carried as PENDING.
  - CARRY — Razer Kiyo Pro Ultra 4K: Best Buy $429.95. UPC lead 840272900376 still conflicted; successor Kiyo V2 Pro announced 2026-09-24 at $299.99. Carried as PENDING with flags.
  - CARRY — Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition: Lenovo.com direct prices confirmed (pin 21NS0012US $1,248.99). Carried as PENDING; Lenovo-direct only, DECISIONS 015 concern.
  - DROP — HP 930 Creator Wireless Mouse: HP Malaysia page says Discontinued; Staples OOS everywhere. Confirmed discontinued/OOS.
  - DROP — ASUS ROG Strix XG27ACS: ASUS US $229 OutOfStock still; Newegg $283.99 seller unconfirmed; Walmart $229 seller unknown. No clean US retailer-direct in-stock row.
  - DROP — Corsair NIGHTSABRE Wireless: Corsair.com now OutOfStock at $149.99; worse than batch 5.
- **Membership check:** script `/tmp/batch6_membership.py` vs `/tmp/catalog_ref_450.tsv` (450 rows built from `price_agent/catalog.py`, 2026-11-20). Checks every candidate by exact key, model-name substring (normalized, both directions), MPN, and UPC. **Final run (after the Tab S11 → HW-QS700F swap): 0 true collisions; intra-batch duplicate keys: none.** The first run caught one true collision — `samsung-galaxy-tab-s11-128gb-gray` matched a catalog row on exact KEY (the Galaxy Tab S11 128GB Gray, SM-X730NZAAXAR, is already in the catalog). It was dropped and replaced with HW-QS700F, and the script was re-run. The 7 remaining hits are adjudicated siblings / false positives, not duplicates:
  - `logitech-signature-m650-l-graphite` vs in-catalog Signature M650 (non-L): M650 L is the larger full-size version, distinct model.
  - `razer-blackshark-v3-black` vs in-catalog BlackShark V3 Pro: standard vs Pro, distinct.
  - `razer-cobra-black` vs in-catalog Cobra Pro: wired vs wireless Pro, distinct.
  - `razer-huntsman-v3-pro-mini-black` vs in-catalog Huntsman V3 Pro: 60% Mini vs full-size, distinct.
  - `anker-soundcore-boom-2-plus-black` vs in-catalog Soundcore Boom 2: Plus vs base, distinct.
  - `garmin-venu-3s-pebble-gray` vs in-catalog Venu 3: 3S is 41mm, Venu 3 is 45mm, distinct.
  - `hyperx-cloud-iii-wireless-black` vs in-catalog Cloud II: false positive — "cloud ii" is a substring of "cloud iii" in the normalized match; different generation.
- **Prices are Black Friday-season snapshots (2026-11-20).** Most Best Buy rows are Black Friday deals ending Nov 28. Re-verify every price and stock state at add time; promo prices will move. Entries flag each promo price and its expiry where known.

## Candidates

### 1. Bose Solo Soundbar Series II — Black
- **Key:** `bose-solo-soundbar-series-ii-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Held from batch 5; re-checked 2026-11-20. Bose.com lists it new at $199.00 (fresh crawl); Costco same-day $212.99 InStock. Mainstream current Bose soundbar.
- **Identifiers:** MPN 845194-2100 (PENDING — from batch-5 draft; no second source). UPC PENDING, no lead — still no retailer spec page for the UPC (batch-5 blocker unresolved).
- **Price / stock:** Bose.com $199.00 new; Costco $212.99 InStock.
- **Flag:** Identifier pending — do not rank until a UPC lead is found on a retailer/manufacturer spec page.

### 2. Razer Kiyo Pro Ultra 4K — Black
- **Key:** `razer-kiyo-pro-ultra-4k-black`
- **Category:** webcams
- **Variant pinned:** Black, 4K
- **Why it qualifies:** Held from batch 5; re-checked 2026-11-20. Best Buy $429.95, SKU 11132802, model confirmed (2-day-old crawl).
- **Identifiers:** MPN RZ19-04420100-R3U1 (PENDING — single source, Best Buy model field). UPC lead 840272900376 (PENDING, CONFLICTED — Snapklik ties it to RZ19-04420100-R3U1; batch 5 noted an eBay listing tying the same code to Kiyo Pro RZ19-03640100-R3U1; eBay-only values are never verified).
- **Price / stock:** Best Buy $429.95. Price confusion persists: Razer direct $299.99 per reviews, other sources $399.99.
- **Flag:** Price conflict ($299.99 / $399.99 / $429.95 across sources — use Best Buy $429.95 as the row, re-check at add time). Supersession risk: successor Kiyo V2 Pro announced 2026-09-24 at $299.99 (also in this batch, entry 16, different model).

### 3. Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition
- **Key:** `lenovo-thinkpad-x1-carbon-gen-13-aura-edition`
- **Category:** laptops
- **Variant pinned:** 21NS0012US
- **Why it qualifies:** Held from batch 5 (dropped there for marketplace-only Best Buy rows); re-checked 2026-11-20. Lenovo.com direct prices confirmed.
- **Identifiers:** MPN 21NS0012US (PENDING — single source, lenovo.com). UPC PENDING, no lead found.
- **Price / stock:** Lenovo.com direct: 21NS0012US $1,248.99; 21NS017AUS $2,499; 21NS017BUS $2,259. Pin 21NS0012US at $1,248.99.
- **Flag:** Lenovo-direct only, no clean retailer row found — DECISIONS 015 concern (never track brand-direct-only configurations). Re-check Best Buy direct at add time.

### 4. Sony WF-C700N — Black
- **Key:** `sony-wf-c700n-black`
- **Category:** earbuds
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony noise-cancelling earbuds; Best Buy live Black Friday row.
- **Identifiers:** MPN WFC700N/B (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $79.99 Black Friday (comp $118) / $119.99 list.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 5. Sony INZONE H3 — White
- **Key:** `sony-inzone-h3-white`
- **Category:** headphones
- **Variant pinned:** White
- **Why it qualifies:** Mainstream Sony gaming headset; Best Buy White listing exists.
- **Identifiers:** MPN MDR-G300 (PENDING — single source, Best Buy White listing MDRG300/W, SKU 6510365). UPC PENDING, no lead found.
- **Price / stock:** Best Buy White listing live; Slickdeals reported Best Buy $78 (2026-04); Audio46 $69.99 sold out; Target bundle $118 via Focus Camera (third-party, not usable). Price ~$78–99 — re-check at add time.
- **Flag:** Current price not captured in-session; verify price/stock at add time.

### 6. Sony HT-A5000 — Black
- **Key:** `sony-ht-a5000-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony 5.1.2 Dolby Atmos soundbar; Best Buy in-stock direct row.
- **Identifiers:** MPN HT-A5000 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $499.99 InStock, sold by Best Buy, Add to cart.
- **Flag:** None.

### 7. Sony HT-S400 — Black
- **Key:** `sony-ht-s400-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Sony 2.1ch soundbar; Best Buy in-stock Black Friday row.
- **Identifiers:** MPN HT-S400 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $199.99 InStock (Black Friday; list $299.99, Sony direct $298).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 8. Logitech G435 — Black
- **Key:** `logitech-g435-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Logitech wireless gaming headset; Best Buy listing live.
- **Identifiers:** MPN 981-001049 (PENDING — single source, Best Buy model field, SKU 6478273). UPC PENDING, no lead found.
- **Price / stock:** Best Buy listing live. Current Black price NOT captured in search results (White shown $29.99 in one snippet) — re-check price at add time.
- **Flag:** Price not captured in-session; verify at add time.

### 9. Logitech Brio 100 — Graphite
- **Key:** `logitech-brio-100-graphite`
- **Category:** webcams
- **Variant pinned:** Graphite
- **Why it qualifies:** Mainstream Logitech 1080p webcam; Best Buy direct row.
- **Identifiers:** MPN 960-001580 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $39.99, sold by Best Buy, Add to cart.
- **Flag:** None.

### 10. Logitech Signature M650 L — Graphite
- **Key:** `logitech-signature-m650-l-graphite`
- **Category:** mice
- **Variant pinned:** Graphite, consumer (full-size L)
- **Why it qualifies:** Mainstream Logitech full-size wireless mouse; Best Buy direct Black Friday row. Distinct from in-catalog Signature M650 (non-L, standard size).
- **Identifiers:** MPN PENDING, no lead found (do not invent a part number). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $24.99 Black Friday (list $39.99), sold by Best Buy. The for-Business variant is a separate $39.99 listing — pin consumer only.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Identifier pending.

### 11. Logitech Zone Vibe 125 — Graphite
- **Key:** `logitech-zone-vibe-125-graphite`
- **Category:** headphones
- **Variant pinned:** Graphite
- **Why it qualifies:** Mainstream Logitech wireless headset; Best Buy direct row. Distinct from in-catalog Zone Vibe 100.
- **Identifiers:** MPN 981-001166 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $129.99.
- **Flag:** Zone Vibe Wireless Teams listing (981-001440) is a different model — pin 125 only.

### 12. JBL Authentics 200 — Black
- **Key:** `jbl-authentics-200-black`
- **Category:** speakers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream JBL home speaker; Best Buy direct Black Friday row.
- **Identifiers:** MPN JBLAUTH200BLKAM (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $189.95 Black Friday (comp $379.95).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 13. JBL PartyBox Encore Essential 2 — Black
- **Key:** `jbl-partybox-encore-essential-2-black`
- **Category:** speakers
- **Variant pinned:** Black, Essential 2
- **Why it qualifies:** Mainstream JBL party speaker; Best Buy list row plus Walmart-direct promo row.
- **Identifiers:** MPN JBLPBENCOREESS2AM (PENDING — single source, VIP Outlet). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $329.99 list, SKU 10209209; Walmart (sold by Walmart) $199.95 promo; Verizon $199.99.
- **Flag:** Promo price $199.95 vs $329.99 list. Premium Encore 2 with 2 mics is a different $400 model (JBLPBENCORE22MICAM) — pin Essential 2 only.

### 14. JBL Bar 500 — Black
- **Key:** `jbl-bar-500-black`
- **Category:** soundbars
- **Variant pinned:** Black, original Bar 500
- **Why it qualifies:** Mainstream JBL 5.1ch Dolby Atmos soundbar; Best Buy direct row.
- **Identifiers:** MPN BAR-500 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $399.95 (was $499.95).
- **Flag:** BAR500MK2 is the newer model at $449.95 (model JBLBAR500M2BLKAM, SKU 12375599), and one screenshot showed the MK2 sold by BrandsMartUSA (marketplace) — pin the original Bar 500.

### 15. JBL Tune 520BT — Black
- **Key:** `jbl-tune-520bt-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream JBL on-ear Bluetooth headphones; JBL.com direct row plus Walmart-direct row. Replaces the discontinued Tune 510BT (see "Not carried"). **The batch's only VERIFIED identifier.**
- **Identifiers:** MPN JBLT520BTBLKAM — **VERIFIED** (JBL.com manufacturer item# + Best Buy Canada model field, two independent sources). UPC PENDING, no lead found.
- **Price / stock:** JBL.com $34.95 (Item# JBLT520BTBLKAM); Walmart $34.95 (was $59.95); Target $59.99 OutOfStock; Best Buy Canada lists model JBLT520BTBLKAM. No Best Buy US listing found.
- **Flag:** Promo price $34.95 vs $59.95 list.

### 16. Razer Kiyo V2 Pro — Black
- **Key:** `razer-kiyo-v2-pro-black`
- **Category:** webcams
- **Variant pinned:** Black
- **Why it qualifies:** New Razer flagship webcam (announced 2026-09-24, 4K60, Sony STARVIS 2 sensor); Razer.com direct, available now. Successor to the held Kiyo Pro Ultra (entry 2, different model).
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Razer.com $299.99, available now, buy button live (per windowsforum). Best Buy search page exists but no direct price captured.
- **Flag:** No retailer-direct row captured yet — DECISIONS 015 concern (brand-direct-only). Identifier pending; re-check Best Buy direct at add time.

### 17. Razer BlackShark V3 — Black (PC version)
- **Key:** `razer-blackshark-v3-black`
- **Category:** headphones
- **Variant pinned:** Black, PC version
- **Why it qualifies:** Mainstream Razer wireless gaming headset; Best Buy direct Black Friday row. Distinct from in-catalog BlackShark V3 Pro.
- **Identifiers:** MPN PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy Black $129.99 (was $149.99), PC version; Target PS5 version $113.99, Xbox $127.99 — pin PC version.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Identifier pending.

### 18. Razer Cobra (wired) — Black
- **Key:** `razer-cobra-black`
- **Category:** mice
- **Variant pinned:** Black, wired
- **Why it qualifies:** Mainstream Razer wired gaming mouse; Best Buy direct Black Friday row. Distinct from in-catalog Cobra Pro (wireless).
- **Identifiers:** MPN RZ01-04650100-R3U1 (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $29.99 Black Friday (comp $39.99), sold by Best Buy (per 109-day-old crawl).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Pokémon edition RZ01-04650400-R3M1 ($44.99) is different — do not mix.

### 19. Razer Huntsman V3 Pro Mini 60% — Black
- **Key:** `razer-huntsman-v3-pro-mini-black`
- **Category:** keyboards
- **Variant pinned:** Black, 60% Mini (standard, not 8KHz)
- **Why it qualifies:** Mainstream Razer 60% analog-optical keyboard; Best Buy direct row. Distinct from in-catalog Huntsman V3 Pro (full-size).
- **Identifiers:** MPN not captured — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $128.99 (comp $179.99), sold by Best Buy (open-box Fair $59.99 listing confirms new $128.99); White $124.99.
- **Flag:** A newer "8KHz" version is being promoted by Razer (posts Oct 2026) — pin the standard Mini. Identifier pending.

### 20. Anker Soundcore Boom 2 Plus — Black
- **Key:** `anker-soundcore-boom-2-plus-black`
- **Category:** speakers
- **Variant pinned:** Black, Phantom Black
- **Why it qualifies:** Mainstream Anker outdoor speaker; soundcore.com direct row. Distinct from in-catalog Soundcore Boom 2.
- **Identifiers:** MPN A3134012 (PENDING — single source), SKU 6683800. UPC PENDING, no lead found.
- **Price / stock:** soundcore.com Phantom Black $159.99 (was $249.99). Best Buy standalone listing says "no longer available in new condition" (4-day crawl); Best Buy bundle listings exist ($174.99 with charger, $179.98 with Select 4 GO — bundles not usable as the row). Best Buy reviews show $169.99 (was $249.99).
- **Flag:** Best Buy standalone row is dead — carry via soundcore direct. Promo price $159.99 vs $249.99 list.

### 21. Anker Soundcore AeroFit 2 — Black
- **Key:** `anker-soundcore-aerofit-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, base model
- **Why it qualifies:** Mainstream Anker open-ear earbuds (launched 2026-11-02 per hifiverdict); Best Buy direct row.
- **Identifiers:** MPN/UPC PENDING, no lead found.
- **Price / stock:** Best Buy $79.99 (retail $99.99; launched $129.99). Target $69.99.
- **Flag:** AI Assistant version is a different listing at $109.99 (list $129.99, model A3874Z12 Obsidian Black) — pin base Black only. Identifier pending.

### 22. Anker Prime 67W GaN Wall Charger (3 Ports)
- **Key:** `anker-prime-67w-gan-charger`
- **Category:** chargers
- **Variant pinned:** 67W, 3-port GaN
- **Why it qualifies:** Mainstream Anker GaN charger; Anker.com direct row plus Newegg row.
- **Identifiers:** MPN A2669 (PENDING — single source, Anker.com). UPC PENDING — a Rakuten product URL contained the digits 00194644137373, which look like a GTIN form, but that is NOT a verified identifier from a retailer spec page; treat only as an unverified lead at most, never as verified.
- **Price / stock:** Anker.com $49.99; AnkerDirect via Best Buy $34.99 (Slickdeals 2026-11-02); Newegg $49.99.
- **Flag:** Promo price $34.99 vs $49.99 list. Correction: the brief's "65W A2698" was wrong — the current model is the 67W GaN Wall Charger (3 Ports), model A2669.

### 23. Garmin Venu 3S — Pebble Gray
- **Key:** `garmin-venu-3s-pebble-gray`
- **Category:** wearables
- **Variant pinned:** Pebble Gray, 41mm
- **Why it qualifies:** Mainstream Garmin smartwatch; Best Buy direct row. Distinct from in-catalog Venu 3 (45mm; 3S is 41mm).
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $299.99, sold by Best Buy, Add to cart (fresh crawl <1h).
- **Flag:** Identifier pending.

### 24. Garmin Approach S44 — Black
- **Key:** `garmin-approach-s44-black`
- **Category:** wearables
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Garmin golf smartwatch; Best Buy direct row.
- **Identifiers:** MPN lead 010-03009-00 (PENDING — single source, Staples listing via Klarna). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $249.99 (comp $299.99), sold by Best Buy.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 25. Garmin Edge 1040 Solar — Black
- **Key:** `garmin-edge-1040-solar-black`
- **Category:** cycling-computers
- **Variant pinned:** Black, Solar
- **Why it qualifies:** Mainstream Garmin bike computer; Best Buy direct row. Replaces the non-Solar Edge 1040, whose Best Buy listing says "no longer available in new condition". Distinct from in-catalog Edge 1050.
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy Edge 1040 Solar $599.99 (was $699.99).
- **Flag:** Pin Solar only. Identifier pending.

### 26. Samsung Galaxy SmartTag 2 — Black
- **Key:** `samsung-galaxy-smarttag-2-black`
- **Category:** trackers
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Samsung Bluetooth tracker; Best Buy direct row.
- **Identifiers:** MPN EI-T5600BBEGUS (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $25.00 (comp $29.99), sold by Best Buy. Price fluctuates $25–$26.93 across crawls (promo).
- **Flag:** Promo-sensitive price — re-check at add time.

### 27. Samsung HW-Q800F — Black
- **Key:** `samsung-hw-q800f-black`
- **Category:** soundbars
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Samsung 5.1.2 Dolby Atmos soundbar (2025); Best Buy direct list row. Distinct from in-catalog HW-Q990F.
- **Identifiers:** MPN HW-Q800F/ZA (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $1,099.99 list, model HW-Q800F/ZA; some crawls show $537.99 marketplace rows / "Sold Out" flags.
- **Flag:** Best Buy direct row $1,099.99 needs re-check at add time — marketplace rows at $537.99 are not usable.

### 28. Samsung HW-QS700F — Black
- **Key:** `samsung-hw-qs700f-black`
- **Category:** soundbars
- **Variant pinned:** Black, 3.1.2ch convertible
- **Why it qualifies:** Mainstream Samsung 2025 soundbar (Convertible Flip design, Wireless Dolby Atmos, SpaceFit Sound Pro, Q-Symphony); Best Buy direct Black Friday row plus Crutchfield in-stock row. **Replacement for the Galaxy Tab S11 128GB Gray, which the membership check found already in the catalog (exact-key duplicate).** Found via the Samsung soundbar sweep: samsung.com CA lists the model; the US price row is Best Buy. Distinct from in-catalog HW-Q990F and in-batch HW-Q800F.
- **Identifiers:** MPN HW-QS700F/ZA (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $347.99 Black Friday (list $699.99), model HW-QS700F/ZA; Crutchfield $597.99 (list $697.99), InStock, free shipping.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Crutchfield $597.99 is the non-promo reference; re-check both at add time.

### 29. Samsung Odyssey G5 G55H 27" — Black
- **Key:** `samsung-odyssey-g5-g55h-27-black`
- **Category:** monitors
- **Variant pinned:** Black, 27", curved G55H
- **Why it qualifies:** Mainstream Samsung gaming monitor; Best Buy direct Black Friday row.
- **Identifiers:** MPN LS27HG552ENXZA (PENDING — single source, Best Buy model field), SKU 6685398. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $149.99 Black Friday (comp $299.99), sold by Best Buy (Slickdeals confirms $149.99 at Best Buy Nov 10).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. The G50D flat IPS variant also exists ($313 in one crawl) — pin G55H curved only.

### 30. Apple 140W USB-C Power Adapter — White
- **Key:** `apple-140w-usb-c-power-adapter-white`
- **Category:** chargers
- **Variant pinned:** White, new model
- **Why it qualifies:** Mainstream Apple charger; Best Buy direct row.
- **Identifiers:** MPN MKFQ4AM/A (PENDING — single source, Best Buy model field), SKU 6530838. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $99.00, sold by Best Buy.
- **Flag:** Two Best Buy SKUs exist (old 6485370 vs new MKFQ4AM/A 6530838); pin the new MKFQ4AM/A.

### 31. Apple 35W Dual USB-C Port Compact Power Adapter — White
- **Key:** `apple-35w-dual-usb-c-compact-power-adapter-white`
- **Category:** chargers
- **Variant pinned:** White, compact
- **Why it qualifies:** Mainstream Apple dual-port charger; Best Buy direct row.
- **Identifiers:** MPN MW2H3AM/A (PENDING — single source, an in-store price-tag photo on Instagram). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $59.00 list; some crawls show $49.99 (promo-sensitive).
- **Flag:** Promo-sensitive price ($49.99 vs $59.00 list). MW2K3AM/A is the non-compact larger version — pin compact only.

### 32. Apple Magic Keyboard for iPad Air 11" (M2) — White
- **Key:** `apple-magic-keyboard-ipad-air-11-m2-white`
- **Category:** keyboards
- **Variant pinned:** White, M2
- **Why it qualifies:** Mainstream Apple iPad keyboard; Apple.com is the primary row. Best Buy new listings are marketplace-only, so this is carried on the Apple.com row with a DECISIONS 015 flag.
- **Identifiers:** MPN MJQJ3LL/A (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy new listings sold by HHGregg (marketplace) at $261.99–$262.99; refurbished $149.99. No Best Buy-direct new row captured. Apple.com as primary row ($269 list implied by a Threads post noting a $269 → $200 reduction — price NOT captured from Apple.com in-session, verify at add time).
- **Flag:** Best Buy marketplace-only + DECISIONS 015 concern. Price not captured from Apple.com in-session — verify at add time. M4 version White $259.99 also exists at Best Buy (seller unclear) — pin M2 only.

### 33. ASUS ROG Falchion Ace HFX — Black
- **Key:** `asus-rog-falchion-ace-hfx-black`
- **Category:** keyboards
- **Variant pinned:** Black, standard (M605)
- **Why it qualifies:** Mainstream ASUS 65% gaming keyboard; Best Buy direct Black Friday row. Distinct from in-catalog ROG Falchion RX Low Profile.
- **Identifiers:** MPN ROG FALCHION ACE M605 (PENDING — single source). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $119.99 Black Friday (comp $199.99) per 2-day crawl; other crawls $147.99.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026; price varies $119.99–$147.99 across crawls, re-check at add time. ZywOo edition M606 is a different variant — pin standard Black M605 only.

### 34. ASUS ZenWiFi AXE7800 Tri-Band Mesh Wi-Fi 6E System (3-Pack) — White
- **Key:** `asus-zenwifi-axe7800-3-pack-white`
- **Category:** networking
- **Variant pinned:** White, 3-pack
- **Why it qualifies:** Mainstream ASUS tri-band Wi-Fi 6E mesh system; Best Buy direct Black Friday row. Replaces the standalone RT-AXE7800 router (no current direct price — see "Not carried"). Different product from the standalone router.
- **Identifiers:** MPN ZenWiFi AXE7800 (PENDING — single source). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $302.49 (Black Friday; list ~$399.99 per review).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026.

### 35. Dell XPS 14 9440 — Platinum
- **Key:** `dell-xps-14-9440-platinum`
- **Category:** laptops
- **Variant pinned:** Platinum, config XPS9440-7816SLV-PUS (Ultra 7, RTX 4050, 1TB, FHD)
- **Why it qualifies:** Mainstream Dell premium laptop; Best Buy row for the pinned config.
- **Identifiers:** MPN/config XPS9440-7816SLV-PUS (PENDING — single source, Best Buy Q&A page). UPC PENDING, no lead found.
- **Price / stock:** Best Buy Q&A page shows $1,199.99 for config XPS9440-7816SLV-PUS; Smartprix lowest $1,222.99.
- **Flag:** Price from a Q&A page (2-day crawl), not a product page; re-check at add time.

### 36. Dell G16 7630 — Gray
- **Key:** `dell-g16-7630-gray`
- **Category:** laptops
- **Variant pinned:** Gray, RTX 4070 / i9-13900HX / 32GB / 1TB (Dell-direct config)
- **Why it qualifies:** Mainstream Dell gaming laptop; Dell-direct row. Best Buy only shows an "Upgraded" third-party config (not usable).
- **Identifiers:** MPN 7630 model; specific config unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Dell direct: RTX 4070 i9-13900HX 32GB/1TB at $1,169–$1,299 (Notebookcheck, multiple reports, coupon-dependent). Best Buy only shows an "Upgraded" third-party config at $2,879 (model G16-7630-Upgraded) — not usable.
- **Flag:** Dell-direct only, coupon-dependent promo price (~$1,169 with 10% newsletter coupon / $1,299 sale price); no clean Best Buy direct row. Re-check at add time.

### 37. HP Victus 15 (15-fb3093dx) — Mica Silver
- **Key:** `hp-victus-15-fb3093dx-mica-silver`
- **Category:** laptops
- **Variant pinned:** Mica Silver, 15-fb3093dx (Ryzen 7 7445HS, RTX 4050, 16GB, 512GB)
- **Why it qualifies:** Mainstream HP gaming laptop; Best Buy direct Holiday Deal row.
- **Identifiers:** MPN 15-fb3093dx / BM4X8UA#ABA (PENDING — single source, Best Buy model field), SKU 6623881. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $949.99 (Holiday Deal). One snippet mentions $639.99 for the same specs (possibly an older deal price).
- **Flag:** Price volatility ($639.99 vs $949.99) — re-check at add time.

### 38. HP 430 Multi-Device Wireless Mouse — Black
- **Key:** `hp-430-multi-device-wireless-mouse-black`
- **Category:** mice
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream HP multi-device wireless mouse; Best Buy direct row.
- **Identifiers:** MPN unknown — PENDING, no lead found (do NOT write 3B4Q2AA — it was not captured in-session). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $28.99 (9-day crawl; list $48.99 / comp $60.70).
- **Flag:** Promo price. Identifier pending.

### 39. Lenovo Legion Pro 5 16IRX9 — Onyx Grey
- **Key:** `lenovo-legion-pro-5-16irx9-onyx-grey`
- **Category:** laptops
- **Variant pinned:** Onyx Grey, 16IRX9 (i9 14th gen, RTX 4070, 32GB, 2TB), 83DF00A8US
- **Why it qualifies:** Mainstream Lenovo gaming laptop; Best Buy row for the pinned config.
- **Identifiers:** MPN 83DF00A8US (PENDING — single source, Best Buy Q&A page). UPC PENDING, no lead found.
- **Price / stock:** Best Buy Q&A shows 83DF00A8US at $1,799.99.
- **Flag:** Price from a Q&A page; re-check at add time. Newer 83LT000MUS (Ryzen 9 8945HX, RTX 5060) exists at $1,179.99 — pin 16IRX9 only.

### 40. Lenovo ThinkPad T14 Gen 6 — Black
- **Key:** `lenovo-thinkpad-t14-gen-6-black`
- **Category:** laptops
- **Variant pinned:** Black, 21QJ00CSUS
- **Why it qualifies:** Mainstream Lenovo business laptop; Lenovo.com is the row (all Best Buy listings are marketplace sellers).
- **Identifiers:** MPN 21QJ00CSUS (PENDING — single source, a marketplace listing; weak lead). UPC PENDING, no lead found.
- **Price / stock:** All Best Buy listings are marketplace sellers (Mobile Advance $1,744.14 for 21QJ00CSUS; Merchant Expo $1,524.16 for 21QG00DJUS; PC Heaven / IST Computers "Upgraded" listings). No Best Buy-direct row. Pin 21QJ00CSUS with Lenovo.com as the row — price NOT captured this session, verify at add time.
- **Flag:** Marketplace-only at Best Buy + DECISIONS 015 concern (Lenovo-direct-only). Price not captured in-session — verify at add time.

### 41. Microsoft Surface Thunderbolt 4 Dock — Black
- **Key:** `microsoft-surface-thunderbolt-4-dock-black`
- **Category:** docks
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream Microsoft dock; Best Buy direct row. Replaces the Surface Dock 2 (clearance-only — see "Not carried").
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $299.99 (one crawl $214.99 — promo-sensitive), sold by Best Buy, Add to cart.
- **Flag:** Promo-sensitive price — varies $214.99–$299.99 across crawls; use $299.99, re-check at add time. Identifier pending.

### 42. Meta Oakley Meta Vanguard (Prizm Black lenses) — White
- **Key:** `meta-oakley-vanguard-prizm-black-white`
- **Category:** smart-glasses
- **Variant pinned:** White, Prizm Black lenses
- **Why it qualifies:** Mainstream Meta smart glasses (Oakley line); Best Buy direct Black Friday row. Distinct from in-catalog Oakley Meta HSTN.
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $424.00 Black Friday (comp $499.00), Add to cart; Prizm 24K Black $499.00. Pin Prizm Black White at $424.00 (promo, list $499.00).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Identifier pending.

### 43. Meta Ray-Ban Meta Skyler (Gen 2) (Green lenses) — Shiny Black
- **Key:** `meta-ray-ban-skyler-gen-2-green-shiny-black`
- **Category:** smart-glasses
- **Variant pinned:** Shiny Black, Green lenses
- **Why it qualifies:** Mainstream Meta smart glasses (Ray-Ban line, Gen 2); Best Buy direct row, meta.com also $379.
- **Identifiers:** MPN lead 0RW4014_601/7152 (PENDING — single source, Best Buy Q&A). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $379.00; meta.com also $379.
- **Flag:** Transitions variants $459 — pin Green only.

### 44. Google Nest Hub (2nd Gen) — Charcoal
- **Key:** `google-nest-hub-2nd-gen-charcoal`
- **Category:** smart-home
- **Variant pinned:** Charcoal
- **Why it qualifies:** Mainstream Google smart display; Best Buy direct list row.
- **Identifiers:** MPN GA01892-US (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $99.99 list. One crawl showed Chalk "Sold Out" — Charcoal listing $99.99 live.
- **Flag:** 2021 hardware (5 years old), frequently discounted to $49.99–$59.99; $99.99 is list. Not discontinued, but age noted.

### 45. Keychron K11 Max — Black (Alice layout)
- **Key:** `keychron-k11-max-black`
- **Category:** keyboards
- **Variant pinned:** Black, Alice layout
- **Why it qualifies:** Mainstream Keychron Alice-layout wireless keyboard; Keychron direct row.
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Keychron direct $89.00 (keeb-finder, multiple comparisons: "$89 at Keychron"). Best Buy search page exists (54-day crawl) but NO product page/price captured.
- **Flag:** Brand-direct-only, DECISIONS 015 concern; price $89 per keeb-finder tracking, verify at add time. Note: keychroncompany.us / keychron-shop.us ($35–43 prices) are lookalike domains, NOT official keychron.com — do not use. Identifier pending.

### 46. Keychron Q0 Max — Carbon Black
- **Key:** `keychron-q0-max-carbon-black`
- **Category:** keyboards
- **Variant pinned:** Carbon Black, Fully Assembled Knob, Gateron Jupiter Red
- **Why it qualifies:** Mainstream Keychron Q-series number pad; Keychron.com direct row.
- **Identifiers:** MPN: Keychron's own SKU Q0M-M1 (PENDING — single source). UPC PENDING, no lead found.
- **Price / stock:** Keychron.com direct $113.99 (was $129.99), Fully Assembled Knob / Carbon Black / Gateron Jupiter Red Available. Brand-direct only (no Best Buy found).
- **Flag:** DECISIONS 015 concern (brand-direct-only). Promo price $113.99 vs $129.99 list. **It is a NUMBER PAD, not a keyboard** — note that at add time.

### 47. HyperX Cloud III Wireless — Black
- **Key:** `hyperx-cloud-iii-wireless-black`
- **Category:** headphones
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream HyperX wireless gaming headset; Best Buy direct row. Distinct from in-catalog Cloud III S Wireless.
- **Identifiers:** MPN 77Z45AA (PENDING — single source, Best Buy model field). UPC PENDING, no lead found.
- **Price / stock:** Best Buy $149.99 (one crawl $174.49 — price varies), 1-day and 8-day crawls.
- **Flag:** Promo-sensitive price ($149.99 vs $174.49 across crawls) — re-check at add time.

### 48. HyperX Alloy Origins 60 — Black
- **Key:** `hyperx-alloy-origins-60-black`
- **Category:** keyboards
- **Variant pinned:** Black
- **Why it qualifies:** Mainstream HyperX 60% gaming keyboard; Best Buy direct row. Distinct from in-catalog Alloy Origins 65.
- **Identifiers:** MPN 4P5N4AA#ABA (PENDING — single source, Best Buy model field) / HKBO1S-RB-US/G. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $77.99–$86.99 (comp $114.99).
- **Flag:** Promo-sensitive price (varies $77.99–$114.99 across crawls) — re-check at add time.

### 49. Corsair K65 PRO MINI — Black (OPX)
- **Key:** `corsair-k65-pro-mini-black`
- **Category:** keyboards
- **Variant pinned:** Black, OPX optical switches
- **Why it qualifies:** Mainstream Corsair 60% keyboard; Corsair direct + Best Buy promo rows. Distinct from in-catalog K65 Plus Wireless (wired optical OPX vs wireless).
- **Identifiers:** MPN unknown — PENDING, no lead found. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $149.99 list; crawls show $72.98–$76.99 (comp $149.99); Corsair direct $79.99 per pricertoday. Pin $79.99 (Corsair direct / Best Buy promo).
- **Flag:** Promo price — list $149.99, promo ~$73–$80. Identifier pending.

### 50. Alienware 18 Area-51 (Ultra 9 275HX, RTX 5070 Ti, 32GB, 2TB) — Liquid Teal
- **Key:** `alienware-18-area-51-rtx-5070-ti-2tb-liquid-teal`
- **Category:** laptops
- **Variant pinned:** Liquid Teal, Ultra 9 275HX / RTX 5070 Ti / 32GB / 2TB, LAA18250-9444BLU-PUS
- **Why it qualifies:** Mainstream Alienware flagship gaming laptop; Best Buy direct row. Distinct from in-catalog 16 Area-51 (same config family, 16-inch). Alienware had zero picks in the batch before this entry.
- **Identifiers:** MPN LAA18250-9444BLU-PUS (PENDING — single source, Best Buy model field), SKU 12741185. UPC PENDING, no lead found.
- **Price / stock:** Best Buy $3,949.00. Price varies $3,369.99–$3,999 across crawls (one $3,378.99 clearance row — ignore, use $3,949 new).
- **Flag:** Price varies across crawls — re-check at add time. Do not use the $3,378.99 clearance row.

## Not carried

### Held items, dropped on re-check (2026-11-20)
- **HP 930 Creator Wireless Mouse (1D0K9AA)** — HP Malaysia page says Discontinued; Staples OOS everywhere ($81.49/$99.99 listings all Out of stock). Confirmed discontinued/OOS — do not carry.
- **ASUS ROG Strix XG27ACS** — ASUS US $229 OutOfStock still; Newegg $283.99 seller unconfirmed; Walmart $229 seller unknown. No clean US retailer-direct in-stock row — drop again.
- **Corsair NIGHTSABRE Wireless (CH-931B011-NA)** — Corsair.com now OutOfStock at $149.99; Newegg $149.99 seller unclear; ShopAbunda $99.99 is Amazon-fulfilled (not usable). Worse than batch 5 — drop.

### Duplicate found by the membership check (2026-11-20)
- **Samsung Galaxy Tab S11 128GB Gray (SM-X730NZAAXAR)** — already in the catalog (exact key `samsung-galaxy-tab-s11-128gb-gray`). Was the planned 50th model; dropped and replaced with HW-QS700F (entry 28). Best Buy $699.99 Black Friday (list $999.99) was the row — do not re-add.

### Samsung / Lenovo sweep — already in the catalog (2026-11-20)
- **Samsung Galaxy Watch8 Classic 46mm Black (SM-L500NZKAXAA)** — already in catalog (verified). samsung.com $499.99 InStock.
- **Samsung Galaxy Watch8 40mm / 44mm Graphite** — already in catalog (verified). samsung.com $299.99 / $329.99.
- **Samsung Galaxy Watch9 40mm / 44mm Graphite** — already in catalog (verified).
- **Samsung Galaxy Buds4 / Buds4 Pro / Buds3 FE** — already in catalog (verified).
- **Lenovo Legion Go 2 32GB/1TB Eclipse Black (83N0000BUS)** — already in catalog (pending). lenovo.com entry $1,099.99; top config $3,081.99.
- **Lenovo Legion Go S (SteamOS)** — already in catalog (verified).

### Samsung / Lenovo sweep — passed checks, not carried (strongest alternate)
- **Lenovo Legion Pro 7 Gen 10 AMD (83RU0002US, RTX 5070 Ti, 16")** — lenovo.com $2,799.99 (39% off est. value $4,562.99). NOT in the catalog. Not carried: Lenovo-direct-only (DECISIONS 015 concern), promo-sensitive est-value price, and the batch already carries three Lenovo picks. Strongest alternate if a slot opens at add time.

### Fresh picks, dropped on research (2026-11-20)
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

### Passed checks but cut to hold the batch at exactly 50 (strongest alternates)
- **Sony ULT Tower 10 Black (SRSULT1000)** — Best Buy $799.99 (comp $1,199.99), sold by Best Buy, SKU 6577679; Costco $789.99/$799.99. MPN SRSULT1000 single source (Best Buy) — PENDING. Distinct from in-catalog ULT TOWER 9/7/5/MAX. Promo price — Black Friday ends Nov 28, 2026.
- **Logitech Signature Slim K950 Graphite** — Best Buy $89.99 (was $99.99), Add to cart. MPN PENDING, no lead. Note: K980 Solar+ ($99.99) and MK950 combo are different models — pin K950 standalone Graphite only.
- **Microsoft Surface Laptop 13" (2025) Snapdragon X Plus** — Best Buy Ocean 512GB $1,149.99 Black Friday (comp $1,249.99), Add to cart; Platinum 256GB $979.00 at Best Buy per Klarna. MPN PENDING, no lead. Distinct from in-catalog Surface Laptop 13.8" 8th Edition and 15" 8th Edition. Promo price — Black Friday ends Nov 28, 2026.

### Batch-5 do-not-carry items (no genuinely new evidence, 2026-11-20)
- **Samsung Galaxy Buds Core** — not a US-market product.
- **Corsair K70 MAX RGB / Dell S2725H / Sony HT-S2000 / Sony SRS-XG300 / Razer Leviathan V2 Pro / Razer Kiyo Pro / Sony SRS-XG500 / Sony LinkBuds S** — discontinued or clearance-only.
- **Garmin Epix Pro Gen 2** — suspicious above-MSRP row.

---
*Draft only — do not modify `price_agent/catalog.py`, `DECISIONS.md`, `BUILD_LOG.md`, `CHANGELOG.md`, snapshots, or site files from this document. Add-time session: re-verify every price/stock state (Black Friday pricing ends Nov 28, 2026 at Best Buy), re-check the flagged DECISIONS 015 brand-direct-only entries (3, 16, 32, 40, 45, 46, 36) for a retailer-direct row, and confirm identifiers against two qualifying sources before marking anything VERIFIED.*
