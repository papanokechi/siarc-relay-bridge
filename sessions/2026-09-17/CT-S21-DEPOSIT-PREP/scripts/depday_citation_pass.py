# -*- coding: utf-8 -*-
"""Deposit-day citation pass (walkthrough A1.2, notice final section rows 1-4).

Fetch/hash only. The page images this renders are then re-read BY EYE; the text
layer is never the evidence for a quoted passage.

Anything that cannot be re-fetched is recorded NOT RE-FETCHED with the reason.
No cached copy is silently substituted.
"""
import hashlib
import io
import json
import os
import re
import urllib.request

import fitz

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
PAGES = os.path.join(HERE, 'pages')
UA = {'User-Agent': 'siarc-relay-bridge/CT-S21 deposit-day citation pass'}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def get(url, dest=None):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    if dest:
        open(dest, 'wb').write(data)
        assert os.path.getsize(dest) == len(data), 'short write %s' % dest
    return data


rep = {}

# ---- Row 1: van der Put & Saito, AIF 59 (2009) ------------------------------
vdps = os.path.join(SESS, 'CT-R1-AUDIT', 'refs',
                    'vanderPut-Saito-AIF-2009-59-7-2611.pdf')
d = fitz.open(vdps)
first_printed = 2611                      # volume page of PDF page index 0
wanted = [2634, 2635, 2637]
imgs = []
for pp in wanted:
    idx = pp - first_printed
    page = d[idx]
    stamp = re.sub(r'\s+', ' ', page.get_text()).strip()
    out = os.path.join(PAGES, 'vdps_p%d.png' % pp)
    page.get_pixmap(dpi=200).save(out)
    # confirm the page really is the printed page claimed, from its own text
    ok = str(pp) in stamp[:120] or str(pp) in stamp[-120:]
    imgs.append({'printed_page': pp, 'pdf_index': idx, 'image': os.path.basename(out),
                 'page_number_visible_in_text': ok})
d.close()
rep['row1_vdps'] = {
    'source': 'van der Put & Saito, Ann. Inst. Fourier 59 (2009) 2611-2667',
    'refetch': 'NOT RE-FETCHED',
    'refetch_reason': ('paywalled and the title page prints "tous droits '
                       'reserves"; the held copy is the one previously '
                       'obtained. Integrity checked by sha256 instead.'),
    'local_file': os.path.relpath(vdps, SESS),
    'sha256': sha(vdps),
    'pages_rendered_for_eye_read': imgs,
}

# ---- Row 2: Jimbo, Publ. RIMS 18 (1982), p. 1152 ----------------------------
jim = os.path.join(SESS, 'CT-S9-PVPARAMS', 'refs', 'jimbo_1982_prims.pdf')
d = fitz.open(jim)
idx = 16                                   # established in CT-S9 as printed 1152
page = d[idx]
flat = re.sub(r'\s+', ' ', page.get_text())
out = os.path.join(PAGES, 'jimbo_p1152.png')
page.get_pixmap(dpi=200).save(out)
d.close()
rep['row2_jimbo'] = {
    'source': 'Jimbo, Publ. RIMS 18 (1982), p. 1152',
    'refetch': 'NOT RE-FETCHED',
    'refetch_reason': 'held copy; no open re-fetch route recorded for this scan.',
    'local_file': os.path.relpath(jim, SESS),
    'sha256': sha(jim),
    'pdf_index': idx,
    'page_1152_visible_in_text': '1152' in flat,
    'image': os.path.basename(out),
}

# ---- Row 3: companion v1.2 from Zenodo --------------------------------------
meta_p = os.path.join(HERE, 'outputs', 'depday_zenodo_20481592.json')
row3 = {'source': 'V_quad companion v1.2, Zenodo record 20481592'}
try:
    raw = get('https://zenodo.org/api/records/20481592')
    open(meta_p, 'wb').write(raw)
    m = json.loads(raw.decode('utf-8'))
    row3['refetch'] = 'OK'
    row3['metadata_sha256'] = hashlib.sha256(raw).hexdigest()
    row3['doi'] = m.get('doi')
    row3['conceptdoi'] = m.get('conceptdoi')
    row3['version'] = (m.get('metadata') or {}).get('version')
    row3['title'] = (m.get('metadata') or {}).get('title')
    files = m.get('files') or []
    row3['files'] = [{'key': f.get('key'),
                      'size': f.get('size'),
                      'checksum': f.get('checksum')} for f in files]
except Exception as e:                                    # noqa: BLE001
    row3['refetch'] = 'NOT RE-FETCHED'
    row3['refetch_reason'] = '%s: %s' % (type(e).__name__, e)

local_v12 = os.path.join(SESS, 'CT-R1-AUDIT', 'refs',
                         'vquad_resurgence_v1.2_zenodo-20481592.pdf')
row3['local_pdf'] = os.path.relpath(local_v12, SESS)
row3['local_sha256'] = sha(local_v12)
row3['local_sha256_matches_manifest'] = row3['local_sha256'].startswith('a5d9e264')
rep['row3_companion_v12'] = row3

# ---- Row 4: DLMF 32.2 --------------------------------------------------------
row4 = {'source': 'DLMF section 32.2'}
try:
    html = get('https://dlmf.nist.gov/32.2',
               os.path.join(HERE, 'outputs', 'depday_dlmf_32.2.html')).decode(
                   'utf-8', 'replace')
    row4['refetch'] = 'OK'
    row4['sha256'] = hashlib.sha256(html.encode('utf-8')).hexdigest()
    v = re.search(r'Version\s+([0-9.]+)', html)
    dt = re.search(r'Release date\s*([0-9]{4}-[0-9]{2}-[0-9]{2})', html) \
        or re.search(r'([0-9]{4}-[0-9]{2}-[0-9]{2})', html)
    row4['release_version'] = v.group(1) if v else 'NOT FOUND'
    row4['release_date'] = dt.group(1) if dt else 'NOT FOUND'
except Exception as e:                                    # noqa: BLE001
    row4['refetch'] = 'NOT RE-FETCHED'
    row4['refetch_reason'] = '%s: %s' % (type(e).__name__, e)
rep['row4_dlmf'] = row4

p = os.path.join(HERE, 'outputs', 'depday_citation_pass.json')
with io.open(p, 'w', encoding='utf-8') as f:
    json.dump(rep, f, indent=1, ensure_ascii=False)
back = json.load(io.open(p, encoding='utf-8'))
assert back == rep, 'READBACK MISMATCH'
print(json.dumps(rep, indent=1, ensure_ascii=False)[:3000])
print('\nreadback OK ->', p)
