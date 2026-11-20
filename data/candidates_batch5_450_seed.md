# Batch 5 seed pack — catalog 400 → 450 (seed only, 12 models)

- **Date:** 2026-11-18 (evening, after batch 4 landed as commit `f6e63ac`)
- **Status:** SEED ONLY — read-only preparation while the batch-5 draft awaits the user's nod. Nothing in this file has been added to the catalog. No repo file other than this one was created or modified; nothing committed or pushed.
- **How it was built:** carried forward from `data/candidates_batch4_400.md` — the 3 Reserve items (INZONE E9, Apple Watch Ultra 3, JBL Charge 5) plus the 9 "held for a future batch — not rejected" items that survive a fresh check. Each held item was re-researched this evening (web search, 2026-11-18): model existence, US MPN, UPC lead, US price/stock. Two items from the held list were NOT carried (see "Deliberately not carried").
- **Rules applied:** DECISIONS 001–005, 015, 016, 020, 021, 027, 057, 068 (same as batch 4). Mainstream/new products; US-market versions only; seller-direct only; no Amazon in any form, no third-party/marketplace sellers, no parallel imports, no international variants, no second-hand/refurbished/clearance-only/discontinued stock. Every seed checked against all 400 catalog rows (key/model/MPN/UPC, including different colors/configs of the same model) — 0 collisions (see "Membership check").
- **Identifier honesty:** UPC/EAN is marked VERIFIED only when found on a retailer/manufacturer spec page or an official source. Otherwise PENDING, with the lead value (if any) and what was checked. Amazon-only and eBay-only values are never treated as verified. Non-US suffixes (R3G1, EUB, CE7) are never carried as the US code. Keychron-style EAN+SKU precedent not needed here.
- **Identifier tally for the 12 seeds:** UPC/EAN VERIFIED 0 / PENDING 12. MPN pinned for 9 of 12 (see per-entry notes); MPN pending for Nommo V2 Pro (US-suffix trap), Tab A11 (no US code found), Watch Ultra 3 (Medium US code not found). Zero verified UPCs is expected for a seed: the verified codes in past batches came from the fresh-pick research and the add-time re-verification, not from the carry-forward pool. Do not read 0/12 as a quality failure — read it as "these 12 are the known-quantity nucleus; the fresh 38 picks supply the verified codes."
- **Brands with zero models in this seed:** Bose, Microsoft, Lenovo, Alienware, Meta — same gap as batch 4, unchanged. No Bose/Microsoft model passed this round either (see "Deliberately not carried").

## Seeds (12)

### S1. Sony BRAVIA Theatre Rear 9, Black — `sony-bravia-theatre-rear-9-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SA-RS9 (Sony US PDP "Model: SA-RS9"; Best Buy model SARS9, SKU 6673696).
- **Why it qualifies:** Current Sony rear-speaker pair (2026, 180W, Dolby Atmos/DTS:X, 360 Spatial Sound Mapping); pairs with Bar 9/8/7 and HT-A7000/A5000/A3000. Sony direct list $749.99.
- **Identifiers:** MPN SA-RS9; UPC PENDING, no lead found (targeted search 2026-11-18 + Abt page fetch — no UPC printed; Best Buy spec-panel check at add time).
- **Price/stock:** Sony direct $749.99; Best Buy $549.99, sold by Best Buy, "Not in stock — Ready Fri, Nov 20"; Abt $548 InStock (manufacturer rebate ends 11/18/2026 — price may move after today); Target $548 InStock.
- **Flag:** Promo price + Best Buy restock Fri Nov 20 — re-check stock and price when the full draft is completed.

### S2. JBL Authentics 500, Black — `jbl-authentics-500-black`
- **Category:** speakers (smart-home speaker with Alexa/Google voice)
- **Variant pinned:** Black, MPN JBLAUTH500BLKAM (JBL.com + Crutchfield MFR # + Amazon item details agree).
- **Why it qualifies:** Current JBL flagship home speaker, Dolby Atmos Music, Wi-Fi/Bluetooth; clean direct rows at Abt/Sweetwater/Crutchfield.
- **Identifiers:** MPN JBLAUTH500BLKAM; UPC PENDING — lead 050036396264 (eBay + Amazon agree; no retailer spec page seen yet — verify at add time). Do NOT use the JBLAUTH500BLKAM-Z listing ($562.95) as price evidence — -Z is a different listing.
- **Price/stock:** Abt $399.95 (rebate to 12/05/2026, comp $749.95); Sweetwater $399.95 in stock; Crutchfield $449.95 in stock; JBL direct $399.95 OutOfStock.
- **Flag:** Smart-home category (Alexa/Google). Batch 4 rejected the Authentics 200 for smart-home + marketplace-only Best Buy; that reason does NOT apply here (direct rows exist), but note the category when the full draft is assembled.

### S3. JBL Vibe Flex 2, Black — `jbl-vibe-flex-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLVFLEX2BLKAM (JBL.com; White is JBLVFLEX2WHTAM).
- **Why it qualifies:** Current JBL true-wireless earbuds (2024–now, 12mm drivers, Smart Ambient); JBL direct $69.95.
- **Identifiers:** MPN JBLVFLEX2BLKAM; UPC PENDING, no lead found (targeted search 2026-11-18). Do NOT use gen-1 codes: UPC 050036391368 and eBay GTIN 0050036391344 belong to the gen-1 Vibe Flex (JBLVFLEXMITAM etc.).
- **Price/stock:** JBL direct $69.95 — Black OutOfStock, White InStock.
- **Flag:** Black OOS at JBL direct — check Best Buy/B&H stock when the full draft is completed; if Black stays OOS everywhere direct, hold or pin White instead (do not silently switch variant).

### S4. Razer Leviathan V2 X, Black — `razer-leviathan-v2-x-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN RZ05-04280100-R3U1 (Best Buy model, SKU 6521035).
- **Why it qualifies:** Current Razer compact PC soundbar (USB-C, Bluetooth 5.0, Chroma RGB, no subwoofer); Best Buy $99.99 sold by Best Buy.
- **Identifiers:** MPN RZ05-04280100-R3U1; UPC PENDING, no lead found. Do NOT use R3M1 (UK/EU, EAN 8886419379645) or the Kuromi edition RZ05-04280300-R3M1.
- **Price/stock:** Best Buy $99.99.
- **Flag:** Distinct from in-catalog Leviathan V2 (`razer-leviathan-v2-black`, RZ05-04160100-R3U1, with subwoofer, batch 4 pending) — V2 X has no subwoofer; keep the two entries separate and do not merge rows.

### S5. Razer Nommo V2 Pro, Black — `razer-nommo-v2-pro-black`
- **Category:** speakers
- **Variant pinned:** Black, 2.1 with wireless subwoofer + wireless control pod, THX Spatial Audio.
- **Why it qualifies:** Razer's top desktop speaker set; Razer US list $449.99 (confirmed Nov 12, 2026).
- **Identifiers:** MPN PENDING — lead RZ05-04740100-R3G1 is UK/EU packaging (Overclockers + netcodex agree on R3G1; EAN 8887910060490 belongs to R3G1). The US suffix -R3U1 is inferred from the V2 X pattern only and is NOT confirmed — verify at draft completion, do not carry R3G1 as the US code. UPC PENDING, no lead.
- **Price/stock:** Razer US $449.99 list.
- **Flag:** Distinct from in-catalog Nommo V2 (`razer-nommo-v2-black`, mid tier, wired sub, batch 4 pending) — Pro has wireless sub + control pod + rear-projection Chroma. MPN suffix trap is the main risk on this entry.

### S6. Razer Nommo V2 X, Black — `razer-nommo-v2-x-black`
- **Category:** speakers
- **Variant pinned:** Black, 2.0, no subwoofer, THX Spatial Audio, MPN RZ05-04760100-R3U1 (Best Buy model, SKU 6547859, 4.6 stars / 143 reviews).
- **Why it qualifies:** Entry tier of the Nommo V2 line; Razer US list $149.99; Best Buy $149.99.
- **Identifiers:** MPN RZ05-04760100-R3U1; UPC PENDING, no lead (Best Buy spec panel not in fetched page text — spec-panel check at add time). EAN 8887910060292 belongs to the UK R3G1 — do not attach.
- **Price/stock:** Best Buy $149.99; Razer US $149.99 list.
- **Flag:** Distinct from in-catalog Nommo V2 — V2 X has no subwoofer, no control pod, no Chroma. Keep separate.

### S7. HyperX Cloud Stinger 2 Core, PC, Black — `hyperx-cloud-stinger-2-core-pc-black`
- **Category:** headphones
- **Variant pinned:** PC version, Black, MPN 683L9AA (Amazon.in item details, twice).
- **Why it qualifies:** Current HyperX entry-level wired PC headset (40mm drivers, swivel-to-mute); HyperX US $39.99 InStock (Black + White).
- **Identifiers:** MPN 683L9AA; UPC PENDING — lead 196548418183 (Amazon.in only — not verified).
- **Price/stock:** HyperX US $39.99 InStock.
- **Flag:** Variant matrix — PS version is 6H9B5AA (White) / 6H9B6AA (Black), Xbox version is "CloudX Stinger 2 Core". This entry pins the PC version 683L9AA only. Distinct from in-catalog Cloud Stinger 2 (`hyperx-cloud-stinger-2-black`, non-Core).

### S8. Samsung Galaxy Tab A11, 8.7" 64GB Wi-Fi, Gray — `samsung-galaxy-tab-a11-64gb-wifi-gray`
- **Category:** tablets
- **Variant pinned:** 8.7", 4GB/64GB, Wi-Fi, Gray (base A11, not A11+).
- **Why it qualifies:** Samsung's current entry tablet (announced Sep 2025, launch MSRP $180, 90Hz, metal frame).
- **Identifiers:** MPN PENDING, no US lead (EU SM-X130NZAAEUB / SM-X130NZSAEUB — do NOT use as the US code; a US XAR-suffix code is unconfirmed). UPC PENDING, no lead.
- **Price/stock:** Micro Center $149.99 (Aug 2026); Walmart low $127.49 (Aug 2026). No Samsung US / Best Buy / Amazon US listing found in this round — US channel is thin.
- **Flag:** Weakest seed on channel evidence. Hold unless a US retailer-direct row firms up when the full draft is completed; drop it from the 50 if it does not. Distinct from in-catalog Tab A11+ (`samsung-galaxy-tab-a11-plus-128gb-gray`, 11", verified).

### S9. Garmin Descent G1, Slate Gray (non-Solar) — `garmin-descent-g1-slate-gray`
- **Category:** wearables
- **Variant pinned:** Standard (non-Solar), Slate Gray, MPN 010-02604-00 (GPS Nation, Garmin authorized dealer, "Garmin USA" + San Diego Divers part number agree).
- **Why it qualifies:** Garmin dive computer/smartwatch, $549.99 list; niche like the in-catalog Descent G2/X10.
- **Identifiers:** MPN 010-02604-00; UPC PENDING, no lead. Note: Garmin's own page shows 010-02604-10 — possible regional/bundle suffix; re-check at draft completion.
- **Price/stock:** $549.99 list; new stock sold out at GPS Nation and Ascent Outdoors; Best Buy $449.99 row is marketplace seller Focus Camera — excluded by rule.
- **Flag:** New-stock channel is thin. Hold unless Garmin US shows stock when the full draft is completed. Distinct from in-catalog Descent G2/X10 (batch 4 pending).

### S10. Sony INZONE E9, Black — `sony-inzone-e9-black` (Reserve R1, carried from batch 4)
- **Category:** earbuds (wired IEM)
- **Variant pinned:** Black, MPN IER-G900B (Sony US PDP, model IER-G900B; US variant IERG900B.UC; EU CE7 is IERG900B.CE7 — different suffix, do not mix).
- **Why it qualifies:** Current Sony IEM (Aug 2025 launch with Fnatic; no mic; Glass Purple is a new colorway Oct 2026, not a separate model). Held as Reserve because no clean current in-stock retailer-direct row for Black was found — latest Sony direct crawl shows Black Out Of Stock; White shows In Stock at Best Buy ($118, SKU 10938757, seller unclear).
- **Identifiers:** MPN IER-G900B; UPC PENDING — lead 027242933187 (Amazon.in only; no non-Amazon source found, so not verifiable).
- **Price/stock:** Sony direct list $149.99; sale $139.99 seen in an April crawl, $129.99 for White on Oct 7.
- **Flag:** Weakest candidate — re-check Black stock at add time, or hold.

### S11. Apple Watch Ultra 3, Black Titanium, Black Alpine Loop Medium — `apple-watch-ultra-3-49mm-gps-cellular-black-alpine-medium` (Reserve R2, carried from batch 4)
- **Category:** wearables
- **Variant pinned:** GPS + Cellular 49mm, Black Titanium case, Black Alpine Loop, Medium.
- **Why it qualifies:** Previous-gen Apple watch still sold new at Target ($799.99 list, In Stock). Held as Reserve because the UPC is conflicted and the model is superseded.
- **Identifiers:** MPN PENDING, no confirmed US code (Best Buy Small = MF0Q4LW/A; Medium US MPN not found; Harvey Norman IE lists MF0V4DH/A — regional, do not use). UPC PENDING — conflicted: Target lists 195950484991 for this exact variant; Littlewoods UK lists EAN 195950484892 for the same Medium variant. Two different codes, no tiebreaker.
- **Price/stock:** Target $799.99, In Stock (list price); Best Buy Small $549.00 promo, sold by Best Buy, only 3 left.
- **Flag:** Superseded — Ultra 4 is already in catalog; 9to5Mac (2026-11-06) explicitly calls current Ultra 3 deals "clearance pricing" ($250 off). Watch for clearance-only drift.

### S12. JBL Charge 5, Black — `jbl-charge-5-black` (Reserve R3, carried from batch 4)
- **Category:** speakers
- **Variant pinned:** Black, MPN JBLCHARGE5BLKAM.
- **Why it qualifies:** Previous-gen JBL speaker still sold new at JBL US ($139.95, was $179.95). Held as Reserve because of the current-status tension — Zoro marks it Discontinued, and Charge 6 is the current model in the catalog.
- **Identifiers:** MPN JBLCHARGE5BLKAM; UPC lead 050036380218 (OfferUp + Visions CA recertified JBLCHARGE5BLKAMB1 + eBay GTIN 0050036380218 multiple + Zoro MFR/UPC + BigaMart — strong agreement, but no B&H/Best Buy spec page seen yet → treat as PENDING/strong lead, verify at add time).
- **Price/stock:** JBL US $139.95 InStock (was $179.95).
- **Flag:** Previous generation (Charge 6 is current and in catalog) but still sold new at JBL US; Zoro marks it Discontinued — tension to note, do not overstate current status. (Note: the batch-3 brief's claim that "in-catalog Charge 5 exists" is wrong — only Charge 6 is in the catalog.)

## Deliberately not carried (held-list items that fail on re-check)
- **JBL Live Beam 4** — no US channel yet (TechRadar Aug 2026; the-gadgeteer 2026-11-02: no US pricing/launch/listing). Re-check before any future batch; do not draft it blind.
- **JBL Authentics 200** — rejected in batch 4 (smart-home speaker + Best Buy new stock marketplace-only; Best Buy own listing open-box clearance). The Authentics 500 above is the one that passes.
- **Corsair HS65 Surround, Carbon** — no in-stock new row anywhere direct (Corsair Revival Series $39.99 OutOfStock; Best Buy own row Unavailable; Corsair-fulfilled Sold Out; rest marketplace).
- **ASUS ROG Swift OLED PG27AQDP** — cut at batch-4 synthesis: no shippable in-stock row.
- **ASUS TUF VG27AQML1A** — held: ASUS US $369 but OutOfStock at brand direct, no US retailer price or UPC found; white-variant MPN only from Egypt.
- **HP Poly Voyager Focus 2** — still unfirmed (variant matrix + HP.com price conflict $199.93 vs $381.95 for the same MPN; 2021-era) — dropped again.
- **Anker Nano Charger 45W** — held: model confusion (Smart Display 180° foldable vs older plain 45W); assumed MPN A2694 never surfaced; UPC 194644347703 single-source (Very UK EAN).
- **Logitech K780 Multi-Device Keyboard, White** — cut at batch-4 synthesis on age (2017-era, $69.99); identifiers are actually verified (MPN 920-008149, UPC 097855122834, B&H). Kept out on age, not identifiers.
- **Microsoft Surface Arc Mouse, Black** — cut at batch-4 synthesis on age (2017-era, $89.99); MPN corrected to FHD-00016, UPC still pending. Microsoft gap persists; this is the only Microsoft pass and it is 2017 stock.
- **Logitech Zone Vibe 125** — same hardware as Zone Vibe 100 (business/UC naming); do not create a separate entry.
- **Meta Quest 3S (white)** — same model as in-catalog, different colorway.
- **HyperX Alloy Origins Core, Red** — cut at batch-4 synthesis (2020-era; Icecat lists EndOfLifeDate 2026-10-31 for the Blue sibling; UPC pending with ambiguous EAN lead).

## Membership check (so a later session can repeat it)
- Reference: `price_agent/catalog.py` EVAL_SET, 400 models (verified 2026-11-18 after batch 4 landed).
- Script: `/tmp/batch5_seed_check.py` — load the reference, check the 12 seed entries (key, MPN, UPC/EAN, including intra-batch collisions) and list in-catalog siblings sharing a model core. Run 2026-11-18: **0 collisions, 0 errors** (no proposed key, MPN, or UPC/EAN matches any catalog row; no two seeds share a key, MPN, or UPC/EAN).
- Siblings confirmed distinct (same family, different model — do not merge): Leviathan V2 (in catalog) vs V2 X (seed); Nommo V2 (in catalog) vs V2 Pro / V2 X (seeds); Cloud Stinger 2 (in catalog) vs Stinger 2 Core PC (seed); Tab A11+ (in catalog, verified) vs Tab A11 base (seed); Descent G2/X10 (in catalog) vs Descent G1 (seed); Charge 6 (in catalog) vs Charge 5 (seed).
- Note: the reference was built from the 2026-11-18 catalog (400 models). If the catalog changes before this seed is used, re-run the check against the new snapshot before adding anything.

## Needs the user's decision
1. **Complete the full batch-5 draft (50) from this seed + ~38 fresh picks?** Recommended timing: AFTER tomorrow's 10:52 PT refresh (2026-11-19), so batch 4's 50 new models get their first quotes first and the 23 verified batch-4 models can be probed for rows — that is higher-value work than drafting batch 5 tonight. Two seed prices are also promo-sensitive (Rear 9 Abt rebate ends 11/18; Best Buy restock Fri Nov 20), so a draft finished tomorrow is fresher. Nothing is lost by waiting: the seed is saved and membership-checked here.
2. **Or draft immediately tonight?** The seed is ready to build on now; the cost is drafting blind before batch-4 quotes land.
3. **Flagged seeds — drop now or keep as pending?** Tab A11 (thin US channel), Descent G1 (new stock sold out), Watch Ultra 3 (superseded + conflicted UPC) — keep as pending and decide at draft completion, or cut any of them now.
