# -*- coding: utf-8 -*-
"""Acquire the two CC-BY-4.0 arXiv references into CT-R1-AUDIT/refs/ and add
their rows to REFS-MANIFEST.md with the licence as printed on the source.

Both were confirmed CC-BY-4.0 by scripts/verify_refs.py, so unlike
arXiv:0902.1702 (nonexclusive-distrib/1.0) they carry a redistribution right.
"""
import hashlib
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
REFS = os.path.join(SESS, 'CT-R1-AUDIT', 'refs')
MAN = os.path.join(SESS, 'CT-R1-AUDIT', 'REFS-MANIFEST.md')
V = json.load(open(os.path.join(HERE, 'outputs', 'refs_verify.json'), encoding='utf-8'))

WANT = {
    '2204.09305': 'wong_zhao_2022_recent_advances_arxiv-2204.09305.pdf',
    '2306.05930': 'ibrahim_salvy_2023_positivity_certificates_arxiv-2306.05930.pdf',
}
os.makedirs(REFS, exist_ok=True)
rows = []
for aid, name in WANT.items():
    rec = V['arxiv'][aid]
    lic = rec['licence_as_printed']
    assert any('creativecommons.org/licenses/by/4.0' in l for l in lic), \
        'refusing to acquire %s: licence is %r' % (aid, lic)
    url = 'https://arxiv.org/pdf/' + aid
    dest = os.path.join(REFS, name)
    req = urllib.request.Request(url, headers={'User-Agent': 'curl/8'})
    with urllib.request.urlopen(req, timeout=90) as r:
        blob = r.read()
    assert blob[:5] == b'%PDF-', 'not a PDF: %r' % blob[:16]
    open(dest, 'wb').write(blob)
    got = open(dest, 'rb').read()
    assert got == blob, 'readback: written bytes differ'
    rows.append({
        'file': 'CT-R1-AUDIT/refs/' + name,
        'aid': aid, 'url': url,
        'title': rec['title'], 'authors': '; '.join(rec['authors']),
        'jref': rec['journal_ref'], 'doi': rec['doi'],
        'bytes': len(got), 'sha256': hashlib.sha256(got).hexdigest(),
        'licence': lic[0],
    })
    print('%-58s %8d bytes  %s' % (name, len(got), rows[-1]['sha256'][:16]))

MARK = '### CT-S21 addendum - two CC-BY references acquired for v1.7'
before = open(MAN, encoding='utf-8').read()
assert MARK not in before
L = ['', MARK, '',
     'Acquired 2026-09-18. Both carry **CC-BY-4.0 as printed on the arXiv abstract',
     'page**, which grants a redistribution right - unlike arXiv:0902.1702, whose',
     'default `nonexclusive-distrib/1.0` licence grants none. These two are therefore',
     'the first third-party files in `refs/` cleared for redistribution on evidence.',
     'The blanket media exclusion still applies until the operator re-admits them by',
     'name; the licence is recorded here so that decision rests on evidence.', '',
     '| file | source | licence | bytes | sha256 |', '|---|---|---|---|---|']
for r in rows:
    L.append('| `%s` | `%s` | **%s** | %d | `%s` |' % (
        r['file'], r['url'], r['licence'], r['bytes'], r['sha256']))
L += ['', '| arXiv | citation |', '|---|---|']
for r in rows:
    L.append('| `%s` | %s. *%s*. %s DOI `%s` |' % (
        r['aid'], r['authors'], r['title'], (r['jref'] or '') + '.', r['doi']))
L += ['',
      '**Purchase target, citation confirmed today by DOI content negotiation:**',
      'R. Wong and H. Li, *Asymptotic Expansions for Second-Order Linear Difference',
      'Equations, II*, **Stud. Appl. Math. 87(4) (1992), 289-324**, DOI',
      '`10.1002/sapm1992874289`, issued 1992-11. This matches the citation table in',
      '`P0-CITATION-RULE.md` exactly, including the "II" and the word "linear" whose',
      'omission was the trap recorded at `R1-61`.', '']
with open(MAN, 'a', encoding='utf-8') as f:
    f.write('\n'.join(L) + '\n')
back = open(MAN, encoding='utf-8').read()
assert MARK in back
for r in rows:
    assert r['sha256'] in back, 'readback: missing hash for ' + r['file']
assert '10.1002/sapm1992874289' in back
print('REFS-MANIFEST.md %d -> %d lines' % (before.count('\n'), back.count('\n')))
print('READBACK OK')
