# Public Build Log (Build in Public)

This file is the vehicle for "open-sourcing the whole process": what was done at each step,
why, and how it turned out — recorded truthfully, including ugly numbers.

## 001 — 2026-10-31: Project kickoff

- Trigger: reading Stripe CEO Patrick Collison's 2026-10-09 long post (personal agents
  comparing prices for buyers, rewarding good products), and deciding to build the
  "price comparison" piece hands-on.
- Done today:
  - Repository skeleton: README / PLAN / ARCHITECTURE / DECISIONS / LICENSE / CONTRIBUTING
  - Minimal compare core + mock merchants + tests; `python3 -m price_agent.cli compare` runs
  - Five non-negotiable principles set (see DECISIONS 001–005)
- Current status: skeleton runs, merchants are mock data; real merchant integration not started.
- Pending: how to publish the public GitHub repository, first category, target market
  (defaults: United States + standardized electronics models).
- Next: Phase 1 same-product identifier normalization + landed total price + transparent bill;
  first define a 20-model eval set.

## 002 — 2026-10-31: Phase 1 kickoff (eval set + identifier matching + catalog snapshot)

- User said "start" without changing defaults: proceeding per DECISIONS 005 (US market,
  standardized electronics models).
- GitHub public repository created: https://github.com/enxi6/price-compare-agent (Public),
  13 Phase 0 files uploaded via the web UI; note that local git history and remote upload
  history are out of sync — Phase 1 uses local commits only, and the history difference must
  be handled before pushing (see pending items at the end).
- Done today:
  - 20-model eval set (`price_agent/catalog.py`): 6 identifiers verified (UPC/MPN per retailer
    or manufacturer pages, with variants pinned by color/version — XM5 black vs silver, AirPods
    Lightning vs USB-C, and MX Master 3S versions each have different UPCs; mixing them is an
    error); the other 14 identifiers left blank pending verification, never invented.
  - Identifier matching module (`price_agent/identity.py`): only identifier matches enter the
    main ranking; GTIN-14 and UPC-12 can match after normalization; title similarity goes to
    the suspected table only.
  - Tier-1 adapter (`price_agent/adapters_shopify.py`): Shopify store public product JSON
    endpoint; shipping/tax never invented (shipping unknown, tax 0); raises an error and stops
    when blocked; tests use stub data, no network.
  - Catalog snapshot (`data/eval_snapshots.json`, Meta Catalog collected 2026-10-31): 12 real
    quotes covering 5 verified models; Buds2 Pro white has no clean quote — a coverage gap,
    not $0. The catalog source provides no UPC, so all snapshot quotes land in the suspected
    table with 0 in the main ranking — the rule working as designed, not a bug; the next step
    needs a source that returns identifiers (official API/feed) to raise the match rate.
  - CLI gains `compare --model` and `eval`: `eval` now reports 20 models, 6 verified,
    5 with snapshots, 12 quotes, 0 matched, 12 suspected.
  - Tests grew from 8 to 18, all passing; also fixed the first commit accidentally including
    `__pycache__` (added .gitignore and removed it from the index).
  - Caught anti-gaming examples recorded in the snapshot's excluded_traps: T-Mobile's Bose
    $37.50 is a monthly-installment price, Switch bundles, refurbished units, color mismatches,
    and variant mismatches — ready-made Phase 2 anti-gaming cases.
- Ugly numbers recorded truthfully: 0% match rate, snapshot coverage 5/20, identifiers verified 6/20.
- Pending: how to merge local commits with the remote upload history (decide before pushing);
  Shopify adapter not yet connected to a real store (store domain and product handle must be
  verified first; URLs must not be guessed); 14 remaining model identifiers pending verification.

## 003 — 2026-10-31: First identifier-verification wave (6/7) + live-store CLI

- First wave of 7 models, 6 verified; verified total rises from 6 to 12:
  - WF-1000XM5 Black (WF1000XM5/B): UPC 027242925601 (Adorama + Amazon US + Abt + eBay agree;
    international and bundle UPCs differ and were excluded).
  - AirPods 4 USB-C (MXP63LL/A): UPC 195949688522 (Adorama + B&H + Amazon US agree;
    India version and ANC version are different products and were excluded).
  - Watch SE 2 40mm GPS Midnight (MXE93LL/A): UPC 195949641756 (Micro Center, single source;
    band size unconfirmed in the source and noted on the entry; other colors/bands/cellular/years
    each have different UPCs).
  - Kindle Paperwhite 16GB 2024 Black (B0CFPL6CFY): UPC 840268942847 (PBTech NZ/AU, single seller).
  - MX Keys S: correction — 920-011559 is Pale Grey, not Graphite (Graphite is 920-011406);
    entry renamed and pinned to Pale Grey, UPC 097855187857.
  - Switch Lite Turquoise (HDHSBAZAA): UPC 045496882266 (eBay + Desertcart + Ubuy agree;
    Canada refurbished code excluded).
  - Not verified: Keychron K8 Pro — the direct store uses SKUs (K8P-G1 etc.) rather than UPC,
    and SKUs vary by configuration; the K8 (non-Pro) UPC must not be reused; entry stays pending
    with the reason written down.
- CLI gains `compare --model … --shopify store/handle`: full chain from live-store public product
  JSON → identifier matching → ranking works; stops with an error when blocked, no workarounds.
- Keychron live-store endpoint verification handed to a read-only browser check (store
  www.keychron.com, handle keychron-k8-pro-qmk-via-wireless-mechanical-keyboard, from a search
  result URL); results to be logged when they return; this commit contains no unverified
  live-store claims.
- Tests still 18, all passing; eval now reports 20 models, 12 verified, 5 with snapshots,
  12 quotes, 0 matched, 12 suspected.
- Pending: second wave of 7 model identifiers; Keychron endpoint verification result; local vs
  remote history merge.

## 004 — 2026-10-31: Second identifier-verification wave (6/7), eval set 18/20

- Second wave of 7 models, 6 verified; verified total rises from 12 to 18:
  - Xbox Wireless Controller Carbon Black Series X|S (1914): UPC 196388518159 (PayMore + eBay
    agree; the older QAT-00001 code and another PayMore code excluded as different versions).
  - Quest 3S 128GB (SK-1000926-01): UPC 815820025825 (B&H + Amazon US + PayMore agree;
    Singapore, New Zealand, and refurbished SKUs each differ).
  - Anker 737 120W US plug (A2148): UPC 194644099008 (Swiftsly + Ubuy agree;
    EAN 0194644099008 is the same code in GTIN form; the UK-plug version is a different reference).
  - Magic Mouse USB-C White (MXK53AM/A): UPC 195949655883 (Apple official;
    NZ code and Black version excluded).
  - G Pro X Superlight 2 Black (910-006630): EAN 5099206104525 (multiple EU retailers agree;
    US UPC not separately confirmed, so the GTIN-family EAN is used; 910-006631 differs only in
    regional packaging).
  - Pixel Buds Pro 2 Porcelain US (GA05760-US): UPC 840244604448 (B&H + DirectDial agree;
    the 840244604516 group and AU code are other regional versions).
  - Not verified: DualSense White — three-way UPC conflict (Amazon US 711719574293, NZ/AU
    PBTech 711719575856, other 711719541080); no clean consistent value, so left blank pending
    a second check against a US manufacturer/retailer page.
- Eval set remaining pending: only 2 — Keychron K8 Pro (SKU-based) and DualSense White (UPC conflict).
- Tests still 18, all passing; eval now reports 20 models, 18 verified (snapshot quotes still
  12, matches still 0, because newly verified models have no snapshot quotes yet — identifiers
  are ready, the next step is adding quote sources for them).
- Keychron endpoint browser verification result still not returned; still blocked — no chasing,
  no duplicate dispatch.

## 005 — 2026-10-31: Keychron live-store endpoint verified, eval set 19/20

- Read-only browser verification (nothing added to cart, no sign-in, no purchase): Keychron's
  official-store public product JSON (keychron-k8-pro-qmk-via-wireless-mechanical-keyboard)
  loads fine with no blocking; title Keychron K8 Pro QMK/VIA Wireless Mechanical Keyboard,
  31 variants in total.
- Key correction: the earlier statement "Keychron uses SKUs, not UPC" was wrong — every variant
  in the JSON carries a barcode, e.g. K8P-G1 (Black, Fully Assembled Hot-Swappable, White
  Backlight, Gateron G Pro Red) barcode 4895248806837, K8P-G2 4895248806844. The K8 Pro entry
  is now pinned to the K8P-G1 configuration and promoted to verified; verified total rises to
  19/20, leaving only DualSense White (UPC conflict).
- One real bug: the endpoint's variant objects carry no available field; the old adapter logic
  treated a missing field as out of stock, sinking all variants to the bottom. Fixed: a missing
  field = stock not asserted (treated as listed), with the CLI live-store path printing a note
  that stock must be verified on the product page; regression test added.
- Tests grew from 18 to 19, all passing.
- Pending: DualSense White UPC conflict second check; local vs remote history merge.

## 007 — 2026-10-31: Apple model cluster joins the eval set (8/8 verified)

- After user approval, 8 Apple models added, each pinned to a base configuration + color part
  number; eval set grows from 20 to 28, verified from 19 to 27, leaving only DualSense White pending:
  - MacBook Air 13 M4 Starlight (MW0Y3LL/A): UPC 195949837197
    (eBay + Bestpeek agree; Best Buy US confirms the MPN).
  - MacBook Air 15 M4 Sky Blue (MC7A4LL/A): UPC 195949893162 (two distinct eBay listings agree).
  - MacBook Pro 14 M4 Space Black (MW2U3LL/A): UPC 195949507786
    (two distinct eBay listings + Back Market agree; UK/AU suffixes are regional).
  - Mac mini M4 (MU9D3LL/A): UPC 195949080296 (many distinct listings agree).
  - iPad A16 Silver (MD3Y4LL/A): UPC 195950086232 (Best Buy bundle pages + eBay agree).
  - iPad Air M3 Purple (MCA04LL/A): UPC 195949997952 (two distinct listings agree).
  - iPad Pro M4 Space Black (MVV83LL/A): UPC 195949222467 (many distinct listings agree).
  - AirPods Max USB-C Midnight (MWW43AM/A): UPC 195949543890
    (Best Buy US + many eBay listings agree; another code from an eBay catalog page excluded).
- Lesson of this wave: for Apple, color = a different part number, so entries must pin color;
  Wi-Fi + Cellular versions, the Lightning version, and regional-suffix versions are all different
  SKUs and were excluded in the source notes.
- iPhone still excluded (carrier financing / network lock makes "cheapest" non-comparable);
  an Apple showcase page is deferred to Phase 4; next step is adding quote sources for the Apple
  cluster (Apple's own site, Amazon, and Best Buy are not Shopify — new adapters needed).

## 008 — 2026-10-31: Apple quote-source first test — Meta Catalog is not enough

- Ran Meta Catalog against the 8 Apple part numbers: 50 results, only 3 survive curation into
  the snapshot (data/eval_snapshots_apple.json; eval: 28 models, 3 with quotes):
  iPad A16 Silver Abt $427, iPad Pro M4 Space Black Staples $1,023.99,
  AirPods Max Midnight P.C. Richard $449.98.
- Excluded traps and new findings of this wave: PayMore storefront quotes whose condition is not
  asserted as new (suspected used/refurbished) all excluded; open-box, drop-shippers, and
  non-US merchants excluded; M5-generation MacBooks are already out, so M4 entries are
  previous-generation and their clearance-price context differs; MacBook Air/Pro M4 base configs
  and iPad Air M3 Purple 128GB have 0 clean new-unit quotes in this batch — a coverage gap,
  not a price signal.
- Conclusion: Meta Catalog alone cannot carry Apple new-unit pricing; the real adapter work
  (Best Buy / B&H / Amazon official channels or browser read-only verification) is still pending;
  snapshot quotes all carry identifier=None and by rule can only enter the suspected table.
- Pending: DualSense White UPC conflict second check; local vs remote history merge.

## 009 — 2026-10-31: Retailer-page check — M4 Air 13 discontinued as new

- Read-only browser check (nothing added to cart, no sign-in, no purchase; both sites reachable,
  no blocking): MacBook Air 13 M4 Starlight (MW0Y3LL/A) shows as no longer sold new at both
  Best Buy US and B&H (Best Buy: "no longer available in new condition";
  B&H: "No Longer Available", noting a used model exists, which is not cited under the
  new-unit criterion).
- Significance: M4 entries' live new-unit quote coverage at major retailers will naturally decay,
  which explains part of the gap in 008; adapters must be able to express the "discontinued"
  state rather than going silent when no price is available or substituting a similar model.
  M5 prices appearing on B&H search pages must never be mixed into this SKU.
- Next: re-test with a current model (iPad A16 Silver MD3Y4LL/A) at the same two stores to verify
  whether the adapter pattern holds on an in-stock SKU; whether M4 entries become clearance
  tracking or gain M5 successors is for the user to decide.

## 010 — 2026-10-31: Current-model re-test passes — iPad A16 $399 at both stores

- Read-only browser re-test (nothing added to cart, no sign-in, no purchase; both sites
  reachable, no blocking): iPad A16 Silver 128GB Wi-Fi (MD3Y4LL/A) new standalone units are $399
  at both Best Buy and B&H (comparable value $449, saving $50), both in stock; Best Buy free
  shipping is the browser-location rate (not the user's address); B&H shipping is charged
  separately and the delivered total was not verified (no checkout entered).
- Excluded confounders: the 256GB model at $499, open-box/refurbished price ranges, and B&H's
  AppleCare+ bundle at $478 — none mixed into the standalone price. The B&H quote is noted as
  ending 10-31 23:59 ET, limited quantity — a promotional price, not an everyday price.
- Snapshot updated (data/eval_snapshots_apple.json; eval: 3 with quotes, 5 quotes total):
  iPad A16 compare output shows Best Buy $399 = B&H $399 tied, Abt $427; because catalog sources
  provide no UPC, snapshot quotes can still only enter the suspected table — the rule working.
- Conclusion: retailer pages as browser-verified quote sources (Tier 4) hold on current SKUs;
  but turning HTML scraping into automatic adapters is fragile and risks tripping retailer
  limits, so no Best Buy/B&H scraper adapters are built at this stage — snapshots + browser
  verification are the right shape for this tier. Automatic fetching must go through official
  channels (requiring API access) — a separate decision.

## 011 — 2026-10-31: Apple cluster refreshed — discontinued generations replaced with current models

- User-confirmed replacement list (DECISIONS 006: in-sale new products only;
  9 replaced, 3 kept; eval set still 28 models, verified identifiers 27 -> 26):
  - MacBook Air 13 M4 Starlight MW0Y3LL/A -> M5 13 Midnight MDHE4LL/A,
    UPC 195950690200 (Best Buy US SKU 6397846 + B&H agree).
  - MacBook Air 15 M4 Sky Blue MC7A4LL/A -> M5 15 Midnight MDVH4LL/A,
    UPC 195950697087 (Best Buy US SKU 6571043 + eBay listings).
  - MacBook Pro 14 M4 Space Black MW2U3LL/A -> M6 14 Space Black MHWT4LL/A,
    16GB/1TB, $1,999, pre-order shipping 2026-11-06; UPC not yet published,
    so the entry stays pending with empty identifiers (never matched)
    until a retailer listing states the UPC. User chose the M6 base over
    the in-stock M5 24GB/1TB (MDE34LL/A, Best Buy $2,049).
  - Mac mini M4 MU9D3LL/A -> M6 MHQK4LL/A, UPC 195951021089 (Adorama spec
    table, single source; Best Buy US SKU 6566933 confirms the MPN).
  - iPad Air M3 Purple MCA04LL/A -> M4 11 Space Gray MH304LL/A,
    UPC 195950823578 (eBay US + Amazon-derived listings; Best Buy US
    SKU 6586895 confirms the MPN; OnBuy code 195950823516 excluded as a
    suspected non-US variant).
  - iPad Pro M4 Space Black MVV83LL/A -> M5 11 Space Black MDWK4LL/A,
    UPC 195950395419 (Micro Center SKU 941617 + multiple listings;
    single-seller eBay code 195950391077 excluded).
  - AirPods Max USB-C Midnight MWW43AM/A -> AirPods Max 2 Midnight MHWK4AM/A,
    UPC 195951039060 (Abt + Best Buy US SKU 6494847).
  - AirPods Pro 2 Lightning MQD83AM/A -> AirPods Pro 3 MFHP4LL/A,
    UPC 195950543698 (Best Buy US SKU 6376563 + eBay GTIN agree).
  - Watch SE 2 40mm GPS Midnight MXE93LL/A -> Watch SE 3 GPS 40mm Midnight
    MEH94LW/A, UPC 195950387070 (multiple eBay listings agree; Best Buy's
    current GPS 40mm Midnight listings are Navy Blue band variants, band
    detail to pin at snapshot time).
  - Kept (still current): iPad A16 Silver MD3Y4LL/A, AirPods 4 MXP63LL/A
    (Best Buy in stock), Magic Mouse USB-C MXK53AM/A (Best Buy/B&H in stock).
- Keys renamed to the new generations (e.g. apple-macbook-air-13-m4 ->
  apple-macbook-air-13-m5) so old snapshot quotes cannot silently attach
  to new models. The Apple snapshot (data/eval_snapshots_apple.json) still
  holds quotes for the retired models and needs a fresh collection round
  for the new ones; it is dated evidence and was not edited here.
- Test update: test_eval_set_shape now expects 26 verified and pending ==
  {sony-dualsense-white, apple-macbook-pro-14-m6}.
- Non-Apple entries were not re-checked for discontinuation in this pass.
- Also fixed in passing: the catalog module docstring said 20 models (stale
  since the set grew to 28), and a stale "pending" section header above
  already-verified entries.

## 012 — 2026-10-31: Fresh quote collection for the new Apple generation

- First quote round for the 9 replacement + 3 kept Apple models (011 swapped the
  keys; the old Apple snapshot still holds retired-model quotes and was left
  untouched as dated evidence). New file: data/eval_snapshots_apple_2026-10-31.json.
- Method, same as 008/010: Meta Catalog first (2 batches, 100 raw listings),
  then read-only browser verification for the gaps. No cart, no sign-in, no
  checkout. URLs cleaned of fbclid/utm; shipping unknown, tax not included,
  stock not asserted by the snapshot.
- Result: 23 quotes across 11 of 12 Apple models. Per model:
  - Air 13 M5 Midnight: Abt $1,234, CDW $1,319 (Meta Catalog, authorized retailers).
  - Air 15 M5 Midnight: Best Buy $1,349 in stock, save $150 off $1,499 (browser).
  - Pro 14 M6 Space Black: Best Buy $1,999 PRE-ORDER, release 2026-11-06 (browser).
    The page is the exact config returned by searching Best Buy for MHWT4LL/A;
    the part number itself was not shown in the visible model field, and the
    free $100 e-gift card offer was not netted into the price.
  - Mac mini M6: Abt $899 (Meta Catalog).
  - iPad Air M4 Space Gray: B&H $699, Abt / RC Willey / Staples $749,
    Quill $823.99 (page-verified new standalone).
  - iPad Pro M5 Space Black: BJ's $1,099.99, Walmart $1,150, Staples $1,199,
    Quill $1,228.49.
  - AirPods Max 2 Midnight: Best Buy $499, Staples $549.
  - AirPods Pro 3: Staples $249.
  - iPad A16 Silver: Best Buy $399, B&H $399 (both promos ending 2026-10-31
    23:59 ET / "deal ends tomorrow" — valid at collection time, stale after 24h
    per snapshot rules), Abt $427.
  - AirPods 4: Abt $109.99, Staples $129.
  - Magic Mouse USB-C: Staples $79.
- Coverage gap, kept honest: Watch SE 3 (apple-watch-se3-40mm) has 0 quotes.
  Apple.com configurator shows $249 for a 40mm GPS Midnight case + S/M Sport
  Band, but the band is labeled "Navy Blue" there and MEH94LW/A is not displayed
  on the page, so the quote was NOT attached to the pinned entry. Best Buy's
  S/M and M/L Navy Blue variants are different part numbers and were not
  substituted. The pinned band-color mapping needs one part-number-level check.
- Rejected claims worth recording:
  - Quill catalog-feed iPad Air $600.99: the product page shows $823.99 new
    standalone. The feed price was not carried into the snapshot.
  - DataVision $898 mini / $249 Pro 3: excluded because the listings do not
    assert new condition (same rule as the PayMore storefronts in 008).
  - Non-US merchants (ar-lb.com, syscom.com.lb) and title/URL variant
    mismatches (Clemson "Midnight" title vs "Sky Blue" URL slug; sigmatiendas
    256GB title vs 512GB MDWM4LL/A URL) excluded.
- Verification: `eval --snapshot data/eval_snapshots_apple_2026-10-31.json`
  reports 28 models, 11 with snapshot quotes, 23 total quotes, 0 identifier
  matches (expected: snapshot offers carry identifier=None, so all 23 land in
  the suspected table, never the ranking). Tests: 19 passed.
- Still open: Watch SE 3 band mapping (above); M6 Pro UPC (pending until
  post-launch retailer pages show it); DualSense White UPC conflict.

## 013 — 2026-10-31: Non-Apple quote round — Phase 1 coverage now 25 of 28

- Same method as 012 (Meta Catalog 3 batches, 150 raw listings; Keychron
  official-store adapter; read-only browser verification; no cart, no sign-in).
  New file: data/eval_snapshots_nonapple_2026-10-31.json (18 quotes, 10 models).
  The 4 models already quoted in data/eval_snapshots.json (Sony XM5, Bose QC
  Ultra 2, Switch OLED, MX Master 3S, collected the same day) were not
  duplicated; all four are manufacturer-current, so the discontinuation check
  for them is today's own listings.
- Per model (new-unit, shipping unknown, tax excluded):
  - WF-1000XM5 Black: Suncoast Audio Direct $299.99.
  - DualSense White: PlayStation Direct $74, Kohl's / Macy's / GameStop /
    Best Buy $74.99 (5 quotes).
  - Xbox Carbon Black 1914: Newegg $49, MaxLevel $49.99.
  - Quest 3S 128GB: Abt / B&H $349.99 (four US retailers agree on $349.99;
    bundle, 256GB, Business, and refurbished rows excluded).
  - Switch Lite Turquoise: Walmart $229, NFM $229.99.
  - MX Keys S Pale Grey 920-011559: ThinkEdu $138.99 (the $109.99 "for Mac"
    row is 920-011622, a different SKU, excluded).
  - G Pro X Superlight 2 Black: Sweetwater / Logitech G direct $159.99
    (all DEX / SE / 2c variants and open-box excluded).
  - Kindle Paperwhite 16GB 2024 Black: Best Buy $199.99 — this resolves a
    feed conflict (the same Best Buy URL appeared at $199.99 and $229.99;
    the page shows $199.99 new standalone, $229.99 is marketplace range).
  - Pixel Buds Pro 2 Porcelain: Best Buy $169.00 (Holiday Deal, GA05760-US
    confirmed; the B&H $229.99 catalog row was the Hazel variant, excluded).
  - Keychron K8 Pro K8P-G1: official store $49.99 after a $25 discount off
    $74.99 list. The store CLI identifier-matched this variant (EAN
    4895248806837) — the only live identifier match so far; the snapshot
    format carries identifier=None, so it lands in the suspected table here.
    That is a format limitation, not a data problem.
- Three models still without quotes, each for a different stated reason:
  - Buds2 Pro White (SM-R510NZWAXAR): discontinued as new. B&H search says
    "no longer available", Best Buy shows only Buds3/Buds4 plus a sold-out
    refurbished Graphite unit, Samsung US has no model page. Per DECISIONS
    006 there is NO auto-swap: the replacement (Buds3 Pro? drop the entry?)
    needs a user decision. SM-R510NLVAXAR is a different regional suffix
    and was not substituted.
  - Anker 737 120W (A2148): gap, NOT declared discontinued. Not found on
    Anker US or Best Buy pages; Amazon US refused AI-agent access and was
    treated as unavailable, not bypassed. Needs one more check before any
    discontinuation claim.
  - Watch SE 3 (Apple): still 0 new-unit quotes, but the mapping question
    moved: a Best Buy refurbished listing displays MEH94LW/A for exactly
    GPS 40mm Midnight, S/M, Midnight Sport Band. Refurbished is excluded
    per DECISIONS 006, so this corroborates the mapping in the catalog
    notes without becoming a quote.
- Two identifier findings, neither silently resolved:
  - DualSense UPC conflict is now FOUR codes: the Best Buy spec-comparison
    table gives 711719023197 for the standard White column (other columns:
    Chroma Teal 711719022497, GTA VI LE 711719072683, 007 LE 711719027119).
    Entry stays pending; the tiebreaker (physical box barcode or a Sony
    spec sheet) is still missing. Catalog notes updated with all four.
  - G Pro X Superlight 2 SKU question: Logitech's US store URL for the
    $159.99 Black mouse shows 910-006628, while the eval entry pins
    910-006630 from EU retailers. Flagged in the snapshot traps, NOT
    changed in the catalog — the URL slug alone is not conclusive proof
    the US SKU differs.
- Verification: eval on the new file reports 10 models with quotes, 18 total
  quotes, 0 identifier matches (expected: snapshot offers carry no
  identifier). Combined coverage across the three snapshot files is now
  25 of 28 models (main 4 + Apple 11 + non-Apple 10). Tests: 19 passed.
  One self-inflicted syntax slip (a stray parenthesis in the catalog edit)
  was caught by the test run and fixed before commit.

## 014 — 2026-10-31: Buds2 Pro retired, Buds4 Pro White takes its place (user-confirmed)

- Trigger: BUILD_LOG 013 found the Buds2 Pro US white model discontinued as
  new. The user chose Buds4 Pro over Buds3 Pro and over dropping the entry
  (DECISIONS 009).
- New entry: samsung-buds4-pro-white — Galaxy Buds4 Pro, White, US version
  SM-R640NZWAXAR (released 2026-03-11, MSRP $249.99). Old key
  samsung-buds2-pro-white is retired, never reused; no quote carried over.
  No test referenced the old key, so no test change was needed.
- Identifier: UPC 198957273582, agreed by three sources — Best Buy spec
  page, a distributor catalog (GTIN 0198957273582, the same code), and
  T-Mobile's URL sku. Entry status: verified (26 verified identifiers
  maintained: one out, one in).
- Quotes (new file data/eval_snapshots_buds4pro_2026-10-31.json, 3 quotes):
  Samsung direct $249.99, B&H Photo $249.99, Abt $249.99. Excluded: a
  DataVision row whose title said White SM-R640NZWAXAR but whose URL slug
  said Black SM-R640NZKAXAR; an Ayoub $162 row with a truncated model
  code; the Amazon SM-R640NZWFXAR variant; MEA / Latino Americana
  suffixes; Buds4 non-Pro rows; open-box rows.
- Eval on the new file: 1 model with quotes, 3 total quotes, 0 identifier
  matches (expected, snapshot format). Combined coverage across all four
  snapshot files is now 26 of 28 models; still missing: Anker 737 (gap,
  not declared discontinued) and Watch SE 3 (0 new-unit quotes).
- Tests: 19 passed.

## 015 (2026-10-31): Superlight 2 US identifier corrected (DECISIONS 010)

- The eval entry pinned the European reference (910-006630 / EAN
  5099206104525). Re-checking against US sources: Abt (US) Model
  910-006628 + UPC 097855177797 + Black, DirectDial MFG part + UPC
  agreement, Best Buy Canada Model 910-006628 Black, Logitech G US store
  URL 910-006628. Entry corrected to MPN 910-006628 / UPC 097855177797;
  key unchanged; the two $159.99 quotes stand, and the Logitech G quote
  now identifier-matches its own entry instead of contradicting it.
- The superseded European reference stays recorded in DECISIONS 010, not
  deleted. The dated 2026-10-31 non-Apple snapshot file is left untouched
  (append-only record); its trap note describing the old flag is now
  historical.
- Tests: 19 passed (re-run after the edit).

## 016 (2026-10-31): Anker 737 re-check — still no qualifying US offer (DECISIONS pending)

- Meta Catalog (40 results, USD, Anker-restricted) returned two 737 rows
  worth checking: Ayoub Computers $99 and Newegg $158.58. Both failed
  browser verification 2026-10-31 20:09-20:11 PT (read-only, no cart):
  Ayoub is fulfilled from Lebanon with prices excluding 11% VAT, MPN
  A2148311 (not the pinned A2148111), plug type unstated — not a US
  offer. Newegg is third-party marketplace seller TECHVAULT shipping
  from China, no condition label, no MPN/UPC, title omits brand and
  color, brand-path mismatch, wrong category — excluded on five
  independent grounds.
- Supporting traces, none qualifying: ShopAbunda lists the charger but
  out of stock; Bluum (distributor) lists A2148111 with no price or
  stock asserted; Anker AU single unit sold out. The charger is alive
  internationally (EG/PK/BD/KE/MY/PT/AU listings) but no US new-unit
  offer qualifies as of 2026-10-31.
- Entry keeps 0 quotes. No auto-replacement per DECISIONS 006: the
  entry's fate (keep as documented gap / replace with a current Anker
  model / drop) is a user decision, requested 2026-10-31.
- DualSense note updated in the same round: fifth UPC code 711719541226
  (eBay + refurbished store); Amazon/Camel code 711719574293 tied to
  model CFI-ZCT1W. Still no tiebreaker; entry stays pending.
- Tests: 19 passed (re-run after the edits).

## 017 (2026-10-31): Watch SE 3 first new-unit quote — BJ's $239.99, mapping confirmed

- Meta Catalog (Apple-restricted, USD) returned the exact configuration;
  browser verification 2026-10-31 20:10-20:12 PT (read-only, no
  sign-in, no cart) confirmed: Apple Watch SE 3 (GPS) 40mm Midnight
  Aluminum Case with Midnight Sport Band - S/M, $239.99, Condition New,
  Model Number MEH94LW/A, UPC 195950387070. The price was visible to a
  non-signed-in visitor and not labeled member-only. This independently
  confirms the MEH94LW/A mapping that previously rested only on a
  refurbished listing, and confirms the entry's UPC.
- Fulfillment is mixed and recorded as such, not simplified: Free
  Shipping In Stock (3-5 business days); Pickup and Delivery sold out
  at the displayed club. Snapshot format carries identifier=None, so
  the quote lands in the suspected table; the MPN/UPC evidence is
  preserved in the offer title.
- Excluded in the same round: BrandsMart title-S/M vs URL-M/L
  mismatch; Apple.com MEHC4LW/A (M/L sibling); Clemson wrong product
  (44mm loop); an $8.34 garbage row; a $299.99 Navy Blue S/M row whose
  title omits GPS vs cellular while its price matches the cellular
  tier (ambiguous, not confirmed).
- New file data/eval_snapshots_watchse3_2026-10-31.json (1 quote).
  Combined coverage across all five snapshot files is now 27 of 28
  models; only Anker 737 still holds 0 quotes (fate pending user
  decision, BUILD_LOG 016).
- Tests: 19 passed (re-run after the edit).

## 018 (2026-10-31): Anker 737 replaced by Prime 100W (DECISIONS 012) — entry swap done, quote verification running

- Old entry anker-737-120w deleted from the catalog (Buds2 Pro
  precedent: retired keys are removed, never reused); new entry
  anker-prime-100w added with UPC 194644040635 / MPN A2688 (see
  DECISIONS 012 for the full identifier case). The dated snapshot
  files mentioning the 737 are left untouched (append-only record).
- The Prime 100W quote ($69.99, Anker direct + B&H, Meta Catalog)
  is held for browser verification of the Anker US page before it
  enters a snapshot file; this entry records the swap, and the
  snapshot + commit follow the verification result.

## 019 (2026-10-31): Prime 100W quote verified — Anker direct $69.99 in stock, swap complete

- Browser verification 2026-10-31 21:39-21:40 PT (read-only, no
  sign-in, no cart): Anker US page confirms Prime Charger 100W,
  3 ports (2 USB-C + 1 USB-A), GaN, Model A2688, $69.99, In Stock,
  delivery 3-7 business days. The page shows a $10 auto-applied-code
  promotion; the recorded price is the shown $69.99 with no further
  discount applied. No official color name appears on the page, so
  the variant carries no color; the page shows no UPC (the UPC comes
  from the multi-source agreement) and does not explicitly label
  condition (regular direct listing, separate from the Certified
  Refurbished promotion).
- New file data/eval_snapshots_ankerprime_2026-10-31.json (2 quotes:
  Anker direct $69.99, B&H $69.99). Combined coverage across all six
  snapshot files is now 28 of 28 models. The Anker 737 gap is closed
  by replacement, not by a new 737 offer.
- Tests: 19 passed (re-run after the edit).

## 020 (2026-10-31): Apple official-catalog sweep, first brand (DECISIONS 013)

- Read-only sweep of apple.com US regular store, 2026-10-31
  21:40-21:49 PT (no sign-in, no cart). One early click landed on
  the education store and was corrected; all prices below are
  regular-store prices. Pickup/delivery wording was for the
  browser's approximated location and is not recorded as a
  universal fact.
- Result: 10 of 12 entries CURRENT, 1 LISTED-PRE-ORDER, 1
  DISCONTINUED.
  - Current (Apple direct price, regular store): Air 13 M5 $1,299;
    Air 15 M5 $1,499; mini M6 $899; iPad A16 $449; iPad Air M4
    $749; iPad Pro M5 11 $1,199 (the entry pins 256GB Wi-Fi Space
    Black, exactly the configuration verified); Max 2 $549;
    Pro 3 $249; Watch SE 3 $249 (verification used Black Sport
    Band S/M; band is not part of the entry); Magic Mouse $79.
  - Listed, pre-order only: Pro 14 M6 $1,999, "Available starting
    11.6"; delivers/pickup from Nov 6. No UPC on the page, so the
    entry stays pending and the 2026-11-07 re-check stands.
  - Discontinued: AirPods 4 (MXP63LL/A). Its buy page redirects
    to the AirPods 5 page and its product page states it is no
    longer available on apple.com; the catalog lists only
    AirPods 5, Pro 3, Max 2. Replacement (AirPods 5) needs user
    confirmation per DECISIONS 013; no catalog change made yet.
- Method caveat, stated plainly: Apple buy pages for entries 1-11
  did NOT display part numbers, so this sweep confirms line /
  configuration currency, not MPN mappings. The one exception is
  Magic Mouse: its accessory page shows "UPC or EAN No.:
  195949655883", independently confirming that entry's
  identifier.
- Candidate lines observed (NOT approved additions): MacBook Neo
  from $699; Pro 14/16 PROLED XDR from $2,899 (pre-order 11.6);
  iMac from $1,499 (pre-order 11.6); Mac Studio from $2,499;
  Studio Display $1,599 / XDR $3,299; iPad Pro 13 from $1,499;
  iPad Air 13 from $949; iPad mini (new, A20 Pro) from $699
  (pre-order); Watch Series 12 from $399; Watch Ultra 4 from
  $799; AirPods 5 $129 (wireless charging case $149); Magic
  Trackpad $129 and Magic Keyboards $99-$199; Apple adapters
  and cables $19-$159; third-party accessories incl. Logitech
  MX Master 4 $119.95. iPhones were excluded from the sweep by
  scope (DECISIONS 006/013).

## 021 (2026-10-31): AirPods 4 replaced by AirPods 5 USB-C case (DECISIONS 014)

- Old entry apple-airpods-4-usbc deleted from the catalog (retired
  keys are removed, never reused); new entry apple-airpods-5-usbc
  added with UPC 195951378978 / MPN MKFW4LL/A (see DECISIONS 014
  for the identifier case). The dated Apple snapshot file
  mentioning AirPods 4 is left untouched (append-only record).
- New file data/eval_snapshots_airpods5_2026-10-31.json (3 quotes,
  all $129: Staples + Abt via Meta Catalog, Best Buy via search
  snippet — catalog-grade, page not browser-verified; Apple direct
  $129 from the apple.com sweep corroborates but is not a row,
  since no verified product URL for the USB-C case was found).
  Combined coverage stays 28 of 28 models.
- Tests: 19 passed (re-run after the edit).

## 022 (2026-10-31): Sony official-catalog sweep, second brand (DECISIONS 013)

- Read-only sweep of Sony Electronics US + PlayStation US, 2026-10-31
  22:51-22:55 PT (no sign-in, no cart). Sources reached through the
  sites' own navigation after first guessed URLs 404'd.
- Result: all 3 entries CURRENT.
  - WH-1000XM5 Black: current, Sony direct sale $228.00 (was
    $399.99). Direct-delivery shown out of stock at check time
    (email-me-when-available) — listing current, not Sony-direct
    availability; eval quotes come from retailers and are
    unaffected.
  - WF-1000XM5 Black: current, Sony direct sale $249.99 (was
    $329.99). Same direct-delivery out-of-stock note.
  - DualSense White: current, PlayStation Direct $74.00.
- DualSense identifier: still unresolved on official evidence. No
  official Sony/PlayStation page states a UPC, and none of the five
  conflicting codes appears on official pages. New partial evidence:
  PlayStation Support lists CFI-ZCT1W as a DualSense model code
  (manuals page + serial-number article), but neither page ties it
  to White or states a UPC — recorded in the entry notes as a
  general model-code confirmation, not a white-specific identifier
  and not a UPC resolution. Entry stays pending.
- Candidate lines observed (NOT approved additions): WH-1000XM6
  $459.99, WF-1000XM6 $329.99, WH-1000XM4C $299.99, ULT WEAR
  $249.99, LinkBuds Clip/Fit/Open $229.99, WH-CH720N $89.99,
  WF-C710N $129.99, WF-C510 $69.99, INZONE line, MDR pro line
  (MDR-7506 $114.99, MDR-M1 $269.99, MDR-MV1 $339.99); DualSense
  Edge $199, Access controller $89, PlayStation Portal $249,
  PS5 Pro $899, PS5 1TB $649, PS5 Digital 825GB $599, PULSE Elite
  $149, PULSE Explore $149, PULSE headset $99 (pre-order).
  Refurbished lines and third-party controllers on PlayStation
  Direct are excluded from candidacy by scope (DECISIONS 006).

## 023 (2026-10-31): Nintendo official-catalog sweep, fourth brand (DECISIONS 013)

- Read-only sweep of nintendo.com US, 2026-10-31 23:19-23:21 PT
  (no sign-in, no cart). Consoles + controllers families only;
  games, amiibo, cases, docks, chargers, cameras, and other
  accessories were out of scope.
- Result: both entries CURRENT.
  - Switch OLED White: $399.99, Add to cart shown, not sold out.
  - Switch Lite Turquoise: $229.99, Add to cart shown, not sold
    out.
- Candidate lines observed (NOT approved additions): Switch 2
  system $499.99; Switch 2 bundles $549.99 (Mario Kart World),
  $529.99 (Sports Resort), $519.99 (Zelda 40th, sold out); OLED
  Neon set $399.99; Switch Neon $339.99; Lite Yellow/Blue $229.99
  (Gray/Coral sold out); Switch 2 Pro Controller $89.99, Switch
  Pro Controller $79.99, Joy-Con 2 pairs $99.99, Joy-Con pairs
  $89.99, single Joy-Con $44.99-$54.99, retro controllers
  $34.99-$69.99; third-party controllers $22.99-$69.99.
  Refurbished variants are excluded from candidacy by scope
  (DECISIONS 006); controller grips/straps/wheels are accessories,
  not controllers. OLED Mario Red Edition $349.99 (sold out) was
  found via the product selector, not the main grid.

## 024 (2026-10-31): Logitech official-catalog sweep, third brand (DECISIONS 013)

- Read-only sweep of logitech.com + logitechg.com US, 2026-10-31
  23:19-23:23 PT (no sign-in, no cart). Catalogs walked in full:
  Mice 65 products, Keyboards 49, G Mice 23, G Keyboards 19.
  Many prices are LogiWork Deal Days special pricing through Nov 1
  11:59pm PDT (regular price in parentheses where shown).
  Webcams, headsets, and other families were out of scope.
- Result: 2 current, 1 not current as pinned.
  - MX Master 3S standard edition 910-006557: NOT CURRENT as a
    plain consumer model — absent from the 65-product Mice
    catalog; the line's current flagship is MX Master 4.
    Related variants still sold (different products, not
    equivalents): MX Master 3S Bluetooth Edition 910-007499
    ($79.99, reg $99.99, in stock) and MX Master 3S for Business
    ($109.99). Replacement decision pending user; no catalog
    change made yet.
  - MX Keys S pale grey 920-011559: CURRENT, $119.99 special
    (reg $129.99), in stock. Official spelling is "Pale Gray"
    vs the entry's "Pale Grey" — cosmetic, model matches.
  - Superlight 2 black 910-006628: CURRENT, $159.99, in stock.
    Specs confirm Black 910-006628 (White 910-006636, Magenta
    910-006795). UPC not displayed on the official page —
    unchanged (retailer agreement).
- Candidate lines observed (NOT approved additions): MX Master 4
  $119.99 (+ for Mac, Special Edition), MX Anywhere 3S $69.99,
  Lift $69.99, MX Vertical $99.99, G502 X PLUS $149.99,
  Superlight 2 DEX $159.99, Superstrike $179.99, MX Keys Mini
  $89.99, MX Mechanical $149.99, ERGO K860 $119.99, Wave Keys
  $69.99, POP Keys $99.99, G915 X $129.99, PRO X TKL $219.99, and
  dozens more across the four catalogs. MX Keys S Combo is a
  bundle, not a standalone line.
