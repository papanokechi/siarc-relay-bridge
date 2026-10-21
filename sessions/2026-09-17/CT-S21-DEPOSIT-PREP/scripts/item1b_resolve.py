# -*- coding: utf-8 -*-
"""CT-S21 item 1b - resolve the two sources that need more than a byte compare.

Zenodo: the API returns metadata, not the PDF. Read the version DOI and the
concept DOI separately (they are different objects), confirm the record is the
version the notice cites, and compare Zenodo's own recorded checksum against the
local file. Fetch the PDF itself and compare bytes.

DLMF: a URL is not a citation. Record the release version and date printed on
the page.
"""
import datetime
import hashlib
import json
import os
import re
import subprocess
import tempfile

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'outputs', 'item1b_resolve.json')
TMP = os.path.join(tempfile.gettempdir(), 'ct-s21-refetch')
TODAY = datetime.date.today().isoformat()


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def md5(p):
    h = hashlib.md5()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def curl(url, dest, headers=None):
    cmd = ['curl', '-sSL', '--max-time', '120', '-w', '%{http_code}', '-o', dest]
    for h in (headers or []):
        cmd += ['-H', h]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, (p.stdout or '').strip(), (p.stderr or '')[:300]


res = {'retrieved': TODAY}

# ---- Zenodo ---------------------------------------------------------------
api = os.path.join(TMP, 'companion-v1.2')
z = json.load(open(api, encoding='utf-8'))
meta = z.get('metadata', {})
zz = {
    'record_id': z.get('id'),
    'doi_version': z.get('doi') or meta.get('doi'),
    'conceptdoi': z.get('conceptdoi') or meta.get('conceptdoi'),
    'conceptrecid': z.get('conceptrecid'),
    'version_field': meta.get('version'),
    'title': meta.get('title'),
    'publication_date': meta.get('publication_date'),
    'license_legacy': meta.get('license'),
    'files': [],
}
for f in z.get('files', []):
    zz['files'].append({'key': f.get('key'), 'size': f.get('size'),
                        'checksum': f.get('checksum'),
                        'link': (f.get('links') or {}).get('self')})

# licences: the legacy field reports only one; the InvenioRDM view reports all
inv = os.path.join(TMP, 'companion-v1.2-inveniordm')
rc, code, err = curl('https://zenodo.org/api/records/20481592', inv,
                     ['Accept: application/vnd.inveniordm.v1+json'])
zz['rights_http'] = code
if code == '200':
    try:
        iv = json.load(open(inv, encoding='utf-8'))
        zz['rights'] = [r.get('id') or r.get('title')
                        for r in (iv.get('metadata', {}) or {}).get('rights', [])]
    except Exception as e:
        zz['rights'] = 'PARSE FAILED: %s' % e
else:
    zz['rights'] = 'NOT CHECKED (HTTP %s)' % code

# fetch the PDF itself and compare with the local copy
local = os.path.join(SESS, 'CT-R1-AUDIT', 'refs',
                     'vquad_resurgence_v1.2_zenodo-20481592.pdf')
zz['local_sha256'] = sha(local)
zz['local_md5'] = md5(local)
zz['local_bytes'] = os.path.getsize(local)
pdf_link = None
for f in zz['files']:
    if (f['key'] or '').lower().endswith('.pdf'):
        pdf_link = f['link']
        break
if pdf_link:
    dest = os.path.join(TMP, 'companion-v1.2.pdf')
    rc, code, err = curl(pdf_link, dest)
    zz['pdf_url'] = pdf_link
    zz['pdf_http'] = code
    if code == '200' and os.path.getsize(dest) > 0:
        zz['pdf_bytes'] = os.path.getsize(dest)
        zz['pdf_sha256'] = sha(dest)
        zz['pdf_matches_local'] = (zz['pdf_sha256'] == zz['local_sha256'])
    else:
        zz['pdf_status'] = 'NOT RE-FETCHED: HTTP %s %s' % (code, err)
else:
    zz['pdf_status'] = 'NOT RE-FETCHED: no PDF file entry in the record'
res['zenodo'] = zz

# ---- DLMF -----------------------------------------------------------------
html = open(os.path.join(TMP, 'DLMF-32.2'), encoding='utf-8', errors='replace').read()
d = {'url': 'https://dlmf.nist.gov/32.2'}
m = re.search(r'Version\s*([0-9.]+)', html)
d['version_raw'] = m.group(0) if m else None
m2 = re.search(r'Release\s*([0-9.]+)\s*of\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', html)
if m2:
    d['release'] = m2.group(1)
    d['release_date'] = m2.group(2)
else:
    m3 = re.search(r'([0-9]{4}-[0-9]{2}-[0-9]{2})', html)
    d['release'] = 'NOT FOUND in page text'
    d['release_date'] = m3.group(1) if m3 else 'NOT FOUND'
d['title'] = (re.search(r'<title>(.*?)</title>', html, re.S).group(1).strip()
              if re.search(r'<title>(.*?)</title>', html, re.S) else None)
ctx = re.search(r'.{200}Release.{200}', html, re.S)
d['context'] = re.sub(r'\s+', ' ', ctx.group(0)) if ctx else None
d['sha256'] = sha(os.path.join(TMP, 'DLMF-32.2'))
d['bytes'] = os.path.getsize(os.path.join(TMP, 'DLMF-32.2'))
res['dlmf'] = d

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=1, ensure_ascii=False)
back = json.load(open(OUT, encoding='utf-8'))
assert 'zenodo' in back and 'dlmf' in back, 'readback failed'
print('wrote', OUT)
print(json.dumps(back, indent=1, ensure_ascii=False)[:2600])
print('READBACK OK')
