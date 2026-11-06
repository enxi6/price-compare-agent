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

## 025 (2026-10-31): Small-brands official-catalog sweep, fifth part (DECISIONS 013)

- Read-only sweep of Samsung, Bose, Google, Amazon, Meta, Xbox,
  Keychron US pages, 2026-10-31 23:19-23:24 PT (no sign-in, no
  cart). Same-family candidates only; no new categories.
- Result: 5 current, 1 listed-but-sold-out, 1 unverified-blocked.
  - Samsung Buds4 Pro White: CURRENT, from $249.99, White shown.
    Model number not displayed on the overview page — name +
    color match, not an MPN mapping.
  - Bose QC Ultra Earbuds 2nd gen Black: CURRENT, $229 (was
    $299).
  - Pixel Buds Pro 2 Porcelain: CURRENT, $169 (was $229). Model
    number not displayed — name + color match.
  - Quest 3S 128GB: CURRENT, $349.99 (256GB is a storage variant
    of the same line).
  - Xbox Wireless Controller Carbon Black 1914: CURRENT, $49.49
    (was $64.99). Model number not displayed — name + color
    match.
  - Keychron K8 Pro K8P-G1: LISTED BUT SOLD OUT on keychron.com
    (0 in stock; sale $74.99, reg $99.99). Page points to
    successors K8 HE & K8 Ultra 8K. Sold-out is not
    discontinuation; handling pending user decision. Entry
    unchanged.
  - Kindle Paperwhite 16GB (2024) Black: NOT VERIFIED — amazon.com
    refused AI-agent access (Conditions of Use wall). Entry
    unchanged; neither confirmed nor removed. Needs live-browser
    takeover or a retailer currency check.
- Candidate lines observed (NOT approved additions): Galaxy Buds4
  $179.99, Buds3 FE $149.99; Bose Ultra Open 2nd gen $299, Sport
  Open $199, QC Earbuds $129, NC Wired $99; Pixel Buds 2a $129;
  Quest 3 $599.99 (512GB shown); Elite Series 2 $167.99, Elite
  Core $111.74-$139.99, Nano $49.99, Adaptive Controller $99.99,
  Adaptive Joystick $29.99, special editions $49.06-$98.97 (some
  sold out); Keychron K8 HE $139.99, K8 Ultra 8K $119.99, K8
  $59.99+, Q6/Q1/Q11 lines $229.99-$254.99, B40 $49.99, B39
  $54.99 (Keychron's All Keyboards collection showed 339 items,
  so the keyboard candidate list is representative, not
  exhaustive). Refurbished lines excluded by scope.

## 026 (2026-11-01): MX Master 3S replaced by MX Master 4 Graphite (DECISIONS 017) — entry swap done, quote verification running

- Old entry logitech-mx-master-3s-graphite deleted from the catalog
  (retired keys are removed, never reused); new entry
  logitech-mx-master-4-graphite added with UPC 097855207623 / MPN
  910-007558 (see DECISIONS 017 for the full identifier case).
  The dated snapshot files mentioning the 3S are left untouched
  (append-only record).
- The MX Master 4 quote ($119.99, Logitech direct + retailers,
  Meta Catalog) is held for browser verification of the Logitech
  US Graphite page before it enters a snapshot file; this entry
  records the swap, and the snapshot + commit follow the
  verification result.

## 027 (2026-11-01): MX Master 4 Graphite quote verified — Logitech direct $119.99 in stock, swap complete

- Browser verification 2026-11-01 08:11-08:12 PT (read-only, no
  sign-in, no cart): Logitech US Graphite page confirms standard
  consumer MX Master 4 (not for Mac/Business/Special Edition),
  Graphite swatch selected, $119.99, In stock. Ready to ship;
  Specs confirm Graphite 910-007558 (Pale Gray 910-007559, Black
  910-007560). No UPC on the page (UPC comes from the
  Camel/WantItAll agreement).
- New file data/eval_snapshots_mxmaster4_2026-11-01.json (1 quote:
  Logitech direct $119.99). Two Meta Catalog rounds found no US
  retailer Graphite row — Pale Gray rows are a different variant,
  Ayoub 910-007562 is non-US + a different code, RC Willey states
  no color — so retailer Graphite coverage is an open follow-up,
  not a gap in the entry. Combined coverage stays 28 of 28 models.
- Nuance recorded: the Meta Catalog feed still shows a 910-006557
  product page ($99.99), but the live 65-product Mice catalog walk
  (BUILD_LOG 024) found no plain 3S listing. Feed rows can lag,
  so the live-catalog finding stands; the swap decision is
  unaffected.
- Tests: 19 passed (re-run after the edit).

## 028 (2026-11-01): Amazon strategy written (DECISIONS 018, AMAZON_STRATEGY.md)

- Trigger: the Kindle Paperwhite case exposed Amazon's AI-access
  wall as a plan-level constraint, not a one-off failure. Research
  (2026-11-01) found PA-API 5.0 reportedly deprecated in favor of
  the Creators API, with a rolling referred-sales gate — meaning a
  new site cannot get official API access before it has Amazon
  referral traffic. Licensed providers (Keepa API from ~EUR
  49/month, Rainforest API from $23/month) are the industry route.
- Decision recorded: no bypass scraping; Amazon layer in Phase 2;
  ranking identical across tiers with Pro paying for depth. Pro
  price, refresh cadence, and provider choice explicitly deferred
  to Phase 2 evaluation, not launch-day decisions.
- Tests: 19 passed (re-run after the edit; no code changed).

## 029 (2026-11-01): K8 Pro replaced by K8 Ultra 8K (DECISIONS 019) — entry swap done, quote verification running

- Old entry keychron-k8-pro deleted from the catalog (retired
  keys are removed, never reused); new entry keychron-k8-ultra-8k
  added with SKU K8U-J1 (see DECISIONS 019). The dated snapshot
  files mentioning the K8 Pro are left untouched (append-only
  record).
- The K8 Ultra 8K quote ($119.99, Keychron direct, Meta Catalog)
  is held for browser verification of the Keychron official page
  before it enters a snapshot file; the per-variant barcode check
  via the public product JSON is running in the same verification.
  This entry records the swap, and the snapshot + commit follow
  the verification result.
- Consequence stated plainly: the K8 Pro $49.99 quote was the only
  quote entering the main ranking. Until an identifier-matched
  Ultra 8K quote lands, the main ranking holds no verified quote
  again — that is the rule working, not a regression.

## 030 (2026-11-01): K8 Ultra 8K quote verified — Keychron direct $119.99 in US warehouse, swap complete

- Browser verification 2026-11-01 08:25-08:26 PT (read-only, no
  sign-in, no cart): Keychron US page confirms K8 Ultra 8K (not
  Pro/HE/Q-series); only Type Fully Assembled, only Color Black;
  three switch variants all $119.99, all stocked in the US
  warehouse: Red K8U-J1 (page default), Brown K8U-J3, Banana
  K8U-J4. The Red pinning matches the page default.
- New file data/eval_snapshots_k8ultra_2026-11-01.json (1 quote:
  Keychron direct $119.99, Red K8U-J1, free US shipping, 2-5
  days). Combined coverage stays 28 of 28 models. The main
  ranking holds no identifier-matched quote for this entry yet
  (the old K8 Pro $49.99 quote is not carried over) — stated
  plainly, not hidden.
- Open follow-up: no UPC/EAN/barcode on the visible page. The
  per-variant barcode check via Keychron's public product JSON
  (the K8 Pro precedent) is running as a follow-up; if barcodes
  surface, the entry gains an EAN in a follow-up commit.
- Tests: 19 passed (re-run after the edit).

## 031 (2026-11-01): K8 Ultra 8K per-variant barcodes found in Keychron's public product JSON

- Follow-up to BUILD_LOG 030: the visible page showed no barcode,
  but the public product JSON (same product, id 8205260095577)
  carries a barcode per variant, all available, all $119.99:
  Red K8U-J1 4894979057969, Brown K8U-J3 4894979057976,
  Banana K8U-J4 4894979057983.
- Entry updated: identifiers now EAN 4894979057969 + SKU K8U-J1.
  Field note, stated plainly: the JSON field is named 'barcode'
  only (no separate GTIN/UPC/EAN field); recorded as EAN
  following the K8 Pro precedent (13-digit barcodes). No barcode
  type beyond the field name is asserted by the JSON itself.
- Tests: 19 passed (re-run after the edit).

## 032 (2026-11-01): Selection methodology decided (DECISIONS 020) — deal sites rejected as selector

- Trigger: user proposed referencing deal sites (DealMoon) for
  non-Apple selection, inviting a professional override.
- Verdict: proposal partially overturned. DealMoon is not adopted
  as the selection source (audience skew, deal-ephemerality,
  commercial bias — see DECISIONS 020). Brand official catalogs
  stay the backbone; demand prioritization is added as a layer
  (bestseller lists + review volume first, deal sites only as a
  secondary gap-check/alert signal). The user's core point —
  selection needs a demand filter — is kept in this form.
- Tests: 19 passed (re-run after the edit; no code changed).

## 033 (2026-11-01): MX Master 4 retailer Graphite hunt — Best Buy checked, no standard Graphite listing
- Third Meta Catalog round + Best Buy direct check (read-only,
  2026-11-01 08:54-08:57 PT, no cart, no sign-in): Best Buy does
  NOT list the standard consumer MX Master 4 Graphite 910-007558
  in this check — full search for "Logitech MX Master 4 Graphite"
  (22 results) plus an exact part-number search returned only
  adjacent variants, none substituted:
  Pale Gray 910-007559 (SKU 6640819, $119.99), Black 910-007560
  (SKU 12565546, $126.81, marketplace $126.81-$152.00), Adobe
  Edition Black 910-007561 (SKU 6640829, $119.99), for Mac, for
  Business. The Adobe Edition code 910-007561 is newly recorded
  here and excluded as a special edition (different product).
- Conclusion, stated plainly: retailer Graphite coverage remains
  OPEN. The entry keeps its single verified quote (Logitech
  direct $119.99). This check narrows the hunt (Best Buy ruled
  out for now) but does not prove no US retailer carries
  Graphite; the next branches are other major retailers, when
  the catalog refreshes.
- Tests: 19 passed (re-run after the edit; no code changed).

## 034 (2026-11-06): First daily price refresh — all 28 models re-queried

- Trigger: user asked for daily updates on the price comparison
  project. First daily run under the new cadence: every one of
  the 28 eval models re-run through the Meta Catalog CLI
  (`catalog-search --intent targeted --currency USD --retries 2`),
  same query style as the 10-31 rounds. 28 raw files,
  `data/meta_catalog_raw_*_2026-11-06.json` (gitignored),
  549 raw listings total. One new snapshot file,
  `data/eval_snapshots_2026-11-06.json`; no old dated snapshot
  overwritten, no catalog or DECISIONS change, no new models,
  no Amazon touch.
- Result: 56 quotes across 23 of 28 models (prior round: 59
  quotes across 28 models). Eval: 56 quotes, 0 identifier-
  matched, 56 suspected — the catalog source gives no UPC, so
  every quote stays in the suspected table; that is the rule
  working, not a bug.
- Headline finding, stated plainly: **no same-merchant price
  changed at all.** Every continuing merchant held its price
  (Dell XM5 $399.99, Logitech MX Master 4 $119.99, Nintendo
  OLED $399.99, B&H Buds4 Pro $249.99, Staples AirPods 5 $129,
  Best Buy Kindle $199.99, Keychron $119.99, Kohl's DualSense
  $74.99, Anker/B&H $69.99, Sweetwater Superlight 2 $159.99,
  Best Buy Pixel Buds $169). All movement is merchant churn:
  quotes appearing at new merchants, or disappearing from the
  feed. Per-model diff (prior -> new):
  - Anker Prime 100W 2 -> 4 (+Newegg, CDW, all $69.99).
  - AirPods 5 3 -> 4 (Abt/Best Buy $129 gone; Apple $129,
    T-Mobile $129.99, BJ's $129.99 new).
  - AirPods Max 2 2 -> 2 (Best Buy $499 deal and Staples $549
    gone; Apple $549, Sam's Club $549 new).
  - AirPods Pro 3 1 -> 3 (Staples $249 gone; Apple $249,
    T-Mobile $249.99, AT&T $249.99 new).
  - iPad A16 3 -> 0; iPad Pro M5 11 4 -> 0; MacBook Air 13 M5
    2 -> 0; MacBook Air 15 M5 1 -> 0; Watch SE 3 1 -> 0 (see
    feed-gap note below).
  - iPad Air M4 5 -> 1 (Apple direct $749 new; B&H $699 deal
    gone with the rest).
  - Mac mini M6 1 -> 1 (Abt $899 gone, B&H $899 new, same
    price; URL confirms MHQK4LL/A, 16GB/256GB).
  - Magic Mouse 1 -> 2 (Staples $79 gone; Target $79.99,
    Sweetwater $79 new).
  - Bose QC Ultra 2 4 -> 2 (Macy's $398.46,
    RC Willey $449.99, NFM $369, Lenovo $369 all gone;
    Crutchfield Black $449, T-Mobile Black $449.99 new).
  - Pixel Buds Pro 2 1 -> 1 (Best Buy $169 sale, unchanged).
  - K8 Ultra 8K 1 -> 1 (Keychron $119.99, unchanged).
  - Kindle 1 -> 5 (Best Buy $199.99 held; Electronic Express
    $199.99, Abt $199.99, Staples $199.99 new; NFM $196.99
    new low, -$3).
  - Superlight 2 2 -> 4 (Logitech direct gone; Lenovo $159.99
    sale, iBUYPOWER $159.99, Target $159.99 new; Sweetwater
    held).
  - MX Keys S 1 -> 3 (ThinkEdu Pale Grey $138.99 gone — the
    feed's ThinkEdu row is now Graphite 920-011406; Staples
    $129.99 with 920-011559 in the title, Lenovo Pale Grey
    $129.99, Newegg Pale Grey $117 sale new).
  - MX Master 4 1 -> 1 (Logitech direct $119.99, unchanged).
  - Quest 3S 2 -> 4 (Abt/B&H gone; T-Mobile $349.99, QVC
    $349.00, NFM $349.99, Newegg $349.99 new, same level).
  - Switch Lite 2 -> 1 (NFM/Walmart gone; Nintendo direct
    Turquoise $229.99 new, same level).
  - Switch OLED 4 -> 2 (Sam's Club, GameStop,
    iCuracao gone; Nintendo direct $399.99 held, Target
    $399.99 new).
  - Buds4 Pro 3 -> 4 (Abt/Samsung direct gone; AT&T, T-Mobile,
    NFM $249.99 new; B&H held).
  - DualSense White 5 -> 1 (only Kohl's $74.99 held; Best Buy,
    GameStop, Macy's, PlayStation Direct rows absent from the
    feed this round).
  - WF-1000XM5 Black 1 -> 3 (Suncoast $299.99 gone; Best Buy
    $248 sale, P.C. Richard $248 sale, FocusCamera $199.99
    new — street price down $52-$100 vs the prior single
    quote).
  - WH-1000XM5 Black 2 -> 2 (Target $399.99 gone; Dell $399.99
    held, Macy's Black $398 new).
  - Xbox Carbon Black 2 -> 3 (Newegg $49, MaxLevel $49.99
    gone; Lenovo $64.99, ThinkEdu $61.99 sale, iBUYPOWER
    $49.99 sale new — the $49 level survives via iBUYPOWER).
  - MacBook Pro 14 M6 1 -> 2 (see launch-day note below).
- Five models with zero qualifying rows — feed gap, not a
  delisting (stated plainly, each checked): Watch SE 3 (only
  carrier monthly/installment rows, a 44mm BJ's row, wrong
  colors); MacBook Air 13 M5 (Apple rows carry other part
  numbers MDHG4LL/A/MDH74LL/A; campus-bookstore rows are
  education pricing); MacBook Air 15 M5 (only a Silver Best
  Buy row, wrong color); iPad A16 (only carrier $16.67/mo rows
  and accessories — the 10-31 $399 promos expired 10-31 23:59
  ET, per the Apple snapshot traps); iPad Pro M5 11 (only
  1TB/2TB/13-inch/cellular rows; the Staples $1,399 row is
  cellular ME2N4LL/A).
- MacBook Pro 14 M6 launch day (2026-11-06): the catalog round
  returned no $1,999 base row (Apple $2,499 row is a higher
  config). The snapshot's 2 quotes (Apple $1,999, Best Buy
  $1,999, both in stock) come from the launch-day browser
  check done the same day — Apple page still shows no UPC, so
  the 2026-11-07 10:00 PT UPC check cron stands, and the
  catalog.py pre-order note ("pre-order, ships 2026-11-06")
  is left untouched in this commit per the refresh limits
  (it now reads stale: the model is in stock, not pre-order).
  Best Buy's $100 gift-card promo does not change the $1,999
  price.
- MX Master 4 Graphite, still open: no US retailer Graphite
  row again — Best Buy and Newegg rows this round are Pale
  Gray; Lenovo "for Business, Brown Box - Graphite" excluded
  as a business edition; B&H was also checked in the
  launch-day pass and does not list standard Graphite either
  (second retailer ruled out after Best Buy). Only Logitech
  direct $119.99 stands.
- Kindle: entry unchanged (still pinned B0CFPL6CFY, user
  undecided). RC Willey $199.99 excluded although the price
  matches — its URL carries B0CFPJYX7P (the US code from the
  pending decision) and is left out to keep the pinning clean.
  Target Graphite $199.99 excluded (2026-release naming);
  Kohl's $149.99 excluded (base Kindle, not Paperwhite).
- Flags for a merchant-page recheck (no browser recheck in
  this run): FocusCamera WF-1000XM5 $199.99 is a >$5 move vs
  the prior $299.99 quote; NFM Kindle $196.99 is a new low;
  Newegg MX Keys S $117 sale is well under the $129.99
  standard.
- Tests: 19 passed (eval + full suite re-run on the new
  snapshot; no code changed).

## 035 (2026-11-06): Launch-day browser check — MacBook Pro 14 M6 in stock; B&H has no MX Master 4 Graphite

- MacBook Pro 14 M6 base (MHWT4LL/A, 16GB/1TB, Space Black), launch day 2026-11-06, read-only browser check (no cart, no sign-in): Apple US store $1,999.00, in stock — "Pick up Today at Apple South Coast Plaza", 2-hr delivery from store $9, free delivery Mon Nov 9; no "pre-order" wording. Best Buy $1,999.00, in stock — "Pickup FREE Today" (Orange, "Only 2 left!"), "Shipping FREE Tomorrow"; Model MHWT4LL/A, SKU 6565882; a "Free $100 gift card included" offer does not change the $1,999 price. Catalog note fixed in this commit: "pre-order, ships 2026-11-06" → "in stock from launch day 2026-11-06 (Apple + Best Buy, $1,999)" (the 034 refresh had left it stale per its limits).
- Apple UPC: still not published — buy page, specs page, and site search for MHWT4LL/A show no part number or UPC. The 2026-11-07 10:00 PT UPC recheck cron stands. Availability wording is location-specific (Apple 92701 / South Coast Plaza; Best Buy Orange); bag/checkout orderability was not verified (read-only stop).
- MX Master 4 Graphite standard (910-007558, UPC 097855207623): B&H does NOT list it — part-number search, UPC search, name search, and the family variant selector all come back without it (Black 910-007560 $119.99 in stock and Pale Gray 910-007559 are listed; the "for Business (Graphite)" 910-007616 is a different part). B&H is the second retailer ruled out after Best Buy (BUILD_LOG 033). Only Logitech direct $119.99 stands; not listing at B&H does not prove unavailability everywhere.
- Merchant-page rechecks flagged by the 034 refresh (FocusCamera WF-1000XM5 $199.99, NFM Kindle $196.99, Newegg MX Keys S $117) were sent to a separate browser pass the same day; results to be recorded when they return.
- Tests: 19 passed (re-run after the catalog note edit; no code changed).

## 036 (2026-11-06): Merchant-page rechecks — FocusCamera $199.99 is Silver, NFM Kindle $196.99 confirmed, Newegg $117 is a marketplace seller

- WF-1000XM5 Black, FocusCamera $199.99: **NOT confirmed**. The $199.99 on FocusCamera belongs to the Silver model (SKU WF1000XM5S, in stock). A search by the black SKU (WF1000XM5B) returned only Used black units ($229.95 and $214.95, very low stock). The 034 snapshot's FocusCamera $199.99 row is therefore misattributed for the black model — recorded here as the correction, the dated snapshot file itself is not rewritten (snapshots are append-only). Real black street price stands at $248 (Best Buy / P.C. Richard, both sale).
- Kindle Paperwhite 16GB Black, NFM $196.99: **CONFIRMED**. NFM page: "Amazon Kindle Paperwhite E-reader 7\" 16GB in Black | Wi-Fi", $196.99 (Comp. Value $199.99), SKU 67502252, UPC 840268989538, Model B0CFPJYX7P; "In Stock in Omaha Store", pickup today. Caveat: this page's title does not include "(2024)"; the 2024 identification rests on Model B0CFPJYX7P + 7" screen + "next-generation 7\" Paperwhite display" description, identical to NFM's Jade listing explicitly titled "(2024)" (Model B0CFPHV9ZN, also $196.99). Evidence note for the pending Kindle decision: NFM independently confirms B0CFPJYX7P as the US black model with its own UPC 840268989538 — the pin itself is unchanged (still B0CFPL6CFY) until the user decides.
- MX Keys S Pale Grey (920-011559), Newegg $117: **NOT confirmed as a Newegg-sold price**. The page does show $117.00 (was $129.99), right model and part number — but "Sold by Astonlink | Shipped by Astonlink | Ships from China", free delivery Nov 20–Dec 02, quantity 1, no explicit in-stock wording. Newegg's own listing for the same keyboard is $129.99 with free shipping. The $117 is a marketplace-seller price, not a Newegg price.
- Method note: Google Search returned an "unusual traffic" page during this pass; it was not used or worked around — checks went directly to each merchant's own site search instead.
- Tests: 19 passed (re-run after the log edit; no code changed).

## 037 (2026-11-06): Selection and quote-eligibility rules set (DECISIONS 021)

- User decision (2026-11-06): third-party sellers not touched for
  now, non-US-market goods not touched, selection stays each
  brand's mainstream or new products with gradual expansion later.
- Operational effect from the next daily run: marketplace /
  third-party seller rows are excluded from snapshots entirely
  (not just flagged) — the Newegg $117 Astonlink row from the
  2026-11-06 snapshot is out. Non-US rows stay excluded as
  before, now under a named rule. No catalog entry changes: no
  current eval model is itself a third-party or non-US product.
- Daily cron `price-compare-daily-refresh` body updated with the
  three rules so every future run applies them.
- Tests: 19 passed (re-run after the docs edit; no code changed).

## 038 (2026-11-06): Expansion batch 1 — 5 models added, 28 → 33 (user-approved)

- Switch 2, base system (BEE-001): identifiers VERIFIED — UPC
  045496885816 (Nintendo US store page itself, GTIN 00045496885816,
  + Visions + eBay) and MPN BEE-001 (Nintendo Support + iFixit +
  eBay). Quotes (5): Nintendo direct $499.99 (page-verified,
  InStock, SKU 123669), Dell $499.99 (page-verified InStock — the
  feed row's $449.99 was contradicted by the merchant page and is
  excluded as captured), BrandsMart USA $499.99, BJ's $499.99,
  ShopMyExchange $499.99 (military community store; membership-
  gated retailers such as BJ's are already in the set). Nothing
  pending.
- WH-1000XM6 Black (WH1000XM6/B): identifiers VERIFIED — UPC
  027242930698 (B&H kit page + DataVision + Visions + Walts +
  Amazon.ca agree) and MPN WH1000XM6/B (Best Buy US SKU 6620467 +
  Sony). Conflicting code 094148746326 (Sony manual on
  manuals.plus, single source) noted, not used. Quotes (3): Sony
  direct $379.99 (was $459.99, page-verified price), T-Mobile
  $459.99 (business-channel page; the consumer page shows a $38.34
  monthly installment, not an outright price), Best Buy $378.00
  (page-verified bare unit, InStock, sold by Best Buy; Early Black
  Friday, comp. value $458 — the feed carried only the $378
  accessories bundle, so this is a fresh page-verified quote).
  Still pending: Sony direct stock was NOT confirmed in the page
  text (a 2026-11-03 report noted an availability-alert button on
  the page) — the $379.99 is recorded as price-only, flagged in the
  snapshot notes.
- Watch Series 12 GPS 42mm Black Aluminum, Black Sport Band S/M
  (MJEA4LS/A): identifiers PENDING (M6 precedent) — MPN MJEA4LS/A
  confirmed by Abt (US) + iClarified + Apple's own buy-page URL
  parameter, but no US source states a UPC; PBTech NZ UPC
  195951225470 (MJEA4X/A) and Very UK EAN 195951225395 are
  regional and were not used. Quotes (2): Apple direct $399.00
  (page-verified JSON-LD for the exact variant), BJ's $389.99
  (exact variant). Still pending: US UPC — needs a US retailer
  spec page or a physical box barcode.
- MX Anywhere 3S Graphite (910-006928): identifiers VERIFIED — UPC
  097855184030 + MPN 910-006928 (Logitech's own spec sheet + B&H
  spec table + Staples Model # / Color Graphite + Woot). The NZ
  graphite 910-006932 / UPC 097855184047 is a different regional
  SKU, excluded. Quotes (3): B&H $89.99 (page-verified, InStock,
  UPC 097855184030), Sweetwater $89.99, Lenovo $89.99 (all listed
  as "Black" — B&H/Staples/Lenovo/Sweetwater naming for Logitech's
  Graphite). Correction: the BUILD_LOG 024 candidate $69.99 was
  the Pale Grey sale price (Newegg), not Graphite; graphite street
  is $89.99. Still pending: no Logitech-direct Graphite quote —
  the direct page read showed Pale Grey $89.99 (910-006926).
- Galaxy Buds4 Black (SM-R540NZKAXAR): identifiers VERIFIED — UPC
  198957277207 (Abt US + ChannelOnline agree) and MPN
  SM-R540NZKAXAR (Samsung US buy-page URL + Abt). EU EAN
  8806097998563 and MEA SM-R540NZKAMEA excluded as regional.
  Quotes (3): Samsung direct $179.99 (page-verified), NFM $179.99,
  Best Buy $179.99. Nothing pending.
- MX Master 4 Graphite retailer hunt, third retailer ruled out
  (from the parent's 2026-11-06 check, recorded here as arranged):
  Adorama has no standard Graphite 910-007558 listing — part-number
  search, UPC search, and name search all return 0 results or only
  Black / Pale Gray / Mac / for-Business variants. Adorama is the
  third retailer ruled out after Best Buy (BUILD_LOG 033) and B&H
  (BUILD_LOG 035); the entry still holds only the Logitech direct
  $119.99 quote.
- Eval on the new snapshot: 33 models, 30 verified identifiers, 5
  with quotes, 16 total quotes, 0 identifier-matched, 16 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 28 →
  33 / 26 → 30 for the approved expansion).

## 040 (2026-11-06): Expansion batch 3 — 4 new models added, 38 → 42 (user-approved)

- Apple AirPods 5 — NOT added: already in the eval set since
  2026-10-31 as `apple-airpods-5-usbc`, USB-C case (MKFW4LL/A),
  UPC 195951378978, verified (B&H Photo spec + eBay GTIN agree;
  Best Buy US confirms Model MKFW4LL/A, SKU 6376553, $129). The
  Meta Catalog round still ran for it (20 rows; Apple direct
  $129 MKFW4LL/A and $149 MKFT4LL/A wireless-charging-case
  variant both present) — the $149 variant is a different
  configuration and was not added per DECISIONS 015. Batch 3 is
  therefore 4 new models, not 5.
- PlayStation 5 Pro 2TB, White, all-digital (1000046529 /
  CFI-7019B01X): identifiers VERIFIED — UPC 711719595946 (Best
  Buy US, Model 1000046529, SKU 10145289 + Amazon US ASIN
  B0DGY63Z2H + Desertcart + SeekMonkey EAN 0711719595946 agree)
  and MPN 1000046529. The guess 711719581124 appears nowhere in
  any source and was not used. Flagged, not assumed:
  PlayStation's current PDP lists model CFI-7021 and Best Buy's
  current listing (SKU 6601524) shows Model 1000046529/1000050805,
  so the UPC is verified for the launch revision; a separate
  CFI-7021 UPC was not found. Quotes (4): PlayStation Direct
  $899.00 (direct.playstation.com lists $899; US MSRP $899.99
  since 2026-04-02, up from $699.99 launch — stock not confirmed,
  Oct 2026 coverage reports Direct out of stock), Best Buy
  $899.99 (page-verified, sold by Best Buy, SOLD OUT), NFM
  $899.99, GameStop $899.99 (new, Currently Unavailable).
  Excluded: Best Buy marketplace $1,519.99-$1,672.90, Walmart
  $1,644.99 marketplace / $1,919.99 3TB bundle, FlexShopper
  bundle $998.99, renewed $1,264.49, drop-shipper $789.99, and
  all non-US rows (Siman, ZoneTecno, Titan, Distritech, 961souq,
  Outgeeked, Pixels-Bytes, GadgetLB, Boolchand); MDG $29.90 and
  GetItNow $28.05 are nonsense/installment rows, not prices.
- Switch - OLED Model, Neon Blue/Neon Red set (HEGSKABAA; SKU
  115464): identifiers VERIFIED — UPC 045496883409 (Nintendo US
  store page itself, GTIN 00045496883409 + Micro Center SKU 642595
  + J&L Game + eBay agree) and MPN HEGSKABAA (Best Buy Model).
  Console model HEG-001. Quotes (2): Nintendo direct $399.99
  (page-verified JSON-LD, InStock), Best Buy $399.00 (Model
  HEGSKABAA, SKU 11897850, Add to cart present). Excluded: White
  set $399.99 (different color, already in the set), Splatoon 3
  edition $359.99, Mario Red / Zelda rows ($44.99-$54.99, feed
  price errors for game rows), Walmart $399.99 (seller not
  confirmed), Walmart bundles $419.99-$459.99, CDW $532.99 /
  $552.99 (above MSRP), Ayoub $329 (non-US), Walmart JP import
  $385 (non-US).
- Logitech Lift Graphite, standard right-handed (910-006466):
  identifiers VERIFIED — UPC 097855170927 (Logitech's own spec
  sheet, Part # 910-006466, Bar code 097855170927 + Desertcart
  multiple regions, GTIN 00097855170927 + Ubuy agree) and MPN
  910-006466. Quotes (3): Logitech direct $79.99 (page-verified
  JSON-LD, Graphite, In stock. Ready to ship), Dell $69.99
  (graphite, sale), B&H $74.99 (InStock, JSON-LD). Excluded:
  for-Business and for-Mac rows, left-handed rows, Rose /
  Off-White / Sand rows, EMEA rows, Newegg rows (variant/seller
  unclear), Sears $116.89 (above MSRP).
- Meta Quest 3 512GB (899-00583-01): identifiers VERIFIED — UPC
  815820024071 (B&H Photo BH # MEQ3512, MFR # 899-00583-01 +
  Amazon US ASIN B0CD1JTBSC + Amazon.ca + Desertcart/Ubuy agree)
  and MPN 899-00583-01 (B&H MFR # + Best Buy Model + Abt). The
  128GB Quest 3 was phased out in 2024; 512GB is the only current
  tier. Quotes (4, all $599.99): Meta direct $599.99 (meta.com
  JSON-LD, InStock; re-checked by VR.org 2026-11-05), NFM
  $599.99, Abt $599.99 (899-00583-01), Newegg $599.99 (sold by
  Newegg). Excluded: Target $599.99 GOLF+ bundle (bundle), QVC
  $649.99 and CDW $699.99 (above MSRP), Quest 3S rows (different
  model, already in the set), accessories ($37.99/$39.99 facial
  interface), Aaron's / Mike's rent-to-own $100/$30 (rental, not
  sale), Virtuix $599 (third-party checkout).
- Eval on the new snapshot: 42 models, 38 verified identifiers, 4
  with quotes, 13 total quotes, 0 identifier-matched, 13 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 38 →
  42 / 34 → 38 for the approved expansion; the pending set is
  unchanged: DualSense, M6 Pro, Watch Series 12, Watch Ultra 4).

## 039 (2026-11-06): Expansion batch 2 — 5 models added, 33 → 38 (user-approved)

- WF-1000XM6 Black (WF1000XM6/B): identifiers VERIFIED — UPC
  027242933460 (Abt US product page + B&H Photo spec page + eBay
  product identifiers agree) and MPN WF1000XM6/B. Amazon bundle
  UPC 196641206649 and renewed UPC 728434235248 are different
  products, not used. Quotes (4, all $298.00 sale): Sony direct
  $298.00 (was $329.99 — price from Sony's own page via search
  index; the Sony page itself returned 403 on direct fetch, so
  stock is NOT confirmed, price-only), B&H $298.00 (was $328),
  Walts $298.00 (was $328), P.C. Richard $298.00 (was $329.95).
  Excluded: Nordstrom $328 (color unconfirmed in the feed row),
  Platinum Silver rows ($298), Best Buy / Moon Audio / DataVision
  care-program and accessory bundles ($298-$328.48), Target
  earbud-tips bundle $328.48.
- Watch Ultra 4 GPS + Cellular 49mm Natural Titanium, Sand Trail
  Loop M/L (MJAQ4LS/A): identifiers PENDING (M6 precedent) — MPN
  MJAQ4LS/A confirmed by Apple's own buy-page URL parameter +
  Best Buy US (Model MJAQ4LS/A, SKU 6597850) + EveryMac (Apple
  Order No MJAE4LS/A* for the Desert Alpine Loop variant, Model
  No A3579). GPS + Cellular only — no GPS-only tier exists
  (Apple buy page, EveryMac). The only US UPC found,
  195951394480 (Natural M/L Sand Trail Loop), appears in a single
  source (Adorama's spec table) and was NOT used; UK EAN
  195951218090 (Black Burgundy Trail Loop S/M, Very UK) is
  regional. Quotes (2, both $799.00): Apple direct $799.00
  (page-verified JSON-LD for the exact variant; stock not
  confirmed in page text), Best Buy $799.00 (unlocked, sold by
  Best Buy). Excluded: T-Mobile $799.99 Black Titanium Ocean Band
  (different variant), Best Buy AT&T $799.99 (carrier-activated),
  Abt MJA94LS/A Milanese Loop $870 (different variant), Costco
  Black Titanium (different variant), Adorama S/M $939
  (different size, above MSRP, backordered to 01/2027). Still
  pending: US UPC — needs a second independent US source.
- Switch 2 Pro Controller Black (BEE-008): identifiers VERIFIED —
  UPC 045496885861 (Nintendo US store page itself, SKU 123674,
  UPC 00045496885861, + Dell manufacturer part + eBay GTIN
  0045496885861 + PayMore + Ubuy) and MPN BEE-008 (Nintendo
  Support US: "All official Nintendo Switch 2 Pro Controllers
  have the model number BEE-008"). Retail SKU BEE-A-FSSKA.
  Conflicting codes excluded: 0219341384384 (single eBay listing,
  uncorroborated) and 4902370552843 (Japan JAN). Quotes (5):
  Nintendo direct $89.99 (page-verified, InStock), GameStop
  $89.99, R.C. Willey $89.99, Dell $89.99 (manufacturer part
  045496885861), JustPressPlay $79.99. Excluded: Macy's $99.99
  and JNL Game $99.99 (above MSRP; seller not confirmed as the
  merchant itself), Newegg $138.99 (marketplace-style row), Zelda
  40th Anniversary $99.99 and Resident Evil Requiem $119
  (different editions), Japan import $123.31 (non-US).
- MX Keys Mini Black (920-010475): identifiers VERIFIED — UPC
  097855169617 + MPN 920-010475 (Logitech's own spec sheet, P.C.
  Richard-hosted PDF, + manuals.plus + Adorama + DirectDial
  agree). Best Buy Q&A (answered by Logitech) confirms
  920-010475 is Black and 920-010388 is Graphite — different
  SKUs, not one board under two names. Quotes (3, all $89.99):
  Logitech direct $89.99 (was $99.99, page-verified, In stock),
  Staples $89.99 (Model # 920-010475), Lenovo $89.99 (sale, was
  $99.99). Excluded: for-Mac (920-010389 / 920-012644) and
  for-Business (920-010594) rows, Pale Grey (920-010473) and Rose
  (920-010474) rows, Newegg marketplace rows.
- Galaxy Buds3 FE Black (SM-R420NZKAXAR): identifiers VERIFIED —
  UPC 0198957213090 (ChannelOnline multiple storefronts + eBay
  GTIN agree) and MPN SM-R420NZKAXAR (Samsung US buy-page URL +
  SHI Mfr Part # + Newegg Part Number). Regional codes excluded:
  SM-R420NZKAASA (AU), SM-R420NZKAXSE, SM-R420ZNAXNU,
  SM-R420NZAFXAR. Quotes (5, all $149.99): Samsung direct
  $149.99 (page-verified JSON-LD, InStock), T-Mobile $149.99,
  Newegg $149.99 (sold by Newegg, shipped by Newegg), CDW
  $149.99, ShopMyExchange $149.99 (sale, was $249). Excluded:
  Target international version $99.99 sale (non-US), Target
  $117.97 (seller not confirmed), Macy's $149.99 shipped and sold
  by DataVision (marketplace, DECISIONS 021), Ayoub
  SM-R420NZAFXAR $120 (regional suffix), Samsung Latin $114 and
  Newegg LatAm $136.99 (non-US), refurbished rows (DECISIONS
  006). Gray SM-R420NZAAXAR is a different SKU.
- Eval on the new snapshot: 38 models, 34 verified identifiers, 5
  with quotes, 19 total quotes, 0 identifier-matched, 19 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 33 →
  38 / 30 → 34 for the approved expansion).

## 041 (2026-11-06): Expansion batch 4 — 5 models added, 42 → 47 (user-approved)

- Membership check (skill): read the 42-model key list from
  `price_agent/catalog.py` before adding anything. No candidate
  matched an existing model by name, MPN, or UPC: no `ipad-mini`,
  `ps5-digital`, `joy-con-2`, `g502`, or `pixel-buds-2a` key existed;
  the set's iPads are A16/Air M4/Pro M5 (no mini), the only PS5 is
  PS5 Pro, the only Joy-Con is the Switch 2 Pro Controller, the
  only Logitech gaming mice are Superlight 2 and Lift, and the only
  Pixel Buds entry is Pixel Buds Pro 2 Porcelain. All five were
  added; none was dropped. (Batch 3's AirPods 5 precedent was
  checked against and did not recur.)
- Apple iPad mini (A20 Pro), Wi-Fi 128GB Standard Glass, Starlight
  (MJ6J4LL/A, Model A3595) — identifiers VERIFIED: UPC 195951205595
  (B&H spec page + Adorama spec table agree), MPN MJ6J4LL/A (Best
  Buy US SKU 6638325 + CDW CDW# 9296012 + EveryMac + B&H). Released
  2026-11-06, 8.5-inch OLED, A20 Pro, Wi-Fi 7. Quotes (3, all
  $699.00): Apple direct $699.00 (apple.com US buy page JSON-LD,
  price-only), Best Buy $699.00 (sold by Best Buy, InStock), B&H
  $699.00 (In Stock, New Release). CDW $699.00 also seen. Excluded:
  feed Apple brand_direct rows ($599-$849, Space Gray/Purple/Blue)
  are the outgoing A17 Pro model; NFM $999/$1,249 rows are the
  512GB A20 Pro variant; Midnight (MJ6F4LL/A) and 256GB (MJ6R4LL/A)
  are different SKUs.
- Sony PlayStation 5 Slim Digital Edition 825GB, White (CFI-2015)
  — identifiers VERIFIED: UPC 711719541035 (PayMore US spec table
  + eBay GTIN agree), MPN CFI-2015 (PayMore + eBay + pawn listings).
  Best Buy Model 1000049898, SKU 6646420. Quotes (2): Best Buy
  $599.99 (sold by Best Buy, Add to cart, JSON-LD InStock on the
  page read 2026-11-06; one earlier crawl showed Unavailable for
  shipping — mixed signals, flagged), Sam's Club $599.00 (feed,
  authorized_retailer). Excluded: 1TB CFI-2015 revision UPC
  711719548539 (different revision); CFI-1015B launch digital
  $409.99 (marketplace, different model); $519.97 row (seller
  unconfirmed); $716.99-$1,107.99 import/reseller rows; bundles
  (Fortnite $709-$793, Marvel's Wolverine $925.99-$980). Candidate
  price $599 corrected to $599.99.
- Nintendo Joy-Con 2 (L)/(R) Light Blue / Light Red pair
  (BEEAJAAAA) — identifiers VERIFIED: UPC 045496885892 (Nintendo
  US official page, SKU 123677, UPC 00045496885892 + Snapklik Model
  BEEAJAAAA, UPC 045496885892 agree), MPN BEEAJAAAA. Quotes (2):
  Nintendo direct $99.99 (JSON-LD InStock, page read 2026-11-06),
  Electronic Express $94.99 (feed, authorized_retailer). Excluded:
  PBTech NZ UPC 045496321413 (regional); Newegg $99 row (seller
  not confirmed as merchant itself); Light Purple/Light Green and
  Blue/Light Yellow pairs (different SKUs); single Joy-Con 2 (L)/(R)
  $54.99 singles.
- Logitech G502 X PLUS Black, HERO 25K (910-006160) — identifiers
  VERIFIED: UPC 097855166951 (ErgoDirect + Desertcart + Amazon US
  + DirectDial + eBay agree), MPN 910-006160. Quotes (4):
  Logitech direct $159.99 list (current PDP defaults to the HERO
  44K Black/Purple 910-007808 at the same price, In stock),
  Best Buy $159.99 (HERO 25K Black), Adorama $159.99 (InStock),
  Staples $188.99 (Black 910-006160). Excluded: G502 X wired
  $75.99/$99.99 rows (different model); White $159.99-$326.66 rows
  (910-006169/910-006172, different SKU); Millennium Falcon edition
  $242; $160.99 marketplace row; $123.79 row (seller not
  confirmed). HERO 44K refresh: part numbers conflict (910-007808
  vs 910-007812 for Black/Purple/Dark Lilac) and no UPC was found
  for any 44K part number — open item, 25K UPC not carried over.
  Candidate price $149.99 was stale; street price is $159.99.
- Google Pixel Buds 2a, Hazel (GA06155-US) — identifiers VERIFIED:
  UPC 840353930506 (eBay product catalog MPN GA06155US, GTIN
  0840353930506 + Poshmark US seller GA06155-US, UPC 840353930506
  + Snapklik/ImportItAll/WantItAll agree), MPN GA06155-US (Best
  Buy US SKU 6642707 + B&H BH # GOPBUD2AHAZ agree). Quotes (4):
  Google Store $129.00 (Google support compare page lists From
  $129, price-only), Best Buy $129.00 (sold by Best Buy, InStock),
  B&H $129.00 (In Stock), T-Mobile $129.99 (feed, brand_direct).
  Excluded: OnBuy UK conflicting UPC 840353930520 (single UK
  source, not used; JP 840353933019, EU 840353930537 are regional);
  Best Buy $119.99 row (SKU 12951378, sold by TheRightOne,
  marketplace, DECISIONS 021); AT&T $129.99 seen in feed
  (brand_direct, not carried); Iris/Fog/Berry (different colors).
- Eval on the new snapshot: 47 models, 43 verified identifiers, 5
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 42 →
  47 / 38 → 43 for the approved expansion).

## 042 (2026-11-06): Expansion batch 5 — 5 models added, 47 → 52 (user-approved)

- Membership check (skill): read the 47-model key list from
  `price_agent/catalog.py` before adding anything. No candidate
  matched an existing model by name, MPN, or UPC: no `ipad-air-13`,
  `dualsense-edge`, `joy-con-pair`, `mx-vertical`, or `qc-earbuds`
  key existed; the set's iPad Air is the 11-inch M4 only, the only
  DualSense is the standard White, the only Joy-Con is the Switch 2
  pair, the only Logitech vertical mice are Lift, and the only Bose
  earbuds entry is QC Ultra 2 Black. All five were added; none was
  dropped. (Batch 3's AirPods 5 precedent was checked against and
  did not recur.)
- Apple iPad Air 13-inch (M4), 128GB Wi-Fi, Space Gray (MH5N4LL/A)
  — identifiers VERIFIED: UPC 195950797817 (Abt US Model MH5N4LL/A
  + iGiftcardz MPN MH5N4LL/A, EAN 0195950797817 agree), MPN
  MH5N4LL/A (Staples US + Quill + Best Buy US SKU 6586913 agree).
  Regional part numbers MH5N4TY/A (CY), MH5N4QA/A (ZA), MH5N4X/A
  (AU), MH5N4KN/A (IE) excluded as different SKUs. Quotes (2, both
  $949.00): Apple direct $949.00 (apple.com US buy page JSON-LD,
  price-only), Best Buy $949.00 (sold by Best Buy, InStock, SKU
  6586913). Excluded: Wi-Fi + Cellular 128GB $1,099 (MH9D4LL/A,
  different SKU); 256GB/512GB/1TB rows; Magic Keyboard $319 rows;
  T-Mobile/AT&T $30.56 installment rows; HSN $1,629.99 bundle.
- Sony DualSense Edge, Black & White (CFI-ZCP1) — identifiers
  PENDING: MPN CFI-ZCP1 confirmed (PlayStation official page +
  PBTech + Desertcart + eBay), but the UPC is unresolved:
  711719444190 (Desertcart GTIN 00711719444190 + Albagame barcode
  711719444190 + itworkup EAN + startech24 datasheet EAN
  0711719444190) vs 711719585552 (eBay product catalog ePID
  10058650690, Glacier White, repeated across eBay listings) vs
  711719586555 (PBTech NZ, regional) — no two independent US sources
  agree, so identifiers stay empty per the DualSense White
  precedent. Midnight Black (MPN 1000046706, UPC 711719596554) is a
  different colorway with Amazon-derived-only support (Desertcart +
  Ubuy, ASIN B0DSQQ1P8D), not pinned. Quotes (4, all $199.99):
  Kohl's $199.99 (Black & White), P.C. Richard $199.99 (Black &
  White, Model 1000035016), R.C. Willey $199.99 (Black and White),
  Abt $199.99 (Model 1000035016). Excluded: direct.playstation.com
  $30 row (not a real price); Macy's $224.95 (above MSRP); Ayoub
  $187/$199 rows (overseas seller); standard DualSense color rows
  ($74.99-$87.25, different model); Target $199.99 MSRP seen but
  not carried.
- Nintendo Joy-Con (L)/(R) Neon Red/Neon Blue pair (HACAJAEAA) —
  identifiers VERIFIED: UPC 045496590130 (Nintendo US official
  store page, SKU 104882, UPC 00045496590130 + eBay product catalog
  MPN HACAJAEAA, UPC 0045496590130 + PayMore US spec table MPN
  HAC-015, UPC 045496590130 agree), MPN HACAJAEAA (eBay + PicClick).
  HAC-015/HAC-016 are the individual left/right controller model
  numbers; the retail pair MPN is HACAJAEAA. Quotes (2, both
  $89.99): Nintendo direct $89.99 (JSON-LD InStock, SKU 104882),
  NFM $89.99. Excluded: Best Buy $115.61 (above MSRP); Newegg
  $89.99 (seller not confirmed as merchant itself); Ayoub $79
  (overseas seller); singles $34.99/$44.99; refurbished rows;
  other color pairs (Neon Purple/Neon Orange, Pastel Purple/Green,
  Neon Pink/Neon Green); one PayMore storefront's outlier UPC
  190403045002, not used.
- Logitech MX Vertical, Graphite (910-005447) — identifiers
  VERIFIED: UPC 097855144461 (Govets Part # 910-005447 + Compsource
  MPN 910-005447 + Desertcart GTIN 00097855144461 + CamelCamelCamel
  UPC 097855144461, Model 910-005447, list $119.99 agree), MPN
  910-005447. Quotes (3, all $99.99 sale): Logitech direct $99.99
  (sale, was $119.99, In stock, JSON-LD), Staples $99.99 (sale, was
  $119.99, Graphite 910-005447), Dell $99.99 (sale, was $119.99).
  Candidate price $99.99 is the current sale price; list is
  $119.99. Excluded: B&H feed sale figure $74.99 (not
  page-verified, not carried; list $119.99); second conflicting Dell
  feed row ($99.99 / sale $89.99); Lift rows ($59.99-$79.99,
  different model); 910-005449 row (different regional SKU);
  drop-shipper rows.
- Bose QuietComfort Earbuds (2024), Black (888507-0100) —
  identifiers VERIFIED: UPC 017817853460 (Abt US Model 888507-0100
  + Adorama spec table Black Earbuds 017817853460 + Ubuy GTIN
  00017817853460 + Desertcart GTIN 00017817853460, ASIN B0D8BZDPXB
  + eBay MPN 888507-0100 agree), MPN 888507-0100 (P.C. Richard +
  Abt + Adorama MFR). Quotes (4): Bose direct $119.00 (sale, was
  $179.00, ends 2026-11-08), P.C. Richard $129.00 (sale, was
  $179.00), Macy's $179.00, CDW $179.00 (Black). Candidate price
  $129 was wrong as a list price: list is $179.00; $129 is
  P.C. Richard's sale price and $119 is Bose direct's current sale
  price. Excluded: 2020 QC Earbuds 831262-0010 (UPC 017817804516,
  different model); QC Earbuds II $279 row (different model);
  refurbished $149 row; White Smoke 888507-0200 (different SKU);
  Ayoub $224 (overseas seller).
- Eval on the new snapshot: 52 models, 47 verified identifiers, 5
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 47 →
  52 / 43 → 47 for the approved expansion).

## 043 (2026-11-06): Continuous expansion starts — authorization recorded (DECISIONS 027)

- User authorized continuous expansion 52 → 200 models without
  per-batch approval (2026-11-06, "这个不需要我每5款确定一次，效率
  太低，目前就按照这个流程，一直加到200款"). Batches of 5 remain
  the documentation unit only.
- Starting state (verified 2026-11-06 09:54 PT): HEAD cfcae58, 52
  models, 47 verified identifiers, 19 tests passing.
- Work queue, in order: (1) remaining candidates from the five brand
  sweeps (BUILD_LOG 020/022/023/024/025); (2) new-brand sweeps
  (Anker, JBL, Razer, Corsair, Dell, HP, Lenovo, ASUS, Microsoft,
  Garmin, …), one brand at a time, official US catalog first,
  candidates list-only until added.
- Coordination: one batch at a time in the repo — never two writers
  on catalog.py/DECISIONS.md/BUILD_LOG.md at once; commits serialized.
  Progress reports at 75, 100, 125, 150, 175, 200 models.

## 044 — 2026-11-06: Expansion batch 6 — 52 → 57 models (DECISIONS 028)

- Membership check (against the 52-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - iPad Pro 13 M5 (MDYJ4LL/A, UPC 195950398090) vs
    apple-ipad-pro-m5-11 (MDWK4LL/A, UPC 195950395419): distinct
    size, MPN and UPC — not a duplicate.
  - PlayStation Portal (MPN 1000041319, UPC 711719579779): no Portal
    in the set; closest are DualSense controllers (different product
    class, different codes) — not a duplicate.
  - Switch Neon (HADSKABAA, UPC 045496883775) vs
    nintendo-switch-oled-neon (HEGSKABAA, UPC 045496883409),
    nintendo-switch-oled-white (UPC 045496883386) and the Joy-Con
    pair (HACAJAEAA, UPC 045496590130): distinct non-OLED console
    line — not a duplicate.
  - G Pro X Superlight 2 DEX Black (910-007328) vs
    logitech-g-pro-x-superlight-2-black (910-006628, UPC
    097855177797): distinct ergonomic asymmetric variant, different
    MPN — not a duplicate.
  - Bose Ultra Open Earbuds 2nd Gen Black (897806-0010, UPC
    017817862714) vs bose-qc-earbuds-black (888507-0100, UPC
    017817853460) and bose-qc-ultra-2-black (890101-0100, UPC
    017817859585): distinct open-ear line — not a duplicate.
- Apple iPad Pro 13-inch M5, 256GB Wi-Fi, Space Black (MDYJ4LL/A) —
  identifiers VERIFIED: UPC 195950398090 (Adorama US spec table,
  Space Black 256GB Wi-Fi Standard Glass + eBay US, MPN MDYJ4LL/A,
  agree), MPN MDYJ4LL/A (Apple direct URL + Best Buy US SKU 6586881
  + Abt + Adorama agree). Excluded: Amazon renewed UPC 728434107965
  (conflicting, renewed-only). Quotes (3): Apple direct $1,499.00
  (page-verified JSON-LD), Staples $1,499.00, Abt $1,424.00 (Comp.
  Value $1,499). Candidate price $1,499 confirmed as the 256GB list
  price; PhoneArena's $1,299 MSRP figure is wrong/stale.
- Sony PlayStation Portal Remote Player, White (1000041319) —
  identifiers VERIFIED: UPC 711719579779 (eBay US, White, MPN
  1000041319 + Snapklik, Model 1000041319 + Canex CA SKU agree),
  MPN 1000041319 (R.C. Willey + Abt Midnight Black is 1000044180, a
  different colorway). Excluded: regional barcode 711719580782
  (LDLC/Gamesmen AU); Ayoub $240 row (CFI-Y1018, overseas seller).
  Quotes (3): PlayStation Direct $249.00 (price-only; crawl mixed
  Currently Unavailable / Low stock flags), NFM $249.99 (JSON-LD
  InStock), R.C. Willey $249.99 (Model 1000041319). Manual model is
  CFI-Y1001; retail MPN is 1000041319.
- Nintendo Switch, Neon Blue/Neon Red set (HADSKABAA; SKU 117972) —
  identifiers VERIFIED: UPC 045496883775 (Nintendo US official store
  page itself, SKU 117972, GTIN 00045496883775 + Amazon B0BFJWCYTL,
  Model HADSKABAH, agree), MPN HADSKABAA (Amazon B07VGRJDFY +
  BuyDig agree; Best Buy/Amazon B0BFJWCYTL spell it HADSKABAH —
  recorded in the entry notes). The older HADSKABAA UPC 045496882174
  (ASIN B07VGRJDFY, 2019 red-box) conflicts with Nintendo's current
  page and was not pinned; HACSKABAA is the 2017 original revision,
  a different SKU. Quotes (3): Nintendo direct $339.99 (JSON-LD
  InStock), NFM $339.99, Best Buy $334.00 (Model HADSKABAH, SKU
  10951790, search-index read, below MSRP).
- Logitech G Pro X Superlight 2 DEX, Black (910-007328) —
  identifiers PENDING (identifiers empty, DualSense Edge precedent):
  MPN 910-007328 confirmed (Logitech G US store URL + Best Buy SKU
  12726725 + Quill) but no US retailer spec page states the UPC
  after repeated searches. B&H White 910-007363 is UPC 097855200471
  and Magenta 910-007371 is UPC 097855200457; the B&H Black page
  (LOPROXS2DBLK) exists but its UPC is not surfaced in the search
  index. Regional part numbers 910-007358/910-007359 and the DEX SE
  (910-007831, $129.99) are different models, excluded. Quotes (3):
  Logitech G direct $159.99 (In stock. Ready to ship, JSON-LD
  InStock), Best Buy $159.99, CDW $159.99.
- Bose Ultra Open Earbuds (2nd Gen), Black (897806-0010) —
  identifiers VERIFIED: UPC 017817862714 (B&H Photo US spec page,
  Black, 897806-0010 + Snapklik, Model 897806-0010 + Harvey Norman
  AU agree), MPN 897806-0010 (Abt US + B&H + Bose URL agree).
  Announced 2026-09-17, US launch 2026-10-01, $299. Quotes (3):
  Bose direct $299.00 (price-only on page text; $299 confirmed by
  Bose press release 2026-09-17), Abt $299.00 (JSON-LD InStock),
  B&H $299.00 (In Stock). 1st-gen Ultra Open rows ($349/$299) are a
  different model, excluded.
- Eval on the new snapshot: 57 models, 51 verified identifiers, 5
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 52 →
  57 / 47 → 51 for the approved expansion).

## 045 — 2026-11-06: Expansion batch 7 — 57 → 62 models (DECISIONS 029)

- Membership check (against the 57-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - MacBook Neo (MHFH4LL/A) vs apple-macbook-pro-14-m6 (MHWT4LL/A),
    apple-macbook-air-13-m5, apple-macbook-air-15-m5,
    apple-mac-mini-m6: distinct entry-laptop line, different MPN —
    not a duplicate.
  - PS5 1TB disc (1000049888, UPC 711719021452) vs
    sony-ps5-digital-825gb (1000049898, UPC 711719021483) and
    sony-ps5-pro (CFI-7021): distinct disc console, different MPN
    and UPC — not a duplicate.
  - Switch Pro Controller (HACAFSSKA, UPC 045496590161) vs
    nintendo-switch-2-pro-controller (BEE-008, UPC 045496885861):
    distinct original line, different MPN and UPC — not a
    duplicate.
  - MX Mechanical Tactile Quiet Graphite (920-010547, UPC
    097855174659) vs logitech-mx-keys-mini-black (920-010475) and
    logitech-mx-keys-s-pale-grey (920-011559): distinct mechanical
    line, different MPN and UPC — not a duplicate. The MX
    Mechanical Mini (Dell $149.99 rows) is a different model and
    was not added.
  - Xbox Elite Series 2 Black (FST-00001, UPC 889842196344) vs
    xbox-wireless-controller-black (1914, UPC 196388518159):
    distinct pro line, different MPN and UPC — not a duplicate.
    The Elite Series 2 Core (4IK-00001/4IK-00002, $134.99–$149.99)
    is a different line and was not added.
- Apple MacBook Neo 13-inch, A18 Pro, 8GB/256GB, Blush (MHFH4LL/A) —
  identifiers PENDING (identifiers empty, DualSense Edge / DEX
  precedent): MPN MHFH4LL/A confirmed (Apple US buy page title
  "Buy MacBook Neo, Blush, 256GB" + Best Buy US Model MHFH4LL/A,
  SKU 6615878) but no US source states a UPC for the Blush
  variant. The only Neo UPC found, 195950852745, is Indigo
  MHFF4LL/A's (B&H standalone page + Canex CA + eBay agree) and
  was not copied across colors; Courts Barbados lists it against
  MHFH4LL/A but its fields are garbled (GTIN 472384200015) and it
  mislabels the color. EveryMac's $599 256GB figure is stale/wrong
  against live $699. Quotes (2): Apple direct $699.00 (Meta
  Catalog brand_direct row), Best Buy $699.00 (page-verified
  JSON-LD InStock). Excluded: NFM $854 (Silver 256GB + 3-year
  AppleCare+ bundle), 512GB tiers $799 (MHFC4LL/A, MHFJ4LL/A,
  MHFE4LL/A, MHFG4LL/A), education-store rows ($738–$850).
- Sony PlayStation 5 Slim Console 1TB, disc, White (CFI-2100 model
  group; retail MPN 1000049888) — identifiers VERIFIED: UPC
  711719021452 (Amazon B0FRGTYSL5, Model Number CFI-2100, MPN
  1000049888 + two eBay US listings agree), MPN 1000049888 (Best
  Buy Model + Amazon MPN agree). Correction: the US disc model is
  NOT CFI-2016 (EU disc code; 15 = US, 16 = EU — eBay US lists the
  CFI-2000-group disc as CFI-2015, UPC 711719573364; PCShop.ge
  lists the CFI-2100-group disc as CFI-2116); the current US disc
  is the CFI-2100 group (CFI-2115 per JNLGame). Quotes (3):
  PlayStation Direct $649.00 (price-only; crawl mixed Currently
  Unavailable / Coming Soon / Low stock flags), Best Buy $649.99
  (page-verified, sold by Best Buy, SKU 6646419), Sam's Club
  $649.00 (standalone feed row). Excluded: Staples $722.99 (old
  CFI-2000 model 1000039671), marketplace rows $789–$1,246.99,
  game bundles ($1,040.99/$799.99/$699.99), rental rows
  ($26.99/$29.99/$100).
- Nintendo Switch Pro Controller, Black (HAC-013; retail MPN
  HACAFSSKA) — identifiers VERIFIED: UPC 045496590161 (Amazon
  B01NAWKYZ0, GTIN 00045496590161 + Abt page title + Newegg URL
  slug + Poggers item UPC agree), MPN HACAFSSKA (Amazon model
  number + MPN; HAC-013 is the hardware model per Nintendo Support
  US + Wikipedia). Quotes (3): Dell $79.99, NFM $79.99, Target
  $79.98 (product-page JSON-LD InStock, A-52180631; Target search
  listings show $79.99). Nintendo direct store page not re-reached
  (2026-10-31 sweep had $79.99 on nintendo.com); Abt lists it as
  no longer available. Excluded: Zelda/Smash/Splatoon special
  editions ($54.99–$140.99), third-party pads, Switch 2 Pro
  Controller rows. Wikipedia notes EU discontinuation February
  2027; the US listing is current as of 2026-11-06.
- Logitech MX Mechanical, full-size, Tactile Quiet, Graphite
  (920-010547) — identifiers VERIFIED: UPC 097855174659 (Amazon
  B09LK1P1RD, GTIN 00097855174659 + eBay UPC 0097855174659 agree),
  MPN 920-010547 (Amazon + eBay + Best Buy SKU 6502579 + Target +
  Staples agree). MPN mapping corrected: 920-010547 is Tactile
  Quiet; 920-010548 is Linear (Best Buy + BuyDig agree; its UPC
  097855174666 excluded). Quotes (3): Logitech direct $179.99
  (page-verified JSON-LD InStock, "In stock. Ready to ship"),
  Dell $169.99, Best Buy $179.99 (page-verified JSON-LD InStock,
  sold by Best Buy). Target $179.99 (JSON-LD InStock) also
  confirmed. Candidate price $149.99 corrected: it was the Oct 31
  LogiWork Deal Days sale price; current full-size list is
  $179.99 and the $149.99 rows today are the Mini (different
  model, excluded).
- Microsoft Xbox Elite Wireless Controller Series 2, Black
  (FST-00001) — identifiers VERIFIED: UPC 889842196344 (Amazon
  B07SFKTLZM first-listed + eBay agree for FST-00001 Black), MPN
  FST-00001 (Amazon item model number + eBay MPN + Microsoft Store
  product ID 8RSN7J6375GG cross-ref). Amazon's other two codes
  (889842613926, 750466003847) are unattributed variants, excluded;
  Core codes 4IK-00001/4IK-00002 are a different line. Quotes (3):
  Microsoft direct $167.99 (page-verified JSON-LD; stock not
  confirmed in page text), Target $167.99, Best Buy $159.99 sale
  (list $179.99). CDW $183.99 not used. Amazon flags the ASIN
  "discontinued by manufacturer" but Microsoft/Target/Best Buy all
  list it new on 2026-11-06, so it stays in as a current US line.
- Eval on the new snapshot: 62 models, 55 verified identifiers, 5
  with quotes, 14 total quotes, 0 identifier-matched, 14 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 57 →
  62 / 51 → 55 for the approved expansion).

## 046 — 2026-11-06: Expansion batch 8 — 62 → 67 models (DECISIONS 030)

- Membership check (against the 62-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - iMac M6 10-core Blue (MH094LL/A, UPC 195950838091) vs
    apple-mac-mini-m6 (MHQK4LL/A, UPC 195951021089),
    apple-macbook-pro-14-m6 (MHWT4LL/A), apple-macbook-air-13-m5,
    apple-macbook-air-15-m5, apple-macbook-neo-13-256gb-blush
    (MHFH4LL/A): no iMac in the set at all; distinct desktop line,
    different MPN and UPC — not a duplicate. The M4 iMac rows in
    the feed (MWV13LL/A etc., $1,699) are the outgoing model and
    were not added.
  - WH-1000XM4C Black (WH1000XM4C/B) vs sony-wh1000xm5-black
    (WH1000XM5/B, UPC 027242923232) and sony-wh1000xm6-black
    (WH1000XM6/B, UPC 027242930698): distinct 2026 M4-refresh line,
    different model number — not a duplicate. The original XM4
    (WH1000XM4/B, UPC 027242919419) is a different model and was
    not added.
  - PULSE Elite Midnight Black (1000044173) vs
    sony-playstation-portal (1000041319, UPC 711719579779),
    sony-dualsense-white, sony-dualsense-edge-black-white: no
    PULSE headset in the set; distinct headset line, different MPN
    — not a duplicate. The PULSE 3D (CFI-ZWH1) and PULSE Explore
    earbuds (CFI-ZWE1) are different models and were not added.
  - ERGO K860 Graphite (920-009166, UPC 097855151667) vs
    logitech-mx-keys-s-pale-grey (920-011559), logitech-mx-keys-mini-
    black (920-010475), logitech-mx-mechanical-tactile-quiet-
    graphite (920-010547): distinct split ergonomic line, different
    MPN and UPC — not a duplicate. The K860 for Business
    (920-010175, Logi Bolt) is a different SKU and was not added.
  - K8 HE Special Edition Black (K8H-F1, EAN 4894979028990) vs
    keychron-k8-ultra-8k (K8U-J1, EAN 4894979057969): distinct Hall
    Effect line, different SKU and EAN — not a duplicate. The K8
    HE Standard Version (K8H-J1), All-Wood Special Edition
    ($199.99) and Lime-switch variants are different variants and
    were not added.
- Apple iMac 24-inch M6, 10-core CPU/GPU, 16GB/256GB, Blue
  (MH094LL/A) — identifiers VERIFIED: UPC 195950838091 (B&H Photo
  US spec page for the exact MPN — single source so far, launch
  day; EveryMac still lists M6 iMac identifiers as Pending, so
  re-confirm on the next refresh), MPN MH094LL/A (Apple US buy
  page + Best Buy Model + EveryMac + MacSolutions Plus agree).
  Correction: the new iMac is M6, not M5 — it skips M5 entirely
  (announced 2026-10-27, pre-orders Oct 28, availability Nov 6,
  today). Quotes (3): Apple direct $1,499.00 (US buy page
  MH094LL/A, JSON-LD price; stock not stated in the page-text
  crawl), Best Buy $1,499.00 (page-verified JSON-LD InStock, sold
  by Best Buy, SKU 6566940), B&H $1,499.00 (New Release, In Stock,
  JSON-LD InStock). The Meta Catalog feed returned no M6 rows at
  all (all M4/M3/M1), so all three quotes are page-verified.
  Excluded: M4 iMac rows ($1,499–$2,099, incl. Apple direct M4
  colors $1,699), 12-core tiers ($1,699–$2,099), nano-texture
  ($1,899, MH2U4LL/A), M1 marketplace/rental rows.
- Sony WH-1000XM4C, Black (WH1000XM4C/B) — identifiers PENDING:
  MPN WH1000XM4C/B confirmed (Best Buy Model + Sony US store +
  Adorama + Canada Computers + Abt WH1000XM4CB agree) but no UPC
  found for Black in any US source. The only XM4C barcode found,
  4548736181861, is the Platinum Silver EAN (Harvey Norman AU,
  WH1000XM4CS) and was not copied across colors; the original XM4
  Black UPC 027242919419 (Abt) belongs to WH1000XM4/B and was
  excluded. Quotes (3): Best Buy $299.99 (WH1000XM4C/B, SKU
  6689199, sold by Best Buy), Target $299.99 (JSON-LD InStock,
  A-1012764580), Sweetwater $298.00 (feed row, WH1000XM4CB). Sony
  direct lists the model at $299.99 (store JSON-LD, same price all
  colors; Sony Sept 7 2026 announcement) and Abt/Nordstrom/
  Crutchfield $298.00 also confirmed. The XM4C is a 2026 hardware
  refresh of the 2020 XM4 (retuned sound, 10-band EQ, Bluetooth
  6.0, replaceable battery), announced Sept 7 2026. Excluded:
  original XM4 rows ($312.99–$349.99), XM4C Silver/Lavender
  colorways, FocusCamera/BuyDig accessory bundles.
- Sony PULSE Elite Wireless Headset, Midnight Black (retail MPN
  1000044173) — identifiers PENDING: MPN 1000044173 confirmed
  (Best Buy Model + P.C. Richard MODEL + ShopCGX + Big Apple Buddy
  agree) but the UPC was not verified from a non-Amazon US source.
  The only UPC seen, 711719588009, appears on a single Amazon
  listing (hardware model CFI-ZWH2) with no second source, so it
  was not recorded. The EU retail code 1000044483 (barcode
  711719590392) is a different retail code and was not copied.
  CFI-ZWH1 is the PULSE 3D headset, not the Elite. Quotes (3):
  PlayStation Direct $149.00 (price-only; crawl mixes Currently
  Unavailable / Low stock / Coming Soon flags), Best Buy $149.99
  (page-verified JSON-LD InStock, sold by Best Buy, SKU 6614841),
  P.C. Richard $149.99 (JSON-LD InStock, ships by Mon, Nov 9).
  Newegg $149.99 and Walmart $149.00 also confirmed (feed rows).
  Midnight Black released 2025-02-20; the White Elite is a
  different colorway. Excluded: PULSE 3D ($99.99), PULSE Explore
  earbuds ($149.99–$199.99), White Elite ($149), skins-voucher
  bundle ($229.99), earpads accessory ($19.99).
- Logitech ERGO K860, Graphite, standard edition (920-009166) —
  identifiers VERIFIED: UPC 097855151667 (Adorama US spec page,
  MFR 920-009166 + B&H kit pages, K860 section + eBay US item
  specifics agree), MPN 920-009166 (Dell manufacturer part + Best
  Buy Model + Adorama MFR + CompSource + DirectDial agree).
  Correction vs the 2026-10-31 candidate price: $119.99 was an
  Amazon-only sale price (TechTimes 2026-10-19, 20% off the
  $149.99 MSRP) and no Amazon price is used; the current
  first-party list is $149.99. The feed's Dell $129.99 row is stale
  (Dell page text now $149.99) and the feed's B&H $159.99 row is
  the K860 for Business (920-010175, Logi Bolt). Quotes (3): Best
  Buy $149.99 (page-verified JSON-LD InStock, sold by Best Buy,
  SKU 6395346), Dell $149.99 (page text, MPN 920-009166), Newegg
  $149.99 (feed row, 920-009166). Logitech US direct lists the
  Business variant, not the standard consumer page, so no
  Logitech-direct quote this batch. Excluded: K860 for Business
  (920-010175, $139.99–$193.99), regional MPNs 920-009167/
  920-010107/920-010348, K860+mouse kits ($224.98) and Mk860
  bundle ($338.99), Woot $109.99 (deal-site row, not used).
- Keychron K8 HE, Special Edition, Black, Gateron Double-Rail
  Magnetic Nebula Switch (K8H-F1) — identifiers VERIFIED: EAN
  4894979028990, SKU K8H-F1 (Keychron official store public
  product JSON, browser-verified 2026-11-06; Special Edition
  White K8H-Q1 is 4894979029003, Standard Black K8H-J1 is
  4894979028952). Correction vs the 2026-10-31 candidate note:
  $139.99 is the Special Edition (OSA double-shot PBT, wood
  trim); the Standard Version is $129.99 (K8H-J1) and is currently
  unavailable at Keychron. The feed's keychron.com $139.99 row is
  the Japan JIS Layout product, a different layout, and was not
  used. Quotes (1): Keychron direct $139.99 (official store JSON,
  available: true; the K8 HE is sold only through Keychron's own
  store). Excluded: Newegg rows $221.48–$273.99 (third-party
  inflated), All-Wood Special Edition ($199.99), Lime-switch
  variants (unavailable, no barcode), K8/K8 Pro/K8 Max/K8 Ultra
  8K and Q1/Q5/Q6/J2/K10 HE rows.
- Eval on the new snapshot: 67 models, 58 verified identifiers, 5
  with quotes, 13 total quotes, 0 identifier-matched, 13 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 62 →
  67 / 55 → 58 for the approved expansion).

## 047 — 2026-11-06: Expansion batch 9 — 67 → 72 models (DECISIONS 031)

- Membership check (against the 67-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - Mac Studio M5 Max 36GB/512GB Silver (MHL64LL/A, UPC
    195951078564) vs apple-mac-mini-m6 (MHQK4LL/A, UPC
    195951021089), apple-imac-m6-24-10core-blue (MH094LL/A, UPC
    195950838091), apple-macbook-pro-14-m6 (MHWT4LL/A),
    apple-macbook-air-13-m5, apple-macbook-air-15-m5,
    apple-macbook-neo-13-256gb-blush (MHFH4LL/A): no Mac Studio
    in the set at all; distinct desktop line, different MPN and
    UPC — not a duplicate. The M4 Max (MU963LL/A), M3 Ultra
    (MU973LL/A), M2 Max/Ultra rows in the feed are outgoing
    generations and were not added.
  - ULT WEAR Black (WHULT900N/B, UPC 027242928688) vs
    sony-wh1000xm5-black (WH1000XM5/B, UPC 027242923232),
    sony-wh1000xm6-black (WH1000XM6/B, UPC 027242930698),
    sony-wh1000xm4c-black (WH1000XM4C/B): distinct ULT Power
    Sound bass line (WH-ULT900N, 2024), different model number
    and UPC — not a duplicate.
  - PULSE Explore Midnight Black (retail MPN 1000044170, CFI-ZWE1)
    vs sony-pulse-elite-midnight-black (retail MPN 1000044173),
    sony-playstation-portal (1000041319, UPC 711719579779),
    sony-dualsense-white, sony-dualsense-edge-black-white: no
    PULSE earbuds in the set; the Elite is the over-ear headset
    (different MPN), the Explore is the earbuds line — not a
    duplicate. The PULSE 3D (CFI-ZWH1) is a different headset and
    was not added.
  - Wave Keys Graphite (920-011898) vs logitech-ergo-k860-graphite
    (920-009166, UPC 097855151667), logitech-mx-keys-s-pale-grey
    (920-011559), logitech-mx-keys-mini-black (920-010475),
    logitech-mx-mechanical-tactile-quiet-graphite (920-010547):
    no Wave Keys in the set; distinct wavy-keyframe ergonomic
    keyboard, different MPN — not a duplicate. The MK670 combo
    (920-012059), Wave Keys for Business (920-012058) and Wave
    Keys for Mac (920-012402) are different SKUs and were not
    added.
  - Sport Open Earbuds Black (901149-0010) vs
    bose-qc-earbuds-black (888507-0100, UPC 017817853460),
    bose-qc-ultra-2-black (890101-0100, UPC 017817859585),
    bose-ultra-open-earbuds-2nd-gen-black (897806-0010, UPC
    017817862714): distinct 2026 clip-on sport line, different
    MPN — not a duplicate. The original 2021 Sport Open Earbuds
    (857628-0010, UPC 017817826211) are a different product and
    were not added.
- Apple Mac Studio, M5 Max 18-core CPU/32-core GPU, 36GB/512GB,
  Silver (MHL64LL/A) — identifiers VERIFIED: UPC 195951078564
  (B&H US spec page + Adorama US UPC Codes list agree), MPN
  MHL64LL/A (Apple US buy page + B&H + Best Buy US Model +
  EveryMac agree; Mac17,14, A3545). Quotes (3): Apple direct
  $2,499.00 (JSON-LD price; stock not stated in page-text crawl),
  B&H $2,499.00 (page-verified In Stock, JSON-LD InStock), Best
  Buy $2,499.00 (Model MHL64LL/A, SKU 6566932, sold by Best Buy).
  Adorama $2,399.00 also seen. The B&H $2,299 sale price reported
  by MacPrices on Oct 14/28 is gone — the B&H page today shows
  $2,499.00. Excluded: M5 Ultra ($5,499, MHL74LL/A), 40-core GPU
  tiers (48GB/1TB $3,399 Z1U4000E9), M4 Max/M3 Ultra/M2
  marketplace rows, the feed's MU963LL/A $2,499 row (old MPN,
  new price), UK MHL64B/A (UPC 195951078380) and AU MHL64X/A
  (UPC 195951078724) regional variants.
- Sony ULT WEAR, Black (WHULT900N/B) — identifiers VERIFIED: UPC
  027242928688 (Amazon.com WHULT900NB.UC + Simcoe AV Canada
  authorized-dealer barcode + ShopCGX US Style agree), MPN
  WHULT900N/B (Best Buy Model + Crutchfield MFR + BuyDig agree).
  Quotes (3): Best Buy $148.00 (SKU 6576179, Holiday Deal, comp
  value $248.00), Crutchfield $148.00 (In Stock, Item 158ULT900B,
  $100 off $248.00), BuyDig $148.00 (WHULT900N/B). Correction vs
  the 2026-10-31 candidate price: $249.99 is the list price; the
  current street price is $148 at all three retailers. Excluded:
  headphone+adapter/stand/warranty bundles ($169.99-$386),
  Target gSport case bundle ($249.99, third-party seller),
  Coolblue NL $106 (non-US), the $25 copy row, Macy's SD-card
  bundle ($386), White UPC 027242929449.
- Sony PULSE Explore Wireless Earbuds, Midnight Black (retail MPN
  1000044170, CFI-ZWE1) — identifiers PENDING: MPN 1000044170
  confirmed (Best Buy Model + ShopCGX + P.C. Richard MODEL + Big
  Apple Buddy agree) but the UPC was not verified from a
  non-Amazon US source. The only US UPC seen, 711719587972,
  appears on Amazon listings (ASIN B0DSQSX7FB) with no second
  source; the UK/AU barcode 711719590231 (HMV + Gamesmen) is a
  different regional code and was not copied. Quotes (3): Best
  Buy $149.99 (page-verified JSON-LD InStock, Model 1000044170,
  SKU 6614843, sold by Best Buy), Target $149.99 (feed row,
  A-94472835), GameStop $149.99 (feed row). ShopCGX $149.99
  (feed row, Model 1000044170, InStock) also confirmed. P.C.
  Richard $199.99 OutOfStock is the list price. Excluded: White
  Explore, PULSE Elite (1000044173), PULSE 3D (CFI-ZWH1),
  PlayStation Link USB adapter ($24.99-$30), the $114.99
  secret-castle row (unverified seller).
- Logitech Wave Keys, Graphite (920-011898) — identifiers PENDING:
  MPN 920-011898 confirmed (Amazon.com US Mfr Part Number +
  Ryans Graphite agree) but the UPC 097855191533 appears only on
  that Amazon listing, with no second US source. Quotes (3):
  Logitech direct $69.99 (page-verified JSON-LD InStock; page
  default color Off-white, price uniform $69.99 across colors),
  Lenovo $69.99 (feed row, 'Wave Keys Wireless Ergonomic
  Keyboard - Graphite' — suspected, no identifier in the feed
  row), Newegg $69.99 (feed row — suspected). Correction vs the
  2026-10-31 candidate note: $69.99 is the current price (the
  2023 launch price was $59.99 per Logitech's blog). Excluded:
  MK670 combo 920-012059 ($89.99), Wave Keys for Business
  920-012058 ($76.99-$139.99), Wave Keys for Mac 920-012402,
  Sand 920-013925 2026 refresh (B&H $69.99, Staples $77.27),
  Wave Keys + Lift combos ($119.99), Rose / Off-White (Off-White
  is 920-012275), US International layout 920-012304 (EAN
  5099206117471), AU Graphite 920-012281, 920-013269 (a
  single-source roundup figure conflicting with 920-011898),
  the $50.97 / $81.10 / $86 Newegg rows (unverified variants).
- Bose Sport Open Earbuds, Black (901149-0010) — identifiers
  PENDING: MPN 901149-0010 confirmed (Best Buy Model + Abt +
  The Good Guys AU + BuyDig feed agree) but no UPC was found for
  the Black variant in any US source. B&H publishes only the
  Eucalyptus Green UPC 017817865449, which was not copied across
  colors. Quotes (3): Best Buy $199.00 (page-verified JSON-LD
  InStock, Model 901149-0010, SKU 6688450, sold by Best Buy),
  Abt $199 (page-verified price), Lenovo $199 (feed row,
  brand_direct — suspected, no identifier in the feed row).
  Bose direct price was not shown in the bose.com page text this
  batch. Excluded: the original 2021 Sport Open Earbuds
  857628-0010 (UPC 017817826211, ASIN B08VRLZGMF — a different
  in-ear product), Eucalyptus Green 901149-0030 / White Smoke
  901149-0020, Best Buy charger bundle ($202.99), BuyDig $204.
- Eval on the new snapshot: 72 models, 60 verified identifiers, 5
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 67 →
  72 / 58 → 60 for the approved expansion).

## 048 — 2026-11-06: Expansion batch 10 — 72 → 77 models (DECISIONS 032)

- Membership check (against the 72-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - Studio Display (2026), Standard glass, Tilt-adjustable stand
    (MFEX4LL/A, UPC 195950529173) vs apple-mac-studio-m5-max-36gb-
    512gb-silver (MHL64LL/A, UPC 195951078564),
    apple-imac-m6-24-10core-blue (MH094LL/A, UPC 195950838091),
    apple-mac-mini-m6 (MHQK4LL/A, UPC 195951021089): no monitor in
    the set at all; distinct display line, different MPN and UPC —
    not a duplicate. The 2022 Studio Display (MK0U3LL/A, UPC
    0194253030447) is the superseded generation and was not added;
    the Studio Display XDR (from $3,299) is a separate line and was
    not added.
  - LinkBuds Fit Black (WFLS910N/B, UPC 027242929289) vs
    sony-wf1000xm5-black (WF1000XM5/B, UPC 027242925601),
    sony-wf1000xm6-black (WF1000XM6/B, UPC 027242933460),
    sony-wh1000xm5-black, sony-wh1000xm6-black, sony-wh1000xm4c-
    black, sony-ult-wear-black (WHULT900N/B, UPC 027242928688):
    distinct open-fit LinkBuds line (WF-LS910N, 2024, Air Fitting
    Supporters), different model number and UPC — not a duplicate.
    The LinkBuds Open (also $228) is a different line and was not
    added.
  - Access Controller White (retail MPN 1000037579, CFI-ZAC1) vs
    sony-dualsense-white, sony-dualsense-edge-black-white
    (CFI-ZCP1), sony-playstation-portal (1000041319, UPC
    711719579779), sony-pulse-elite-midnight-black (1000044173),
    sony-pulse-explore-midnight-black (1000044170): no
    accessibility controller in the set; the Access (CFI-ZAC1) is
    the PS5 accessibility kit, different MPN from every controller
    in the set — not a duplicate.
  - POP Keys Cosmos (920-011233) vs logitech-mx-mechanical-tactile-
    quiet-graphite (920-010547, UPC 097855174659),
    logitech-mx-keys-s-pale-grey (920-011559),
    logitech-mx-keys-mini-black (920-010475),
    logitech-ergo-k860-graphite (920-009166, UPC 097855151667),
    logitech-wave-keys-graphite (920-011898): no POP Keys in the
    set; distinct typewriter-style emoji-key keyboard, different
    MPN — not a duplicate. The POP Icon Keys ($49.99) are a
    different keyboard line and were not added; Blast Yellow
    920-010707, Heartbreaker Rose 920-010709, Mist 920-011232 and
    Daydream are different colorways and were not added.
  - Elite Wireless Controller Series 2 – Core White (4IK-00001) vs
    xbox-elite-series-2-black (FST-00001, UPC 889842196344),
    xbox-wireless-controller-black (1914, UPC 196388518159):
    distinct cheaper Elite line (Core, no component pack / dock /
    case), different MPN — not a duplicate. The 2025 Core
    colorways (Blue, Red and Blue, Green and Blue, Astral Purple,
    Gray, Dark Green) are different models and were not added.
- Apple Studio Display (2026), Standard glass, Tilt-adjustable
  stand (MFEX4LL/A) — identifiers VERIFIED: UPC 195950529173
  (B&H US spec page for the exact MPN + the B&H Studio Display
  with AppleCare+ page, which lists the same display UPC
  195950529173 alongside the kit UPC 195951182148, agree), MPN
  MFEX4LL/A (Abt US Model + Apple US buy page agree; UK MFEX4B/A
  GTIN 195950528992 excluded). Quotes (3): Apple direct $1,599.00
  (buy page "from $1,599", base tilt config; page JSON-LD $1,999
  is a different selected config), B&H $1,549.00 (page-verified
  In Stock, JSON-LD InStock; Holiday Savings $50 off $1,599,
  limited supply at this price), Abt $1,599.00 (Model MFEX4LL/A,
  JSON-LD InStock). Correction vs the 2026-10-31 candidate note:
  the current Studio Display is the March 2026 refresh (A19,
  Thunderbolt 5, 12MP Center Stage with Desk View, 27-inch 5K
  60Hz 600-nit panel, on sale 2026-03-11), not the 2022 model
  (A13, Thunderbolt 3, MK0U3LL/A, UPC 0194253030447). Excluded:
  Studio Display XDR (from $3,299, MFE* XDR codes), MFEW4LL/A
  tilt-and-height $1,999, MFEY4LL/A VESA $1,599, MFF14LL/A nano
  tilt $1,899, MFF04LL/A nano tilt-and-height $2,299, MFF24LL/A
  nano VESA, the 2022 MK0U3LL/A, the feed's $5,499 Mac Studio row
  (a computer, not a display), Samsung/VITURE monitor rows.
- Sony LinkBuds Fit, Black (WFLS910N/B) — identifiers VERIFIED:
  UPC 027242929289 (B&H US spec page for the exact MPN + Tanotis
  WFLS910N/B agree), MPN WFLS910N/B (Best Buy US Model, SKU
  6594431 + B&H agree). Quotes (3): Best Buy $199.99 (Model
  WFLS910N/B, SKU 6594431, JSON-LD price; stock not stated in the
  page-text crawl), B&H $198.00 (page-verified; Special Order,
  expected availability 2-4 Weeks — not in stock at B&H; Holiday
  Savings $30 off $228.00), Crutchfield $198.00 (feed row —
  suspected, no identifier in the feed row). Correction vs the
  2026-10-31 candidate price: $229.99 is the list price; the
  current street price is $198–$199.99. Dell Black $229.99
  (brand_direct) and Sony direct Pink $229.99, sale $199.99, also
  seen. Excluded: LinkBuds Open ($228, different line), White /
  Sage Green / Pink / Violet colorways, LinkBuds Fit + accessories
  combos (Sony Panama store), the NZ EAN 4548736157897.
- Sony Access Controller, White (retail MPN 1000037579, CFI-ZAC1)
  — identifiers PENDING: retail MPN 1000037579 confirmed (Best
  Buy US Model, SKU 12348387) and hardware model CFI-ZAC1
  confirmed (playstation.com + SIE manuals), but no UPC was
  verified from a US source. The only barcode seen, 711719567929,
  is a UK EAN (Very.co.uk) with no US source and was not copied.
  Quotes (3): PlayStation Direct $89.00 (page-verified, Color:
  White, release 12/06/2023; stock not stated in the page-text
  crawl), GameStop $89.99 (feed row — suspected), Target $87.99
  (Target search listing — suspected). Correction vs the
  2026-10-31 candidate price: $89 is $89.00 direct / $89.99 list
  (Best Buy comp value $89.99). Excluded: Best Buy $79.95 (sold
  by marketplace seller A2Z Games Inc, DECISIONS 021), CDW
  $117.99 (inflated vs list), Siemens industrial "access
  controller" rows (different products), the $250 961souq row
  (non-US). White is the only colorway.
- Logitech POP Keys, Cosmos (920-011233) — identifiers PENDING:
  MPN 920-011233 confirmed (Dell US Manufacturer Part Number +
  Colamco + BuyDig + iFixit agree; logitech.com product URL
  carries .920-011233), but the UPC 097855179401 appears only on
  the Amazon listing (ASIN B0BMX9KRDN), with no second US source,
  so identifiers stay empty per the Wave Keys precedent. Quotes
  (3): Logitech direct $99.99 (page-verified JSON-LD InStock;
  Color Cosmos), Dell $89.99 (feed row, brand_direct — suspected;
  sale off the $99.99 list), Colamco $99.99 (search-verified, MPN
  920-011233 stated). Correction vs the 2026-10-31 candidate note:
  $99.99 is confirmed current. Excluded: Blast Yellow 920-010707
  (Best Buy $69.99 sale), Heartbreaker Rose 920-010709 ($117.22),
  Mist 920-011232, Daydream, the POP Icon Keys line ($49.99),
  POP Mouse rows ($29.99–$39.99), the AU Cosmos Lavender
  920-011227 (GTIN 097855179340), the POP Keys + POP Mouse combo,
  Target $111.22 (marketplace seller Mega Retail Store), the
  920-010817 feed row (not Cosmos — Cosmos is 920-011233).
- Xbox Elite Wireless Controller Series 2 – Core, White
  (4IK-00001) — identifiers PENDING: MPN 4IK-00001 confirmed
  (Best Buy US Model + P.C. Richard MODEL + ThinkEdu + Microsoft
  Store agree), but the UPC was not verified from a US source.
  The only barcodes seen conflict and are both non-US: Gamesmen
  AU 889842717082 vs a Latvian listing 889842717075; neither was
  copied. Quotes (3): Microsoft direct $111.74 (page-verified
  JSON-LD price; stock not confirmed in the page text), Best Buy
  $149.99 (Model 4IK-00001, SKU 6514400, price shown on the Best
  Buy reviews-page crawl), P.C. Richard $149.99 (MODEL:
  4IK-00001, JSON-LD). Correction vs the 2026-10-31 candidate
  range $111.74–$139.99: $111.74 is the current Microsoft Store
  sale price and $149.99 is the current retailer list (Kohl's and
  Lenovo also $149.99; Target lists it at $109.99); the $139.99
  ShopCGX feed row is titled "Series 2", not Core, and was not
  used. Excluded: the full Elite Series 2 Black (FST-00001,
  $159.99–$179.99), the 2025 Core colorways (Blue, Red and Blue,
  Green and Blue, Astral Purple, Gray, Dark Green, all $149.99
  at Best Buy), the $289.98 dual-controller bundle, NFM $106.99
  sale (unverified), DreamController custom-painted rows
  ($279.99–$299.99).
- Eval on the new snapshot: 77 models, 62 verified identifiers, 5
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 72 →
  77 / 60 → 62 for the approved expansion).

## 049 — 2026-11-06: Expansion batch 11 — 77 → 82 models (DECISIONS 033)

- Membership check (against the 77-model set, by name, MPN and UPC —
  no matches, all 5 are new lines):
  - Magic Trackpad USB-C White (MXK93AM/A, UPC 195949654305) vs
    apple-magic-mouse-usbc (MXK53AM/A, UPC 195949655883): the
    set's only Apple pointing device is the Magic Mouse; the
    Trackpad is the distinct glass-trackpad line, different MPN
    and UPC — not a duplicate. The Black trackpad (MXKA3AM/A,
    $149) is a different colorway and was not added.
  - WH-CH720N Black (WHCH720N/B, UPC 027242925397) vs
    sony-wh1000xm5-black, sony-wh1000xm6-black,
    sony-wh1000xm4c-black, sony-ult-wear-black (WHULT900N/B, UPC
    027242928688): distinct lightweight mid-range
    noise-cancelling line (WH-CH720N, 2023, Integrated
    Processor V1), different model number and UPC — not a
    duplicate. Blue/White/Pink are different colorways and
    were not added.
  - G915 X LIGHTSPEED full-size Tactile Black (920-012670, UPC
    097855195005) vs logitech-mx-mechanical-tactile-quiet-
    graphite (920-010547), logitech-mx-keys-s-pale-grey
    (920-011559), logitech-mx-keys-mini-black (920-010475),
    logitech-ergo-k860-graphite (920-009166), logitech-wave-
    keys-graphite (920-011898), logitech-pop-keys-cosmos
    (920-011233): no G915 line in the set; distinct Logitech
    G low-profile wireless gaming keyboard, different MPN —
    not a duplicate. The Linear (920-012696), Clicky
    (920-012704), TKL and wired variants are different
    configurations and were not added.
  - Xbox Adaptive Controller White (JMU-00003) vs
    xbox-wireless-controller-black (1914, UPC 196388518159),
    xbox-elite-series-2-black (FST-00001, UPC 889842196344),
    xbox-elite-series-2-core-white (4IK-00001): no
    accessibility controller in the set; the Adaptive
    Controller is the large-button hub for external switches,
    different MPN from every controller in the set — not a
    duplicate. The Adaptive Joystick ($29.99) and Adaptive
    Dual Button ($59.99) are companion accessories, not the
    controller, and were not added.
  - Keychron K8 hot-swappable Red (K8-G1, UPC 617748997921) vs
    keychron-k8-he-special-black (K8H-F1, EAN 4894979028990),
    keychron-k8-ultra-8k (K8U-J1, EAN 4894979057969): distinct
    base K8 line — the original tenkeyless keyboard, not the
    Hall Effect or 8K-polling successor — different SKU and
    barcode — not a duplicate. The K8 Max, K8 Pro and K8 HE
    lines are different models and were not added.
- Apple Magic Trackpad (USB-C), White Multi-Touch Surface
  (MXK93AM/A) — identifiers VERIFIED: UPC 195949654305 (Apple US
  official store page for MXK93AM/A, Part Number UPC or EAN No.:
  195949654305 + Adorama US spec, SKU ACMXK93AMA, MFR MXK93AM/A,
  UPC 195949654305 + eBay US product identifiers, GTIN
  0195949654305, MPN MXK93AMA, agree), MPN MXK93AM/A (Apple +
  Adorama agree). Quotes (3): Apple direct $129.00 (US store
  page JSON-LD, InStock, page-verified 2026-11-06), CDW $129.00
  (feed row, White/Silver, authorized retailer — suspected, no
  identifier in the feed row), Target $129.99 (feed row, White
  Multi-Touch Surface, authorized retailer — suspected).
  Correction vs the 2026-10-31 candidate price: $129 is the White
  price; the Black trackpad (MXKA3AM/A) is $149 at Apple direct,
  Staples and P.C. Richard ($149.99 at Best Buy). Excluded: Black
  rows ($149/$149.99), iStyles skins ($13.59–$15.99, accessories),
  non-US rows (961souq $230, icon.co.cr $174.99/$184.99,
  soytechno $268), bkstr campus-store $129 rows (same price, not
  needed), DataVision White $134 (not needed).
- Sony WH-CH720N, Black (WHCH720N/B) — identifiers VERIFIED: UPC
  027242925397 (B&H Photo US spec page, BH #SOWHCH720NB, UPC
  027242925397 + eBay US product identifiers, MPN WH-CH720N/B,
  UPC 027242925397 + Ubuy, Model WHCH720N/B, UPC 027242925397 +
  Amazon.ca, Model WHCH720N/B, UPC 027242925397, ASIN B0BS1QCFHX,
  agree), MPN WHCH720N/B (Sony US page + B&H + Crutchfield MFR #
  agree). Quotes (3): Sony direct $89.99 (electronics.sony.com
  WHCH720N/B page, JSON-LD $89.99, Save $90.00 off $179.99; free
  shipping, est. delivery Nov 3-4, page-verified 2026-11-06),
  BJ's $179.99 (feed row, authorized retailer — suspected),
  P.C. Richard $179.95 (feed row, WHCH720N-B, authorized
  retailer — suspected). Correction vs the 2026-10-31 candidate
  price: $89.99 is the current Sony direct sale price, not a
  stale figure — the launch MSRP was $149.99 (Sony press release
  2023-02-21) while Sony's own page now lists MSRP $179.99 and
  a $90 saving; retailer street price is $178–$180 (B&H $178.00
  InStock, page crawled 2026-09-12 — dated; OfficeDepot $179.99
  also seen). Excluded: DataVision $130 (condition not asserted,
  BUILD_LOG 012 precedent), BuyDig $129.99 E993 kit SKU (bundle,
  not the bare unit), the +26-month-extended-warranty bundle
  $129.99, Newegg rows (Blue $179.99, WHCH720NL Blue $195.99,
  $160.99/$140.99 seller-ambiguous), GearOne $201.56 (inflated),
  shopcgx $69.99 (below cost, suspicious), pens.com $981.05
  (garbage), Target $183.34 (not needed), iCuracao $179.99
  (non-US), the Blue WHCH720N/L UPC 027242925502 and the EU
  WHCH720NB.CE7 EAN 4548736142428 (different variants).
- Logitech G915 X LIGHTSPEED, Full-size, GL Tactile (Brown),
  Black (920-012670) — identifiers VERIFIED: UPC 097855195005
  (B&H Photo US spec page for 920-012670 + Abt US, Model
  920-012670, UPC 097855195005, Tactile Wireless in Black +
  Amazon US, Model 920-012670, UPC 097855195005, ASIN B0DB1WNZJY
  + Desertcart, Mfr Part 920-012670, UPC 097855195005, agree),
  MPN 920-012670 (Best Buy US Model + Quill + B&H agree).
  Quotes (3): Logitech G direct $259.99 (logitechg.com
  .920-012670 page, JSON-LD InStock, page-verified 2026-11-06;
  Color Black), Best Buy $259.99 (Model 920-012670, SKU
  6595193, Sold by Best Buy, JSON-LD InStock, page-verified
  2026-11-06), B&H $219.99 (sale, was $259.99, In Stock,
  search-index). Correction vs the 2026-10-31 candidate price:
  $129.99 was an Amazon Clicky-switch deal price (Grail Alerts
  2026-11-01; pricehistory.app Clicky 920-012704 at $129.99),
  not the standard US Tactile price. Variant pinning, recorded
  explicitly: logitechg.com defaults to the full-size
  LIGHTSPEED line at $259.99 with per-switch URLs (.920-012670
  Tactile, .920-012696 Linear UPC 097855195166, .920-012704
  Clicky UPC 097855195029); the pinned variant is the Tactile
  (Brown) full-size Black, the line's standard US variant.
  Excluded: Clicky 920-012704 and Linear 920-012696 (both
  $259.99, different switches), TKL Tactile 920-012726
  ($229.99), wired Linear 920-012950 ($199.99; $169.99 at
  Staples), the feed's Best Buy $259.99 Tactile row (White
  variant, SKU 6595195, 920-012685 — not used for the Black
  price), Lenovo brand_direct rows (variant-ambiguous across
  the three switch types), Ayoub $143 (non-US), fnac $173.16
  (non-US marketplace). Quill $259.99 (Model 920-012670) also
  seen as corroboration.
- Microsoft Xbox Adaptive Controller, White (JMU-00003) —
  identifiers PENDING: retail MPN JMU-00003 confirmed (Best Buy
  US current listing, Model JMU-00003, SKU 6455394, Sold by Best
  Buy, $99.99, JSON-LD InStock; Microsoft Store product page
  $99.99, xbox.com JSON-LD InStock), but the UPC is unresolved:
  889842295368 (eBay product identifiers, GTIN 0889842295368,
  MPN JMU-00003) vs 889842439038 (PriceCharting, model 1836;
  also an eBay listing ties this code to JMU-00003) — two codes
  circulate for the same MPN and no US retailer spec page
  states a UPC, so identifiers stay empty per the DualSense
  Edge / DEX / Neo / PULSE Elite precedent. The older Best Buy
  listing JMU-00001 (SKU 6381218) is no longer available in new
  condition and was not used. Quotes (2): Microsoft direct
  $99.99 (microsoft.com / xbox.com JSON-LD; stock not confirmed
  in the microsoft.com page text — price-only), Best Buy $99.99
  (Model JMU-00003, SKU 6455394, JSON-LD InStock). Correction
  vs the 2026-10-31 candidate price: $99.99 is confirmed current
  at both Microsoft Store and Best Buy. Excluded: CDW $128.99
  and BuyDig $124.99 (above list), FlexShopper $123.99
  (marketplace, DECISIONS 021), the Adaptive Joystick ($29.99)
  and Adaptive Dual Button ($59.99, different accessories).
- Keychron K8, White Backlight, Keychron Super Switch
  (Hot-Swappable), Red (K8-G1) — identifiers VERIFIED: UPC
  617748997921 (Keychron official store public product JSON,
  product id 4669741170777, variant 32018252791897, SKU K8-G1,
  barcode 617748997921, $69.99 + Desertcart spec table, Mfr Part
  Number K8 G1, UPC 617748997921, ASIN B0875W65Z2, agree), SKU
  K8-G1 (Keychron JSON + Desertcart agree). Quotes (1): Keychron
  direct $69.99 (keychron.com K8 page, variant K8-G1,
  price-only: K8-G1 shows out of stock in the 2026-11-06 JSON
  read but was Available in the search-index crawl 2 days
  earlier, and the Blue/Brown hot-swappable siblings K8-G2/K8-G3
  are in stock — inventory churn, not discontinuation). Variant
  pinning: the base K8 line has 36 variants (White/RGB
  backlight, plastic/aluminum frame, Gateron G Pro / Keychron
  Super / Gateron Optical / Keychron Optical, Red/Blue/Brown);
  the pinned variant mirrors the K8 Pro precedent
  (hot-swappable, White Backlight, Red). The page-default K8-A1
  (White Backlight, Gateron G Pro Mechanical, Red, $59.99,
  barcode 4897115556074) is the soldered version, not
  hot-swappable, and is also out of stock in this read, so it
  was not pinned; the RGB hot-swappable Red K8-H1 ($79.99, in
  stock, barcode 617748997952) and the aluminum-frame variants
  ($79.99–$89.99) are different configurations. Correction vs
  the 2026-10-31 candidate price: the base K8 starts at $59.99
  (K8-A1) and the hot-swappable Red is $69.99. The old-K8
  barcode 753610396260 does not appear in the current JSON and
  was not used; 617748997846 is K8-A2 (Blue, Gateron G Pro), a
  different variant. Excluded: Newegg K8 rows ($127.99 Version
  2 QMK, $126.55 White Backlight — third-party/unclear variant,
  DECISIONS 021), Newegg K8 HE $221.48 and K8 Pro $217.91
  (different models), Woot $39.99 (deal/clearance, variant
  ambiguous, 90-day warranty). Like the K8 HE, the base K8 is
  sold through Keychron's own store only, so it holds a single
  quote.
- Eval on the new snapshot: 82 models, 66 verified identifiers, 5
  with quotes, 12 total quotes, 0 identifier-matched, 12 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 77 →
  82 / 62 → 66 for the continuous expansion).

## 050 — 2026-11-06: Expansion batch 12 — 82 → 87 models (DECISIONS 034)

- Membership check (against the 82-model set, by name, MPN and UPC —
  run programmatically against price_agent/catalog.py, no matches,
  all 5 are new lines):
  - Magic Keyboard Touch ID + Numeric Keypad White (MJM64LL/A, UPC
    195951258324) vs apple-magic-mouse-usbc (MXK53AM/A, UPC
    195949655883) and apple-magic-trackpad-usbc (MXK93AM/A, UPC
    195949654305): the set has no keyboard from Apple at all; the
    Keyboard is the distinct typing line, different MPN and UPC —
    not a duplicate. The Black Keys MJM74LL/A ($199) is a different
    colorway and was not added; the older MXK73LL/A is a superseded
    part number for the same White variant, not a separate model.
  - WF-C710N Black (WFC710N/B, UPC 027242931770) vs
    sony-wf1000xm5-black (UPC 027242923232) and sony-wf1000xm6-black
    (UPC 027242933460): the C710N is Sony's everyday mid-range
    noise-cancelling earbud line, different MPN and UPC — not a
    duplicate. White (UPC 027242931794), Glass Blue (027242931817)
    and Pink are different colorways and were not added.
  - LinkBuds Open Black (WFL910/B, UPC 027242928695) vs
    sony-linkbuds-fit-black (WFLS910N/B, UPC 027242929289): the Open
    is the distinct open-ring open-ear line, different MPN and UPC
    — not a duplicate. The LinkBuds Clip (WFLC900, 2026 clip-on
    line) is a different model and was not added. White (UPC
    027242928701) is a different colorway and was not added.
  - PRO X TKL LIGHTSPEED Tactile Black (920-012127, UPC
    097855188984) vs logitech-g915-x-lightspeed-tactile-black
    (920-012670, UPC 097855195005), logitech-g-pro-x-superlight-2-
    black (910-006628) and -dex-black: the PRO X TKL is Logitech
    G's standard tenkeyless wireless gaming keyboard, different MPN
    and UPC from the low-profile G915 X and the Superlight mice —
    not a duplicate. White 920-012143 and Magenta 920-012154 are
    different colorways, Linear Black 920-012122 a different switch,
    the PRO X TKL RAPID (920-013131) a different wired Hall-Effect
    model, the PRO X 60 a different 60% model — none added.
  - Keychron Q1 Knob Navy Blue Red (Q1-O1Z, EAN 4895248817345) vs
    keychron-k8-hot-swappable-red (K8-G1, UPC 617748997921),
    keychron-k8-he-special-black (K8H-F1) and keychron-k8-ultra-8k
    (K8U-J1): the Q1 is the original 75% full-aluminum Q-series
    line, different SKU and barcode from every K8 line — not a
    duplicate. The Q1 Pro / Max / HE / Ultra 8K are different models
    and were not added.
- Apple Magic Keyboard with Touch ID and Numeric Keypad, US English,
  White Keys (MJM64LL/A) — identifiers PENDING: MPN MJM64LL/A
  confirmed (Apple US store page + Best Buy US Model MJM64LL/A, SKU
  6556937 agree), but UPC 195951258324 is stated on the Apple US
  store page only — no second source surfaced (Adorama lists the
  older MXK73LL/A, Best Buy shows no UPC), so identifiers stay empty
  per the Adaptive Controller / DualSense precedent. Quotes (3):
  Apple direct $179.00 (JSON-LD InStock, page-verified), Best Buy
  $179.99 (Model MJM64LL/A, SKU 6556937, Sold by Best Buy), NFM
  $180.00 (feed row — suspected). Correction vs the 2026-10-31
  candidate range $99-$199: $99 is the plain Magic Keyboard and
  $129 the Numeric-Keypad-only Lightning model — different models;
  the pinned Touch ID + Numeric Keypad USB-C White is $179. The
  2026 MJM64LL/A supersedes MXK73LL/A (Adorama $179.00, on backorder
  to 01/2027). Excluded: Black Keys MJM74LL/A $199 (different
  colorway), plain Magic Keyboard $99 and iPad Magic Keyboards
  $269/$319 (different models), Sweetwater $199 Black Keys (different
  colorway).
- Sony WF-C710N, Black (WFC710N/B) — identifiers VERIFIED: UPC
  027242931770 (Amazon US product info, Model WFC710N/B, UPC
  027242931770, ASIN B0DWHPBK42 + Snapklik, Model WFC710N/B, UPC
  027242931770 + Beach Camera Meta Catalog feed row, brand field
  027242931770, agree), MPN WFC710N/B (Sony + Best Buy agree).
  Quotes (5): Best Buy $98.00 (Model WFC710N/B, SKU 6620461, Sold by
  Best Buy, JSON-LD InStock, page-verified), Dell $129.99 (feed row,
  Black), Beach Camera $98.00, Crutchfield $98.00, Abt $98.00 (feed
  rows, Black). Correction vs the 2026-10-31 candidate price: $129.99
  is the list price (Sony US store); the current street/sale price
  is $98. Sony direct Black price was not freshly confirmed (the
  Sony Black page crawl is stale at the $119.99 launch price; the
  White page shows a $99.99 sale) and is not quoted. Excluded:
  Target $78.99 Pink, Best Buy White $128 / Glass Blue $129.99
  (different colorways), bundle rows, iCuracao / Ayoub / TechStop
  (non-US), Snapklik $124.98/$129.98 (aggregator, seller unclear),
  Macy's $98.00 (shipped/sold by Focus Camera via Macy's storefront).
- Sony LinkBuds Open, Black (WFL910/B) — identifiers VERIFIED: UPC
  027242928695 (Amazon US product info, Model WFL910B.UC, UPC
  027242928695, ASIN B0DGVH7FJV + Simcoe Audio Video, authorized
  Sony dealer, Barcode 027242928695, Black + Ubuy, UPC
  027242928695, Model WFL910B.UC, agree), MPN WFL910/B (Sony + Best
  Buy + Crutchfield agree). Note: an early guess of 027242928694 for
  the Black UPC was wrong — the verified code ends 8695; the guess
  was never recorded. Quotes (4): Sony direct $229.99 (JSON-LD,
  'Only 3 left', page-verified), Dell $229.99 (feed row, Black),
  Best Buy $228.00 (feed row, Black), BuyDig $228.00 (Part #
  WFL910/B, In Stock, page-verified). Correction vs the 2026-10-31
  candidate price: $229.99 is confirmed current at Sony direct and
  Dell. Excluded: bkstr $199.99 (below-list edu-store price, variant
  unconfirmed), FlexShopper $199.99 (marketplace), Macy's $228
  bundle, Beach Camera $239.99 (above list, warranty bundle),
  andreselectronicexperts $29,999 (garbage), LinkBuds Clip rows
  (different model), White rows (different colorway), StackSocial
  open-box $89.99 (not new).
- Logitech PRO X TKL LIGHTSPEED, GX Brown Tactile, Black
  (920-012127) — identifiers PENDING: MPN 920-012127 confirmed
  (Best Buy US Model 920-012127, SKU 10111534 + BuyDig Part #
  920-012127 + manuals.plus spec table + Amazon US ASIN B0BQBSH6NQ
  agree), but UPC 097855188984 appears in eBay product identifiers
  only — no second source surfaced, so identifiers stay empty per
  the Adaptive Controller / DualSense precedent. Quotes (3): Lenovo
  US $219.99 (Black, page-verified 'Available Soon' — price-only,
  stock not confirmed), Focus Camera $219.99 (920-012127, feed row),
  CDW $219.99 (feed row). Correction vs the 2026-10-31 candidate
  price: $219.99 is confirmed as the current list (launch SRP was
  $199); the Logitech G direct US price was not confirmed in page
  text. Excluded: Newegg $299.99 (above list), Compsource Black
  920-012118 $257.17 (above list, OutOfStock, different/older Black
  listing), Woot Magenta open-box $109.99 (deal/clearance, different
  colorway), Target $202.99 (sold by antonline — marketplace),
  Rakuten Magenta $219.99 and Best Buy White $151.99 / Magenta
  $189.99 sale rows (different colorways), shopabunda Linear $164.99
  (different switch, fulfilled by Amazon), PRO X TKL RAPID and PRO
  X 60 rows (different models).
- Keychron Q1 Version 2, Fully Assembled Knob, Navy Blue - B,
  Gateron G Pro Red (Q1-O1Z) — identifiers PENDING: SKU Q1-O1Z and
  EAN 4895248817345 come from the Keychron official store public
  product JSON only (product id 7043863576665, variant 39974600015961,
  available:true, $89.99, compare $189.99) — no second source
  surfaced, so identifiers stay empty per the Adaptive Controller /
  DualSense precedent. Quotes (1): Keychron direct $89.99 (sale, was
  $189.99, JSON available:true, page-verified 2026-11-06). Variant
  pinning: the page-default in-stock variant — Fully Assembled Knob
  / Navy Blue - B / Gateron G Pro Red; the Carbon Black knob Red
  Q1-M1Z (EAN 4895248817284) and all Carbon Black / Silver Grey knob
  variants are out of stock in this read, while Navy Blue - B
  Red/Blue/Brown and the Barebone Knob Carbon Black / Navy Blue are
  in stock. Correction vs the 2026-10-31 candidate range
  $229.99-$254.99: that was the Q-line range (the Q1 Max is $229.99),
  not the base Q1 — the base Q1 V2 fully assembled knob lists
  $189.99 and is currently $89.99 on sale. Excluded: Woot $79.99
  (deal/clearance, Blue switch — different switch), Q1 Pro/Max/HE/
  Ultra 8K rows (different models), Q1 plates and keycap sets
  (accessories), Q1 barebone rows ($59.99-$85.99, different
  configurations). Like the K8, the base Q1 is sold through
  Keychron's own store only, so it holds a single quote.
- Eval on the new snapshot: 87 models, 68 verified identifiers, 5
  with quotes, 16 total quotes, 0 identifier-matched, 16 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 82 →
  87 / 66 → 68 for the continuous expansion).

## 051 — 2026-11-06: Expansion batch 13 — 87 → 92 models (DECISIONS 035)

- Membership check (against the 87-model set, by name, MPN and UPC —
  run programmatically against price_agent/catalog.py, no matches,
  all 5 are new lines):
  - MacBook Pro 14 PROLED XDR (MJ2K4LL/A, UPC 195951196749) vs
    apple-macbook-pro-14-m6 (MHWT4LL/A, UPC pending): the set's M6
    is the separate entry-level M6 line ($1,999, 16GB/1TB); the
    PROLED XDR is the distinct touchscreen tandem-OLED line with
    M5 Pro silicon, different MPN — not a duplicate. The Liquid
    Retina XDR M5 Pro 24GB/1TB (MGDR4LL/A, $2,499) is a different
    display line and was not added; the 16-inch, M5 Max, 48GB/1TB
    MMF64LL/A and Nano-texture configurations are different
    configurations and were not added.
  - WF-C510 Black (WFC510/B, UPC 027242930339) vs
    sony-wf-c710n-black (WFC710N/B, UPC 027242931770) and
    sony-wf1000xm5-black / sony-wf1000xm6-black: the C510 is Sony's
    compact everyday budget earbud line (2024, no noise
    cancelling), different MPN and UPC — not a duplicate. White
    (UPC 027242930346), Blue and Yellow are different colorways
    and were not added.
  - INZONE H5 Black (WHG500/B, UPC 027242927919) vs
    sony-pulse-elite-midnight-black and sony-pulse-explore-midnight-
    black: the set has no INZONE model at all; the H5 (WH-G500,
    2023) is Sony's mid-range wireless gaming headset, different
    MPN and UPC from the PULSE headsets — not a duplicate. White
    (UPC 027242927896) is a different colorway and was not added;
    the INZONE Buds (WF-G700N) and INZONE H9 are different models
    and were not added.
  - PRO X2 SUPERSTRIKE Lunar Eclipse (910-007700, UPC
    097855211309) vs logitech-g-pro-x-superlight-2-black
    (910-006628, UPC 097855177797), logitech-g-pro-x-superlight-2-
    dex-black and logitech-g915-x-lightspeed-tactile-black
    (920-012670): the Superstrike is Logitech G's haptic-trigger
    (HITS) PRO mouse line, different MPN and UPC from the
    Superlight mice and the G915 X keyboard — not a duplicate. The
    newer PRO X3 SUPERSTRIKE (910-007876, $199.99) is a different
    model and was not added; the EU/Asia 910-007777 / 910-007778
    are different regional part numbers and were not added.
  - Keychron B40 Deep Black (B40-K9, no UPC/EAN) vs
    keychron-k8-hot-swappable-red (K8-G1, UPC 617748997921),
    keychron-k8-he-special-black (K8H-F1), keychron-k8-ultra-8k
    (K8U-J1) and keychron-q1-knob-navy-blue-red (Q1-O1Z): the B40
    is Keychron's budget 75% Alice scissor-switch line, different
    SKU from every K8/Q1 line — not a duplicate. The B39 (96%
    Alice, $54.99, B39-K9) is the larger sibling, a different
    model, and was not added.
- Apple MacBook Pro 14-inch with PROLED XDR Display, M5 Pro
  15-core/16-core, 24GB/1TB, Space Black, Standard display
  (MJ2K4LL/A) — identifiers PENDING: MPN MJ2K4LL/A confirmed by
  Best Buy US only (Model MJ2K4LL/A, SKU 6565892; the AU/NZ
  MJ2K4X/A is the same configuration in a different region suffix),
  and UPC 195951196749 is stated in the Adorama spec table only —
  no second source surfaced for either, so identifiers stay empty
  per the Adaptive Controller / DualSense precedent. Quotes (2):
  Apple direct $2,899.00 (US store buy page, "Available starting
  11.6", page-verified — price per the Apple announcement and Best
  Buy, not shown in the page text), Best Buy $2,899.00 (Model
  MJ2K4LL/A, SKU 6565892, Sold by Best Buy, JSON-LD InStock,
  page-verified; free $100 e-gift card promo). Correction vs the
  2026-10-31 candidate note "from $2,899 (pre-order 11.6)":
  confirmed current, on sale from 2026-11-06, and the base 14-inch
  runs M5 Pro — not M6. Excluded: NFM $3,699 48GB/1TB and $3,294
  Silver 2TB (different configurations), all Meta Catalog rows for
  other PROLED configs (16-inch, M5 Max, Nano-texture), the
  Liquid Retina M5 Pro rows (MDE34LL/A / MGDR4LL/A, $2,199-$2,499
  — a different display line), dbrand skins (accessories).
- Sony WF-C510, Black (WFC510/B) — identifiers PENDING: MPN
  WFC510/B confirmed (Best Buy US Model WFC510/B, SKU 6594425 +
  B&H + Sony AU Model WFC510B agree), but UPC 027242930339 is
  stated on the B&H spec page only — no second non-Amazon US
  source surfaced, so identifiers stay empty per the Adaptive
  Controller / DualSense / PULSE Elite precedent. Quotes (6):
  Best Buy $59.99 (Model WFC510/B, SKU 6594425, JSON-LD InStock,
  page-verified), B&H Photo $58.00 (In Stock, was $68.00,
  page-verified), Abt $58.00 (feed row; manufacturer rebate ends
  11/08/2026, comp. value $68), Electronic Express $58.00 and
  Focus Camera $58.00 (feed rows, Black), Fred Meyer $69.99
  (JSON-LD InStock, page-verified — the list price). Correction vs
  the 2026-10-31 candidate price $69.99: that is the list price —
  the current street price is $58. Sony direct Black price was not
  freshly confirmed (no current US Sony store page surfaced) and is
  not quoted. Excluded: ShopMyExchange $49.99 (military exchange,
  restricted eligibility), Newegg $58 rows (seller unclear —
  marketplace risk), Sweetwater $48.00 (backordered + $20-off
  promo), Macy's $68 Yellow and shop.simon $58 Yellow (different
  colorway + marketplace), Ayoub $52 / iCuracao $69.99 (non-US),
  White/Blue/Yellow rows (different colorways).
- Sony INZONE H5, Black (WHG500/B) — identifiers PENDING: MPN
  WHG500/B confirmed (Best Buy US Model WHG500/B, SKU 6562125 +
  Crutchfield MFR # WHG500/B + Abt agree), but UPC 027242927919
  appears in the Sony spec sheet via manuals.plus only — no second
  non-Amazon US source surfaced, so identifiers stay empty per the
  Adaptive Controller / DualSense / PULSE Elite precedent. Quotes
  (3): Focus Camera $128.00 (Black, $128 vs $178, page-verified —
  the feed row for the same URL was $178, so the price has dropped
  since the feed was cut), Datavision $128.00 (feed row, Black),
  Abt $128.00 (page-verified — price-only: "Notify me when this
  item is available", PreOrder; rebate ends 11/22/2026, comp.
  value $178). Correction vs the 2026-10-31 candidate price
  ~$249.99: that matches no current US price — the current street
  price is $128 (comp. value $178); Sony direct lists the White at
  $159.99 sale / $179.99 original (stale category crawl; the Black
  direct price was not confirmed) and is not quoted. Excluded:
  Focus Camera White $128 and Sweetwater White $178 (different
  colorway), INZONE Buds rows ($159.99-$239.99, WF-G700N) and
  INZONE H9 rows (different models), Crutchfield (no price in the
  76-day-old crawl), Best Buy (price not confirmed in page text).
- Logitech PRO X2 SUPERSTRIKE LIGHTSPEED, Lunar Eclipse
  (910-007700) — identifiers PENDING: MPN 910-007700 confirmed
  (B&H + Abt + Electronic Express agree), but UPC 097855211309 is
  stated on the B&H spec page only — no second non-Amazon US
  source surfaced, so identifiers stay empty per the Adaptive
  Controller / DualSense / PULSE Elite precedent. Quotes (5):
  B&H Photo $179.99 (In Stock, page-verified), Abt $179.99
  (Lunar Eclipse, search-index read), Target $179.99, Lenovo
  $179.99 and Electronic Express $179.99 (feed rows, Lunar
  Eclipse). Correction vs the 2026-10-31 candidate note: the
  candidate called this a gaming keyboard — it is a MOUSE (HITS
  haptic triggers, HERO 2, 8 kHz, 61 g, white casing / black
  buttons, the only US colorway). The Logitech G direct US price
  was not confirmed in page text (Notebookcheck reports $179.99
  at the Logitech online store). Excluded: Best Buy $199.99 PRO
  X3 SUPERSTRIKE (910-007876, newer successor, different model),
  Etsy $15 (marketplace), Lethal.gg mouse skates/grips
  (accessories for the Superlight, not the mouse), Newegg $179.99
  (seller unclear — marketplace risk).
- Keychron B40, 75% Alice, Deep Black (B40-K9) — identifiers
  PENDING: SKU B40-K9 comes from the Keychron official store page
  only and no UPC/EAN for the B40 surfaced anywhere, so
  identifiers stay empty per the Adaptive Controller / DualSense
  precedent. Quotes (1): Keychron direct $49.99 (Deep Black
  variant Available, page-verified 2026-11-06). Variant pinning:
  Deep Black is the only colorway sold. Correction vs the
  2026-10-31 candidate price: $49.99 is confirmed current at
  Keychron direct. Excluded: B39 $54.99 (larger 96% sibling,
  different model), B1/B2/B3/B4 Pro rows (different lines), Q/V/K
  rows in the same feed (different models). Like the K8 and Q1,
  the B40 is sold through Keychron's own store only, so it holds a
  single quote.
- Eval on the new snapshot: 92 models, 68 verified identifiers, 5
  with quotes, 17 total quotes, 0 identifier-matched, 17 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 87 →
  92 / verified stays 68 for the continuous expansion; the pending
  set gains the 5 new keys).

## 052 — 2026-11-06: Expansion batch 14 — 92 → 96 models (DECISIONS 036)

- Membership check (against the 92-model HEAD set, by name, MPN and
  UPC — run programmatically against git HEAD price_agent/catalog.py
  before adding anything; no catalog keys matched, all 5 are new
  lines):
  - Apple Pro Display XDR (MWPE2LL/A standard glass / MWPF2LL/A
    nano-texture, $4,999 / $5,999) vs
    apple-studio-display-2026-standard-tilt (MFEX4LL/A, UPC
    195950529173): no match on any field — but NOT ADDED (see below).
    The set's Studio Display 2026 is the separate non-XDR line
    ($1,599, A19, Thunderbolt 5); the Studio Display XDR (from
    $3,299) is a third, distinct line and was not substituted in.
  - Sony MDR-7506 (MDR7506) vs every Sony headphone in the set
    (WH-1000XM5/XM6, WH-1000XM4C, WH-CH720N, ULT WEAR, INZONE H5,
    PULSE Elite/Explore): the set has no MDR model at all; the
    MDR-7506 is Sony's pro studio monitor line, different model
    from every WH/INZONE/PULSE line — not a duplicate. The MDR-V6
    (discontinued 2020) is a different model and was not added.
  - Sony PlayStation Pulse Wireless Headset, White (2026, $99.99,
    pre-order) vs sony-pulse-elite-midnight-black (retail MPN
    1000044173, CFI-ZWH2) and sony-pulse-explore-midnight-black
    (1000044170, CFI-ZWE1): the new Pulse is the base
    planar-magnetic headset line below the Elite, different model
    from both — not a duplicate. The PULSE 3D (CFI-ZWH1, 2020,
    $99.99) is a different, older model and was not added; the
    Pulse Edge (ANC, early 2027, no price yet) is a different model
    and was not added.
  - Sony LinkBuds Clip Black (WFLC900/B, UPC 027242934054) vs
    sony-linkbuds-fit-black (WFLS910N/B, UPC 027242929289) and
    sony-linkbuds-open-black (WFL910/B, UPC 027242928695): the Clip
    (WF-LC900, 2026 clip-on open-ear) is a distinct line, different
    MPN and UPC — not a duplicate. The only HEAD mention of the
    Clip is a notes reference in the Open entry ("a different model
    and was not added") — no catalog key. Greige (UPC
    027242934177), Green and Lavender are different colorways and
    were not added.
  - Nintendo 64 Controller, Gray (HAC-043, Nintendo SKU 128577,
    UPC 00045496894948) vs nintendo-joy-con-2-pair-light-blue-
    light-red, nintendo-joy-con-pair-neon-red-neon-blue and
    nintendo-switch-pro-controller (HACAFSSKA, UPC 045496590161):
    the N64 controller is the distinct retro NSO controller line,
    different model — not a duplicate. Third-party N64-style pads
    (Retro Fighters Brawler64, 8BitDo 64, Retro-Bit Tribute) are
    different models and were not added.
- Apple Pro Display XDR — NOT ADDED: discontinued March 3, 2026
  (EveryMac: "Discontinued Date: March 3, 2026"; AppleInsider: "A
  March 2026 revision introduced the Studio Display XDR, which
  replaced the Pro Display XDR in the lineup"; photoworkout: "The
  old Pro Display XDR ($4,999) is officially discontinued") and
  Apple no longer sells it — apple.com/shop/buy-mac/pro-display-xdr
  now serves the "Buy Studio Display XDR" page. The Meta Catalog
  feed for the query returns Studio Display XDR rows (Apple direct
  MFEP4LL/A nano-texture tilt-height $3,599, MFEQ4LL/A nano VESA
  $3,199; Sweetwater standard-glass tilt-height $3,299; Sam's Club
  $3,299) plus one $4,999 row from mtsproservices.com, an
  unverifiable merchant — not a first-party/retailer-direct quote.
  The $3,299 candidate figure is the Studio Display XDR launch
  price, not a Pro Display XDR configuration. The Studio Display
  XDR (27-inch 5K mini-LED, 120Hz, from $3,299) is a candidate for
  a future batch, not substituted here. No catalog entry, no
  snapshot model.
- Sony MDR-7506, Black (MDR7506) — identifiers PENDING: MPN
  MDR7506 confirmed (Sony US + Abt + Sweetwater agree), but no UPC
  for the MDR-7506 surfaced on any US manufacturer or retailer spec
  page checked (Sony direct, Abt, Sweetwater, B&H), so identifiers
  stay empty per the Adaptive Controller / DualSense / PULSE Elite
  precedent. Quotes (8): Sony direct $114.99 (MSRP, JSON-LD price;
  page crawled 2026-10-17, stock not stated in the page text), Abt
  $113.00 (JSON-LD InStock, page-verified), Sweetwater $113.00
  (Open Graph instock, page-verified), Full Compass $114.99,
  Samy's $114.99, Vintage King $114.99 and Focus Camera $113.00
  (feed rows — suspected, no identifier in the feed rows),
  MusicArts $89.99 (feed row — suspected; the low outlier vs
  $113–$114.99 elsewhere, not page-verified). Correction vs the
  2026-10-31 candidate price $114.99: confirmed current at Sony
  direct; the street price is $113. Excluded: Best Buy $119.99
  (bundle with a desktop headphone stand), Newegg $160.99
  (open-box "Level 2") and $163.99 (International Model, no US
  warranty), Sweetwater $162.99 (bundle with bag), B&H $157.94
  (bundle with earpads and case), Target $114.99 "w/ Nylon Braided
  Cable" row (ambiguous listing phrasing, not used).
- Sony PlayStation Pulse Wireless Headset, White — identifiers
  PENDING: no hardware model number (CFI-...), retail MPN or UPC
  for the new Pulse has been published on any official or retailer
  page yet, so identifiers stay empty per the Adaptive Controller /
  DualSense / PULSE Elite precedent; re-check after the Nov 19
  launch. Quotes (1): PlayStation Direct $99.99 (PRE-ORDER —
  launches 2026-11-19; $99.99 recommended retail price per the
  official PlayStation Blog Oct 21 update; pre-orders via
  direct.playstation.com from Oct 29, 7am PT in the US; no Direct
  product-page URL surfaced, so the announcement URL is the quote
  URL). Best Buy, Walmart and Target pre-order listings at $99.99
  are confirmed by IGN / The Shortcut, but no verbatim Best Buy
  product URL surfaced, so no second quote is recorded — add one
  once a URL surfaces. Correction vs the 2026-10-31 candidate note
  "$99 (pre-order)": the figure is the NEW PlayStation Pulse
  headset (2026, planar magnetic drivers, PlayStation Link +
  Bluetooth, up to 30 hours, White and Midnight Black), NOT the
  PULSE 3D (CFI-ZWH1, 2020, $99.99). White is pinned as the
  first-listed launch colorway in Sony's announcement; Midnight
  Black is the other launch colorway. Excluded: all PULSE 3D rows
  ($99.99–$149.99, CFI-ZWH1), all PULSE Elite rows ($149.99) and
  all PULSE Explore rows ($159.99–$199.99) in the same feed
  (different models), the Pulse Edge (early 2027, no price yet),
  headset cases and accessories.
- Sony LinkBuds Clip, Black (WF-LC900/B) — identifiers PENDING:
  MPN WFLC900/B confirmed (Best Buy US Model WFLC900/B, SKU
  12317215 + Abt Model WFLC900B + BuyDig Part # WFLC900/B + Sony
  AU Model WFLC900B agree; hardware model WF-LC900 / YY2999 per
  the Sony reference guide), but UPC 027242934054 is stated on the
  BuyDig spec table only — no second non-Amazon US source surfaced,
  so identifiers stay empty per the Adaptive Controller / DualSense
  / PULSE Elite precedent. The Greige UPC 027242934177 (BuyDig) is
  a different colorway and was not copied; the AU EAN 4548736173699
  (Sony AU) is a different regional code and was not copied.
  Quotes (5): Best Buy $198.00 (Model WFLC900/B, SKU 12317215,
  JSON-LD InStock, page-verified; comp. value $228.00), Sweetwater
  $198.00 (feed row — suspected, $198 sale vs $228 list), BuyDig
  $198.00 (Part # WFLC900/B, In Stock, page-verified; list
  $229.99), Abt $198.00 (Model WFLC900B, comp. value $228,
  search-index read of the Greige page which lists the Black at
  $198; manufacturer rebate ends 11/08/2026), Sony direct SRP
  $229.99 (Greige page, electronics.sony.com — stale crawl, 270
  days; same SRP across colors per the Jan 2026 announcement).
  Correction vs the 2026-10-31 candidate price $229.99: that is
  the launch SRP — the current US street price is $198. Excluded:
  Datavision / Focus Camera bundle rows (with care program / case
  bundle), ListenUp Greige $198 and Best Buy Greige / Lavender /
  Green rows (different colorways), Best Buy Lavender $129.99 (a
  different colorway on a holiday deal — not the Black price),
  StaplesPromo $975 (3-pack bundle).
- Nintendo 64 Controller, Gray (HAC-043; Nintendo SKU 128577) —
  identifiers PENDING: hardware model HAC-043 confirmed (Nintendo
  Support US: "Nintendo 64 Controller (model No. HAC-043)") and
  Nintendo SKU 128577 confirmed (Nintendo US store page), but UPC
  00045496894948 is stated on the Nintendo US store page only — no
  second US source surfaced, so identifiers stay empty per the
  Adaptive Controller / DualSense / PULSE Elite precedent. Quotes
  (1): Nintendo direct $54.99 (JSON-LD InStock, page-verified
  2026-11-06; the only seller — Nintendo Store exclusive; a paid
  Nintendo Switch Online membership is required to purchase, limit
  four per Nintendo Account, ships to the US and Canada only).
  Correction vs the 2026-10-31 candidate price $49.99: that was
  the 2021 launch price — the current Nintendo direct price is
  $54.99. Excluded: all third-party N64-style pads in the feed
  (Retro Fighters Brawler64 $44.99–$69.99, 8BitDo 64 $37.99–$39.99,
  Retro-Bit Tribute $44.99, Hyperkin Admiral $45.99, Old Skool
  $19.99 — different models), Rock Candy / REMATCH controllers
  (different models), Displate / Intec accessories.
- Eval on the new snapshot: 96 models, 68 verified identifiers, 4
  with quotes, 15 total quotes, 0 identifier-matched, 15 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 92 →
  96 / verified stays 68 for the continuous expansion; the pending
  set gains the 4 new keys).

## 053 — 2026-11-06: Expansion batch 15 — 96 → 100 models (DECISIONS 037)

- Membership check (against the 96-model HEAD set, by name, MPN and
  UPC — run programmatically against git HEAD price_agent/catalog.py
  before adding anything; no catalog keys matched, 4 of 5 are new
  lines, 1 not added):
  - Apple Studio Display XDR, Standard glass, Tilt- and
    height-adjustable stand (MFEL4LL/A, $3,299) vs
    apple-studio-display-2026-standard-tilt (MFEX4LL/A, UPC
    195950529173): no match on any field — the 2026 Studio Display
    is the separate non-XDR line ($1,599, 60Hz, A19); the XDR
    (27-inch 5K mini-LED, 120Hz, 2000 nits peak HDR, Thunderbolt 5,
    released March 11, 2026) is a distinct line. The discontinued
    Pro Display XDR (32-inch 6K, $4,999, discontinued March 3,
    2026) is a different model and was not added.
  - Sony MDR-M1 (MDRM1, $269.99 candidate) vs sony-mdr-7506
    (MDR7506) and every other Sony headphone in the set
    (WH-1000XM5/XM6, WH-1000XM4C, WH-CH720N, ULT WEAR, INZONE H5,
    PULSE Elite/Explore, LinkBuds lines): the M1 (2024, 40mm
    closed-back, 50 ohm, 216 g, 5Hz–80kHz) is Sony's modern pro
    reference closed monitor line, different model from the 1991
    MDR-7506 and from every WH/INZONE/PULSE line — not a
    duplicate. The MDR-M1ST ($389.99, Japan-domestic) is a
    different model and was not added.
  - Sony MDR-MV1 (MDRMV1, $339.99 candidate) vs sony-mdr-7506 and
    sony-mdr-m1 (added in this same batch): the MV1 (2023, 40mm
    open-back, 24 ohm, 223 g, 5Hz–80kHz) is the open-back
    reference monitor sibling of the M1, different model from
    both — not a duplicate.
  - Sony INZONE H7 (WH-G700, ~$349.99 candidate) vs
    sony-inzone-h5-black (WHG500/B): the H7 is the distinct
    mid-range wireless INZONE line (2022, 40-hour battery, no ANC)
    above the H5 — no match — but NOT ADDED (see below).
  - Keychron B39 (B39-K9, $54.99 candidate) vs
    keychron-b40-deep-black (B40-K9, 75% Alice, $49.99) and the
    set's K8 lines (K8-G1, K8 HE, K8 Ultra 8K) and Q1: the B39
    (96% Alice with dedicated numpad) is the larger sibling of
    the B40, a different model — not a duplicate.
- Apple Studio Display XDR, Standard glass, Tilt- and
  height-adjustable stand (MFEL4LL/A) — identifiers PENDING: MPN
  MFEL4LL/A confirmed (Apple US buy page + Best Buy US Model
  MFEL4LL/A, SKU 6505397 + Abt Model MFEL4LL/A agree), but no UPC
  for MFEL4LL/A surfaced on any US retailer spec page checked —
  the B&H UPC 195950527650 belongs to the VESA config (MFEN4LL/A;
  the B&H MFEN page and the VESA + AppleCare+ kit page both list
  it), so it was not copied; the UK GTIN 195950527858 is the
  MFEP4B/A (different region) and was not copied. Quotes (5):
  Apple direct $3,299.00 (US buy page JSON-LD, search-index read;
  stock not stated); Best Buy $3,299.99 (Model MFEL4LL/A, SKU
  6505397, JSON-LD InStock, page-verified, sold by Best Buy); Abt
  $3,299.00 (Model MFEL4LL/A, JSON-LD InStock, page-verified, est.
  delivery Nov 10); Sam's Club $3,299.00 and Sweetwater $3,299.00
  (feed rows — suspected, no identifier in the feed rows).
  Correction vs the 2026-10-31 candidate price $3,299: confirmed
  current — it is the standard-glass tilt-and-height config;
  $2,899 is the standard-glass VESA config (MFEN4LL/A) and
  $3,599 / $3,199 are the nano-texture tilt-height / VESA configs.
  Excluded: refurbished Apple $2,799 (refurbished, not new); NFM
  rows (bundles with 3-year AppleCare+); Melrose Mac $2,899 and
  SVA Campus Store $3,199 (VESA-config prices on tilt-height
  rows); nano-texture rows ($3,499–$3,599); non-US rows (Artifact
  Argentina $5,700, 961souq $3,000); MacExperience $6,998 (Pro
  Display XDR, different model).
- Sony MDR-M1, Black (MDRM1) — identifiers PENDING: MPN MDRM1
  confirmed (Sony US + B&H + Sweetwater agree), but UPC
  027242930612 is stated on the B&H US spec page only — the only
  other source stating it is manuals.plus, which mirrors the
  Amazon ASIN listing, and Amazon is not used for identifier
  corroboration, so identifiers stay empty per the Adaptive
  Controller / DualSense / PULSE Elite precedent; re-check next
  refresh. Quotes (6): Sony direct $249.99 (launch MSRP, page
  crawled 2024-10-22 — stale, stock not stated); B&H $268.00
  (JSON-LD InStock, page-verified); Sweetwater $268.00 (Open Graph
  instock, page-verified); Guitar Center $268.00, Vintage King
  $269.99 and Focus Camera $268.00 (feed rows — suspected, no
  identifier in the feed rows). Correction vs the 2026-10-31
  candidate price $269.99: confirmed current-ish — $268 at B&H
  and Sweetwater, $269.99 at Vintage King; $249.99 is the launch
  MSRP, not the current street price. Excluded: MDR-M1ST $389.99
  (Japan-domestic model), 5-pack $1,002.99 bundle, WUQ / Newegg
  $426.99 (third-party seller row), MercadoLibre $219 (non-US
  marketplace), Walmart $268 feed row (marketplace ambiguity —
  seller not confirmed first-party), MDR-MV1 rows (different
  model), MDR-ZX110NC rows (different model).
- Sony MDR-MV1, Black (MDRMV1) — identifiers PENDING: MPN MDRMV1
  confirmed (Sony AU/NZ Product ID + Macy's + Sweetwater agree;
  EAN 4548736147836 is the AU/NZ regional code and was not
  copied), but UPC 027242926585 appears in an eBay listing only —
  no US retailer spec page surfaced, so identifiers stay empty per
  the Adaptive Controller / DualSense / PULSE Elite precedent;
  re-check next refresh. Quotes (5): Sweetwater $418.00 (Open
  Graph instock, page-verified); Macy's $419.99, SoundPure
  $419.99, Unique Photo $418.00 and Impulse Cameras $419.99 (feed
  rows — suspected, no identifier in the feed rows). Correction vs
  the 2026-10-31 candidate price $339.99: that matches no US
  price — the MSRP is $419.99 (SoundGuys) and the current US
  street price is $418–$419.99; $399 was a launch-era figure in
  some reviews. The Sony direct US page returned 403 on
  2026-11-06, so no direct quote is recorded. Excluded: Target
  $418 bundle (with hard shell case), Newegg 5-pack $1,002.99
  bundle, Greentoe $386 ("make an offer" marketplace-style row),
  Voomisupply $928.42, Walmart $418 feed row (marketplace
  ambiguity), MDR-M1 rows (different model), 360 VME software $269
  and the Mogami cable $204.95 (different products).
- Keychron B39, 96% Alice, Deep Black (B39-K9) — identifiers
  PENDING: SKU B39-K9 comes from the Keychron official store page
  only and no UPC/EAN for the B39 surfaced anywhere, so
  identifiers stay empty per the Adaptive Controller / DualSense
  precedent; re-check next refresh. Quotes (1): Keychron direct
  $54.99 (official store, Deep Black variant Available,
  page-verified 2026-11-06; the only seller — Keychron's own store
  only, so it holds a single quote, like the B40). Correction vs
  the 2026-10-31 candidate price $54.99: confirmed current at
  Keychron direct.
- Sony INZONE H7 — NOT ADDED (batch split, Pro Display XDR
  precedent): discontinued by Sony — Audio46 lists it
  "Discontinued" and Headphone Zone says it is "permanently
  discontinued by the manufacturer"; the Meta Catalog feed for the
  query returns no Sony-direct H7 row and no Best Buy H7 row
  (only H5/H9/H3/H6 rows and H9/H7 earpads); the only remaining US
  listing found is ListenUp $228.00 (Available, page-verified
  2026-11-06). The candidate "~$349.99 launch price" was also
  wrong: the H7 launched in 2022 at $229.99 US (Audio46 $229.99;
  GamesRadar $200 after a launch-price adjustment). Revisit only
  if Sony re-lists it; the H9 (WH-G900N, $329.99) and H9 II are
  the current upper INZONE lines, not substitutes.
- Eval on the new snapshot: 100 models, 68 verified identifiers, 4
  with quotes, 17 total quotes, 0 identifier-matched, 17 suspected
  (snapshot offers carry no identifier — the rule working, not a
  bug). Tests: 19 passed (test_snapshot_eval counts updated 96 →
  100 / verified stays 68 for the continuous expansion; the pending
  set gains the 4 new keys).

## 054 — 2026-11-06: Expansion batch 16 — 100 → 105 models (DECISIONS 038)

- Anker US homepage sweep (anker.com, read-only, 2026-11-06
  ~19:06 UTC): 24 shelf listings, 23 distinct models. Full
  candidate list (list-only): MagGo 2 Pro Magnetic Power Bank
  (10K, Qi2 25W, Active Cooling) $109.99; Laptop Charger Pro
  $49.99 (was $59.99); Nano Charger (45W, Smart Display, 180°
  Foldable) $29.99 (was $34.99) and a second listing $25.99 (was
  $39.99); Desktop USB-C Hub $79.99 (was $99.99); Universal
  Charger (4-in-1, 100W, Smart Display) $79.99; Nano Docking
  Station (13-in-1, Triple Display) $119.99 (was $149.99); Prime
  Power Bank (26K, 300W) $199.99 (was $229.99); Prime Charger
  (160W, 3 Ports, Smart Display) $115.99 (was $149.99); Prime
  DL7400 Docking Station (14-in-1, Triple Display, DisplayLink)
  $299.99; Prime Power Bank (20K, 220W) $129.99 (was $179.99);
  Charger (100W, 3 Ports, Smart Display) $59.99 (was $69.99);
  Prime Wireless Charging Station (3-in-1, MagGo, AirCool, Dock
  Stand) Sold Out; Prime Wireless Car Charger (MagGo, AirCool,
  Pad) $89.99; Nano Power Strip (10-in-1, 70W, Clamp) $69.99;
  Nano Power Bank (5K, MagGo, Slim) $54.99; Nano Charger (45W)
  with USB-C to USB-C Cable $25.99; Nano Charging Station
  (7-in-1, 100W) $79.99; Nano Power Bank (10K, 45W, Built-In
  Retractable USB-C Cable) $59.99; Nano Charger (70W, 3 Ports)
  $39.99; Nano Travel Adapter (5-in-1, 20W, 1-Pack) $25.99;
  Laptop Power Bank (25K, 165W, Built-In and Retractable Cables)
  $119.99; Charger (140W, 4-Port, PD 3.1) with USB-C Cable
  $79.99 (was $89.99); Prime Charger (250W, 6 Ports, GaNPrime)
  $149.99. Soundcore earbuds/speakers are not listed on anker.com
  (separate soundcore.com store) — no Soundcore model picked, per
  the "only what the official US catalog actually lists as
  current" rule; a soundcore.com sweep is a candidate for a later
  batch.
- Membership check (against the 100-model set by name, MPN and
  UPC, 2026-11-06): the only existing Anker entry is
  anker-prime-100w (Prime Charger 100W, A2688, UPC 194644040635).
  All 5 candidates are distinct — no name, MPN or UPC match:
  MagGo 2 Pro A110R (no other magnetic power bank in the set);
  Prime Power Bank 26K A110A (no other high-capacity power bank
  in the set); Desktop USB-C Hub A210C (no hub/dock in the set);
  Prime Wireless Car Charger A2933 (no car charger in the set);
  Nano Charger 70W B121A (no 70W charger in the set; distinct
  from the A2688 100W Prime charger). The homepage "Anker Charger
  (100W, 3 Ports, Smart Display)" $59.99 was NOT added: it may be
  a newer non-Prime 100W charger and its model number was not
  established, so it stays out rather than risk a duplicate of
  the A2688 entry — needs a model-number check before any add.
  The Prime Wireless Charging Station (3-in-1, Dock Stand) was
  NOT added: Sold Out on the Anker homepage.
- Anker MagGo 2 Pro Magnetic Power Bank (10K, Qi2 25W, Active
  Cooling), Phantom Gray (A110R) — identifiers PENDING: MPN
  A110R confirmed (Anker US official page + reviews agree), but
  no UPC for A110R surfaced anywhere, so identifiers stay empty
  per the Adaptive Controller / DualSense / PULSE Elite
  precedent; re-check next refresh. Quotes (2): Anker direct
  $109.99 (JSON-LD InStock, page-verified); Newegg $109.99 (feed
  row — suspected, no identifier in the feed row). Colors:
  Starlight Silver, Polar Night Blue, Phantom Gray, Burgundy Red
  (Android Headlines + Anker page); Phantom Gray pinned — the page
  does not state which Shopify variant is Phantom Gray, so the
  color-to-variant mapping is recorded as unverified; price is
  color-independent ($109.99 for all colors in the feed).
  Excluded: Member Exclusive page (same model/price, duplicate);
  Starlight Silver feed row (different color); bundle kits
  $144.98/$149.98/$229.98 (bundles); MagGo Power Bank (10K)
  $135, MagGo Wireless Charging Station rows, 622/623 chargers
  (different models); refurbished 621 $42.99 (refurbished).
- Anker Prime Power Bank (26K, 300W), Black (A110A) —
  identifiers PENDING: MPN A110A confirmed (Anker US + Best Buy
  US agree), colour Black confirmed (Heavins IE lists A110AH11
  Black — but its EAN 0194644239299 is the EU/IE regional code
  for the H11 variant and was not copied, per the MDR-MV1 EAN
  precedent), but no US UPC for A110A surfaced on any US retailer
  spec page, so identifiers stay empty per the Adaptive
  Controller / DualSense precedent; re-check next refresh. Quotes
  (2): Anker direct $199.99 (sale — $30 off the $229.99 list;
  homepage shelf + "$30 OFF" banner, page-verified; JSON-LD and
  the feed both show $229.99); Best Buy $229.99 (Model A110A,
  SKU 11919239, page-verified; feed row — suspected, no
  identifier in the feed row). Excluded: with Charging Base
  $329.99 (bundle, different SKU B110A); CDW $229.99 feed row
  (title does not name the 26K model); Prime 20K 220W /
  27,650mAh 250W / 12,000mAh 130W / 9.6K 65W Fusion rows
  (different models); no Amazon rows used.
- Anker Desktop USB-C Hub, 10-in-1 Dual 4K (A210C) —
  identifiers PENDING: MPN A210C confirmed (Anker US official
  page), but the only UPC stating a code, 194644340506, comes
  from pickoryx, which mirrors the Amazon ASIN listing
  (B0H36FV12Q) — Amazon is not used for identifier
  corroboration, so identifiers stay empty per the MDR-M1 /
  Adaptive Controller precedent; re-check next refresh. Quotes
  (1): Anker direct $79.99 (sale — $20 off the $99.99 list;
  homepage shelf + Anker blog "$20 OFF, $79.99, Code:
  WSPDV2ONVYED"; JSON-LD and the feed both show $99.99; JSON-LD
  InStock, page-verified; the only seller — Anker's own store
  only, so it holds a single quote, like the B39). Excluded:
  VALORANT Limited Edition $109.99 (same A210C base, different
  edition/price — not pinned); Anker 575 Docking Station $199.99,
  13-port hub $149.99, 332/364/565 and other hubs (different
  models); Walmart/Target/Newegg generic hub rows (different
  models). No color claimed — the Anker page names no colorway
  (an Amazon-derived listing calls it Iron Gray, not
  corroborated).
- Anker Prime Wireless Car Charger (MagGo, AirCool, Pad)
  (A2933) — identifiers PENDING: MPN A2933 confirmed (Anker US
  + manuals.plus agree), colour Matte Black per a Bangladesh
  listing only (not a US source), but no UPC for A2933 surfaced
  anywhere, so identifiers stay empty per the Adaptive
  Controller / DualSense precedent; re-check next refresh. Quotes
  (2): Anker direct $89.99 (JSON-LD InStock, page-verified);
  Target $89.99 (feed row — suspected, no identifier in the feed
  row; title matches the A2933 spec — Qi2 25W + AirCool +
  included 60W adapter). Excluded: anker.com feed row $135
  (stale/conflicting — live page JSON-LD and the us.anker.com
  feed row both say $89.99); Target $69.99 "Anker Prime MagGo
  Wireless Car Charger with AirCool" (title does not establish
  Qi2 25W/A2933 — likely the older 15W MagGo car charger);
  K-Rauta $78.90 (Estonia, non-US); Nano Wireless Car Charger
  bundle $77.98 and Prime Wireless Charging Station rows
  (different products).
- Anker Nano Charger (70W, 3 Ports), Black Stone (B121A) —
  identifiers PENDING: MPN B121A confirmed (Anker US official
  page states Model Number B121A; Notebookcheck and Amazon
  listings call the same charger A121A — the Anker page takes
  precedence and A121A was not recorded as a separate
  identifier); UPC 194644241247 for Black is stated on Amazon
  listings only and Amazon is not used for identifier
  corroboration, so identifiers stay empty per the Adaptive
  Controller / DualSense precedent; re-check next refresh. Quotes
  (3): Anker direct $39.99 (JSON-LD InStock, page-verified);
  Newegg $39.99 (feed row — suspected, no identifier in the feed
  row, no color stated); Impulse Cameras $39.99 (feed row —
  suspected, no identifier in the feed row; names the pinned
  Black Stone colorway). Excluded: Best Buy White $34.99
  (different colorway — white is cheaper than black at Best Buy);
  Walmart $39.99 feed row (marketplace ambiguity); corexlb $45
  (not_a_seller); Nano 70W + Nano Power Bank bundle $99.98
  (bundle); Nano Power Strip $69.99, Zolo 70W, Nano Neo
  (different products). Note: the bundle slug
  "bundle-b121a111-a1638011" hints the black variant MPN may be
  B121A111 (mirroring A121D121 = White, confirmed by Best Buy
  Canada) — unverified, not recorded; check next refresh.
- Anker Nano Charger (45W, Smart Display, 180° Foldable)
  (A121D) — NOT ADDED (batch split, Pro Display XDR / INZONE H7
  precedent): two different US product pages ($34.99 PreOrder on
  the dual-foldable page, variant 46557402398870, vs $39.99
  InStock on the foldable-plug-compact page, variant
  46070529196182) and the page text never states which Shopify
  variant is which color (colors: Aurora White, Misty Blue, Black
  Stone, Orange per the Bangladesh listing; 4–5 colors per the US
  pages), so no color can be pinned cleanly. The Nano 70W
  replaces it as this batch's charger pick. Revisit only if Anker
  consolidates the two US pages or a US retailer spec page
  settles the color-to-variant mapping. (The $25.99 homepage
  listing is the sale price of the $39.99 InStock page; the
  $29.99 homepage listing is the sale price of the $34.99
  PreOrder page — sale prices, not different models.)
- Not added from the sweep (held for later batches, all current
  US models, no defect): Laptop Charger Pro $49.99; Universal
  Charger (4-in-1, 100W) $79.99; Nano Docking Station (13-in-1)
  $119.99; Prime Charger (160W) $115.99; Prime DL7400 Docking
  Station $299.99; Prime Power Bank (20K, 220W) $129.99; Nano
  Power Strip $69.99; Nano Power Bank (5K, MagGo, Slim) $54.99;
  Nano Charger (45W) with cable $25.99 (bundle with cable;
  A121D-adjacent, same pinning problem); Nano Charging Station
  (7-in-1, 100W) $79.99; Nano Power Bank (10K, 45W, retractable
  cable) $59.99; Nano Travel Adapter (5-in-1, 20W) $25.99; Laptop
  Power Bank (25K, 165W) $119.99; Charger (140W, 4-Port, PD 3.1)
  $79.99; Prime Charger (250W, 6 Ports) $149.99.
- Eval on the new snapshot: 105 models, 68 verified identifiers,
  5 with quotes, 10 total quotes, 0 identifier-matched, 10
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 100 → 105 / verified stays 68 for the
  continuous expansion; the pending set gains the 5 new keys).

## 055 — 2026-11-06: Expansion batch 17 — 105 → 110 models (DECISIONS 039)

- JBL US storefront sweep (jbl.com, read-only, 2026-11-06
  ~18:10–19:13 UTC / 10:10–11:13 PT): the homepage text fetch
  returned only a locale prompt ("Want the local experience?"),
  so the sweep is recorded from search-index reads of the US
  storefront and category pages. Homepage shelf observed: JBL
  PartyBox 130 (30% off), Flip 7 (over 10% off), Tune 730BT
  (over 30% off), EON700 Series (save $50–$100), Charge 5
  ($139.95, was $179.95), Live 780NC, Flip Essential 2 ($59.99,
  was $129.95), Sense Lite, PartyBox Club 120, Clip 5. Category
  pages observed: Tour Pro 3 $329.95 (noise-cancelling earbuds,
  12 results), Tour One M3 Smart Tx $449.95 (US over-ear
  catalog). Full candidate list (list-only): Flip 7 $129.95;
  Charge 5 $139.95 (previous generation, still listed); Charge 6
  (2025, not individually priced this sweep); Clip 5; Go 4;
  Xtreme 4 / Boombox 4; Flip Essential 2 $59.99; PartyBox Club
  120; PartyBox Stage 320 $569.95; PartyBox 330 (new Sept 2026,
  US price conflicting — see below); PartyBox Encore 2;
  PartyBox 130; Tour One M3 Smart Tx $449.95; Live 780NC
  $139.95 (comp. value $249.95); Tune 730BT; Tour Pro 3
  $329.95; Live Beam 3; Tune Beam 2; Wave Buds 2; Sense Lite;
  Bar 1300XMK2 $1,699.95; Bar 1000MK2 $1,199; Bar 700MK2 $899;
  Bar 500MK2 $649; Bar 300MK2 $449; Cinema SB510MK2 / SB550MK2
  (PH launch, US availability unconfirmed); JBL Cove M1/P1/X1
  (PH launch, US availability unconfirmed); Quantum 120 / 520
  (PH launch, US availability unconfirmed); EON700 Series (pro
  PA, out of Phase 1 consumer scope).
- Membership check (against the 105-model set, by name, MPN and
  UPC): the set had no JBL entry at all — no name, MPN or UPC
  overlap for any of the 5 picked models. Flip 7
  (JBLFLIP7BLKAM / 050036407342): no match — the set's only
  portable speakers are none (first in the set). Tour One M3
  Smart Tx (JBLTOM3AVIBLKAM): no match — distinct from the set's
  Sony WH-1000XM5/XM6 and Bose QuietComfort Ultra (different
  brand, model and MPN). Tour Pro 3 (JBLTOURPRO3BLKAM): no match
  — distinct from the set's Sony WF-1000XM5/XM6, AirPods Pro 3
  and Galaxy Buds4 Pro. Bar 1300XMK2 (JBLBAR1300XM2BLKAM): no
  match — the set had no soundbar. PartyBox Stage 320
  (JBLPBSTAGE320AM): no match — the set had no party speaker.
  The non-Tx Tour One M3 (JBLTOURONEM3BLKAM) and the non-US Bar
  1300MK2 (dual 8-inch sub) were checked as separate models and
  deliberately not added (see DECISIONS 039).
- Per-model record (all 5 added; identifiers, quotes, pending):
- JBL Flip 7, Black (JBLFLIP7BLKAM) — VERIFIED: UPC 050036407342
  + MPN JBLFLIP7BLKAM (JBL/Harman Salsify syndication catalog +
  eBay listing 187108565342 agree; manuals.plus/B&H data dump
  agrees; Amazon listings agree but Amazon is not used for
  corroboration). Not copied: UPC 050036407250 (eBay, MPN
  JBLFLIP7BLK without AM — a different variant). Quotes (2): JBL
  direct $129.95 (sale, JSON-LD InStock, page-verified; feed
  Black row $129.95 vs $149.95 list); Target Black $129.99
  (JSON-LD InStock, page-verified). Excluded: Target feed row
  $114.99 (Red — a different colorway); Crutchfield $109.95
  (stale crawl, 360 days); Dell colorway rows at list price; a
  Samsung-sold $114.99 feed row; crestline $851.76 (bulk).
- JBL Tour One M3 Smart Tx, Black (JBLTOM3AVIBLKAM) —
  identifiers PENDING: MPN confirmed (Abt + Best Buy US Model +
  PC Richard MPN + Crutchfield MFR# agree), but UPC 050036414029
  is stated on snapklik + tanotis aggregators only — no US
  retailer spec page states it. Not copied: Blue UPC 050036414098
  and Latte UPC 050036414067 (Abt, different colorways); global
  EAN 1200130025112 (regional code). Quotes (3): JBL direct
  $449.95 (feed Black row); Abt $449.95 (JSON-LD InStock,
  page-verified); Best Buy $449.95 (Model JBLTOM3AVIBLKAM, SKU
  6623867, page-verified). The $199.95 sale (audiowords Nov 1 +
  Slickdeals/Best Buy ~8 days ago) has ended — Best Buy page now
  $449.95. Excluded: Best Buy Mocha/Blue $472.45 feed rows (with
  case bundle); Newegg Mocha $199.95 feed row (different
  colorway, suspected).
- JBL Tour Pro 3, Black (JBLTOURPRO3BLKAM) — identifiers
  PENDING: MPN confirmed (Crutchfield MFR# + Abt + B&H Latte
  sibling agree), but UPC 050036402392 is stated on Amazon
  listings only. Not copied: Latte UPC 050036402415 (B&H,
  different colorway). Quotes (3): JBL direct $329.95 (category
  pages; feed Latte row $329.95 brand_direct); Crutchfield Black
  $329.95 (JSON-LD InStock, page-verified); Abt Black $329.95
  (JSON-LD InStock, page-verified). Excluded: the feed's Abt
  $229.95 Black row (stale — live Abt page is $329.95);
  Crutchfield $229.95 sale (ended 9/13); Best Buy $346.45 bundle
  rows; Charge 6 + Tour Pro 3 kit $476.91; Greentoe
  marketplace-style rows; icuracao $209.99 (non-US).
- JBL Bar 1300XMK2, Black (JBLBAR1300XM2BLKAM) — identifiers
  PENDING: MPN confirmed (global.jbl.com Item# + Best Buy US
  Model + Abt + shopabunda agree), but UPC 050036414869 is
  stated on Amazon + an eBay refurbished listing + Target Plus
  partner data only. Not copied: global EAN 1200130026843
  (regional code). Quotes (4): JBL direct $1,699.95 (feed Black
  row; Harman press release lists $1,699.95); Best Buy $1,699.95
  (Model JBLBAR1300XM2BLKAM, SKU 6643311, sold by Best Buy,
  page-verified); Abt $1,699.95 (page-verified); Macy's $1,199.95
  (feed row — suspected, not page-verified). Excluded: Best Buy
  $1,742.45 and Newegg $1,499.90/$1,514.99 and jbl.com $1,690.94
  (bundles with cable/protection plan); Belk $2,040 (outlier);
  Dolby.com $1,019.99 (the old Bar 1300X, 650W — a different
  model).
- JBL PartyBox Stage 320, Black (JBLPBSTAGE320AM) — identifiers
  PENDING: MPN confirmed as the US Black code (JBL US page
  Item# + Sharaf DG lists PARTYBOXSTAGE320AM as Black; White is
  JBLPBSTAGE320SWAM), but no UPC surfaced anywhere. Quotes (4):
  JBL direct $569.95 (product-page JSON-LD InStock,
  page-verified; feed White row also $569.95); Best Buy Black
  $629.95 (feed row — suspected); Target Black $629.99 (JSON-LD
  InStock, page-verified); RC Willey Black $499.95 (feed row —
  suspected low outlier, not page-verified). Excluded: 'The
  Works' bundle $739.90 (OutOfStock); Woot refurbished $399.95;
  B&H mic/PartyLight kits $729.90/$799.90 (bundles,
  discontinued).
- PartyBox 330 — NOT ADDED (batch split, Pro Display XDR /
  INZONE H7 precedent): the new 2026 successor to the Stage 320
  (280W, 18 hours, launched Sept 2026 in PH) has a conflicting
  US price — $499.95 on the JBL US page per one source vs $630
  per another — so no price can be pinned cleanly. Revisit next
  sweep once the US price settles.
- Not added from the sweep (held for later batches, all current
  US models, no defect): Charge 5 $139.95; Charge 6; Clip 5; Go
  4; Xtreme 4 / Boombox 4; Flip Essential 2 $59.99; PartyBox
  Club 120; PartyBox Encore 2; PartyBox 130; Live 780NC $139.95;
  Tune 730BT; Live Beam 3; Tune Beam 2; Wave Buds 2; Sense Lite;
  Bar 1000MK2 $1,199; Bar 700MK2 $899; Bar 500MK2 $649; Bar
  300MK2 $449. Not added (US availability unconfirmed): Cinema
  SB510MK2 / SB550MK2; JBL Cove M1/P1/X1; Quantum 120 / 520.
  Not added (out of scope): EON700 Series (pro PA).
- Eval on the new snapshot: 110 models, 69 verified identifiers,
  5 with quotes, 16 total quotes, 0 identifier-matched, 16
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 105 → 110 / verified 68 → 69 for the
  continuous expansion; the pending set gains the 4 new pending
  keys — the Flip 7 is verified).

## 056 — 2026-11-06: Expansion batch 18 — 110 → 115 models (DECISIONS 040)

- Razer US store sweep (razer.com, read-only, 2026-11-06
  ~19:10–19:30 UTC / 11:10–11:30 PT): the US product pages resolve
  for every pick (page titles confirm the right products), but the
  text fetch returns only the "MORE GAMER GEAR YOU'LL DIG"
  carousel, not the product's own price or stock — so direct prices
  are taken from the Meta feed brand_direct rows carrying the exact
  US MPN in the URL, corroborated by Razer's own launch releases
  and retailer pages (the JBL batch 17 precedent). Feed shelf
  observed across the 5 runs (100 rows): Viper V4 Pro $159.99;
  DeathAdder V4 Pro Black $169.99 / White $169.99 / Esports Green
  $152.99 sale / NiKo $189.99; Basilisk V4 Pro Black/White
  $169.99; Naga V3 Pro $179.99; BlackWidow V4 Pro Green/Yellow
  $229.99 (Orange row is the R3M1 code); BlackWidow V4 Pro 75%
  $299.99; BlackWidow V4 Low-Profile HyperSpeed $199.99;
  BlackShark V3 Pro $249.99 (PC/Xbox/PlayStation, Black/White);
  BlackShark V3 $149.99; BlackShark V3 X HyperSpeed $99.99;
  Wolverine V3 Pro Black/White $199.99; Wolverine V3 Pro 8K PC
  $199.99; Wolverine V3 Tournament Edition $99.99; Wolverine V4
  Tournament Edition $99.99; Raiju V3 Pro $219.99; Kraken V4 Pro
  $399.99; Kraken V4 $179.99; Kraken V4 X $79.99; Seiren V3 Pro
  $249.99; Huntsman V3 Pro Mini 8KHz $179.99; Hammerhead V3
  HyperSpeed $129.99; Gigantus V2 Pro mats $49.99. Full candidate
  list (list-only): DeathAdder V4 Pro Black $169.99; DeathAdder V4
  Pro White $169.99; Basilisk V4 Pro Black $169.99; Basilisk V4
  Pro White $169.99; Naga V3 Pro $179.99; Viper V3 Pro SE $99.99;
  Cobra HyperSpeed $99.99; Orochi V2 $39.99; BlackWidow V4 Pro
  75% $299.99; BlackWidow V4 Low-Profile HyperSpeed $199.99;
  BlackWidow V4 $169.99; BlackWidow V4 75% $189.99; Huntsman V3
  Pro Mini 8KHz $179.99; Huntsman V3 HE Magnetic TKL 8KHz
  $139.99; BlackShark V3 $149.99; BlackShark V3 X HyperSpeed
  $99.99; Kraken V4 $179.99; Kraken V4 X $79.99; Barracuda X
  Chroma $129.99; Wolverine V3 Pro 8K PC $199.99; Wolverine V3
  Tournament Edition $99.99; Wolverine V4 Tournament Edition
  $99.99; Raiju V3 Pro $219.99; Seiren V3 Pro $249.99; Hammerhead
  V3 HyperSpeed $129.99; Blade 14 from $2,299 / Blade 16 from
  $2,399 / Blade 18 from $3,499 (configurable — no single
  retailer-pinned base config found, DECISIONS 015, not added).
- Membership check (against the 110-model set, by name, MPN and
  UPC): the set had no Razer entry at all — no name, MPN or UPC
  overlap for any of the 5 picked models. Viper V4 Pro
  (RZ01-05630100-R3U1): no match — the set's only flagship mice
  are Logitech (Superlight 2 / DEX / G502 X PLUS), a different
  brand and model. BlackWidow V4 Pro Green (RZ03-04680200-R3U1):
  no match — distinct from the set's Logitech and Keychron boards.
  BlackShark V3 Pro (RZ04-05400100-R3U1): no match — distinct
  from the set's Sony, Bose and JBL headphones. Wolverine V3 Pro
  (RZ06-05200100-R3U1): no match — distinct from the set's Xbox,
  DualSense and Switch controllers. Kraken V4 Pro
  (RZ04-05160100-R3U1): no match — distinct from the BlackShark
  V3 Pro added in this same batch (different line, different MPN).
- Per-model record (all 5 added; identifiers, quotes, pending):
- Razer Viper V4 Pro, Black (RZ01-05630100-R3U1) — identifiers
  PENDING: MPN confirmed (Best Buy US Model + Canada Computers
  MPN + ShopAbunda + Big Apple Buddy sourced from Best Buy
  agree), but no US UPC surfaced anywhere. Not copied: EU EAN
  8887910085134 (Scan UK + Singular CY + startech24 datasheet —
  the R3G1 variant); White MPN RZ01-05630200-R3U1 (different
  colorway). Quotes (3): Razer direct $159.99 (March 24, 2026
  launch release US$159.99 MSRP + Windows Central 'directly from
  Razer's website'; US product URL resolves — price-only, stock
  not confirmed in the page text); Best Buy Black $159.99 (Model
  RZ01-05630100-R3U1, SKU 6669259, sold by Best Buy, Add to cart,
  JSON-LD InStock, page-verified); NFM Black $156.99 (feed row —
  suspected). Excluded: Ayoub $191 R3G1 (non-US variant); Lethal
  Aero Base Mod $14.99 (accessory); DeathAdder/Basilisk rows
  (different models).
- Razer BlackWidow V4 Pro, Green switches, Black
  (RZ03-04680200-R3U1) — identifiers PENDING: MPN confirmed
  (B&H + Newegg + NeweggBusiness agree), but UPC 840272903315 is
  stated on the B&H page only — no second non-Amazon US source.
  Not copied: Yellow-switch UPC 840272903339 (Amazon listing for
  RZ03-04681900-R3U1 — different switch variant); Orange MPN
  RZ03-04683500-R3M1 (non-US code); EU Yellow code
  RZ03-04682200-R3F1. Quotes (3): Razer direct $229.99 (feed
  brand_direct row, URL carries the MPN; February 2023 launch
  MSRP); B&H $199.99 (Holiday Savings $50 off $249.99, In Stock,
  JSON-LD InStock, page-verified; UPC on the page); Staples
  $267.93 (feed row for the exact MPN — suspected; above list).
  Excluded: Best Buy White $199.99 (different colorway);
  gadgetlb $279 (non-US); BlackWidow V4 Pro 75% $299.99
  (different model).
- Razer BlackShark V3 Pro, PC version, Black
  (RZ04-05400100-R3U1) — identifiers PENDING: MPN confirmed
  (Best Buy US Model + manuals.plus agree), but UPC 840272919484
  is stated on Amazon listings only. Not copied: White
  RZ04-05400200-R3U1; PlayStation Black RZ04-05400500-R3G1;
  Xbox Black RZ04-05400300-R3U1; CS2 Edition RZ04-05400800-R3M1
  (GTIN 8887910061657). Quotes (3): Razer direct $249.99 (feed
  brand_direct row; US store price read 2026-10-15 at $249.99
  with Add to cart); Best Buy Black $249.99 (Model
  RZ04-05400100-R3U1, SKU 6632881, sold by Best Buy, search-index
  page read); Electronic Express Black $249.99 (feed row —
  suspected). Excluded: Abt Xbox-variant row (different platform
  variant); Sentinels team-store row (not a general retailer);
  Esports Green / NiKo / CS2 edition rows.
- Razer Wolverine V3 Pro, Black (RZ06-05200100-R3U1) —
  identifiers PENDING: MPN confirmed (Best Buy US Model +
  ShopAbunda + Eneba spec table agree), but no UPC surfaced on
  any US manufacturer or retailer spec page. Not copied: White
  MPN RZ06-05200200-R3U1 (Best Buy $191.99); EU code
  RZ06-05200100-R3M1 (Overclockers UK). Quotes (3): Razer direct
  $199.99 (feed brand_direct row; August 2024 launch MSRP); Best
  Buy Black $169.99 (Model RZ06-05200100-R3U1, SKU 6594728, save
  $30 off comp. value $199.99, page-verified); NFM Black $166.99
  sale vs $199.99 list (feed row — suspected). Excluded:
  FlexShopper $247.99 / $10 (lease-to-own); Staples White $213.60
  (different colorway); Macy's Wolverine V3 Pro 8K PC row
  (different, PC-only model); Woot $109.99 White (different
  colorway); sigmatiendas $279.42 (non-US).
- Razer Kraken V4 Pro, Black (RZ04-05160100-R3U1) — identifiers
  PENDING: MPN confirmed (Best Buy US Model + manuals.plus
  agree), but no US UPC surfaced — PBTech lists UPC 840272909980
  against the R3M1 variant and the EU EAN is 8887910060094, so
  neither was carried across regions. Not copied: Kraken V4
  (non-Pro) UPC 840272910054 (different model, RZ04-05170100-
  R3U1). Quotes (3): Razer direct $399.99 (feed brand_direct row;
  September 2024 launch MSRP); Best Buy Black $299.99 (Model
  RZ04-05160100-R3U1, SKU 6589878, comp. value $399.99,
  search-index page read); Beach Camera $299.00 (feed row —
  suspected; the same row appears twice in the feed). Excluded:
  Kraken V4 Pro + Base Station V2 Chroma bundle $469.98; Kraken
  V4 $179.99 / CDW $205.99 (non-Pro model); Newegg Evangelion
  combo $1,149.99 (bundle).
- Not added from the sweep (held for later batches, all current
  US models, no defect): DeathAdder V4 Pro Black $169.99 / White
  $169.99; Basilisk V4 Pro Black $169.99 / White $169.99; Naga V3
  Pro $179.99; Viper V3 Pro SE $99.99; Cobra HyperSpeed $99.99;
  Orochi V2 $39.99; BlackWidow V4 Pro 75% $299.99; BlackWidow V4
  Low-Profile HyperSpeed $199.99; BlackWidow V4 $169.99;
  BlackWidow V4 75% $189.99; Huntsman V3 Pro Mini 8KHz $179.99;
  Huntsman V3 HE Magnetic TKL 8KHz $139.99; BlackShark V3
  $149.99; BlackShark V3 X HyperSpeed $99.99; Kraken V4 $179.99;
  Kraken V4 X $79.99; Barracuda X Chroma $129.99; Wolverine V3
  Pro 8K PC $199.99; Wolverine V3 Tournament Edition $99.99;
  Wolverine V4 Tournament Edition $99.99; Raiju V3 Pro $219.99;
  Seiren V3 Pro $249.99; Hammerhead V3 HyperSpeed $129.99.
  Not added (no clean pin): Blade 14/16/18 (configurable laptops
  — no single retailer-pinned base config, DECISIONS 015).
- Eval on the new snapshot: 115 models, 69 verified identifiers,
  5 with quotes, 15 total quotes, 0 identifier-matched, 15
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 110 → 115 for the continuous expansion;
  verified stays 69; the pending set gains the 5 new Razer keys).

## 057 — 2026-11-06: Expansion batch 19 — 115 → 120 models (DECISIONS 041)

- Corsair US store sweep (corsair.com, read-only, 2026-11-06
  ~19:26–19:30 UTC / 11:26–11:30 PT): unlike the Razer sweep, the
  US product pages return full product offers (price + InStock) in
  the page text for every pick, so direct prices are page-verified
  rather than feed-derived. Feed shelf observed across the 5 Meta
  Catalog runs (100 rows): M65 RGB Ultra $59.99 wired / $129.99
  wireless; M65 RGB Elite $79.99 / Pro RGB $59.99–$69.99 (older
  models); K65 Plus Wireless $159.99 base / $129.99 Tactile /
  $119.99 Atomic Purple / $169.99 licensed editions (CoD: Black
  Ops 7, Witcher 3, Cyberpunk Edgerunners 2, Cyberpunk 2077
  Arasaka White) / $179.99 Frost White + Glacier Blue Mac-and-PC
  editions / $67.99 Revival; K70 MAX $249.99 Discontinued; K70
  CORE SE $89.99–$109.99; K100 RGB OPX standard page not current
  (Revival only, $129.99); Virtuoso Max $249.99 Carbon/Silver/Xbox
  (list $299.99); Virtuoso RGB Wireless XT $199.99; HS80 Max
  Wireless $119.99; HS80 v2 Max $199.99; FRAME 4000D RS ARGB
  $119.99 Black / $124.99 White; FRAME 4000D $104.99; FRAME 4000D
  LCD RS ARGB $399.99; Titan II 360 RX RGB $179.99 / Titan II 360
  RX LCD $239.99; Titan (gen 1) 360 RX RGB $199.99 OutOfStock;
  iCUE H150i RGB Pro XT $159.99 Discontinued / Elite $204.90
  Discontinued; RM850x $149.99 Discontinued / RM850x SHIFT 2nd gen
  (US price unverified); Vengeance RGB DDR5 32GB 6000 CL30
  $599.99–$657.99 with conflicting stock; XENEON 27QHD240 OLED
  $999.99 OutOfStock direct; WARTHOG $179.99 / WARTHOG RS $199.99
  pre-order only. Full candidate list (list-only): M65 RGB Ultra
  Wireless $129.99; Sabre RGB Pro Wireless (price unverified);
  K65 Plus Wireless Tactile $129.99; K70 CORE SE $89.99–$109.99;
  K100 RGB OPX (Revival $129.99 only); HS80 Max Wireless $119.99;
  HS80 v2 Max $199.99; Virtuoso RGB Wireless XT $199.99; Vengeance
  RGB DDR5 32GB 6000 CL30 $599.99–$657.99; RM850x SHIFT 2nd gen
  (US price unverified); XENEON 27QHD240 OLED $999.99 (direct
  OutOfStock); WARTHOG $179.99 / WARTHOG RS $199.99 (pre-order).
  Not added (no clean pin): K70 MAX and RM850x (2024) — both
  Discontinued on corsair.com; the older iCUE 4000D RGB Airflow —
  Discontinued; XENEON 27QHD240 OLED — direct OutOfStock; WARTHOG
  — pre-order only, not shipping; Vengeance RGB DDR5 — prices
  volatile across $599.99–$657.99 with conflicting stock crawls.
  No controller pick: Corsair sells no first-party controller on
  corsair.com US (SCUF is a separate store).
- Membership check (against the 115-model set, by name, MPN and
  UPC): grep finds zero 'corsair' in price_agent/catalog.py — the
  set had no Corsair entry at all, so no name, MPN or UPC overlap
  for any of the 5 picked models. M65 RGB Ultra (CH-9309411-NA2):
  no match — the set's mice are Logitech and Razer, different
  brands and models. K65 Plus Wireless (CH-91D401L-NA): no match —
  distinct from the set's Logitech, Keychron and Razer boards.
  Virtuoso Max (CA-9011372-WW): no match — distinct from the set's
  Sony, Bose, JBL and Razer headsets. FRAME 4000D RS ARGB
  (CC-9011296-WW): no match — the set had no PC case at all.
  Titan II 360 RX RGB (CW-9061037-WW): no match — the set had no
  CPU cooler at all.
- Per-model record (all 5 added; identifiers, quotes, pending):
- Corsair M65 RGB Ultra, Black, wired (CH-9309411-NA2) —
  identifiers PENDING: MPN confirmed (Corsair US SKU + Micro
  Center feed row + ShopAbunda spec table agree; ShopAbunda also
  ties the SKU to Black), but UPC 840006657613 is stated on the
  Micro Center feed row only — no second non-Amazon US source.
  Not copied: the original CH-9309411-NA SKU (US page $69.99
  Discontinued — a superseded revision); the Wireless MPN
  CH-9319511 (EU White CH-9319511-EU2 at 129.99 EUR); the M65 RGB
  Elite / Pro RGB (different, older models). Quotes (3): Corsair
  direct $59.99 (US page $59.99 InStock, page-verified; feed
  brand_direct rows agree); Micro Center $59.99 (feed row, Mfr
  Part # + UPC in the row; page-verified $59.99 InStock, JSON-LD);
  CDW $84.99 (feed row — suspected; above list, not
  page-verified). Excluded: FlexShopper $3/$6/$7 rows
  (lease-to-own marketplace); the $469.97 mouse + headset +
  keyboard bundle; wireless rows (different connectivity).
- Corsair K65 Plus Wireless, Midnight Grey, MLX Red linear
  (CH-91D401L-NA) — identifiers PENDING: MPN confirmed (Corsair
  US SKU + Best Buy US Model agree), but no UPC surfaced on any US
  manufacturer or retailer spec page. Not copied: the Tactile MPN
  CH-91D441F-NA ($129.99, different switches); the licensed-edition
  SKUs (CoD: Black Ops 7 CH-91B4BCD-NA, Witcher 3 CH-91B4BBD-NA,
  Cyberpunk Edgerunners 2 CH-91D401N-NA, Cyberpunk 2077 Arasaka
  White CH-91D401M-NA); the Frost White / Glacier Blue Mac-and-PC
  editions (different colorways); the K65 Plus wired ($179.99).
  Quotes (2): Corsair direct $159.99 (US page $159.99 InStock,
  page-verified; feed brand_direct row agrees); Best Buy $159.99
  (Model CH-91D401L-NA, SKU 6572502, Black/Gray, search-index page
  read). A 4-day-old crawl showed $129.99 InStock and another
  $159.99 OutOfStock — the live page read today says $159.99
  InStock and Best Buy agrees, so $159.99 is recorded and $129.99
  is treated as a lapsed sale. Excluded: Revival/refurbished rows
  ($67.99/$79.99); the Tactile and licensed-edition rows
  (different variants).
- Corsair Virtuoso Max Wireless, Carbon (CA-9011372-WW) —
  identifiers PENDING: MPN confirmed (Corsair US SKU + Best Buy
  US Model + manuals.plus agree), but UPC 840440484615 is stated
  only by manuals.plus (reproducing the manual's spec table), an
  eBay listing and Amazon — no retailer or manufacturer listing
  states it and the Best Buy page text does not carry it. Not
  copied: the Silver EAN 0840440484622 (CA-9011373-WW, different
  colorway); the Xbox EAN 0840440484639 (CA-9011374-WW, different
  platform variant). Quotes (3): Corsair direct $249.99 (US page
  $249.99 InStock, page-verified; feed brand_direct rows agree —
  a holiday sale price vs the $299.99 list, re-check after the
  sale ends, Early Black Friday ends Nov 8); Best Buy $249.99
  (Model CA-9011372-WW, SKU 6594136, Holiday Deal, comp. value
  $299.99, page-verified); Corsair $299.99 (feed brand_direct row
  on checkout.corsair.com — suspected; a stale list-price row).
  Excluded: Virtuoso RGB Wireless XT $199.99 / Virtuoso RGB
  Wireless $199.99 (previous-generation lines); Revival $147.99
  (refurbished); ShopAbunda $229.99 (Amazon-fulfilled).
- Corsair FRAME 4000D RS ARGB, Black (CC-9011296-WW) —
  identifiers PENDING: MPN confirmed (Corsair US SKU +
  custompcgaming, mixed-news and Toppreise spec tables agree it is
  the Black RS ARGB case), but UPC 840440487715 is stated on
  Amazon.in only. Not copied: the White MPN CC-9011297-WW
  ($124.99, confirmed by Newegg + Scan UK — a different colorway;
  its Amazon-only UPC 840440487722 was not recorded either); the
  fanless FRAME 4000D ($104.99) and FRAME 4000D RS non-ARGB
  (CC-9011312-WW, $114.99 — different fan configuration); the
  FRAME 4000D LCD RS ARGB ($399.99, different model). Quotes (2):
  Corsair direct $119.99 (US page $119.99 InStock, page-verified;
  feed brand_direct rows agree); Newegg $114.99 (feed row —
  suspected; the feed title reads 'Non-LED' while the model is RS
  ARGB and the Newegg page text shows no price or MPN, so the row
  may belong to the non-ARGB RS case). Excluded: the older iCUE
  4000D RGB Airflow (Discontinued); the RS ARGB All-in-One bundles
  ($399.96/$484.96).
- Corsair iCUE LINK Titan II 360 RX RGB, Black (CW-9061037-WW) —
  identifiers PENDING: MPN confirmed (Corsair US SKU + Best Buy
  US Model + Newegg + Scan UK agree), but GTIN 840440419464 is
  stated on the Scan UK page only — no second, US source. Not
  copied: the White GTIN 840440419471 (CW-9061038-WW, different
  colorway, OutOfStock on corsair.com); the Titan II 360 RX LCD
  ($239.99, different model); the previous-generation Titan 360 RX
  RGB (CW-9061018-WW, $199.99, OutOfStock). Quotes (3): Corsair
  direct $179.99 (US page $179.99 InStock, page-verified); Best Buy
  $179.99 (Model CW-9061037-WW, SKU 6683807, Black, sold by Best
  Buy, Add to cart, JSON-LD InStock, page-verified — the page's
  'About this product' block wrongly describes the Titan II Ultra
  360 LX LCD, a Best Buy copy error); Newegg $179.99 (feed row —
  suspected; no identifier in the feed row, not page-verified).
  Excluded: FlexShopper $11 (lease-to-own marketplace); the Titan
  360 RX LCD + fan bundles ($309.97–$414.97); the iCUE H150i RGB
  Pro XT / Elite (Discontinued).
- Not added from the sweep (held for later batches, all current
  US models, no defect): M65 RGB Ultra Wireless $129.99; K65 Plus
  Wireless Tactile $129.99; K70 CORE SE $89.99–$109.99; HS80 Max
  Wireless $119.99; HS80 v2 Max $199.99; Virtuoso RGB Wireless XT
  $199.99; Vengeance RGB DDR5 32GB 6000 CL30 $599.99–$657.99
  (volatile, conflicting stock); WARTHOG $179.99 / WARTHOG RS
  $199.99 (pre-order only). Not added (no clean pin): K70 MAX /
  RM850x (2024) / iCUE 4000D RGB Airflow (Discontinued); XENEON
  27QHD240 OLED (direct OutOfStock); K100 RGB OPX (standard US
  page not current — Revival only).
- Eval on the new snapshot: 120 models, 69 verified identifiers,
  5 with quotes, 13 total quotes, 0 identifier-matched, 13
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 115 → 120 for the continuous expansion;
  verified stays 69; the pending set gains the 5 new Corsair keys).

## 058 — 2026-11-06: Expansion batch 20 — 120 → 125 models (DECISIONS 042)

- Dell US store sweep (dell.com, read-only, 2026-11-06
  ~19:33–19:35 UTC / 11:33–11:35 PT): Dell US product pages confirm
  model identity and MPNs in page text, but prices render via JS,
  so Dell direct prices are search-index / category-page reads —
  the Dark Side of the Moon category page returns full offers with
  Add to Cart for the Pro Mouse and Pro Keyboard, and the monitor
  pages return full Tech Specs (S3225QS MPN F06FR, Ash White;
  AW2726DM MPN JW05F, Black). Dell laptops and desktops are
  configurable: XPS 14 (2026) DA14260 from ~$1,599 and XPS 14 9440
  $1,700 sale have no fixed base configuration; Alienware 16 Aurora
  AC16250 featured config $1,349.99 is Sold Out; XPS Desktop 8960
  $1,060 sale and Alienware Aurora R16 RTX 5080 from $1,849.99 are
  configurable — no laptop or desktop was added (DECISIONS 015).
  Feed shelf observed across the 5 Meta Catalog runs (99 rows):
  S3225QS Dell $369.99 list / Best Buy $379.99 / Micro Center
  $399.99; AW2726DM Dell $349.99 list (plus AW3226DM 32-inch
  $299.99, AW2726DL 280 Hz $229.99, AW3426DWM 34-inch $399.99,
  AW2725QF 4K $499.99, AW3926QW 39-inch 5K $1,099.99, AW2525HM
  25-inch 320 Hz $249.99, AW2725DM $269.99, AW3425DWM $349.99);
  Pro Mouse Best Buy Lunar Light $149.99 / Newegg $160.99 /
  AW720M $79.99 / AW620M $99.99; Pro Keyboard Best Buy Lunar Light
  $199.99 / Newegg $294.99 / AW920K $159.99 / AW510K $129.99 /
  AW420K $99.99; Pro Headset Dell $229.99 + $199.99 (Dark Side
  slug) / Best Buy Dark Side $229.99 + Lunar Light $199.99 /
  Newegg $301.99 / AW725H $149.99 / AW920H $109.99 / AW520H $79.99;
  S3225QC 32-inch 4K QD-OLED $620.41 (Walmart). Full candidate list
  (list-only): S2725QS 27-inch 4K ~$279.99; S2725DSM 27-inch QHD
  $189.99; S2725HSM 27-inch FHD $159.99; S2425HSM 24-inch FHD
  $129.99; SE2426H 24-inch $89.99; S3225QC 32-inch 4K QD-OLED
  $620.41; UltraSharp U3225QE 32-inch 4K $1,099.99; AW3226DM 32-inch
  240 Hz $299.99; AW2726DL 27-inch 280 Hz $229.99; AW3225DM 32-inch
  $249.99; AW2525HM 25-inch 320 Hz $249.99; AW2725DM 27-inch
  $269.99; AW2725QF 27-inch 4K dual-resolution $499.99; AW3426DWM
  34-inch 240 Hz $399.99; AW3425DWM 34-inch $349.99; AW3926QW
  39-inch 5K OLED $1,099.99; AW2725Q 27-inch 4K $799.99; AW720M
  Tri-Mode Mouse $79.99; AW620M Wireless Mouse $86.99 sale; AW920K
  Tri-Mode Keyboard $159.99; AW510K Low Profile Keyboard $129.99;
  AW420K Tenkeyless Keyboard $99.99; AW725H Tri-Mode Headset
  $149.99; AW920H Tri-Mode Headset $109.99; AW520H Wired Headset
  $79.99; AW320M Wired Mouse $69.99; Dell Pro 7 Webcam WB726; Dell
  Pro Thunderbolt 5 Smart Dock SD25TB5; Dell Premier Wireless ANC
  Headset WL7022 $299.99; Dell Pro Plus Wireless Speakerphone
  SL525. Not added (no clean pin): XPS 14 (2026), XPS 14 9440,
  Alienware 16 Aurora, XPS Desktop 8960, Alienware Aurora R16 —
  all configurable with no retailer-pinned base configuration
  (DECISIONS 015); Alienware 16 Aurora featured config also Sold
  Out.
- Membership check (against the 120-model set, by name, MPN and
  UPC): grep finds zero 'dell' or 'alienware' brand entries in
  price_agent/catalog.py — 'Dell' appears only as a merchant in
  other entries' notes, so no name, MPN or UPC overlap for any of
  the 5 picked models. S3225QS (F06FR / UPC 884116485131): no
  match — the set had no Dell monitor at all, and no entry carries
  that UPC. AW2726DM (JW05F): no match — distinct from the set's
  monitors (none) and from the AW2724DM (different, older 180 Hz
  model, not in the set). Pro Mouse (PRO-MS-G-DEAM / UPC
  884116464914): no match — the set's mice are Logitech, Razer and
  Corsair, different brands and models. Pro Keyboard (WR47C): no
  match — distinct from the set's Logitech, Keychron, Razer and
  Corsair boards. Pro Headset: no match — distinct from the set's
  Sony, Bose, JBL, Razer and Corsair headsets.
- Per-model record (all 5 added; identifiers, quotes, pending):
- Dell 32 Plus 4K Monitor S3225QS, Ash White (F06FR) —
  identifiers VERIFIED: UPC 884116485131, agreed by the Icecat
  datasheet for DELL-S3225QS (EAN 5397184962374 / GTIN
  0884116485131) and the eBay US product catalog (GTIN
  0884116485131, ePID 21080788835); Amazon US also states it but
  was not used as corroboration. MPN F06FR confirmed (Dell US
  page). Not copied: the Ireland MPN MX17X (regional). Quotes
  (3): Dell direct $329.99 (sale vs $369.99 estimated value,
  search-index reads 2026-10-23/26, topsave + Windows Central;
  the feed brand_direct row still shows the $369.99 list); Best
  Buy $379.99 (Model S3225QS, SKU 6619489, feed row — suspected,
  not page-verified); Micro Center $399.99 (feed row — suspected,
  not page-verified). Excluded: non-US retailer rows (ermitazas,
  k-rauta, nexoltic, cybermoa); the S3225QC QD-OLED rows
  ($620.41, a different model); the P3225QE/P3225DE Pro rows
  (different models); the shop.app $249.95 marketplace row.
- Alienware 27 240Hz QD-OLED Gaming Monitor AW2726DM, Black
  (JW05F) — identifiers PENDING: MPN confirmed (Dell US + CA +
  AU pages agree; the UK MPN N0XJ0 is regional and was not used),
  but no US UPC surfaced — the only code found is EAN
  5397321030553 on a single Icecat datasheet (EU). Not copied:
  the AW2724DM (different, older 180 Hz model); the AW2726DL
  280 Hz IPS ($229.99, different panel); the AW3226DM 32-inch
  ($299.99, different size). Quotes (3): Dell direct $319.99
  (sale vs $349.99 Estimated Value, mixed-news 2026-10-30, 'the
  US listing was accepting orders when checked'; Windows Central
  2026-10-26 agrees); Best Buy $349.99 (Model AW2726DM, SKU
  6670439, search-index JSON-LD read); Dell $349.99 (feed
  brand_direct row — the list price). Excluded: the sigmatiendas
  $660 row (non-US); the Newegg $426.49 row (title truncated,
  model unconfirmed); the AW2724DM $314.99 / AW2725DM $269.99
  Best Buy rows (different models).
- Alienware Pro Wireless Gaming Mouse, Dark Side of the Moon
  (PRO-MS-G-DEAM) — identifiers VERIFIED: UPC 884116464914,
  agreed by the Icecat datasheet for PRO-MS-G-DEAM (EAN
  5397184877548 / GTIN 0884116464914, product color Black,
  multiple locale PDFs of the same datasheet) and the axitech.be
  Black listing (545-BBFP PRO-MS-G-DEAM, EANs 5397184877548
  0884116464914). Dell MPN 2021Y / Dell part 570-BBGJ is the
  Dell-side code for the Dark Side mouse (Ubuy ties 2021Y to Dark
  Side of the Moon; Dell's own accessory listing ties 2021Y to
  the Pro Mouse). Not copied: the Lunar Light UPC 884116464945
  (PRO-MS-W-DEAM, 545-BBFN, a different colorway); the AW720M
  Tri-Mode ($79.99) and AW620M ($86.99 sale) — different, cheaper
  Alienware mice. Quotes (2): Dell direct $129.99 (sale vs
  $149.99 list, Dell US Dark Side of the Moon category page,
  Offer ID 584RN, Add to Cart, page-verified 2026-11-06; 4.5
  stars, 501 reviews); Newegg $160.99 (feed row — suspected;
  above list, color unstated, not page-verified). Excluded: the
  FlexShopper $136.99 row (lease-to-own marketplace); the AW720M
  $149.99 Dell row (a different model mislabeled in the feed);
  the Corsair Sabre v2 Pro rows (different brand).
- Alienware Pro Wireless Gaming Keyboard, Dark Side of the Moon
  (WR47C) — identifiers PENDING: MPN confirmed (Dell US page,
  Dell part 580-BBMZ), and the color mapping is by elimination —
  the other variant X3V4D is Lunar Light (Ubuy + ShopAbunda +
  Icecat PRO-KB-W-WW), so WR47C is Dark Side of the Moon — but
  no Dark Side UPC surfaced: the only UPC found, 884116464853,
  belongs to the White/Lunar Light board (Icecat datasheet
  PRO-KB-W-WW + Ubuy X3V4D agree) and was not carried across
  colorways. Not copied: the AW920K Tri-Mode ($159.99), AW510K
  Low Profile ($129.99) and AW420K TKL ($99.99) — different
  Alienware keyboards. Quotes (2): Dell direct $174.99 (sale vs
  $199.99 list, Dell US Dark Side of the Moon category page,
  Offer ID K6YT7, Add to Cart, page-verified 2026-11-06; 4.6
  stars, 448 reviews; the Dell US product page 580-BBMZ agrees
  at $174.99 InStock; the feed brand_direct row still shows the
  $199.99 list); Newegg $294.99 (feed row — suspected; above
  list, color unstated, not page-verified). Excluded: the Best
  Buy Lunar Light $199.99 row (SKU 6571728, a different
  colorway); the AULA / CHERRY / YUNZII rows (different brands).
- Alienware Pro Wireless Gaming Headset, Dark Side of the Moon —
  identifiers PENDING: no MPN pinned (the 83XJY code in a
  distributor pricelist covers both colorways, so it is a family
  code, not a Dark Side code; Best Buy's BBY-AWProH-D is a
  Best Buy-specific model code). The only UPC candidate,
  884116469728, is stated on manuals.plus alone (reproducing the
  manual's spec table for ASIN B0DHWH425M, color unattributed),
  while Amazon's Lunar Light listing states 884116469759 — two
  colorways, two codes, neither corroborated by a second
  non-Amazon source, so identifiers stay empty per the DualSense
  precedent. Not copied: the Lunar Light UPC 884116469759; the
  AW725H Tri-Mode ($149.99) and AW920H ($109.99) — different
  Alienware headsets. Quotes (2): Dell direct $174.99 (sale vs
  $199.99 list, Dell US search-index read, Offer ID 9K2M1;
  techaeris Black Friday hub 2026-11-05 agrees at $174.99); Best
  Buy $199.99 (Dark Side of the Moon, Model BBY-AWProH-D, SKU
  6605023, save $30 off comp. value $229.99, search-index page
  read). The Meta feed today shows $229.99 list rows for both
  merchants and a $199.99 Dell row (N6YJD, Dark Side slug) — the
  feed lags the sale, so the page reads win per the Quill
  precedent; re-check after the Early Black Friday event ends
  Nov 8. Excluded: the mydex.shop $319.49 row (unknown merchant,
  seller_type 'other'); the Newegg $301.99 row (above list,
  color unstated); the Walmart $228.99 AW720H row (different
  model); the SteelSeries / Logitech / Turtle Beach rows sold on
  dell.com (different brands).
- Not added from the sweep (held for later batches, all current
  US models, no defect): S2725QS 27-inch 4K ~$279.99; S2725DSM
  27-inch QHD $189.99; S2725HSM 27-inch FHD $159.99; S2425HSM
  24-inch FHD $129.99; SE2426H 24-inch $89.99; S3225QC 32-inch 4K
  QD-OLED $620.41; UltraSharp U3225QE 32-inch 4K $1,099.99;
  AW3226DM 32-inch 240 Hz $299.99; AW2726DL 27-inch 280 Hz
  $229.99; AW3225DM 32-inch $249.99; AW2525HM 25-inch 320 Hz
  $249.99; AW2725DM 27-inch $269.99; AW2725QF 27-inch 4K
  dual-resolution $499.99; AW3426DWM 34-inch 240 Hz $399.99;
  AW3425DWM 34-inch $349.99; AW3926QW 39-inch 5K OLED $1,099.99;
  AW2725Q 27-inch 4K $799.99; AW720M $79.99; AW620M $86.99 sale;
  AW920K $159.99; AW510K $129.99; AW420K $99.99; AW725H $149.99;
  AW920H $109.99; AW520H $79.99; AW320M $69.99; Dell Pro 7 Webcam
  WB726; Dell Pro Thunderbolt 5 Smart Dock SD25TB5; Dell Premier
  Wireless ANC Headset WL7022 $299.99; Dell Pro Plus Wireless
  Speakerphone SL525. Not added (no clean pin): XPS 14 (2026),
  XPS 14 9440, Alienware 16 Aurora, XPS Desktop 8960, Alienware
  Aurora R16 — all configurable with no retailer-pinned base
  configuration (DECISIONS 015).
- Eval on the new snapshot: 125 models, 71 verified identifiers,
  5 with quotes, 12 total quotes, 0 identifier-matched, 12
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 120 → 125 / 69 → 71 for the continuous
  expansion; the pending set gains the 3 new pending keys:
  alienware-27-qd-oled-aw2726dm,
  alienware-pro-wireless-gaming-keyboard-dark-side-of-the-moon,
  alienware-pro-wireless-gaming-headset-dark-side-of-the-moon).

## 059 — 2026-11-06: Brand sweep — HP, Lenovo, ASUS + remaining Dell (candidates LIST-ONLY, DECISIONS 013/015/021)

- Read-only sweep, 2026-11-06 ~19:40–20:10 UTC / 11:40–12:10 PT (no
  cart, no sign-in, no purchase; no Meta Catalog CLI run, no Amazon
  anywhere). Sources: hp.com/us-en product and category pages
  (search-index reads, prices in JSON-LD), asus.com/us + rog.asus.com
  US store/category pages (search-index + one direct page read),
  lenovo.com/us (see the Lenovo caveat below — the US store would
  not surface in search; Lenovo prices below are corroborated from
  US press/retailer reads and are flagged where they are not
  lenovo.com-direct), and the Dell held-candidate list from BUILD_LOG
  058 (recorded earlier today, carried forward, not re-priced).
  Membership check: grep of price_agent/catalog.py finds zero HP,
  Lenovo or ASUS brand entries in the 125-model set (the only
  'HP'/'Lenovo'/'ASUS' strings are merchant mentions in other
  entries' notes), and no Dell model below duplicates the 5 Dell
  entries added in batch 20 (S3225QS, AW2726DM, Pro Mouse, Pro
  Keyboard, Pro Headset). No candidate below matches an existing
  model on name, MPN or UPC. Nothing was added to catalog.py.
- HP (hp.com/us-en — readable, prices in page JSON-LD):
  - OMEN 27s 27" FHD 240Hz gaming monitor, $389.99, InStock, MPN
    780G5AA#ABA.
  - OMEN 27k 27" UHD 144Hz gaming monitor, $370.32, InStock, MPN
    780G8AA#ABA.
  - HyperX OMEN OLED 27q 27" QHD 240Hz gaming monitor, $399.99,
    InStock, MPN CH0R2AA#ABA.
  - OMEN 27q G2 27" QHD 180Hz gaming monitor, $203.99, InStock,
    MPN AV4H6AA#ABA.
  - HP Series 3 Pro 27" FHD Monitor 327pf, $194.00, In Stock, MPN
    B0CG3UT#ABA.
  - HP E24mv G4 FHD Conferencing Monitor, $210.40, InStock, MPN
    169L0AA#ABA.
  - HP E27k G5 4K USB-C Monitor, $504.00, In Stock, MPN
    6N4C4AA#ABA.
  - HyperX Cloud III Gaming Headset, Black-Red, $99.99, MPN
    4P5M0AA (bundle listing + OMEN desktop accessory upsell agree).
  - HyperX Cloud III S Wireless, Black-Red, $179.99 (hp.com US
    headsets category page).
  - HyperX CloudX Flight 2 Wireless Gaming Headset, Black (Xbox),
    $139.99 (hp.com US headsets category page).
  - HyperX CloudX Gaming Headset, Black-Silver (Xbox), $59.99
    (hp.com US headsets category page).
  - HyperX Alloy Rise 75 Gaming Keyboard, $84.99 sale (was
    $169.99), MPN 7G7A4AA#ABA.
  - HyperX Pulsefire Haste 2 Pro Wireless Gaming Mouse, $119.99
    (hp.com US accessory upsell on OMEN laptop pages).
  - HyperX Pulsefire Haste 2 Wireless Gaming Mouse, Black, $89.99,
    MPN 6N0B0AA.
  - HyperX QuadCast 2 S USB Microphone, Black, $149.99 sale (was
    $199.99), MPN 9A273AA.
  - HP 920 Ergonomic Vertical Mouse, $68.99, InStock, MPN
    6H1A4AA#ABA.
  - HP 710 Rechargeable Silent Mouse, $79.99 (US list price from
    2023 reviews; US MPN not confirmed on hp.com/us — 6E6F1AA is
    the AU SKU, 6E6F2AA appears on an India listing — identifier
    stays open).
  - HP 960 4K Streaming Webcam, $219.99 list (2022 reviews; no
    current hp.com/us price read this sweep — stale, needs a
    fresh page read before any batch).
  - HP Series 3 27" FHD 327se (2025), ~$178.49, and HP E27u G4
    QHD, $343.98–$499.00 — observed only in third-party roundups,
    not on hp.com/us; prices NOT pinned, needs an hp.com read.
  - Excluded (HP): all OMEN / Victus / HP laptops and OMEN 35L
    desktops — configurable, no single pinnable base configuration
    (DECISIONS 015; e.g. OMEN 15t-ga000 from $1,249.99, OMEN
    35L GT16-0100t from $2,699.99); all HyperX bundles (Cloud II +
    Haste 2 + Alloy Core kit $129.00; Alloy Rise + Cloud III S +
    Saga Pro kit $286.00; Alloy Core + Pulsefire Fuse kit $78.99;
    Cloud II + Haste 2 kits $100.00; HP 920 + HP 960 bundle
    $144.73) — bundles, not standalone lines; HP 725 keyboard/
    mouse combo — bundle; HP printers (OfficeJet/LaserJet) — not
    swept in depth: no printer category exists in the 125-model
    set, so adding one needs a category decision first, not a
    silent batch addition; refurbished/clearance lines — none
    listed as candidates.
- Lenovo (lenovo.com/us — NOT readable this sweep, stated plainly):
  every search for the US store returned the India store
  (store.lenovo.com/in, INR prices) or non-US regional pages; no
  lenovo.com/us/en product page surfaced with a USD price, so no
  Lenovo price below is a lenovo.com-direct read. Candidates rest
  on US press/retailer corroboration and need a lenovo.com/us
  page read (live-browser takeover or a later indexed read) before
  any batch:
  - Lenovo Legion Tab Gen 5, 8.8", 12GB/256GB, Eclipse Black
    (ZAH20126US) — Lenovo direct $699.99 sale (was $899.99 list;
    launch $849, May 2026); B&H $799.99 (was $899.99), UPC
    199275342448. Single US configuration, so pinnable.
  - Lenovo Yoga Tab Plus Gen 2, 13", 12GB/256GB, Snapdragon 8
    Elite — Lenovo direct $799.99 sale (was $999.99 list); ships
    with Tab Pen Pro 2 + folio keyboard in the box (bundled
    accessories, not a multi-product bundle — flag at batch time).
  - Lenovo Yoga Tab Gen 2, 11.1" — Lenovo direct $599.99 sale
    (was $729.99 list).
  - Lenovo Tab Plus Gen 2, 12.1", 8GB/128GB (only NA config) —
    $399.99 at North-America launch, now $469.99 per PhoneArena
    2026-10-26 (price moved; re-check before any batch).
  - Lenovo Legion Go 2, 1TB — Lenovo US $1,999.99, but listed
    "available soon" / out of stock at Lenovo (Best Buy has
    stock); price has climbed twice from a $1,349.99 launch, so
    treat as volatile. The 32GB/2TB config at $3,081.99 is
    excluded (out of stock at Lenovo + 2x launch price).
  - Lenovo Legion R34w-30 34" Curved WQHD 180Hz monitor —
    Staples $453.29 (JSON-LD, LimitedAvailability); US MPN not
    confirmed.
  - Lenovo Legion Y25-25 24.5" FHD 240Hz monitor — $249.99 US
    (price-history trackers, Amazon-derived; list $369.99/$339.99
    conflicting) — needs a US retailer page read.
  - Lenovo Legion R27fc-30 27" FHD 280Hz curved monitor — $179
    US (Kotaku, Amazon-derived, was $239); US MPN 67B6GAC1US
    appears on AU/IN listings only (67B6GAC1AU / 67B6GAC1IN) —
    US code unconfirmed.
  - Lenovo Legion K500 RGB Mechanical Gaming Keyboard, US English
    (GY40T26478) — $63.99–$87.34 US (Amazon-derived $63.99;
    Compsource $87.34 InStock); 2019 line, still sold in the US.
  - Lenovo Legion M600 RGB Wireless Gaming Mouse (GY51C96033) —
    $123.49 US (Amazon-derived only) — needs a US retailer read.
  - ThinkVision P34WD-4v $699 / P27UL-40 $1,299 / T32UD-4v $899 —
    IFA 2026 launch prices, global rollout; US availability not
    confirmed — observed only, not pinned.
  - Legion 24-1r / 27-1r 280Hz monitors from $99 (July 2026
    launch) — US availability not confirmed — observed only.
  - Excluded (Lenovo): all ThinkPad / Yoga / Legion / IdeaPad
    laptops and Legion / ThinkCentre desktops — configurable, no
    single pinnable base configuration (DECISIONS 015); Legion
    MK2 keyboard — China-only, no US release (DECISIONS 021);
    Legion H500 Pro headset ($99.99, 2019 launch) — legacy line,
    no current US price found; Legion 27Q-20 monitor — China-only
    launch (¥1,149), global release unconfirmed.
- ASUS (asus.com/us + rog.asus.com — readable; ASUS Store prices
  shown on category pages, eShop operated by a reseller/distributor
  per ASUS's own note):
  - ROG Swift OLED PG27UCWM 27" 4K 240Hz, $1,199.00 (flagged
    Temporarily out of stock on one ROG listing).
  - ROG Swift OLED PG32UCWM 32" 4K 240Hz, $1,399.00 (also flagged
    Temporarily out of stock on one ROG listing).
  - ROG Swift OLED PG27AQDPR 27" QHD 500Hz, $899.00 (sale, save
    $170).
  - ROG Swift OLED PG32UCDM Gen3 (PG32UCDM3) 32" 4K 240Hz,
    $1,299.00.
  - ROG Swift OLED PG27UCDM 27" 4K 240Hz, $1,099.00.
  - ROG Strix OLED XG32UQDS 32" 4K 180Hz, $749.00.
  - ROG Swift OLED PG34WCDN 34" ultrawide, $1,299.00.
  - ROG Swift OLED PG32UCDMR 32", $1,299.00 — Out of Stock on the
    ASUS eShop page (Part No. 90LM0C00-B019B2); candidate with a
    stock caveat, not a clean pin.
  - ROG Delta II Gaming Headset, $185.99 (rog.asus.com JSON-LD,
    InStock).
  - ROG Delta Gaming Headset (USB-C), $149.99.
  - ROG Pelta Core Gaming Headset, $119.99.
  - ROG Pelta Gaming Headset, from $84.99 ($129.99 full price
    shown on the same listing — two prices, needs a page read to
    pin which tier is the base).
  - ROG Cetra Open Wireless Gaming Earbuds, $229.99.
  - ROG Kithara Gaming Headset, $259.99 sale (was $299.99).
  - ROG Gladius IV Ace Gaming Mouse, $169.99.
  - ROG Spatha X 65K Gaming Mouse, $179.99.
  - ROG Harpe II Ace Gaming Mouse, price not shown on the
    category-page read (name/specs only) — needs a page read.
  - ROG Harpe Mini Core Gaming Mouse, $69.99.
  - ROG Keris II Origin-KJP Gaming Mouse, price not shown on the
    category-page read — needs a page read.
  - ROG Azoth 96 HE Lite analog keyboard, $359.99.
  - ROG Azoth 96 HE analog keyboard, $308.99.
  - ROG Strix Morph 96 Wireless keyboard, $115.99 sale (was
    $139.99).
  - ROG Strix Scope II 96 RX Wireless keyboard, $132.99 sale (was
    $179.99).
  - ROG Falchion Ace 75 HE keyboard, from $177.99 (was $219.99).
  - Excluded (ASUS): all Zenbook / Vivobook / ROG / TUF laptops
    and desktops — configurable, no single pinnable base
    configuration (DECISIONS 015); ROG Azoth Extreme Edition 20
    keyboard ($599.99) and ROG Harpe II Extreme Edition 20 mouse
    ($259.99) — limited 20th-anniversary editions, not mainstream
    lines; ROG Gjallar Gaming Soundbar $599.99 — soundbar, no
    soundbar category in the set (same category-decision caveat as
    HP printers); mouse pads (Scabbard/Sheath/Hone, $35.99–
    $89.99) — accessories, not a set category; phones (Zenfone)
    — out of scope per the iPhone precedent (DECISIONS 006/013);
    ASUS routers — not swept (no router category in the set).
  - Identifier note (ASUS): no MPN/UPC surfaced on the ASUS
    category pages read; the one part number seen is PG32UCDMR
    90LM0C00-B019B2. ASUS identifiers will need per-model page
    reads at batch time — 0 of ~24 ASUS candidates carry an
    identifier from this sweep.
- Dell, remaining (carried forward from BUILD_LOG 058, recorded
  2026-11-06, not re-priced): S2725QS 27" 4K ~$279.99; S2725DSM
  27" QHD $189.99; S2725HSM 27" FHD $159.99; S2425HSM 24" FHD
  $129.99; SE2426H 24" $89.99; S3225QC 32" 4K QD-OLED $620.41;
  UltraSharp U3225QE 32" 4K $1,099.99; AW3226DM 32" 240Hz
  $299.99; AW2726DL 27" 280Hz $229.99; AW3225DM 32" $249.99;
  AW2525HM 25" 320Hz $249.99; AW2725DM 27" $269.99; AW2725QF 27"
  4K dual-resolution $499.99; AW3426DWM 34" 240Hz $399.99;
  AW3425DWM 34" $349.99; AW3926QW 39" 5K OLED $1,099.99;
  AW2725Q 27" 4K $799.99; AW720M Tri-Mode Mouse $79.99; AW620M
  Wireless Mouse $86.99 sale; AW920K Tri-Mode Keyboard $159.99;
  AW510K Low Profile Keyboard $129.99; AW420K Tenkeyless Keyboard
  $99.99; AW725H Tri-Mode Headset $149.99; AW920H Tri-Mode
  Headset $109.99; AW520H Wired Headset $79.99; AW320M Wired
  Mouse $69.99; Dell Pro 7 Webcam WB726; Dell Pro Thunderbolt 5
  Smart Dock SD25TB5; Dell Premier Wireless ANC Headset WL7022
  $299.99; Dell Pro Plus Wireless Speakerphone SL525. Excluded
  (Dell, unchanged from 058): XPS 14 (2026), XPS 14 9440,
  Alienware 16 Aurora, XPS Desktop 8960, Alienware Aurora R16 —
  configurable, no retailer-pinned base configuration
  (DECISIONS 015); Alienware 16 Aurora featured config also Sold
  Out.
- Pool assessment: yes — comfortably big enough for 25 more models
  (batches 21–25). Cleanest, best-evidenced pool is HP (~17
  candidates with hp.com/us prices + MPNs) + ASUS (~24 candidates,
  prices confirmed but identifiers open) + Dell held list (~30
  candidates from 058). Lenovo is the thin leg: ~10 candidates,
  none with a lenovo.com/us-direct price this sweep, and two of
  the strongest (Legion Tab Gen 5, Yoga Tab Plus Gen 2) need a
  lenovo.com/us page read before a batch. Recommended batch order:
  HP monitors/accessories first, then ASUS monitors/headsets,
  then Dell held monitors/accessories, with Lenovo tablets held
  until the US store can be read. No catalog, DECISIONS,
  CHANGELOG, test or snapshot file was touched.

## 060 — 2026-11-06: Expansion batch 21 — 125 → 130 models (DECISIONS 043)

- HP official US store verification (hp.com/us-en + hyperx.com US,
  read-only, 2026-11-06 ~19:43–19:50 UTC / 11:43–11:50 PT): all
  five HP US product pages return full JSON-LD offers, InStock, at
  the sweep prices — OMEN 27s $389.99 (780G5AA#ABA), Cloud III
  Black-Red $99.99 (Product # 727A9AA), HP 920 $68.99
  (6H1A4AA#ABA), OMEN 27q G2 $203.99 (AV4H6AA#ABA), Alloy Rise 75
  $84.99 (hyperx.com, single variant Black / US Layout / HyperX
  Red - Linear, wired, Available). HP laptops and desktops are
  configurable: no laptop or desktop was added (DECISIONS 015).
  Feed shelf observed across the 5 Meta Catalog runs (100 rows):
  27s HP $389.99 brand_direct (hp.com + hyperx.com rows) /
  Distritech $217.49 / Newegg $309; Cloud III HP $99.99
  brand_direct for every colorway (Black-Red, Black, White,
  White/Pink, Black/Blue) / Best Buy Black-Blue $99.99 / Staples
  Black/Red 727A9AA $104.59 / thinkedu Black 727A8AA $99.99 /
  Newegg $159.69 (color unstated); HP 920 HP $114.99 list / $68.99
  sale brand_direct / Best Buy $68.99 sale (SKU 12714516) / HP 925
  $114 list / $68 sale (different, business model) / tecisoft
  $298.65 / tech-ment $167.99; 27q G2 HP $339.99 list / $203.99
  sale brand_direct / Newegg $218.99 (AV4H6AA) / Micro Center
  $169.99 marketplace / Newegg $553.98; Alloy Rise 75 HyperX
  $84.99 brand_direct / Target $84.99 sale / Best Buy $84.99 sale
  (SKU 11006248) / Newegg $169.99 list / Newegg $281.98 (second,
  unconfirmed listing).
- Membership check (against the 125-model set, by name, MPN and
  UPC): grep finds zero 'HP', 'HyperX' or 'OMEN' brand entries in
  price_agent/catalog.py — the only 'HP' strings are merchant
  mentions in other entries' notes, and the '920' hits are
  Logitech part numbers (920-011559, 920-010475), so no name, MPN
  or UPC overlap for any of the 5 picked models. OMEN 27s
  (780G5AA#ABA): no match — the set had no HP monitor at all.
  Cloud III (727A9AA): no match — distinct from the set's Sony,
  Bose, JBL, Razer and Corsair headsets. HP 920 (6H1A4AA#ABA / UPC
  197029640277): no match — the set's mice are Logitech, Razer,
  Corsair and Alienware. OMEN 27q G2 (AV4H6AA#ABA): no match —
  distinct from the 27s (different resolution/refresh) and from
  the OMEN 27q (780H4AA, older 165 Hz model, not in the set).
  Alloy Rise 75 (7G7A4AA#ABA): no match — distinct from the set's
  Logitech, Keychron, Razer, Corsair and Alienware boards.
- Per-model record (all 5 added; identifiers, quotes, pending):
- HP OMEN 27s FHD 240Hz Gaming Monitor, Black (780G5AA#ABA) —
  identifiers PENDING: MPN confirmed (HP US page), but the US UPC
  is single-source only — the HP datasheet (1WorldSync syndication
  + the same document mirrored on Etilize) lists UPC/EAN (ABA)
  197029615442 for P/N 780G5AA#ABA, and no second independent
  non-Amazon source states it (B&H lists the 780G5AA#ABA page with
  no UPC and marks it Discontinued at $349.99; Amazon also states
  197029615442 but Amazon never corroborates), so identifiers stay
  empty per the strict two-source rule. Not copied: 197029615466
  (the ABB regional code); the OMEN 27 (165 Hz, Z4D33AA) and OMEN
  27q/27qs lines (different models). Quotes (2): HP direct $389.99
  (InStock, page JSON-LD read); Newegg $309 (feed
  authorized_retailer row — suspected; color unstated, not
  page-verified). Excluded: the Distritech $217.49 row (44% below
  the HP list, not page-verified, unconfirmed outlier); the OMEN
  27q G2 $553.98 row in the same feed run (different model).
- HyperX Cloud III Gaming Headset, Black-Red (727A9AA) —
  identifiers PENDING: MPN confirmed (HP US page + Staples feed
  row agree), but the only UPC found, 197029008237, is stated on
  Amazon listings only (Amazon.com/.ca/.in, ASIN B0C3BV19Q3) — and
  those same listings also carry a second, conflicting code
  740617255522 — so identifiers stay empty per the DualSense
  precedent. Correction vs sweep 059: the Black-Red MPN is 727A9AA
  on the HP US product page, not 4P5M0AA (bundle/upsell code);
  4P5M0AA was not recorded. Not copied: 727A8AA (Black), BS7C1AA
  (White), DF7F0AA (Black/Lavender) — different colorways at the
  same $99.99; the Cloud III Wireless / Cloud III S Wireless
  (different, wireless models). Quotes (3): HP direct $99.99
  (InStock, page JSON-LD read); Staples $104.59 (Black/Red 727A9AA,
  feed row — suspected; not page-verified); Newegg $159.69 (feed
  row — suspected; color unstated, above list, not
  page-verified). Excluded: the Best Buy Black-Blue $99.99 row (a
  different colorway); the Cloud III bundle rows ($179.99/$199.99,
  bundles, not standalone).
- HP 920 Ergonomic Vertical Mouse, Black (6H1A4AA#ABA) —
  identifiers VERIFIED: UPC 197029640277, agreed by the HP
  datasheet for the 920 Ergonomic Wireless Mouse (Product number
  6H1A4AA; UPC number (ABA) 197029640277) and the eBay US product
  catalog (item 156358903729, MPN 6H1A4AA#ABA, UPC 197029640277);
  Amazon was not used as corroboration (S3225QS precedent:
  datasheet + eBay). Not copied: 196548939633 (the ABB/EMEA code);
  the HP 925 Ergonomic Vertical Mouse (different, business model)
  and the HP 710 Rechargeable Silent Mouse ($79.99) — different
  mice. Quotes (2): HP direct $68.99 (sale vs $114.99 list,
  InStock, page JSON-LD read; wireless 2.4 GHz + Bluetooth 5.3,
  detachable wrist rest, 6 buttons, up to 4000 dpi); Best Buy
  $68.99 (sale vs $114.99 list, SKU 12714516, feed row —
  suspected; the feed title says 'Wired' but the HP US page specs
  the mouse as wireless, so the title is a feed mislabel, not a
  second variant; not page-verified). Excluded: the tecisoft
  $298.65 and tech-ment $167.99 rows (unconfirmed resellers, above
  list); the HP 925 rows (different model).
- HP OMEN 27q G2 QHD 180Hz Gaming Monitor, Black (AV4H6AA#ABA) —
  identifiers PENDING: MPN confirmed (HP US page + Harvey Norman
  UK + DirectDial agree), but no US UPC surfaced — the HP
  datasheet lists UPC codes for #A2N (198701661184), #ABB
  (198701661221), #ABT, #ABU, #ABV, #ACQ, #UUG and #UUZ, and the
  (ABA) slot is absent, so identifiers stay empty per the
  DualSense precedent. Not copied: 198701661221 (the ABB regional
  code); the OMEN 27qs G2 280 Hz (AW3V0AA#ABA, different, faster
  panel) and the OMEN 27q (780H4AA, older 165 Hz model) —
  different monitors. Quotes (2): HP direct $203.99 (sale vs
  $339.99 list, InStock, page JSON-LD read); Newegg $218.99
  (AV4H6AA in the title, feed row — suspected; not
  page-verified). Excluded: the Micro Center $169.99 shop.app row
  (new_item_marketplace, DECISIONS 021); the Newegg $553.98 row
  (same model name at 2.7x the direct price, unconfirmed listing).
- HyperX Alloy Rise 75 Mechanical Gaming Keyboard, Black, US
  Layout, HyperX Red - Linear, wired (7G7A4AA#ABA) — identifiers
  PENDING: MPN confirmed (HP US page + HyperX feed spec row
  agree), but the US UPC is single-source only — the HP leaflet
  (mirrored on expert.de) lists HP GTIN (ABA) 197192334096, and no
  second independent non-Amazon source states it, so identifiers
  stay empty per the strict two-source rule. Not copied: the Alloy
  Rise 75 Wireless (different, wireless model, up to 1500-hour
  battery) and the Alloy Rise Top Plates (accessory, $49.99) —
  different products. Quotes (4): HyperX direct $84.99 (InStock,
  hyperx.com US store page read — the only variant listed); Best
  Buy $84.99 (sale vs $169.99 list, SKU 11006248, feed row —
  suspected; not page-verified); Target $84.99 (sale vs $169.99
  list, feed row — suspected; not page-verified); Newegg $169.99
  (feed row — the list price; not page-verified). Excluded: the
  Newegg $281.98 row (second, unconfirmed listing).
- Not added from the sweep (held for later batches, all current
  US models, no defect): OMEN 27k $370.32; OMEN OLED 27q $399.99;
  Series 3 Pro 327pf $194.00; E24mv G4 $210.40; E27k G5 $504.00;
  Cloud III S Wireless $179.99; CloudX Flight 2 $139.99; CloudX
  $59.99; Pulsefire Haste 2 Pro $119.99; Pulsefire Haste 2 Wireless
  $89.99; QuadCast 2 S $149.99. Not added (no clean pin): all OMEN
  / Victus / HP laptops and OMEN 35L desktops — configurable with
  no retailer-pinned base configuration (DECISIONS 015); all
  HyperX bundles — bundles, not standalone lines.
- Eval on the new snapshot: 130 models, 72 verified identifiers,
  5 with quotes, 13 total quotes, 0 identifier-matched, 13
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 125 → 130 / 71 → 72 for the continuous
  expansion; the pending set gains the 4 new pending keys:
  hp-omen-27s-black, hyperx-cloud-iii-black-red,
  hp-omen-27q-g2-black, hyperx-alloy-rise-75-black).

## 061 — 2026-11-06: Expansion batch 22 — 130 → 135 models (DECISIONS 044)

- HP official US store verification (hp.com/us-en + hyperx.com US,
  read-only, 2026-11-06 ~19:49–19:51 UTC / 11:49–11:51 PT): all
  five HP US product pages return full JSON-LD offers, InStock, at
  the sweep prices — OMEN 27k $370.32 (780G8AA#ABA), OMEN OLED 27q
  $399.99 (CH0R2AA#ABA), Cloud III S Wireless Black-Red $179.99
  (Product # A59Z0AA), Pulsefire Haste 2 Pro $119.99 (Product #
  A1KY5AA, Slate grey), QuadCast 2 S $149.99 (Product # 9A273AA,
  Black). The QuadCast 2 S $149.99 was confirmed on the fresh page
  read: a 5-day-old search-index read showing $159.99 was stale
  and was not used. HP laptops and desktops are configurable: no
  laptop or desktop was added (DECISIONS 015). Feed shelf observed
  across the 5 Meta Catalog runs (100 rows): 27k HP brand_direct
  absent / Newegg $609.99; OLED 27q HyperX $399.99 brand_direct
  (hyperx.com) / HP $399.99 sale brand_direct (hp.com) / Best Buy
  $379.99 (SKU 6669985) / mydex.shop $822.69 (other); Cloud III S
  Wireless HP $179.99 brand_direct for every colorway (Black-Red,
  Black, White, Lavender, Black/Blue, White/Pink) / Target $129.99
  (color unstated) / Best Buy $179.99 Black/Sci-Fi Blue Special
  Edition (SKU 6687475, different colorway) / Newegg $170.99
  Black-Red / Ayoub $145 Black/Red A59Z0AA / buyitsolutions
  $165.23 Black/Red / Newegg $197.99 / $250.69 / $216; Haste 2 Pro
  HyperX $119.99 brand_direct (hyperx.com, Slate Gray) / HP
  $119.99 brand_direct (hp.com) / Best Buy $99.99 (SKU 6626287) /
  Newegg $201.98; QuadCast 2 S HyperX $149.99 brand_direct
  (hyperx.com) / Newegg $223.99 (Barrow) / $329.98 / Mister Spex
  $180 drop_shipper.
- Membership check (against the 130-model set, by name, MPN and
  UPC): grep of price_agent/catalog.py finds zero matches for
  omen-27k, omen-oled-27q, cloud-iii-s, pulsefire-haste-2-pro,
  quadcast-2-s, 780G8AA, CH0R2AA or 9A273AA. OMEN 27k
  (780G8AA#ABA): no match — distinct from the OMEN 27s (FHD 240
  Hz), the OMEN 27q G2 (QHD 180 Hz) and the OMEN 27q (older 165
  Hz, not in the set). OMEN OLED 27q (CH0R2AA#ABA): no match —
  the set had no OLED monitor at all. Cloud III S Wireless
  (A59Z0AA / UPC 198415435569): no match — distinct from the
  Cloud III wired (727A9AA, already in the set) and from the
  Cloud III Wireless (older model, not in the set). Pulsefire
  Haste 2 Pro (A1KY5AA): no match — the set had no HyperX mouse
  at all. QuadCast 2 S (9A273AA): no match — the set had no
  microphone at all (new category, decided in DECISIONS 044).
- Per-model record (all 5 added; identifiers, quotes, pending):
- HP OMEN 27k UHD 144Hz Gaming Monitor, Black (780G8AA#ABA) —
  identifiers PENDING: MPN confirmed (HP US page), but the HP
  datasheet (1WorldSync) lists UPC codes only for #ABB
  (197029615961) and #ABU (197029615992) — the (ABA) slot is
  absent, so no US UPC surfaced; identifiers stay empty per the
  DualSense precedent. Not copied: 197029615961 (ABB) and
  197029615992 (ABU); the OMEN 27qs G2 280 Hz (AW3V0AA#ABA,
  different, faster panel) and the OMEN 27q G2 (already in the
  set). Quotes (1): HP direct $370.32 (InStock, page JSON-LD
  read; 4K UHD 3840x2160 IPS 144 Hz 1ms GtG, G-SYNC compatible,
  DisplayHDR 400, KVM switch). Excluded: the Newegg $609.99 row
  (65% above the HP direct price, unconfirmed outlier,
  Distritech precedent).
- HyperX OMEN OLED 27q QHD 240Hz Gaming Monitor, Black
  (CH0R2AA#ABA) — identifiers PENDING: MPN confirmed (HP US page
  + Best Buy agree), but the UPC is conflicted — the HP datasheet
  (1WorldSync) states P/N CH0R2AA, UPC 199642944442, while Amazon
  states UPC 199642944428 for CH0R2AA#ABA, and no second
  non-Amazon source states either code, so identifiers stay empty
  per the DualSense precedent; neither code was recorded. Not
  copied: 199642944442 / 199642944428; the OMEN OLED 34
  (different, 34-inch) and the OMEN 27q G3 (different, IPS 240
  Hz). Quotes (3): HP direct $399.99 (sale vs $499.99 list,
  InStock, page JSON-LD read; QD-OLED 240 Hz 0.03ms GtG, G-SYNC,
  HyperX OLED Core Protect); HyperX direct $399.99 (feed
  brand_direct row — suspected; not page-verified); Best Buy
  $379.99 (Model CH0R2AA, SKU 6669985, feed authorized_retailer
  row — suspected; not page-verified). Excluded: the mydex.shop
  $822.69 row (seller_type other, DECISIONS 021).
- HyperX Cloud III S Wireless Gaming Headset, Black-Red (A59Z0AA)
  — identifiers VERIFIED: UPC 198415435569, agreed by the PBTech
  retailer listing (Manufacturer Part No A59Z0AA, UPC
  198415435569, Black-Red) and the trippodo spec database (EAN13
  0198415435569, the same code in GTIN-13 form, for A59Z0AA
  Black-Red); the HP datasheet for this model states the MPN
  A59Z0AA but no UPC, so it was not counted as a second source.
  Amazon was not used as corroboration. Not copied: A59YZAA
  (Black), AX6G1AA (White), DF7E9AA (Black/Blue), White/Pink —
  different colorways at the same $179.99; the Cloud III Wireless
  (different, older model, $99.99 sale) and the Cloud III wired
  (already in the set). Quotes (4): HP direct $179.99 (InStock,
  page JSON-LD read; wireless 2.4 GHz + Bluetooth 5.3 + Instant
  Pair, 53 mm angled drivers, up to 120-hour battery, DTS
  Headphone:X); Best Buy $129.99 (Model A59Z0AA, SKU 6618287,
  Red/Black, Best Buy page text read via search index 2026-11-06
  — sale price); Target $129.99 (feed row — suspected; color
  unstated, not page-verified); Newegg $170.99 Black-Red (feed
  row — suspected; not page-verified). Excluded: the Ayoub $145
  row (overseas seller, DECISIONS 021), the buyitsolutions
  $165.23 row (unconfirmed reseller), the Newegg $197.99 /
  $250.69 / $216 rows (above list, unconfirmed), the Best Buy
  $179.99 Black/Sci-Fi Blue Special Edition row (different
  colorway) and all HyperX bundle rows.
- HyperX Pulsefire Haste 2 Pro 4K Wireless Gaming Mouse, Slate
  Grey (A1KY5AA) — identifiers PENDING: MPN confirmed (HP US page
  + HyperX feed agree), but the UPC is single-source only —
  Currys Business UK lists EAN 198122802432 for A1KY5AA, and no
  second independent source states it (no UPC surfaced in the HP
  datasheet copies read), so identifiers stay empty per the strict
  two-source rule. Not copied: 198122802432 (single-source); the
  Pulsefire Haste 2 S Navy/Silver (different, S model), the
  Pulsefire Haste 2 Wireless Black (6N0B0AA, different, $89.99)
  and the Pulsefire Saga Pro (different mouse). Quotes (3): HP
  direct $119.99 (InStock, page JSON-LD read; true 4 kHz wireless
  polling, 61 g, HyperX 26K sensor, up to 90-hour battery,
  Instant Pair); HyperX direct $119.99 (feed brand_direct row —
  suspected; not page-verified); Best Buy $99.99 (Slate Grey, SKU
  6626287, feed row — suspected; not page-verified). Excluded: the
  Newegg $201.98 row (above list, unconfirmed) and all HyperX
  bundle rows.
- HyperX QuadCast 2 S USB Microphone, Black (9A273AA) —
  identifiers PENDING: MPN confirmed (HP US page), but the UPC is
  single-non-Amazon-source only — the HP user manual (via
  manuals.plus) states UPC 197961186741 for 9A273AA, and every
  other source stating it is Amazon (.com/.ca/.in/.ie), which
  never corroborates, so identifiers stay empty per the strict
  two-source rule. Not copied: 197961186741 (manual-only); the
  QuadCast 2 Black (872V1AA, different, $149.99, red-only
  lighting, 24-bit/96 kHz) and QuadCast 2 Frost ($129.99) —
  different mics; the QuadCast S (4P5P7AA, older model). Quotes
  (2): HP direct $149.99 (sale vs $199.99 list, InStock, page
  JSON-LD read; 32-bit/192 kHz, 100+ aRGB LEDs, tap-to-mute,
  multifunction knob); HyperX direct $149.99 (feed brand_direct
  row — suspected; not page-verified). Excluded: the Newegg
  $223.99 / $329.98 rows (above list, unconfirmed; the $223.99
  row carries third-party brand Barrow) and the Mister Spex $180
  drop_shipper row (DECISIONS 021), plus all HyperX bundle rows.
- Not added from the sweep (held for later batches, all current
  US models, no defect): Series 3 Pro 327pf $194.00; E24mv G4
  $210.40; E27k G5 $504.00; CloudX Flight 2 $139.99; CloudX
  $59.99; Pulsefire Haste 2 Wireless $89.99. Not added (no clean
  pin): all OMEN / Victus / HP laptops and OMEN 35L desktops —
  configurable with no retailer-pinned base configuration
  (DECISIONS 015); all HyperX bundles — bundles, not standalone
  lines.
- Eval on the new snapshot: 135 models, 73 verified identifiers,
  5 with quotes, 13 total quotes, 0 identifier-matched, 13
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 130 → 135 / 72 → 73 for the continuous
  expansion; the pending set gains the 4 new pending keys:
  hp-omen-27k-black, hyperx-omen-oled-27q-black,
  hyperx-pulsefire-haste-2-pro-slate-grey,
  hyperx-quadcast-2-s-black).

## 062 — 2026-11-06: Expansion batch 23 — 135 → 140 models (DECISIONS 045)

- ASUS official US store verification (asus.com/us + rog.asus.com
  US store, eshop.asus.com/us, read-only, 2026-11-06 ~19:54–20:00
  UTC / 11:54–12:00 PT): PG27UCWM $1,199.00 (ROG US monitors
  category page, Temporarily out of stock); Delta II Black $185.99
  InStock (ASUS eShop USA page read fresh, Product Name A701 ROG
  DELTA II/BLK, Part Number 90YH03W0-BHAA03, Color Black);
  Gladius IV Ace $169.99 (ROG US product page JSON-LD, OutOfStock
  at direct; Best Buy page read fresh, InStock, Model P729 ROG
  GLADIUS IV ACE/BLK, SKU 6690126, Sold by Best Buy); Azoth 96 HE
  $359.99 InStock (ASUS eShop USA Open Graph read, Product Name
  M901 ROG AZOTH 96 HE/BLK/HFXV2/CA/PBT, Part Number
  90MP040H-BKAA20); Cetra Open Wireless $229.99 (ASUS eShop USA
  page read via search index, Product Name O701 ROG CETRA OPEN
  WIRELESS/BLK, Part Number 90YH0450-BTAA00). ASUS laptops and
  desktops are configurable: no laptop or desktop was added
  (DECISIONS 015). Feed shelf observed across the 5 Meta Catalog
  runs (100 rows): PG27UCWM ROG $1,699 brand_direct (ca-en, CAD,
  non-US) / Newegg $1,199.99 authorized_retailer; Delta II ASUS
  $229.99 brand_direct (shop.asus.com/us, BHAA10 White) / ASUS
  $229.99 seller_type unstated (shop.asus.com/us, BHAA03 list) /
  ROG $177.99 brand_direct (eshop.asus.com/us, BHAA03 — stale) /
  Delta II KJP $269.99 brand_direct / Target $199.99 sale
  authorized_retailer / andromedainsights.com $219.99 brand_direct
  (unconfirmed reseller); Gladius IV Ace Best Buy $169.99
  authorized_retailer / AliExpress $271.08 (overseas marketplace);
  Azoth 96 HE ROG $359.99 brand_direct (rog.asus.com spec page) /
  ROG $359.99 brand_direct (eshop.asus.com/us) / ASUS $359.99
  brand_direct (shop.asus.com/us) / Target $339.99 sale ($399.99
  reg) authorized_retailer / Newegg $359.99 authorized_retailer /
  ROG $305.99 sale brand_direct (rog.asus.com helpdesk page —
  stale/unclear) / Azoth 96 HE Lite $359.99 brand_direct
  (different model); Cetra Open Wireless ASUS $229.99 brand_direct
  (shop.asus.com/us) / Best Buy $229.99 authorized_retailer /
  Walmart $229.99 authorized_retailer (sold-by unconfirmed) /
  Newegg WUQ $390.99 authorized_retailer / 961souq $325 sale ($399
  list) authorized_retailer (overseas) / ROG $339.99 brand_direct
  (ca-en, CAD, non-US).
- Membership check (against the 135-model set, by name, MPN and
  UPC): grep of price_agent/catalog.py finds zero matches for
  asus, rog-swift-oled-pg27ucwm, rog-delta-ii, rog-gladius-iv-ace,
  rog-azoth-96-he, rog-cetra-open-wireless, 90YH03W0, 90MP040H,
  90YH0450, 199291335226, 199291008571, 199291232747 or
  199291232754 — the set had no ASUS brand entry at all (the only
  prior 'ASUS' strings are none; the sweep 059 check at 125 models
  found the same). PG27UCWM: no match — distinct from the
  PG27UCDM (QD-OLED, $1,099) and PG32UCWM (32-inch, $1,399).
  Delta II (90YH03W0-BHAA03): no match — the set had no ASUS
  headset at all. Gladius IV Ace (P729 ROG GLADIUS IV ACE/BLK):
  no match — the set had no ASUS mouse at all. Azoth 96 HE
  (90MP040H-BKAA20): no match — the set had no ASUS keyboard at
  all. Cetra Open Wireless (90YH0450-BTAA00): no match — the set
  had no ASUS earbuds at all.
- Per-model record (all 5 added; identifiers, quotes, pending):
- ASUS ROG Swift OLED PG27UCWM 27-inch 4K 240Hz Gaming Monitor,
  Black (single colorway) — identifiers PENDING: UPC 199291335226
  is B&H-only (page read fresh 2026-11-06 states it); Scan UK
  lists GTIN 4711636505857 for the EU listing, a different
  regional code, not a corroboration; no ASUS part number (90LM…)
  surfaced for the US listing, so identifiers stay empty per the
  strict two-source rule. Not copied: 199291335226
  (single-source); 4711636505857 (EU GTIN); the PG32UCWM 32-inch
  ($1,399) and PG27UCDM ($1,099, QD-OLED) — different monitors.
  Quotes (3): ASUS $1,199.00 (ROG US category page read,
  Temporarily out of stock — price verified; 26.5-inch Tandem RGB
  OLED, dual mode 4K@240Hz / FHD@480Hz, TrueBlack Glossy, DP
  2.1a, USB-C 90W); B&H $1,199.00 (page read fresh, "New Item -
  Coming Soon", OutOfStock); Newegg $1,199.99 (feed
  authorized_retailer row — suspected; stock not confirmed on the
  page read). Excluded: the rog.asus.com/ca-en $1,699 row (CAD,
  non-US, DECISIONS 021). Stock caveat: temporarily out of stock
  at ROG US and coming soon at B&H — added per the PS5 Pro
  precedent (batch 3); re-check stock next refresh.
- ASUS ROG Delta II Wireless Gaming Headset, Black
  (90YH03W0-BHAA03) — identifiers PENDING: MPN confirmed (ASUS
  eShop USA page), but no US UPC surfaced — the EAN 4711387604847
  stated by Overclockers UK and itworkup.co.za is for
  90YH03W0-BHUA00 (the UK Black part number), not the US BHAA03,
  so it was not carried across regions per the strict two-source
  rule. Not copied: 4711387604847 (UK part); 90YH03W0-BHAA10
  (Moonlight White, CA $339.99 CAD — different colorway);
  90YH04C0-BHAA10 (Delta II KJP limited edition, $269.99 —
  different headset). Quotes (3): ASUS eShop $185.99 (InStock,
  page read fresh; tri-mode BT/2.4GHz/3.5mm, 50 mm
  titanium-plated drivers, up to 110-hour battery, 318 g); Target
  $199.99 Black (feed authorized_retailer row — suspected; not
  page-verified); ASUS shop $229.99 list (feed row for the same
  part, seller_type unstated — suspected; list price). Excluded:
  the eShop feed row at $177.99 (stale — the fresh page read shows
  $185.99) and the pricehistory.app $177.99 figure
  (Amazon-derived; Amazon never corroborates), plus the
  andromedainsights.com $219.99 row (unconfirmed reseller).
- ASUS ROG Gladius IV Ace Wireless Gaming Mouse, Black (P729 ROG
  GLADIUS IV ACE/BLK) — identifiers PENDING: no MPN in 90MP…
  form and no UPC surfaced for this model in any source read
  (launched 2026-10-30; B&H carries no listing yet), so
  identifiers stay empty per the strict two-source rule. Not
  copied: nothing — no candidate code surfaced. Not the Gladius
  III (different mouse) or the Harpe II Ace ($150.99, different
  mouse). Quotes (2): Best Buy $169.99 (InStock, page read fresh,
  Model P729 ROG GLADIUS IV ACE/BLK, SKU 6690126, Sold by Best
  Buy; 56 g, AimPoint Pro 65K sensor, SpeedNova 8K Gen II,
  customizable weight); ASUS $169.99 (ROG US product page JSON-LD
  read — price verified, Availability OutOfStock at direct).
  Excluded: the AliExpress $271.08 row (overseas marketplace,
  DECISIONS 021).
- ASUS ROG Azoth 96 HE Wireless Gaming Keyboard, Black
  (90MP040H-BKAA20) — identifiers PENDING: MPN confirmed (ASUS
  eShop USA page), but the only UPC surfaced, 199291008571, is
  stated on Amazon only (for M901 ROG AZOTH 96 HE/BLK/HFXV2/
  CA/ABS — note ABS keycaps vs the eShop's PBT), and Amazon never
  corroborates, so identifiers stay empty per the strict
  two-source rule. Not copied: 199291008571 (Amazon-only);
  4711636009126 (EAN for 90MP040H-BKDA20, the QWERTZ EU part) and
  4711636009201 (barcode for 90MP040H-BKUA20, the UK part) —
  different regional parts. Not the Azoth 96 HE Lite
  (90MP048H-BKAA00, different keyboard, also $359.99) or the
  Azoth Extreme ($499.99). Quotes (3): ASUS eShop $359.99
  (InStock, Open Graph read; HFX V2 magnetic switches, SpeedNova
  8K, OLED touchscreen); Newegg $359.99 (feed authorized_retailer
  row — suspected; not page-verified); Target $339.99 sale (feed
  authorized_retailer row — suspected; Target's $399.99 reg
  conflicts with the ASUS $359.99 list). Excluded: the $305.99
  sale row on a rog.asus.com helpdesk page (stale/unclear). The
  sweep's $308.99 is superseded — the fresh eShop read, the feed
  and Newegg all agree on $359.99.
- ASUS ROG Cetra Open Wireless Gaming Earbuds, Black
  (90YH0450-BTAA00) — identifiers PENDING: the UPC is a genuine
  conflict, not a verification — PBTech (NZ retailer) and the
  LittleBit datasheet agree on UPC 199291232747 for
  90YH0450-BTUA00 (the non-US part), while Amazon states UPC
  199291232754 for the same US model name (O701 ROG CETRA OPEN
  WIRELESS/BLK); neither code was recorded, per the DualSense
  precedent and the strict two-source rule (no US source ties a
  UPC to the US part BTAA00). Not copied: 199291232747 (non-US
  part) or 199291232754 (Amazon-only, conflicting);
  90YH0450-BTUA00 (non-US part). Not the Cetra True Wireless
  SpeedNova (different earbuds, $199.99). Quotes (2): ASUS eShop
  $229.99 (page read via search index; dual-mode BT + SpeedNova
  2.4 GHz, 14.2 mm DLC drivers, open-ear, 16-hour battery +
  48-hour case); Best Buy $229.99 (feed authorized_retailer row +
  page text read via search index, Model O701 ROG CETRA OPEN
  WRLS/BLK, SKU 6668329, Sold by Best Buy — suspected; not freshly
  page-verified). Excluded: the Walmart $229.99 feed row (sold-by
  unconfirmed — marketplace risk, DECISIONS 021), the Newegg WUQ
  $390.99 row (third-party brand, above list), the 961souq
  $325/$399 rows (overseas), the rog.asus.com/ca-en $339.99 CAD
  row (non-US).
- Not added from the sweep (held for later batches, all current
  US models, no defect): PG32UCWM $1,399; PG27AQDPR $899 sale;
  PG32UCDM Gen3 $1,299; PG27UCDM $1,099; XG32UQDS $749; PG34WCDN
  $1,299; Delta $149.99; Pelta Core $119.99; Kithara $259.99 sale;
  Spatha X 65K $179.99; Harpe Mini Core $69.99; Azoth 96 HE Lite
  $359.99; Strix Morph 96 $115.99 sale; Strix Scope II 96 RX
  $132.99 sale; Falchion Ace 75 HE from $177.99. Not added (no
  clean pin): all ASUS laptops and desktops — configurable with no
  retailer-pinned base configuration (DECISIONS 015); Azoth
  Extreme Edition 20 keyboard ($599.99) and Harpe II Extreme
  Edition 20 mouse ($259.99) — limited 20th-anniversary editions,
  not mainstream lines; Gjallar soundbar, mouse pads, Zenfone
  phones, routers — no set category / out of scope (BUILD_LOG
  059).
- Eval on the new snapshot: 140 models, 73 verified identifiers,
  5 with quotes, 13 total quotes, 0 identifier-matched, 13
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 135 → 140, verified stays 73, for the continuous
  expansion; the pending set gains the 5 new pending keys:
  asus-rog-swift-oled-pg27ucwm-black, asus-rog-delta-ii-black,
  asus-rog-gladius-iv-ace-black, asus-rog-azoth-96-he-black,
  asus-rog-cetra-open-wireless-black).

## 063 — 2026-11-06: Expansion batch 24 — 140 → 145 models (DECISIONS 046)

- Membership check (against the 140-model set in
  price_agent/catalog.py, by name, MPN and UPC — recorded here so
  a later session can repeat it): S2725QS — NO MATCH (the set has
  dell-32-plus-4k-monitor-s3225qs, a different 32-inch monitor);
  U3225QE — NO MATCH (the set has no UltraSharp); AW3225DM — NO
  MATCH (the set has alienware-27-qd-oled-aw2726dm, a different
  27-inch QD-OLED monitor, and no 32-inch AW3225DM); AW920K — NO
  MATCH (the set has alienware-pro-wireless-gaming-keyboard-dark-
  side-of-the-moon, a different keyboard; AW920K is named there
  only as a not-copied different model); WB726 — NO MATCH (the set
  has no webcam). None of the 5 duplicates an existing model on
  name, MPN or UPC. Dell/Alienware keys already in the set:
  dell-32-plus-4k-monitor-s3225qs, alienware-27-qd-oled-aw2726dm,
  alienware-pro-wireless-gaming-mouse-dark-side-of-the-moon,
  alienware-pro-wireless-gaming-keyboard-dark-side-of-the-moon,
  alienware-pro-wireless-gaming-headset-dark-side-of-the-moon.
- Dell 27 Plus 4K Monitor S2725QS, Ash White (T4CNF) —
  identifiers PENDING: MPN confirmed (Dell US + CA pages agree;
  AU 8PRJ8 / IE-UK V424D / SG-MY 2M7P9 are regional and were not
  used), but the only UPC surfaced, 884116485117, is stated on
  Amazon only (with a second code, 738060953201, on the same
  listing), and the Icecat EAN 5397184962350 is a single-source EU
  datasheet, so identifiers stay empty per the strict two-source
  rule. Not copied: 884116485117 / 738060953201 (Amazon-only);
  5397184962350 (Icecat-only EAN); 8PRJ8 / V424D / 2M7P9
  (regional MPNs). Quotes (3): Dell $299.99 (feed brand_direct row
  — suspected; Dell US page text carries no price); Newegg $299.99
  (feed authorized_retailer row — suspected; page read fresh
  2026-11-06 confirms the exact model, no price in text);
  ThinkEdu $284.99 (feed authorized_retailer row — suspected).
  Excluded: the Nexoltic $385.18 row (unconfirmed reseller), the
  K-Rauta rows (Estonia, non-US), and every $279.99 figure traced
  this round (Amazon prices — BetterBuyBase, Gadget Review — the
  sweep's ~$279.99 is superseded for Dell direct). Dell US page
  read fresh 2026-11-06 20:00 UTC: MPN T4CNF, Ash White, 27-inch
  4K IPS 120 Hz, FreeSync Premium, 99% sRGB, dual 5 W speakers,
  4.7 stars (616 reviews).
- Dell UltraSharp 32 4K Thunderbolt Hub Monitor U3225QE, Silver
  (3PVPJ) — identifiers VERIFIED: UPC 884116484561 (B&H Photo
  spec page, MFR # U3225QE + CompTechDirect Icecat-derived listing,
  EAN/UPC code 5397184923399 0884116484561, MFG # DELL-U3225QE
  agree); MPN 3PVPJ (Dell US page, read fresh 2026-11-06 20:01
  UTC). Not copied: the UK MPN FPG3K (regional). Quotes (5): Dell
  $1,029.99 (feed brand_direct row — suspected; Dell US page text
  carries no price); Target $799.99 (InStock, search-index JSON-LD
  read 2026-11-06, listing A-1004931139); Adorama $799.00
  (InStock, search-index JSON-LD read 2026-11-06); CDW $949.99
  (feed authorized_retailer row — suspected); Newegg $1,099.99
  (feed authorized_retailer row — suspected; the list price).
  Excluded: the Target 2-pack bundle $1,699 (different product),
  the second Target feed row $1,028.97 (listing A-1006296976,
  conflicts with the $799.99 Target listing), the BuyItSolutions
  $1,034.83 row (unconfirmed reseller), the K-Rauta rows (non-US).
  The sweep's $1,099.99 is the list price, not the current Dell
  price. Dell US page: 31.5-inch 4K IPS Black 120 Hz, Thunderbolt
  4 hub, 140 W PD, 2.5GbE, KVM, Delta E <1.5.
- Alienware 32 Curved Gaming Monitor AW3225DM, Dark Blue (VX89X)
  — identifiers PENDING: MPN confirmed (Dell US + CA pages agree),
  but no US UPC surfaced — the only code found is EAN
  5397184962725 on a single Icecat datasheet (mirrored by
  startech24, e-misija and manua.ls, all the same source family),
  so identifiers stay empty per the strict two-source rule. Not
  copied: 5397184962725 (Icecat-only EAN). Quotes (3): Dell
  $249.99 (sale vs $299.99 list; Windows Central 2026-10-26 +
  topsave.org 2026-10-23 + BUILD_LOG 058 Dell US sweep
  2026-11-06); Best Buy $319.99 (InStock, page read fresh
  2026-11-06, Model AW3225DM, SKU 6619487, Sold by Best Buy, 4.8
  stars, 954 reviews); Newegg $370.30 (feed authorized_retailer
  row — suspected; above list). Excluded: the Sigmatiendas $507.99
  sale row (overseas). Dell US page read fresh 2026-11-06 20:01
  UTC: MPN VX89X, Dark Blue (Best Buy calls the same colorway
  Interstellar Indigo), 31.5-inch QHD VA 180 Hz 1500R curved,
  FreeSync Premium, DisplayHDR 400, 4.4/5 (139 ratings).
- Alienware Tri-Mode Wireless Gaming Keyboard AW920K, Dark Side of
  the Moon (6R87M) — identifiers PENDING: no Dark Side UPC
  surfaced — the only UPC found, 884116448686, is stated on a
  single Icecat datasheet for AW920K-W-WW (the Lunar Light / White
  colorway) and was not carried across colorways, so identifiers
  stay empty per the strict two-source rule. Not copied:
  884116448686 (Lunar Light only, Icecat-only); EAN 5397184790397
  (same Icecat datasheet, Lunar Light). Quotes (1): Dell $159.99
  (feed brand_direct row for the 6R87M Dark Side slug — suspected;
  Dell US page text carries no price). Excluded: the Fnac $218.02
  row (overseas marketplace) and the second Dell feed row $149.99
  sale vs $159.99 list on the generic 520-bbcg accessories path
  (colorway unstated — not attributed to the pinned variant).
  Dell US page (6R87M slug) read fresh 2026-11-06 20:01 UTC:
  Dark Side of the Moon confirmed by the slug and /dsotm/ image
  paths, CHERRY MX Red, tri-mode, magnetic snap-on charging,
  4.3/5 (326 ratings, 230 reviews).
- Dell Pro 7 Webcam 4K WB726, Black (G4MYM) — identifiers
  PENDING: MPN confirmed (Dell US page), but no US UPC surfaced —
  the only code found is EAN 5397321028925 on Icecat datasheets
  for WB726-EMEA (the EMEA part, mirrored by several EU resellers,
  one source family), so identifiers stay empty per the strict
  two-source rule. Not copied: 5397321028925 (Icecat-only EAN,
  EMEA part). Quotes (1): Dell $199.99 (Dell US webcams category
  pages, Offer ID V813W, Add to Cart, crawled 2026-11-06; product
  page search-index read agrees at $199.99, Manufacturer part
  V813W). Excluded: the silarius $209.99 sale row (mislabeled
  brand_direct in the feed — unconfirmed reseller, not Dell) and
  the shop.app $174 marketplace row (DECISIONS 021). The $189.99
  figure in Lifewire's September 10 report is stale. Single
  colorway (Black). New category "webcams" (precedent:
  "microphones", DECISIONS 044).
- Eval on the new snapshot: 145 models, 74 verified identifiers,
  5 with quotes, 13 total quotes, 0 identifier-matched, 13
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 140 → 145, verified 73 → 74, for the continuous
  expansion; the pending set gains the 4 new pending keys:
  dell-27-plus-4k-monitor-s2725qs,
  alienware-32-curved-gaming-monitor-aw3225dm,
  alienware-tri-mode-wireless-gaming-keyboard-aw920k-dark-side-of-the-moon,
  dell-pro-7-webcam-4k-wb726).

## 063 — 2026-11-06: Daily price refresh (PM) — 100 models, supersedes the morning 28-model snapshot

- Trigger: scheduled daily refresh (`price-compare-daily-refresh`,
  10:52 PT). Second run of the day. Scope frozen at 100 models: 92
  swept at run start + 8 more swept after the expansion update to
  100 (Sony MDR-7506, Pulse headset white, LinkBuds Clip black,
  N64 controller, Studio Display XDR standard tilt/height, MDR-M1,
  MDR-MV1, Keychron B39 Deep Black). Expansion batches 16+ (Anker,
  JBL, Razer, Corsair, Dell, HP, Lenovo, ASUS — live EVAL_SET now
  140, batch 24 landing) have their own batch snapshots and join the
  consolidated daily snapshot tomorrow; this run lists candidates
  only and adds no model. All 100 models re-queried through the Meta
  Catalog CLI (`catalog-search --intent targeted --currency USD
  --retries 2`), 1,987 raw listings, raw files
  `data/meta_catalog_raw_*_2026-11-06.json` (gitignored). One new
  dated snapshot, `data/eval_snapshots_2026-11-06.json`, OVERWRITES
  the morning 28-model file (same date, larger scope — stated in
  the snapshot meta); no old dated snapshot overwritten, no catalog
  or DECISIONS change, no new models, no Amazon touch, no Kindle
  pin change.
- Result: 192 quotes across 82 of 100 models. Eval (live set is
  140, so the 40 batch-16+ models show 0 quotes — expected):
  82 with snapshot quotes, 192 total quotes, 0 identifier-matched,
  192 suspected — the catalog source gives no UPC, so every quote
  stays in the suspected table; that is the rule working, not a bug.
  Tests: 19 passed (`pytest tests/ -q`). Note: pytest briefly
  failed mid-run on a transient syntax error in the coordinator's
  uncommitted batch-24 edit to `catalog.py` (a mis-escaped note
  string); the coordinator fixed it before this commit and the
  suite passes on the committed tree. This refresh did not touch
  `catalog.py` or `tests/`.
- Price moves (same-merchant, >$5) and their verification:
  - CONFIRMED: Keychron Q1 Keychron $89.99 -> $69.99 — keychron.com
    product page shows "Sale $69.99 $169.99", JSON-LD $69.99.
  - UNVERIFIED: WH-CH720N BJ's $179.99 -> $99.99 — the BJ's page
    shows "Member Only Price — Sign in to see price" (no sign-in
    attempted); the item is in stock at BJ's. The $99.99 feed row
    stays in the snapshot, flagged unverified; Sony direct $89.99
    is the model's cheapest quote either way.
  - REJECTED (feed row contradicted by the merchant's own page,
    added to KNOWN_BAD): Kindle Best Buy $229.99 (bestbuy.com
    JSON-LD $199.99 InStock; $229.99 is the top of the
    marketplace-seller range on that page — carried forward as
    $199.99, browser-verified); PS5 Digital Best Buy $729 (page:
    "Sold & shipped by RYTEK", marketplace; Best Buy own listing
    out of stock); Quest 3S Best Buy $422.82 (page: "Sold &
    shipped by EZ Tech", marketplace); Xbox controller Best Buy
    $89.25 (live-browser check: "Sold & shipped by IPC-STORE",
    marketplace; price itself matches the feed); MX Vertical Dell
    $89.99 (dell.com shows $119.99 — carried) and Logitech $84.99
    (logitech.com shows $99.99, sale from $119.99 — the feed also
    returned a correct $99.99 Logitech row, so no duplicate was
    carried). Samsung Buds4 $135 (shop.samsung.com/latin/pa/ —
    Panama shop; excluded by a new URL-path non-US check; US price
    $179.99 at Best Buy/NFM/Samsung US).
  - Trivial (<$5, not rechecked): Switch 2 ShopMyExchange $499.99
    -> $499.00; DualSense Edge Abt $199.99 -> $199.00; WH-1000XM4C
    Best Buy $299.99 -> $298.00.
- Carried quotes (CARRIED_QUOTES, browser-verified, used only where
  the feed has no surviving row for that merchant): M6 Pro Apple
  $1,999 / Best Buy $1,999 (launch-day check, AM); Kindle Best Buy
  $199.99 (PM); MX Vertical Dell $119.99 (PM). Logitech MX Vertical
  $99.99 was NOT carried — the feed returned a correct $99.99 row.
- GONE characterization: 164 rows GONE vs the prior baseline
  (morning + batch 1–15 snapshots). Most are feed churn — the feed
  returns a different sample each round (e.g. all prior MDR-7506,
  MDR-MV1/M1, Buds3 FE quotes absent). A minority are rule-driven:
  host-blocked (Newegg, bkstr campus subdomains), variant-filtered
  (keyboard switch/layout rows, Anker 200W/bundle, Joy-Con single),
  or price-band drops (scalpers, games, accessories). No model was
  removed from the catalog.
- Zero-quote models (18) — feed gaps, not delistings (each checked
  against its raw rows): Anker Prime 100W (only a 200W row, a
  charger+cable bundle, and a Panama seller); iMac M6 (only a
  12-core NFM row; pinned is 10-core); iPad A16 / Air 11 / Air 13
  / mini / Pro 11 / Pro 13 (Apple rows are other configs — MPN
  check); MacBook Air 13/15 M5 (Apple rows are other part numbers);
  MacBook Neo (no Apple feed rows; listed on apple.com at $699
  after the 2026-06-25 increase); Mac Studio (Apple $5,499 row is
  a higher config; Abt $2,799 is 1TB vs pinned 512GB); Bose QC
  Earbuds (Bose direct rows carry no color); Keychron K8 HE / K8
  hot-swappable (Keychron rows carry no color/switch); N64
  controller (Nintendo row carries no color); Switch Pro Controller
  (Dell row carries no color); Pulse headset white (only Pulse
  Elite rows returned); PS5 Digital (Best Buy own listing out of
  stock; only RYTEK marketplace $729, excluded).
- Builder fixes applied in this refresh (in the refresh builder,
  not in the repo): "joy con" removed from the global exclusion
  list (the Switch console's own title names Joy-Con — restores
  Nintendo Switch Neon $339.99); "core" added as a config unit with
  a per-unit any-match rule (a title stating one of two required
  core counts is not a conflict — restores MacBook Pro 14 ProLED
  XDR NFM $2,899); MPN-in-URL check skipped for watches (the Watch
  MPN encodes only the band — restores Watch SE 3 Apple $249);
  "w" (watts) added as a config unit (rejects the Anker 200W row);
  charger+cable "and" titles rejected as bundles; Joy-Con pairs
  must name both sides in the title (rejects the single (L) $54.99
  row); keyboard switch/layout exclusions (MX Mechanical
  Mini/Clicky/Linear, G915 X Clicky/GL Blue/TKL/Core, PRO X TKL
  Rapid/Linear/Core/INT'L); duplicate magic-mouse MODEL_MATCH entry
  removed; "combo" added to traps; ankerpanama.com, fattalonline.com,
  bkstr.com (incl. campus subdomains) blocked; URL-path non-US check
  (/latin/ and non-/us/ Samsung shops); merchant canonicalization
  completed (Logitech G, Lenovo US, JustPressPlay, RC Willey,
  Electronic Express, Impulse Cameras, CDW, PlayStation Direct,
  MacExperience, MelroseMac, Walt's, HSN, Silarius, Boolchand,
  Golf+ VR, Virtuix, Quill, Antonline; also fixed the
  "electronicsexpress.com" map-key typo).
- Rotation items: (1) MX Master 4 Graphite retailer hunt — Walmart:
  BLOCKED. `browser.search` found no Walmart listing; `browser.open`
  on walmart.com/search returned a "Robot or human?" bot-check page.
  Stopped, marked unverified, no workaround. Still only Logitech
  direct $119.99. Next retailer: Target, then Costco. (Best Buy,
  B&H, Adorama already ruled out; Newegg rows are Pale Gray only.)
  (2) Brand patrol — Apple, first in rotation: 9 of 11 zero-quote
  Apple models have apple.com rows for other configs in the feed;
  iPad A16 and MacBook Neo have no Apple feed rows but are listed
  on apple.com (iPad A16 US $449; MacBook Neo Blush 256GB listed,
  US $699). No Apple model is delisted. M6 Pro $1,999 in stock
  (launch-day check) and Watch SE 3 Apple $249 confirmed.
  M6 Pro UPC check (one-off, 2026-11-07 10:00 PT) not duplicated.
- New merchants to watch (first appearance as a model's only or
  cheapest quote, not page-verified this run): Silarius (Buds3 FE
  $169.99, only quote — MPN in title matches exactly); Quill (G Pro
  X Superlight 2 DEX $214.99, only quote vs prior $159.99);
  MelroseMac (Studio Display XDR $2,899 vs $3,299 list); Golf+ VR
  (Quest 3 512GB $599.99); Smith's Food and Drug (Pulse Elite
  $149.99). Also flagged, unverified: Switch OLED White Best Buy
  $411.38 (above the $399.99 list); BuyDig CH720N $129.99 and
  Datavision XM6 $298 rows carry protection-plan suffixes (price is
  the product's own, kept).
- Kindle: pin UNCHANGED (B0CFPL6CFY). Best Buy's own page lists
  Model B0CFPJYX7P — further evidence for the pending user decision,
  no change made. Target $199.99 new; NFM $196.99 still the low.
- Switch 2: Nintendo $499.99 keeps — the earlier GONE was a dedupe
  bug (a $3.99 game row shadowed the merchant; fixed by per-row
  band filtering). Dell $449.99 stays KNOWN_BAD.

## 064 — 2026-11-06: Expansion batch 25 — 145 → 150 models (DECISIONS 047)

- Membership check (against the 145-model set in
  price_agent/catalog.py, by name, MPN and UPC — recorded here so
  a later session can repeat it): PG32UCWM — NO MATCH (the set has
  asus-rog-swift-oled-pg27ucwm-black, the 27-inch sibling — a
  different monitor; PG32UCWM appears only as a mention in that
  entry's notes); PG27AQDPR — NO MATCH (the set has no 500Hz
  monitor; PG27AQDP is a different 480Hz model and is not in the
  set either); Delta USB-C — NO MATCH (the set has
  asus-rog-delta-ii-black, the Delta II — a different headset);
  Harpe Mini Core — NO MATCH (the set has no Harpe mouse;
  asus-rog-gladius-iv-ace-black is a different mouse); Pelta —
  NO MATCH (the set has no Pelta; asus-rog-cetra-open-wireless-black
  is different earbuds). No candidate matches an existing model on
  name, MPN or UPC. The five are the ASUS held candidates from
  BUILD_LOG 059, re-priced fresh this batch.
- ROG Swift OLED PG32UCWM, Black (90LM0DN0-B019B1) —
  identifiers PENDING: UPC 199291571570 is B&H-only — no second
  independent source states it (Scan UK lists GTIN 4711636571531
  for the EU listing, a different regional code, not a
  corroboration), and MPN 90LM0DN0-B019B1 is ASUS eShop USA only,
  so identifiers stay empty per the strict two-source rule. Not
  copied: 199291571570 (single-source); 4711636571531 (EU GTIN);
  90LM0DN0-B019B2 (PG32UCDMR part). Quotes (3): ASUS $1,399.00
  (ROG US product page JSON-LD read fresh 2026-11-06 20:06 UTC,
  InStock); B&H $1,399.00 (page read fresh 2026-11-06, InStock,
  UPC 199291571570); Newegg $1,399.99 (feed authorized_retailer
  row — suspected). Excluded: the silarius $1,427.99 row
  (mislabeled brand_direct in the feed — unconfirmed reseller,
  not ASUS; same pattern as batch 24's WB726). ROG US page read
  fresh 2026-11-06 20:06 UTC: 31.5-inch 4K Tandem RGB OLED, dual
  mode 4K@240Hz / FHD@480Hz, TrueBlack Glossy, DP 2.1a, USB-C
  90W, 3-year warranty.
- ROG Swift OLED PG27AQDPR, Black — identifiers PENDING: no UPC
  and no ASUS part number (90LM...) surfaced for this model in
  any source read, so identifiers stay empty per the strict
  two-source rule. Not copied: nothing — no candidate code
  surfaced. Quotes (2): ASUS $729.00 sale vs $899.00 list (ROG
  US monitors category page, search-index read crawled
  2026-11-03, Temporarily out of stock at direct); Best Buy
  $999.99 (page read fresh 2026-11-06, InStock, Model PG27AQDPR,
  SKU 6685336, Sold by Best Buy, 27-inch QHD QD-OLED 500Hz).
  Correction vs sweep 059: the sweep's $899.00 "sale, save $170"
  misreads the category page — $899.00 is the LIST and $729.00
  is the sale (save $170.00); the feed's $599.00 ROG row is a
  category-page misassociation (that price belongs to another
  monitor on the same page — the ROG US product page carries no
  offer block on the fresh read) and was not used. Stock caveat:
  temporarily out of stock at ROG US — added per the PS5 Pro
  precedent (batch 3); Best Buy has stock. ROG US page read
  fresh 2026-11-06 20:06 UTC: 27-inch 500Hz QHD QD-OLED,
  OLED Anti-Flicker 2.0, OLED Care Pro, DisplayHDR 500 True
  Black, Neo Proximity Sensor.
- ROG Delta USB-C Gaming Headset, Black (90YH01D1-B2UA00) —
  identifiers PENDING: MPN 90YH01D1-B2UA00 confirmed (ASUS
  eShop USA page, Product Name ROG DELTA/SR/UBW/ACI, Color
  Black), but no US UPC surfaced in any source read, so
  identifiers stay empty per the strict two-source rule. Not
  copied: 90YH00Z1-B2UA00 (UK part, different regional part);
  90YH02K0-B2UA00 (Delta S, different headset). Quotes (2):
  ASUS $149.99 (ROG US product page JSON-LD + ASUS eShop USA
  page read fresh 2026-11-06, OutOfStock at direct; ESS 9218
  Quad-DAC, USB-C + USB 2.0 adapter, Aura Sync RGB, 387 g);
  Newegg $102.78 (feed authorized_retailer row — suspected;
  "ASUS ROG DELTA USB Connector Circumaural Headset", not
  page-verified). Excluded: the 961souq $203/$250 rows
  (overseas). Stock caveat: out of stock at ASUS direct — added
  per the PS5 Pro precedent (batch 3); re-check stock next
  refresh. Not the Delta II ($185.99) or Delta White Edition.
- ROG Harpe Mini Core Gaming Mouse, Black (90MP04D0-BMAA02) —
  identifiers PENDING: UPC 199291014046 is B&H-only — no second
  independent source states it — and MPN 90MP04D0-BMAA02 is ASUS
  eShop USA only (the JP part is 90MP04D0-BMUA00, also listed by
  PB Tech NZ), so identifiers stay empty per the strict
  two-source rule. Not copied: 199291014046 (single-source);
  90MP04D0-BMUA00 (JP/non-US part). Quotes (3): ASUS $44.99
  (ROG US product page JSON-LD + ASUS eShop USA read fresh
  2026-11-06, InStock; 52 g wired, 12,000 DPI, ROG Micro Switch
  II, Push-Fit sockets, Paracord, P524 ROG HARPE MINI CORE);
  B&H $29.99 (page read fresh 2026-11-06, InStock, UPC
  199291014046); Newegg $32.00 sale vs $44.99 (feed
  authorized_retailer row — suspected). Correction vs sweep 059:
  the sweep's $69.99 is the list — the current ASUS price is
  $44.99 sale (was $59.99). Excluded: the MercadoLibre $55
  marketplace row (DECISIONS 021) and the JP 8,980 yen row
  (non-US). Not the Harpe Ace Mini (wireless, $81.99-$129.99).
- ROG Pelta Gaming Headset, Black (90YH0410-BHAA00) —
  identifiers PENDING: MPN 90YH0410-BHAA00 confirmed (ASUS
  eShop USA, Product Name A501 ROG PELTA/BLK, Color Black), but
  no US UPC surfaced — the only UPC found, 199291069725, is
  stated on a single ASUS datasheet for 90YH0410-BHUA10 (the
  White non-US part, EAN 4711636069724), so identifiers stay
  empty per the strict two-source rule. Not copied: 199291069725
  (non-US White part, single datasheet); 90YH0410-BHAA10 (White,
  $104.99 — different colorway); 90YH0410-BHUA00 (non-US Black
  part). Quotes (1): ASUS $104.99 sale vs $129.99 list (ASUS
  eShop USA BHAA00 page read fresh 2026-11-06, InStock; ROG US
  product page JSON-LD agrees at $104.99; tri-mode BT/2.4GHz/
  USB-C, 50 mm titanium drivers, 309 g, up to 70-hour battery).
  The base tier is pinned Black (BHAA00); White (BHAA10, also
  $104.99) is the other colorway. Correction vs sweep 059: the
  sweep's "from $84.99" is not corroborated — no $84.99 price
  appears on any fresh read; the $114.99 feed row for BHAA00 is
  stale (fresh eShop read $104.99) and was not used. Excluded:
  the Walmart $104.99 feed row (sold-by unconfirmed —
  marketplace risk, DECISIONS 021, same as batch 23's Cetra).
  Not the Pelta Core (wired, $119.99, different headset).
- Eval on the new snapshot: 150 models, 74 verified identifiers,
  5 with quotes, 11 total quotes, 0 identifier-matched, 11
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 145 → 150, verified stays 74, for the
  continuous expansion; the pending set gains the 5 new pending
  keys: asus-rog-swift-oled-pg32ucwm-black,
  asus-rog-swift-oled-pg27aqdpr-black,
  asus-rog-delta-usb-c-black, asus-rog-harpe-mini-core-black,
  asus-rog-pelta-black).

## 065 — 2026-11-06: Expansion batch 26 — 150 → 155 models (DECISIONS 048)

- Membership check (against the 150-model set in
  price_agent/catalog.py, by name, MPN and UPC — recorded here so
  a later session can repeat it): Legion Tab Gen 3 — NO MATCH
  (the set has no Lenovo entry of any kind and no 8.8-inch gaming
  tablet; the six tablets in the set are all Apple iPads);
  Tab Plus Gen 2 — NO MATCH (the set has no Tab Plus; the
  original Tab Plus is a different, 2024 tablet and is not in the
  set either); Idea Tab Pro Gen 2 — NO MATCH (the set has no Idea
  Tab; the Idea Tab Pro Gen 1 is a different tablet and is not in
  the set); Tab One — NO MATCH (the set has no Tab One); Yoga Tab
  Plus Gen 2 — NO MATCH (the set has no Yoga Tab; the Yoga Tab
  Plus Gen 1 is a different tablet and is not in the set). No
  candidate matches an existing model on name, MPN or UPC. The
  five are the Lenovo US store sweep candidates, one per tablet
  family; the Lenovo US store was unreadable in the previous
  round and is readable this round (guide page, category page,
  and all five product pages return JSON-LD on fresh reads).
- Lenovo Legion Tab Gen 3, Eclipse Black (ZAEF0068US) —
  identifiers PENDING: no UPC surfaced for ZAEF0068US in any
  source read, so identifiers stay empty per the strict
  two-source rule. Not copied: nothing — no candidate code
  surfaced. Quotes (1): Lenovo $549.99 (US product page JSON-LD
  read fresh 2026-11-06 21:08 UTC, InStock; 8.8-inch 2.5K 165Hz,
  Snapdragon 8 Gen 3, 12GB LPDDR5X / 256GB UFS 4.0, Eclipse
  Black single colorway). Excluded: the feed's dbrand skin
  ($26.95) and m2skins ($24) rows (accessories, not the tablet);
  the Meta Catalog feed for this query carried no direct tablet
  row at all. Not the FIFA World Cup 26 Edition (ZAEF0096US,
  White, $569.99) or the Legion Tab Gen 5 ($899.99 list / $699.99
  sale). Lenovo-only in the US per Notebookcheck — no second
  retailer quote exists.
- Lenovo Tab Plus Gen 2, Celestial White (ZAHT0078US) —
  identifiers PENDING: no UPC surfaced for ZAHT0078US in any
  source read, so identifiers stay empty per the strict
  two-source rule. Not copied: nothing — no candidate code
  surfaced. Quotes (2): Lenovo $469.99 (US product page JSON-LD
  read fresh 2026-11-06 21:08 UTC, InStock; feed brand_direct
  row agrees at $469.99; 12.1-inch 2.5K 120Hz, Dimensity 7400,
  8GB LPDDR5 / 128GB UFS 3.1, JBL 9-unit Pro speakers, Celestial
  White); Newegg $299.99 (feed authorized_retailer row —
  suspected; not page-verified; 8GB/128GB, part ZAHT0078US).
  Correction vs earlier sale reports: the $269.99 sale
  (Slickdeals, Sep 29) and $289.99/$299.99 October sale prices
  are stale — the current Lenovo direct price is $469.99 on two
  agreeing reads. Excluded: the Best Buy ZAHT0043US row (8GB/
  256GB, $449.99 sale $379 — different storage config). Not the
  original Tab Plus (11.5-inch, 2024).
- Lenovo Idea Tab Pro Gen 2, Cloud Grey (ZAHD0826US) —
  identifiers PENDING: no UPC surfaced for ZAHD0826US in any
  source read, so identifiers stay empty per the strict
  two-source rule. Not copied: nothing — no candidate code
  surfaced. Quotes (2): Lenovo $399.99 sale vs $549.99 list (US
  product page JSON-LD read fresh 2026-11-06 21:08 UTC, InStock;
  feed brand_direct row agrees at price $549.99 / sale $399.99;
  13-inch 3.5K 144Hz, Snapdragon 8s Gen 4, 8GB / 128GB, Cloud
  Grey); Newegg $527.99 sale vs $549.99 (feed
  authorized_retailer row — suspected; not page-verified;
  TB390FU, 8GB/128GB, part number not stated in the feed row).
  Excluded: the Best Buy ZAHD0863US row ($529.99, with Tab Pen
  Plus — different part/bundle) and the CDW ZAHC 256GB row
  ($606.99 — different storage config). Bundle conflict
  recorded: the feed description for ZAHD0826US says "Folio
  case and Pen included" while droidgadgets (Oct 23) says this
  part ships without pen or keyboard. Not the Idea Tab Pro Gen 1
  (12.7-inch 3K, Dimensity 8300).
- Lenovo Tab One, Luna Grey (ZAF00008US) — identifiers PENDING:
  no UPC surfaced for ZAF00008US in any source read, so
  identifiers stay empty per the strict two-source rule. Not
  copied: nothing — no candidate code surfaced. Quotes (1):
  Lenovo $149.99 sale vs $199.99 est. value (US product page
  JSON-LD read fresh 2026-11-06 21:08 UTC, InStock; feed
  brand_direct row agrees at price $199.99 / sale $149.99;
  8.7-inch HD, Helio G85, 4GB / 64GB eMMC, Luna Grey). Excluded:
  the Best Buy ZAF00067US row (SKU 6621480, $99.99 Holiday Deal
  — a Best Buy-specific part number for the same 4GB/64GB Luna
  Grey specs, confirmed on a fresh Best Buy page read
  2026-11-06 21:09 UTC; the $99.99 price was NOT used) and the
  Staples ZAF00043US row ($209.99 — different part) and the
  Newegg folio-case bundle row ($149.99 — a bundle, not the bare
  tablet). Not the Tab One LTE 128GB (different
  storage/connectivity).
- Lenovo Yoga Tab Plus Gen 2, Cosmic Blue (ZAHX0159US) —
  identifiers PENDING: no UPC surfaced for ZAHX0159US in any
  source read, so identifiers stay empty per the strict
  two-source rule. Not copied: nothing — no candidate code
  surfaced. Quotes (1): Lenovo $799.99 sale vs $999.99 list (US
  product page JSON-LD read fresh 2026-11-06 21:08 UTC, InStock;
  feed brand_direct row agrees at price $999.99 / sale $799.99;
  Notebookcheck confirms the first discount, $999.99 to
  $799.99; 13-inch 4K PureSight Pro 144Hz, Snapdragon 8 Elite,
  12GB LPDDR5X / 256GB UFS 4.0, Cosmic Blue, clamshell keyboard
  + Tab Pen Pro 2 included, Android 17 with 7 OS upgrades).
  Excluded: the "Yoga Tab Plus (Gen 2) + Earbud" feed row
  ($1,069.98 — a bundle). Not the Yoga Tab Plus Gen 1
  (12.7-inch, Snapdragon 8 Gen 3, 16GB/256GB) or the Yoga Tab
  Gen 2 (11.1-inch, $729.99).
- Eval on the new snapshot: 155 models, 74 verified identifiers,
  5 with quotes, 7 total quotes, 0 identifier-matched, 7
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 150 → 155, verified stays 74, for the
  continuous expansion; the pending set gains the 5 new pending
  keys: lenovo-legion-tab-gen-3-eclipse-black,
  lenovo-tab-plus-gen-2-celestial-white,
  lenovo-idea-tab-pro-gen-2-cloud-grey, lenovo-tab-one-luna-grey,
  lenovo-yoga-tab-plus-gen-2-cosmic-blue).

## 066 — 2026-11-06: Expansion batch 27 — 155 → 160 models (DECISIONS 049)

- Membership check (against the 155-model set in
  price_agent/catalog.py, by name, MPN and UPC — recorded here so
  a later session can repeat it): Xbox Series X — NO MATCH (the
  set has no Xbox console of any kind; the four Microsoft entries
  are all controllers — Wireless 1914, Elite Series 2 FST-00001,
  Elite Core 4IK-00001, Adaptive Controller; the consoles in the
  set are PS5 and Switch lines); Xbox Series S — NO MATCH (no
  Series S of any kind; the 1TB Robot White/Carbon Black are
  different configs of the same console family and are not in
  the set either); Xbox Wireless Headset (2024 refresh) — NO
  MATCH (the set has no Xbox headset; the PULSE Elite/Explore
  are Sony headsets); Xbox Stereo Headset — NO MATCH (no Xbox
  wired headset; the 20th Anniversary Special Edition is a
  different headset and is not in the set); Surface Laptop,
  13.8-inch (8th Edition) — NO MATCH (the set has no Surface
  device of any kind; the laptops in the set are MacBook lines
  plus Lenovo/Dell/HP/ASUS entries). No candidate matches an
  existing model on name, MPN or UPC. The five are the Microsoft
  US store sweep candidates, one per hardware family; all five
  Microsoft US store pages return JSON-LD Product.offers on
  fresh reads 2026-11-06 ~21:13–21:14 UTC.
- Xbox Series X 1TB Disc Edition, Black (RRT-00001) —
  identifiers VERIFIED: UPC 889842640724 + MPN RRT-00001
  (Micro Center US spec, SKU 191429, HDR Blu-ray drive, + marknet
  auction listing agree on the exact pair; Amazon's RRT-00001
  listing corroborates the code as GTIN 00889842640724).
  Quotes (2): Microsoft $799.99 (US store page JSON-LD read
  fresh 2026-11-06 21:13 UTC, $749.99 to $799.99 — $799.99 is
  the Disc Black pinned here, $749.99 is the Digital White;
  stock not stated in the page text); ShopCGX $799.99 (Model
  RRT-00001, OutOfStock — agrees on price). Stock caveat: Micro
  Center and ShopCGX both show RRT-00001 OutOfStock, and gamegpu
  (Nov 1) reports US shortages after the Digital Edition was
  discounted to $599.99 at Amazon/Target — re-check stock next
  refresh. Not the 1TB Digital Edition in White ($749.99), the
  2TB Galaxy Black Special Edition (sunset Aug 2026) or the Xbox
  Series X25 Limited Edition ($899.99, launches Nov 13). The
  $799.99 is the Aug 1, 2026 list price (was $649.99), not a
  sale.
- Xbox Series S 512GB All-Digital, Robot White — identifiers
  PENDING: no code has two agreeing US sources — Micro Center
  lists the current 512GB console as Mfr Part # EP2-10050, UPC
  196388421343 (single source); eBay lists the original part
  RRS-00001, UPC 0889842651317 (single source); Amazon's Series
  X listing lumps 889842640731 among five unattributed UPCs;
  PBTech NZ lists EP2-10071, UPC 196388421541 (regional).
  Nothing was copied; re-check next refresh. Quotes (2):
  Microsoft $499.99 (US store page JSON-LD read fresh
  2026-11-06, $499.99 to $599.99 — $499.99 is the 512GB Robot
  White pinned here; stock not stated); feed rows at $499.99 for
  the 512GB Digital console agree (suspected; not
  page-verified). The $499.99 is the Aug 1, 2026 list price (was
  $399.99). Not the 1TB Robot White ($599.99) or the 1TB Carbon
  Black.
- Xbox Wireless Headset, 2024 refresh, Black — identifiers
  PENDING: no MPN or UPC surfaced for the 2024 refresh in any
  source read; the 2021 model's TLL-00001 code was not copied
  across. Not copied: nothing — no candidate code surfaced.
  Quotes (2): Microsoft $110.99 (US store page JSON-LD, two
  fresh crawls agree 2026-11-06; stock not stated; feed
  Microsoft row agrees at $110.99). Correction vs the stale
  price: the feed's Microsoft $99.99 row is the 2021-model
  price; the 2024 refresh launched at $109.99 (Xbox Wire Oct 22,
  2024 — Dolby Atmos, Bluetooth 5.3, 20-hour battery, upgraded
  mic, green accents removed) and now lists at $110.99, $1
  above launch. Not the Starfield Limited Edition ($250.79 feed
  row) or the Forza Horizon 6 Limited Edition ($134.99 feed
  row).
- Xbox Stereo Headset, Black (8LI-00001) — identifiers VERIFIED:
  UPC 889842748031 + MPN 8LI-00001 (Ubuy listing, Model
  8LI-00001, UPC 889842748031, + eBay US product identifiers,
  MPN 8LI00001, UPC 0889842748031, agree; MPN corroborated by
  Verizon + Best Buy US Model 8LI-00001 SKU 6474763 +
  manuals.plus). A second eBay listing's 499007320363 conflicts
  and was excluded. Quotes (2): Microsoft $59.99 (US store page
  JSON-LD read fresh 2026-11-06; stock not stated); Verizon
  $59.99 (Model 8LI-00001/Black) agrees. The feed's Microsoft
  $79.99 and $74.99 rows are third-party inflated and were not
  used. Launched Sep 2021 at $59.99 — price unchanged five years
  on. Not the 20th Anniversary Special Edition (feed rows
  $99.99–$119.99).
- Surface Laptop, 13.8-inch (8th Edition), Platinum
  (EP2-59028) — identifiers PENDING: MPN EP2-59028 is stated
  only by TheGoodGuys AU for this exact config (single non-US
  source) and no UPC surfaced, so identifiers stay empty per the
  strict two-source rule; the MPN lives in the variant string
  only, as in batches 23–26. Not copied: nothing — no candidate
  code surfaced. Quotes (2): Microsoft $1,299.99 sale vs
  $1,599.99 list (US store configure page, two fresh crawls
  2026-11-06 agree — X2 Plus (10 Core) 'From $1,299.99' with
  'Save $300.00' on the Platinum 16GB/512GB config; the
  $1,599.99 list is the per-config price on the 5-day-old crawl
  and pcdepo's 'starts at around $1,600'); Best Buy $1,199.99
  sale (reg $1,600), reported by 9to5Toys Nov 2 (early Black
  Friday) — reported, not page-verified. Base config pinned
  cleanly: 8th Edition introduced Jun 16, 2026 (Snapdragon X2,
  120 Hz HDR PixelSense Flow, haptic touchpad, up to 20-hour
  battery); US base is X2 Plus 10-core / 16GB / 512GB / Platinum
  (pcdepo confirms the entry config; 512GB is the storage
  minimum). Not the X2 Elite 12-core, 32GB/64GB or 1TB configs,
  the 15-inch 8th Edition, the 7th Edition (feed row $1,799.99)
  or the 256GB EP2-77788 (smaller 13-inch Surface Laptop, a
  different model). Re-check the $1,299.99 sale price after
  Black Friday (Nov 27).
- Skipped this batch, list-only: Surface Slim Pen 2 ($129.99 at
  Microsoft direct; MPN 8WV-00001 vs 8WX-00001 conflict
  unresolved — feed rows cite both codes); Xbox Rechargeable
  Battery + USB-C Cable SXW-00001 ($24.99; UPC 889842590364
  appears as a feed brand field, single source); Surface Pro
  11th Edition (base config price not pinned cleanly — LCD
  256GB vs 512GB rows conflict across feed and Microsoft
  crawls); Xbox Series X 2TB Galaxy Black Special Edition
  (sunset Aug 2026); Xbox Series X25 Limited Edition ($899.99,
  launches Nov 13).
- Eval on the new snapshot: 160 models, 76 verified identifiers,
  5 with quotes, 10 total quotes, 0 identifier-matched, 10
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 155 → 160, verified 74 → 76, for the
  continuous expansion; the pending set gains the 3 new pending
  keys: xbox-series-s-512gb-robot-white,
  xbox-wireless-headset-2024-black,
  microsoft-surface-laptop-13-8-8th-edition-platinum).

## 067 — 2026-11-06: Expansion batch 28 — 160 → 165 models (DECISIONS 050)

- Membership check (against the 160-model set in
  price_agent/catalog.py, by name, MPN and UPC — recorded here so
  a later session can repeat it): vívoactive 6 — NO MATCH (the
  set has no Garmin entry of any kind; the wearables in the set
  are 3 Apple Watch lines); Venu 4 — NO MATCH (no Venu of any
  kind; the 41mm is a different size and is not in the set
  either); Forerunner 570 — NO MATCH (no Forerunner of any
  kind; the 47mm is a different size and is not in the set
  either); Edge 1050 — NO MATCH (the set has no cycling
  computer of any kind and no "cycling-computers" category);
  fēnix 9 — NO MATCH (no fēnix of any kind; the fēnix 8 is a
  different model and is not in the set either). No candidate
  matches an existing model on name, MPN or UPC. The five are
  the Garmin US store sweep candidates, one per hardware
  family; all five Garmin US store pages return JSON-LD
  Product.offers on fresh reads 2026-11-06 ~21:21 UTC.
- Garmin vívoactive 6, Slate with Black silicone band
  (010-02985-00) — identifiers VERIFIED: UPC 753759342807 +
  MPN 010-02985-00 (Petra US, Vendor SKU 010-02985-00, UPC
  753759342807, + HeartRateMonitorsUSA MPN/UPC table,
  Slate/Black 010-02985-00 / 753759342807, agree; MPN
  corroborated by Dell US Mfr Part # 010-02985-00 + Best Buy
  US Model 010-02985-00, SKU 6628683). Quotes (2): Garmin
  $299.99 (US store page JSON-LD read fresh 2026-11-06 —
  the page shows the Lunar Gold variant but the price is
  uniform $299.99 across all four colors); Dell $299.99
  (Mfr Part # 010-02985-00, Temporarily Out of Stock —
  stock caveat recorded). 42.2 mm AMOLED, up to 11 days
  battery, launched 2025. Not the Lunar Gold/Bone
  010-02985-01 (UPC 753759342814), Metallic Jasper Green
  010-02985-02 (UPC 753759342821) or Pink Dawn 010-02985-03
  (UPC 753759342838) colorways, and not the vívoactive 5.
- Garmin Venu 4, 45mm, Silver stainless steel bezel with
  Silver Gray silicone band (010-03014-01) — identifiers
  VERIFIED: UPC 753759342883 + MPN 010-03014-01 (Petra US,
  Vendor SKU 010-03014-01, UPC 753759342883, GTIN
  00753759342883, + HeartRateMonitorsUSA MPN/UPC table,
  45mm Silver / Silver Gray 010-03014-01 / 753759342883,
  agree; MPN corroborated by Abt US Model 010-03014-01 +
  the Garmin US store URL pn/010-03014-01). Quotes (2):
  Garmin $549.99 (US store page JSON-LD read fresh
  2026-11-06 — the page description is the pinned variant
  exactly); Dell $499.99 sale vs $549.99 list (Meta Catalog
  feed authorized_retailer row for this exact variant —
  early Black Friday pricing, suspected, not
  page-verified). Launched Sep 22, 2025 at $549.99 (Garmin
  press release); 45 mm AMOLED, stainless steel bezel, ECG
  app, LED flashlight, up to 12 days battery. Not the 41 mm
  (different size, same $549.99), the Slate/Black silicone
  010-03014-00 (UPC 753759342876), the Silver/Citron
  010-03014-02, or the Slate/Black + Brown leather
  010-03014-03 ($599.99).
- Garmin Forerunner 570, 42mm, Raspberry Aluminum with
  Translucent Bone/Mango band (010-02970-02) — identifiers
  VERIFIED: UPC 753759349820 + MPN 010-02970-02 (Target US,
  TCIN 94760143, UPC 753759349820, $549.99, In Stock, +
  Selenal.lv, part code 010-02970-02, Barcode 753759349820,
  agree; CycleSuperStore.ie barcode list confirms the
  -00/-01/-02 mapping, 753759349806 / 753759349813 /
  753759349820; MPN corroborated by the Garmin US store URL
  pn/010-02970-02 + the Meta Catalog feed row for this exact
  variant). Amazon item details were read only as a third
  corroboration and are not needed for the verification.
  Quotes (2): Garmin $549.99 (Meta Catalog feed Garmin row
  for this exact variant pn/010-02970-02; Garmin US store
  page JSON-LD read fresh 2026-11-06 confirms $549.99 for
  the 42mm line — the page shows the Slate Gray variant but
  the price is uniform across sizes and colors); Target
  $549.99 In Stock (TCIN 94760143 — agrees with Garmin
  direct). Launched May 21, 2025 at $549.99 alongside the
  Forerunner 970; 42 mm AMOLED, multi-band GPS, speaker and
  mic, up to 10 days battery — no offline maps and no ECG,
  which stay exclusive to the 970. Not the 47 mm 570
  (different size, same $549.99), the Slate Gray
  010-02970-00 or Cloud Blue 010-02970-01 colorways, or the
  Forerunner 970 ($749.99).
- Garmin Edge 1050, device only, Black (010-02890-00) —
  identifiers VERIFIED: UPC 753759336288 + MPN 010-02890-00
  (HeartRateMonitorsUSA 010-02890-00 / 753759336288 +
  6ave UPC 753759336288, MPN 010-02890-00 + The Pro's
  Closet mpn 010-02890-00, upc 753759336288 + SunnySports
  MFR 010-02890-00, UPC 753759336288 agree; the Meta
  Catalog feed row for this device carries GTIN
  753759336288. The 010-02890-01 bundle's EAN
  0753759336295 is a different code and was excluded.)
  Quotes (2): Garmin $699.99 (US store page JSON-LD read
  fresh 2026-11-06); BikeTiresDirect $699.99 (Mfg PartNum
  010-02890-00 — agrees with Garmin direct). Best Buy feed
  row $699.99 sale (list $704.95) also agrees. Launched Jun
  2024 at $699.99; 3.5-inch 480x800 touchscreen, 64 GB,
  speaker and bike bell, Garmin Pay, up to 20 hours
  demanding use / 60 hours battery saver. The Edge 1060
  launched Oct 20, 2026 at $799.99 and replaces the 1050 as
  Garmin's premium computer, but the 1050 is still listed
  and sold at $699.99 at Garmin direct and multiple US bike
  shops on 2026-11-06 — not discontinued. Not the
  010-02890-01 sensor bundle (different MPN/EAN) or the
  Edge 1040 Solar (previous generation).
- Garmin fēnix 9, 47mm, Titanium with Pebble Gray silicone
  band (010-04762-00) — identifiers PENDING: MPN
  010-04762-00 is confirmed by Garmin US + Abt + RA Cycles,
  but no UPC surfaced in any source read — the fēnix 9 is
  ten weeks old and retailer UPC fields are still blank;
  the MPN lives in the variant string only, per the Surface
  Laptop (batch 27) precedent; re-check next refresh.
  Quotes (2): Garmin $999.99 (US store page JSON-LD read
  fresh 2026-11-06 — the page description is the pinned
  variant exactly); Abt $999.99 (Model 010-04762-00,
  InStock — agrees with Garmin direct). NFM $999.99 also
  agrees, and the Meta Catalog feed carries five $999.99
  rows naming MPN 010-04762-00. Announced Aug 25, 2026,
  orderable Aug 28; 47 mm AMOLED (twice as bright as
  fēnix 8), titanium bezel, sapphire lens, leakproof metal
  buttons, LED flashlight, 64 GB, up to 16 days battery.
  Not the 43 mm or 51 mm fēnix 9 ($999.99 / $1,099.99),
  the Carbon Gray DLC Titanium 010-04762-10 ($1,049.99),
  or any fēnix 9 Pro line ($1,099.99+, full titanium case
  and/or inReach/solar).
- Skipped this batch, list-only: Forerunner 970 47mm Carbon
  Gray DLC Titanium 010-02969-00 ($749.99 at Garmin direct,
  Abt and Best Buy — UPC conflicted: Amazon item details +
  Snapklik say 753759349929, a single eBay listing says
  753759349899, and the -01 variant is likewise conflicted,
  Abt 753759349905 vs Snapklik 753759349936 — nothing
  copied; needs a dedicated tiebreak, e.g. Best Buy specs
  or a box barcode, before any code is recorded); Edge 1060
  ($799.99, launched Oct 20, 2026 — too new for UPC
  verification; re-check once retailer UPC fields
  populate); Fenix 8 47mm AMOLED (superseded by the
  fēnix 9, now discounted last-gen); Instinct 3, Forerunner
  165, Edge 850, Garmin dash cams (not yet swept).
- Eval on the new snapshot: 165 models, 80 verified identifiers,
  5 with quotes, 10 total quotes, 0 identifier-matched, 10
  suspected (snapshot offers carry no identifier — the rule
  working, not a bug). Tests: 19 passed (test_snapshot_eval
  counts updated 160 → 165, verified 76 → 80, for the
  continuous expansion; the pending set gains the 1 new pending
  key: garmin-fenix-9-47mm-titanium-pebble-gray).
