# Track E — Lenovo.com sweep (batch-6 rework)

- **Date observed:** 2026-11-20
- **Scope:** lenovo.com current mainstream lineup — ThinkPad (T14 Gen 5/6, X1 Carbon, X1 Yoga, T16, E16/E14), Yoga / IdeaPad Slim, Legion (Pro 5, Pro 7, 5i, LOQ), ThinkVision monitors, Lenovo accessories (docks). Plus re-confirmation of the 3 Lenovo entries already in `data/candidates_batch6_500.md` (entries 3, 39, 40).
- **Method:** `browser.search` + `browser.open` (text fetch only). No live browser, no purchases, no sign-ins.
- **Rules applied:** US-market models only; seller-direct or retailer-direct only; no Amazon as a source in any form; no eBay; no marketplace/third-party sellers. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant/config. Qualifying sources: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, CDW spec page, Newegg spec page, Best Buy spec panel, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators (Snapklik, Desertcart, Ubuy, Klarna, Slickdeals, Smartprix, laptopvslaptop, kelaptop, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. No identifier was invented; each source page was checked to name the same model/config.
- **Catalog membership baseline (checked 2026-11-20):** `price_agent/catalog.py` holds 450 models (`key=` count = 450). Only **11 Lenovo keys** exist, all tablets/handhelds — **no Lenovo laptop, monitor, or accessory is in the catalog**. The 11: `lenovo-legion-tab-gen-3-eclipse-black`, `lenovo-tab-plus-gen-2-celestial-white`, `lenovo-idea-tab-pro-gen-2-cloud-grey`, `lenovo-tab-one-luna-grey`, `lenovo-yoga-tab-plus-gen-2-cosmic-blue`, `lenovo-legion-tab-gen-5-eclipse-black`, `lenovo-yoga-tab-gen-2-cosmic-blue`, `lenovo-idea-tab-luna-grey`, `lenovo-idea-tab-plus-cloud-grey`, `lenovo-legion-go-s-steamos`, `lenovo-legion-go-2-32gb-1tb-eclipse-black`. Every laptop candidate below is therefore new by key/MPN/UPC unless stated otherwise.
- **Refinement applied (user, 2026-11-20):** do NOT force weak Lenovo picks — the batch fills from Samsung, then ASUS, if Lenovo yield is thin. Only the strongest Lenovo finds are picks; a model with no retailer-direct row and no second identifier source goes to backlog, not picks. **Yield is 7 picks (4 MPN-VERIFIED, 2 MPN-PENDING with direct rows, 1 flagged lenovo.com-only), against the ~10 cap. The 3 unfilled Lenovo slots are intentionally left for Samsung/ASUS.** A thin yield is reported honestly, not padded.
- **Best Buy seller note:** where a Best Buy price/stock is captured, the seller is recorded — "sold & shipped by" a marketplace seller (IST Computers, PC Heaven, Mobile Advance, Merchant Expo, antonline, etc.) is NOT a direct row. Best Buy laptop listings are heavily polluted with "Upgraded" third-party configs (PC Heaven / IST Computers reseal-and-upgrade units with seller warranties); those model fields read `83LY0000US -Upgraded` and are never the pinned config.

## Method caveats (read before using the verdicts)

1. **Newegg bot wall (2026-11-20):** direct opens of newegg.com product pages hit a CAPTCHA ("Are you a human?"). The Newegg legs for #3 (T16 Gen 4 21QN005XUS), #7 (X1 Carbon 21NS0012US) and the Legion 5i (#5) therefore rest on search fetches of the Newegg listing/spec pages, not direct opens — flagged again at each entry, following the Track B #8 precedent. The search fetch is the Newegg page's own crawled text (title/spec naming the part number), not a snippet alone, but it is one step weaker than a direct open.
2. **CDW prices:** CDW product pages opened in-session print the MFG# and specs but the fetched text does not always reproduce the advertised price. CDW prices below come from CDW search-result crawls of the same product pages (same MFG#/CDW#), not from the direct open — flagged at each entry. The CDW row is a direct row (CDW sells it, In Stock); the price is the one to re-verify at add time.
3. **Staples is NOT on the strict qualifying-source list** (B&H, Abt, Micro Center, Crutchfield, CDW, Newegg, Best Buy spec panel, brand official, authorized distributor). The IdeaPad 5 (#6) MPN therefore stays PENDING even though Staples corroborates B&H; the entry is carried as a pick only because it has a clean B&H direct row and the corroboration is from a second major US retailer. Add-time decision: accept Staples as a second source or leave MPN PENDING.
4. **Legion 5i Walmart row (#5):** the $1,499 Walmart-direct row is reported by a Slickdeals deal post ("Sold and shipped by Walmart.com"), not by a direct open of the Walmart listing. The row must be re-verified on walmart.com at add time (price, seller, part number on the listing).
5. **Legion Pro 5 Best Buy price (#2):** the $1,179.99 figure in the draft/Slickdeals (Feb 2026) is stale. Recent Best Buy crawls of the direct SKU show $1,579.99 (13-day crawl) and $1,774.99/$2,449 on other SKUs. Re-check price at add time; do not carry $1,179.99.
6. **B&H T14 Gen 5 price moved in-session:** search snippets showed $1,799.00; the direct open on 2026-11-20 showed $1,499.00 In Stock. Use $1,499.00, re-check at add time.
7. **"2K" vs FHD conflict on the LOQ (#backlog):** Best Buy titles the LOQ 83VA001PUS "15.6\" 2K" but its own spec text and the Lenovo PSREF-derived spec say FHD 144Hz. Unresolved — one reason it is backlog, not a pick.

---

## PICKS (7) — for batch 6

### 1. Lenovo ThinkPad T14 Gen 5 — Black (21MC000CUS) ★ strongest pick
- **Key:** `lenovo-thinkpad-t14-gen-5-black`
- **Category:** laptops
- **Variant pinned:** Black, 21MC000CUS — AMD Ryzen 7 PRO 8840U, 16GB DDR5, 512GB SSD, 14" WUXGA 1920x1200 IPS non-touch, Win 11 Pro
- **Membership:** NOT in catalog (no key/MPN/UPC match; catalog has no ThinkPad at all). Distinct from in-draft T14 Gen 6 (21QJ00CSUS, different generation/config) and from the 21ML0053US touchscreen config (checked, no clean row — see Skipped).
- **Identifiers:**
  - MPN 21MC000CUS — **VERIFIED** (B&H spec page, opened 2026-11-20: title "Lenovo 14\" ThinkPad T14 Gen 5 Laptop (Black) 21MC000CUS" + CDW spec page: "MFG#: 21MC000CUS | CDW#: 7941798", same Ryzen 7 PRO 8840U / 16GB / 512GB / Win 11 Pro config).
  - UPC 198153286874 — **PENDING + lead (B&H only)**. Printed on the opened B&H spec page. No second qualifying source found.
- **Price / stock:** B&H $1,499.00 In Stock (direct open, 2026-11-20). CDW In Stock, $1,486.99 advertised (27-day crawl) / $1,811.99 (225-day crawl) — price varies across crawls, re-check at add time. Best Buy has only "Upgraded" IST Computers listings for T14 Gen 5 — not usable.
- **Flag:** UPC single-source (B&H only). CDW price needs re-check at add time (see caveat 2).

### 2. Lenovo Legion Pro 5 Gen 10 AMD — Eclipse Black (83LT000MUS)
- **Key:** `lenovo-legion-pro-5-gen-10-eclipse-black`
- **Category:** laptops
- **Variant pinned:** Eclipse Black, 83LT000MUS — AMD Ryzen 7 8745HX, RTX 5060 8GB, 32GB DDR5, 1TB SSD, 16" WQXGA 2560x1600 OLED 165Hz
- **Membership:** NOT in catalog. Distinct from in-draft Legion Pro 5 16IRX9 83DF00A8US (different generation/config — see Dropped below) and from Legion Pro 7 (83RU0002US, backlog).
- **Identifiers:**
  - MPN 83LT000MUS — **VERIFIED** (lenovo.com product page, title "… | 83LT000MUS", $2,360.15 InStock + Best Buy model field: Model 83LT000MUS, SKU 6619246, Sold by Best Buy).
  - UPC — **PENDING, no lead found.**
- **Price / stock:** Best Buy direct SKU 6619246, Sold by Best Buy — **price must be re-checked at add time** (see caveat 5: $1,179.99 Slickdeals figure is stale; recent crawls $1,579.99 on this SKU, $1,774.99/$2,449 on sibling SKUs; some sibling SKUs now read "no longer available in new condition"). lenovo.com $2,360.15 InStock as the non-promo reference.
- **Flag:** Best Buy price unstable across crawls — re-check at add time; do not carry $1,179.99. Do not mix with the kelaptop listing that mislabels the CPU as Ryzen 9 7845HX (non-qualifying source, wrong CPU — Best Buy + lenovo.com agree on Ryzen 7 8745HX).

### 3. Lenovo ThinkPad T16 Gen 4 — Black (21QN005XUS)
- **Key:** `lenovo-thinkpad-t16-gen-4-black`
- **Category:** laptops
- **Variant pinned:** Black, 21QN005XUS — AMD Ryzen AI 7 PRO 350, 16GB DDR5, 512GB SSD, 16" WUXGA 1920x1200, Win 11 Pro
- **Membership:** NOT in catalog. Distinct from the 21QN0045US config (Ryzen AI 5 PRO 340, 256GB — backlog sibling).
- **Identifiers:**
  - MPN 21QN005XUS — **VERIFIED** (CDW spec page: "MFG#: 21QN005XUS | CDW#: 8436800" + Newegg listing page naming 21QN005XUS, search-fetch — see caveat 1; corroborated by SHI distributor listing: "Mfr Part #: 21QN005XUS", stock 955).
  - UPC — **PENDING, no lead found.**
- **Price / stock:** CDW In Stock, $1,483.99 advertised (search-result crawl of the CDW page — see caveat 2). Adorama lists it at $1,649.00, "Ships from Manufacturer" (Adorama is not on the strict qualifying list; recorded only as corroboration). Newegg listings $1,162.02–$1,257.93 (seller attribution unclear in the search fetch — do not use as the row). Best Buy has only "Upgraded" PCOnline/IST listings — not usable.
- **Flag:** Newegg leg is search-fetch only (bot wall). CDW price from search crawl — re-check at add time.

### 4. Lenovo ThinkPad E16 Gen 3 — Black (21ST0008US)
- **Key:** `lenovo-thinkpad-e16-gen-3-black`
- **Category:** laptops
- **Variant pinned:** Black, 21ST0008US — AMD Ryzen 7 250, 16GB DDR5, 512GB SSD, 16" WUXGA 1920x1200 touchscreen IPS, Win 11 Pro
- **Membership:** NOT in catalog. Distinct from in-catalog Lenovo tablets (different product class) and from ThinkPad E14 Gen 7 (seen in CDW results, not pursued — see Skipped).
- **Identifiers:**
  - MPN 21ST0008US — **VERIFIED** (CDW spec page: "MFG#: 21ST0008US | CDW#: 9084576", In Stock + NeweggBusiness spec page: "Part Number | 21ST0008US", same Ryzen 7 250 / 16GB / 512GB / touchscreen config).
  - UPC 198157339941 — **PENDING + lead (non-qualifying only)**. Appears only on technologygalaxy.com (unknown retailer, not a qualifying source). No qualifying retailer spec page prints it.
- **Price / stock:** CDW In Stock, $1,212.99 advertised (list $1,599.00). Best Buy listing is sold by Merchant Expo LLC (marketplace) at $1,311.63 — not usable. Newegg's own listing is sold by antonline (marketplace) — not usable as the row.
- **Flag:** UPC lead is non-qualifying only — do not upgrade on it. CDW price from search crawl — re-check at add time.

### 5. Lenovo Legion 5i 15" — Black (83LY0000US)
- **Key:** `lenovo-legion-5i-15-rtx-5060-black`
- **Category:** laptops
- **Variant pinned:** Black, 83LY0000US — Intel Core i7-14700HX, RTX 5060 8GB, 16GB DDR5, 1TB SSD, 15.1" WQXGA 2560x1600 OLED 165Hz
- **Membership:** NOT in catalog. Distinct from Legion Pro 5 83LT000MUS (different model/config) and from the Legion 5i 15.3" Ultra 7 251HX (Best Buy SKU 12906541, model number not captured — see Skipped).
- **Identifiers:**
  - MPN 83LY0000US — **PENDING + strong lead** (Newegg listing page naming 83LY0000US, search-fetch — see caveat 1 + Slickdeals reporting the Walmart listing for "the same model (83LY0000US)"). Two retailer listings name the part number, but the Walmart leg is second-hand (deal-post report, not the Walmart page itself), so this stays PENDING, not VERIFIED. **Add-time step: open the Walmart listing directly; if it names 83LY0000US, the MPN becomes VERIFIED (Newegg + Walmart).**
  - UPC — **PENDING, no lead found.**
- **Price / stock:** Walmart $1,499.00, sold and shipped by Walmart.com (per Slickdeals, 2026-11 — see caveat 4, re-verify at add time). Newegg $1,705.99; Best Buy $1,949.00 (per the same Slickdeals street-price check). Best Buy's own listings for this part are all "Upgraded" PC Heaven configs ($1,949–$3,749) — not usable.
- **Flag:** Walmart row and MPN second leg both need a direct Walmart check at add time. Color "Black/Eclipse Black" taken from the Best Buy Upgraded listings — confirm on the Walmart page at add time.

### 6. Lenovo IdeaPad 5 2-in-1 14" — Snapdragon X Plus (83GH000AUS)
- **Key:** `lenovo-ideapad-5-2-in-1-14-black`
- **Category:** laptops
- **Variant pinned:** 83GH000AUS — Snapdragon X Plus 8-core, 16GB LPDDR5x, 1TB SSD, 14" 1920x1200 OLED touchscreen, Win 11 Home. (Family 14Q8X9 per Klarna; B&H lists it as "IdeaPad 5 2-in-1", Staples as "IdeaPad 5x" — same part number, same config.)
- **Membership:** NOT in catalog.
- **Identifiers:**
  - MPN 83GH000AUS — **PENDING** (B&H spec page: "BH # LE83GH000AUS MFR # 83GH000AUS", $699.00 In Stock + Staples listing: "Model: 83GH000AUS", $899.99. Staples is not on the strict qualifying list — see caveat 3 — so this stays PENDING. If the catalog owner accepts Staples as a qualifying retailer, the MPN would be VERIFIED.)
  - UPC 198154657529 — **PENDING + lead (B&H only)**. Printed on the B&H spec page. No second qualifying source found.
- **Price / stock:** B&H $699.00 In Stock (was $999.00, Holiday Savings $300.00), direct open confirmed. Staples $899.99, in-store only (49–75-day crawls, stale — do not use as the row).
- **Flag:** MPN PENDING on the Staples question (caveat 3). Color not pinned from the B&H title — confirm color at add time before finalizing the key. Do not mix with the 83GH0008US config (B&H: "No Longer Available").

### 7. Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition (21NS0012US) — FLAGGED lenovo.com-only pick (draft entry 3, re-confirmed)
- **Key:** `lenovo-thinkpad-x1-carbon-gen-13-aura-edition` (draft key, unchanged)
- **Category:** laptops
- **Variant pinned:** 21NS0012US — Intel Core Ultra 7 258V, 32GB LPDDR5X-8533, 1TB SSD, 14" 2.8K OLED 120Hz, Win 11 Pro, Eclipse Black
- **Membership:** NOT in catalog (draft membership check already cleared it; re-confirmed — no key/MPN/UPC match).
- **Identifiers:**
  - MPN 21NS0012US — **VERIFIED with caveat** (lenovo.com product page, title "… | 21NS0012US", $1,248.99 InStock + Newegg listing page naming 21NS0012US with the same Ultra 7 258V / 32GB / 1TB config, search-fetch — see caveat 1, Newegg direct open hit the bot wall). The Newegg leg is one step weaker than a direct open; if the catalog owner requires a direct-open second source, this drops to PENDING + strong lead.
  - UPC — **PENDING, no lead found (qualifying).** B&H prints UPC 828143670351, but that is for a DIFFERENT config (21NTSB8E00, $2,099.00) — do NOT attach it to 21NS0012US. Amazon prints UPC 197528630519 for a 255U/FHD+ config (different config, non-qualifying anyway).
- **Price / stock:** lenovo.com $1,248.99 InStock (JSON-LD, 1-day crawl). Best Buy has only an IST Computers "Upgraded" listing (Model 21NS-Upgraded, $2,399.99) — not a direct row. No retailer-direct row found.
- **Flag:** **DECISIONS 015 concern — lenovo.com-only row (the single flagged brand-direct-only pick in this sweep; the brief allows at most 1–2).** No retailer-direct row; UPC has no qualifying lead. Carried because the MPN is two-sourced and the lenovo.com price/stock is confirmed live — but if the batch prefers zero brand-direct-only entries, drop this one first and fill the slot from Samsung/ASUS.

---

## DRAFT ENTRY RE-EVALUATION (the other 2 Lenovo entries in the batch-6 draft)

### Legion Pro 5 16IRX9 83DF00A8US (draft entry 39) — RECOMMEND DROPPING from batch 6
- **Draft claim:** Best Buy Q&A page shows 83DF00A8US at $1,799.99.
- **Re-check 2026-11-20:** Best Buy product page (SKU 6575390, Model 83DF00A8US, i9-14900HX / RTX 4070 / 32GB / 2TB, Onyx Grey) now reads **"This item is no longer available in new condition."** No second identifier source found for this config (no B&H/CDW/Newegg/lenovo.com hit in the sweep; the only other hits are Instagram box-label photos and an Indonesian resale post — non-qualifying). No retailer-direct in-stock row exists.
- **Recommendation:** drop entry 39 from the batch and replace it with pick #2 (Legion Pro 5 Gen 10 83LT000MUS — newer generation, MPN VERIFIED, Best Buy direct row). Do not carry 83DF00A8US on the Q&A-page price alone.

### ThinkPad T14 Gen 6 21QJ00CSUS (draft entry 40) — NOT A PICK, moved to backlog
- **Draft claim:** MPN 21QJ00CSUS single-source (marketplace listing); lenovo.com row, price not captured; all Best Buy listings marketplace.
- **Re-check 2026-11-20:** MPN improved — **VERIFIED** (CDW spec page, opened: title names 21QJ00CSUS, Ryzen AI 7 PRO 350 / 16GB / 512GB / WUXGA, same config + Best Buy model field: Model 21QJ00CSUS, multiple SKUs). UPC: B&H prints UPC 199272842804, but that is for a DIFFERENT T14 Gen 6 config (21QDS2VV00, $1,699.00) — do NOT attach it. No qualifying UPC lead for 21QJ00CSUS.
- **Why not a pick:** still no usable price row — Best Buy new listings are marketplace (Mobile Advance $1,744.14; $1,663.58–$1,856.01 range) or refurbished ($1,049.00, SKU 12834639); CDW lists it but the fetched page shows no price; no lenovo.com US page for this exact part surfaced in search (only the Intel config 21QC007CUS at $667.99). Per the refinement (no retailer-direct row → backlog), it goes to backlog, not picks. See backlog entry B3.

---

## QUEUED LENOVO BACKLOG (verified or well-evidenced, not carried — cap / priority, not quality)

### B1. Lenovo Legion Pro 7 Gen 10 AMD — Eclipse Black (83RU0002US) ★ strongest backlog item
- **Key (if carried later):** `lenovo-legion-pro-7-gen-10-amd-eclipse-black`
- **Category:** laptops
- **Variant pinned:** 83RU0002US — Ryzen 9 9955HX, RTX 5070 Ti, 32GB, 2TB SSD, 16" 240Hz OLED
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 83RU0002US — **PENDING (lenovo.com only)**. No second qualifying source found; no retailer listing surfaced. UPC — no lead.
- **Price / stock:** lenovo.com $2,799.99 InStock (39% off est. value $4,562.99 — promo-sensitive est-value price; a Jan 2026 coupon price of $1,649 is historical, not live).
- **Why backlog, not pick:** lenovo.com-only (DECISIONS 015 concern), single-source MPN, est-value promo price. The draft already named it the strongest alternate; it stays that. Carry only if a slot opens and no better Samsung/ASUS fill exists.

### B2. Lenovo Yoga Slim 7x 14" — Cosmic Blue (83QR000AUS)
- **Key (if carried later):** `lenovo-yoga-slim-7x-14-cosmic-blue`
- **Category:** laptops
- **Variant pinned:** 83QR000AUS — Snapdragon X2 Plus X2P-42-100, 16GB, 512GB, 14" 2K OLED touchscreen, Cosmic Blue
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 83QR000AUS — **PENDING (Best Buy only)**. No second qualifying source found despite targeted searches (no lenovo.com page, no B&H listing surfaced). UPC — no lead.
- **Price / stock:** Best Buy direct, SKU 6672161, Sold by Best Buy, **$649.99 Holiday Deal** (comp $1,299.99; Slickdeals confirms $649.99, Nov 16). Open-box Excellent $584.99. (A second Best Buy SKU 12949047 shows $949.00 and a PC Heaven marketplace variant — pin SKU 6672161 only.)
- **Why backlog, not pick:** strong direct row and strong deal, but MPN single-source. One lenovo.com or B&H/Crutchfield confirmation of 83QR000AUS would promote this to a pick.

### B3. Lenovo ThinkPad T14 Gen 6 — Black (21QJ00CSUS) (draft entry 40)
- **Key:** `lenovo-thinkpad-t14-gen-6-black` (draft key, unchanged)
- **Category:** laptops
- **Variant pinned:** 21QJ00CSUS — AMD Ryzen AI 7 PRO 350, 16GB, 512GB, 14" WUXGA
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 21QJ00CSUS — **VERIFIED** (CDW spec page opened + Best Buy model field). UPC — PENDING, no lead (do not use B&H's 199272842804 — different config 21QDS2VV00).
- **Price / stock:** No usable direct row captured (see Draft Re-evaluation above). Best Buy refurb $1,049.00; marketplace new $1,663.58–$1,856.01.
- **Why backlog, not pick:** verified MPN but no direct price row. Promote if a CDW price or lenovo.com price is captured at add time.

### B4. Lenovo ThinkPad T16 Gen 4 — Black (21QN0045US)
- **Key (if carried later):** `lenovo-thinkpad-t16-gen-4-ryzen-5-black`
- **Category:** laptops
- **Variant pinned:** 21QN0045US — AMD Ryzen AI 5 PRO 340, 16GB, 256GB SSD, 16" WUXGA, Win 11 Pro
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 21QN0045US — **VERIFIED** (CDW spec page: "MFG#: 21QN0045US | CDW#: 8391839" + Newegg listing page naming 21QN0045US, search-fetch — see caveat 1; corroborated by SHI distributor: "Mfr Part #: 21QN0045US", stock 568).
- **Price / stock:** CDW In Stock, $1,445.37 advertised (search crawl — see caveat 2). Newegg $1,378.08 (seller unclear). Best Buy marketplace only (Merchant Expo $1,697.05).
- **Why backlog, not pick:** sibling of pick #3 (21QN005XUS, Ryzen 7 PRO / 512GB). One T16 config per batch is enough; this is the next T16 up if a slot opens.

### B5. Lenovo LOQ Essential 15ARP11 — Eclipse Black (83VA001PUS)
- **Key (if carried later):** `lenovo-loq-essential-15arp11-eclipse-black`
- **Category:** laptops
- **Variant pinned:** 83VA001PUS — AMD Ryzen 7 170, RTX 5050 8GB, 16GB, 512GB, 15.6" FHD 144Hz
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 83VA001PUS — **PENDING (Best Buy only)**. Second sources found are non-qualifying only (Microless Dubai, ictechdistribution). UPC — no lead.
- **Price / stock:** Best Buy direct, SKU 6673556, Sold by Best Buy, $1,049.99 (Black Friday Deal flags in crawls; price seen $1,049.99–$1,449.99 across crawls — re-check).
- **Why backlog, not pick:** MPN single-source + unresolved "2K" (title) vs FHD 144Hz (specs) discrepancy (see caveat 7). Needs a lenovo.com/B&H/CDW confirmation and a spec reconciliation before it can be a pick.

### B6. Lenovo ThinkPad T14 Gen 5 — Gray (21MC000NUS)
- **Key (if carried later):** `lenovo-thinkpad-t14-gen-5-gray`
- **Category:** laptops
- **Variant pinned:** 21MC000NUS — same Ryzen 7 PRO 8840U / 16GB / 512GB config as pick #1, Gray
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 21MC000NUS — **PENDING (B&H only)**. UPC 198153286256 — **PENDING (B&H only)**. Both printed on the B&H spec page; no second source found.
- **Price / stock:** B&H $1,323.58, "In Stock at Supplier, expected to ship in 7–14 Business Days" (not B&H warehouse stock).
- **Why backlog, not pick:** sibling of pick #1; single-source identifiers and supplier stock (weaker than pick #1's B&H In Stock).

### B7. Lenovo ThinkVision P27u-20 27" 4K IPS Monitor (62CBRAR6US) — weak alternate
- **Key (if carried later):** `lenovo-thinkvision-p27u-20-27-black`
- **Category:** monitors
- **Variant pinned:** 62CBRAR6US — 27" 4K UHD 3840x2160 IPS, Raven Black
- **Membership:** NOT in catalog.
- **Identifiers:** MPN 62CBRAR6US — **PENDING (Best Buy model field only)**. UPC 195713542920 — **PENDING (B&H only)**.
- **Price / stock:** B&H $749.99 (83-day-old crawl — stale, re-check). Best Buy listings are all marketplace sellers (IPC-STORE $817.41, Staples Inc. $771.38, Newegg Official $929.99, Beach Camera $899.00) — no Best Buy-direct row.
- **Why backlog, not pick:** stale B&H price, marketplace-only at Best Buy, older (2020-era) model. Weakest backlog item; carry only if a monitor slot is otherwise empty and the B&H price/stock re-verifies live.

---

## CHECKED AND SKIPPED (already in catalog / discontinued / no direct row)

- **Lenovo Legion Go 2 32GB/1TB Eclipse Black (83N0000BUS)** — already in catalog (pending). lenovo.com entry $1,099.99. Skip.
- **Lenovo Legion Go S (SteamOS)** — already in catalog (verified). Skip.
- **Lenovo Legion Pro 5 16IRX9 83DF00A8US** — draft entry 39; Best Buy row dead ("no longer available in new condition"), no second source. **Recommend dropping from the draft** (see Draft Re-evaluation). Not carried, not backlogged as a live alternate.
- **Lenovo ThinkPad T14 Gen 5 21ML0053US** (touchscreen, Ultra 5 125U, 16GB/512GB) — Best Buy has only "Upgraded" IST Computers listings; lenovo.com outlet lists a different AMD config (21MDX003R2, $1,304.36). No clean retailer-direct row for 21ML0053US. Skip; pick #1 (21MC000CUS) is the T14 Gen 5 carried instead.
- **Lenovo ThinkPad X1 Yoga Gen 10 (21NU family)** — no clean US retailer-direct row found; lenovo.com US part numbers not pinned to a single config in-session (AU part 21NU004LAU is not US; laptopvslaptop/Amazon-only evidence is non-qualifying). Skip.
- **Lenovo Yoga 7 2-in-1 83JR0003US (Seashell, Ryzen AI 5 340, 1TB)** — Best Buy listing sold by NextGen Outlet (marketplace, "an authorized Lenovo Reseller" — still a marketplace seller, not Best Buy direct). No direct row. Skip.
- **Lenovo Yoga Slim 7x 83QR0002US** (Snapdragon X2 Elite, 1TB) — Best Buy direct $1,649.99, but MPN single-source and the cheaper 83QR000AUS config is the stronger of the pair. Not pursued further; the family is represented by backlog B2.
- **Lenovo IdeaPad Slim 5 83HY001PUS (16", Cosmic Blue)** — lenovo.com only, $449.99 after a $500 eCoupon (list $949.99). Coupon-dependent brand-direct-only price, no retailer row. Skip.
- **Lenovo IdeaPad Slim 5 14IMH9 (83DA… family)** — EU/regional part numbers only in search results (83DA003LRM, 83DA0077SP, etc.); no US part pinned with a retailer-direct row. Skip.
- **Lenovo IdeaPad Flex 5 14ALC05 82HU0158US** — Best Buy listing is a Velztorm "Upgraded" config (marketplace). Skip.
- **Lenovo IdeaPad 5 2-in-1 83GH0008US** — B&H: "No Longer Available". Different config from pick #6; skip.
- **Lenovo Legion 5i 15.3" Ultra 7 251HX (Best Buy SKU 12906541)** — Best Buy listing exists (price seen $799.99–$1,899.99 across crawls, seller/model number not captured). Model/part number not pinned in-session. Skip; the Legion 5i family is represented by pick #5 (83LY0000US).
- **Lenovo Legion 5i 83LY000LUS (i7-14700HX, 512GB)** — Smartprix: "Out Of Stock" at Lenovo ($1,139.99). Skip.
- **Lenovo Legion 5i 16" 83NX0000US (Ultra 9 275HX, RTX 5060, 32GB)** — only a Woot Grade-A refurbished listing found. Skip.
- **Lenovo LOQ 15.3" 83TN0000US (Ryzen 7 250, RTX 5050, Luna Grey)** — Best Buy listing sold by antonline (marketplace) at $1,099.99. Skip.
- **Lenovo LOQ 15.6" 83JG000JUS (Ryzen 5, RTX 5050, Gray)** — Best Buy $999.99, seller not captured in-session. Not pursued; family represented by backlog B5.
- **Lenovo Legion Pro 7i Gen 10 (Best Buy SKU 12270126, RTX 5080, Ultra 9 275HX, 64GB, 1TB, Eclipse Black)** — Best Buy direct $4,399.00 In Stock, but the Lenovo part number was not pinned in-session and the price tier is well above the rest of the sweep. Not pursued; noted here so it is not mistaken for the AMD Pro 7 (83RU0002US, backlog B1).
- **Lenovo ThinkPad T16 Gen 4 22AW002NUS (Ultra 5 238V, 32GB, touchscreen)** — Best Buy listing sold by Merchant Expo LLC (marketplace) at $2,447.42. Skip.
- **Lenovo ThinkPad E14 Gen 7 (Ryzen 7 250)** — seen in CDW search results; not pursued (the E16 Gen 3, pick #4, is the E-family representative). Skip.
- **Lenovo ThinkPad T14 Gen 6 Intel 21QC007CUS** — lenovo.com $667.99 (a different, Intel config of the T14 Gen 6 family). Not pursued; the AMD config is backlog B3. Skip.
- **Lenovo ThinkVision T27UD-40 64AFGAR2US** — Best Buy listings all marketplace sellers (SpaceBound $483.37, etc.); no US B&H listing found (lenovo.com hit was the MY regional page, 64AFGAR2MY). No direct row. Skip.
- **Lenovo ThinkVision T27hv-30** — Best Buy marketplace (EP Holdings $659.41) only. Skip.
- **Lenovo ThinkVision P27Q-40 64A7GAR6UZ** — Best Buy marketplace (Beach Audio $363.48) only. Skip.
- **Lenovo ThinkVision T27h-30 63A3GAR1US** — Best Buy marketplace (Wingmoon $499.00) only. Skip.
- **Lenovo ThinkVision T27-40 64A5MAT6UZ** — Staples $99.99 (was $229.99), single source, no second identifier source. Skip.
- **Lenovo ThinkVision S27-4e 64BEKAT1UZ (2-pack)** — Best Buy marketplace (Velztorm) bundle listing only; a 2-pack is not a single-unit model. Skip.
- **Lenovo ThinkVision T27p-10 (61DAMAR1US)** — B&H: "No Longer Available" / Discontinued. Skip.
- **Lenovo ThinkPad USB-C Dock Gen 2 40AS0090US** — Best Buy listings marketplace (antonline) or seller-unclear; lenovo.com price (~$104) only via the FindTheDeal aggregator. No clean direct row. Skip.
- **Lenovo ThinkPad Universal USB-C Dock 40AY0090US** — Best Buy marketplace (Telesource $180.00) only. Skip.
- **Lenovo ThinkPad Dock 135W 40AY0135US** — Best Buy marketplace (SpaceBound $249.99) only. Skip.
- **Lenovo ThinkPad Hybrid USB-C Dock 40AF0135US** — Best Buy listing $323.26, seller not captured; bundle listings are marketplace (Abe's Electronics). Not pursued. Skip.

---

## Tally

- **Models/configs checked in total: ~35** (counting each distinct part number/config above: 3 draft entries + Pro 7 + T14 Gen 5 x3 configs + X1 Yoga + Yoga Slim 7x x2 + Yoga 7 + IdeaPad Slim 5 x2 families + IdeaPad 5 2-in-1 x2 + IdeaPad Flex 5 + Legion 5i x4 + LOQ x3 + Legion Pro 7i + T16 Gen 4 x3 + E16 + E14 + T14 Gen 6 Intel + ThinkVision x8 + docks x4 + Legion Go 2 / Go S already-in-catalog).
- **Picks for batch 6: 7** (4 MPN-VERIFIED: T14 Gen 5 21MC000CUS, Legion Pro 5 83LT000MUS, T16 Gen 4 21QN005XUS, E16 Gen 3 21ST0008US; 2 MPN-PENDING with direct rows: Legion 5i 83LY0000US, IdeaPad 5 83GH000AUS; 1 flagged lenovo.com-only: X1 Carbon 21NS0012US). **UPC verified: 0** — every UPC in this sweep is single-source or no-lead.
- **Backlog: 7** (B1 Pro 7 83RU0002US, B2 Yoga Slim 7x 83QR000AUS, B3 T14 Gen 6 21QJ00CSUS, B4 T16 21QN0045US, B5 LOQ 83VA001PUS, B6 T14 Gen 5 Gray 21MC000NUS, B7 ThinkVision P27u-20).
- **Draft corrections:** drop entry 39 (Legion Pro 5 83DF00A8US — row dead); entry 40 (T14 Gen 6) moves to backlog (verified MPN, no direct row); entry 3 (X1 Carbon) stays as the single flagged lenovo.com-only pick, with its MPN now two-sourced (lenovo.com + Newegg, bot-wall caveat).
- **Net recommendation:** carry the 7 picks above (Lenovo contributes 7 of the 50 batch-6 slots, not 10); leave the remaining 3 Lenovo slots to the Samsung/ASUS sweeps. Strongest next-up if a slot opens: B2 Yoga Slim 7x (one second source away from a pick) and B1 Legion Pro 7 (lenovo-only, needs a retailer row).
