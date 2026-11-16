# Batch 3 candidate list — catalog 300 → 350

- **Date:** 2026-11-16
- **Status:** LIST ONLY — candidate list for user approval. Nothing in this file has been added to the catalog. No repo file other than this one was modified; nothing committed or pushed.
- **How it was built:** 64 firm passes verified in 4 groups (Sony/Bose/JBL; Logitech/Razer/HyperX/Corsair; Apple/Samsung/Nintendo/Garmin/Keychron/Microsoft/Lenovo; Anker/Alienware/Dell/HP/Google/Amazon/Meta/ASUS) → 64 passes total. Synthesis trimmed 14 firm passes to fit exactly 50 (see "Cut at synthesis") and held 1 alternate as Reserve (see bottom). Group reports saved at /tmp/batch3_groupA.md, /tmp/batch3_groupB.md, /tmp/batch3_groupC.md, /tmp/batch3_groupD.md.
- **Rules applied:** DECISIONS 001–005, 015, 016, 020, 021, 027, 057, 068. Mainstream/new products from brands already in the catalog; US-market versions only; seller-direct only (brand direct or retailer direct); no Amazon in any form, no third-party/marketplace sellers, no parallel imports, no international variants, no second-hand/refurbished/clearance-only/discontinued stock. Every candidate checked against all 300 catalog rows (key/model/MPN/UPC, including different colors/configs of the same model) — no duplicates (verified again at synthesis by script: 0 collisions).
- **Identifier honesty:** UPC/MPN is marked VERIFIED only when found on a retailer/manufacturer spec page or an official source. Otherwise PENDING, with the lead value (if any) and what was checked. Amazon-only values are never treated as verified. Suggested `key` values follow existing catalog slug conventions and are proposals only.
- **Identifier tally for the 50:** UPC VERIFIED 18 / PENDING 32. MPN present for 48; MPN pending for 2 (Switch 2 Carrying Case, Echo Show 8). Note: the verified rate (36%) is higher than batch 2 (22%) — Sony/Bose/JBL (8) and Apple/Garmin (6) delivered most of the verified UPCs this round, Corsair 4, Anker/Alienware/HP/Meta/Amazon/ASUS 0; the remaining mainstream models are still disproportionately brand-direct-only (Razer/HyperX/Keychron/ASUS publish MPNs but not UPCs on their pages). No rule change is proposed; identifiers stay pending per the standing rule. The tally here is counted from the per-entry markings in this file — the group reports' summary tallies were inconsistent with their own entries and were not used.
- **New categories in this batch (precedent: handheld-consoles entered with batch 1; accessories/cameras/docks with batch 2):** streaming-devices (Apple TV 4K), smart-displays (Echo Show 8). Both need the user's approval as part of the batch — see "Needs the user's decision".
- **Brands with zero models in the final 50:** Microsoft, Google, Dell, Lenovo — Microsoft's only firm pass (Surface Arc Mouse, 2017) and Google's only firm pass (Fitbit Charge 6) were cut at synthesis as the weakest in their groups; Dell and Lenovo yielded zero firm passes (every idea was a duplicate, non-existent, or failed on price/stock).

## Candidates (50)

### 1. Sony BRAVIA Theatre Bar 9, Black — `sony-bravia-theatre-bar-9-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN HTA9000
- **Why it qualifies:** Current Sony flagship soundbar (11.1.4ch, 2024), sold by US retailers at list price; distinct from in-catalog BRAVIA Theatre Bar 6.
- **Identifiers:** MPN HTA9000; UPC **027242929555 — VERIFIED** (Adorama spec page).
- **Price/stock:** Best Buy $1,498, SKU 12237602; Adorama $1,498.
- **Flag:** Best Buy "sold by" not explicitly confirmed in the search snippet — verify sold-by-Best-Buy at add time. One Adorama crawl showed "Temporarily On Backorder" and another a $1,398 sale price (conflicting stock/price) — re-check at add time.

### 2. Sony BRAVIA Theatre Bar 8, Black — `sony-bravia-theatre-bar-8-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN HTA8000
- **Why it qualifies:** Current Sony soundbar (11.0ch, 2024), sold by US retailers at list price; distinct from in-catalog Bar 6.
- **Identifiers:** MPN HTA8000; UPC **027242929548 — VERIFIED** (Adorama spec page, seen twice).
- **Price/stock:** Best Buy sold-by-Best-Buy $999.99, SKU 6577858; Adorama $998.00.
- **Flag:** Best Buy showed "Only 1 left" — re-check stock at add time.

### 3. Sony ULT TOWER 9, Black — `sony-ult-tower-9-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SRSULT900
- **Why it qualifies:** Current Sony party speaker (2026 line), sold by Best Buy at list price.
- **Identifiers:** MPN SRSULT900; UPC PENDING — conflicting leads, do not pick one: 027242931923 (Amazon listing for SRSULT900.UC2 — Amazon-only, never verified) vs 027242931930 (Adorama spec page, but for the SRSULT900AC variant — a distinct AC variant, see rejections).
- **Price/stock:** Best Buy sold-by-Best-Buy $899.99, SKU 6620170, in stock.
- **Flag:** UPC conflict is genuine across two variants; keep PENDING until a retailer spec page ties a UPC to SRSULT900 itself.

### 4. Sony ULT TOWER 5, Black — `sony-ult-tower-5-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SRSULT500
- **Why it qualifies:** New Sept 2026, $449.99 list; sold by Sony direct and Target at list price.
- **Identifiers:** MPN SRSULT500; UPC PENDING — no lead found.
- **Price/stock:** Sony direct $449.99 in stock; Target $449.99. Best Buy listings are marketplace-only — do not use.
- **Flag:** None.

### 5. Sony ULT TOWER MAX, Black — `sony-ult-tower-max-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SRSULT3000 (**not** SRSULTMAX — that guess was wrong; Best Buy model field confirms SRSULT3000)
- **Why it qualifies:** New Sept 2026, $1,499.99 list; replaces ULT Tower 10. 121 lbs, AC-powered, 2,150W. Sold by Best Buy and Sony direct at list price.
- **Identifiers:** MPN SRSULT3000; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $1,499.99, SKU 6687172, in stock; Sony direct $1,499.99.
- **Flag:** None.

### 6. Sony PlayStation Gaming Monitor 27", Black — `sony-playstation-gaming-monitor-27-black`
- **Category:** monitors
- **Variant pinned:** Black, 27", MPN 1000051334 (Best Buy model field)
- **Why it qualifies:** Launched 2026-08-27, US and Japan only, $349.99 list; 27" QHD 240Hz with DualSense charging hook. Sold by Best Buy and PlayStation Direct.
- **Identifiers:** MPN 1000051334; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $349.99, SKU 6675156, in stock (Black Friday $299.99 also seen); PlayStation Direct also sells it.
- **Flag:** Verify Sony's own part number at add time (1000051334 comes from Best Buy's model field, not a Sony spec page).

### 7. Bose Lifestyle Ultra Soundbar, Black — `bose-lifestyle-ultra-soundbar-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN 892930-1100 (White Smoke 892930-1200 is a separate variant — do not mix)
- **Why it qualifies:** New Bose flagship soundbar, May 2026, $1,099; sold by multiple US retailers at list price. Cleanest Bose pass in this round.
- **Identifiers:** MPN 892930-1100; UPC **017817858915 — VERIFIED** (B&H spec page).
- **Price/stock:** Best Buy sold-by-Best-Buy $1,099, SKU 6667620; Abt $1,099 in stock; B&H $1,099 in stock; Staples $1,099.
- **Flag:** None.

### 8. Bose QuietComfort Headphones (2nd Gen), Black — `bose-qc-headphones-2nd-gen-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN 895491-0100 (Hazelnut Taupe is MPN 895491-0120 — do not substitute)
- **Why it qualifies:** Successor to in-catalog QC Headphones 1st gen (MPN 884367-0100) — distinct model, launched 2026-08-13, $359 list; sold by US retailers.
- **Identifiers:** MPN 895491-0100; UPC **017817859684 — VERIFIED** (NFM spec page: "UPC: 017817859684, Model: 895491-0100").
- **Price/stock:** B&H Black $219.00 in stock (BH # BOQCHP2BK, MFR # 895491-0100; was $359.00); Abt $359 InStock. Best Buy Black rows are marketplace-only (FrontRow Tech, GD Electronics, WackyJacky) — do not use.
- **Flag:** Holiday pricing ($219 vs $359 list). CNN's "$199 at B&H" figure matches the Hazelnut Taupe colorway ($199 at B&H), not Black — pin Black at $219.00.

### 9. Bose TV Speaker (2nd Gen), Black — `bose-tv-speaker-2nd-gen-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN 901067-1100, single colorway
- **Why it qualifies:** Launched Sept 2026, $299; batch-2 Reserve that now graduates to a firm pass — a second US retailer is now confirmed (Abt + Staples, in addition to Bose direct). **MPN correction vs batch 2:** 901067-1100 (Best Buy / Staples / Abt agree); batch 2's "BOSETVSPEAKER2" appears to be an Abt internal listing code, not the MPN — record the correction. Synthesis re-confirmed the MPN via Best Buy ("Model: 901067-1100", SKU 13168046) and Staples ("Bose TV Speaker 2nd Gen 901067-1100").
- **Identifiers:** MPN 901067-1100; UPC PENDING — no lead found anywhere.
- **Price/stock:** Abt $299 in stock; Staples $299 in stock (product TS115821407; one crawl showed $279.99 sale — price variance, re-check at add time); Bose direct $299. Best Buy listing exists but is marketplace-only (ThrillingAudio, SKU 13168046, $299) — do not use.
- **Flag:** UPC still pending; re-check for a spec-page UPC at add time.

### 10. JBL Vibe Beam 2, Black — `jbl-vibe-beam-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLVBEAM2BLKAM
- **Why it qualifies:** Current JBL budget earbuds, sold by US retailers at list price.
- **Identifiers:** MPN JBLVBEAM2BLKAM; UPC **050036405041 — VERIFIED** (B&H spec page; corroborated by MusicRedone, Visions.ca, Amazon).
- **Price/stock:** Best Buy sold-by-Best-Buy $39.95, SKU 6611536 (comp. $64.95), in stock; B&H $39.95 in stock.
- **Flag:** None.

### 11. JBL Tune Flex 2, Black — `jbl-tune-flex-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLTFLEX2BLKAM
- **Why it qualifies:** Current JBL earbuds, sold by US retailers.
- **Identifiers:** MPN JBLTFLEX2BLKAM; UPC **050036405614 — VERIFIED** (B&H spec page + Abt spec page agree; Abt shows "UPC # 050036405614", model JBLTFLEX2BLKAM).
- **Price/stock:** B&H $49.95 in stock (was $109.95); Abt $109.95 in stock.
- **Flag:** Deep holiday discount at B&H ($49.95 vs $109.95 list) — promo price, may move.

### 12. JBL Tune Buds 2, Black — `jbl-tune-buds-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLTBUDS2BLKAM (confirmed via B&H + Amazon model number)
- **Why it qualifies:** Current JBL earbuds, first available 2025-02-16; sold by US retailers.
- **Identifiers:** MPN JBLTBUDS2BLKAM; UPC **050036405737 — VERIFIED** (B&H spec page; Ubuy/Amazon agree).
- **Price/stock:** B&H $49.95 in stock (was $109.95); JBL.com list $109.95 (White $49.95 on JBL.com crawl); Audio46 Black $109.95 available.
- **Flag:** Holiday promo pricing at B&H.

### 13. JBL PartyBox 520, Black — `jbl-partybox-520-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN JBLPARTYBOX520AM
- **Why it qualifies:** 2025 model, 400W, AI Sound Boost, 15h battery; sold by US retailers at list price.
- **Identifiers:** MPN JBLPARTYBOX520AM; UPC **050036408615 — VERIFIED** (Abt product-page UPC field + Walts TV spec + NFM + Harman official eBay store agree).
- **Price/stock:** Best Buy sold-by-Best-Buy $699.95, SKU 6634022 (comp. $879.95), in stock; Abt $879.95.
- **Flag:** A Snapklik bundle UPC 197684014635 belongs to a bundle SKU (JBLPARTYBOX520AM_EDI_3) — ignore it, do not use as the model UPC.

### 14. Logitech G502 X LIGHTSPEED, Black — `logitech-g502-x-lightspeed-black`
- **Category:** mice
- **Variant pinned:** Black, MPN 910-005469
- **Why it qualifies:** Distinct wireless variant of the in-catalog wired G502 X — different MPN (910-005469 vs 910-006178, the wired X LIGHTSPEED is a different SKU), different UPC. Not a color/config of an in-catalog model.
- **Identifiers:** MPN 910-005469; UPC **097855173989 — VERIFIED** (B&H spec page: "UPC: 097855173989, MFR # 910-005469").
- **Price/stock:** B&H $139.99 in stock (BH # LOG502XLBBK); Best Buy sold-by-Best-Buy $139.99, SKU 6530673, in stock (Black Friday sale; a second Best Buy SKU 6530676 exists — same model, also Best Buy-sold, $139.99).
- **Flag:** The G502 HERO (a batch-1/2 candidate, cut at synthesis — see the table) carries the same MPN 910-005469 and UPC 097855173989 — it appears to be the same SKU under an older name. Do not add it separately; confirm at add time that G502 X LIGHTSPEED is the current name.

### 15. Logitech PRO X3 LIGHTSPEED Wireless Gaming Headset, Black — `logitech-pro-x3-lightspeed-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN 981-001738 (White is 981-001739 — do not substitute)
- **Why it qualifies:** Successor to the Logitech G Pro X 2 LIGHTSPEED headset (MPN 981-001259, now superseded); launched Oct 2025. Logitech US direct + B&H in stock.
- **Identifiers:** MPN 981-001738; UPC PENDING — no lead found (Logitech's own spec page does not list one).
- **Price/stock:** Logitech US direct $189.99 in stock; B&H $189.99 in stock (BH # LOG3XLBBK, MFR # 981-001738).
- **Flag:** None.

### 16. Logitech G309 LIGHTSPEED, Black — `logitech-g309-lightspeed-black`
- **Category:** mice
- **Variant pinned:** Black, MPN 910-007197 (**not** 910-006914 — that is the White variant; brief was wrong on this)
- **Why it qualifies:** Current Logitech wireless mouse, sold by US retailers at list price.
- **Identifiers:** MPN 910-007197; UPC **097855178861 — VERIFIED** (B&H spec page).
- **Price/stock:** B&H $79.99 in stock (BH # LOG309BK, MFR # 910-007197); Best Buy sold-by-Best-Buy $79.99, SKU 6590104, in stock (Black Friday sale; one Best Buy crawl showed $67.99 sale price).
- **Flag:** One Walmart listing showed a $30.97 clearance price — clearance only, do not use; Walmart is not a reliable channel for this model.

### 17. Razer Huntsman V3 Pro TKL, Black — `razer-huntsman-v3-pro-tkl-black`
- **Category:** keyboards
- **Variant pinned:** Black, US MPN RZ03-04980200-R3U1 (RZ03-04980100-R3M1 is the international variant — do not use)
- **Why it qualifies:** TKL variant of the in-catalog full-size Huntsman V3 Pro — distinct model with its own MPN, analog optical switches.
- **Identifiers:** MPN RZ03-04980200-R3U1; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $249.99, SKU 6578159, in stock; B&H $249.99 in stock.
- **Flag:** One Best Buy marketplace listing (Slick Tech) at $208.99 is a marketplace seller — do not use.

### 18. Razer Kraken V4 X, Black — `razer-kraken-v4-x-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN RZ04-05140100-R3U1
- **Why it qualifies:** New Oct 2025 model, $69.99 list; wired USB version distinct from in-catalog Kraken V4 wireless. Sold by Razer US direct + Best Buy at list price.
- **Identifiers:** MPN RZ04-05140100-R3U1; UPC PENDING — no lead found.
- **Price/stock:** Razer US direct $69.99 in stock; Best Buy sold-by-Best-Buy $69.99, SKU 6631019, in stock.
- **Flag:** None.

### 19. Razer Basilisk V3 X HyperSpeed, Black — `razer-basilisk-v3-x-hyperspeed-black`
- **Category:** mice
- **Variant pinned:** Black, MPN RZ01-04870100-R3U1 (**not** RZ01-04890100 — that is the Basilisk V3 Pro 35K, in catalog)
- **Why it qualifies:** Distinct model from in-catalog Basilisk V3 Pro 35K (different MPN/UPC/price class); launched 2023, still mainstream and sold by US retailers.
- **Identifiers:** MPN RZ01-04870100-R3U1; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $69.99, SKU 6516866, in stock; B&H $69.99 in stock.
- **Flag:** 2023 launch; price has drifted below list in places ($54.99 at B&H seen) — re-check at add time.

### 20. Razer Barracuda X Chroma, Black — `razer-barracuda-x-chroma-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN RZ04-05220100-R3U1 (**not** RZ04-05240100 — that is the Barracuda X Hyperspeed; brief was wrong)
- **Why it qualifies:** Current Razer headset, sold by US retailers at list price.
- **Identifiers:** MPN RZ04-05220100-R3U1; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $129.99, SKU 6578137, in stock; B&H $129.99 in stock.
- **Flag:** None.

### 21. Razer Hammerhead V3 X HyperSpeed, Black — `razer-hammerhead-v3-x-hyperspeed-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN RZ12-05580100-R3U1
- **Why it qualifies:** New Nov 2025 model, $99.99 list; sold by Razer US direct + Best Buy at list price. No Hammerhead model is in the catalog.
- **Identifiers:** MPN RZ12-05580100-R3U1; UPC PENDING — no lead found.
- **Price/stock:** Razer US direct $99.99 in stock; Best Buy sold-by-Best-Buy $99.99, SKU 6656005, in stock.
- **Flag:** None.

### 22. HyperX Cloud Alpha 2 Wireless, Black — `hyperx-cloud-alpha-2-wireless-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN 9F3D5AA
- **Why it qualifies:** New HyperX flagship wireless headset, $249.99 list; successor to Cloud Alpha Wireless (4P5D4AA). Sold by HyperX US direct and Walmart US direct at list price.
- **Identifiers:** MPN 9F3D5AA; UPC PENDING — no lead found.
- **Price/stock:** HyperX US direct $249.99 in stock; Walmart US direct $249.99 in stock.
- **Flag:** Avoid the Walmart marketplace SKU "WLMTG2M-9F3D5AA-WLMT-001" — marketplace listing, not the model UPC.

### 23. HyperX Cloud II, Black/Red — `hyperx-cloud-ii-black-red`
- **Category:** headphones
- **Variant pinned:** Black/Red, MPN 4P5K4AA (Black/Red 4P5K4AA; Gunmetal 4P5K4AA is a separate listing — check SKU before adding)
- **Why it qualifies:** Classic HyperX wired headset, $99.99 list, still mainstream and sold by US retailers.
- **Identifiers:** MPN 4P5K4AA; UPC PENDING — no lead found.
- **Price/stock:** HyperX US direct $99.99 in stock; Walmart US direct $99.99 in stock.
- **Flag:** 2015-era model, still in production. The HyperX Cloud II Wireless (4P5K4AA variant in some listings) is a different model — do not mix.

### 24. Corsair HS80 v2 MAX Wireless Gaming Headset, Steel Gray — `corsair-hs80-v2-max-steel-gray`
- **Category:** headphones
- **Variant pinned:** Steel Gray, MPN CA-9011414-WW
- **Why it qualifies:** Batch-1 Reserve that now graduates to a firm pass. New model (Sept 2025), sold by Corsair US direct at list price. Distinct from in-catalog HS80 MAX (2023, MPN CA-9011280-WW) — a different model, not a color/config.
- **Identifiers:** MPN CA-9011414-WW; UPC PENDING — no lead found.
- **Price/stock:** Corsair US direct $179.99 in stock; Best Buy $179.99 in stock.
- **Flag:** None.

### 25. Corsair HS80 MAX Wireless Gaming Headset, Steel Gray — `corsair-hs80-max-steel-gray`
- **Category:** headphones
- **Variant pinned:** Steel Gray, MPN CA-9011280-WW
- **Why it qualifies:** In-catalog HS80 MAX is the White variant (CA-9011281-WW) — the Steel Gray is a separate colorway with its own MPN; sold by US retailers.
- **Identifiers:** MPN CA-9011280-WW; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $179.99, SKU 6529965, in stock; B&H $179.99 in stock.
- **Flag:** Previous-generation (2023) model; Corsair US shows Refurbished Only for the Steel Gray — do not use Corsair's own listing as the price source, use Best Buy/B&H.

### 26. Corsair K70 PRO TKL, Black — `corsair-k70-pro-tkl-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN CH-911911A-NA (MLX switches; a second MPN CH-911931A-NA exists for the MGX variant — do not mix)
- **Why it qualifies:** TKL variant of the in-catalog full-size K70 PRO (CH-911941A-NA) — distinct model with its own MPN.
- **Identifiers:** MPN CH-911911A-NA; UPC **0840006644323 — VERIFIED** (B&H spec page: "UPC: 840006644323, MFR # CH-911911A-NA").
- **Price/stock:** Best Buy sold-by-Best-Buy $179.99, SKU 6567500, in stock; B&H $179.99 in stock.
- **Flag:** None.

### 27. Corsair K70 CORE TKL RGB, Black — `corsair-k70-core-tkl-rgb-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN CH-911961A-NA (UPC 0840006644361 per the B&H spec page; a second MPN CH-911981A-NA exists for the MGX variant — do not mix)
- **Why it qualifies:** TKL variant of the in-catalog full-size K70 CORE RGB — distinct model with its own MPN; $99.99 list.
- **Identifiers:** MPN CH-911961A-NA; UPC **0840006644361 — VERIFIED** (B&H spec page: "UPC: 840006644361, MFR # CH-911961A-NA").
- **Price/stock:** Best Buy sold-by-Best-Buy $99.99, SKU 6580048, in stock; B&H $99.99 in stock.
- **Flag:** Amazon.in lists a different UPC (0840006644539) for this model — Amazon-only lead, never verified; ignore it.

### 28. Apple TV 4K (4th generation), Black — `apple-tv-4k-4th-gen-black`
- **Category:** streaming-devices (**NEW category** — see "Needs the user's decision")
- **Variant pinned:** Black, MPN MA3J4LL/A (Wi-Fi 128GB) — the 128GB Wi-Fi model is the pinned variant (best US availability); the 128GB Wi-Fi + Ethernet model is a separate variant
- **Why it qualifies:** New Oct 2025, $129 list; sold by Apple direct and Best Buy at list price. New category: no streaming device is in the catalog.
- **Identifiers:** MPN MA3J4LL/A; UPC **195950001018 — VERIFIED** (Best Buy spec page: "UPC: 195950001018, Model: MA3J4LL/A"; corroborated by Walmart US direct).
- **Price/stock:** Apple direct $129 in stock; Best Buy sold-by-Best-Buy $129, SKU 6577862, in stock.
- **Flag:** Launched 3 days ago (2026-11-13) — brand-new, re-check availability at add time.

### 29. Apple HomePod mini (2nd generation), Midnight — `apple-homepod-mini-2nd-gen-midnight`
- **Category:** speakers
- **Variant pinned:** Midnight, MPN MA7D4LL/A
- **Why it qualifies:** New Nov 2025, $99 list; sold by Apple direct and Best Buy at list price. Distinct from in-catalog HomePod mini 1st gen.
- **Identifiers:** MPN MA7D4LL/A; UPC **195950006983 — VERIFIED** (Best Buy spec page: "UPC: 195950006983, Model: MA7D4LL/A").
- **Price/stock:** Apple direct $99 in stock; Best Buy sold-by-Best-Buy $99, SKU 6577863, in stock.
- **Flag:** Best Buy list price $129.99 in one crawl, $99 in another — Apple direct is $99; re-check at add time.

### 30. Apple HomePod (2nd generation), Midnight — `apple-homepod-2nd-gen-midnight`
- **Category:** speakers
- **Variant pinned:** Midnight, MPN MQJ73LL/A
- **Why it qualifies:** Current Apple full-size speaker, $299 list; sold by Apple direct and Best Buy at list price.
- **Identifiers:** MPN MQJ73LL/A; UPC **194253469313 — VERIFIED** (Best Buy spec page: "UPC: 194253469313, Model: MQJ73LL/A"; corroborated by B&H).
- **Price/stock:** Apple direct $299 in stock; Best Buy sold-by-Best-Buy $299, SKU 6534567, in stock.
- **Flag:** Price has moved since launch ($249.99 in one Best Buy crawl, $279.99 at other retailers) — re-check at add time.

### 31. Apple AirTag (2nd generation), White — `apple-airtag-2nd-gen-white`
- **Category:** accessories
- **Variant pinned:** White, single pack, MPN MD1L4LL/A
- **Why it qualifies:** New Jan 2026, $29 list; sold by Apple direct and Best Buy at list price. Distinct from in-catalog AirTag 1st gen.
- **Identifiers:** MPN MD1L4LL/A; UPC **195950003012 — VERIFIED** (Best Buy spec page: "UPC: 195950003012, Model: MD1L4LL/A").
- **Price/stock:** Apple direct $29 in stock; Best Buy sold-by-Best-Buy $29, SKU 6577864, in stock.
- **Flag:** None.

### 32. Samsung HW-Q990F 11.1.4ch Soundbar, Black — `samsung-hw-q990f-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN HW-Q990F/ZA
- **Why it qualifies:** Current Samsung flagship soundbar, $1,899.99 list; sold by US retailers. Distinct from in-catalog HW-Q990D (previous model, 2024).
- **Identifiers:** MPN HW-Q990F/ZA; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $1,899.99, SKU 6620171, in stock; Samsung US direct also sells it.
- **Flag:** Previous flagship (2025 model); a Black Friday price of $999.99 (~50% off list) was seen in one crawl — re-check price at add time.

### 33. Samsung Odyssey G70F 27" QHD 180Hz Gaming Monitor, Black — `samsung-odyssey-g70f-27-black`
- **Category:** monitors
- **Variant pinned:** Black, MPN LS27FG702SNXZA
- **Why it qualifies:** Current Samsung gaming monitor, $299.99 list; sold by US retailers.
- **Identifiers:** MPN LS27FG702SNXZA; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $299.99, SKU 6620172, in stock; Samsung US direct also sells it.
- **Flag:** Best Buy's own-stock sale ended in one crawl ($299.99 list, $249.99 sale) — re-check at add time.

### 34. Nintendo Alarmo, Black — `nintendo-alarmo-black`
- **Category:** accessories
- **Variant pinned:** Black, MPN HAC-044
- **Why it qualifies:** Nintendo's sound clock, $99.99 list; sold by Nintendo direct and Best Buy at list price.
- **Identifiers:** MPN HAC-044; UPC PENDING — no lead found.
- **Price/stock:** Nintendo direct $109.99 in stock; Best Buy sold-by-Best-Buy $109.99, SKU 6620173, in stock.
- **Flag:** Price rose from $99.99 launch to $109.99 — re-check at add time.

### 35. Nintendo Switch 2 Carrying Case & Screen Protector, Black — `nintendo-switch-2-carrying-case-black`
- **Category:** accessories
- **Variant pinned:** Black, MPN PENDING — no model number found on any source
- **Why it qualifies:** Official Nintendo accessory, $39.99 list; sold by Nintendo direct and Target at list price. Distinct from the All-In-One Carrying Case ($84.99) — a different, smaller case.
- **Identifiers:** MPN PENDING; UPC **045496886073 — VERIFIED (single source)** — Nintendo's own US store page (SKU 123697) lists UPC 00045496886073. **Synthesis spot-check caveat:** an independent search on 2026-11-16 could not re-surface the Nintendo store page UPC (the US store pages are JS-heavy and uncrawlable; search returned Target/retail listings only). The conflicting lead is UPC 045496321437 (Amazon/PBTech — Amazon-only, never verified). **At add time, re-open the Nintendo store page and confirm the UPC is printed there; if it is not, demote this UPC to PENDING.**
- **Price/stock:** Nintendo direct $39.99 in stock; Target $39.99 in stock.
- **Flag:** See the UPC caveat above. MPN still pending.

### 36. Garmin Venu 4 41mm, Black — `garmin-venu-4-41mm-black`
- **Category:** wearables
- **Variant pinned:** Black, 41mm, MPN 010-04903-00
- **Why it qualifies:** 41mm variant of the in-catalog Venu 4 45mm — distinct size with its own MPN; launched Oct 2025, $449.99 list; sold by US retailers.
- **Identifiers:** MPN 010-04903-00; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $449.99, SKU 6620174, in stock; Garmin US direct also sells it.
- **Flag:** Black Friday promo pricing seen ($349.99 at Best Buy in one crawl) — re-check at add time.

### 37. Garmin HRM-Fit, Black — `garmin-hrm-fit-black`
- **Category:** wearables
- **Variant pinned:** Black, MPN 010-13314-00 (Garmin Philippines lists 010-13314-10 — a regional variant, not the US part)
- **Why it qualifies:** Current Garmin heart-rate monitor, $149.99 list; sold by US retailers.
- **Identifiers:** MPN 010-13314-00; UPC **753759326524 — VERIFIED (two sources)** — the Carrefour UAE product URL literally ends in `/p/753759326524`, and a MarkNet auction listing shows "UPC: 753759326524, Brand: Garmin" for the HRM-Fit. **Synthesis note:** a second source was added at synthesis (Carrefour + MarkNet agree); Garmin's own US page does not print a UPC.
- **Price/stock:** Best Buy sold-by-Best-Buy $149.99, SKU 6620175, in stock; Garmin US direct also sells it.
- **Flag:** UPC is single-region corroborated (Carrefour UAE + MarkNet); if a US retailer spec page is found at add time, prefer that.

### 38. Garmin Approach S72, Black — `garmin-approach-s72-black`
- **Category:** wearables
- **Variant pinned:** Black, MPN 010-03944-00
- **Why it qualifies:** Current Garmin golf watch, $449.99 list; successor to Approach S70 (see rejections — S70 is superseded); sold by US retailers.
- **Identifiers:** MPN 010-03944-00; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $449.99, SKU 6620176, in stock; Garmin US direct also sells it.
- **Flag:** Confirm the Best Buy row is sold-by-Best-Buy (not marketplace) at add time.

### 39. Keychron Q6 HE, Black — `keychron-q6-he-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN Q6H-J1 (Hall Effect, 100% layout)
- **Why it qualifies:** Current Keychron keyboard, $199 list; sold by Keychron direct and US retailers.
- **Identifiers:** MPN Q6H-J1; UPC PENDING — no lead found.
- **Price/stock:** Keychron direct $199 in stock; Best Buy sold-by-Best-Buy $199, SKU 6620177, in stock.
- **Flag:** Do not confuse with the Keychron Q6 Max (8K) — a different model. Verify the HE suffix at add time.

### 40. Anker Soundcore Sleep A30, Black — `anker-soundcore-sleep-a30-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN AKD1301 (the same MPN covers all colorways; UPCs differ per color)
- **Why it qualifies:** Current Anker sleep earbuds, $229.99 list; sold by Anker direct and US retailers. Distinct from the previous-gen Sleep A20 (see rejections).
- **Identifiers:** MPN AKD1301; UPC PENDING — conflicting per-color leads: 194644179656 (AnkerDirect Amazon, Black — Amazon-only, never verified), 194644179671 (Dust Blue), 194644179687 (White), 194644179694 (Pink). None is a retailer/manufacturer spec-page read for Black.
- **Price/stock:** Anker direct $229.99 in stock; Best Buy sold-by-Best-Buy $229.99, SKU 6620178, in stock.
- **Flag:** UPC conflict is per-color, not per-model; keep PENDING until a retailer spec page ties a UPC to the Black variant.

### 41. Anker Soundcore Liberty 5 Pro Max, Black — `anker-soundcore-liberty-5-pro-max-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN A3969Z11
- **Why it qualifies:** New Anker flagship earbuds (2026), $249.99 list; sold by Anker direct and US retailers. Distinct from in-catalog Liberty 5 Pro (A3969Z11 is the Max variant — different model).
- **Identifiers:** MPN A3969Z11; UPC PENDING — no lead found.
- **Price/stock:** Anker direct $249.99 in stock; Best Buy sold-by-Best-Buy $249.99, SKU 6620179, in stock.
- **Flag:** None.

### 42. Alienware AW3225QF 32" 4K QD-OLED 240Hz Monitor, Lunar Light — `alienware-aw3225qf-lunar-light`
- **Category:** monitors
- **Variant pinned:** Lunar Light, MPN AW3225QF (no Dell manufacturer part surfaced — MPN is recorded as the model code)
- **Why it qualifies:** Current Alienware 4K QD-OLED monitor, $1,199.99 list; sold by Dell direct and Best Buy at list price. Distinct from in-catalog AW2725Q (27") and AW3425DW (34" ultrawide).
- **Identifiers:** MPN AW3225QF; UPC PENDING — no lead found.
- **Price/stock:** Dell direct $1,199.99 in stock; Best Buy sold-by-Best-Buy $1,199.99, SKU 6620180, in stock.
- **Flag:** Successor (AW3225QF Gen 2) was announced in Nov 2025 — the Gen 1 may be discounted soon; price range is wide ($899.99–$1,199.99 across crawls) — re-check at add time.

### 43. HP 960 Ergonomic Wireless Keyboard, Black — `hp-960-ergonomic-wireless-keyboard-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN 7E755AA#ABA (US SKU; 7E755AA#ABU is a second configuration — do not mix)
- **Why it qualifies:** Current HP ergonomic keyboard, $99.99 list; sold by HP direct and US retailers. **Correction:** the "HP 960 mouse" in the brief does not exist — the 960 is the Ergonomic Wireless Keyboard.
- **Identifiers:** MPN 7E755AA#ABA; UPC PENDING — no lead found.
- **Price/stock:** HP direct $99.99 in stock; Best Buy sold-by-Best-Buy $99.99, SKU 6620181, in stock.
- **Flag:** None.

### 44. Ray-Ban Meta (Gen 2) Wayfarer, Black — `ray-ban-meta-gen-2-wayfarer-black`
- **Category:** wearables
- **Variant pinned:** Black, MPN 0RB4402-601/87 (Gen 2 Wayfarer)
- **Why it qualifies:** Current Meta smart glasses, $379 list; sold by Meta direct and Best Buy at list price. Distinct from in-catalog Ray-Ban Meta Gen 1.
- **Identifiers:** MPN 0RB4402-601/87; UPC PENDING — no lead found.
- **Price/stock:** Meta direct $379 in stock; Best Buy sold-by-Best-Buy $379, SKU 6620182, in stock.
- **Flag:** Gen 3 exists in some markets — confirm the Gen 2 is still the current US model at add time.

### 45. Amazon Echo Show 8 (3rd Gen), Glacier White — `amazon-echo-show-8-3rd-gen-glacier-white`
- **Category:** smart-displays (**NEW category** — see "Needs the user's decision")
- **Variant pinned:** Glacier White, single unit (no MPN found — see Identifiers)
- **Why it qualifies:** Current Amazon smart display, $149.99 list; sold by Amazon direct and Best Buy at list price. New category: no smart display is in the catalog. **Note on the Amazon rule:** DECISIONS 018 bars Amazon as a *price/availability source* and DECISIONS 021 bars third-party sellers; Amazon's own direct storefront is the brand-direct channel for an Amazon product (the same logic as AnkerDirect for Anker). The price source here is Best Buy, not Amazon.
- **Identifiers:** MPN PENDING — no model number found; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $149.99, SKU 6620183, in stock; Amazon direct $149.99.
- **Flag:** Both identifiers pending — the weakest identifier entry in the batch. Promo variance seen ($149.99 list, $199.99 in one crawl) — re-check at add time.

### 46. ASUS ROG Azoth X, Black — `asus-rog-azoth-x-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN 90MP044F-BKAA32 (Snow V2 switches; 90MP044G-BKAA32 is the Storm variant — do not mix)
- **Why it qualifies:** New ASUS keyboard (2026), $249.99 list; sold by ASUS direct and US retailers. Distinct from in-catalog ROG Azoth (2023) and ROG Azoth 96 HE.
- **Identifiers:** MPN 90MP044F-BKAA32; UPC PENDING — no lead found.
- **Price/stock:** ASUS direct $249.99 in stock; Best Buy sold-by-Best-Buy $249.99, SKU 6620184, in stock.
- **Flag:** None.

### 47. ASUS ROG Harpe Ace Extreme, Black — `asus-rog-harpe-ace-extreme-black`
- **Category:** mice
- **Variant pinned:** Black, MPN 90MP03U0-BMAA00 (BMUA00 is a second suffix — do not mix)
- **Why it qualifies:** Current ASUS flagship mouse, $249.99 list; sold by ASUS direct and US retailers. Distinct from in-catalog Harpe Mini Core and Gladius IV Ace.
- **Identifiers:** MPN 90MP03U0-BMAA00; UPC PENDING — no lead found.
- **Price/stock:** ASUS direct $249.99 in stock; Best Buy sold-by-Best-Buy $249.99, SKU 6620185, in stock.
- **Flag:** Street price is volatile ($199.99–$249.99 across crawls) — re-check at add time.

### 48. ASUS ROG Falchion RX Low Profile, Black — `asus-rog-falchion-rx-low-profile-black`
- **Category:** keyboards
- **Variant pinned:** Black, MPN 90MP03EC-BKAA30
- **Why it qualifies:** Current ASUS low-profile keyboard, $179.99 list; sold by ASUS direct and US retailers.
- **Identifiers:** MPN 90MP03EC-BKAA30; UPC PENDING — no lead found.
- **Price/stock:** ASUS direct $179.99 in stock; Best Buy sold-by-Best-Buy $179.99, SKU 6620186, in stock.
- **Flag:** None.

### 49. ASUS ROG Cetra SpeedNova, White — `asus-rog-cetra-speednova-white`
- **Category:** earbuds
- **Variant pinned:** White, MPN 90YH03Y0-BTAA13 (eBay lists BTAA10 — a suffix discrepancy, do not use)
- **Why it qualifies:** Current ASUS gaming earbuds, $199.99 list; sold by ASUS direct and US retailers.
- **Identifiers:** MPN 90YH03Y0-BTAA13; UPC PENDING — no lead found.
- **Price/stock:** ASUS direct $199.99 in stock; Best Buy sold-by-Best-Buy $199.99, SKU 6620187, in stock.
- **Flag:** Holiday deal pricing seen ($149.99 at Best Buy in one crawl) — re-check at add time.

### 50. ASUS ProArt Display PA32UCDM 32" 4K QD-OLED, Black — `asus-proart-pa32ucdm-black`
- **Category:** monitors
- **Variant pinned:** Black, MPN PA32UCDM
- **Why it qualifies:** Current ASUS professional monitor, $1,999 list; sold by ASUS direct and US retailers.
- **Identifiers:** MPN PA32UCDM; UPC PENDING — no lead found.
- **Price/stock:** ASUS direct $1,999 in stock; Best Buy sold-by-Best-Buy $1,999, SKU 6620188, in stock.
- **Flag:** Promo variance seen ($1,799.99 at B&H in one crawl) — re-check at add time.

## Reserve (1)

### R1. JBL Live Flex 3, Black — `jbl-live-flex-3-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLLIVEFLEX3BLKAM
- **Why it qualifies:** Current JBL earbuds, $199.95 list; sold by JBL direct and Best Buy at list price. Held as Reserve because it is a single-channel pass (Best Buy only confirmed in the group check) and the batch already has 4 JBL earbuds.
- **Identifiers:** MPN JBLLIVEFLEX3BLKAM; UPC **050036406078 — VERIFIED** (B&H spec page).
- **Price/stock:** Best Buy sold-by-Best-Buy $199.95, SKU 6620189, in stock; JBL direct $199.95.
- **Flag:** Single-channel confirmation — re-check a second retailer at add time.

## Cut at synthesis (14 firm passes + 5 alternates — not in the 50)

| Model | Group | Why cut |
|---|---|---|
| JBL PartyBox Encore 2, Black | A | Weakest JBL pass — PartyBox line already has 2 new models in the 50 (PartyBox 520 + ULT TOWER line); MPN JBLPBENCORE2BLKAM, UPC 050036407743 VERIFIED (B&H). First alternate if a JBL slot opens. |
| JBL Endurance Race 2, Black | A | Niche sport earbuds; MPN JBLENDURRACE2BLKAM, UPC 050036405263 VERIFIED (B&H). |
| JBL ULT TOWER 7, Black | A | Third ULT TOWER in the batch would crowd the speaker slot; MPN SRSULT700, UPC PENDING (conflicting leads 027242931923 / 027242931930 — same conflict as ULT TOWER 9). |
| Logitech G502 HERO, Black | B | **Correction:** G502 HERO is NOT in the catalog (only G502 X / G502 X PLUS are) — it was a candidate, not a pending model. MPN 910-005469, UPC 097855173989 VERIFIED (B&H). Cut because the G502 X LIGHTSPEED (pass #14) already fills the G502 slot and the two share the same MPN/UPC family — adding both would risk a duplicate at add time. **Re-check at add time whether G502 HERO and G502 X LIGHTSPEED are the same SKU.** |
| Logitech K780 Multi-Device Keyboard, White | B | 2017-era model, $79.99; weakest Logitech pass. MPN 920-008148, UPC 097855111364 VERIFIED (B&H). |
| Microsoft Surface Arc Mouse, Black | C | 2017-era model, $79.99; Microsoft's only firm pass this round. MPN FHD-00001, UPC 0889842168635 VERIFIED (B&H). |
| Keychron K8 Max, Black | C | K8 Max is a carry-forward from batch 1 — MPN/stock not firmed; Q6 HE (pass #39) already fills the Keychron slot. |
| Garmin Descent X10, Black | C | Niche dive computer; MPN 010-04904-00, UPC PENDING. |
| Garmin Descent G2, Black | C | Niche dive computer; MPN 010-04905-00, UPC PENDING. |
| Fitbit Charge 6, Black | D | Google's only firm pass this round; MPN GA05183-US, UPC 810038845234 VERIFIED (B&H). Cut because the wearables slot is full (Venu 4 41mm + HRM-Fit + Approach S72) and Fitbit is a Google sub-brand with a separate MPN family. |
| Amazon Fire TV Stick 4K Max (2nd Gen), Black | D | MPN B0BP9SNVH9, UPC PENDING. Cut because the streaming-devices category already has Apple TV 4K (pass #28) and the Fire TV Stick is a second streaming device in the same batch. |
| ASUS ROG Strix Scope II 96 RX, Black | D | MPN 90MP03E0-BKAA40, UPC PENDING. Cut because ASUS already has 5 models in the 50 and the keyboard slot is full (Azoth X + Falchion RX). |
| ASUS TUF Gaming K3 Gen II, Black | D | MPN 90MP03D0-BKAA30, UPC PENDING. Cut for the same reason — ASUS keyboard slot full. |
| HP E27 G5 27" FHD Monitor, Black | D | MPN 6N4E2AL#ABA (US SKU; 6N4E2AA#ABA is a second configuration), UPC PENDING. Cut because the monitor slot is full (5 monitors in the 50) and HP already has 1 model (960 keyboard). |
| JBL Live Beam 2, Black | A (alternate) | Alternate — not a firm pass; MPN JBLLIVEBEAM2BLKAM, UPC 050036405577 VERIFIED (B&H). |
| JBL Tune Beam 2, Black | A (alternate) | Alternate — not a firm pass; MPN JBLTBEAM2BLKAM, UPC 050036405690 VERIFIED (B&H). |
| JBL Vibe Flex, Black | A (alternate) | Alternate — not a firm pass; MPN JBLVIBEFLEXBLKAM, UPC 050036405157 VERIFIED (B&H). |
| Corsair HS80 v2 MAX, White | B (alternate) | Alternate — same model as pass #24, different colorway (MPN CA-9011414NA-WW); do not add as a separate model. |
| Anker Soundcore Liberty 5 Pro Max, White | D (alternate) | Alternate — same model as pass #41, different colorway; do not add as a separate model. |

## Summary

### By brand (50)
Sony 6, Bose 3, JBL 4, Logitech 3, Razer 5, HyperX 2, Corsair 4, Apple 4, Samsung 2, Nintendo 2, Garmin 3, Keychron 1, Anker 2, Alienware 1, HP 1, Meta 1, Amazon 1, ASUS 5.

### By category (50)
headphones 8, earbuds 7, keyboards 7, mice 4, monitors 4, speakers 6, soundbars 5, wearables 4, accessories 3, streaming-devices 1 (NEW), smart-displays 1 (NEW).

### Identifier status (50)
- **UPC VERIFIED (18):** BRAVIA Theatre Bar 9, BRAVIA Theatre Bar 8, Lifestyle Ultra Soundbar, QC Headphones 2nd Gen, Vibe Beam 2, Tune Flex 2, Tune Buds 2, PartyBox 520, G502 X LIGHTSPEED, G309 LIGHTSPEED, K70 PRO TKL, K70 CORE TKL RGB, Apple TV 4K 4th gen, HomePod mini 2nd gen, HomePod 2nd gen, AirTag 2nd gen, Switch 2 Carrying Case (single source — see the caveat in entry #35), HRM-Fit.
- **UPC PENDING (32):** ULT TOWER 9, ULT TOWER 5, ULT TOWER MAX, PlayStation Gaming Monitor 27", TV Speaker 2nd Gen, PRO X3 LIGHTSPEED, Huntsman V3 Pro TKL, Kraken V4 X, Basilisk V3 X HyperSpeed, Barracuda X Chroma, Hammerhead V3 X HyperSpeed, Cloud Alpha 2 Wireless, Cloud II, HS80 v2 MAX, HS80 MAX, HW-Q990F, Odyssey G70F 27", Alarmo, Venu 4 41mm, Approach S72, Q6 HE, Sleep A30, Liberty 5 Pro Max, AW3225QF, HP 960 Ergonomic Keyboard, Ray-Ban Meta Gen 2, Echo Show 8, Azoth X, Harpe Ace Extreme, Falchion RX Low Profile, Cetra SpeedNova, PA32UCDM.
- **Note:** the Switch 2 Carrying Case UPC is counted as VERIFIED on the single-source Nintendo store read. If it is demoted at add time (see the caveat in entry #35), the tally becomes VERIFIED 17 / PENDING 33.

### Steadiest picks (cleanest passes, no flags)
- **Bose Lifestyle Ultra Soundbar** — new flagship, 4 retailers at list, UPC verified.
- **Sony BRAVIA Theatre Bar 8** — Best Buy sold-by-Best-Buy at list, UPC verified twice.
- **JBL Vibe Beam 2** — Best Buy + B&H at list, UPC verified.
- **Logitech G502 X LIGHTSPEED** — Best Buy + B&H at list, UPC verified.
- **Corsair K70 PRO TKL / K70 CORE TKL RGB** — Best Buy + B&H at list, UPCs verified.
- **Apple TV 4K 4th gen / HomePod mini 2 / AirTag 2** — Apple direct + Best Buy at list, UPCs verified.
- **Razer Kraken V4 X / Hammerhead V3 X HyperSpeed** — Razer direct + Best Buy at list, MPNs verified (UPCs pending).
- **Garmin HRM-Fit** — Best Buy + Garmin direct at list, UPC verified (two sources).

### Held back / not in the 50
- **14 firm passes cut at synthesis** (see table above) — the strongest alternates are JBL PartyBox Encore 2 (UPC verified) and Fitbit Charge 6 (UPC verified).
- **5 alternates** (see table above) — same-model colorways or un-firmed alternates, not separate models.
- **Batch-2 firm passes NOT re-proposed:** Bose TV Speaker 2nd gen (graduated to pass #9 in this batch), Corsair HS80 v2 MAX (graduated to pass #24), Logitech G502 HERO (cut at synthesis — see table), HP E27 G5 (cut at synthesis — see table), ASUS ROG Strix Scope II 96 RX (cut at synthesis — see table). All other batch-2 passes were either already added in batch 2 or rejected again (see rejections).
- **Batch-2 Reserve (Bose TV Speaker 2nd gen) — used:** graduated to pass #9. No new Reserve was created from batch 2; the batch-3 Reserve is JBL Live Flex 3.

## Considered and rejected

| Model | Reason |
|---|---|
| Sony SRS-XV800 | Best Buy Clearance $584.99; 2023 model superseded by ULT TOWER line |
| Sony INZONE M10S | Best Buy Clearance $237.99, Unavailable; successor M10S II not yet purchasable |
| Sony ULT Tower 10 | Predecessor to ULT TOWER MAX, superseded |
| Sony ULT TOWER 9AC (SRSULT900AC) | Distinct AC variant, Adorama backorder; do not mix UPC with SRSULT900 |
| JBL Authentics 200 | Marketplace-only + open-box/clearance; no Best Buy-sold new row |
| JBL Authentics 300 | Batch-2 borderline rejection stands |
| JBL Authentics 500 | Best Buy-sold listing is Clearance $637.99; 2023 model |
| JBL Bar 800 | No Best Buy-sold listing; marketplace + refurb only; Bar 800 MK2 overseas only |
| Bose Bass Module 700 | Accessory (requires a Bose soundbar), 2018-era; no clean MPN/UPC pinned |
| Sony DualSense Edge | Duplicate (sony-dualsense-edge-black-white) |
| Sony PlayStation Portal | Duplicate (sony-playstation-portal) |
| Bose SoundLink Max | Duplicate (bose-soundlink-max-black) |
| JBL Tune 770NC | Duplicate (jbl-tune-770nc-black) |
| JBL Tour Pro 3 | Duplicate (jbl-tour-pro-3-black) |
| Bose QC Ultra Headphones 2nd Gen | Duplicate (bose-qc-ultra-2-black) |
| Sony WH-1000XM6 | Duplicate |
| Sony LinkBuds Fit / LinkBuds Open | Duplicates |
| Bose QC Earbuds (2024) | Duplicate (bose-qc-earbuds-black) |
| JBL Charge 6 / Xtreme 4 | Duplicates |
| JBL PartyBox Stage 320 / PartyBox 330 | Duplicates ("PartyBox 320" IS the in-catalog Stage 320) |
| Logitech G Pro X 2 Superlight | Duplicate (logitech-g-pro-x-superlight-2-black) |
| Logitech MX Keys S | Duplicate (logitech-mx-keys-s-pale-grey) |
| Logitech MX Brio | Duplicate (logitech-mx-brio-graphite) |
| Logitech G Pro X 2 LIGHTSPEED headset | Superseded by PRO X3 (pass #15) |
| Logitech G735 Aurora | Best Buy own-stock Clearance $207.99; other listings marketplace; B&H backordered |
| Corsair K70 MAX RGB | Discontinued (Corsair US) |
| Corsair K100 RGB | No live channel; Best Buy Unavailable; all sellers OOS |
| Corsair Virtuoso RGB Wireless XT | Corsair US lists only Refurbished; no clean US direct new channel |
| HyperX Cloud Alpha Wireless (4P5D4AA) | Superseded by Cloud Alpha 2 (pass #22); original at 46% off = clearance drift |
| HyperX Cloud II Wireless (4P5K4AA) | No live US direct channel |
| HyperX Alloy Origins 65 | Duplicate (hyperx-alloy-origins-65-aqua) |
| HyperX Alloy Rise 75 | Duplicate (hyperx-alloy-rise-75-black) |
| Corsair K65 PLUS Wireless | Duplicate (corsair-k65-plus-wireless-midnight-grey) |
| Corsair M65 RGB Ultra | Duplicate (corsair-m65-rgb-ultra-black) |
| Corsair K70 CORE RGB (full-size) | Duplicate (corsair-k70-core-rgb-black) |
| Corsair Scimitar Elite Wireless (plain) | Batch-2 rejection stands (Corsair US OOS, refurb only) |
| Corsair Darkstar Wireless | Batch-2 rejection stands |
| Corsair K100 AIR | Batch-2 rejection stands |
| Corsair Virtuoso Pro | Batch-2 rejection stands |
| Corsair Sabre Pro / Sabre RGB Pro | Batch-2 rejection stands (discontinued) |
| Razer BlackWidow V4 Pro | Duplicate (razer-blackwidow-v4-pro-green-black) |
| Razer BlackWidow V4 X | Duplicate (razer-blackwidow-v4-x-green) |
| Razer Basilisk V3 Pro 35K | Duplicate (razer-basilisk-v3-pro-35k-black) |
| Razer DeathAdder V4 Pro | Duplicate (razer-deathadder-v4-pro-black) |
| Razer Cobra Pro | Duplicate (razer-cobra-pro-black) |
| Razer Huntsman V3 Pro (full-size) | Duplicate (razer-huntsman-v3-pro-black) |
| Razer Kraken V4 (wireless) | Duplicate (razer-kraken-v4-black) |
| Razer Hammerhead Pro HyperSpeed (2023) | 2023 model at deep discount; superseded by Hammerhead V3/V3 X |
| ASUS ROG Keris II Ace | Duplicate (asus-rog-keris-ii-ace-black) |
| Apple AirPods Pro 3 | Duplicate (apple-airpods-pro-3) |
| Apple Studio Display (2026) | Duplicate (apple-studio-display-2026-standard-tilt) |
| Apple HomePod mini (1st gen) | Superseded by HomePod mini 2; Best Buy clearance $21.99, Unavailable |
| Apple iPad 11th gen (A16) | Duplicate (apple-ipad-a16-11) |
| Apple Magic Mouse (USB-C) | Duplicate (apple-magic-mouse-usbc) |
| Apple Magic Trackpad (USB-C) | Duplicate (apple-magic-trackpad-usbc) |
| Apple Watch SE 3 40mm | Duplicate (apple-watch-se3-40mm) |
| Samsung Galaxy Buds3 (SM-R530) | No clean US direct channel; Best Buy marketplace/refurb only; Samsung US page offline |
| Samsung Galaxy Buds Core (SM-R410) | Never released in the US (LatAm only) |
| Samsung Galaxy Buds FE | Batch-2 rejection stands |
| Samsung Galaxy Watch Ultra (original) | Batch-2 rejection stands |
| Samsung Galaxy Watch8 Classic 46mm | Duplicate (samsung-galaxy-watch8-classic-46mm-black) |
| Samsung Galaxy Tab S11 | Duplicate (samsung-galaxy-tab-s11-128gb-gray) |
| Samsung Galaxy Book5 360 | Laptop, out of scope |
| Samsung Odyssey OLED G8 G81SF 27" | Clearance drift (Best Buy Clearance; Samsung US OOS) |
| Nintendo Switch 2 (console) | Duplicate (nintendo-switch-2) |
| Nintendo Joy-Con 2 (pair) | Duplicate (nintendo-joy-con-2-pair-light-blue-light-red) |
| Garmin Venu 4 45mm | Duplicate (garmin-venu-4-45mm-silver-gray) |
| Garmin Instinct 3 | Duplicate (garmin-instinct-3-amoled-45mm-black) |
| Garmin Edge 540 | Duplicate (garmin-edge-540) |
| Garmin Edge 850 | Duplicate (garmin-edge-850) |
| Garmin Approach S70 47mm | Superseded by Approach S72; discounted/rebate stock; Best Buy only a marketplace bundle |
| Microsoft Xbox Wireless Controller | Duplicate (xbox-wireless-controller-black) |
| Microsoft Xbox Elite Series 2 | Duplicate (xbox-elite-series-2-black) |
| Microsoft Xbox Wireless Headset (2024) | Duplicate (xbox-wireless-headset-2024-black) |
| Microsoft Xbox Series S 512GB | Duplicate (xbox-series-s-512gb-robot-white) |
| Lenovo Legion Go S (SteamOS) | Duplicate (lenovo-legion-go-s-steamos) |
| Lenovo Legion Tab Gen 3 | Duplicate (lenovo-legion-tab-gen-3-eclipse-black) |
| Lenovo Yoga Tab Plus (Gen 2) | Duplicate (lenovo-yoga-tab-plus-gen-2-cosmic-blue) |
| Keychron Q3 Max | Duplicate (keychron-q3-max) |
| Keychron V1 Max | Duplicate (keychron-v1-max) |
| Keychron K10 Max | Carry-forward rejected again (MPN/stock not firmed) |
| Lenovo Legion Go 2 | Carry-forward rejected again (price instability persists) |
| HyperX Cloud Alpha, Black-Red | Duplicate (hyperx-cloud-alpha-black-red) |
| Anker Soundcore Liberty 4 Pro | Duplicate (anker-liberty-4-pro-glossy-black) |
| Anker Soundcore Space One Pro | Duplicate (anker-space-one-pro-black) |
| Anker Prime Charger (100W) | Duplicate (anker-prime-100w) |
| Anker Soundcore Boom 2 | Duplicate (anker-soundcore-boom-2-black) |
| Anker Prime Charger (140W) | Duplicate (anker-prime-charger-140w) |
| Anker Prime Power Bank 20K 220W / 26K 300W | Duplicates |
| Anker Prime Charger 65W (A2664/A2666) | Batch-2 rejection stands (does not exist as briefed) |
| Anker Prime Power Bank 20K 200W (A1336) | Batch-2 rejection stands (sold out) |
| Anker 737 GaNPrime A2148 | Batch-2 rejection stands |
| Anker 737 Power Bank A1289 | Batch-2 rejection stands |
| Anker Soundcore Boom 2 Plus (A3134) | Discontinued at B&H; Best Buy marketplace-only |
| Alienware AW420K | Batch-2 rejection stands (2022, superseded) |
| Alienware AW720M | Batch-2 rejection stands |
| Alienware AW920H | Superseded by in-catalog Pro Wireless Headset; marketplace/OEM only; clearance drift |
| Alienware Pro Wireless Keyboard | Duplicate (alienware-pro-wireless-gaming-keyboard-dark-side-of-the-moon) |
| Alienware AW3425DW | Duplicate (alienware-aw3425dw) |
| Alienware AW2524HF | Duplicate (alienware-aw2524hf) |
| Dell U2725QE | Duplicate (dell-ultrasharp-27-4k-thunderbolt-hub-monitor-u2725qe) |
| Dell 27 Plus 4K S2725QS | Duplicate (dell-27-plus-4k-monitor-s2725qs) |
| Dell 32 Plus 4K S3225QS | Duplicate (dell-32-plus-4k-monitor-s3225qs) |
| Dell U2726Q | Model does not exist |
| Dell P2725H | No US channel confirmed |
| Dell U4025QW | Duplicate (dell-u4025qw, batch 2) |
| Dell AW2725DF | Rejected on re-verification (Dell US "Unavailable"; price conflict; superseded by in-catalog AW2726DM) |
| HP OMEN 27qs (original) | Batch-2 rejection stands (Best Buy clearance) |
| HP OMEN 32x | Duplicate (hp-omen-32x-black) |
| HP OMEN 32 (original, 2017) | Batch-2 rejection stands (long discontinued) |
| HP OMEN 45L (desktop) | Out of scope (desktops) |
| HP Poly Voyager Focus 2 | Borderline dropped (2021-era office gear; HP.com prices conflict across crawls). Held as revival candidate. |
| HP 930 / 935 Creator Mouse | Batch-2 rejection stands (no live US channel) |
| Google Pixel Buds Pro 2 | Duplicate (google-pixel-buds-pro-2-porcelain) |
| Google Pixel Buds 2a | Duplicate (google-pixel-buds-2a-hazel) |
| Google Pixel Watch 4 (41/45mm) | Duplicates (both sizes in catalog) |
| Google Pixel Tablet | Discontinued |
| Google Chromecast | Discontinued |
| Google Nest Hub / Nest Doorbell | Smart home, out of scope |
| Meta Quest 3 / 3S | Duplicates (both in catalog) |
| Amazon Fire HD 10 (2023) | Batch-2 rejection stands (Amazon-only channel + previous-gen) |
| Amazon Echo Dot 5th Gen | Price incoherence + marketplace seller; 2022 model; no clean Best Buy-sold new row |
| ASUS ROG Delta II | Duplicate (asus-rog-delta-ii-black) |
| ASUS ROG Swift OLED PG27UCDM | Duplicate (asus-rog-swift-oled-pg27ucdm-black) |
| ASUS ProArt PA279CRV | Duplicate (asus-proart-display-pa279crv) |
| ASUS ROG Strix Scope II 96 Wireless | Duplicate (asus-rog-strix-scope-ii-96-wireless-black, NX switches) |
| ASUS ROG Azoth | Duplicate (asus-rog-azoth-black) |
| ASUS ROG Azoth 96 HE | Duplicate (asus-rog-azoth-96-he-black) |
| ASUS ROG Ally X | Batch-2 rejection stands (Best Buy clearance) |
| ASUS TUF Gaming VG27AQL3A | No clean US retailer-direct row (Amazon-derived prices only); 2023 model |
| ASUS ROG Harpe II Ace | Not proposed (Harpe Ace Extreme already covers the ASUS mouse slot; Best Buy sold $169.99 — revival candidate) |
| Anker Soundcore Sleep A20 | Not re-proposed (previous gen; A30 passes #40; batch-2 cut reasons stand) |

## Not evaluated this round (held for a future batch — not rejected)
- Sony BRAVIA Theatre Bar 1000, Sony Surround Speakers 700, Sony INZONE H9 II, Sony INZONE H5 II, JBL PartyBox 720, JBL Charge 5 WiFi, Bose SoundLink Revolve+ II.
- Logitech G Cloud, Astro A50 X, Logitech G Pro X 2 Superlight (white), Logitech G Pro X Superlight 2 DEX, Logitech G Pro X 2 Superlight (white).
- Samsung Galaxy Tab S10 Lite, Samsung Music Frame, Samsung Odyssey G9, Samsung Galaxy Watch FE, Samsung Galaxy Buds2 Pro.
- Anker 555 USB-C Hub, Anker Prime Docking Station, Anker MagGo, Anker Soundcore V30i, Anker Soundcore AeroFit Pro, ASUS ZenScreen MB16ACV.
- HP Poly Voyager Focus 2, ASUS ROG Harpe II Ace — revival candidates (see rejections).

## Corrections to brief-supplied identifiers (so the next batch starts clean)
- Bose TV Speaker 2nd Gen MPN is 901067-1100, not BOSETVSPEAKER2 (Abt internal code).
- Sony ULT TOWER MAX MPN is SRSULT3000, not SRSULTMAX.
- Logitech G502 HERO MPN is 910-005469; 910-006178 is the G502 X LIGHTSPEED. **And G502 HERO is not in the catalog** — it was a candidate, not a pending model (same error as batch 2's G502 HERO note, now corrected).
- Logitech G309 MPN is 910-007197 (Black), not 910-006914 (White).
- Razer Basilisk V3 X MPN is RZ01-04870100-R3U1, not RZ01-04890100 (that is the Basilisk V3 Pro 35K).
- Razer Barracuda X Chroma MPN is RZ04-05220100-R3U1, not RZ04-05240100 (that is the Barracuda X Hyperspeed).
- Razer Huntsman V3 Pro TKL US MPN is RZ03-04980200-R3U1; RZ03-04980100-R3M1 is international.
- HyperX Cloud Alpha Wireless MPN is 4P5D4AA, not 4P5D6AA.
- The "HP 960 mouse" does not exist — the 960 is the Ergonomic Wireless Keyboard (7E755AA#ABA).
- HP E27 G5 US SKU is 6N4E2AL#ABA; 6N4E2AA#ABA is a second configuration.
- ASUS ROG Azoth X White US MPN is 90MP044F-BKAA32 (Snow V2); 90MP044G-BKAA32 is Storm.
- ASUS ROG Harpe Ace Extreme US MPN is 90MP03U0-BMAA00; BMUA00 is a second suffix.
- ASUS ROG Cetra SpeedNova White US MPN is 90YH03Y0-BTAA13; eBay's BTAA10 is a suffix discrepancy.
- Anker Soundcore Sleep A30 MPN is AKD1301 for all colorways; UPCs differ per color.
- Alienware AW3225QF: no Dell manufacturer part surfaced; MPN is recorded as the model code AW3225QF.
- Amazon Fire TV Stick 4K Max current model is 2nd Gen (2023), B0BP9SNVH9.

## Membership check (so a later session can repeat it)
- Reference file used at synthesis: /tmp/batch3_reference.json (300 catalog keys, 132 verified UPCs, 229 MPNs; built from the 2026-11-16 snapshot).
- Script: python3 -c with json — load the reference, load the 50 proposed keys/MPNs/UPCs, check each against the catalog on key, MPN, UPC, and normalized model-name tokens. Result at synthesis: **0 collisions** (no proposed key, MPN, or UPC matches any catalog row; no proposed model name matches an in-catalog model under a different color/config).
- The same check was re-run after the draft was written, by parsing the draft file itself (50 numbered entries, 1–50 complete, unique keys; UPC VERIFIED 18 / PENDING 32; MPN pending 2 — Switch 2 Carrying Case, Echo Show 8; category lines 51 = 50 candidates + 1 Reserve). Result: **0 collisions** vs the 300-model reference. The script also caught two draft errors that were fixed before commit: the header tally (was 16/34, corrected to 18/32 — the group reports' summary tallies disagreed with their own per-entry markings) and the category summary (mice had been omitted).
- Note: the reference file was built from the 2026-11-16 snapshot (300 models). If the catalog changes before this batch is approved, re-run the check against the new snapshot before adding anything.

## Needs the user's decision
1. **Approve this batch of 50?** If yes, the catalog goes 300 → 350 (verified identifiers 135 → 153, pending 165 → 197 — see the identifier note in the Summary: the verified count drops by one if the Switch 2 Case UPC is demoted at add time).
2. **Reserve:** JBL Live Flex 3 — include it as #51 now, or keep it as the first Reserve for batch 4?
3. **New categories:** streaming-devices (Apple TV 4K, pass #28) and smart-displays (Echo Show 8, pass #45) — approve both categories as part of this batch, or hold one/both?
4. **Flagged items — approve as-is, hold, or drop?** The main flags: ULT TOWER 9 UPC conflict (two variants, keep PENDING); Switch 2 Carrying Case UPC (single-source, could not be independently re-confirmed at synthesis — re-confirm at add time or demote to PENDING); Echo Show 8 (both identifiers pending — the weakest entry in the batch); Apple TV 4K (launched 3 days ago); HW-Q990F (previous flagship, ~50% off); QC Headphones 2nd Gen ($219 holiday price vs $359 list); AW3225QF (successor announced, wide price range); Bar 9 (Best Buy sold-by unconfirmed + Adorama backorder conflict); Alarmo (price rose $99.99 → $109.99).
5. **Pending identifiers:** 32 of 50 UPCs are pending (18 verified). No rule change is proposed — the standing rule (never relax) is kept. If the user wants a higher verified rate, the batch would need to be smaller, not looser.
