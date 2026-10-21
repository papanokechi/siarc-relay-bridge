# -*- coding: utf-8 -*-
"""CT-S21 item 3 - licence strings AS PRINTED on the source.

No licence determination is made and no exclusion is changed. Where a licence
string cannot be read from the source, the row is NOT CHECKED - never inferred
from the publisher, the venue, or a neighbouring row.
"""
import datetime
import json
import os
import re
import subprocess
import tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, 'outputs', 'item3_licences.json')
TMP = os.path.join(tempfile.gettempdir(), 'ct-s21-licence')
os.makedirs(TMP, exist_ok=True)
TODAY = datetime.date.today().isoformat()


def curl(url, dest, headers=None):
    cmd = ['curl', '-sSL', '--max-time', '90', '-w', '%{http_code}', '-o', dest]
    for h in (headers or []):
        cmd += ['-H', h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True)
    return (p.stdout or '').strip()


def text(dest):
    return open(dest, encoding='utf-8', errors='replace').read()


out = {'retrieved': TODAY, 'rows': []}


def row(target, source_url, status, licence, quote=None, note=None):
    out['rows'].append({'target': target, 'source_url': source_url,
                        'status': status, 'licence_as_printed': licence,
                        'quote': quote, 'note': note})


# ---- Zenodo: the operator's own deposits -----------------------------------
for rid, ver in (('20455090', 'v1.0'), ('20480603', 'v1.1'), ('20481592', 'v1.2')):
    d = os.path.join(TMP, 'z%s.json' % rid)
    code = curl('https://zenodo.org/api/records/%s' % rid, d,
                ['Accept: application/vnd.inveniordm.v1+json'])
    if code != '200':
        row('companion %s (zenodo %s)' % (ver, rid), 'https://zenodo.org/api/records/' + rid,
            'NOT CHECKED', 'NOT CHECKED', note='HTTP %s' % code)
        continue
    j = json.loads(text(d))
    rights = [(r.get('id') or r.get('title')) for r in
              (j.get('metadata', {}) or {}).get('rights', [])]
    row('companion %s (zenodo %s)' % (ver, rid),
        'https://zenodo.org/api/records/%s' % rid, 'READ',
        ', '.join(str(r) for r in rights) if rights else 'NOT CHECKED',
        quote='metadata.rights (inveniordm view) = %s' % json.dumps(rights, ensure_ascii=False),
        note="operator's own deposit")

# ---- arXiv: the licence is PER SUBMISSION ----------------------------------
d = os.path.join(TMP, 'arxiv_abs.html')
code = curl('https://arxiv.org/abs/0902.1702', d)
if code == '200':
    h = text(d)
    m = re.search(r'(http[s]?://arxiv\.org/licenses/[^"\'<> ]+|'
                  r'http[s]?://creativecommons\.org/licenses/[^"\'<> ]+)', h)
    ctx = re.search(r'.{0,300}[Ll]icense.{0,300}', h, re.S)
    row('CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf',
        'https://arxiv.org/abs/0902.1702', 'READ',
        m.group(1) if m else 'NOT CHECKED - no licence URL found in the abs page',
        quote=re.sub(r'\s+', ' ', ctx.group(0))[:300] if ctx else None,
        note='arXiv licences are per submission; the default grants no redistribution right')
else:
    row('CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf',
        'https://arxiv.org/abs/0902.1702', 'NOT CHECKED', 'NOT CHECKED',
        note='HTTP %s' % code)

# ---- EMS Press, Jimbo ------------------------------------------------------
d = os.path.join(TMP, 'ems.html')
code = curl('https://ems.press/journals/prims/articles/1195183300', d)
if code == '200':
    h = text(d)
    m = re.search(r'(creativecommons\.org/licenses/[^"\'<> ]+)', h)
    ctx = re.search(r'.{0,250}(?:[Ll]icen[cs]e|©|[Cc]opyright).{0,250}', h, re.S)
    row('CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf',
        'https://ems.press/journals/prims/articles/1195183300', 'READ',
        m.group(1) if m else 'NOT CHECKED - no licence string located on the article page',
        quote=re.sub(r'\s+', ' ', ctx.group(0))[:300] if ctx else None)
else:
    row('CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf',
        'https://ems.press/journals/prims/articles/1195183300', 'NOT CHECKED',
        'NOT CHECKED', note='HTTP %s' % code)

# ---- Centre Mersenne, AIF --------------------------------------------------
d = os.path.join(TMP, 'aif.html')
code = curl('https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0/', d)
if code == '200':
    h = text(d)
    m = re.search(r'(creativecommons\.org/licenses/[^"\'<> ]+)', h)
    ctx = re.search(r'.{0,300}(?:[Ll]icen[cs]e|droits r|©).{0,300}', h, re.S)
    row('CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf',
        'https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0/', 'READ',
        m.group(1) if m else 'NOT CHECKED - no CC licence string on the item page',
        quote=re.sub(r'\s+', ' ', ctx.group(0))[:300] if ctx else None,
        note='the PDF title page prints "tous droits reserves"; see the page image row')
else:
    row('CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf',
        'https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0/', 'NOT CHECKED',
        'NOT CHECKED', note='HTTP %s' % code)

# ---- DLMF ------------------------------------------------------------------
d = os.path.join(TMP, 'dlmf_notices.html')
code = curl('https://dlmf.nist.gov/about/notices', d)
if code == '200':
    h = re.sub(r'<[^>]+>', ' ', text(d))
    ctx = re.search(r'.{0,400}(?:copyright|Copyright|reproduce|permission).{0,400}', h, re.S)
    row('DLMF sections 32.2 / 2.9 / 3.6 / 5.11 (html, tex)',
        'https://dlmf.nist.gov/about/notices', 'READ',
        'see quote - NIST notices page, verbatim',
        quote=re.sub(r'\s+', ' ', ctx.group(0))[:700] if ctx else None)
else:
    row('DLMF sections', 'https://dlmf.nist.gov/about/notices', 'NOT CHECKED',
        'NOT CHECKED', note='HTTP %s' % code)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
back = json.load(open(OUT, encoding='utf-8'))
assert len(back['rows']) == len(out['rows']) and back['rows'], 'readback failed'
print('wrote', OUT, '-', len(back['rows']), 'rows')
for r in back['rows']:
    print('%-52s %-12s %s' % (r['target'][:52], r['status'],
                              str(r['licence_as_printed'])[:70]))
print('READBACK OK')
