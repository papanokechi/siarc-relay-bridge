# -*- coding: utf-8 -*-
"""Locate the two attributed passages in the acquired PDFs.

Text layer is used for LOCATION ONLY. Anything quoted is read afterwards from a
rendered page image, per the standing rule in this thread.
"""
import json
import os
import re

import fitz

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
REFS = os.path.join(SESS, 'CT-R1-AUDIT', 'refs')

SALVY = os.path.join(REFS, 'ibrahim_salvy_2023_positivity_certificates_arxiv-2306.05930.pdf')
WZ = os.path.join(REFS, 'wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf')

SALVY_PAT = [r'connexion', r'connection problem', r'not computable', r'computable',
             r'leading coefficient', r'cannot .{0,40}(zero|vanish)',
             r'certified numerical']
# The growth law as this project states it: Q_n / Gamma(dn+1) ~ K (beta_d/d^d)^n n^s
# with s = beta_{d-1}/beta_d + (d-1)/2. Search for any component of it.
WZ_PAT = [r'\bGamma\s*\(\s*dn', r'growth', r'\bK\b\s*\(', r'Birkhoff',
          r'Perron', r'second-order linear difference', r'Wong', r'\bLi\b',
          r'asymptotic .{0,20}difference equation']

out = {}
for tag, path, pats in (('salvy', SALVY, SALVY_PAT), ('wong_zhao', WZ, WZ_PAT)):
    doc = fitz.open(path)
    hits = []
    for i in range(doc.page_count):
        t = doc[i].get_text()
        flat = re.sub(r'\s+', ' ', t)
        for p in pats:
            for m in re.finditer(p, flat, re.I):
                a = max(0, m.start() - 170)
                hits.append({'page_index': i, 'printed_guess': i + 1,
                             'pattern': p,
                             'context': flat[a:m.end() + 230]})
    out[tag] = {'file': os.path.basename(path), 'pages': doc.page_count,
                'n_hits': len(hits), 'hits': hits}
    print('=== %s: %d pages, %d hits' % (tag, doc.page_count, len(hits)))
    doc.close()

# Section map for the Wong-Zhao survey, so "section 3" can be located exactly.
doc = fitz.open(WZ)
secs = []
for i in range(doc.page_count):
    for line in doc[i].get_text().split('\n'):
        s = line.strip()
        if re.match(r'^\d+\.\s+\S', s) and len(s) < 90:
            secs.append({'page_index': i, 'printed_guess': i + 1, 'heading': s})
out['wong_zhao']['section_headings'] = secs
doc.close()
print('\nWong-Zhao section headings found:', len(secs))
for s in secs[:14]:
    print('  p%-3d %s' % (s['printed_guess'], s['heading'][:70]))

with open(os.path.join(HERE, 'outputs', 'locate_passages.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
assert os.path.exists(os.path.join(HERE, 'outputs', 'locate_passages.json'))
print('\nwrote outputs/locate_passages.json')
print('READBACK OK')
