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
