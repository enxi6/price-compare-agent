# Track A — Sony / Logitech / JBL second-source re-probes (batch-6 rework)

- Track: Sony / Logitech / JBL (12 models)
- Researched: 2026-11-20 (searches + page opens, ~17:18–17:19 UTC)
- Rules applied: US-market models only; seller-direct / retailer-direct only; no Amazon as a source in any form; no eBay; no marketplace / third-party sellers. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant. Qualifying sources: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, Newegg spec page, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators (Snapklik, Desertcart, Ubuy, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. Best Buy model/spec field counts as the draft's lead source (as in the batch-6 draft itself).
- Verdict key: **VERIFIED** = two qualifying sources agree (both named) · **PENDING + lead** = single source, named (qualifying unless marked non-qualifying) · **NO LEAD** = no source found at all.
- Prices are as captured on 2026-11-20 unless a crawl age is noted; Best Buy Black Friday deals end Nov 28, 2026 — re-verify promo prices at add time.

## Tally (12 models, 24 identifiers)

- **MPN VERIFIED: 12 / 12** (all models; Bar 500 with a correction — see §11).
- **UPC VERIFIED: 1 / 12 clean** (G435). Brio 100 is VERIFIED with a datasheet-hosting caveat (see §6) — counts as 2 / 12 if the parent accepts it, 1 / 12 under the strictest reading.
- **UPC PENDING with a qualifying lead: 6** — WF-C700N (Abt), INZONE H3 (B&H), Zone Vibe 125 (Logitech datasheet), M650 L (B&H), Authentics 200 (B&H), Encore Essential 2 (B&H).
- **UPC PENDING with a non-qualifying lead only: 4** — HT-A5000 (manuals.plus), HT-S400 (Amazon), Bar 500 (Amazon / Walts / Zoro), Tune 520BT (BJ's).
- **UPC NO LEAD: 0** — every identifier has at least a lead.

---

## 1. Sony WF-C700N — Black

- **MPN `WFC700N/B` — VERIFIED.**
  - Best Buy (lead): model field `WFC700N/B`.
  - Crutchfield: "MFR # WFC700N/B" (Item # 158WFC700B), page "Sony WF-C700N" — https://www.crutchfield.com/p_158WFC700B/Sony-WF-C700N.html
  - Abt: "Model # WFC700N/B", page title "Sony Black Truly Wireless Noise Canceling In-Ear Headphones - WFC700N/B" — https://www.abt.com/Sony-Black-Truly-Wireless-Noise-Canceling-In-Ear-Headphones-WFC700NB/p/192386.html
- **UPC `027242925625` — PENDING + lead (Abt).**
  - Abt: "UPC # 027242925625" (same page as above) — one qualifying source.
  - Amazon (non-qualifying) lists the same UPC; Amazon.in also shows Model WFC700N/B + UPC 027242925625 — corroboration only.
  - B&H page opened 2026-11-20 17:18 UTC showed no MFR # or UPC in visible text; status "No Longer Available", $118.00, Availability: Discontinued — https://www.bhphotovideo.com/c/product/1762430-REG/sony_wfc700n_b_wf_c700n_truly_wireless_in_ear.html
  - Micro Center search returned no listing; Newegg has a WF-C700N page but its snippet shows no MPN/UPC lines.
- **Price/stock:** Best Buy $79.99 Black Friday (list $119.99) per draft; not re-captured in this session.

## 2. Sony INZONE H3 — White

- **MPN `MDR-G300` (rendered `MDRG300/W`) — VERIFIED.**
  - Best Buy (lead): Model `MDRG300/W`, SKU 6510365, White listing.
  - B&H: "BH # SOMDRG300W • MFR # MDRG300/W" — https://www.bhphotovideo.com/c/product/1720014-REG/sony_mdrg300_w_inzone_h3_wired_headset.html (specs variant: …/sony_mdrg300_w_inzone_h3_wired_headset.html/overview)
  - Crutchfield: "MFR # MDRG300/W" (Item # 158MDRG300) — https://www.crutchfield.com/ISEO-rgbtcspd/p_158MDRG300/Sony-INZONE-H3.html
- **UPC `027242923546` — PENDING + lead (B&H).**
  - B&H specs page: "UPC: 027242923546" for the White headset — one qualifying source.
  - Amazon (non-qualifying) agrees: UPC 027242923546, White, ASIN B0B1SXW7LB.
  - Best Buy spec-page searches did not surface a UPC line.
  - **Conflict flagged:** Kawartha TV (Canadian retailer, non-qualifying) lists UPC 027242923522 for MDRG300/W — treat as outlier; B&H + Amazon agree on …546.
- **Price/stock captured:** Best Buy $69.99, sold by Best Buy, SKU 6510365 (multiple crawls 3–7 days old as of 2026-11-20; older crawls showed $79.99 / $119.99). B&H $68.00 In Stock (was $118.00, Holiday Savings $50.00), Add to Cart, free delivery Wed Nov 25 (page opened 2026-11-20 17:18 UTC).

## 3. Sony HT-A5000 — Black

- **MPN `HT-A5000` (rendered `HTA5000` by retailers) — VERIFIED.**
  - Best Buy (lead): Model `HTA5000`.
  - Crutchfield: "MFR # HTA5000" (Item # 158HTA5000) — https://www.crutchfield.com/p_158HTA5000/Sony-HT-A5000.html
  - Note: retailers strip the hyphen (HTA5000 = HT-A5000); keep the hyphenated form per Sony naming.
- **UPC `656942665540` — PENDING, lead is non-qualifying only (manuals.plus).**
  - No qualifying source found. manuals.plus (non-qualifying) lists UPC 656942665540.
  - B&H no longer carries it — the B&H page is a replacement page for the HT-A8000, "No Longer Available".
  - Best Buy spec-page search did not surface a UPC line. (A live-browser check of Best Buy "See all specifications" at add time could still settle this.)
- **Price flag:** Best Buy shows two SKUs/prices — $499.99 (SKU 6467455, crawl 10 days old) vs $699.99 (SKU 10917148, crawl 3 days old). Draft had $499.99 InStock. **Re-check at add time.**

## 4. Sony HT-S400 — Black

- **MPN `HT-S400` (rendered `HTS400`) — VERIFIED.**
  - Best Buy (lead): Model `HTS400`.
  - B&H: "BH # SOHTS400 • MFR # HTS400".
- **UPC `027242923942` — PENDING, lead is non-qualifying only (Amazon).**
  - Amazon (non-qualifying) lists UPC 027242923942 for HTS400.
  - A Best Buy-spec mirror site (trusthavensolution.com) also shows "UPC: 027242923942" — a mirror of Best Buy spec data, not a qualifying source; corroboration only.
  - B&H specs search showed no UPC line; Best Buy spec-page search did not surface a UPC line. Abt hosts a Sony spec-sheet PDF (content.abt.com, HTS400) but it contains no UPC.
- **Price/stock captured:** Best Buy $199.99 InStock, Model HTS400, SKU 6498905 (crawl 1 day old as of 2026-11-20). B&H $298.00 In Stock (older crawl).

## 5. Logitech G435 — Black

- **MPN `981-001049` — VERIFIED.**
  - Best Buy (lead): model field `981-001049`, SKU 6478273.
  - Abt: "Model # 981-001049", page title "Logitech G435 LIGHTSPEED Wireless Gaming Headset in Black - 981-001049" — https://www.abt.com/Logitech-G435-LIGHTSPEED-Wireless-Gaming-Headset-in-Black-981001049/p/215639.html
- **UPC `097855165763` — VERIFIED.**
  - Abt: "UPC # 097855165763" (same page as above).
  - Best Buy spec page: "Model Number: 981-001049 … UPC: 097855165763".
  - (Manuals.plus Logitech datasheet and Amazon agree; not needed.)
- **Price captured:** Best Buy $49.99 (crawls 1 day and 8 days old as of 2026-11-20), Black Friday banner ends Nov 28, 2026. In-stock wording was NOT explicitly captured in the snippets — re-check at add time. Note: Abt's own listing says "Sorry, this item is no longer available" — Abt is a source only, not the row.

## 6. Logitech Brio 100 — Graphite

- **MPN `960-001580` — VERIFIED.**
  - Best Buy (lead): Model `960-001580`, SKU 6550199.
  - B&H: page title / URL slug `logitech_960_001580_brio_100_full_hd` ("Logitech Brio 100 1080p Full HD Webcam (Graphite)") — https://www.bhphotovideo.com/c/product/1786643-REG/logitech_960_001580_brio_100_full_hd.html
- **UPC `097855188588` — VERIFIED (with caveat).**
  - B&H (opened 2026-11-20 17:18 UTC): "UPC: 097855188588" for the Graphite webcam — qualifying source #1.
  - Logitech's own datasheet PDF (© 2023 Logitech): "Part # 960-001580 … Bar code 097855188588 (EAN-13)" — brand-official spec content, qualifying source #2.
  - **Caveat:** the datasheet PDF is hosted on Zoro's static CMS (https://www.zoro.com/static/cms/enhanced_pdf/16ce75bc-62a1-44d3-9f94-b538455c8ff7.pdf), not on logitech.com. The content is verbatim Logitech. If the parent applies the strictest reading of the qualifying list, downgrade to PENDING + lead (B&H).
  - NFM also lists UPC 097855188588 + Model 960001580 (not in the qualifying list). Best Buy spec-page search did not surface a UPC line.
- **Price/stock captured:** Best Buy $39.99, sold by Best Buy, InStock, SKU 6550199. B&H $24.99 In Stock (was $39.99, Holiday Savings $15.00).

## 7. Logitech Zone Vibe 125 — Graphite

- **MPN `981-001166` — VERIFIED.**
  - Best Buy (lead): model field `981-001166`.
  - B&H: page title "Logitech Zone Vibe 125 Wireless Headphones 981-001166 B&H" — https://www.bhphotovideo.com/c/product/1706460-REG/logitech_981_001166_zone_vibe_125_wireless.html?fromDisList=y
- **UPC `097855175113` — PENDING + lead (Logitech datasheet).**
  - Logitech datasheet PDF (doi-product-assets S3, © 2022 Logitech): "Part # 981-001166 … UPC 097855175113" — https://doi-product-assets.s3.amazonaws.com/pub/Manufacturer-Brochure/1073571733.pdf
  - Amazon (non-qualifying) agrees: UPC 097855175113, Model 981-001166, Graphite.
  - B&H page opened 2026-11-20 (crawl 2026-05-11): title confirms the model/part number, but the fetched text shows NO UPC line; status "No Longer Available", $129.99, Discontinued.
  - **Conflict flagged:** Snapklik lists UPC 657768069680 for this part number — ignored (non-qualifying aggregator, conflicts with datasheet + Amazon).
- **Do not mix:** Zone Vibe Wireless Teams listing 981-001440 is a different model.
- **Price:** Best Buy $129.99; B&H "No Longer Available", $129.99, Discontinued.

## 8. Logitech Signature M650 L — Graphite

- **MPN `910-006231` — VERIFIED.**
  - Best Buy (lead): Model `910-006231`, SKU 6491142 (sold by Best Buy).
  - Newegg: "Model # 910-006231" on "Logitech M650 Signature wireless Mouse 910-006231 Graphite 5 Buttons 1 x Wheel Wireless Mouse" — https://www.newegg.com/logitech-910-006231-m650-signature-wireless-mouse/p/N82E16826197520
  - NeweggBusiness: "Mfr. Part #: 910-006231" (Item # 9SIV04GJVB7832) — https://www.neweggbusiness.com/logitech-910-006231-m650-signature-wireless-mouse/p/9B-26-197-520
  - (B&H URL slug / title also carries 910-006231 — https://www.bhphotovideo.com/c/product/1679950-REG/logitech_910_006231_signature_m650_l_wireless.html — not needed now that Newegg confirms it cleanly.)
- **UPC `097855167583` — PENDING + lead (B&H).**
  - B&H (opened 2026-11-20 17:18 UTC): "UPC: 097855167583" for the Graphite, full-size, right-handed M650 L — one qualifying source.
  - Adorama's UPC list agrees ("Large Graphite Right-Handed: 097855167583") but Adorama is not in the qualifying list. A Rakuten URL slug contains `00097855167583_upc` (non-qualifying corroboration). Newegg snippets show no UPC.
- **Do not mix:** 910-006347 is the for-Business Off-White variant (Newegg / Beach Audio confirm 910-006347 = M650 L for Business, Off White).
- **Price captured:** Best Buy $24.99 Black Friday, sold by Best Buy, SKU 6491142, InStock (crawl 1 day old as of 2026-11-20; another crawl showed $29.99 Black Friday Deal; list $39.99). Ignore marketplace SKU 13197120 (Gamzi Digital, $90.99) and SKU 10735960 (Electronic Express, $43.99). B&H $29.99 In Stock (was $39.99).

## 9. JBL Authentics 200 — Black

- **MPN `JBLAUTH200BLKAM` — VERIFIED.**
  - JBL.com: "Item#: JBLAUTH200BLKAM" — https://www.jbl.com/JBLAUTH200BLKAM.html?cgid=wifi-speakers
  - B&H: page title "JBL Authentics 200 Wireless Home Speaker JBLAUTH200BLKAM" — https://www.bhphotovideo.com/c/product/1790807-REG/jbl_jblauth200blkam_authentics_200_wireless_home.html/specs
  - Crutchfield: "MFR # JBLAUTH200BLKAM" (Item # 109ATH200B) — https://www.crutchfield.com/S-lb9sKKrMxwv/p_109ATH200B/JBL-Authentics-200.html
- **UPC `050036396219` — PENDING + lead (B&H).**
  - B&H specs page: "UPC: 050036396219" — one qualifying source.
  - Abt page opened 2026-11-20 17:19 UTC shows price/model in URL but NO "UPC #" field in fetched text — https://www.abt.com/JBL-Speaker-Authentics-200-Wireless-Smart-Home-JBLAUTH200BLKAM/p/201881.html
  - Amazon, manuals.plus, Snapklik, camelcamelcamel, eBay all agree on 050036396219 — all non-qualifying. A Newegg search returned no listing.
- **Price/stock captured:** B&H $189.95 In Stock (was $379.95, Holiday Savings $190.00). Abt $189.95, InStock (manufacturer rebate ends 12/05/2026, comp. value $379.95). JBL.com $189.95.

## 10. JBL PartyBox Encore Essential 2 — Black

- **MPN `JBLPBENCOREESS2AM` — VERIFIED.**
  - B&H: "BH # JBPBENCRESM MFR # JBLPBENCOREESS2AM" — https://www.bhphotovideo.com/c/product/1875203-REG/jbl_jblpbencoreess2am_partybox_encore_essential_100w.html
  - Best Buy: Model `JBLPBENCOREESS2AM`, SKU 6644260.
  - Abt: page title "JBL JBLPBENCOREESS2AM PartyBox Encore Essential 2 Portable Speaker Bluetooth in Black" — https://www.abt.com/JBL-PartyBox-Encore-Essential-2-Portable-Speaker-Bluetooth-in-Black-JBLPBENCOREESS2AM/p/218823.html
  - Dell: "Manufacturer Part Number, JBLPBENCOREESS2AM".
  - **Draft supersession:** the draft said single-source VIP Outlet and Best Buy SKU 10209209 at $329.99 — superseded by current Best Buy SKU 6644260 at $199.95.
- **UPC `050036411059` — PENDING + lead (B&H).**
  - B&H page (opened 2026-11-20 17:18 UTC): "UPC: 050036411059" — one qualifying source.
  - Abt page opened 2026-11-20 17:19 UTC shows NO "UPC #" field in fetched text (same URL as above).
  - Walts.com (not qualifying) corroborates: "Model PARTYBOX-ENCORE-ESSENTIAL-2 | MPN JBLPBENCOREESS2AM | UPC 050036411059" — https://walts.com/product/partybox-encore-essential-2
  - Crutchfield page opened 2026-11-20 (crawl 2026-11-06): features + $329.95 InStock, but NO MFR # and NO UPC in fetched text — https://www.crutchfield.com/p_109PBENCR2/JBL-PartyBox-Encore-Essential-2.html
  - NFM lists Model JBLPBENCOREESS2AM + UPC 050036411059 (not in the qualifying list).
- **Price/stock captured:** B&H $199.95 In Stock (was $329.95, Holiday Savings $130.00). Best Buy $199.95 InStock, sold by Best Buy, SKU 6644260. Abt $199.95 InStock (rebate ends 12/05/2026). Crutchfield still shows $329.95 (14-day-old crawl — stale vs $199.95 at three sellers). Do NOT use Best Buy SKU 12942222 — that is a bundle with EASYSING mic, sold/shipped by Electronics Expo (marketplace), $329.90.

## 11. JBL Bar 500 — Black

- **MPN CORRECTION — draft `BAR-500` is a shortened display name, not the full MPN. Full MPN `JBLBAR500PROBLKAM` — VERIFIED.**
  - JBL.com: "Item#: JBLBAR500PROBLKAM" — http://jbl.com/soundbars/BAR-500-.html?cgid=soundbars&dwvar_BAR-500-_color=Black-AM-Current
  - Crutchfield: "MFR # JBLBAR500PROBLKAM" (Item # 109BAR500) — https://www.crutchfield.com/S-P3w84d4chpZ/p_109BAR500/JBL-Bar-500.html
  - Best Buy: Model `JBLBAR500PROBLKAM`, SKU 11113238.
  - **Flag:** one JBL.com crawl (2026-11-20) showed "Item#: BAR500PROBLKAM-Z" on a different JBL.com URL variant — note the -Z suffix discrepancy.
- **UPC `050036387743` — PENDING, lead is non-qualifying sources only.**
  - Amazon, Walts (Model BAR-500, MPN JBLBAR500PROBLKAM, UPC 050036387743), and Zoro (MFR # JBLBAR500PROBLKAM, UPC # 50036387743 — 11 digits, missing leading 0) all agree — none is in the qualifying list.
  - No B&H original Bar 500 page found (B&H shows only the MK2 now).
  - **Conflict flagged:** manuals.plus lists UPC 094148727882 for the Bar 500 — ignored (non-qualifying, conflicts with the Amazon/Walts/Zoro agreement).
- **Do not mix:** BAR500MK2 / JBLBAR500M2BLKAM is the newer model (B&H UPC 050036408127 belongs to the MK2).
- **Price/stock captured:** Best Buy $399.95 InStock, SKU 11113238. JBL.com $399.95 in one crawl, $349.95 OutOfStock in a later crawl (2026-11-20).

## 12. JBL Tune 520BT — Black

- **MPN `JBLT520BTBLKAM` — already VERIFIED per the batch-6 draft (JBL.com + Best Buy Canada). Re-confirmed.**
  - JBL.com: "Item#: JBLT520BTBLKAM", $34.95 InStock (crawl 2026-11-20) — https://www.jbl.com/JBLT520BTBLKAM.html
  - Kohl's lists the color-variant family: "Model no. JBLT520BTPURAM, JBLT520BTBLKAM, JBLT520BTBLUAM, JBLT520BTWHTAM" — https://www.kohls.com/product/prd-6887285/jbl-tune-520bt-wireless-on-ear-headphones.jsp?skuid=78671343
  - Ace Hardware: "Mfr # JBLT520BTBLKAM" (not in the qualifying list) — https://www.acehardware.com/departments/lighting-and-electrical/home-electronics/audio-accessories/6086901
  - Note: JBL.com also lists a personalized variant Item# T520BTBLKAMCSTM — different item, do not mix.
- **UPC `050036394925` — PENDING, lead is non-qualifying only (BJ's).**
  - BJ's Wholesale lists "Model Number JBLT520BTBLKAM … upc 050036394925" — BJ's is not in the qualifying list.
  - Amazon (non-qualifying) agrees: UPC 050036394925, Item model number JBLT520BTBLKAM.
  - No B&H / Crutchfield / Newegg qualifying source found. JBL.com global lists EAN 6925281963582, not a UPC.
- **Price:** JBL.com $34.95 InStock. (Kohl's $59.99 OutOfStock; Ace Hardware $59.99 InStock — both above JBL.com.)

---

## Flags for the parent / add-time re-checks

1. **Bar 500 MPN correction:** draft "BAR-500" → full MPN `JBLBAR500PROBLKAM`; also note the JBL.com `-Z` variant (`BAR500PROBLKAM-Z`).
2. **Encore Essential 2 Best Buy SKU supersession:** draft SKU 10209209 @ $329.99 → current SKU 6644260 @ $199.95 (sold by Best Buy, InStock).
3. **HT-A5000 price conflict:** Best Buy shows $499.99 (SKU 6467455, 10-day crawl) and $699.99 (SKU 10917148, 3-day crawl) — re-check at add time.
4. **UPC conflicts (all from non-qualifying sources, noted and ignored):** INZONE H3 …546 (B&H/Amazon) vs Kawartha …522; Bar 500 …387743 (Amazon/Walts/Zoro) vs manuals.plus 094148727882; Zone Vibe 125 …175113 (datasheet/Amazon) vs Snapklik 657768069680.
5. **Brio 100 UPC caveat:** second source is Logitech's own datasheet PDF hosted on Zoro's static CMS — accept as brand-official spec or downgrade to PENDING + lead (B&H).
6. **M650 L MPN now clean:** Newegg + NeweggBusiness confirm 910-006231, so the earlier B&H-URL-slug caveat no longer matters.
7. **G435 in-stock wording** not explicitly captured at Best Buy — re-check at add time (price $49.99 captured).
8. **Promo prices:** Best Buy BF deals end Nov 28, 2026; JBL.com Bar 500 already flipped $399.95 → $349.95 OutOfStock in a later crawl the same day.
