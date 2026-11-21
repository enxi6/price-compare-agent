"""Batch 7 membership check — coordinator's own run.

Checks every candidate in data/rework7/candidates_batch7_*.tsv against
data/rework7/catalog_ref_500.tsv (500 rows from price_agent/catalog.py)
by exact key, normalized model-name substring (both directions), MPN,
and UPC (incl. pending leads), plus intra-batch duplicate keys / MPNs /
UPCs. Mirrors the batch-6 rework script (/tmp/batch6_rework_membership.py).
"""
import csv
import re
import sys
from collections import Counter, defaultdict

CAT = 'data/rework7/catalog_ref_500.tsv'


def norm(s):
    return re.sub(r'[^a-z0-9]+', '', (s or '').lower())


def load_tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def main(cand_path):
    cat = load_tsv(CAT)
    cands = load_tsv(cand_path)
    print(f'catalog rows: {len(cat)}; candidates: {len(cands)}')

    # catalog lookup structures
    cat_keys = {r['key'] for r in cat}
    cat_mpn = defaultdict(list)
    cat_upc = defaultdict(list)
    for r in cat:
        if r['MPN']:
            cat_mpn[norm(r['MPN'])].append(r['key'])
        if r['UPC']:
            cat_upc[norm(r['UPC'])].append(r['key'])
    cat_names = [(norm(r['model'] + ' ' + r['variant']), r['key'],
                  r['model']) for r in cat]

    hits = []
    for c in cands:
        ck, cm = c['key'], norm(c['model'] + ' ' + c['variant'])
        if ck in cat_keys:
            hits.append((c['key'], 'EXACT-KEY', ck))
        if c['mpn'] and norm(c['mpn']) in cat_mpn:
            hits.append((c['key'], 'MPN', f"{c['mpn']} -> {cat_mpn[norm(c['mpn'])]}"))
        if c['upc'] and norm(c['upc']) in cat_upc:
            hits.append((c['key'], 'UPC', f"{c['upc']} -> {cat_upc[norm(c['upc'])]}"))
        for cn, ckey, cmodel in cat_names:
            if len(cm) >= 6 and len(cn) >= 6 and (cm in cn or cn in cm):
                hits.append((c['key'], 'NAME-SUBSTRING',
                             f"'{c['model']} {c['variant']}' <-> catalog '{cmodel}' ({ckey})"))
    # intra-batch duplicates
    for field in ('key', 'mpn', 'upc'):
        seen = Counter(c[field] for c in cands if c[field])
        for val, n in seen.items():
            if n > 1:
                hits.append(('*BATCH*', f'DUP-{field.upper()}', f'{val} x{n}'))

    print(f'raw hits: {len(hits)}')
    for h in hits:
        print(' -', h[0], '|', h[1], '|', h[2])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else
                  'data/rework7/candidates_batch7_47.tsv'))
