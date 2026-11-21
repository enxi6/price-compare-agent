# Track A — Shokz + Sonos (Batch 7 rework, 6 models)

- **Date:** 2026-11-21
- **Researcher:** Track A (Shokz 4 + Sonos 2)
- **Catalog state at check time:** 500 models (`/tmp/catalog_ref_500.tsv`, verified 211 / pending 289), repo `price_agent/catalog.py`.
- **Tally: MPN VERIFIED 5 / 6, UPC VERIFIED 5 / 6. Carried 5 verified + 1 pending, DROPPED 0.**
- **Method:** `browser.search` / `browser.open` in-session, 2026-11-21. No identifier, price, or SKU reconstructed from memory or a compacted summary. Every code below traces to a named page read in this session.

## Membership check

- Checked every candidate against `/tmp/catalog_ref_500.tsv` by exact key, model-name substring (normalized, both directions), MPN, and UPC, plus a second grep of `price_agent/catalog.py` for `shokz|sonos|openrun|openfit` (the `/tmp` file was wiped between exec calls, so the check was re-run against `catalog.py` directly).
- **Result: 0 collisions.** There is no Shokz or Sonos model anywhere in the 500-row catalog (0 grep hits in both sources). All six are new by membership.
- Sibling adjudications (no script hit, recorded so they are not re-litigated):
  - OpenRun (standard, S803) vs OpenRun Pro / OpenRun Pro 2 / OpenRun Mini: distinct models. Standard = S803-ST-GY-US, UPC 850033806229. Mini = S803-MN-BK-US, UPC 850033806236 — a different code, do not mix. Pro is a separate model line (S810 family).
  - OpenFit 2 SE vs OpenFit 2 (non-SE): distinct. SE is the Costco-exclusive trim (model code T920-ST-CB-US-326-COS). Do NOT attach the non-SE codes T920-ST-BK-US / UPC 810160666967 (B&H + RunUnited, both naming plain OpenFit 2 Black).
  - OpenRun Air 2 (S610) vs OpenRun Air (1st gen, S804?) / OpenRun Pro 2 (S820): distinct. Air 2 launched 2026-08-27, $129.95 list.
  - OpenDots Air (E210) vs OpenDots 2 (flagship, E211 family): distinct; OpenDots Air is the mid-range clip-on sibling launched alongside OpenDots 2 (2026-06).
  - Sonos Arc Ultra vs Sonos Arc (1st gen): distinct; Ultra = ARCG2US1BLK.
  - Sonos Era 100 vs Era 300: distinct; Era 100 = E10G1US1BLK.

## Candidates

### 1. Shokz OpenFit 2 SE — Black (Costco exclusive)
- **Key:** `shokz-openfit-2-se-black`
- **Category:** earbuds
- **Variant pinned:** Black, Costco-exclusive trim. Costco item 1926991, model code T920-ST-CB-US-326-COS. Underlying family is OpenFit 2 (T920); the `-CB-US-326-COS` suffix is a Costco-specific pack code.
- **Why it qualifies:** Mainstream current Shokz open-ear earbuds; Costco direct Black Friday row at $109.99 (list $149.99). Carried as PENDING only — identifiers do not verify (see below).
- **Identifiers:** MPN T920-ST-CB-US-326-COS — **PENDING (single-source, Costco only).** Costco product page lists it as the Model field (two crawls agree); no second source prints this code anywhere. UPC — **PENDING, no lead.** Three targeted searches (incl. `1926991` + barcode terms) found no UPC on any page. Do NOT attach OpenFit 2 (non-SE) UPC 810160666967 / MPN T920-ST-BK-US — those name the plain OpenFit 2 Black, a different model.
- **Price / stock:** Costco $109.99 after $40 manufacturer's savings (list $149.99), valid 11/16/26–11/30/26, members only, limit 5. **Stock signals conflict:** Costco.com JSON-LD read InStock in one crawl and OutOfStock in another (both crawled 2026-11-18/19, list price $149.99 shown); warehouse trackers (CostClubWeekly, WarehouseRunner) show in stock at $109.99 in multiple regions. Re-check stock live at add time; do not write the row from the snapshot if Costco.com still reads OutOfStock.
- **Flag:** Costco-exclusive variant code; UPC unfindable. Weakest entry in this track — pending on both identifiers. If the coordinator needs the slot for a verified model, this is the one to swap out.
- **Deal-site evidence:** Slickdeals Black Friday Sift, Costco $109.99 (reg $149.99), 17 saves, posted Oct 26, "Live Nov 15 until Nov 29" per Slickdeals; DealNews corroborates "$40 off through November 30, members only". Single-deal-site evidence (Slickdeals Sift only; DealNews is a second write-up of the same Costco offer, not an independent deal).

### 2. Shokz OpenRun Air 2 — Black
- **Key:** `shokz-openrun-air-2-black`
- **Category:** headphones
- **Variant pinned:** Black, Standard size, S610-ST-BK-US. (Mini is a separate size, S611-MN-BK-US, UPC 810202689299 — not this entry.)
- **Why it qualifies:** New mainstream Shokz bone-conduction model (launched 2026-08-27, $129.95 list); B&H + Best Buy direct Black Friday rows at ~$99.95, both InStock. Both identifiers VERIFIED (with the UPC caveat below).
- **Identifiers:** MPN S610-ST-BK-US — **VERIFIED** (B&H brand page MFR # + Best Buy Model field, SKU 6680820 + Petra distributor Vendor SKU + Home Depot Model # + Newegg Model #, all naming OpenRun Air 2 Black). UPC 810202689213 — **VERIFIED** (PBTech NZ retailer spec page + MobileCiti AU retailer spec page, both naming OpenRun Air 2 Black; eBay listing agrees; an Abt directory mirror lists 0810202689213 against S610-ST-BK-US).
- **Price / stock:** B&H $99.95 Holiday Savings (was $129.95), Add to Cart, In Stock; Best Buy $99.99 Black Friday (comp $129.99), sold by Best Buy, InStock (page opened 2026-11-21). Shokz direct $99.95 per the brief — corroborated at the same level by B&H/Best Buy; Shokz.com itself was not separately opened, so cite B&H/Best Buy as the rows.
- **Flag:** UPC caveat — both qualifying retailer sources are non-US (PBTech NZ, MobileCiti AU); no US retailer spec page printed the UPC in this session (Best Buy "See all specifications" panel was not expanded in the open). Recommend confirming 810202689213 on the Best Buy spec panel for SKU 6680820 at add time; downgrade to PENDING if it does not match. Newegg $116.84 (SHOKZ store) is higher — ignore, B&H/Best Buy are the rows.
- **Deal-site evidence:** Slickdeals Sift, Shokz direct $99.95 (reg $129.95), per brief. **Single-source evidence** — saves count not supplied in the brief and the Sift listing was not independently re-read; price level independently corroborated by B&H ($99.95) and Best Buy ($99.99).

### 3. Shokz OpenDots Air — Black
- **Key:** `shokz-opendots-air-black`
- **Category:** earbuds
- **Variant pinned:** Black, E210-ST-BK-US. Clip-on open-ear earbuds, 6.3 g per side, IP55, Bluetooth 6.1, 9 h + 36 h with case. (Daybreak Purple is the sibling: E210-ST-PR-US, UPC 810202687400 — not this entry.)
- **Why it qualifies:** Current mid-range Shokz clip-on (launched 2026-06 alongside OpenDots 2); Sam's Club + Best Buy direct rows at $89–$89.99. Both identifiers VERIFIED. Strongest Shokz pick in this track.
- **Identifiers:** MPN E210-ST-BK-US — **VERIFIED** (Best Buy Model field, SKU 6674289, sold by Best Buy + NFM Model field). UPC 810202687417 — **VERIFIED** (Target spec page, TCIN 95002590 + NFM spec page, SKU 70519376 + PBTech NZ spec page, all naming OpenDots Air Black).
- **Price / stock:** Sam's Club $89 (reg $129, $40 off, ends Nov 30, 2026) + $15 Sam's Cash; Best Buy $89.99 InStock, sold by Best Buy (page read 2026-11-21). Target lists $89.95 (JSON-LD).
- **Flag:** Sam's Club's $89 offer is color-agnostic in the sources (Sam's Club instant-savings page lists items 990543127 and 990543136 with no color mapping in the text; the in-store photo shows the $89 tag on the purple variant). Black is pinned via Target / NFM / Best Buy, not via Sam's Club — the $89 row is valid for the model but the color it was photographed against is purple. Re-check the Sam's Club item page at add time if the row must be color-tied. The $15 Sam's Cash is a membership rebate, not a price cut — do not net it against the $89.
- **Deal-site evidence:** Slickdeals, 2026-11-01, Sam's Club $89 (reg $129), 31% off; Sam's Club's own November instant-savings page corroborates ($40 off, ends Nov 30; event Oct 28–Nov 29). Also in the brief as Slickdeals Sift. Not single-source — Slickdeals + Sam's Club's own page.

### 4. Shokz OpenRun (standard) — Gray
- **Key:** `shokz-openrun-gray-standard`
- **Category:** headphones
- **Variant pinned:** Gray, Standard size, S803-ST-GY-US. Bone-conduction endurance headphones, 8 h battery, IP67, 26 g. Explicitly the standard (non-Pro, non-Mini) OpenRun.
- **Why it qualifies:** Long-running mainstream Shokz model; Shokz-direct 50%-off code row at $64.95 today (2026-11-21). Both identifiers VERIFIED. Distinct from OpenRun Pro (separate model) and OpenRun Mini (S803-MN-BK-US).
- **Identifiers:** MPN S803-ST-GY-US — **VERIFIED** (Best Buy Model field, SKU 6506589 + Abt Model # + RunUnited, all naming OpenRun Gray Standard). UPC 850033806229 — **VERIFIED** (Abt UPC # + RunUnited UPC, both on the S803-ST-GY-US page).
- **Price / stock:** Shokz.com $64.95 with code **SDopenrun** at checkout, free shipping (Slickdeals Tech, posted 2026-11-21 08:05; code valid for grey/standard only). Shokz.com list price today is $89.95 (struck $129.95) before the code. Earlier code OPENRUNGREY gave $64.98 on 2026-10-29 — same deal, new code.
- **Flag:** Code-required price — $64.95 is not the shelf price; the row must carry the code or it misleads. Best Buy row is DEAD ("This item is no longer available in new condition", SKU 6506589); Abt reads "no longer available" — Shokz direct is the only live row. Do NOT use the goWholesale refurb UPC 810092677024 for S803 gray — refurb wholesaler, non-qualifying, and it conflicts with the Abt/RunUnited UPC; disregarded. Do NOT attach Mini UPC 850033806236 (belongs to S803-MN-BK-US).
- **Deal-site evidence:** Slickdeals Tech (front-page/Today), 2026-11-21, $64.95 w/ code SDopenrun, thumb score +17; same deal posted 2026-10-29 at $64.98 w/ code OPENRUNGREY. Two Slickdeals postings of the same Shokz-direct offer — single deal site, two dates.

### 5. Sonos Era 100 — Black
- **Key:** `sonos-era-100-black`
- **Category:** speakers
- **Variant pinned:** Black, E10G1US1BLK, single unit. Wi-Fi/Bluetooth smart speaker, 2-way (1x mid-woofer, 2x tweeter), AirPlay 2, Alexa + Sonos Voice.
- **Why it qualifies:** Mainstream current Sonos smart speaker; B&H + Micro Center direct rows at $219.00 InStock. Both identifiers VERIFIED.
- **Identifiers:** MPN E10G1US1BLK — **VERIFIED** (Crutchfield MFR # + Micro Center Mfr Part # + B&H product page, all naming Era 100 Black). UPC 840136805830 — **VERIFIED** (B&H spec page + Micro Center spec page, both naming Era 100 Black; eBay GTIN 0840136805830 agrees). Amazon/camelcamelcamel print the same pair — disregarded as sources (Amazon is non-qualifying in any form); verification does not depend on them.
- **Price / stock:** B&H $219.00 InStock; Micro Center $219.00 (SKU 555730). Crutchfield lists $219.00 range as well (crawl showed $219.00).
- **Flag — READ FIRST: the Costco $329.99 in the brief is the 2-PACK, not the single unit.** Costco item 1731876, "Sonos Era 100 Speakers 2-Pack Black Edition", $329.99 after $80 off (list $409.99), Nov 19–30, 2026. Do NOT attach $329.99 as a single-unit price; per-unit would be $164.995, which is not a price any merchant sells a single unit at. The 2-pack is noted here only so the coordinator does not re-add it as a single-unit row. Costco.com same-day shows $342.99 for the 2-pack (delivery markup) — ignore.
- **Deal-site evidence:** Slickdeals Sift, Costco 2-pack $329.99 (reg $409.99), 37 saves, per brief. **The Sift evidence attaches to the 2-pack, not to the single-unit $219 rows** — the single-unit price has no deal-site evidence in this track. Flagged, not hidden.

### 6. Sonos Arc Ultra — Black
- **Key:** `sonos-arc-ultra-black`
- **Category:** soundbars
- **Variant pinned:** Black, ARCG2US1BLK, single soundbar. 9.1.4ch Dolby Atmos, Sound Motion, 14 drivers, HDMI eARC.
- **Why it qualifies:** Current Sonos flagship soundbar; Costco + Best Buy + NFM direct Black Friday rows at $849–$849.99, InStock. Both identifiers VERIFIED. **NOT a DROP:** the Costco "bundle" resolves cleanly to a single model (see below).
- **Identifiers:** MPN ARCG2US1BLK — **VERIFIED** (Best Buy Model field, SKU 6597167 + Micro Center Mfr Part # + Adorama MFR + NFM Model + WAVE Electronics distributor MPN, all naming Arc Ultra Black). UPC 840136811336 — **VERIFIED** (Micro Center UPC + NFM UPC + Adorama UPC table "Black Standard: 840136811336" + Walts UPC, all naming Arc Ultra Black). The eBay UPC 026531683277 is that listing's eBay-generated code, not the product UPC — disregarded. (My pre-search guess 840136808748 was wrong; the verified value is 840136811336.)
- **Price / stock:** Costco $849.99 after $250 off (list $1,099.99), manufacturer's savings valid 11/19/26–11/30/26, item 1912780, limit 5; Best Buy $849.00 Black Friday Deal, InStock, sold by Best Buy (BF ends Nov 28); NFM $849.00 on sale (comp $1,099.00).
- **Bundle resolution (the brief's DROP condition — resolved, not dropped):** Costco's "Sonos Arc Ultra 9.1.4 Ch Soundbar Bundle" (item 1912780) contains exactly ONE Arc Ultra soundbar plus a $60 Apple or SiriusXM gift card, a $79 wall-mount voucher, and a 30%-off Sonos accessories coupon (Costco product page "Bundle Includes" + holiday-savings circular). There is no Sub, no Era speaker, and no second soundbar in the box — "9.1.4ch" describes the soundbar's own channel config. The $849.99 therefore maps cleanly to the single Arc Ultra black model, with the gift card/voucher noted as bundle extras, not extra hardware. B&H's own kits (Arc Ultra + Sub 4 at $1,998; Arc Ultra + Sub 4 + 2x Era 300 at $2,366–$2,996) are separate B&H Kit SKUs and are NOT the Costco bundle — do not confuse them.
- **Flag:** Costco.com crawl showed OutOfStock on one read (JSON-LD $1,099.99) while the holiday-savings circular and warehouse photos (2026-11-19) show it live at $849.99 — re-check Costco stock at add time. The $849.99 is a Black Friday promo (ends Nov 30 at Costco, Nov 28 at Best Buy).
- **Deal-site evidence:** Slickdeals Sift, Costco $849.99 (reg $1,099.99), 15 saves, per brief; Costco's own holiday-savings circular corroborates ($849.99 after $250 off, item 1912780, Nov 19–30). Not single-source — Slickdeals + Costco circular.

## Summary table

| # | Model | Key suggestion | MPN | UPC | Price row | Verdict |
|---|---|---|---|---|---|---|
| 1 | Shokz OpenFit 2 SE, Black | `shokz-openfit-2-se-black` | T920-ST-CB-US-326-COS (PENDING, Costco-only) | PENDING, no lead | Costco $109.99 (11/16–11/30; stock conflicted) | PENDING — carry, weakest entry |
| 2 | Shokz OpenRun Air 2, Black | `shokz-openrun-air-2-black` | S610-ST-BK-US (VERIFIED) | 810202689213 (VERIFIED, non-US retailer sources — confirm on BB spec panel at add time) | B&H $99.95 / Best Buy $99.99 InStock (BF ends Nov 28) | VERIFIED |
| 3 | Shokz OpenDots Air, Black | `shokz-opendots-air-black` | E210-ST-BK-US (VERIFIED) | 810202687417 (VERIFIED) | Sam's Club $89 (ends Nov 30) / Best Buy $89.99 InStock | VERIFIED |
| 4 | Shokz OpenRun (std), Gray | `shokz-openrun-gray-standard` | S803-ST-GY-US (VERIFIED) | 850033806229 (VERIFIED) | Shokz direct $64.95 w/ code SDopenrun (2026-11-21) | VERIFIED |
| 5 | Sonos Era 100, Black | `sonos-era-100-black` | E10G1US1BLK (VERIFIED) | 840136805830 (VERIFIED) | B&H $219.00 / Micro Center $219.00 InStock | VERIFIED — Costco $329.99 is the 2-pack, NOT a single-unit row |
| 6 | Sonos Arc Ultra, Black | `sonos-arc-ultra-black` | ARCG2US1BLK (VERIFIED) | 840136811336 (VERIFIED) | Costco $849.99 (11/19–11/30) / Best Buy $849.00 InStock (BF ends Nov 28) | VERIFIED — Costco bundle = 1 soundbar + gift card/voucher, maps to single model |

## Open items for the coordinator / add time

- OpenFit 2 SE: UPC has no lead after three searches; MPN is a Costco-only code. If a verified-only bar is applied, drop entry 1 and do not backfill from another track without a fresh membership check.
- OpenRun Air 2 UPC: confirm 810202689213 on the Best Buy spec panel (SKU 6680820) at add time; downgrade to PENDING if it does not match.
- OpenFit 2 SE + Arc Ultra Costco stock: both showed conflicting InStock/OutOfStock crawls — re-check live before writing either row.
- Era 100: no single-unit deal-site evidence; the Sift evidence is 2-pack-only. If the batch requires a deal-site anchor per row, the B&H $219 row stands on its own as a retailer-direct row.
- No DROP in this track. No slot was hard-filled: the one pending entry is carried as pending, per the brief ("缺口不硬补" — entry 1 is flagged as the swap-out candidate, not padded with a substitute).
