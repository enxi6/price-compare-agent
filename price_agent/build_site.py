"""Static-site generator for the price-compare website (Phase 2, v1).

Renders ``data/site_snapshot_*.json`` into a multi-page static site
(``site/`` by default): a home page with client-side search, one
compare page per model (200), a method-and-principles page, and a
coverage-and-gaps page. Stdlib only; re-runnable after every daily
refresh -- a failed render never publishes a half-finished page
(output goes to a temporary directory and is moved into place only
when every page renders).

Honesty rules enforced by this generator (DECISIONS 001/002):
- Snapshot offers carry no identifier, so the verified ranking is
  EMPTY on every product page until an identifier-returning source is
  connected. Offers are shown only in the clearly labeled
  title-matched ("suspected") table, never dressed up as a ranking.
- Every price carries its merchant, source link and fetch time.
  Anything older than 24h at generation time is labeled
  "Needs re-check". The snapshot date is shown prominently.
- Nothing is invented: unknown models say "not indexed"; models with
  no quotes say so; gaps are listed, not hidden.

Usage:
    python3 -m price_agent.build_site
    python3 -m price_agent.build_site --input data/site_snapshot_2026-11-06.json --out site
"""

from __future__ import annotations

import argparse
import html
import json
import os
import shutil
import tempfile
from datetime import datetime, timezone

DEFAULT_INPUT = "data/site_snapshot_2026-11-06.json"
DEFAULT_OUT = "site"
STALE_AFTER_HOURS = 24.0

CSS = """
body{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;max-width:960px;
margin:0 auto;padding:24px 16px;color:#1a1a1a;line-height:1.55}
a{color:#0b5fff}header{border-bottom:2px solid #1a1a1a;padding-bottom:12px;
margin-bottom:24px}nav a{margin-right:16px}.muted{color:#555;font-size:.9em}
.notice{background:#fff8e1;border:1px solid #e6c200;padding:12px 16px;
border-radius:6px;margin:16px 0}.warn{background:#fdecea;border:1px solid #d93025;
padding:12px 16px;border-radius:6px;margin:16px 0}
.ok{background:#e6f4ea;border:1px solid #137333;
padding:12px 16px;border-radius:6px;margin:16px 0}
table{border-collapse:collapse;width:100%;margin:12px 0}
th,td{border:1px solid #ddd;padding:8px;text-align:left;vertical-align:top}
th{background:#f2f2f2}tr:nth-child(even){background:#fafafa}
.tag{display:inline-block;padding:1px 8px;border-radius:10px;font-size:.85em;
background:#e8f0fe}.tag.pending{background:#fef3c7}.tag.stale{background:#fdecea}
input[type=search]{width:100%;padding:10px;font-size:1.05em;margin:12px 0}
.stat{font-size:1.4em;font-weight:700}footer{border-top:1px solid #ddd;
margin-top:40px;padding-top:12px;color:#555;font-size:.9em}
h1{font-size:1.6em}h2{font-size:1.25em;margin-top:28px}
"""

BASE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><style>{css}</style></head>
<body><header><nav>
<a href="{root}index.html">Home</a>
<a href="{root}method.html">Method &amp; principles</a>
<a href="{root}coverage.html">Coverage &amp; gaps</a>
</nav></header>
{body}
<footer><p>Prices are from our latest snapshot ({snapshot_date}). Quotes older
than 24 hours are labeled "Needs re-check". This site earns no commission
from any quote shown, runs no ads, and collects no data. See
<a href="{root}method.html">Method &amp; principles</a>.</p>
<p>Generated {generated_at} from {source_file}.</p></footer>
</body></html>"""


def esc(value) -> str:
    return html.escape(str(value), quote=True)


def money(value: float) -> str:
    return f"${value:,.2f}"


def age_hours(collected_at: str, now: datetime) -> float:
    collected = datetime.fromisoformat(collected_at.replace("Z", "+00:00"))
    return (now - collected).total_seconds() / 3600.0


def freshness_label(collected_at: str, now: datetime) -> str:
    hours = age_hours(collected_at, now)
    if hours > STALE_AFTER_HOURS:
        return '<span class="tag stale">Needs re-check</span>'
    return '<span class="tag">Current</span>'


def render_page(title: str, body: str, root: str, snapshot_date: str,
                generated_at: str, source_file: str) -> str:
    return BASE.format(
        title=esc(title), css=CSS, root=root, body=body,
        snapshot_date=esc(snapshot_date), generated_at=esc(generated_at),
        source_file=esc(source_file),
    )


def offer_rows(model: dict, now: datetime) -> str:
    rows = []
    for offer in model["offers"]:
        rows.append(
            "<tr><td>{merchant}</td><td>{price}</td>"
            "<td>{total}</td><td>{title}</td>"
            "<td><a href=\"{url}\" rel=\"nofollow\">Source</a></td>"
            "<td>{fetched}<br>{fresh}</td></tr>".format(
                merchant=esc(offer["merchant"]),
                price=money(offer["price"]),
                total=(
                    f"{money(offer['price'])} + shipping unknown"
                    " (not included)"
                ),
                title=esc(offer["title"]),
                url=esc(offer["url"]),
                fetched=esc(offer["collected_at"][:16].replace("T", " ")),
                fresh=freshness_label(offer["collected_at"], now),
            )
        )
    return "\n".join(rows)


def verified_rows(model: dict, now: datetime) -> str:
    """Rows for the verified ranking: matched offers, stored order."""
    rows = []
    for rank, offer in enumerate(
        [o for o in model["offers"] if not o["suspected"]], start=1
    ):
        identifier = offer.get("identifier") or ""
        kind = offer.get("identifier_kind") or ""
        rows.append(
            "<tr><td>{rank}</td><td>{merchant}</td><td>{price}</td>"
            "<td>{total}</td><td>{title}</td>"
            "<td>{identifier}</td><td>{source}</td>"
            "<td>{fetched}<br>{fresh}</td></tr>".format(
                rank=rank,
                merchant=esc(offer["merchant"]),
                price=money(offer["price"]),
                total=(
                    f"{money(offer['price'])} + shipping unknown"
                    " (not included)"
                ),
                title=esc(offer["title"]),
                identifier=esc(f"{kind} {identifier}".strip()),
                source=esc(offer.get("source") or "meta-catalog"),
                fetched=esc(offer["collected_at"][:16].replace("T", " ")),
                fresh=freshness_label(offer["collected_at"], now),
            )
        )
    return "\n".join(rows)


def product_page(model: dict, now: datetime, snapshot_date: str,
                 generated_at: str, source_file: str) -> str:
    if model["status"] == "verified":
        id_html = "<p>Identifier verified: " + ", ".join(
            f"{esc(k)} {esc(v)}" for k, v in model["identifiers"].items()
        ) + "</p>"
        status_tag = '<span class="tag">Identifier verified</span>'
    else:
        id_html = (
            "<p>No verified UPC, EAN or MPN yet for this exact variant. "
            "Quotes below are title-matched only and are not a verified "
            "ranking.</p>"
        )
        status_tag = '<span class="tag pending">Identifier pending</span>'
    matched = [o for o in model["offers"] if not o["suspected"]]
    suspected = [o for o in model["offers"] if o["suspected"]]
    if matched:
        id_list = ", ".join(
            f"{esc(k)} {esc(v)}" for k, v in model["identifiers"].items()
        )
        ranking = (
            '<div class="ok"><p><strong>Verified ranking: '
            f"{len(matched)} identifier-matched offer(s).</strong> "
            f"These offers matched the verified identifier(s) for this "
            f"exact variant ({id_list}), ordered by delivered total. "
            "Shipping is unknown unless shown.</p></div>"
            "<h2>Verified ranking (identifier-matched)</h2>"
            "<table><tr><th>Rank</th><th>Merchant</th><th>Price</th>"
            "<th>Landed total</th><th>Listing title</th>"
            "<th>Identifier</th><th>Source</th><th>Fetched</th></tr>"
            + verified_rows(model, now)
            + "</table>"
        )
    else:
        ranking = (
            '<div class="warn"><p><strong>Verified ranking: empty.</strong> No\n'
            "identifier-matched quotes exist in the latest snapshot, because the\n"
            "quote source we use does not return identifiers. Until an\n"
            "identifier-returning source is connected, this page shows\n"
            "title-matched offers only, clearly labeled as such.</p></div>"
        )
    if model["offers"]:
        if not suspected:
            table = (
                '<p class="muted">No additional title-matched offers.</p>'
            )
        else:
            suspected_intro = (
                "These additional offers matched by title only and are not "
                "in the verified ranking above."
                if matched else
                "These offers matched by title only. They are a price "
                "signal, not a verified same-product ranking: our quote "
                "source does not return identifiers, so no offer can enter "
                "the verified ranking yet."
            )
            table = (
                "<h2>Title-matched offers (suspected same product)</h2>"
                f"<p>{suspected_intro}</p>"
                "<table><tr><th>Merchant</th><th>Price</th>"
                "<th>Landed total</th><th>Listing title</th>"
                "<th>Source</th><th>Fetched</th></tr>"
                + offer_rows(
                    {"offers": suspected}, now)
                + "</table>"
            )
    else:
        table = (
            '<div class="notice"><p><strong>No quotes in the latest '
            f"snapshot ({esc(snapshot_date)}).</strong> This model had no "
            "seller-direct quote in the latest sweep. It may be out of "
            "stock or not listed by the sources we check. That is not a "
            "claim that it is discontinued.</p></div>"
        )
    identified_note = ""
    if model.get("identified_source_file"):
        identified_note = (
            f" Identifier-bearing quotes: "
            f"{esc(model['identified_source_file'])} &middot; fetched "
            f"{esc((model.get('identified_collected_at') or '')[:16].replace('T', ' '))} UTC."
        )
    body = f"""<p><a href="../index.html">&larr; All models</a> &middot;
{esc(model['category'])}</p>
<h1>{esc(model['brand'])} {esc(model['model'])}</h1>
<p>{esc(model['variant'])} &middot; {status_tag}</p>
{id_html}
{ranking}
{table}
<p class="muted">Source snapshot: {esc(model['source_file'] or 'none')}
&middot; fetched {esc((model['source_collected_at'] or '')[:16].replace('T', ' '))} UTC.{identified_note}
Shipping is unknown for every offer above, so the landed total is a
lower bound: item price only, shipping not included. Tax is estimated
at $0.00. Check the merchant page before buying.</p>"""
    return render_page(
        f"{model['brand']} {model['model']} — price comparison",
        body, "../", snapshot_date, generated_at, source_file,
    )


def home_page(data: dict, now: datetime, snapshot_date: str,
              generated_at: str, source_file: str) -> str:
    meta = data["meta"]
    models = data["models"]
    index = [
        {
            "key": m["key"],
            "brand": m["brand"],
            "model": m["model"],
            "variant": m["variant"],
            "category": m["category"],
            "identifiers": " ".join(m["identifiers"].values()),
        }
        for m in models
    ]
    from collections import Counter
    cats = Counter(m["category"] for m in models)
    cat_list = "".join(
        f"<li>{esc(c)}: {n} models</li>"
        for c, n in sorted(cats.items())
    )
    ranked_models = meta.get("verified_ranking_models", 0)
    matched_count = meta.get("matched_offers", 0)
    if ranked_models:
        notice = (
            f"<p><strong>Read this first:</strong> {ranked_models} of "
            f"{meta['models']} models now have a verified ranking from "
            f"identifier-matched quotes ({matched_count} matched "
            "offers). Every other product page shows title-matched "
            "offers only, clearly labeled. That is the rule working as "
            "designed, not a bug &mdash; see "
            '<a href="method.html">Method &amp; principles</a>.</p>'
        )
    else:
        notice = (
            "<p><strong>Read this first:</strong> our quote source "
            "does not return identifiers, so no offer on this site is in the "
            "verified ranking yet. Every product page shows title-matched offers "
            "only, clearly labeled. That is the rule working as designed, not a "
            "bug &mdash; see "
            '<a href="method.html">Method &amp; principles</a>.</p>'
        )
    body = f"""<h1>Buyer-side price comparison</h1>
<p>Compare prices for 200 standardized electronics models sold in the
US. Ranking is by delivered total price only. We earn no commission
from any quote shown, and commissions never affect ranking.</p>
<p><span class="stat">{meta['models']}</span> models &middot;
<span class="stat">{meta['verified_identifiers']}</span> verified identifiers
&middot; <span class="stat">{meta['pending_identifiers']}</span> pending
&middot; <span class="stat">{meta['total_offers']}</span> offers in the
latest snapshot (<strong>{esc(snapshot_date)}</strong>) &middot;
<span class="stat">{ranked_models}</span> models with a verified ranking
(<span class="stat">{matched_count}</span> matched offers)</p>
<div class="notice">{notice}</div>
<input type="search" id="q" placeholder="Search by product name, UPC or MPN&hellip;" autocomplete="off">
<div id="results"><p class="muted">Type to search all 200 models.</p></div>
<h2>Browse by category</h2><ul>{cat_list}</ul>
<script type="application/json" id="search-index">
{json.dumps(index, ensure_ascii=False)}
</script>
<script>
const INDEX = JSON.parse(document.getElementById('search-index').textContent);
const box = document.getElementById('q');
const out = document.getElementById('results');
box.addEventListener('input', () => {{
  const q = box.value.trim().toLowerCase();
  if (!q) {{ out.innerHTML = '<p class="muted">Type to search all 200 models.</p>'; return; }}
  const hits = INDEX.filter(m => (m.brand + ' ' + m.model + ' ' + m.variant + ' ' + m.category + ' ' + m.identifiers).toLowerCase().includes(q));
  if (!hits.length) {{ out.innerHTML = '<p><strong>Not indexed.</strong> We do not track this model yet. We never invent results.</p>'; return; }}
  out.innerHTML = '<ul>' + hits.map(m => '<li><a href="products/' + m.key + '.html">' + m.brand + ' ' + m.model + ' &mdash; ' + m.variant + '</a> <span class="muted">' + m.category + '</span></li>').join('') + '</ul>';
}});
</script>"""
    return render_page(
        "Price comparison — 200 electronics models (US)",
        body, "", snapshot_date, generated_at, source_file,
    )


METHOD_BODY = """<h1>Method &amp; principles</h1>
<p>How this site compares prices, what it can and cannot verify, and
where its money does and does not come from. No black-box scores.</p>

<h2>1. Ranking: delivered total, nothing else</h2>
<p>Offers in a verified ranking are ordered by delivered total:
item price + shipping + estimated tax &minus; discounts. Offers with
unknown shipping rank behind offers with known shipping, because an
unknown total is a lower bound, not a delivered price. Ties break by
delivery days, then seller rating. There is no composite score and no
"recommended for you".</p>

<h2>2. Same product means matching identifier</h2>
<p>Only a matching UPC, EAN, MPN or official SKU counts as the same
product. Similar titles go to the "suspected same product" appendix
and never enter the main ranking. An identifier is recorded only when
two independent sources state it for the exact variant (color, storage
and connectivity included). Identifiers are never invented, never
carried across variants, revisions or regions.</p>
<p><strong>Current state, stated plainly:</strong> {current_state}</p>

<h2>3. Data sources, in tiers</h2>
<p>Official APIs and feeds first, then affiliate catalogs, then
structured data, then read-only browser verification. A channel that
is blocked or prohibited by its terms of service stops there: no
bypassing verification, no fake identity, no rotating proxies.</p>
{identified_sources}
<p><strong>Amazon is not covered in v1.</strong> Its access wall is
treated as a permanent property of the retailer, not a temporary
failure. Only legitimate channels will ever be used (its official
API, or licensed data providers); none is live yet, and no Amazon
spend is approved.</p>

<h2>4. Which quotes count</h2>
<p>Only seller-direct or retailer-direct quotes: the merchant itself
selling the product. Marketplace and third-party seller rows are
excluded, even when cheaper. Only US-market goods (US MPN/UPC, sold by
US retailers). Only new units: used, refurbished and open-box are out
of scope for Phase 1. Bundles are excluded at snapshot time.</p>

<h2>5. Freshness</h2>
<p>Every price carries its merchant, source link and fetch time.
Prices are as of their snapshot date, shown on every page. Anything
older than 24 hours is labeled "Needs re-check" and is never
presented as a live price.</p>

<h2>6. Money and disclosure</h2>
<p>This site currently earns no commission from any quote shown. If
affiliate links are added later, they will be disclosed on this page
and will never affect ranking. There are no ads and no sponsored
placements. Ranking factors contain buyer interests only: total
price, delivery, reputation.</p>

<h2>7. Privacy</h2>
<p>This is a static site. No accounts, no login, no tracking, no data
collected. Search runs in your browser; nothing you type leaves the
page.</p>"""


def method_page(data: dict, snapshot_date: str, generated_at: str,
                source_file: str) -> str:
    meta = data["meta"]
    ranked_models = meta.get("verified_ranking_models", 0)
    matched_count = meta.get("matched_offers", 0)
    if ranked_models:
        current_state = (
            f"As of {snapshot_date}, {matched_count} offers across "
            f"{ranked_models} models are identifier-matched and appear "
            "in verified rankings. The remaining offers are "
            "title-matched only. New identifier-returning sources are "
            "added source by source; a model enters the verified "
            "ranking only when a quote's identifier matches its "
            "verified identifier."
        )
    else:
        current_state = (
            "our quote source (Meta Catalog search) returns no "
            "identifiers, so every offer on this site is currently "
            "title-matched only. The verified ranking is empty on "
            "every product page until an identifier-returning source "
            "is connected. The suspected table is shown as what it is "
            "&mdash; a price signal, not a verified ranking."
        )
    tier_names = {
        1: "Shopify public product JSON (tier 1)",
        2: "affiliate catalogs (tier 2)",
        3: "structured data from retailer spec pages (tier 3)",
        4: "browser-verified retailer spec pages (tier 4)",
    }
    tiers = sorted(
        {
            o.get("source_tier")
            for m in data["models"]
            for o in m["offers"]
            if not o["suspected"] and o.get("source_tier") in tier_names
        }
    )
    if tiers:
        identified_sources = (
            "<p>Identifier-bearing quotes currently come from "
            + ", ".join(tier_names[t] for t in tiers)
            + ".</p>"
        )
    else:
        identified_sources = ""
    body = METHOD_BODY.format(
        current_state=current_state,
        identified_sources=identified_sources,
    )
    return render_page(
        "Method & principles — price comparison",
        body, "", snapshot_date, generated_at, source_file,
    )


def coverage_page(data: dict, now: datetime, snapshot_date: str,
                  generated_at: str, source_file: str) -> str:
    meta = data["meta"]
    models = data["models"]
    from collections import Counter
    cats = Counter(m["category"] for m in models)
    ranked_models = meta.get("verified_ranking_models", 0)
    matched_count = meta.get("matched_offers", 0)
    cat_rows = "".join(
        f"<tr><td>{esc(c)}</td><td>{n}</td>"
        f"<td>{sum(1 for m in models if m['category'] == c and m['status'] == 'verified')}</td>"
        f"<td>{sum(1 for m in models if m['category'] == c and m['offers'])}</td>"
        f"<td>{sum(1 for m in models if m['category'] == c and any(not o['suspected'] for o in m['offers']))}</td></tr>"
        for c, n in sorted(cats.items())
    )
    model_rows = "".join(
        "<tr><td><a href=\"products/{key}.html\">{brand} {model}</a></td>"
        "<td>{status}</td><td>{n}</td><td>{matched}</td><td>{fetched}</td></tr>".format(
            key=esc(m["key"]),
            brand=esc(m["brand"]),
            model=esc(m["model"]),
            status=("Verified" if m["status"] == "verified" else "Pending"),
            n=len(m["offers"]),
            matched=sum(1 for o in m["offers"] if not o["suspected"]),
            fetched=esc((m["source_collected_at"] or "")[:16].replace("T", " ")),
        )
        for m in models
    )
    no_quotes = [m for m in models if not m["offers"]]
    no_quote_list = "".join(
        f"<li><a href=\"products/{esc(m['key'])}.html\">"
        f"{esc(m['brand'])} {esc(m['model'])}</a></li>"
        for m in no_quotes
    )
    stale = [
        m for m in models
        if m["offers"]
        and age_hours(m["offers"][0]["collected_at"], now)
        > STALE_AFTER_HOURS
    ]
    if ranked_models:
        ranking_gap = (
            f"<li><strong>Verified ranking populated for "
            f"{ranked_models} of {meta['models']} models "
            f"({matched_count} matched offers);</strong> the remaining "
            "models show title-matched offers only.</li>"
        )
    else:
        ranking_gap = (
            "<li><strong>The verified ranking is empty everywhere.</strong> All\n"
            f"{meta['total_offers']} offers are title-matched (suspected), because the\n"
            "quote source returns no identifiers. See the Method page.</li>"
        )
    body = f"""<h1>Coverage &amp; gaps</h1>
<p><span class="stat">{meta['models']}</span> models &middot;
<span class="stat">{meta['verified_identifiers']}</span> verified identifiers
&middot; <span class="stat">{meta['pending_identifiers']}</span> pending
&middot; <span class="stat">{meta['total_offers']}</span> offers &middot;
<span class="stat">{meta['models_with_offers']}</span> models with at least
one offer &middot; <span class="stat">{ranked_models}</span> models with a
verified ranking (<span class="stat">{matched_count}</span> matched offers).
Snapshot date: <strong>{esc(snapshot_date)}</strong>.</p>

<h2>Gaps, written truthfully</h2>
<ul>
<li><strong>{len(no_quotes)} models have no quotes</strong> in the latest
snapshot: <ul>{no_quote_list}</ul>They may be out of stock or not listed
by the sources we check. That is not a claim that they are discontinued.</li>
{ranking_gap}
<li><strong>{len(stale)} models have offers older than 24 hours</strong>
and are labeled "Needs re-check" on their pages.</li>
<li><strong>Amazon is not covered.</strong> See the Method page for why.</li>
<li><strong>{meta['pending_identifiers']} identifiers are pending.</strong>
Those models can only show title-matched offers until a second source
states their identifier.</li>
</ul>

<h2>Coverage by category</h2>
<table><tr><th>Category</th><th>Models</th><th>Verified</th>
<th>With offers</th><th>With verified ranking</th></tr>{cat_rows}</table>

<h2>Coverage by model</h2>
<table><tr><th>Model</th><th>Identifier</th><th>Offers</th><th>Matched</th>
<th>Latest fetch (UTC)</th></tr>{model_rows}</table>"""
    return render_page(
        "Coverage & gaps — price comparison",
        body, "", snapshot_date, generated_at, source_file,
    )


def build_site(input_path: str, out_dir: str) -> dict:
    """Render the whole site into a temp dir, then move it into place."""
    with open(input_path, encoding="utf-8") as handle:
        data = json.load(handle)
    now = datetime.now(timezone.utc)
    generated_at = now.isoformat()
    snapshot_date = data["meta"]["snapshot_date"]
    source_file = os.path.basename(input_path)

    tmp = tempfile.mkdtemp(prefix="price-compare-site-")
    try:
        os.makedirs(os.path.join(tmp, "products"))
        pages = {}
        pages["index.html"] = home_page(
            data, now, snapshot_date, generated_at, source_file)
        pages["method.html"] = method_page(
            data, snapshot_date, generated_at, source_file)
        pages["coverage.html"] = coverage_page(
            data, now, snapshot_date, generated_at, source_file)
        for model in data["models"]:
            pages[f"products/{model['key']}.html"] = product_page(
                model, now, snapshot_date, generated_at, source_file)
        for rel, content in pages.items():
            path = os.path.join(tmp, rel)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(content)
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
        shutil.move(tmp, out_dir)
    except Exception:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    return {
        "pages": len(pages),
        "models": len(data["models"]),
        "offers": data["meta"]["total_offers"],
        "matched_offers": data["meta"].get("matched_offers", 0),
        "verified_ranking_models": data["meta"].get(
            "verified_ranking_models", 0
        ),
        "out_dir": out_dir,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render the price-compare static site."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--out", default=DEFAULT_OUT)
    args = parser.parse_args()
    result = build_site(args.input, args.out)
    print(
        f"wrote {result['pages']} pages to {result['out_dir']}/ "
        f"({result['models']} models, {result['offers']} offers, "
        f"{result['matched_offers']} matched in "
        f"{result['verified_ranking_models']} verified rankings)"
    )


if __name__ == "__main__":
    main()
