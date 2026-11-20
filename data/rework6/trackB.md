# Track B — Razer / Anker / Garmin second-source re-probes (batch-6 rework)

- **Date observed:** 2026-11-20
- **Scope:** 11 models from `data/candidates_batch6_500.md` (catalog 450 → 500). Second-source re-probes only.
- **Method:** `browser.search` + `browser.open` (text fetch only). No live browser, no purchases, no sign-ins.
- **Rules applied:** US-market models only; seller-direct or retailer-direct only; no Amazon as a source in any form; no eBay; no marketplace/third-party sellers. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant. Qualifying sources: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, Newegg spec page, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators (Snapklik, Desertcart, Ubuy, Klarna, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. No identifier was invented; each source page was checked to name the same model/variant.
- **Best Buy seller note:** where a Best Buy price/stock is captured, the seller is recorded — "sold & shipped by" a marketplace seller (6ave Electronics, Electronic Express, FrontRow Tech) is NOT a direct row.

## Method caveats (read before using the verdicts)

1. **Newegg bot wall (2026-11-20):** a direct open of a Newegg spec page hit a bot wall/CAPTCHA. The Newegg confirmation for model #8 (Anker Prime A2669) therefore rests on the search fetch of its spec page, not a direct open — flagged again at #8.
2. **Micro Center Huntsman (#5):** the Micro Center spec print for the Huntsman V3 Pro Mini exists only as a search snippet (Mfr Part# shown truncated, see #5). A direct open of the Micro Center product page on 2026-11-20 returned only return-policy text plus a JSON-LD price — the spec panel did NOT reproduce in the fetched text. Per the strict rule (snippets alone are not qualifying), the Micro Center leg cannot support a VERIFIED verdict for #5. The MPN is therefore PENDING, not VERIFIED, despite the snippet corroboration.
3. **Distributor status (#9 Venu 3S):** the two UPC sources for the Venu 3S are distributors (Petra, CompSource). Whether they count as "authorized distributor spec" under the task rules is uncertain. The UPC is scored PENDING, with the conditional noted at #9: if the catalog owner accepts Petra + CompSource as authorized distributors, the UPC would be VERIFIED.
4. **Klarna is an aggregator, not a source:** a Klarna listing showing a Newegg offer for the Boom 2 Plus (#6) is recorded only as a pointer for a possible future Newegg spec-page fetch; it does not count toward verification.

---

## 1. Razer Kiyo Pro Ultra 4K Black

- **Draft lead:** MPN RZ19-04420100-R3U1 (Best Buy only). UPC lead 840272900376 CONFLICTED.
- **Best Buy (qualifying retailer):** product page — Model: RZ19-04420100-R3U1, SKU 11132802, $429.99 → $429.95, InStock — **but sold & shipped by 6ave Electronics (marketplace, NOT Best Buy direct)**. Not a direct row.
- **Second qualifying MPN source — NOT FOUND.** B&H search returned only the non-Ultra Kiyo Pro (RZ19-03640100-R3U1). Abt search returned no Abt listing. Micro Center search returned no listing. Razer.com page exists but fetched text prints no MPN. A Newegg-targeted search on 2026-11-20 returned no Newegg listing.
- **Non-qualifying corroboration of the MPN (does not count):** Amazon ASIN B0CT6FFK4R (Item model number RZ19-04420100-R3U1); Snapklik (Model RZ19-04420100-R3U1); ProductDome (Model RZ19-04420100-R3U1; states its product data comes from public Amazon listings). Walmart $399.99 listing is labeled "(International Model)" — not a US-market direct row. ShopAbunda listing is fulfilled by 6ave.
- **UPC 840272900376 — CONFLICT UNRESOLVED.** Amazon + Snapklik (both non-qualifying) tie it to RZ19-04420100-R3U1 (Ultra). eBay listings (non-qualifying) tie 0840272900376 to the Kiyo Pro, MPN RZ19-03640100-R3U1 — but those listings are internally inconsistent (title says "Kiyo Pro Ultra", MPN field says Kiyo Pro; one listing prints both MPNs), which reads as seller conflation, not evidence. The B&H Kiyo Pro spec page (opened 2026-11-20) prints NO UPC for either model. **No qualifying retailer spec page ties the UPC to either model**, so per the strict rule the conflict stays unresolved. Neither attribution is verified.
- **Verdicts:** MPN RZ19-04420100-R3U1 — **PENDING + lead (Best Buy only)**. UPC 840272900376 — **CONFLICT UNRESOLVED** (no qualifying source).
- **Price/stock:** Best Buy $429.95 InStock via 6ave Electronics (marketplace); Amazon bundle listing shows a variant model number RZ19-04420100-R3U1_AG3_1 (bundle suffix, not the standalone MPN).

## 2. Razer Kiyo V2 Pro Black

- **Draft lead:** none (no MPN, no UPC). New Razer flagship webcam, announced 2026-09-24.
- **Razer.com (brand official, opened 2026-11-20):** Kiyo V2 Pro, $299.99, InStock, 4K 60FPS. Page text prints **no MPN and no UPC**.
- **Best Buy direct row — NONE FOUND.** Best Buy search for "Kiyo V2 Pro" returns only the Kiyo Pro Ultra. No B&H listing found. Newegg search found no listing.
- **Non-qualifying leads only (do not count):** eBay + Ubuy give MPN RZ19-05360100-R3U1, UPC 840272918661. EU variant is RZ19-05360100-R3M1 (24.lv, Latvia). ASIN B0FNBGBJ12.
- **Verdicts:** MPN — **NO LEAD (qualifying)**. UPC — **NO LEAD (qualifying)**. Best Buy row — **none found**.
- **Price/stock:** Razer.com $299.99 InStock.

## 3. Razer BlackShark V3 Black (PC version)

- **Draft lead:** none.
- **Best Buy (qualifying retailer):** product page — Model: RZ04-05410100-R3U1, SKU 12588192 (a second Best Buy SKU 6632891 appears in search snippets). $129.99, InStock — currently **sold & shipped by Electronic Express (marketplace)**; an older crawl said "Sold by Best Buy". Not currently a direct row.
- **Newegg (qualifying retailer):** listing — Model # RZ04-05410100-R3U1, Item # 9SIA1CZKVW4952, $129.99.
- **Razer.com (brand official):** BlackShark V3, $149.99, InStock. Page prints no MPN.
- **Verdict — MPN RZ04-05410100-R3U1: VERIFIED** (Best Buy + Newegg agree).
- **UPC 840272919606 — NO LEAD (qualifying).** Appears only on Amazon / eBay / HeadphoneTune (all non-qualifying). No qualifying spec page prints it.
- **Price/stock:** Best Buy $129.99 InStock (via Electronic Express); Newegg $129.99; Razer.com $149.99 InStock.
- **Do not mix:** V3 Pro is RZ04-05400100-R3U1 (PC) / RZ04-04530100-R3U1 (Xbox); V3 X HyperSpeed is RZ04-05420100-R3U1 / R3M1; EU variant of the V3 is RZ04-05410100-R3M1 (Scan UK, LDLC, Microless).

## 4. Razer Cobra wired Black

- **Draft lead:** MPN RZ01-04650100-R3U1 (Best Buy only).
- **Best Buy (qualifying retailer):** product page — Model: RZ01-04650100-R3U1.
- **B&H (qualifying retailer, spec page opened 2026-11-20):** BH # RA0104650100, MFR # RZ01-04650100-R3U1. Live price $29.99; search snippets showed $34.95 / $34.99 with In Stock / BackOrder varying across crawls.
- **Verdict — MPN RZ01-04650100-R3U1: VERIFIED** (Best Buy + B&H spec page agree).
- **UPC 840272903049 — PENDING + lead (ChannelOnline only).** ChannelOnline distributor listing prints Part # RZ01-04650100-R3U1 + UPC 0840272903049 — one arguably-qualifying (authorized distributor spec) source. eBay / Desertcart also print it (non-qualifying). The B&H spec page fetched text prints no UPC. No second qualifying UPC source found.
- **Price/stock:** B&H $29.99 (live; snippets $34.95–$34.99).
- **Do not mix:** Pokémon edition RZ01-04650400-R3M1 is a different model.

## 5. Razer Huntsman V3 Pro Mini 60% Black (standard, NOT 8KHz)

- **Draft lead:** none.
- **Best Buy (qualifying retailer, page opened 2026-11-20):** Model: RZ03-04990200-R3U1, SKU 6558755, **Sold by Best Buy**, $124.99 Black Friday (comp. value $179.99), InStock. A direct row.
- **Micro Center (qualifying retailer) — snippet only, see caveat 2:** search snippet for product id 670527, SKU 615450 — Mfr Part# shown **truncated as "RZ03-04990200-R"** in the snippet, UPC 840272909409, Keyboard Color Black, 60%, $139.99–$159.99 InStock. A direct open of the Micro Center product page on 2026-11-20 returned only return-policy text plus JSON-LD (Price $139.99, InStoreOnly) — the spec panel did not reproduce, so the full MPN print and the UPC print from Micro Center are **not confirmed by direct open**.
- **Verdict — MPN RZ03-04990200-R3U1: PENDING + lead (Best Buy only as a full print).** Micro Center's snippet corroborates the MPN prefix and the UPC, but a truncated snippet cannot carry a VERIFIED verdict under the strict rule. A clean second full print is still wanted.
- **Verdict — UPC 840272909409: PENDING + lead (Micro Center snippet only as the qualifying source).** eBay / PayMore / Ubuy / Desertcart also print it (non-qualifying). No second qualifying UPC source found.
- **Price/stock:** Best Buy $124.99 InStock (Sold by Best Buy); Micro Center $139.99 InStoreOnly.
- **Do not mix:** the 8KHz version is newer (Razer.com $179.99–$249.99); UK variant RZ03-04990300-R3W1; APAC RZ03-04990100-R3M1; renewed RZ03-04990200-R3UR.

## 6. Anker Soundcore Boom 2 Plus Black (Phantom Black)

- **Draft lead:** MPN A3134012 (single source).
- **Best Buy (qualifying retailer):** Model: A3134012, SKU 6683800, **Sold by Best Buy**, $249.99, **Sold Out**.
- **soundcore.com (brand official):** Boom 2 Plus product page URL contains "a3134"; Phantom Black listed at $159.99 (sale) / $249.99. Page text does **not** print A3134012.
- **Second qualifying MPN source — NOT FOUND.** Abt search returned only Ubuy (non-qualifying). B&H search returned no B&H listing. Klarna (aggregator, non-qualifying) shows a Newegg offer for the Boom 2 Plus at $249.99, but no Newegg spec page was fetched — direct Newegg opens were bot-walled in this session — so Newegg is an unconfirmed pointer only, not a source.
- **Verdict — MPN A3134012: PENDING + lead (Best Buy only).**
- **UPC — NO LEAD (qualifying).** Ubuy (non-qualifying) shows three conflicting UPCs by color — 194644038885, 194644038922, 194644038960 — with no reliable attribution to Phantom Black.
- **Price/stock:** Best Buy $249.99 Sold Out; Best Buy bundle with Nano Pro charger $174.99 InStock (bundle model A3134012*1+A2637117*1 — a different listing); soundcore.com $159.99 sale.

## 7. Anker Soundcore AeroFit 2 Black (base model)

- **Draft lead:** none.
- **B&H (qualifying retailer, spec page):** MPN A3874Z11, UPC 194644036393, Color Black, $79.99 InStock.
- **Crutchfield (qualifying retailer):** Item # 318A3874Z1, MFR # A3874Z11, Black.
- **Verdict — MPN A3874Z11: VERIFIED** (B&H spec page + Crutchfield agree).
- **Verdict — UPC 194644036393: PENDING + lead (B&H only qualifying source printing it).** Micro Center Black page (product 694960) opened 2026-11-20 but the fetch returned a support page with no Mfr Part # / UPC; price $69.99 InStock (was $79.99 in snippets). Micro Center Green variant is a different color: Mfr Part # A3874Z61, UPC 194644210144.
- **Price/stock:** B&H $79.99 InStock; Micro Center $69.99 InStock; soundcore.com $129.99 list.
- **Do not mix:** AI Assistant version A3874Z12 Obsidian Black is a different listing.

## 8. Anker Prime 67W GaN Wall Charger 3-port

- **Draft lead:** MPN A2669 (Anker.com only).
- **Anker.com (brand official):** Model Number: A2669, $49.99 InStock.
- **Newegg (qualifying retailer):** spec page (search fetch) — Model Number A2669. **Caveat:** a direct open of the Newegg page hit the Newegg bot wall on 2026-11-20, so the Newegg leg rests on the search fetch of its spec page, not a direct open.
- **Verdict — MPN A2669: VERIFIED** (Anker.com + Newegg spec page agree).
- **UPC 194644137373 — NO LEAD (qualifying).** Appears only on Amazon / eBay / Ubuy (non-qualifying). B&H search returned no B&H listing. Conflicting non-qualifying UPCs also seen: 194644137359 (Jumia), 0194644136406 (eBay, different listing). The Rakuten product URL digits 00194644137373 are **NOT** a verified identifier (per task rule — URL digits do not count; at most a consistency note that they are the GTIN-14 form of the same digits).
- **Price/stock:** Anker.com $49.99 InStock.

## 9. Garmin Venu 3S Pebble Gray 41mm

- **Draft lead:** none.
- **Best Buy (qualifying retailer, page opened 2026-11-20):** Model: 010-02785-00, SKU 6551502, **Sold by Best Buy**, $299.99 InStock, comp. value $449.99. A direct row. Best Buy spec panel fetched text prints no UPC.
- **Crutchfield (qualifying retailer):** Venu 3S 010-02785-00, Slate Steel bezel / Pebble Gray case and band.
- **Verdict — MPN 010-02785-00: VERIFIED** (Best Buy + Crutchfield agree).
- **UPC 753759314774 — PENDING + lead (distributors only).** Petra (distributor): Vendor SKU 010-02785-00, UPC 753759314774, Retail Price $449.99, "Slate Bezel with Pebble Gray Case". CompSource (distributor): MPN 010-02785-00, UPC/EAN 753759314774, MARKET: US, $494.99. **Caveat:** both are distributors; whether they count as "authorized distributor spec" is uncertain — if the catalog owner accepts them, the UPC would be VERIFIED (two distributor sources agree). No Abt listing found (search 2026-11-20). Non-qualifying corroboration: HeartRateMonitorsUSA table (010-02785-00 / 753759314774), eBay, Visions Canada, PB Tech NZ.
- **Price/stock:** Best Buy $299.99 InStock (Sold by Best Buy); Sportsman's $449.99; Petra retail $449.99; CompSource $494.99.
- **Do not mix:** Venu 3 45mm is a different model (e.g. 010-02784-00 / 010-02784-01).

## 10. Garmin Approach S44 Black

- **Draft lead:** MPN 010-03009-00 (Staples listing via Klarna only).
- **Abt (qualifying retailer, reviews page):** Model # 010-03009-00, UPC # 753759350666, "Silver Aluminum with Black Silicone Band". (Reviews page; no price captured from it.)
- **Garmin.com (brand official):** forum link confirms garmin.com/en-US/p/1604358/pn/010-03009-00 for the Approach S44 Black.
- **Verdict — MPN 010-03009-00: VERIFIED** (Abt + Garmin.com agree). Also: Staples listing (Black Silicone Band, 010-03009-00, $316.79, LimitedAvailability) and a Best Buy bundle Model 010-03009-00_AG2-1 (marketplace 6ave, $304.95).
- **Verdict — UPC 753759350666: PENDING + lead (Abt only qualifying source printing it).** Second qualifying source not found: Crutchfield search returned only the Twilight variant 010-03009-01; B&H search returned no B&H listing. Non-qualifying corroboration: CampSaver (MPN + UPC), HeartRateMonitorsUSA table, Amazon.
- **Price/stock:** $249.99 at several retailers (HeartRateMonitorsUSA, Kohl's, PlayBetter) vs $299.99 list; Staples $316.79 LimitedAvailability.
- **Do not mix:** Twilight variant is 010-03009-01, UPC 753759350673 — different model.

## 11. Garmin Edge 1040 Solar Black

- **Draft lead:** none.
- **Best Buy (qualifying retailer):** Model: 010-02503-20, SKU 13144387, $599.99 InStock — **sold & shipped by FrontRow Tech, an Authorized Dealer marketplace seller**. Not a direct row.
- **buy.garmin.com (brand official store, cart page):** Edge 1040 Solar, Device Only, 010-02503-20, $649.99, ships in 2–3 weeks.
- **Verdict — MPN 010-02503-20: VERIFIED** (Best Buy + Garmin official store agree).
- **UPC 753759279752 — NO LEAD (qualifying).** Appears only at bike shops (Holland Bicycles, Tree Fort Bikes, Worldwide Cyclery, etc. — many sharing one platform template), Summit Racing (MPN + UPC, but an auto-parts retailer, not in the qualifying list), and Snapklik (aggregator). No B&H / Abt / Micro Center / Crutchfield / Newegg / brand spec page prints it.
- **Price/stock:** Garmin.com $649.99 (ships in 2–3 weeks); Best Buy $599.99 via FrontRow Tech; MSRP $699.99.
- **Do not mix:** non-Solar Edge 1040 is 010-02503-00 — different listing. Edge 1050 is a different model. No part number was guessed; 010-02503-20 is what the sources print.

---

## Scoreboard

| # | Model | MPN | UPC |
|---|-------|-----|-----|
| 1 | Razer Kiyo Pro Ultra 4K Black | PENDING — RZ19-04420100-R3U1 (Best Buy only) | **CONFLICT UNRESOLVED** — 840272900376 (no qualifying source ties it to either model) |
| 2 | Razer Kiyo V2 Pro Black | NO LEAD | NO LEAD (non-qualifying: RZ19-05360100-R3U1 / 840272918661) |
| 3 | Razer BlackShark V3 Black (PC) | **VERIFIED** — RZ04-05410100-R3U1 (Best Buy + Newegg) | NO LEAD (non-qualifying: 840272919606) |
| 4 | Razer Cobra wired Black | **VERIFIED** — RZ01-04650100-R3U1 (Best Buy + B&H) | PENDING — 840272903049 (ChannelOnline only) |
| 5 | Razer Huntsman V3 Pro Mini 60% Black | PENDING — RZ03-04990200-R3U1 (Best Buy full print; Micro Center snippet truncated) | PENDING — 840272909409 (Micro Center snippet only) |
| 6 | Anker Soundcore Boom 2 Plus Black | PENDING — A3134012 (Best Buy only) | NO LEAD (non-qualifying: 3 conflicting Ubuy values) |
| 7 | Anker Soundcore AeroFit 2 Black | **VERIFIED** — A3874Z11 (B&H + Crutchfield) | PENDING — 194644036393 (B&H only) |
| 8 | Anker Prime 67W GaN Wall Charger 3-port | **VERIFIED** — A2669 (Anker.com + Newegg, search-fetch leg) | NO LEAD (non-qualifying: 194644137373) |
| 9 | Garmin Venu 3S Pebble Gray 41mm | **VERIFIED** — 010-02785-00 (Best Buy + Crutchfield) | PENDING — 753759314774 (Petra + CompSource; distributor status uncertain — see #9) |
| 10 | Garmin Approach S44 Black | **VERIFIED** — 010-03009-00 (Abt + Garmin.com) | PENDING — 753759350666 (Abt only) |
| 11 | Garmin Edge 1040 Solar Black | **VERIFIED** — 010-02503-20 (Best Buy + buy.garmin.com) | NO LEAD (non-qualifying: 753759279752) |

**Totals:** MPN VERIFIED 7 (#3, #4, #7, #8, #9, #10, #11); MPN PENDING 3 (#1, #5, #6); MPN NO LEAD 1 (#2). UPC VERIFIED 0; UPC PENDING 5 (#4, #5, #7, #9, #10); UPC NO LEAD 5 (#2, #3, #6, #8, #11); UPC conflict unresolved 1 (#1).

## Suggested next probes (not run — for the parent / catalog owner to approve)

1. **#5 Huntsman:** re-open the Micro Center product page (670527) via a live browser or a fresh fetch to get a clean, full MPN + UPC print — that single step would likely move both identifiers to VERIFIED.
2. **#6 Boom 2 Plus:** fetch the Newegg spec page for the Boom 2 Plus (Klarna indicates Newegg carries it) — a Newegg print of A3134012 would verify the MPN; check whether it also prints a UPC.
3. **#9 Venu 3S:** catalog-owner decision — accept Petra + CompSource as authorized distributors (UPC → VERIFIED) or require a B&H/Abt/Crutchfield/Newegg/brand print.
4. **#1 Kiyo Pro Ultra:** a qualifying second MPN source was not found at B&H, Abt, Micro Center, Razer.com, or Newegg (search). The UPC conflict cannot be settled without a qualifying spec page printing 840272900376 against either MPN; B&H's Kiyo Pro page prints no UPC. No further obvious angle — leave PENDING / UNRESOLVED unless a new retailer route appears.
5. **#2 Kiyo V2 Pro:** too new for retailer spec pages as of 2026-11-20; re-probe B&H / Best Buy in a later sweep.
6. **UPC second sources still wanted for:** #4 Cobra, #7 AeroFit 2, #10 S44 (one qualifying print each so far); #3, #8, #11 have no qualifying UPC print at all.
