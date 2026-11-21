# Track D — rework7 findings (TVs / soundbars / speakers, 8 models)

- **Date:** 2026-11-21 (research in-session, via `browser.search` / `browser.open`; no live-browser task).
- **Catalog state at draft time:** 500 models in `price_agent/catalog.py`, verified identifiers 211 / pending 289 (per `/tmp/catalog_ref_500.tsv`, 500 rows). Ranking 151, matched 168 (per MEMORY, 2026-11-21).
- **This track:** 8 candidates (Hisense E6SR 50", Hisense M7 75", Samsung U7900H 75", Samsung S84H 65", TCL Q6CH, Samsung HW-B650F, Samsung Music Studio 5 HW-LS50H, Harman Kardon Onyx Studio 8).
- **Outcome: 7 carried (6 MPN-VERIFIED, 1 MPN-PENDING), 1 DROPPED (E6SR 50"). UPC VERIFIED 1 / 7 carried (LS50H only).** No rule was loosened: the E6SR was dropped exactly on the brief's condition (no clean direct row), and no UPC was attached on a single or conflicting source.
- **Identifier tally (carried 7): MPN VERIFIED 6 / 7. UPC/EAN VERIFIED 1 / 7 (14%). UPC PENDING 6 / 7** (of which 1 has a single-source lead, 2 have conflicting non-qualifying leads, 3 have no lead at all). The UPC gap is structural for this track: both Hisense TVs and both Samsung TVs print no UPC on any qualifying page found, and the two soundbars' UPCs exist only in conflicting non-qualifying sources.

## Membership check

Script: inline Python vs `/tmp/catalog_ref_500.tsv` (500 rows). Checks every candidate by exact key, model-name substring (normalized, both directions), MPN, and UPC (including pending leads). **Result: 0 true collisions; intra-track duplicate keys / MPNs / UPCs: none.**

Adjudicated non-collisions (recorded so they are not re-litigated):
- **No Hisense, no TCL, no Harman Kardon model exists anywhere in the 500.** The catalog's TV count is zero — these would be its first TVs. Category `tvs` does not exist yet in the catalog; coordinator to confirm the category name.
- `samsung-hw-b650f-black` vs **batch-6 Samsung backlog HW-B650 (clearance-flagged)**: distinct models — see entry 6. HW-B650 is NOT in the catalog (grep: no `b650` hit); the backlog flag does not transfer to B650F.
- `samsung-music-studio-5-black` (HW-LS50H/ZA) vs in-catalog `samsung-music-frame-black` (HW-LS60D/ZA, verified): distinct products — Music Studio 5 is a 2.0ch smart speaker; Music Frame is a picture-frame speaker. Do not mix.
- `samsung-u7900h-75` vs Samsung U7900F (2025, UN75U7900FFXZA, Best Buy SKU 6639197): different model year/generation, not in the catalog. Do not mix.
- `samsung-s84h-65` vs Samsung S85H / S90H (2026 OLED siblings seen in Best Buy series rail): different series, neither in the catalog. Do not mix.
- `hisense-m7sr-75` vs Hisense 75M7SG (Canada, Google TV, UPC 888143026817): different regional variant — **do NOT attach the Canadian UPC 888143026817 to the US 75M7SR**.
- `tcl-q6ch-black` vs TCL Q65H / Q75H / Q85H soundbars: different models in TCL's Q Series; Q6CH is the Costco-specific 5.1ch model.
- `harman-kardon-onyx-studio-8-black` vs Onyx Studio 7 / 9: different generations, neither in the catalog.

## Candidates

### 1. Hisense E6SR 50" 4K TV — DROP

- **Key (proposed, unused):** `hisense-e6sr-50`
- **Category:** tvs
- **Variant pinned:** 50" Class E6SR Series Hi-QLED 4K UHD Smart Roku TV (2026), model 50E6SR
- **Why it fails:** the brief's condition was explicit — Amazon's price cannot be used as a price source, find a Best Buy or equivalent direct row, otherwise DROP. No clean direct row exists.
  - Price evidence is Amazon-only: Slickdeals thread f/20148267 (2026-10-12, expired) lists the 50" (50E6SR, 2026 Model) at **$247.99 at Amazon**; Smartprix (aggregator, non-qualifying) lists $247.98–$249.99 "available at Amazon". Amazon in any form is excluded.
  - No Best Buy listing found (searched Best Buy + Walmart: Walmart returns only a different Hisense, the 50" R6 Series 50R6E3 at $228.00; no 50E6SR page at either retailer).
  - No hisense-usa.com product page found for 50E6SR; no Hisense spec sheet found.
  - MPN 50E6SR is attested only by Smartprix (non-qualifying aggregator) — single, non-qualifying source.
  - UPC: no lead anywhere.
- **Identifiers:** MPN 50E6SR — NOT VERIFIED (single non-qualifying source). UPC — PENDING, no lead.
- **Price / stock:** none usable. Amazon $247.99 recorded for the record only, excluded as a source.
- **Flag:** DROP per the brief. Do not revive on the Amazon price. The 65" E6SR sibling appears on Slickdeals ($378, same expired thread) — a different size, needs its own verification, not a substitute.
- **Deal-site evidence:** Slickdeals front page (brief-supplied); independently found thread f/20148267, 2026-10-12, expired, Amazon $247.99 for the 50".

### 2. Hisense M7 75" MiniLED 4K TV — PENDING identifiers, clean direct row

- **Key:** `hisense-m7sr-75`
- **Category:** tvs
- **Variant pinned:** 75" Class M7 MiniLED Series Hi-QLED 4K UHD Smart Roku TV (2026). **US model is 75M7SR (Roku)** — the brief's "约 75M7" is a shorthand; the full US model code is 75M7SR. Do not use the Canadian 75M7SG (Google TV).
- **Why it qualifies:** Mainstream 2026 Hisense MiniLED; Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart. First Hisense TV in the catalog (no Hisense model in the 500 at all).
- **Identifiers:** MPN 75M7SR — **PENDING + strong lead** (Best Buy model field, SKU 6686979, is the only qualifying source; Hisense's own support team answers on the Best Buy Q&A name "the Hisense 75M7SR" — brand confirmation, but hosted on the same Best Buy page, so it does not count as a second source. No hisense-usa.com product page or spec sheet was found). UPC — **PENDING, no lead** (no qualifying page prints one; the Canadian 75M7SG UPC 888143026817 belongs to a different variant — do NOT attach).
- **Price / stock:** Best Buy **$499.99** Black Friday (comp. value $899.99), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). Open-box from $361.99 — excluded (not new).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Refresh-rate conflict — pin 60Hz native:** the Best Buy spec panel, Hisense's own Q&A answers, the Slickdeals spec list, and the Tech Steve review all say 60Hz native (Motion Rate 240, VRR/ALLM); one Best Buy marketing blurb in an older crawl claims "Native 144Hz" — that is wrong for this model, do not carry it. 144Hz / Dolby Atmos are 85"-only features per Hisense's own creator materials.
- **Deal-site evidence:** Slickdeals front page (brief-supplied: Best Buy $500, orig $900); independently found Slickdeals thread 2026-11-16 (75" M7, Best Buy) and a Threads deal post 2026-11-21 ($499.99, down from $899.99). Single deal-site thread retrieved in-session beyond the brief.

### 3. Samsung U7900H 75" Crystal UHD 4K TV — MPN VERIFIED, UPC single-source lead

- **Key:** `samsung-u7900h-75`
- **Category:** tvs
- **Variant pinned:** 75" Class Crystal UHD U7900H 4K Smart TV (2026), UN75U7900HFXZA. Tizen, Crystal Processor 4K, 60Hz native (DLG 120Hz).
- **Why it qualifies:** Mainstream Samsung 2026 Crystal UHD; Best Buy direct Black Friday row + Costco in-store row + Abt in-stock row. Distinct from the 2025 U7900F (UN75U7900FFXZA, SKU 6639197).
- **Identifiers:** MPN UN75U7900HFXZA — **VERIFIED** (samsung.com US product page + Best Buy model field, SKU 6688397). UPC 198957409578 — **PENDING + lead** (P&C Richard Samsung spec-sheet PDF: "MODEL: UN75U7900H / ORDER CODE: UN75U7900HFXZA / UPC CODE: 198957409578" — one qualifying source only; madefordeals.com agrees but is a non-qualifying aggregator. Do not confuse with the U7900F UPCs: UN75U7900FFXZA = 887276951904, UN85U7900FFXZA = 887276951997).
- **Price / stock:** Best Buy **$399.99** Black Friday (comp. value $599.99), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). Costco **$399.99**, item 9675079, Holiday Savings Nov 16–30, 2026 (in-store; also listed online). Abt $397.99 InStock. Samsung.com $399.99 OutOfStock — corroboration only. (An older Slickdeals thread showed $449.99; the price has since dropped to $399.99.)
- **Flag:** Promo price — Best Buy Black Friday ends Nov 28, 2026; Costco Holiday Savings ends Nov 30, 2026. UPC needs one more qualifying source at add time (Best Buy spec panel did not reproduce a UPC in the crawl).
- **Deal-site evidence:** Slickdeals Black Friday Sift (brief-supplied: Costco $399.99, orig $449.99, 130 saves — the "130 saves" figure is brief-supplied, not independently confirmed); independently found Slickdeals thread f/20280309 (UN75U7900HFXZA, $449.99 pre-drop) and Costco97/Instagram 2026-11-18 confirming Costco $399.99, item 9675079.

### 4. Samsung S84H 65" OLED 4K 120Hz TV (2026) — MPN VERIFIED, UPC no lead

- **Key:** `samsung-s84h-65`
- **Category:** tvs
- **Variant pinned:** 65" Class S84H Series OLED 4K UHD SamsungVision AI Smart Tizen TV (2026). **MPN is QN65S84HAEXZA — the brief's "约 UN65S84H" is wrong; Samsung OLEDs use the QN prefix.** "Only at Best Buy" exclusive.
- **Why it qualifies:** Mainstream Samsung 2026 OLED (NQ4 AI Gen2, OLED HDR, Motion Xcelerator 120Hz, 4x HDMI 2.1 with 4K@120Hz/VRR/ALLM, eARC on port 3); Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart.
- **Identifiers:** MPN QN65S84HAEXZA — **VERIFIED with caveat** (Best Buy model field, SKU 6689681 + Samsung Parts USA compatibility list naming QN65S84HAEXZA as a model number — a Samsung-operated page, but a parts listing rather than a product spec page; if a strict product-page second source is required, this drops to PENDING + strong lead). UPC — **PENDING, no lead** (no spec sheet, retailer spec page, or datasheet found printing one; Slickdeals threads name only the MPN).
- **Price / stock:** Best Buy **$899.99** Black Friday (comp. value $2,099.99, save $1,200), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21). "Only at Best Buy" badge on the page.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Price history: $999.99 on 2026-10-30/31 (Slickdeals thread f/20235120), now $899.99. UPC has no lead at all — re-check at add time; do not attach any code from Amazon/eBay mirrors.
- **Deal-site evidence:** Slickdeals Tech / front page (brief-supplied: Best Buy $899.99, orig $2,099.99); independently found Slickdeals front-page thread f/20265210 (2026-11-05, $899.99) and f/20235120 (2026-10-30, $999.99).

### 5. TCL Q6CH 5.1ch Soundbar with Wireless Subwoofer — MPN VERIFIED, UPC no lead, warehouse-only promo price

- **Key:** `tcl-q6ch-black`
- **Category:** soundbars
- **Variant pinned:** Black, Q6CH — 5.1ch, wireless subwoofer, up to 580W, Dolby Atmos, DTS:X, RAY-DANZ, HDMI eARC, Bluetooth 5.3. Costco-specific model (item 2012476).
- **Why it qualifies:** Mainstream TCL Q Series soundbar; Costco is the seller of record (retailer-direct). TCL's own US support site lists Q6CH in its Q Series soundbar manuals.
- **Identifiers:** MPN Q6CH — **VERIFIED** (Costco.com model field, item 2012476 + TCL US support Q Series page listing "Q6CH — User Manual"). UPC — **PENDING, no lead** (no qualifying source prints one; Costco.com spec table has no UPC field).
- **Price / stock:** Costco.com **$299.99 OutOfStock** (JSON-LD, page opened fresh 2026-11-21) — the online row is dead at list price. **In-warehouse $199.99** (Holiday Savings, $100 off, through Nov 30, 2026) — confirmed by CostClubWeekly price history (Nov 16–22, $199.99, Northeast + Midwest) and in-store video 2026-11-18 (item 2012476, $199.99, Holiday Savings through Nov 30).
- **Flag:** **No live online price row** — the $199.99 is warehouse-only and the snapshot feed may not capture it; the online listing is OOS at $299.99. Coordinator decides whether to carry on the warehouse price or hold until an online row returns. UPC has no lead. Do not mix with TCL Q65H/Q75H/Q85H (different Q Series models).
- **Deal-site evidence:** Slickdeals Black Friday Sift — confirmed in-session: "TCL Q6CH 5.1ch Soundbar with Wireless Subwoofer | Costco Wholesale | $199.99, Regular price $299.99, 33% Off, 15 saves, Oct 26, Live Nov 15 until Nov 29".

### 6. Samsung HW-B650F 3.1ch DTS Virtual:X Soundbar — MPN VERIFIED, UPC conflicted (do not attach)

- **Key:** `samsung-hw-b650f-black`
- **Category:** soundbars
- **Variant pinned:** Black, HW-B650F/ZA — B-series 3.1ch, 370W, wireless subwoofer, Dolby Audio / DTS Virtual:X, Q-Symphony, Voice Enhance, Night Mode, Game Mode (2025 model).
- **Why it qualifies:** Mainstream Samsung 2025 B-series soundbar; Best Buy direct Black Friday row, sold by Best Buy, InStock, Add to Cart, 874 reviews.
- **Identifiers:** MPN HW-B650F/ZA — **VERIFIED** (Best Buy model field, SKU 6619391 + Samsung support page "B-series Soundbar HW-B650F 3.1 ch Subwoofer (2025)"). UPC — **PENDING, conflicted leads, do not attach any**: Amazon (non-qualifying) prints 887276936956 for HW-B650F/ZA; Ubuy (non-qualifying) prints 887276864211 for "HW-B650F"; the Canadian HW-B650F/ZC has its own UPC 887276950938 (Kawartha TV, Canadian, non-qualifying — and a different suffix variant). No qualifying source prints a US /ZA UPC.
- **Price / stock:** Best Buy **$199.99** Black Friday (comp. value $349.99, save $150), sold by Best Buy, InStock, Add to Cart (page opened fresh 2026-11-21).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **B650F vs B650 — confirmed different models, do not mix:** HW-B650 (2023, HW-B650/ZA) is 430W, no Q-Symphony, B&H EAN 8806097097099, Crutchfield page is for the B650; HW-B650F (2025, HW-B650F/ZA) is 370W, adds Q-Symphony and a more compact design — Best Buy's own Q&A states "The B650F is the updated version of the HW-B650 with Q-Symphony and a more compact design." The batch-6 backlog entry "HW-B650 (clearance-flagged)" refers to the older model only; its flag does not transfer. EU suffixes (/ZF EAN 8806097069225, /XU EAN 8806097092049) are not US codes.
- **Deal-site evidence:** Slickdeals Sift (brief-supplied, Best Buy); the Slickdeals thread itself was not retrieved in-session — single-source (brief) for the Slickdeals side. Corroborated by dealnews 2026-11-16 ("Best Buy's Black Friday Deal drops the Samsung B-Series HW-B650F soundbar to $150 off its $350 regular price... $200") and Digital Trends.

### 7. Samsung Music Studio 5 HW-LS50H Wireless Smart Speaker — both identifiers VERIFIED; Woot judged NOT qualifying

- **Key:** `samsung-music-studio-5-black`
- **Category:** speakers
- **Variant pinned:** Black, HW-LS50H/ZA — Music Studio 5, 2.0ch, Wi-Fi + Bluetooth, Wireless Dolby Atmos, Q-Symphony, SpaceFit Sound Pro, Alexa + Bixby built-in (2026).
- **Why it qualifies:** Mainstream Samsung 2026 smart speaker; Best Buy direct Black Friday row, sold by Best Buy, InStock. Strongest pick in this track — the only one with both identifiers VERIFIED.
- **Identifiers:** MPN HW-LS50H/ZA — **VERIFIED** (Best Buy model field, SKU 6670424 + Walts TV spec page MPN + Precision distributor Part #). UPC 198957266393 — **VERIFIED** (Walts TV retailer spec page: "Model HW-LS50H | MPN HW-LS50H/ZA | UPC 198957266393" + Precision distributor listing: "Part #: HW-LS50H/ZA, UPC: 0198957266393" — retailer + distributor, per the batch-5 precedent).
- **Price / stock:** Best Buy **$299.99** Black Friday, sold by Best Buy, SKU 6670424, InStock (page data, 2026-11-21; list/reference $499.00). Ignore the Best Buy marketplace SKU 12696700 ($283.68, IPC-STORE) — marketplace, excluded.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. **Woot $214.99 is NOT a qualifying price row — judgment:** (1) Woot is an Amazon subsidiary ("Woot! An Amazon Company", per dealnews) and Amazon in any form is excluded as a price source; (2) the Woot listing carries only a 90-day Woot Limited Warranty, not the Samsung manufacturer warranty — a non-standard channel; (3) the listing is internally inconsistent — title says HW-LS50H, but "What's in the Box" says "(1) Samsung HW-LS51H Wireless Speaker", and the Woot URL slug is for HW-LS51H. The $214.99 is recorded as deal evidence only, never as the price row. Separately: the retail box is labeled "Music Studio 5 HW-LS50H / HW-LS51H", suggesting LS51H is a channel variant of the same hardware — pin /ZA only. Do not use the Canadian /ZC UPC 198957281686 (Visions/McNain) for the US /ZA model.
- **Deal-site evidence:** Slickdeals Tech (brief-supplied: Woot $214.99); independently found dealnews Woot coverage ($215, "best price by $85", free shipping w/ Prime) and a Slickdeals EPP bundle thread f/20179509 naming HW-LS50H/ZA (different deal — QN80H TV + speaker bundle). Single-source (brief) for the Slickdeals-Tech placement itself.

### 8. Harman Kardon Onyx Studio 8 Portable Bluetooth Speaker — MPN VERIFIED, brand-direct row (eBay excluded)

- **Key:** `harman-kardon-onyx-studio-8-black`
- **Category:** speakers
- **Variant pinned:** Black, HKOS8BLKAM — portable stereo Bluetooth speaker, 50W RMS, 120mm woofer + dual tweeters, Bluetooth 5.2, up to 8 hours. (Blue = HKOS8BLUAM, Champagne = HKOS8CPNAM — pin Black only.)
- **Why it qualifies:** Mainstream Harman Kardon portable speaker; **brand-direct row at harmankardon.com, $99.99 InStock**. The brief's eBay $99.99 is unusable (platform seller) — and unnecessary: the same $99.99 is live at the brand's own US store.
- **Identifiers:** MPN HKOS8BLKAM — **VERIFIED** (harmankardon.com "Item#: HKOS8BLKAM" + Best Buy model field, SKU 13145257 + B&H product title/URL). UPC — **PENDING, conflicted leads, do not attach any**: non-qualifying sources disagree — Desertcart prints 028292289859 for Black; eBay/Ubuy print 028292289873, but that code is tied to the **Blue** HKOS8BLUAM (eBay listing: "UPC 028292289873, Model HKOS8BLUAM") — do NOT attach Blue's code to Black; Amazon prints 657768329135 for a Renewed listing; Ubuy prints 094148666167 for a bundle listing. Neither the B&H spec page (opened fresh 2026-11-21 — no UPC row in its spec table) nor harmankardon.com prints a UPC.
- **Price / stock:** harmankardon.com (Official Harman Kardon US store) **$99.99** InStock, list $499.95 (page opened fresh 2026-11-21; JSON-LD InStock). Best Buy's $99.99 row is **sold & shipped by JBL Store** (Best Buy marketplace) — excluded; Best Buy has no Best Buy-direct row for this model. B&H is Discontinued at $499.95 — not a row, corroboration only.
- **Flag:** Deep promo ($99.99 vs $499.95 list, 80% off) with no stated end date — re-check at add time. Model year 2022 (per Amazon) and discontinued at B&H — the brand-direct channel is the only live row; treat as a clearance-style promo, not a new launch. Android Police (2026-11-18) confirms the deal is "purchase directly from Harman Kardon".
- **Deal-site evidence:** Slickdeals front page / Tech (brief-supplied: eBay $99.99 — eBay price excluded as a source); independently found Slickdeals front-page thread f/20314248 (2026-11-15, "Harman Kardon has Onyx Studio 8... on sale for $99.99", updated 2026-11-19 "still available").

## Tally (carried 7)

| # | Model | MPN | UPC | Price row |
|---|---|---|---|---|
| 2 | Hisense M7 75" (75M7SR) | PENDING + lead | PENDING, no lead | Best Buy $499.99 direct, BF ends 11-28 |
| 3 | Samsung U7900H 75" | VERIFIED | PENDING + lead (198957409578, 1 source) | Best Buy $399.99 direct, BF ends 11-28 |
| 4 | Samsung S84H 65" (QN65S84HAEXZA) | VERIFIED w/ caveat | PENDING, no lead | Best Buy $899.99 direct, BF ends 11-28 |
| 5 | TCL Q6CH | VERIFIED | PENDING, no lead | Costco warehouse $199.99 thru 11-30; online OOS |
| 6 | Samsung HW-B650F | VERIFIED | PENDING, conflicted | Best Buy $199.99 direct, BF ends 11-28 |
| 7 | Samsung Music Studio 5 (HW-LS50H/ZA) | VERIFIED | VERIFIED (198957266393) | Best Buy $299.99 direct, BF ends 11-28 |
| 8 | Harman Kardon Onyx Studio 8 Black | VERIFIED | PENDING, conflicted | harmankardon.com $99.99 direct, InStock |

**Dropped (1):** Hisense E6SR 50" — Amazon-only price evidence, no Best Buy/Walmart/hisense-usa.com row, MPN single non-qualifying source, UPC no lead.

## Open items for the coordinator / add time

- Q6CH: decide carry-vs-hold — the only live price is warehouse-only ($199.99 thru Nov 30); Costco.com is OOS at $299.99.
- S84H MPN caveat: second leg is Samsung Parts USA (parts listing); if a product-page second source is required, downgrade MPN to PENDING + strong lead.
- M7SR MPN: single qualifying source (Best Buy); re-check Hisense US site at add time — no hisense-usa.com M7SR page was found on 2026-11-21.
- UPC re-checks at add time: U7900H (198957409578, needs a second qualifying source), B650F (do not attach 887276936956 / 887276864211 — conflicting non-qualifying), Onyx Studio 8 (do not attach 028292289859 / 028292289873 / 657768329135 / 094148666167 — conflicting, one belongs to Blue), S84H / M7SR / Q6CH (no lead).
- All Best Buy Black Friday prices end Nov 28, 2026 — re-verify price + stock at add time; Costco/U7900H Holiday Savings ends Nov 30, 2026; Onyx Studio 8 promo has no stated end date.
- Category `tvs` is new (catalog has zero TVs in the 500) — confirm naming before writing.
