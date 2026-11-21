# Batch 7 draft — 50 candidates (500 → 550)

- **Date:** 2026-11-21 (research in-session, all prices/stock as crawled 2026-11-21; Best Buy Black Friday deals end Nov 28, 2026).
- **Catalog state at draft time:** 500 models in `price_agent/catalog.py`, verified identifiers 211 / pending 289, ranking 151, matched 168, total offers 2,381. Repo HEAD `cd6acce` (`chore: daily refresh 2026-11-21 — 65 moves, 5 page-confirmed cuts, ranking 151`).
- **This batch:** 50 candidates, catalog 500 → 550. First batch past the user's 500 target, built on the deal-site gap-check method (DECISIONS 020, secondary signal only — see Method below).
- **Identifier tally: MPN VERIFIED 39 / 50 (78%). UPC/EAN VERIFIED 18 / 50 (36%). UPC PENDING 32 / 50.** Caveat-verified items are counted as VERIFIED (same as batch 6): S84H MPN (parts-page 2nd leg), XG27UCG UPC (ASUS brochure leg), OmniBook 3 MPN (HP datasheet hosted on Best Buy static), Osmo 360 Standard MPN + UPC (DroneNerds legs), M70F MPN (URL legs), OpenRun Air 2 UPC (non-US retailer sources — confirm on Best Buy spec panel at add time), Marshall Monitor III EAN (EAN, not a 12-digit US UPC — counts per the Keychron EAN+SKU precedent). If the batch lifts verified identifiers 211 → 229 as approved. The UPC rate (36%) is below batches 4–5 (46% / 42%) and in line with batch 6 (36%) — structural: TV and phone UPCs are rarely printed on two qualifying spec pages. No rule was loosened to reach a higher number.
- **Brand counts (50):** Samsung 6, Lenovo 6, Shokz 4, DJI 4, Motorola 3, ASUS 3, Sonos 2, Beats 2, Apple 2, Amazon 2, Marshall 1, Skullcandy 1, Turtle Beach 1, Technics 1, Sennheiser 1, Anker 1, Google 1, Hisense 1, TCL 1, Harman Kardon 1, GoPro 1, Insta360 1, HP 1, MSI 1, Logitech 1, Sony 1. (Bose, Keychron, Alienware, Dell, Corsair, Garmin, Meta, HyperX, Microsoft, JBL, Razer, LG, Nintendo: 0.)
- **Category counts (50):** laptops 9, earbuds 6, headphones 6, phones 5 (new), action-cameras 5 (new), speakers 4, soundbars 3, tvs 3 (new), monitors 3, smart-home 2, accessories 1, cameras 1, microphones 1, wearables 1. New categories are `tvs`, `phones`, `action-cameras` only — `cameras` already exists (Switch 2 Camera) and `microphones` already exists (5 models), so Pocket 3 and Yeti GX join existing categories.
- **Source split (50):** deal-site gap-check 38 + Track E substitute 1 (Osmo 360 Standard Combo, replacing the dropped Skiing Combo) + batch-6 queue top-ups 11 = 50. The two sources are labeled per entry and must not be confused.

## Method — deal-site gap-check (DECISIONS 020, secondary signal only)

**What happened:** the user approved (2026-11-21 12:50 PT) preparing batch 7 on the deal-site gap-check method: Slickdeals Tech (https://slickdeals.net/deals/tech/ + Black Friday Sift hot list, community saves = demand signal) as the primary signal, DealMoon Electronics & Computers (https://www.dealmoon.com/en/electronics-computers) as cross-check. Candidates must be absent from the 500-model catalog and appear repeatedly on the deal lists; brand official catalogs stay the selection backbone and the identifier rules are unchanged (DECISIONS 020/021). The user's correction that stands behind this batch: DECISIONS 020(a)'s audience-skew argument does not hold for the electronics shelf — DealMoon's electronics page is US-mainstream stock (Apple/Samsung/Sony/Logitech, Target/Best Buy/Walmart); the diaspora skew shows in its mobile-plan deals, not in electronics. DECISIONS 020(b) deal-ephemerality and (c) commercial bias still apply, which is why deal sites are only a gap-check signal, never the selector.

**Research:** 7 parallel child tracks, findings in `data/rework7/` (`trackA.md` Shokz/Sonos, `trackB.md` headphones/earbuds, `trackC.md` phones/wearables, `trackD.md` TVs/soundbars, `trackE.md` action cameras/laptops, `trackF.md` displays/accessories/queue, `trackG.md` backfill 3 of 50). The method follows the batch-6 rework: sweep the hot lists, then verify identifiers per model on brand/retailer spec pages, taking only what verifies. Every per-model detail below traces to one of those seven findings files or a search run in this session. No identifier, price, or SKU was reconstructed from memory or from a compacted summary.

**Deal-site evidence, honestly recorded:** several brief-cited posts could not be independently re-located and are marked as brief-only in the entries (Turtle Beach Slickdeals Sift, Technics DealMoon, Anker Space 2 Pro Slickdeals Tech, Marshall Best Buy Sift, MAG 321UP Slickdeals thread for the B&H price, S84H/HW-B650F Sift threads, AirTag Tech front-page placement). Slickdeals thread pages expose Deal Score/Views, not a saves count; Sift saves are recorded where the Sift table shows them — several show **0 saves**, recorded as-is. A model is carried on its retailer-direct row and identifiers, not on the strength of its deal post; a missing post never blocks a carry, and a found post never substitutes for verification.

**Brief corrections (coordinator's calls, recorded here so they can be re-judged):**
- Yeti GX Black MPN is **988-000567**, not the brief's guessed 988-000570 (which does not exist for this mic).
- Echo Show 8 Best Buy price is **$129.99**, not $99.99.
- Action 4 ($155.35), Action 6 ($376), GoPro LIT Hero ($169.99) brief prices are all Amazon-only and unusable; direct rows are DJI $169.00 / $426.00 and Best Buy $269.99. Insta360 Ace Pro 2's $309.99 is a June 2026 expired Slickdeals price; current Costco price is $389.99. Osmo 360 Standard's $404.77 is the Nov 16 price; live price is $417.99.
- The brief's MPN guess for Osmo 360 Standard ("约 CP.OS.00000441.04") is superseded by CP.OS.00000441.02 (Abt + B&H slug + DroneNerds + Abt blog); .04 has no retailer page behind it. Best Buy prints .01 — adjudicated in the entry.
- Anker Space 2 Pro's brief-implied MPN "A3068" is wrong; the real MPN is D1406Z11.
- Samsung S84H's MPN is **QN65S84HAEXZA** (OLEDs use the QN prefix), not the brief's "约 UN65S84H".
- Hisense M7 75" US model is **75M7SR** (Roku), not the brief's shorthand "75M7"; the Canadian 75M7SG is a different variant.
- The brief's premise that the catalog already contains Beats and Sennheiser models is wrong — zero rows for either brand (Track B grep). Nothing to distinguish against; no candidate was dropped on membership.
- IdeaPad 5 key changed from Track E's `…-14-black` to `…-14-luna-grey` — color pinned by Target (Luna Grey).
- Track E's "new category" note for Pocket 3 is wrong — `cameras` already exists (Switch 2 Camera); Pocket 3 joins it. `microphones` also already exists (5 models).

**Coordinator decisions (recorded here so they can be re-judged):**
- New categories `tvs`, `phones`, `action-cameras` are confirmed as the names. Pocket 3 goes in existing `cameras` (not `action-cameras` — it is a gimbal camera); Action 4 / Action 6 / LIT Hero / Ace Pro 2 / Osmo 360 Standard go in `action-cameras`.
- Marshall Monitor III's EAN 7340055411479 counts as VERIFIED (Keychron EAN+SKU precedent; catalog "verified" = UPC/EAN verified).
- Caveat-verified items stay VERIFIED (see tally note above); each caveat is written in its entry, and the strictest-reading downgrade path is noted where it exists (S84H MPN, XG27UCG UPC, Osmo 360 MPN/UPC).
- Echo Show 8 + Echo Hub are carried under the existing `smart-home` category (same as Nest Hub, admitted batch 6 — which supersedes the batch-3 "smart home, out of scope" line; the batch-3 Echo Show 8 removal was driven by both-identifiers-pending weakness, not a category ban). Flagged: if the user wants smart displays out, drop both together at approval.
- TCL Q6CH is carried on the warehouse-only $199.99 price, flagged carry-vs-hold (Costco.com is OOS at $299.99; the snapshot feed may not capture the warehouse price).
- Shokz OpenFit 2 SE is the swap-out candidate (both identifiers PENDING, Costco stock signals conflict) — if the batch needs a verified-only bar, drop entry 1 first.
- Legion 5i 83LY0000US is NOT carried (Walmart $1,499 row could not be opened directly — bot wall on both routes; three independent trackers corroborate the price but it is second-hand). It stays in the Lenovo backlog; do not force it in to reach 50.
- Distributor second sources ACCEPTED where they match the batch-5/6 precedent (retailer + distributor): LS50H UPC (Walts + Precision), U7900H UPC lead (P&C Richard spec-sheet PDF, single source — PENDING), Yeti GX UPC (B&H + CompSource + Logitech datasheet), LIT Hero UPC (B&H + GoPro sell-sheet PDF via Aqipa), XG27UCG UPC (CompSource + ASUS brochure — caveat), E16 Gen 3 UPC (B&H + Lenovo PSREF), OpenRun Air 2 UPC (PBTech NZ + MobileCiti AU — both non-US retailers; confirm on Best Buy spec panel at add time).
- **Prices are Black Friday-season snapshots (2026-11-21).** Most Best Buy rows are Black Friday deals ending Nov 28; Costco Holiday Savings ends Nov 30. Re-verify every price and stock state at add time; promo prices will move.

## Candidates

### 1. Shokz OpenFit 2 SE — Black (Costco exclusive) [SWAP-OUT CANDIDATE — both identifiers pending]
- **Key:** `shokz-openfit-2-se-black`
- **Category:** earbuds
- **Variant pinned:** Black, Costco-exclusive trim. Costco item 1926991, model code T920-ST-CB-US-326-COS.
- **Why it qualifies:** Mainstream current Shokz open-ear earbuds; Costco direct Black Friday row at $109.99 (list $149.99). Carried as PENDING only.
- **Identifiers:** MPN T920-ST-CB-US-326-COS — **PENDING** (single-source, Costco only). UPC — **PENDING, no lead** after three targeted searches. Do NOT attach OpenFit 2 (non-SE) UPC 810160666967 / MPN T920-ST-BK-US — different model.
- **Price / stock:** Costco $109.99 after $40 manufacturer's savings (list $149.99), valid 11/16–11/30, members only, limit 5. **Stock signals conflict** (Costco.com JSON-LD read InStock in one crawl, OutOfStock in another); re-check live at add time.
- **Flag:** Weakest entry in the batch — pending on both identifiers, Costco-exclusive variant code, UPC unfindable. If the batch needs the slot for a verified model, swap this one out.
- **Deal-site evidence:** Slickdeals Black Friday Sift, Costco $109.99 (reg $149.99), 17 saves, posted Oct 26, "Live Nov 15 until Nov 29"; DealNews corroborates ($40 off through Nov 30, members only).

### 2. Shokz OpenRun Air 2 — Black
- **Key:** `shokz-openrun-air-2-black`
- **Category:** headphones
- **Variant pinned:** Black, Standard size, S610-ST-BK-US. (Mini is a separate size, S611-MN-BK-US — not this entry.)
- **Why it qualifies:** New mainstream Shokz bone-conduction model (launched 2026-08-27, $129.95 list); B&H + Best Buy direct Black Friday rows at ~$99.95, both InStock.
- **Identifiers:** MPN S610-ST-BK-US — **VERIFIED** (B&H MFR # + Best Buy Model field, SKU 6680820 + Petra + Home Depot + Newegg). UPC 810202689213 — **VERIFIED with caveat** (PBTech NZ + MobileCiti AU retailer spec pages; both non-US — confirm on Best Buy spec panel SKU 6680820 at add time; downgrade to PENDING if it does not match).
- **Price / stock:** B&H $99.95 Holiday Savings (was $129.95), In Stock; Best Buy $99.99 Black Friday (comp $129.99), sold by Best Buy, InStock.
- **Flag:** UPC caveat (above). Best Buy Black Friday ends Nov 28, 2026.
- **Deal-site evidence:** Slickdeals Sift, Shokz direct $99.95 (reg $129.95); price level independently corroborated by B&H ($99.95) and Best Buy ($99.99).

### 3. Shokz OpenDots Air — Black
- **Key:** `shokz-opendots-air-black`
- **Category:** earbuds
- **Variant pinned:** Black, E210-ST-BK-US. Clip-on open-ear earbuds, 6.3 g per side, IP55, Bluetooth 6.1.
- **Why it qualifies:** Current mid-range Shokz clip-on (launched 2026-06 alongside OpenDots 2); Sam's Club + Best Buy direct rows at $89–$89.99. Both identifiers VERIFIED. Strongest Shokz pick in this track.
- **Identifiers:** MPN E210-ST-BK-US — **VERIFIED** (Best Buy Model field, SKU 6674289 + NFM). UPC 810202687417 — **VERIFIED** (Target spec page, TCIN 95002590 + NFM spec page + PBTech NZ).
- **Price / stock:** Sam's Club $89 (reg $129, $40 off, ends Nov 30) + $15 Sam's Cash (membership rebate, not a price cut); Best Buy $89.99 InStock, sold by Best Buy.
- **Flag:** Sam's Club's $89 offer is color-agnostic in the sources (in-store photo shows the $89 tag on the purple variant); Black is pinned via Target / NFM / Best Buy, not via Sam's Club.
- **Deal-site evidence:** Slickdeals, 2026-11-01, Sam's Club $89 (reg $129), 31% off; Sam's Club's own November instant-savings page corroborates ($40 off, ends Nov 30).

### 4. Shokz OpenRun (standard) — Gray
- **Key:** `shokz-openrun-gray-standard`
- **Category:** headphones
- **Variant pinned:** Gray, Standard size, S803-ST-GY-US. Bone-conduction endurance headphones, 8 h battery, IP67, 26 g.
- **Why it qualifies:** Long-running mainstream Shokz model; Shokz-direct 50%-off code row at $64.95 today (2026-11-21). Both identifiers VERIFIED. Distinct from OpenRun Pro (S810 family) and OpenRun Mini (S803-MN-BK-US).
- **Identifiers:** MPN S803-ST-GY-US — **VERIFIED** (Best Buy Model field, SKU 6506589 + Abt + RunUnited). UPC 850033806229 — **VERIFIED** (Abt UPC # + RunUnited UPC). Do NOT attach Mini UPC 850033806236 or the refurb wholesaler's 810092677024.
- **Price / stock:** Shokz.com $64.95 with code **SDopenrun** at checkout, free shipping (code valid for grey/standard only). Shokz.com list price today is $89.95 (struck $129.95) before the code. Best Buy row is DEAD ("no longer available in new condition"); Abt reads "no longer available" — Shokz direct is the only live row.
- **Flag:** Code-required price — $64.95 is not the shelf price; the row must carry the code or it misleads.
- **Deal-site evidence:** Slickdeals Tech, 2026-11-21, $64.95 w/ code SDopenrun, thumb score +17; same deal posted 2026-10-29 at $64.98 w/ code OPENRUNGREY.

### 5. Sonos Era 100 — Black
- **Key:** `sonos-era-100-black`
- **Category:** speakers
- **Variant pinned:** Black, E10G1US1BLK, single unit. Wi-Fi/Bluetooth smart speaker, AirPlay 2, Alexa + Sonos Voice.
- **Why it qualifies:** Mainstream current Sonos smart speaker; B&H + Micro Center direct rows at $219.00 InStock. Both identifiers VERIFIED.
- **Identifiers:** MPN E10G1US1BLK — **VERIFIED** (Crutchfield MFR # + Micro Center Mfr Part # + B&H). UPC 840136805830 — **VERIFIED** (B&H spec page + Micro Center spec page; eBay GTIN agrees).
- **Price / stock:** B&H $219.00 InStock; Micro Center $219.00 (SKU 555730).
- **Flag — READ FIRST: the Costco $329.99 in the brief is the 2-PACK, not the single unit.** Costco item 1731876, "Sonos Era 100 Speakers 2-Pack Black Edition", $329.99 after $80 off (list $409.99), Nov 19–30. Do NOT attach $329.99 as a single-unit price.
- **Deal-site evidence:** Slickdeals Sift, Costco 2-pack $329.99 (reg $409.99), 37 saves. **The Sift evidence attaches to the 2-pack, not to the single-unit $219 rows** — the single-unit price has no deal-site evidence in this track.

### 6. Sonos Arc Ultra — Black
- **Key:** `sonos-arc-ultra-black`
- **Category:** soundbars
- **Variant pinned:** Black, ARCG2US1BLK, single soundbar. 9.1.4ch Dolby Atmos, Sound Motion, 14 drivers, HDMI eARC.
- **Why it qualifies:** Current Sonos flagship soundbar; Costco + Best Buy + NFM direct Black Friday rows at $849–$849.99, InStock. Both identifiers VERIFIED. **NOT a DROP:** the Costco "bundle" resolves cleanly to a single model (see below).
- **Identifiers:** MPN ARCG2US1BLK — **VERIFIED** (Best Buy Model field, SKU 6597167 + Micro Center + Adorama + NFM + WAVE Electronics). UPC 840136811336 — **VERIFIED** (Micro Center + NFM + Adorama + Walts, all naming Arc Ultra Black).
- **Price / stock:** Costco $849.99 after $250 off (list $1,099.99), valid 11/19–11/30, item 1912780, limit 5; Best Buy $849.00 Black Friday Deal, InStock, sold by Best Buy (BF ends Nov 28); NFM $849.00.
- **Flag:** Costco.com crawl showed OutOfStock on one read while the holiday-savings circular and warehouse photos (2026-11-19) show it live at $849.99 — re-check Costco stock at add time. **Bundle resolution:** Costco's "Sonos Arc Ultra 9.1.4 Ch Soundbar Bundle" (item 1912780) contains exactly ONE Arc Ultra soundbar plus a $60 Apple/SiriusXM gift card, a $79 wall-mount voucher, and a 30%-off accessories coupon — no Sub, no Era speaker. "9.1.4ch" describes the soundbar itself, so $849.99 maps cleanly to the single model.
- **Deal-site evidence:** Slickdeals Sift, Costco $849.99 (reg $1,099.99), 15 saves; Costco's own holiday-savings circular corroborates ($849.99 after $250 off, item 1912780, Nov 19–30).

### 7. Marshall Monitor III ANC — Cream
- **Key:** `marshall-monitor-iii-anc-cream`
- **Category:** headphones
- **Variant pinned:** Cream, MPN 1009077. Black sibling is MPN 1006861 (also $199.99).
- **Why it qualifies:** Marshall's 2025 flagship ANC over-ear (70h BT+ANC / 100h BT, Soundstage spatial audio). Best Buy direct Black Friday row + B&H in-stock row at the same $199.99.
- **Identifiers:** MPN 1009077 — **VERIFIED** (Best Buy model field + B&H product page, BH #MAMONITOR3C / MFR #1009077). EAN 7340055411479 — **VERIFIED** (B&H spec page prints "EAN: 7340055411479" + Aqipa distributor PDF, EU — retailer + distributor per the batch-5 precedent). **Caveat: this is an EAN, not a 12-digit US UPC** — no US UPC was found anywhere; B&H prints EAN only. Counts as verified per the Keychron EAN+SKU precedent. B&H data quirk, recorded: the Cream product page's spec table lists "Color: Black" while the title, variant selector, and MPN all say Cream — do not let the quirk reassign the code to Black.
- **Price / stock:** Best Buy Cream SKU 6670036 **$199.99 Black Friday** (comp $279.99), sold by Best Buy, InStock, Add to Cart; B&H **$199.99 In Stock** (Holiday Savings, free delivery Nov 25).
- **Flag:** Promo price — Best Buy Black Friday ends Nov 28, 2026. EAN-not-UPC caveat (above).
- **Deal-site evidence:** Slickdeals f/20196168 — Amazon $199.99 (Black + Cream), Deal Score +5, 2,191 views. The brief's "Best Buy Sift post" was not re-located — single-source evidence (this one post only).

### 8. Skullcandy Crusher Evo — Matte Black
- **Key:** `skullcandy-crusher-evo-matte-black`
- **Category:** headphones
- **Variant pinned:** Matte Black, MPN S6EVW-S978. Do NOT mix with Staples' other colors: True Black S6EVW-N740, Chill Gray S6EVW-N744.
- **Why it qualifies:** Frontpage Slickdeals post (Nov 17) for a Best Buy direct Black Friday row at $89.99 (57% off $209.99).
- **Identifiers:** MPN S6EVW-S978 — **PENDING** (Best Buy model field only — single source; needs a 2nd). UPC 810145320815 — **PENDING** (eBay + layupshop only, both non-qualifying; no qualifying source).
- **Price / stock:** Best Buy SKU 6580350 **$89.99 Black Friday**, InStock, sold by Best Buy (comp $209.99).
- **Flag:** Both identifiers PENDING — the weakest entry on identifiers, carried on the clean direct BF row + located frontpage post.
- **Deal-site evidence:** Slickdeals frontpage f/20329254, **Nov 17, 2026 8:42 PM**, 3.8K views, $89.99 (was $209.99, 57% off), Best Buy, free S/H.

### 9. Turtle Beach Stealth Pro II — Xbox Black (multiplatform)
- **Key:** `turtle-beach-stealth-pro-ii-xbox-black`
- **Category:** headphones
- **Variant pinned:** Black, Xbox/PS5/PC multiplatform, MPN TBS-2104-05. Do NOT mix: PS/PC-only TBS-5105-05, White TBS-2104-15, dead Best Buy SKU 13215425, marketplace SKU 12653616 ($349.99, sold by Turtle Beach Gaming).
- **Why it qualifies:** Current Turtle Beach flagship gaming headset; Best Buy direct Black Friday row at $249.99 (comp $349.99); both identifiers verified.
- **Identifiers:** MPN TBS-2104-05 — **VERIFIED** (Best Buy model field + shopmyexchange "Model: TBS-2104-05"). UPC 840454400755 — **VERIFIED** (GameStop US retailer spec page + CLD Distribution EU distributor spec printing the same EAN; Gamesmen AU / Kmart AU barcodes agree) — retailer + distributor per the batch-5 precedent.
- **Price / stock:** Best Buy SKU 6672065 **$249.99 Black Friday**, InStock, Add to Cart. GameStop $249.99 Currently Unavailable — not a usable row.
- **Flag:** Deal post unlocated (see below); otherwise clean.
- **Deal-site evidence:** The Slickdeals Sift post cited in the brief was **not re-located** (two searches returned only Best Buy pages). Deal evidence = brief only — single-source, unlocated.

### 10. Technics EAH-AZ100 — Black
- **Key:** `technics-eah-az100-black`
- **Category:** earbuds
- **Variant pinned:** Black, EAH-AZ100-K. Siblings: Silver EAH-AZ100-S, Champagne Gold EAH-AZ100-N, Midnight Blue EAH-AZ100-A, Moonlight Lilac EAH-AZ100-V.
- **Why it qualifies:** Technics' reference-class flagship TWS (Magnetic Fluid Driver, Dolby Atmos + head tracking, 3-device multipoint). **The tentative mid-session DROP is reversed:** us.technics.com sells Black direct at $149.99 InStock — a clean brand-direct row exists.
- **Identifiers:** MPN EAH-AZ100-K — **VERIFIED** (B&H MFR # EAH-AZ100-K + Crutchfield MFR # EAH-AZ100-K). UPC — **PENDING, CONFLICT unresolved:** B&H spec page prints **885170433021** (corroborated only by PBTech NZ + Excellent Photo CA — both non-US); Amazon / eBay GTIN / Snapklik / WirelessEmporium print **885170441613**. Both values pass check-digit validation. Do NOT attach either value to Black until a qualifying spec page settles it.
- **Price / stock:** **us.technics.com Black $149.99 InStock** (brand direct; all five variants $149.99). B&H $149.99 Temporarily Out of Stock, expected availability Nov 30, 2026. Best Buy Black SKU 11078993 $149.99 InStock (2-day crawl) but **seller attribution unverified** — do not use as the primary row.
- **Flag:** UPC conflict (above); B&H price volatile; re-check B&H restock ~Nov 30, 2026.
- **Deal-site evidence:** The DealMoon post (Amazon $142.49) was **not located**. The $142.49 price is corroborated only by a Noted Deals Instagram ad, 2026-11-20 — an aggregator ad, not the DealMoon post, and Amazon is not a price source in any case.

### 11. Sennheiser MOMENTUM True Wireless 4 — Black Graphite
- **Key:** `sennheiser-momentum-true-wireless-4-black-graphite`
- **Category:** earbuds
- **Variant pinned:** Black Graphite, article 700365. Siblings: White Silver 700366, Black Copper 700367, Gold 700441, Denim 700449.
- **Why it qualifies:** Sennheiser's 2024 flagship TWS (aptX Lossless, adaptive ANC, BT 5.4, LE Audio/Auracast, 30h total). **The only fully verified entry in Track B (MPN + UPC).** Best Buy direct row at $249.95.
- **Identifiers:** MPN 700365 — **VERIFIED** (Crutchfield MFR # + Sennheiser US refurbished page SKU 700365 + B&H). UPC 810091272466 — **VERIFIED** (B&H spec page + Abt "UPC # 810091272466", Model # 700365 + Sennheiser official spec-sheet PDF: EAN 4260752332408 / UPC 810091272466, article 700365).
- **Price / stock:** Best Buy **$249.95**, SKU 10904810. B&H lists it Discontinued — source only, not a price row.
- **Flag:** None on identifiers. Deal evidence is for the Denim colorway, not Black Graphite (below).
- **Deal-site evidence:** The brief's "Slickdeals Tech, Amazon $149.98" post was **not located**. Located instead: Slickdeals f/19786128, **Jul 20, 2026**, Best Buy MTW4 **Denim** $149.99 (expired) — a different colorway, store, and date than the brief cited.

### 12. Anker Soundcore Space 2 Pro — Jet Black (standalone)
- **Key:** `anker-soundcore-space-2-pro-jet-black`
- **Category:** headphones
- **Variant pinned:** Jet Black **standalone** (not bundle), MPN D1406Z11. Colors: Jet Black, Midnight Grey, Linen White. Launched 2026-09-22, $199.99 list.
- **Why it qualifies:** Anker's 2026 flagship over-ear; Best Buy standalone direct row + brand-direct Black Friday price + Target Anker-sold row.
- **Identifiers:** MPN D1406Z11 — **PENDING** (Best Buy model field only — single source; soundcore.com product page not yet opened, Newegg spec page is a candidate for the 2nd source). UPC — **PENDING, no lead**. Do NOT attach Target UPCs 194644380014 / 194644379674 — those belong to **Space 2 (non-Pro)** bundles. The brief's implied "A3068" MPN guess was WRONG — soundcore.com slug is `d1406-space-2-pro` and the Best Buy model field is D1406Z11.
- **Price / stock:** Best Buy standalone SKU 6694762 **$199.99**. Target standalone **$169.99** sold & shipped by Anker. soundcore.com Black Friday **$169.99** (was $199.99), sale Nov 19–30. Bundles to avoid: Best Buy Space 2 Pro + Select 4 GO (SKU 13237711 $179.98; SKU 13232533 $209.98); Target bundles $176.98 / $215.99; Amazon bundle $170.62 (not a price source).
- **Flag:** Both identifiers PENDING. Brand-direct BF price $169.99 is time-boxed to Nov 30, 2026.
- **Deal-site evidence:** The Slickdeals Tech post (Amazon $170.62 bundle) was **not located**. The $170.62 bundle price is corroborated only by affiliate review tables, not by the Slickdeals post.

### 13. Beats Solo Buds — Orange
- **Key:** `beats-solo-buds-orange`
- **Category:** earbuds
- **Variant pinned:** Orange, MPN MJKQ4LL/A. Best Buy-exclusive color in the US (also 7-Eleven Japan); launched ~2026-06-30. Do NOT attach Matte Black values: Matte Black is MUVW3LL/A (Apple.com), barcode 195949116391 (Clove, non-qualifying) — a different part.
- **Why it qualifies:** Located Slickdeals post (Jul 10) for a Best Buy direct Black Friday row at $49.99 (37% off $79.99), still live at that price.
- **Identifiers:** MPN MJKQ4LL/A — **PENDING** (Best Buy model field only — single source). UPC — **PENDING, no lead anywhere**.
- **Price / stock:** Best Buy SKU 6677082 **$49.99 Black Friday**, InStock, sold by Best Buy (comp $79.99).
- **Flag:** Both identifiers PENDING. Best Buy Black Friday ends Nov 28, 2026.
- **Deal-site evidence:** Slickdeals f/19743849, **Jul 10, 2026 7:15 AM**, 8.8K views, $49.99 (was $79.99, 37% off), Best Buy, free S/H; expired (price has recurred at Black Friday).

### 14. Beats Studio Buds+ — Ivory
- **Key:** `beats-studio-buds-plus-ivory`
- **Category:** earbuds
- **Variant pinned:** Ivory, MPN MQLJ3LL/A. Released 2023-05-18, retail $169.99; model numbers A2870/A2871/A2872.
- **Why it qualifies:** Best Buy direct Black Friday row at $89.99 (47% off $169.99); MPN verified three ways.
- **Identifiers:** MPN MQLJ3LL/A — **VERIFIED** (Best Buy model field, SKU 6501046 + Apple.com shop product MQLJ3LL/A, $169.99 InStock + Adorama MFR MQLJ3LL/A + Shipt + Staples). UPC — **PENDING, no lead** (searching "195949676" returned nothing).
- **Price / stock:** Best Buy **$89.99 Black Friday**, InStock, sold by Best Buy — pin SKU 6501046. Ignore marketplace SKUs: 13171926 ($139.95, Abe's), 12563311 ($155.07, Adorama), 12945056 ($129.99). Apple.com $169.99 InStock.
- **Flag:** UPC no lead. Best Buy Black Friday ends Nov 28, 2026.
- **Deal-site evidence:** Slickdeals f/19652868 — Amazon $89.95 (Black/Gold, Ivory, Transparent). Older Slickdeals f/18436519 is Jul 8, 2025, expired.

### 15. Google Pixel 10a 128GB — Obsidian
- **Key:** `google-pixel-10a-128gb-obsidian`
- **Category:** phones (new category — no phone in catalog yet)
- **Variant pinned:** Obsidian, 128GB, unlocked (GA09561-US). 8GB RAM, Tensor G4, 6.3" Actua, 48MP main. Launched 2026-02-18. Do not mix with Pixel 10 (different model) or the 256GB variant (GA09605-US).
- **Why it qualifies:** Mainstream Google A-series phone; Best Buy direct Black Friday row confirmed live + Slickdeals BF Sift row. Distinct from every Pixel item in the catalog (Buds/Watch only).
- **Identifiers:** MPN GA09561-US — **PENDING + strong lead** (Best Buy model field only as a qualifying source: live open 2026-11-21 SKU 6668565 + multiple crawls; a Best Buy mirror site prints the same MPN but is non-qualifying; Google Store page did not surface GA09561-US in search). UPC 840353949768 — **PENDING + lead** (Best Buy mirror site spec table only, non-qualifying). Do NOT use EAN 840353949737 — that is the UK variant GA09561-GB, a different region/part.
- **Price / stock:** Best Buy **$549.00 Black Friday** (comp. value $599.00, Save $50), **Sold by Best Buy, InStock, Add to cart**, SKU 6668565. Launch MSRP was $499 (Feb 2026) — the $599 comp. value reflects a later price rise, so $549 is $50 off the *current* $599 comp, not off launch price.
- **Flag:** **Trap avoided — the $499.99 row is marketplace, not Best Buy direct.** Best Buy SKU 13239207 shows $499.99 InStock but is "Sold & shipped by YY Wireless". The direct new row is SKU 6668565 at $549.00. Also exclude open-box $416.99–$449.99 and refurbished $399.99–$439.97 rows. MPN and UPC both need a second qualifying source at add time.
- **Deal-site evidence:** Slickdeals **Black Friday Sift**, Tech & Electronics: "Google - Pixel 10a 128GB (Unlocked) - Obsidian | Best Buy | $549.00, regular $599.00, 8% off, **0 saves**, Nov 19, Live Nov 18 until Dec 05" (crawl 2026-11-20). Note the Sift window runs to Dec 05 while the Best Buy banner says Black Friday ends Nov 28 — re-check expiry at add time.

### 16. Motorola moto g stylus 2025 256GB — PANTONE Gibraltar Sea
- **Key:** `motorola-moto-g-stylus-2025-256gb-gibraltar-sea`
- **Category:** phones (new category)
- **Variant pinned:** PANTONE Gibraltar Sea, 256GB, unlocked (PB6V0014US). 8GB RAM, Snapdragon 6 Gen 3, 6.7" pOLED 120Hz, 50MP + 13MP, built-in stylus. Model XT2517 / XT2517-1. Do not mix with moto g stylus 2024 or the 128GB config.
- **Why it qualifies:** Mainstream Motorola 2025 stylus phone; Best Buy direct Black Friday row + distributor/retailer corroboration; strongest MPN in Track C.
- **Identifiers:** MPN PB6V0014US — **VERIFIED** (Best Buy model field, SKU 6617940 + SHI distributor spec page "Mfr Part #: PB6V0014US" + Newegg listing naming PB6V0014US + Best Buy Q&A linking motorola.com `?pn=PB6V0014US`). UPC 840023282829 — **PENDING + lead** (LakeshoreIT distributor spec "UPC: 0840023282829" + seekknowhow eBay listing; only one distributor-grade source. A conflicting eBay UPC 609921770100 for XT2517-1 exists and is disregarded as non-qualifying/conflicted.)
- **Price / stock:** Best Buy **$199.99 Black Friday** (comp. $399.99, Save $200), **Sold by Best Buy, InStock, Add to cart**, SKU 6617940. Motorola.com also lists $199.99.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Exclude refurbished $279.00 and open-box $157.99–$169.99 rows. UPC needs a second qualifying source at add time (Best Buy spec panel / B&H).
- **Deal-site evidence:** Slickdeals **Black Friday Sift**: "Motorola - moto g stylus 2025 256GB (Unlocked) - PANTONE Gibraltar Sea | Best Buy | $199.99, regular $399.99, 50% off, **0 saves**, Nov 19, Live Nov 18 until Nov 28". Plus standalone Slickdeals threads 2026-11-19 (f/20341674; thread-20340123) and a "Most Popular Tech" listing. Multi-source deal evidence.

### 17. Motorola moto g power 2025 5G 128GB — Leaf Green
- **Key:** `motorola-moto-g-power-2025-128gb-leaf-green`
- **Category:** phones (new category)
- **Variant pinned:** Leaf Green, 128GB, unlocked (PB640007US). 8GB RAM, MediaTek Dimensity 6300, 6.8" 120Hz LCD, 50MP OIS, 5000mAh. Model XT2515 / XT2515-1. Do not mix with moto g power 2024 or the Slate Gray sibling (PB640006US, different color/part).
- **Why it qualifies:** Mainstream Motorola 2025 budget phone; Best Buy direct Black Friday row confirmed live + Slickdeals BF Sift row. No Motorola in the catalog at all.
- **Identifiers:** MPN PB640007US — **PENDING + lead** (Best Buy model field only as a qualifying source: live open 2026-11-21 SKU 6611546 + multiple crawls). **motorola.com does NOT corroborate this part number:** its moto g power 2025 page uses `pn=PB640006US`, which is the **Slate Gray** variant. Do not cite motorola.com as a second source for PB640007US. UPC 840023277283 — **PENDING + conflicted lead, do NOT attach** (Amazon + Snapklik print it for the Leaf Green 128GB, both non-qualifying; Snapklik ties it to Model **PB640003US**, a different channel part number).
- **Price / stock:** Best Buy **$199.99 Black Friday** (comp. $299.99, Save $100), **Sold by Best Buy, InStock, Add to cart**, SKU 6611546. Motorola.com lists $199.99 as well.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Trap avoided — the $99.99 is a carrier-activation price**, not the unlocked price. Also exclude SKU 11519725 ($269.99, Sold Out in one crawl — a different SKU for the same model/color; pin SKU 6611546). MPN and UPC both need a second qualifying source at add time.
- **Deal-site evidence:** Slickdeals **Black Friday Sift**: "Motorola - moto g power 2025 5G 128GB (Unlocked) - Leaf Green | Best Buy | $199.99, regular $299.99, 33% off, **0 saves**, Nov 19, Live Nov 18 until Nov 28". Plus Slickdeals threads 2026-10-28 (f/20221539) and 2026-10-09 (f/20134938). Multi-source deal evidence.

### 18. Motorola edge 2026 128GB — PANTONE Martini Olive
- **Key:** `motorola-edge-2026-128gb-martini-olive`
- **Category:** phones (new category)
- **Variant pinned:** PANTONE Martini Olive, 128GB, unlocked (PBC70002US). 8GB LPDDR5X, MediaTek Dimensity 7450, 6.3" 1.5K AMOLED 120Hz, triple 50MP, 5000mAh. Single color, single storage tier. Do not mix with Edge 2025 / Edge 2024 / Edge 70.
- **Why it qualifies:** Motorola's 2026 US mid-ranger (launched Jun 11, 2026, $599.99); Best Buy direct Black Friday row confirmed live + motorola.com direct row at the same price. MPN fully verified.
- **Identifiers:** MPN PBC70002US — **VERIFIED** (Best Buy model field, SKU 6677356, live open 2026-11-21 + Lenovo.com product page "Part Number : PBC70002US", $599.99 InStock + motorola.com product page `?pn=PBC70002US` + Wireless Dealer Group spec). UPC — **PENDING, no lead found** (targeted searches and B&H search returned no UPC value on any source).
- **Price / stock:** Best Buy **$399.99 Black Friday** (comp. $599.99, Save $200), **Sold by Best Buy, InStock, Add to cart**, SKU 6677356. Corroborated: motorola.com **$399.99** InStock (with a $99.99 Moto Buds 2 gift included — bundle gift, do not price into the row). Lenovo.com still shows $599.99 (non-promo reference).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Trap avoided — SKU 12901739 at $707.17 is a marketplace listing** for the same model/color; pin SKU 6677356 only. Exclude refurbished $499.95. UPC has no lead — the weakest identifier in this track after the g power conflict.
- **Deal-site evidence:** Slickdeals **Black Friday Sift**: "Motorola - edge 2026 128GB (Unlocked) - PANTONE Martini Olive | Best Buy | $399.99, regular $599.99, 33% off, **0 saves**, Nov 19, Live Nov 18 until Nov 28". Corroborated by PhoneArena (2026-11-19, $399.99 "record low" + free Moto Buds 2) and The Gadgeteer.

### 19. Apple iPhone 17 Pro 256GB — Silver (Unlocked)
- **Key:** `apple-iphone-17-pro-256gb-silver`
- **Category:** phones (new category)
- **Variant pinned:** Silver, 256GB, unlocked (MG7K4LL/A). A19 Pro, 6.3" ProMotion, all-48MP rear cameras, eSIM-only, model A3256. Do not mix with Cosmic Orange (different MPN) or Deep Blue, or with iPhone 17 Pro Max, or iPhone 16 Pro.
- **Why it qualifies:** Current-generation Apple flagship; Best Buy direct Black Friday row confirmed live + two further retailer MPN sources; first iPhone in the catalog (no iPhone of any generation is in the 500).
- **Identifiers:** MPN MG7K4LL/A — **VERIFIED** (Best Buy model field, SKU 6418044, live open 2026-11-21 + Abt "Model # MG7K4LL/A" + CDW product page title "iPhone 17 Pro - 256GB - Silver - MG7K4LL/A"). UPC 195950626162 — **PENDING + lead** (BarcodesInc product-data page + shopabunda marketplace listing + multiple Venezuelan retailer price lists tying it to "IPHONE 17 PRO 256GB SILVER MODEL A3256"; no core retailer spec page — needs a B&H / Best Buy spec-panel confirmation at add time).
- **Price / stock:** Best Buy **$999.99 Black Friday** (comp. $1,099.99, Save $100), **Sold by Best Buy, InStock**, SKU 6418044. Abt lists $1,099.99 (InStoreOnly — reference only).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Traps avoided:** (a) the **$30.55/mo installment price + $500 gift card** on the Sift榜单 are carrier-financing terms — never a quote row; (b) the **$899.99 "connect to any carrier later"** price is a carrier-activation price, not the unlocked price; (c) refurbished $879.97–$999.97 rows are excluded; (d) **MG7L4LL/A is NOT Silver** — most plausibly another color variant; do not attach it to the Silver entry.
- **Deal-site evidence:** Slickdeals **Black Friday Sift**: "Apple - iPhone 17 Pro 256GB - Silver (Unlocked) | Best Buy | $999.99, regular $1,099.99, 9% off, **0 saves**, Nov 19, Live Nov 18 until Nov 28" (Sift also lists Cosmic Orange and Deep Blue at the same $999.99). Corroborated by dealnews threads: 2026-11-13 ($1,069.99) and BF week ($1,000, ends Nov 28). Multi-source deal evidence.

### 20. Apple AirTag (2nd Generation) 4-Pack — White
- **Key:** `apple-airtag-2nd-gen-4-pack-white`
- **Category:** accessories (matches the in-catalog single-pack sibling `apple-airtag-2nd-gen-white`)
- **Variant pinned:** White, 4-pack (MFEA4LL/A). AirTag 2nd generation (Jan 2026): 2nd-gen Ultra Wideband chip, louder speaker, Precision Finding on Apple Watch. Do not mix with 1st-gen AirTag 4-pack (MX542LL/A / MX542AM/A, $98.99) or the UK variant MFEA4ZM/A.
- **Why it qualifies:** Current-generation Apple tracker, 4-pack is the volume SKU; both identifiers VERIFIED — the only fully-verified model in Track C. Distinct from the in-catalog single pack (MFE94LL/A, UPC 195950667295) by MPN and UPC; the catalog's own single-pack notes anticipate this 4-pack as "a separate variant, not added".
- **Identifiers:** MPN MFEA4LL/A — **VERIFIED** (B&H product page + Apple.com shop product MFEA4LL/A, 4 pack $99.00 + Best Buy SKU 6377586, Model MFEA4LL/A + Slickdeals threads naming MFEA4LL/A). UPC 195950667455 — **VERIFIED** (B&H spec page "UPC: 195950667455" + Datavision Apple Authorized Reseller listing "MFR: MFEA4LL/A, UPC: 195950667455"; T-Mobile uses 195950667455 as its SKU for the same 4-pack).
- **Price / stock:** Walmart **$69.99** (list $99.00), sold by Walmart — per 2026-11-11/13 Walmart listing screenshots ("Now $69.99", Best seller, "Only 4 left" in one screenshot). **Flag — price is volatile and partly code-gated, re-verify at add time:** Slickdeals' current-prices table still shows Walmart $79.99; the $69.99 has appeared as $79.99 − $10 code SAVE3X (new customers) and as a straight $69.99 listing; select-account codes have taken it to ~$59.99; commenters on 2026-11-02 report the listing bouncing to $104 with the code expired. Clean non-code references: B&H **$95.99 In Stock** (was $99.99) and Apple.com $99.00; Best Buy was $69.99 on 2026-10-30 and $79.99 on 2026-11-07 (SKU 6377586, Sold by Best Buy).
- **Flag:** Do not use the 1st-gen 4-pack row (MX542AM/A, $98.99) or any Amazon price (Amazon had the 4-pack at $89 in July — non-qualifying in any form). If the coordinator wants a code-free row only, use B&H $95.99 instead of Walmart $69.99.
- **Deal-site evidence:** Slickdeals **Tech 今日榜** (per task brief; this session verified the underlying threads but did not independently capture the 今日榜 placement — treat the榜单 placement as brief-sourced). Threads: 2026-09-02 (Walmart $79.99 − SAVE3X = $69.99); 2026-10-30 (Best Buy 4-pack $69.99); 2026-11-11 (select accounts, Walmart $79.99 base / ~$59.99 with code). Multi-thread evidence.

### 21. Hisense M7 75" MiniLED TV — 75M7SR
- **Key:** `hisense-m7sr-75`
- **Category:** tvs (new category — zero TVs in the catalog)
- **Variant pinned:** 75" Class M7 MiniLED Series Hi-QLED 4K UHD Smart Roku TV (2026). **US model is 75M7SR (Roku)** — the brief's "约 75M7" is a shorthand; the full US model code is 75M7SR. Do not use the Canadian 75M7SG (Google TV).
- **Why it qualifies:** Mainstream 2026 Hisense MiniLED; Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart. First Hisense TV in the catalog (no Hisense model in the 500 at all).
- **Identifiers:** MPN 75M7SR — **PENDING + strong lead** (Best Buy model field, SKU 6686979, is the only qualifying source; Hisense's own support team answers on the Best Buy Q&A name "the Hisense 75M7SR" — brand confirmation, but hosted on the same Best Buy page, so it does not count as a second source. No hisense-usa.com product page or spec sheet was found). UPC — **PENDING, no lead** (no qualifying page prints one; the Canadian 75M7SG UPC 888143026817 belongs to a different variant — do NOT attach).
- **Price / stock:** Best Buy **$499.99** Black Friday (comp. value $899.99), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). Open-box from $361.99 — excluded (not new).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Refresh-rate conflict — pin 60Hz native:** the Best Buy spec panel, Hisense's own Q&A answers, the Slickdeals spec list, and the Tech Steve review all say 60Hz native (Motion Rate 240, VRR/ALLM); one Best Buy marketing blurb in an older crawl claims "Native 144Hz" — that is wrong for this model, do not carry it. 144Hz / Dolby Atmos are 85"-only features per Hisense's own creator materials.
- **Deal-site evidence:** Slickdeals front page (brief-supplied: Best Buy $500, orig $900); independently found Slickdeals thread 2026-11-16 (75" M7, Best Buy) and a Threads deal post 2026-11-21 ($499.99, down from $899.99). Single deal-site thread retrieved in-session beyond the brief.

### 22. Samsung U7900H 75" Crystal UHD TV — UN75U7900HFXZA
- **Key:** `samsung-u7900h-75`
- **Category:** tvs (new category)
- **Variant pinned:** 75" Class Crystal UHD U7900H 4K Smart TV (2026), UN75U7900HFXZA. Tizen, Crystal Processor 4K, 60Hz native (DLG 120Hz). Distinct from the 2025 U7900F (UN75U7900FFXZA, Best Buy SKU 6639197).
- **Why it qualifies:** Mainstream Samsung 2026 Crystal UHD; Best Buy direct Black Friday row + Costco in-store row + Abt in-stock row.
- **Identifiers:** MPN UN75U7900HFXZA — **VERIFIED** (samsung.com US product page + Best Buy model field, SKU 6688397). UPC 198957409578 — **PENDING + lead** (P&C Richard Samsung spec-sheet PDF: "MODEL: UN75U7900H / ORDER CODE: UN75U7900HFXZA / UPC CODE: 198957409578" — one qualifying source only; madefordeals.com agrees but is a non-qualifying aggregator. Do not confuse with the U7900F UPCs: UN75U7900FFXZA = 887276951904, UN85U7900FFXZA = 887276951997).
- **Price / stock:** Best Buy **$399.99** Black Friday (comp. value $599.99), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). Costco **$399.99**, item 9675079, Holiday Savings Nov 16–30, 2026 (in-store; also listed online). Abt $397.99 InStock. Samsung.com $399.99 OutOfStock — corroboration only. (An older Slickdeals thread showed $449.99; the price has since dropped to $399.99.)
- **Flag:** Promo price — Best Buy Black Friday ends Nov 28, 2026; Costco Holiday Savings ends Nov 30, 2026. UPC needs one more qualifying source at add time (Best Buy spec panel did not reproduce a UPC in the crawl).
- **Deal-site evidence:** Slickdeals Black Friday Sift (brief-supplied: Costco $399.99, orig $449.99, **130 saves** — the "130 saves" figure is brief-supplied, not independently confirmed); independently found Slickdeals thread f/20280309 (UN75U7900HFXZA, $449.99 pre-drop) and Costco97/Instagram 2026-11-18 confirming Costco $399.99, item 9675079.

### 23. Samsung S84H 65" OLED TV — QN65S84HAEXZA
- **Key:** `samsung-s84h-65`
- **Category:** tvs (new category)
- **Variant pinned:** 65" Class S84H Series OLED 4K UHD SamsungVision AI Smart Tizen TV (2026). **MPN is QN65S84HAEXZA — the brief's "约 UN65S84H" is wrong; Samsung OLEDs use the QN prefix.** "Only at Best Buy" exclusive.
- **Why it qualifies:** Mainstream Samsung 2026 OLED (NQ4 AI Gen2, OLED HDR, Motion Xcelerator 120Hz, 4x HDMI 2.1 with 4K@120Hz/VRR/ALLM, eARC on port 3); Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart.
- **Identifiers:** MPN QN65S84HAEXZA — **VERIFIED with caveat** (Best Buy model field, SKU 6689681 + Samsung Parts USA compatibility list naming QN65S84HAEXZA as a model number — a Samsung-operated page, but a parts listing rather than a product spec page; if a strict product-page second source is required, this drops to PENDING + strong lead). UPC — **PENDING, no lead** (no spec sheet, retailer spec page, or datasheet found printing one; Slickdeals threads name only the MPN).
- **Price / stock:** Best Buy **$899.99** Black Friday (comp. value $2,099.99, save $1,200), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). "Only at Best Buy" badge on the page.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Price history: $999.99 on 2026-10-30/31 (Slickdeals thread f/20235120), now $899.99. UPC has no lead at all — re-check at add time; do not attach any code from Amazon/eBay mirrors.
- **Deal-site evidence:** Slickdeals Tech / front page (brief-supplied: Best Buy $899.99, orig $2,099.99); independently found Slickdeals front-page thread f/20265210 (2026-11-05, $899.99) and f/20235120 (2026-10-30, $999.99).

### 24. TCL Q6CH 5.1ch Soundbar with Wireless Subwoofer — Q6CH
- **Key:** `tcl-q6ch-black`
- **Category:** soundbars
- **Variant pinned:** Black, Q6CH — 5.1ch, wireless subwoofer, up to 580W, Dolby Atmos, DTS:X, RAY-DANZ, HDMI eARC, Bluetooth 5.3. Costco-specific model (item 2012476).
- **Why it qualifies:** Mainstream TCL Q Series soundbar; Costco is the seller of record (retailer-direct). TCL's own US support site lists Q6CH in its Q Series soundbar manuals.
- **Identifiers:** MPN Q6CH — **VERIFIED** (Costco.com model field, item 2012476 + TCL US support Q Series page listing "Q6CH — User Manual"). UPC — **PENDING, no lead** (no qualifying source prints one; Costco.com spec table has no UPC field).
- **Price / stock:** Costco.com **$299.99 OutOfStock** (JSON-LD, page opened fresh 2026-11-21) — the online row is dead at list price. **In-warehouse $199.99** (Holiday Savings, $100 off, through Nov 30, 2026) — confirmed by CostClubWeekly price history (Nov 16–22, $199.99, Northeast + Midwest) and in-store video 2026-11-18 (item 2012476, $199.99, Holiday Savings through Nov 30).
- **Flag — carry-vs-hold:** **No live online price row** — the $199.99 is warehouse-only and the snapshot feed may not capture it; the online listing is OOS at $299.99. Coordinator decides whether to carry on the warehouse price or hold until an online row returns. UPC has no lead. Do not mix with TCL Q65H/Q75H/Q85H (different Q Series models).
- **Deal-site evidence:** Slickdeals Black Friday Sift — confirmed in-session: "TCL Q6CH 5.1ch Soundbar with Wireless Subwoofer | Costco Wholesale | $199.99, Regular price $299.99, 33% Off, **15 saves**, Oct 26, Live Nov 15 until Nov 29".

### 25. Samsung HW-B650F 3.1ch Soundbar — HW-B650F/ZA
- **Key:** `samsung-hw-b650f-black`
- **Category:** soundbars
- **Variant pinned:** Black, HW-B650F/ZA — B-series 3.1ch, 370W, wireless subwoofer, Dolby Audio / DTS Virtual:X, Q-Symphony, Voice Enhance, Night Mode, Game Mode (2025 model).
- **Why it qualifies:** Mainstream Samsung 2025 B-series soundbar; Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart, 874 reviews.
- **Identifiers:** MPN HW-B650F/ZA — **VERIFIED** (Best Buy model field, SKU 6619391 + Samsung support page "B-series Soundbar HW-B650F 3.1 ch Subwoofer (2025)"). UPC — **PENDING, conflicted leads, do not attach any**: Amazon (non-qualifying) prints 887276936956 for HW-B650F/ZA; Ubuy (non-qualifying) prints 887276864211 for "HW-B650F"; the Canadian HW-B650F/ZC has its own UPC 887276950938 (Kawartha TV, Canadian, non-qualifying — and a different suffix variant). No qualifying source prints a US /ZA UPC.
- **Price / stock:** Best Buy **$199.99** Black Friday (comp. value $349.99, save $150), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **B650F vs B650 — confirmed different models, do not mix:** HW-B650 (2023, HW-B650/ZA) is 430W, no Q-Symphony, B&H EAN 8806097097099, Crutchfield page is for the B650; HW-B650F (2025, HW-B650F/ZA) is 370W, adds Q-Symphony and a more compact design — Best Buy's own Q&A states "The B650F is the updated version of the HW-B650 with Q-Symphony and a more compact design." The batch-6 backlog entry "HW-B650 (clearance-flagged)" refers to the older model only; its flag does not transfer. EU suffixes (/ZF EAN 8806097069225, /XU EAN 8806097092049) are not US codes.
- **Deal-site evidence:** Slickdeals Sift (brief-supplied, Best Buy); the Slickdeals thread itself was not retrieved in-session — single-source (brief) for the Slickdeals side. Corroborated by dealnews 2026-11-16 ("Best Buy's Black Friday Deal drops the Samsung B-Series HW-B650F soundbar to $150 off its $350 regular price... $200") and Digital Trends.

### 26. Samsung Music Studio 5 HW-LS50H Wireless Smart Speaker — HW-LS50H/ZA
- **Key:** `samsung-music-studio-5-black`
- **Category:** speakers
- **Variant pinned:** Black, HW-LS50H/ZA — Music Studio 5, 2.0ch, Wi-Fi + Bluetooth, Wireless Dolby Atmos, Q-Symphony, SpaceFit Sound Pro, Alexa + Bixby built-in (2026).
- **Why it qualifies:** Mainstream Samsung 2026 smart speaker; Best Buy direct Black Friday row, sold by Best Buy, InStock. Strongest pick in this track — the only one with both identifiers VERIFIED.
- **Identifiers:** MPN HW-LS50H/ZA — **VERIFIED** (Best Buy model field, SKU 6670424 + Walts TV spec page MPN + Precision distributor Part #). UPC 198957266393 — **VERIFIED** (Walts TV retailer spec page: "Model HW-LS50H | MPN HW-LS50H/ZA | UPC 198957266393" + Precision distributor listing: "Part #: HW-LS50H/ZA, UPC: 0198957266393" — retailer + distributor, per the batch-5 precedent).
- **Price / stock:** Best Buy **$299.99** Black Friday, sold by Best Buy, SKU 6670424, InStock (page data, 2026-11-21; list/reference $499.00). Ignore the Best Buy marketplace SKU 12696700 ($283.68, IPC-STORE) — marketplace, excluded.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Woot $214.99 is NOT a qualifying price row — judgment:** (1) Woot is an Amazon subsidiary ("Woot! An Amazon Company", per dealnews) and Amazon in any form is excluded as a price source; (2) the Woot listing carries only a 90-day Woot Limited Warranty, not the Samsung manufacturer warranty — a non-standard channel; (3) the listing is internally inconsistent — title says HW-LS50H, but "What's in the Box" says "(1) Samsung HW-LS51H Wireless Speaker", and the Woot URL slug is for HW-LS51H. The $214.99 is recorded as deal evidence only, never as the price row. Separately: the retail box is labeled "Music Studio 5 HW-LS50H / HW-LS51H", suggesting LS51H is a channel variant of the same hardware — pin /ZA only. Do not use the Canadian /ZC UPC 198957281686 (Visions/McNain) for the US /ZA model.
- **Deal-site evidence:** Slickdeals Tech (brief-supplied: Woot $214.99); independently found dealnews Woot coverage ($215, "best price by $85", free shipping w/ Prime) and a Slickdeals EPP bundle thread f/20179509 naming HW-LS50H/ZA (different deal — QN80H TV + speaker bundle). Single-source (brief) for the Slickdeals-Tech placement itself.

### 27. Harman Kardon Onyx Studio 8 Portable Bluetooth Speaker — Black
- **Key:** `harman-kardon-onyx-studio-8-black`
- **Category:** speakers
- **Variant pinned:** Black, HKOS8BLKAM — portable stereo Bluetooth speaker, 50W RMS, 120mm woofer + dual tweeters, Bluetooth 5.2, up to 8 hours. (Blue = HKOS8BLUAM, Champagne = HKOS8CPNAM — pin Black only.)
- **Why it qualifies:** Mainstream Harman Kardon portable speaker; **brand-direct row at harmankardon.com, $99.99 InStock**. The brief's eBay $99.99 is unusable (platform seller) — and unnecessary: the same $99.99 is live at the brand's own US store.
- **Identifiers:** MPN HKOS8BLKAM — **VERIFIED** (harmankardon.com "Item#: HKOS8BLKAM" + Best Buy model field, SKU 13145257 + B&H product title/URL). UPC — **PENDING, conflicted leads, do not attach any**: non-qualifying sources disagree — Desertcart prints 028292289859 for Black; eBay/Ubuy print 028292289873, but that code is tied to the **Blue** HKOS8BLUAM (eBay listing: "UPC 028292289873, Model HKOS8BLUAM") — do NOT attach Blue's code to Black; Amazon prints 657768329135 for a Renewed listing; Ubuy prints 094148666167 for a bundle listing. Neither the B&H spec page (opened fresh 2026-11-21 — no UPC row in its spec table) nor harmankardon.com prints a UPC.
- **Price / stock:** harmankardon.com (Official Harman Kardon US store) **$99.99** InStock, list $499.95 (page opened fresh 2026-11-21; JSON-LD InStock). Best Buy's $99.99 row is **sold & shipped by JBL Store** (Best Buy marketplace) — excluded; Best Buy has no Best Buy-direct row for this model. B&H is Discontinued at $499.95 — not a row, corroboration only.
- **Flag:** Deep promo ($99.99 vs $499.95 list, 80% off) with no stated end date — re-check at add time. Model year 2022 (per Amazon) and discontinued at B&H — the brand-direct channel is the only live row; treat as a clearance-style promo, not a new launch. Android Police (2026-11-18) confirms the deal is "purchase directly from Harman Kardon".
- **Deal-site evidence:** Slickdeals front page / Tech (brief-supplied: eBay $99.99 — eBay price excluded as a source); independently found Slickdeals front-page thread f/20314248 (2026-11-15, "Harman Kardon has Onyx Studio 8... on sale for $99.99", updated 2026-11-19 "still available").
### 28. DJI Osmo Action 4 Essential Combo — Black
- **Key:** `dji-osmo-action-4-essential-combo-black`
- **Category:** action-cameras (new category)
- **Variant pinned:** Black, Essential Combo — camera + 1× Extreme Battery + Horizontal-Vertical Protective Frame + Quick-Release Adapter Mount + Locking Screw + Type-C to Type-C PD Cable + Lens Hood + Anti-Slip Pad. (Per DJI US store "In the Box"; the Standard Combo adds a Curved Adhesive Base, the Adventure Combo adds 2 more batteries, battery case, extension rod — pin Essential only.)
- **Why it qualifies:** Mainstream DJI action camera (1/1.3" sensor, 4K/120fps); brand-direct row at DJI US store below list. No camera of this model in the catalog.
- **Identifiers:** MPN — **PENDING, no qualifying lead.** Do NOT attach the Standard Combo MPN CP.OS.00000269.01 or the Adventure Combo MPN CP.OS.00000270.01 (both confirmed on B&H pages for those combos, not Essential). UPC — **PENDING + lead 190021133402** (Sharaf DG UAE retailer listing only — single source, non-qualifying; Amazon prints EAN 6937224107922 for this combo, also non-qualifying). Neither code is verified.
- **Price / stock:** DJI US store **$169.00** (was $229.00), variant 67781549949002, page fetched 2026-11-21. Explicit InStock wording was not captured in the fetch — re-check stock at add time. Best Buy Essential listing (SKU 12596918) is $229.00 Sold Out via Focus Camera (marketplace) — not usable. B&H does not list the Essential Combo as a separate SKU (only Standard/Adventure + B&H kits).
- **Flag:** The brief's Amazon $155.35 (list $239) cannot be used — Amazon in any form is not a price source. The live direct price is $169.00, i.e. higher than the Amazon deal price; the catalog row would carry $169.00, not $155.35. Refurb/used AliExpress rows (~$111–$129) are excluded.
- **Deal-site evidence:** Slickdeals thread 2026-11-08, $189 Amazon (DJI Tech Hub via Amazon), marked still available in-thread; a 2026-11-21 Amazon price report puts it at $155.35 (brief's figure). DealMoon asserted by the brief — not independently re-verified in this session. Saves counts not captured. Single-side-verified (Slickdeals only, in-session).

### 29. GoPro LIT Hero 4K60 — Black
- **Key:** `gopro-lit-hero-4k60-black`
- **Category:** action-cameras (new category)
- **Variant pinned:** Black, standalone LIT Hero (built-in light, 4K60, 12MP, 93 g). Pin the standalone camera, not the Best Buy accessory bundles (CHDXF-131/132/133/134, CHDHF-132-AT_EDI_1).
- **Why it qualifies:** GoPro's 2025 compact HERO (successor to the original HERO CHDHF-131-AT); Best Buy direct in-stock row + B&H in-stock row. Both identifiers VERIFIED — the cleanest camera in this track.
- **Identifiers:** MPN CHDHF-132-AT — **VERIFIED** (Best Buy model field, SKU 6642404 and SKU 12726374 + B&H "MFR # CHDHF-132-AT", BH # GOLITHERO). UPC 810116384129 — **VERIFIED** (B&H spec page "UPC: 810116384129" + GoPro's own LIT HERO sell-sheet PDF, hosted on Aqipa's asset server — Aqipa is a GoPro distributor; the PDF is verbatim GoPro and prints "UPC: 810116384129 SKU: CHDHF-132-AT"). Retailer + manufacturer-PDF/distributor pair, same shape as the batch-5/6 accepted precedents.
- **Price / stock:** Best Buy **$269.99** InStock, sold by Best Buy (SKU 6642404; second SKU 12726374 also $269.99 InStock — same model, two SKUs; use 6642404). B&H $269.99 In Stock (BH # GOLITHERO). No promo at either direct channel.
- **Flag:** Do NOT attach Amazon bundle UPC 197684015847 (belongs to the CHDHF-132-AT_EDI_2 accessory bundle) or the NZ variant CHDHF-132-AS / UPC 810116384143 (different region). The brief's Slickdeals Amazon $169.99 (list $269.99) is Amazon-only and unusable — the direct-channel price is the $269.99 list price, so this entry adds a list-price row, not a deal row.
- **Deal-site evidence:** Slickdeals Tech, Amazon $169.99 (brief-asserted; thread not independently re-verified in-session). Single-source deal evidence; saves count not captured.

### 30. DJI Osmo Action 6 Essential Combo 8K — Black
- **Key:** `dji-osmo-action-6-essential-combo-black`
- **Category:** action-cameras (new category)
- **Variant pinned:** Black, Essential Combo — camera + 1× Extreme Battery Plus (1950 mAh) + Dual-Direction Quick-Release Adapter Mount + Locking Screw + USB-C to USB-C PD Cable (USB 3.1) + Anti-Slip Pad. (Per DJI store "In the Box"; the Standard Combo adds a Curved Adhesive Base, the Adventure Combo adds 2 more batteries, battery case, extension rod — pin Essential only.) 1/1.1" square sensor, 8K video, 50 GB built-in storage.
- **Why it qualifies:** Current DJI flagship action camera (announced 2025-11-18); brand-direct row at DJI US store. No Action 6 of any kind in the catalog.
- **Identifiers:** MPN — **PENDING, no qualifying lead.** An eBay UK listing prints "CPOS0000037701" for the Essential Combo — eBay is non-qualifying and the number does not fit the Standard/Adventure sequence (CP.OS.00000505.02 / CP.OS.00000506.02), so it is recorded here as an unconfirmed lead only and must NOT be attached. UPC — **PENDING + lead 190021161696** (Amazon + TradeKorea + Ubuy agree — all three non-qualifying; no retailer spec page prints it). Do NOT attach UPC 190021997370 (Essential + Street Photography Handle Kit bundle) or 190021998407 (Essential + 58-piece kit bundle).
- **Price / stock:** DJI US store **$426.00**, Essential variant 67656937701450 (variant table fetched live 2026-11-21; Standard $436.00, Adventure $454.00 on the same page). Explicit InStock wording not captured in the fetch — re-check stock at add time; djiindex's 2026-11-20 DJI-store check also lists the Essential at $426. B&H does not list the Essential Combo separately (Standard $436.00 In Stock / Adventure $454.00 In Stock only).
- **Flag:** The brief's Amazon $376 (list $446) cannot be used. The direct price is $426.00 — only $10 under the Standard Combo, so the Essential's value vs Standard is thin (the missing piece is one curved adhesive base); keep the entry as briefed, but do not present $376 anywhere. Note the brief's "2026 新款" is slightly off: launched 2025-11-18, still the current model.
- **Deal-site evidence:** DealMoon, Amazon $376 (brief-asserted; thread not independently re-verified in-session). Single-source deal evidence; saves count not captured.

### 31. DJI Osmo Pocket 3 Creator Combo — Black
- **Key:** `dji-osmo-pocket-3-creator-combo-black`
- **Category:** cameras (existing category — Switch 2 Camera is the only other model; Track E's "new category" note is corrected)
- **Variant pinned:** Black, Creator Combo — Pocket 3 + DJI Mic 2 Transmitter + Wide-Angle Lens + Battery Handle + Osmo Mini Tripod + Carrying Bag. (Per B&H "Kit Contains" and Micro Center "What's in the Box"; the plain Pocket 3 and the B&H accessory-bundle variants DJOP3CCAK / DJOP3CC are different listings — pin the DJI Creator Combo only.)
- **Why it qualifies:** Mainstream DJI 3-axis gimbal camera (1" CMOS, 4K120); B&H Top Seller in-stock row. Both identifiers VERIFIED.
- **Identifiers:** MPN CP.OS.00000302.01 — **VERIFIED** (B&H page slug/title `dji_cp_os_00000302_01_osmo_pocket_3_creator` + Micro Center "Mfr Part #: CP.OS.00000302." + Adorama "MFR: CP.OS.00000302.01 A"). UPC 190021095007 — **VERIFIED** (Micro Center spec panel "UPC: 190021095007" + Target UPC field 190021095007 + Adorama bundle UPC-codes list includes 190021095007 for the Creator Combo kit).
- **Price / stock:** B&H **$466.00** In Stock (was $549.00, Holiday Savings $83.00), Add to Cart, free delivery Wed Nov 25, page opened live 2026-11-21. Micro Center lists $549.99 (OutOfStock in one crawl) — B&H is the row.
- **Flag:** Do NOT attach any B&H component UPC from this page to the kit: 190021094970 is the Pocket 3 camera alone, 190021094949 the wide-angle lens, 190021094932 the battery handle, 190021094918 the mini tripod, 190021094796 the carrying bag. Kit UPC is 190021095007 only.
- **Deal-site evidence:** DealMoon, Amazon $466 (list $629) (brief-asserted; thread not independently re-verified in-session). Note the B&H direct price is also $466.00 — the deal price coincides with the direct row. Single-source deal evidence; saves count not captured.

### 32. Insta360 Ace Pro 2 Xplorer Action Camera Bundle — Black (Costco)
- **Key:** `insta360-ace-pro-2-xplorer-bundle-costco-black`
- **Category:** action-cameras (new category)
- **Variant pinned (bundle contents nailed down — Costco.com):** Ace Pro 2 camera + **2 total batteries + Xplorer Grip Kit + Quick Release Standard Mount + USB-C Cable + Mic Cap + Wrist Strap + 128GB microSD card**. Costco Item 9536006, Model "Ace Pro 2 Xplorer Bundle", Black, Online Only, Limit 5 Per Member. This is the Costco-exclusive bundle — NOT the Target/Best Buy "Xplorer Pro Bundle" (Pro grip, no card) and NOT the Best Buy "Octa Edition" (see Flag).
- **Why it qualifies:** Mainstream Insta360 flagship action camera (8K, Leica optics, 1/1.3" sensor); Costco retailer-direct row with contents fully pinned. Bundle composition is unambiguous, so the brief's DROP condition (unclear contents) does not trigger.
- **Identifiers:** MPN — **PENDING, no lead.** Costco lists only the model name "Ace Pro 2 Xplorer Bundle" and Item 9536006 (a Costco item number, not a manufacturer MPN); Newegg repeats "MPN: 9536006", which is the same Costco number, not an Insta360 MPN. The base camera MPN CINSBBGA belongs to the camera alone, not this bundle — do not attach it. UPC — **PENDING + weak lead 6977644766460** (13-digit EAN; Newegg listing for the "Xplorer Dual Battery … with 128GB Card" bundle only, and that Newegg page is a third-party-seller bundle — single weak source; no second source found).
- **Price / stock:** Costco **$389.99**, "Available", "While supplies last" (Costco.com crawl 9 days old; a second crawl showed OutOfStock, so re-check stock at add time). Costco membership required to buy — flag for the coordinator (Costco is retailer-direct, but gated).
- **Flag — brief's numbers are stale, do not carry them:** the brief says Costco $309.99 (list $339.99). The $309.99 was a Slickdeals thread from 2026-06-23 (valid through 7/5/26, expired); other Slickdeals threads show $329.99 (2026-03-16, valid 3/16–3/31/26; and 2026-05-16, valid through 5/26/26) and $379.99 (2025-10-06, valid until 10/16/25). Current Costco price is $389.99; no current $309.99/$339.99 figures exist. Do NOT mix with: Best Buy "Ace Pro2 Xplorer Bundle Octa Edition" (Model ACEPRO2140, SKU 6665553, $359.99 Black Friday, comp $449.99) — a different bundle/edition; Target "Xplorer Pro Bundle" UPC 842126120657 — a different bundle; Best Buy SKU 13265746 "Dual Battery Xplorer Bundle, Slate Gray" $479.99 — sold/shipped by Adorama (marketplace), not a direct row.
- **Deal-site evidence:** Slickdeals Tech — threads 2026-06-23 ($309.99, expired 7/5/26), 2026-05-16 ($329.99), 2026-03-16 ($329.99), 2025-10-06 ($379.99). All expired; current deal evidence is stale. Saves counts not captured.

### 33. Lenovo Yoga 7i 2-in-1 16" Gen 10 — Luna Grey (83JT0000US)
- **Key:** `lenovo-yoga-7i-2-in-1-16-gen-10-luna-grey`
- **Category:** laptops
- **Variant pinned:** Luna Grey, **83JT0000US** — Yoga 7i 2-in-1 Gen 10 (16" Intel), Intel Core Ultra 5 226V (Series 2), 16GB, 512GB SSD, 16" WUXGA 1920×1200 IPS touch, Win 11 Home, Copilot+ PC. (Per lenovo.com product page 83jt0000us + Best Buy model field + Newegg "Yoga 7 16ILL10, Part Number 83JT0000US, Ultra 5 226V".)
- **Why it qualifies:** Mainstream Lenovo convertible; Best Buy direct Black Friday Doorbuster row + lenovo.com in-stock row. MPN two-sourced (three, counting Newegg).
- **Identifiers:** MPN 83JT0000US — **VERIFIED** (lenovo.com product page, $899.99 InStock + Best Buy model field, SKU 6615769 + Newegg model number). UPC 198155420948 — **PENDING + lead** (Slickdeals thread + eBay listings agree — both non-qualifying; the Best Buy spec panel did not reproduce the UPC in the live page open, so no qualifying second source yet).
- **Price / stock:** Best Buy **$649.99** Doorbuster, sold by Best Buy, InStock (JSON-LD), comp value $999.99, SKU 6615769, page opened live 2026-11-21. Black Friday ends **Nov 28, 2026**. lenovo.com $899.99 InStock as the non-promo reference.
- **Flag — twin-config trap, the most important flag in this track:** Best Buy lists a SECOND Yoga 7i at the same $649.99 — **83TE0004US** (2026 model, Intel Core Ultra 5 322 Series 3, 16GB/512GB, Luna Grey, SKU 6672158, list $1,649.99, Holiday Deal $649.99; Slickdeals thread 2026-11-19). The two configs are different generations with different CPUs and different list prices. The brief's "原价 $899.99" matches 83JT0000US (lenovo.com $899.99), NOT 83TE0004US ($1,649.99) — so 83JT0000US is the pinned config. Do not mix the two, and do not attach the 83TE0004US price history to 83JT0000US. Also ignore marketplace/refurb SKUs for this model (e.g. SKU 13168212 JW Tech LLC, SKU 13199730/13263455 refurbished, $579.99–$949.99).
- **Deal-site evidence:** DealMoon (brief-asserted; not independently re-verified). Independently confirmed: DealNews 2026-11-19, "Lenovo Yoga 7i Core Ultra 5 16\" 2-in-1 Touchscreen Laptop: $650 — 83JT0000US", Best Buy Black Friday Doorbuster, "best price we've seen", expires 11/28/2026; Slickdeals threads 2026-11-10 and 2026-11-19 for 83JT0000US at $649.99 (UPC 198155420948 printed in-thread). Dual-source deal evidence for the pinned config. Saves counts not captured.

### 34. Lenovo Legion 5a 15.3" — Eclipse Black (83Q70068US)
- **Key:** `lenovo-legion-5a-15-3-eclipse-black`
- **Category:** laptops
- **Variant pinned:** Eclipse Black, **83Q70068US** — Legion 5a Gen 11, AMD Ryzen 7 250 (8-core, 3.3–5.1 GHz), NVIDIA GeForce RTX 5060 8GB GDDR7 (115W TGP), 16GB DDR5 (1×16GB, 2 slots, up to 32GB), 512GB M.2 NVMe SSD, 15.3" WQXGA 2560×1600 OLED 165Hz, Win 11 Home, Wi-Fi 7. (Per B&H product page + Slickdeals spec list + Target listing.)
- **Why it qualifies:** Mainstream 2026 Legion gaming laptop; B&H direct in-stock row with the largest holiday cut in this track. Both identifiers VERIFIED — the strongest laptop in this track.
- **Identifiers:** MPN 83Q70068US — **VERIFIED** (B&H "MFR # 83Q70068US", BH # LE83Q70068US + Target "Model name: 83Q70068US" + Slickdeals thread naming 83Q70068US). UPC 199276132093 — **VERIFIED** (B&H spec page "UPC: 199276132093" + Target UPC field 199276132093 + MyNavyExchange "UPC 199276132093 / Model 83Q70068US" — three agreeing sources).
- **Price / stock:** B&H **$1,249.99** In Stock (was $1,799.99, Holiday Savings $550.00), Add to Cart, free delivery Tue Nov 24, page crawls 1 day old; B&H flags "Limited supply at this price". Target lists the same config at $1,399.99 (reg $1,799.99) as the non-promo reference.
- **Flag:** Do not mix with sibling config **83Q70003US** (same Ryzen 7 250 / RTX 5060 / 16GB but **1TB** SSD, also $1,249 at Walmart in a July 2026 Slickdeals thread) — different MPN, different storage. The B&H row is a Holiday Savings price with no stated end date — re-check at add time.
- **Deal-site evidence:** Slickdeals thread 2026-11-17, "Lenovo Legion 5a Gaming Laptop: Ryzen 7 250, 15.3\" OLED, 16GB DDR5, RTX 5060 — $1249.99", B&H, free S&H. Single-source (Slickdeals) deal evidence; saves count not captured.

### 35. ASUS Zenbook A14 UX3407QA-PS76 — Iceland Gray [queue top-up]
- **Key:** `asus-zenbook-a14-ux3407qa-ps76-iceland-gray`
- **Category:** laptops
- **Variant pinned:** Iceland Gray, **UX3407QA-PS76** — Qualcomm Snapdragon X (X1-26-100), 32GB LPDDR5X, 1TB PCIe 4.0 SSD, 14" WUXGA 1920×1200 OLED 60Hz 600-nit, Win 11 Home, 70Wh, 2.18 lb. (Per ASUS press release spec table + ASUS Store + Best Buy.) This is the batch-6 alternate, re-checked live 2026-11-21.
- **Why it qualifies:** ASUS's lightest Copilot+ PC (launch Jan 2025, still current); Best Buy direct row confirmed live at the brief's price. MPN VERIFIED.
- **Identifiers:** MPN UX3407QA-PS76 — **VERIFIED** (ASUS US press release, spec table "Model UX3407QA-PS76" + ASUS Store product page, Part Number 90NB1502-M00FM0 + Best Buy model field, SKU 6616965). UPC 197105832077 — **PENDING + lead** (laptoparena.net "EAN/UPC code 0197105832077, 197105832077" only — spec aggregator, single source, non-qualifying; no retailer spec page prints it).
- **Price / stock:** Best Buy **$1,199.99** (comp $1,599.99), sold by Best Buy, Add to Cart, InStock (JSON-LD), SKU 6616965, page opened live 2026-11-21. ASUS Store lists the same config at $1,599.99. The batch-6 alternate's "$1,199.99 direct" claim is confirmed live.
- **Flag:** Ignore the Best Buy "Upgraded" bundles carrying this model number (SKU 12927567 $2,099.00 with 4TB SSD + dock; SKU 12939083 $1,579 with 1TB dock set) — third-party-modified, not the direct row. Do not mix with the Zabriskie Beige sibling UX3407QA-X1P512 (16GB/512GB, Snapdragon X Plus) or with ASUS part suffix 90NB1502-M00Z60 seen on overseas resellers (different region/config).
- **Deal-site evidence:** None — **队列顶位** (batch-6 backlog alternate, not a deal-site gap). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 36. HP OmniBook 3 14 hz0788dx — Nouvelle Silver [queue top-up]
- **Key:** `hp-omnibook-3-14-hz0788dx-nouvelle-silver`
- **Category:** laptops
- **Variant pinned:** Nouvelle Silver, **14-hz0788dx / DM2Z9UA#ABA** — Snapdragon X X1-26-100 (8-core), Qualcomm Hexagon NPU 45 TOPS, 16GB, 512GB PCIe Gen4 NVMe SSD, 14" 2K (1920×1200) OLED UWVA, Win 11 Home, Copilot+ PC, 41h45m video playback, 3.13 lb. (Per Best Buy model field + HP datasheet PDF.) This is the batch-6 alternate, re-checked live 2026-11-21.
- **Why it qualifies:** Mainstream HP Copilot+ laptop; Best Buy direct Black Friday row confirmed live at the brief's price.
- **Identifiers:** MPN 14-hz0788dx / DM2Z9UA#ABA — **VERIFIED with caveat** (Best Buy model field "14-hz0788dx/DM2Z9UA#ABA", SKU 6679357 + HP's own datasheet PDF "HP OmniBook 3 14 inch Laptop Next Gen AI PC 14-hz0788dx", hosted on Best Buy's static file server files.bbystatic.com — the content is verbatim HP, but the host is not hp.com; same caveat shape as the batch-6 Brio 100 acceptance. A direct hp.com product-page re-check at add time would remove the caveat.) UPC — **PENDING, no lead.** No qualifying (or non-qualifying) UPC surfaced in any search.
- **Price / stock:** Best Buy **$599.99** Black Friday (comp $799.99, save $200), sold by Best Buy, Add to Cart, InStock (JSON-LD), SKU 6679357, page opened live 2026-11-21. Black Friday ends **Nov 28, 2026**. A second Best Buy SKU for the same model (13225916) shows $689.90 — use SKU 6679357 at $599.99.
- **Flag:** Do not mix with the Starlit Blue 8GB/256GB OmniBook 3 sibling ($399.99) or the 256GB Nouvelle Silver variant — different configs. The OLED-vs-UWVA wording conflict on the Best Buy page is resolved by HP's datasheet (2K OLED panel; UWVA is the viewing-angle technology).
- **Deal-site evidence:** None — **队列顶位** (batch-6 backlog alternate, not a deal-site gap). No Slickdeals/DealMoon thread cited or found for this model in-session. (A 2026-11-12 social post notes the same $599 Best Buy price.)

### 37. MSI MAG 321UP 32" QD-OLED 4K 165Hz — Black
- **Key:** `msi-mag-321up-qd-oled-black`
- **Category:** monitors
- **Variant pinned:** Black, 31.5" QD-OLED, 3840x2160, 165Hz, 0.03ms, MAG321UPQDOLED (2024 model; first MSI model in the catalog — 0 MSI rows today)
- **Why it qualifies:** Mainstream MSI 4K QD-OLED gaming monitor; B&H direct in-stock Holiday Savings row + Micro Center spec row. Both identifiers VERIFIED — the strongest deal-site item in this track.
- **Identifiers:** MPN MAG321UPQDOLED — **VERIFIED** (B&H page slug/title `msi_mag321upqdoled` + Micro Center spec "Mfr Part# MAG 321UP QD-OLED" + AVADirect "MPN: MAG 321UP QD-OLED", all for the same 165Hz model). UPC 824142363720 — **VERIFIED** (B&H spec page "UPC: 824142363720" + Micro Center spec "UPC, 824142363720", agree).
- **Price / stock:** B&H $569.99 In Stock (was $699.99, Holiday Savings $130.00), free delivery Wed, Nov 25 (crawl 2 days ago; Pangoly price history confirms $569.99 first hit 2026-11-19, lowest ever). MSI US Store lists the model (price not captured — B&H is the row).
- **Flag:** Do NOT mix with the **MAG 321UP QD-OLED X24** (240Hz, MPN MAG321UPQDOLEDX24, UPC 824142449561, B&H $799.99) — a different, newer model with its own UPC. Pin the 165Hz original only.
- **Deal-site evidence:** Brief-reported "Slickdeals Tech 今日榜, B&H $569.99" — **not independently re-found in-session.** The only Slickdeals thread surfaced is the expired 2026-10-06 Newegg $571.14 one (`slickdeals.net/f/20110209`). No current Slickdeals thread for the B&H price, no saves count captured. Treat the deal-site leg as brief-reported / single-source; the B&H price itself is independently confirmed.

### 38. Logitech G Yeti GX — Black
- **Key:** `logitech-g-yeti-gx-black`
- **Category:** microphones (existing category — 5 models already)
- **Variant pinned:** Black, dynamic USB-C, supercardioid, LIGHTSYNC RGB
- **Why it qualifies:** Mainstream Logitech G streaming microphone (2023, still current); Best Buy direct Black Friday row + B&H in-stock row. Both identifiers VERIFIED — the second fully-verified pair in this track.
- **Identifiers:** MPN 988-000567 — **VERIFIED** (B&H "MFR #988-000567" + Best Buy model field 988-000567, SKU 6556755 + Dell "Manufacturer Part Number, 988-000567" + Lenovo US "Manufacturer PN, 988-000567" + Staples title). **Correction to the brief:** the brief's guessed "988-000570" does not exist for this mic — 988-000567 is Black; 988-000574 is White (B&H white page, UPC 097855190987). Do not use 988-000570. UPC 097855190994 — **VERIFIED** (B&H spec page "UPC: 097855190994" + CompSource distributor spec "UPC EAN CODE: 097855190994" for 988-000567 + Logitech's own package-spec datasheet PDF: "Part # 988-000567 … Bar code 097855190994 (EAN-13)" — brand-authored content, same shape as the batch-6 Brio 100 precedent).
- **Price / stock:** Best Buy $89.99 Black Friday Deal (comp $169.99), Sold by Best Buy, Add to cart, InStock — **page opened fresh 2026-11-21 12:55 PST** (crawl 2026-11-21 20:55 UTC). B&H $169.99 In Stock (list reference). Staples $89.99 InStock (corroborating direct row at the same price).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon $89.99 (brief) was never used as a source. Do not mix with White (988-000574 / 097855190987) or Yeti Orb (different mic).
- **Deal-site evidence:** Brief-reported "Slickdeals Tech, Amazon $89.99" — Amazon price disregarded per the rule (never used as a source). The $89.99 price is independently confirmed at **Best Buy direct** and at Staples $89.99 InStock. No current Slickdeals thread re-found in-session (only an expired 2024 thread); deal-site leg is brief-reported.

### 39. Amazon Echo Show 8 (2025) — Glacier White [CARRY with category flag]
- **Key:** `amazon-echo-show-8-2025-glacier-white`
- **Category:** smart-home (existing category — same as Nest Hub; no new category invented)
- **Variant pinned:** Glacier White, 2025 release / 4th Gen, 8.7" HD touchscreen, spatial audio, Alexa+, model B0DC93K4NW (AZ3 Pro chip, 13MP camera). Distinct from the batch-3 3rd-gen Echo Show 8 (8" HD) that was swapped out — different generation, different size, different ASIN.
- **Why it qualifies:** Current-generation Amazon smart display; Best Buy direct Black Friday row + Abt in-stock row. MPN VERIFIED.
- **Identifiers:** MPN B0DC93K4NW — **VERIFIED** (Best Buy model field, SKU 6642846 + Staples "Model #: B0DC93K4NW" + Abt "Model: B0DC93K4NW" + Dell "Manufacturer Part Number, B0DC93K4NW"). UPC 840414682108 — **PENDING + lead (non-qualifying only).** camelcamelcamel lists it for B0DC93K4NW (ASIN-derived, non-qualifying); an eBay description page and a wholesale Instagram post agree — both non-qualifying. No qualifying retailer spec page prints it. Do NOT use the Graphite UPC 840414684003 (BJ's, for B0DC8ZMR1P) for this white pin.
- **Price / stock:** Best Buy **$129.99** Black Friday Deal (comp $199.99), SKU 6642846, InStock, Add to cart (multiple 2-day crawls). Abt $129.99 InStock (manufacturer rebate ends 11/30/2026, comp $199.99). Staples $199.99, Out of stock for delivery. **Correction:** the brief's $99.99 was not confirmed anywhere — $129.99 is the live Best Buy price.
- **Flag — category flag:** display-form-factor addition to `smart-home`; drop at batch approval if the user wants smart displays out (see "Category judgment" in the Method section). Promo price — Black Friday ends Nov 28, 2026. Amazon's own price never used. A second Best Buy SKU 12376837 shows $156.55 — pin SKU 6642846 ($129.99) only.
- **Deal-site evidence:** Brief-reported "Slickdeals Tech / DealMoon, Best Buy $99.99" — **the $99.99 is NOT confirmed and looks wrong.** Live Best Buy price is **$129.99 Black Friday Deal**, confirmed across multiple 2-day crawls; Abt $129.99 InStock agrees. Correction recorded; do not carry $99.99.

### 40. Amazon Echo Hub 8" — White [CARRY with category flag]
- **Key:** `amazon-echo-hub-white`
- **Category:** smart-home (existing category — same as Nest Hub)
- **Variant pinned:** White, 8" smart home control panel, Alexa+, model B0BCR7M9KX (hardware model G6A87E; Zigbee/Matter/Thread)
- **Why it qualifies:** Current Amazon smart-home control panel; Best Buy direct Black Friday row + B&H in-stock row. MPN VERIFIED.
- **Identifiers:** MPN B0BCR7M9KX — **VERIFIED** (Best Buy model field, SKU 6562248 + B&H page slug/title `amazon_b0bcr7m9kx_echo_hub`). UPC 840268960544 — **PENDING + lead (B&H only).** B&H spec page prints it; the only other prints are non-qualifying (everzento mirror, tanotis, eBay, camelcamelcamel). No second qualifying source found.
- **Price / stock:** Best Buy **$74.99** Black Friday Deal (comp $179.99), SKU 6562248, Sold by Best Buy, InStock (multiple crawls 2–7 days old; a Threads screenshot of the Best Buy page the same day also shows $74.99). B&H $109.99 In Stock (was $179.99, Holiday Savings $70.00).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon's own price never used. Category flag: same as item 39 — drop with item 39 if the user wants smart-home control panels out. Note a BrickSeek post flagged Walmart clearance $45 (Aug 2026) — clearance chatter, not a usable row; the Best Buy new row is clean.
- **Deal-site evidence:** Brief-reported "Slickdeals Tech, Best Buy $74.99" — **confirmed.** Best Buy $74.99 Black Friday Deal (comp $179.99), Sold by Best Buy, multiple crawls; B&H $109.99 InStock.

### 41. Sony ULT Tower 10 — Black [queue top-up]
- **Key:** `sony-ult-tower-10-black`
- **Category:** speakers
- **Variant pinned:** Black, SRSULT1000 (360° party speaker, wireless mic included)
- **Why it qualifies:** Mainstream Sony party speaker; Best Buy direct row re-confirmed live. MPN VERIFIED; UPC still single-source (unchanged from track D).
- **Identifiers:** MPN SRSULT1000 — **VERIFIED** (B&H spec page "MFR # SRSULT1000" + Crutchfield "MFR # SRSULT1000" + Best Buy model field, SKU 6577679). UPC 027242928978 — **PENDING + lead (Adorama only).** Adorama spec page lists "UPC Code 027242928978" for SRSULT1000 — the same single source as track D; no second qualifying source surfaced in this session (Amazon/eBay/camelcamelcamel agree, all non-qualifying). B&H spec page still prints no UPC; Best Buy crawled page contains no UPC.
- **Price / stock:** Best Buy $799.99 (comp $1,199.99, Save $400), Sold by Best Buy, SKU 6577679, InStock (multiple crawls 1–3 days old; open-box $567.99–$610.99 — pin new only). B&H "No Longer Available"/Discontinued (track D) — Best Buy is the row.
- **Flag:** UPC needs one more qualifying source. Costco $789.99/$799.99 (item 1916855) is Instagram price-tag only — not a row.
- **Deal-site evidence:** None — **队列顶位** (strongest non-carried alternate, track D). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 42. ASUS ROG Strix G16 G614PR — Eclipse Gray [queue top-up]
- **Key:** `asus-rog-strix-g16-g614pr-rtx-5070-ti-eclipse-gray`
- **Category:** laptops
- **Variant pinned:** Eclipse Gray, G614PR-G16.R95070TI — Ryzen 9 8940HX, RTX 5070 Ti 12GB, 16GB DDR5-5600, 1TB SSD, 16" WUXGA 1920x1200 165Hz, Win 11 Home
- **Why it qualifies:** Current ROG gaming laptop; Best Buy direct Black Friday row. **MPN now VERIFIED — the missing leg from track G is closed this session** (ROG official spec page names the exact config).
- **Identifiers:** MPN G614PR-G16.R95070TI — **VERIFIED** (Best Buy model field, SKU 6613956 + ROG official spec page `rog.asus.com/us/laptops/rog-strix/rog-strix-g16-2025-g614/spec/`, opened 2026-11-21, which lists "G614PR-G16.R95070TI" twice in its config list). UPC — **PENDING, no lead for this config.** No qualifying source prints a UPC for G614PR-G16.R95070TI. laptoparena lists 197105821606, but that is for a DIFFERENT regional config (G614PR-RV003W, 90NR0NJ7-M000M0) — do NOT attach it to the US Best Buy config. B&H does not carry this config.
- **Price / stock:** Best Buy $1,749.99 Black Friday Deal, SKU 6613956, Sold by Best Buy, InStock (multiple 2-day crawls; JSON-LD confirms InStock). A second Best Buy SKU 10936980 shows $2,209.99 — pin SKU 6613956 only. Open-box Excellent $1,267.99 (Slickdeals, expired) — not a new row.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Best Buy price was volatile in track G ($1,749.99–$2,209.99 across SKUs/crawls) — re-check at add time. ASUS Store US lists the G614 family from $2,099.99 (different configs).
- **Deal-site evidence:** None — **队列顶位** (strongest ASUS backlog item, track G). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 43. Samsung Galaxy Watch7 40mm BT — Green [queue top-up]
- **Key:** `samsung-galaxy-watch7-40mm-green`
- **Category:** wearables
- **Variant pinned:** Green, 40mm BT, SM-L300NZGAXAA (2024; sibling color of track-F F4 Cream)
- **Why it qualifies:** Prior-generation Samsung watch, still sold new by Best Buy; Best Buy direct row. MPN VERIFIED on the same two legs as the Cream sibling.
- **Identifiers:** MPN SM-L300NZGAXAA — **VERIFIED** (Best Buy model field, SKU 6585116 + Samsung official Wearables MSRP Price Lists, Mar/Jun/Jul/Sep 2026 editions, all agree — the same pair that verified the Cream sibling F4 in track F). UPC 887276868905 — **PENDING + lead (Samsung MSRP list only).** The Samsung MSRP price list (Mar 2026 PDF) ties SM-L300NZGAXAA = Galaxy Watch7 BT 40mm Green, UPC 887276868905, MSRP $249.99 — but that is one publisher; no B&H/Abt retailer spec page printing the same UPC was found in-session. Do not mark VERIFIED until that second source is found.
- **Price / stock:** Best Buy $249.99, SKU 6585116, Sold by Best Buy, InStock (multiple 2–3 day crawls; JSON-LD confirms InStock). **Note the color split:** the Cream sibling is $149.99 Black Friday; Green shows $249.99 with no Black Friday deal in crawls (one crawl showed $229.99 on a different SKU 10923234 — seller unclear, do not use). Refurbished Excellent $134.97 (Networkstore marketplace) and open-box $64.99 exist — pin the new SKU 6585116 only.
- **Flag:** Prior generation (2024), superseded by Watch8/Watch9, but still sold new by Best Buy — not clearance (no clearance tag on the new row). Membership: catalog has no Watch7 at all; distinct from Watch8 40mm Graphite (SM-L320NDAAXAA) and Watch9 40mm (SM-L340NZKAXAA).
- **Deal-site evidence:** None — **队列顶位** (queue B1, track F). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 44. Lenovo ThinkPad E16 Gen 3 — Black (21ST0008US) [queue top-up]
- **Key:** `lenovo-thinkpad-e16-gen-3-black`
- **Category:** laptops
- **Variant pinned:** Black, 21ST0008US — AMD Ryzen 7 250, 16GB DDR5, 512GB SSD, 16" WUXGA 1920x1200 touchscreen IPS, Win 11 Pro
- **Why it qualifies:** **The UPC gap from track E is closed this session — now a fully VERIFIED MPN+UPC pair**, plus a fresh B&H direct in-stock row. Strongest queue promotion in this track.
- **Identifiers:** MPN 21ST0008US — **VERIFIED** (CDW spec page "MFG#: 21ST0008US | CDW#: 9084576" + NeweggBusiness spec page "Part Number | 21ST0008US", same config; B&H page slug `lenovo_21st0008us` agrees). UPC 198157339941 — **VERIFIED (new)** (B&H spec page, opened fresh 2026-11-21: "UPC: 198157339941" on the 21ST0008US page, Ryzen 7 250 / 16GB / 512GB / touchscreen + Lenovo official PSREF for ThinkPad E16 Gen 3 (AMD), hosted on Ingram Micro: "21ST0008US … EAN / UPC / JAN : 198157339941". Brand-authored PSREF + retailer spec page — same shape as the batch-6 Brio 100 datasheet precedent. technologygalaxy / simplifiedcomputers agree, non-qualifying.)
- **Price / stock:** B&H $1,217.50 In Stock, Add to cart, free delivery Wed, Nov 25 (page opened fresh 2026-11-21). CDW In Stock, $1,212.99 advertised (track E, search crawl — re-check at add time; B&H is the row). Best Buy listing is Merchant Expo marketplace ($1,311.63) — not usable.
- **Flag:** None on identifiers. Note the B&H page also lists a Ryzen 5 / 256GB config and a non-touch option — pin the Ryzen 7 250 / 512GB / Multi-Touch config only.
- **Deal-site evidence:** None — **队列顶位** (Lenovo sweep pick not carried, track E). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 45. ASUS ROG Swift OLED XG27UCG 27" — Black [queue top-up]
- **Key:** `asus-rog-strix-xg27ucg-black`
- **Category:** monitors
- **Variant pinned:** Black, 27" 4K 160Hz / FHD 320Hz dual-mode Fast IPS, XG27UCG
- **Why it qualifies:** Current ROG dual-mode gaming monitor; MPN VERIFIED (unchanged from track G); UPC now two-sourced — see caveat. Price row is the weak leg (see Flag).
- **Identifiers:** MPN XG27UCG — **VERIFIED** (Micro Center product name + CompSource "Mfr Part # XG27UCG", per track G; Adorama "MFR: XG27UCG" agrees). UPC 197105564633 — **VERIFIED with caveat** (CompSource distributor spec "UPC EAN CODE: 197105564633" for XG27UCG + ASUS official brochure/catalog-object print for 90LM0AG1-B01370 (XG27UCG): "4711387564646 0197105564633 / 197105564633" — brand-authored content mirrored via distributor catalog hosts; Adorama spec page also prints "UPC Code 197105564633". **Caveat:** track G called this PENDING on a stricter reading (CompSource single-source + Adorama not on its qualifying list). This verdict upgrades on the ASUS brochure leg, not on Adorama. If the coordinator applies the strictest reading, downgrade to PENDING + lead (CompSource) — the code itself is not in doubt, only the leg-counting.)
- **Price / stock:** No single clean row — re-confirm at add time:
  - Best Buy $464.99–$469.99 (Model XG27UCG, SKU 12567152; 8–10 day crawls) — **seller of the main offer not confirmed** ("More options from Marketplace sellers $464.99–$575.93"); do not use as the row without a fresh seller check.
  - Micro Center $349.96 InStoreOnly (track G) — in-store-only row, weak.
  - Adorama $464.99 (170-day crawl) / $469.99 — retailer-direct, but Adorama has not been used as the price row in prior batches; corroboration only unless the coordinator accepts it.
  - Slickdeals 2026-04-15: Best Buy $299 (expired); Pangoly 90-day average $444, lowest $299.
- **Flag:** Price row to confirm at add time (Best Buy seller check first). **Supersession risk:** the Gen2 XG27UCGR (4K 162Hz / FHD 485Hz) is current at ROG US $399.00 InStock and Micro Center $399.99 — the original XG27UCG is being superseded; if the Best Buy row is dead at add time, consider the Gen2 instead (it has no UPC lead yet — see track G backlog item 4). Do NOT mix with XG27UCSR (UPC conflicted) or XG27UCDMG / XG27UQDMS (OLED, different models).
- **Deal-site evidence:** None — **队列顶位** (ASUS backlog, track G). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 46. Lenovo Yoga Slim 7x 14" — Cosmic Blue (83QR000AUS) [queue top-up]
- **Key:** `lenovo-yoga-slim-7x-14-cosmic-blue`
- **Category:** laptops
- **Variant pinned:** Cosmic Blue, 83QR000AUS — Snapdragon X2 Plus X2P-42-100 (2026), 16GB LPDDR5X, 512GB SSD, 14" 2K OLED touchscreen (1920x1200, 60Hz, 600 nits), Copilot+ PC
- **Why it qualifies:** Current 2026 ARM ultraportable; Best Buy direct Holiday Deal row. MPN still single-source — the second source sought this session was not found (see Identifiers).
- **Identifiers:** MPN 83QR000AUS — **PENDING (Best Buy model field only).** Targeted re-search for a second source (lenovo.com, B&H, PSREF, "14Q8Y11") surfaced only Best Buy listings and a review-site mention ("Yoga Slim 7 14Q8Y11 (83QR000AUS)" — non-qualifying). No lenovo.com page, no B&H listing, no PSREF hit in-session. One second source away from a pick, same as track E. UPC — **PENDING, no lead found.**
- **Price / stock:** Best Buy SKU 6672161, Sold by Best Buy, Holiday Deal **$649.99** (comp $1,299.99), Add to cart (5-day crawl; Slickdeals confirms $649.99, Nov 16). **Price may have moved:** the freshest 1–2 day crawls show $1,299.99 as the main offer price, with the $649.99 appearing only in the older crawl — re-check live at add time and carry the live price. A second Best Buy SKU 12949047 ($949.00) is sold by PC Heaven (marketplace) — pin SKU 6672161 only. Open-box Excellent $584.99.
- **Flag:** MPN single-source + price in flux ($649.99 vs $1,299.99 across crawls). Do not mix with the 2024 X Elite version (83ED0001US/83ED004WUS/83ED0003US, 14.5" 3K) or the 1TB config 83QR0002US (Best Buy $1,649.99, single-source).
- **Deal-site evidence:** None — **队列顶位** (queue B2, track E). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 47. Lenovo ThinkPad T14 Gen 6 — Black (21QJ00CSUS) [queue top-up]
- **Key:** `lenovo-thinkpad-t14-gen-6-black`
- **Category:** laptops
- **Variant pinned:** Black, 21QJ00CSUS — AMD Ryzen AI 7 PRO 350, 16GB DDR5, 512GB SSD, 14" WUXGA 1920x1200, Win 11 Pro
- **Why it qualifies:** **The missing direct price row from track E is found this session — CDW In Stock with an advertised price.** MPN VERIFIED (unchanged). Promoted from backlog.
- **Identifiers:** MPN 21QJ00CSUS — **VERIFIED** (CDW spec page: "MFG#: 21QJ00CSUS | CDW#: 8391802", Ryzen AI 7 PRO / 16GB / 512GB / WUXGA + Best Buy model field, multiple SKUs). UPC — **PENDING, no lead found.** **Do NOT attach B&H's UPC 199272842804 — that belongs to a DIFFERENT T14 Gen 6 config (21QDS2VV00, $1,699.00).** Repeated here because the warning matters: the code is one search away and wrong for this pin.
- **Price / stock:** CDW In Stock, **$1,811.99 advertised** (CDW#: 8391802; "Ships same day if ordered before 2 PM CT" — multiple CDW search crawls agree on $1,811.99; one crawl showed $1,712.99). **Caveat:** the CDW crawls are 167–173 days old — the price must be re-verified live at add time (track-E caveat 2: CDW prices come from search crawls, not the direct open). Best Buy new listings remain marketplace (Mobile Advance $1,744.14; $1,663.58–$1,856.01 range) or refurbished ($1,049.00, SKU 12834639) — not usable; CDW is the row. No lenovo.com US page for this exact part surfaced.
- **Flag:** CDW price is stale-dated (see above) — re-check at add time; if CDW no longer lists it in stock, this drops back to backlog. Distinct from the carried T14 Gen 5 (21MC000CUS, different generation) and from the Intel config 21QC007CUS (lenovo.com $667.99, different pin).
- **Deal-site evidence:** None — **队列顶位** (queue B3, track E — PROMOTED). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 48. DJI Osmo 360 Standard Combo — Black [Track E substitute]
- **Key:** `dji-osmo-360-standard-combo-black`
- **Category:** action-cameras (same category as Track E's Osmo Action entries)
- **Variant pinned:** Black, Standard Combo — Osmo 360 camera ×1 + Osmo Action Extreme Battery Plus (1950 mAh) ×1 + Protective Pouch ×1 + Rubber Lens Protection Cover ×1 + Lens Cleaning Cloth ×1 + USB-C to USB-C PD Cable ×1. (Per DJI US store "In the Box" + Abt footnotes.) **No Invisible Selfie Stick and no Adjustable Quick-Release Adapter Mount** — DJI US and Abt both state this explicitly; those accessories belong to the Adventure/Essential/Skiing combos. Pin Standard only.
- **Why it qualifies:** DJI's 2025 1-inch 360° camera (native 8K30, 120MP stills, 105GB built-in storage); B&H + Abt in-stock direct rows at the same price; the Track E substitute for the dropped Skiing Combo, now verified on its own merits.
- **Identifiers:** MPN CP.OS.00000441.02 — **VERIFIED with caveat** (Abt product-page body, title "DJI CP.OS.00000441.02 Osmo 360 Camera Standard Combo", opened live 2026-11-21 + Abt launch-day blog "Meet DJI Osmo 360" listing Standard CP.OS.00000441.02 / Adventure CP.OS.00000442.02 + B&H product-page URL slug `dji_cp_os_00000441_02_…` + DroneNerds spec table "SKU CP.OS.00000441.02"). **Caveat — suffix conflict, recorded honestly:** Best Buy's model field prints **CP.OS.00000441.01** (two crawls, SKUs 11961375 / 6635780; one of those rows is 6ave marketplace, the other reads "Sold by Best Buy" at $444.99), and the cameraegg tracker printed **CP.OS.00000441.04** on Nov 16 with no retailer page behind it. The .02 call wins on weight of evidence (Abt page body + Abt blog + B&H slug + DroneNerds spec table, four sources, vs one Best Buy model field and one tracker figure), and all three suffixes share the same UPC 190021135994 and the same box contents, so this is a retailer data-entry variant, not a different product. If the coordinator requires zero-conflict, downgrade MPN to PENDING + strong lead (.02) and do NOT attach .01 or .04. UPC 190021135994 — **VERIFIED with caveat** (B&H spec page "UPC: 190021135994", opened live 2026-11-21 + DroneNerds spec table "UPC 190021135994"; Amazon / Snapklik / Tanotis / PhotoGear NZ agree, all non-qualifying). Caveat: the second leg is DroneNerds (US DJI authorized dealer, off the core qualifying list), same shape as the batch-5/6 accepted retailer+distributor precedents.
- **Price / stock:** B&H **$417.99** In Stock (was $549.99, Holiday Savings $132.00), Add to Cart, free delivery Wed Nov 25, page opened live 2026-11-21 21:01 UTC. Abt **$417.99**, comp. value $549.99, "Price includes manufacturer rebate which ends **11/30/2026**", limit 2 per customer. DroneNerds **$417.99** In Stock – Ready to Ship. DJI US list $549.99 (Standard Combo; Adventure Combo $531.99 on the same page — a promo inversion, not an error).
- **Flag — the brief's price is stale, do not carry it:** the brief (and Track E) cited B&H **$404.77**. That was the Nov 16 price (cameraegg tracker + 3-day-old B&H crawl). The live B&H open on Nov 21 shows **$417.99**; Abt and DroneNerds agree at $417.99. Price moved up $404.77 → $417.99 during the week; carry $417.99 and re-check at add time. B&H page slug says "adventure_combo" while the page content is the Standard Combo — the slug is unreliable for the combo name (the .02 number in it still corroborates the MPN). Best Buy rows are not the row (6ave marketplace $428.99; $444.99 SKU). Do NOT mix with Adventure Combo CP.OS.00000442.02 ($531.99), Essential Combo ($599.00), Skiing Combo (dropped in Track E — DJI US OutOfStock, no MPN), Vlog / Helmet / Vortex combos.
- **Deal-site evidence:** None — **Track E substitute** (replaces the dropped Skiing Combo; verified on its own merits in Track G). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 49. Samsung Smart Monitor M70F 32" — White (LS32FM703UNXZA) [queue top-up]
- **Key:** `samsung-smart-monitor-m70f-32-white`
- **Category:** monitors
- **Variant pinned:** White, 32", LS32FM703UNXZA — 4K UHD (3840×2160) VA, 60Hz, HDR10, Samsung Vision AI, Tizen Smart TV Apps, Gaming Hub, USB-C 65W, 2× HDMI 2.0, 10W speakers. (Per Abt + B&H + Samsung.com.) 2025 model (Amazon "Date First Available June 24, 2025" — Amazon is non-qualifying for price/identifiers but the date is corroborated by Samsung review dates from Jul 2025.)
- **Why it qualifies:** Mainstream Samsung 2025 Smart Monitor; three-way price agreement at $299.99 across B&H + Abt + Samsung.com, all InStock live 2026-11-21. The strongest Samsung backlog item from batch 6 (track F B3), now with a B&H row that did not exist in-session then.
- **Identifiers:** MPN LS32FM703UNXZA — **VERIFIED with caveat** (Abt product-page title/body names "Samsung LS32FM703UNXZA M7 M70F Smart Monitor", opened live 2026-11-21 + B&H product-page URL slug `samsung_ls32fm703unxza_m70f_32_4k_hdr` + Samsung.com canonical product URL `…/32-inch-smart-monitor-m70f-4k-uhd-vision-ai-monitor-sku-ls32fm703unxza/`). Caveat: only the Abt leg prints the MPN in page body text; the B&H and Samsung.com legs carry it in the product URL. No second body-text print was found in-session. UPC 198957027796 — **PENDING + lead (B&H only)**. Printed on the opened B&H spec page ("UPC: 198957027796"). Tanotis (India) agrees — non-qualifying, does not upgrade. No second qualifying source found despite a targeted search.
- **Price / stock:** B&H **$299.99** In Stock (was $399.99, Holiday Savings $100.00), Add to Cart, free delivery Wed Nov 25, page opened live 2026-11-21 21:01 UTC. Abt **$299.99** InStock (JSON-LD), page opened live the same day. Samsung.com **$299.99** InStock (JSON-LD), page opened live the same day. No promo end date stated at any of the three channels — re-check at add time.
- **Flag:** No Best Buy 32" M70F row exists (Best Buy carries only the 43" M70F, LS43FM702UNXZA, SKU 6632216). Woot lists a **factory-reconditioned** 32" M70F at $239.99 — excluded (refurb, not a new direct row). Do NOT mix with the 43" M70F (UPC 198957005435 per B&H, different size/MPN/UPC), the M70B LS32BM703UNXZA (older generation), or the M70D. B&H's page also offers a Black 32" option at $299.99 — the Black 32" is a different MPN (not pinned here); the UPC 198957027796 is read against the page's White 32" default variant (URL slug + JSON-LD product name both say White).
- **Deal-site evidence:** None — **队列顶位** (batch-6 Samsung backlog, track F B3). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 50. Lenovo IdeaPad 5 2-in-1 14" — Luna Grey (83GH000AUS) [queue top-up]
- **Key:** `lenovo-ideapad-5-2-in-1-14-luna-grey`
- **Category:** laptops
- **Variant pinned:** Luna Grey, 83GH000AUS — Snapdragon X Plus X1P-42-100 8-core (up to 3.4 GHz), 16GB LPDDR5x-8448 onboard, 1TB M.2 NVMe SSD, 14" WUXGA 1920×1200 OLED touchscreen (glossy, 400 nits, 100% DCI-P3, 60Hz), Win 11 Home, Wi-Fi 7, 57Wh, 3.28 lb. Family 14Q8X9. (Per B&H spec page + Target + Newegg + Lenovo PSREF family sheet.)
- **Why it qualifies:** Mainstream Lenovo Copilot+ convertible; clean B&H in-stock direct row at $699.00; the MPN is now three-sourced (the batch-6 blocker — Staples as second source — is no longer needed).
- **Identifiers:** MPN 83GH000AUS — **VERIFIED** (B&H spec page, URL slug `lenovo_83gh000aus_…`, Q&A confirms "model 83GH000AUS", opened live 2026-11-21 + Target product page, description "The Lenovo IdeaPad 5x 2-in-1 14Q8X9 (83GH000AUS)…" + Newegg listing page "Model Identifiers … model/part 83GH000AUS", search-fetch — Newegg direct open still hits the bot wall, per the Track E caveat, but it is now the third leg, not the second). Target is used as a qualifying retailer here, following the batch-7 Track E precedent (Target legs for Legion 5a MPN/UPC). UPC 198154657529 — **PENDING + lead (B&H only)**. Printed on the opened B&H spec page. A targeted search for the number returned only B&H hits (plus the Newegg MPN page, which prints no UPC). No second source found.
- **Price / stock:** B&H **$699.00** In Stock (was $999.00, Holiday Savings $300.00), Add to Cart, free delivery Wed Nov 25, page opened live 2026-11-21 21:01 UTC. Staples $899.99, in-store only (stale 49–75-day crawls — not the row). Target $1,017.99 Out of Stock (not the row).
- **Flag:** Color pinned **Luna Grey** — Target titles the listing "…Luna Gray" and names 83GH000AUS in the description; corroborated by Lenovo PSREF for the 14Q8X9 family ("Case Color – Luna Grey") and by the Woot 83GH0009US Luna Grey listing (different config). Do NOT mix with 83GH0008US (B&H "No Longer Available"), 83GH0000US (different Newegg config), 83GH0009US (Woot refurbished), or the AMD Ryzen AI 5 340 IdeaPad 5 2-in-1 configs (different CPU family). "IdeaPad 5x" (Target/Staples naming) vs "IdeaPad 5 2-in-1" (B&H naming) is the same part/config — a naming variant, not a different model. B&H Used from $621.95 excluded (used, not new).
- **Deal-site evidence:** None — **队列顶位** (batch-6 Lenovo backlog). No Slickdeals/DealMoon thread cited or found for this model in-session.

## Membership check (coordinator, scripted)

- Reference rebuilt from `price_agent/catalog.py` as `data/rework7/catalog_ref_500.tsv` (500 rows, verified 211 / pending 289). Each track re-ran its own check against a rebuild; the coordinator re-ran the scripted check on the final 50 in `data/rework7/candidates_batch7_50.tsv` (`data/rework7/membership_batch7.py`): exact key, model-name substring (normalized, both directions), MPN, UPC (including pending leads), plus intra-batch duplicates. **Result: 0 collisions.**
- Track-level membership: A 0, B 0 (incl. the false "Beats/Sennheiser already in catalog" brief premise — grep finds zero rows for either brand), C 0 (AirTag 4-pack adjudicated as a distinct pack-size sibling of the in-catalog single pack, per the catalog's own note), D 0, E 0, F 0 (Echo Show 8 grep hit is only a notes-field mention in `jbl-live-flex-3-black`), G 0 (Osmo 360 vs Track E Action 4/6 + Pocket 3; Legion 5i vs catalog Legion Pro 5 Gen 10 + Track E Legion 5a; M70F vs M70B/M70D; IdeaPad 5 zero hits in the whole catalog).
- Sibling adjudications recorded in the entries above (OpenRun vs Pro/Mini, OpenFit 2 SE vs OpenFit 2, Era 100 2-pack vs single, Arc Ultra bundle vs soundbar, Monitor III Cream vs Black, Crusher Evo color MPNs, Stealth Pro II Xbox vs PS/PC-only, AZ100 UPC conflict, MTW4 colorways, Space 2 Pro vs Space 2, Solo Buds Orange vs Matte Black, Pixel 10a vs Pixel 10, moto g stylus/power vs 2024, edge 2026 vs Edge 2025/2024/70, iPhone 17 Pro Silver vs Cosmic Orange/Deep Blue, M7 75M7SR vs 75M7SG, U7900H vs U7900F, S84H QN vs UN, Q6CH vs Q65H/Q75H/Q85H, HW-B650F vs HW-B650, LS50H vs Music Frame, Onyx Studio 8 vs 7/9, Action 4/6 Essential vs Standard/Adventure, LIT Hero vs HERO 13, Pocket 3 Creator vs Standard, Ace Pro 2 Costco bundle vs Octa Edition / Xplorer Pro Bundle, Yoga 7i 83JT0000US vs 83TE0004US, Legion 5a 83Q70068US vs 83Q70003US, Zenbook A14 vs UX3407RA, OmniBook 3 vs Starlit Blue sibling, MAG 321UP vs X24, Yeti GX Black vs White, Echo Show 8 2025 vs 3rd-gen, Echo Hub vs Nest Hub, ULT Tower 10 vs track-D row, Strix G16 G614PR vs regional config, Watch7 Green vs Watch8/Watch9, E16 Gen 3 config pins, XG27UCG vs XG27UCSR/Gen2, Yoga Slim 7x vs 2024 X Elite, T14 Gen 6 21QJ00CSUS vs 21QDS2VV00, Osmo 360 Standard vs Adventure/Essential/Skiing, M70F 32" vs 43" / M70B / M70D, IdeaPad 5 83GH000AUS vs 83GH0008US/0000US/0009US).

## Dropped / not carried

- **Hisense E6SR 50" (50E6SR) — DROP.** Amazon-only price evidence (Slickdeals thread f/20148267, 2026-10-12, expired, Amazon $247.99); no Best Buy listing, no Walmart row (Walmart returns only the 50" R6 Series 50R6E3 at $228.00), no hisense-usa.com product page, no spec sheet. MPN 50E6SR attested only by Smartprix (non-qualifying aggregator). UPC: no lead anywhere. Do not revive on the Amazon price. The 65" E6SR sibling appears on Slickdeals ($378, same expired thread) — a different size, needs its own verification, not a substitute.
- **DJI Osmo 360 Skiing Combo — DROP.** No MPN lead at all (no B&H/Best Buy spec page; Standard = CP.OS.00000441.04, Adventure = CP.OS.00000442.04 — neither belongs to the Skiing Combo). UPC non-qualifying lead only (Amazon 190021996731, and its "Built-In Media" text contradicts DJI's own box contents — Amazon says a 1.5m selfie stick; DJI says 1.2m). No in-stock direct row: DJI US $618.99 OutOfStock. Replaced by entry 48 (Osmo 360 Standard Combo), verified on its own merits in Track G.
- **Samsung Galaxy Book5 360 15.6" Gray (NP750QHA-KA1US) — DROP, stays in backlog.** Price conflict still unresolved after re-check: Best Buy crawl A $358.99 ("Save $991, Comp. Value: $1,349.99" — glitch-shaped), crawl B $2,187.81 Unavailable (SKU 13224856); buybeststores.com mirror $609.99 (not qualifying). MPN NP750QHA-KA1US single-source (Best Buy model field only); UPC no lead. Do NOT carry on the $358.99 or the $2,187.81. Do not confuse with Galaxy Book5 15.6" NP750XHD-KB1US (Best Buy $799.99 BF) or Book5 Pro 360 (marketplace-only at Best Buy).
- **Lenovo Legion 5i 15.1" Eclipse Black (83LY0000US) — NOT carried, stays in backlog.** MPN VERIFIED with caveat (Newegg listing + Lenovo PSREF spec PDF on a mirror host); UPC 198155802546 PENDING + lead (PSREF only). Walmart $1,499 row could not be opened directly — Slickdeals click-through redirect and walmart.com search both hit Walmart's "Robot or human?" wall, and the full listing slug is truncated in every search result, so the URL cannot be reconstructed without guessing. Three independent trackers corroborate $1,499 (Nov 14–21), but the row is second-hand. **Do not force it in to reach 50 — the batch is already at 50 without it.** Revisit only after a live walmart.com open (price, seller = Walmart.com, part number on the listing) plus a second UPC source.

## Queued backlogs (remaining, after this batch)

Batch-6 leftovers not used in this batch, plus the four items dropped/not carried above. Start the next batch here.

- **Lenovo:** Legion 5i 83LY0000US (see above — needs a live Walmart open); Legion Pro 7 Gen 10 AMD; T16 Gen 4 21QN0045US; LOQ 83VA001PUS; T14 Gen 5 Gray 21MC000NUS; ThinkVision P27u-20.
- **Samsung:** G6 G60SD; G8 G80SD; HW-B650 (older model, clearance-flagged — do not confuse with the carried HW-B650F); Watch Ultra gen 1; Buds2 Pro; Tab S10 FE 256GB; M70F 43" (LS43FM702UNXZA, different size from the carried 32").
- **ASUS:** XG27UCSR (UPC conflicted); XG27UCG Gen2 (XG27UCGR, ROG US $399.00 InStock, no UPC lead yet); Delta II White; Keris II Ace White; Scope II 96 White; BT8 3-pack; BT10 1-pack; VG27AQ1A; VG279QM5F; TUF M3 Gen II; Vivobook S 14 Q423SA.
- **Alternates:** ROG Zephyrus G14 2025 GA403UM; HP OMEN Transcend 14 2025; Alienware 16 Aurora (HOLD).
- **New backlog from this batch:** Hisense E6SR 50" (needs a direct row); DJI Osmo 360 Skiing Combo (needs DJI restock + qualifying MPN/UPC); Samsung Galaxy Book5 360 (needs a consistent direct price + second MPN source); Lenovo Legion 5i (needs a live Walmart open); TCL Q6CH online row (if the warehouse-only carry is held); XG27UCG Gen2 (see ASUS above).

## Add-time re-check list (per skill, before any row is written)

- All Best Buy Black Friday prices (end Nov 28, 2026) and all Costco Holiday Savings prices (end Nov 30, 2026); every price and stock state on the live merchant page.
- OpenFit 2 SE: Costco stock (conflicted crawls); UPC still has no lead.
- OpenRun Air 2 UPC 810202689213 on the Best Buy spec panel (SKU 6680820); downgrade to PENDING if it does not match.
- Era 100: no single-unit deal-site evidence (Sift evidence is 2-pack-only); the B&H $219 row stands on its own.
- Arc Ultra: Costco stock (conflicted crawls).
- Technics AZ100 UPC conflict (885170433021 vs 885170441613) — needs a qualifying spec page; re-check B&H after the Nov 30, 2026 restock.
- Pixel 10a MPN + UPC; g stylus UPC; g power MPN + UPC (do not attach 840023277283 without a qualifying tie to PB640007US); edge 2026 UPC (no lead); iPhone 17 Pro UPC (B&H spec page / Best Buy spec panel); AirTag Walmart price ($69.99 vs $79.99 vs code-gated $59.99).
- M7SR MPN second source (no hisense-usa.com page found 2026-11-21); S84H MPN caveat (Samsung Parts USA leg); U7900H UPC second source (198957409578); B650F UPC (do not attach 887276936956 / 887276864211); Onyx Studio 8 UPC (do not attach 028292289859 / 028292289873 / 657768329135 / 094148666167); Q6CH carry-vs-hold decision (warehouse-only price).
- Action 4 / Action 6 Essential DJI stock wording; Insta360 Costco stock (one crawl showed OutOfStock); Yoga 7i UPC 198155420948 on a qualifying spec page; OmniBook 3 MPN on hp.com to clear the datasheet-host caveat; Zenbook A14 UPC 197105832077 on a second source; Legion 5a B&H "Limited supply" price.
- XG27UCG Best Buy seller check (SKU 12567152) before using any Best Buy row; Yoga Slim 7x live price ($649.99 vs $1,299.99); T14 Gen 6 CDW price live (crawls 167–173 days old); M70F UPC second source (198957027796); IdeaPad 5 UPC second source (198154657529); Osmo 360 B&H price (moved $404.77 → $417.99 within the week; Abt rebate ends 11/30/2026).
- Echo Show 8 + Echo Hub: drop both together at approval if the user wants smart displays out.
