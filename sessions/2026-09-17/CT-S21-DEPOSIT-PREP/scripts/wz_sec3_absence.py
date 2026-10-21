# -*- coding: utf-8 -*-
"""Absence test for the growth law in Wong-Zhao (arXiv:2204.09305) section 3.

S17-22 guard: a bare absence test CANNOT FAIL if the text extraction is empty or
mis-scoped -- every pattern would be 'absent' and the verdict would look like a
finding. So POSITIVE CONTROLS run first over the same extracted string. If any
control fails to fire, the whole run is VOID and no absence verdict is emitted.
"""
import hashlib
import json
import os
import re

import fitz

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(HERE, '..', 'CT-R1-AUDIT', 'refs',
                   'wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf')

# Section 3 'Difference equations' spans PDF pp. 12-20 per the PDF outline
# ([1,'3 Difference equations',12] and [1,'4 Riemann-Hilbert approach',21]).
FIRST, LAST = 12, 20

doc = fitz.open(PDF)
toc = doc.get_toc()
assert ['3 Difference equations', 12] == [toc[2][1], toc[2][2]], toc
assert ['4 Riemann-Hilbert approach', 21] == [toc[3][1], toc[3][2]], toc

raw = '\n'.join(doc[i].get_text() for i in range(FIRST - 1, LAST))
doc.close()
flat = re.sub(r'\s+', ' ', raw)

# --- positive controls: these MUST all fire -------------------------------
CONTROLS = {
    'section heading present': r'Di.{0,3}erence equations',
    'Wong-Li cited': r'Wong and Li',
    'eq (3.2) general class': r'y\(n \+ 2\) \+ npa\(n\)',
    'turning point theory': r'turning point',
    'Theorem 3.3 present': r'Theorem 3\.3',
    'normalisation K_n': r'Kn\+1/Kn.{0,3}1 = cn',
}
controls = {k: bool(re.search(p, flat, re.I)) for k, p in CONTROLS.items()}
VOID = not all(controls.values())

# --- the absence patterns -------------------------------------------------
ABSENT = {
    'Gamma(dn+1) normalisation': r'\u0393\s*\(\s*dn|Gamma\s*\(\s*dn|\(dn \+ 1\)',
    'growth-law exponent s = b_{d-1}/b_d + (d-1)/2': r'\(d\s*-\s*1\)\s*/\s*2',
    'beta_d / d^d base': r'd\s*\^?\s*d\b.{0,12}\)\s*n|\u03b2d/dd',
    'explicit leading constant K': r'\bK\b\s*(?:\u00b7|\*|\\cdot)\s*\(',
    'phrase "growth law"': r'growth law',
    'dominant-solution growth rate': r'rate of growth|growth rate',
}
absent = {}
for k, p in ABSENT.items():
    hits = [m.group(0) for m in re.finditer(p, flat, re.I)]
    absent[k] = {'found': bool(hits), 'examples': hits[:4]}

out = {
    'source': 'arXiv:2204.09305 (Wong & Zhao 2022), section 3, PDF pp. %d-%d' % (FIRST, LAST),
    'sha256_pdf': hashlib.sha256(open(PDF, 'rb').read()).hexdigest(),
    'chars_extracted': len(flat),
    'controls': controls,
    'VOID': VOID,
    'absence_patterns': absent,
}
out['verdict'] = (
    'VOID - controls did not fire; no absence claim may be made'
    if VOID else
    'NOT FOUND in section 3 by full-text read: no statement of the growth law'
    if not any(v['found'] for v in absent.values()) else
    'PARTIAL - some pattern matched; inspect examples before claiming absence')

p = os.path.join(HERE, 'outputs', 'wz_sec3_absence.json')
with open(p, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
back = json.load(open(p, encoding='utf-8'))
assert back['verdict'] == out['verdict'], 'READBACK MISMATCH'
print('controls:', json.dumps(controls, indent=1))
print('VOID:', VOID, '| chars:', len(flat))
for k, v in absent.items():
    print('  %-48s found=%s %s' % (k, v['found'], v['examples'][:2]))
print('\nVERDICT:', out['verdict'])
print('readback OK ->', p)
