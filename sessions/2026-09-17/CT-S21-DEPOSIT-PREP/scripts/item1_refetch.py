# -*- coding: utf-8 -*-
"""CT-S21 item 1 - re-fetch every external source the notice cites.

Downloads to a temp directory OUTSIDE the repository: a re-fetch is a
verification, not an acquisition, and copying more third-party bytes into the
tree would enlarge the population under the licence hold.

Records URL, retrieval date, byte size, sha256, and whether the bytes match the
local copy. A source that cannot be re-fetched is recorded NOT RE-FETCHED with
the reason. No cached copy is ever silently substituted.
"""
import datetime
import hashlib
import json
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'outputs', 'item1_refetch.json')
TMP = os.path.join(tempfile.gettempdir(), 'ct-s21-refetch')
os.makedirs(TMP, exist_ok=True)

TODAY = datetime.date.today().isoformat()

SOURCES = [
    {
        'key': 'vdPS-AIF',
        'cite': "van der Put & Saito, Ann. Inst. Fourier 59 (2009) 7, 2611-2667",
        'url': 'https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0.pdf',
        'url_provenance': 'CONSTRUCTED from the Centre Mersenne item id encoded in the '
                          'local filename vanderPut-Saito-AIF-2009-59-7-2611.pdf; no URL '
                          'was recorded in the tree. Confirmed only if the bytes match.',
        'local': 'CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf',
    },
    {
        'key': 'vdPS-arXiv-v5',
        'cite': 'arXiv:0902.1702v5, p. 34',
        'url': 'https://arxiv.org/pdf/0902.1702v5',
        'url_provenance': 'arXiv identifier printed in the notice.',
        'local': 'CT-S16-MEMBERSHIP-C/refs/vdPS-arXiv-0902.1702v5.pdf',
    },
    {
        'key': 'Jimbo-PRIMS',
        'cite': 'Jimbo, Publ. RIMS 18 (1982), p. 1152',
        'url': 'https://ems.press/doi/pdf/10.2977/prims/1195183300',
        'url_provenance': 'RECORDED in the session tree (the URL used at acquisition).',
        'local': 'CT-S9-PVPARAMS/refs/jimbo_1982_prims.pdf',
    },
    {
        'key': 'companion-v1.2',
        'cite': 'V_quad companion v1.2 (Zenodo)',
        'url': 'https://zenodo.org/api/records/20481592',
        'url_provenance': 'Zenodo record id encoded in the local filename '
                          'vquad_resurgence_v1.2_zenodo-20481592.pdf.',
        'local': 'CT-R1-AUDIT/refs/vquad_resurgence_v1.2_zenodo-20481592.pdf',
        'api': True,
    },
    {
        'key': 'DLMF-32.2',
        'cite': 'DLMF section 32.2 (PV normalisation cited by v1.2)',
        'url': 'https://dlmf.nist.gov/32.2',
        'url_provenance': 'DLMF section number printed in the notice checklist.',
        'local': None,
        'html': True,
    },
]


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def fetch(url, dest):
    p = subprocess.run(
        ['curl', '-sSL', '--max-time', '120', '-w', '%{http_code}',
         '-o', dest, url],
        capture_output=True, text=True)
    return p.returncode, (p.stdout or '').strip(), (p.stderr or '').strip()


results = []
for s in SOURCES:
    dest = os.path.join(TMP, s['key'].replace('/', '_'))
    rc, code, err = fetch(s['url'], dest)
    rec = dict(s)
    rec['retrieved'] = TODAY
    rec['http_code'] = code
    rec['curl_rc'] = rc
    if rc != 0 or not os.path.exists(dest) or os.path.getsize(dest) == 0:
        rec['status'] = 'NOT RE-FETCHED'
        rec['reason'] = 'curl rc=%s http=%s %s' % (rc, code, err[:200])
        results.append(rec)
        continue
    rec['bytes'] = os.path.getsize(dest)
    rec['sha256'] = sha(dest)
    if code not in ('200', ''):
        rec['status'] = 'NOT RE-FETCHED'
        rec['reason'] = 'HTTP %s' % code
        results.append(rec)
        continue
    if s.get('local'):
        lp = os.path.join(SESS, s['local'].replace('/', os.sep))
        if os.path.exists(lp):
            rec['local_bytes'] = os.path.getsize(lp)
            rec['local_sha256'] = sha(lp)
            rec['matches_local'] = (rec['local_sha256'] == rec['sha256'])
        else:
            rec['matches_local'] = None
            rec['reason'] = 'local copy absent'
    rec['status'] = 'RE-FETCHED'
    # keep a small head of the body for HTML/API sources so the record is checkable
    if s.get('api') or s.get('html'):
        with open(dest, 'rb') as f:
            rec['head'] = f.read(400).decode('utf-8', 'replace')
    results.append(rec)

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump({'retrieved': TODAY, 'temp_dir': TMP, 'sources': results},
              f, indent=1, ensure_ascii=False)

back = json.load(open(OUT, encoding='utf-8'))
assert len(back['sources']) == len(SOURCES), 'readback count mismatch'
print('wrote', OUT)
for r in back['sources']:
    print('%-16s %-16s http=%-4s bytes=%-9s match_local=%s'
          % (r['key'], r['status'], r.get('http_code'), r.get('bytes'),
             r.get('matches_local')))
    if r['status'] != 'RE-FETCHED':
        print('       reason:', r.get('reason'))
print('READBACK OK')
