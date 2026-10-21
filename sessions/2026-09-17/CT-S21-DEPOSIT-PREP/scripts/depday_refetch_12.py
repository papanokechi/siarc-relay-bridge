# -*- coding: utf-8 -*-
"""Correction to rows 1 and 2 of the deposit-day pass.

The first run recorded NOT RE-FETCHED for van der Put-Saito and Jimbo on the
assumption that paywalling left no route. REFS-MANIFEST.md lines 175 and 177
record working URLs for both. Paywalled-to-redistribute is not the same as
unreachable-to-fetch, and the rule asks for a re-fetch, not for a licence
judgement. So both are re-fetched here and compared byte-for-byte with the held
copies.
"""
import hashlib
import io
import json
import os
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
UA = {'User-Agent': 'siarc-relay-bridge/CT-S21 deposit-day citation pass'}

ROWS = [
    ('row1_vdps',
     'https://aif.centre-mersenne.org/item/AIF_2009__59_7_2611_0.pdf',
     os.path.join(SESS, 'CT-R1-AUDIT', 'refs',
                  'vanderPut-Saito-AIF-2009-59-7-2611.pdf')),
    ('row2_jimbo',
     'https://ems.press/doi/pdf/10.2977/prims/1195183300',
     os.path.join(SESS, 'CT-S9-PVPARAMS', 'refs', 'jimbo_1982_prims.pdf')),
]

p = os.path.join(HERE, 'outputs', 'depday_citation_pass.json')
rep = json.load(io.open(p, encoding='utf-8'))

for key, url, local in ROWS:
    held = hashlib.sha256(open(local, 'rb').read()).hexdigest()
    row = rep[key]
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=180) as r:
            data = r.read()
        fresh = hashlib.sha256(data).hexdigest()
        # keep the bytes only long enough to hash them; refs/ is not re-written
        with tempfile.NamedTemporaryFile(delete=True) as tf:
            tf.write(data)
        row['refetch'] = 'OK'
        row['refetch_url'] = url
        row['refetch_bytes'] = len(data)
        row['refetch_sha256'] = fresh
        row['sha256_unchanged_vs_held_copy'] = (fresh == held)
        row.pop('refetch_reason', None)
        print('%-12s re-fetched %8d bytes  sha256 %s  unchanged=%s'
              % (key, len(data), fresh[:16], fresh == held))
    except Exception as e:                                # noqa: BLE001
        row['refetch'] = 'NOT RE-FETCHED'
        row['refetch_url'] = url
        row['refetch_reason'] = '%s: %s' % (type(e).__name__, e)
        row['sha256_unchanged_vs_held_copy'] = None
        print('%-12s NOT RE-FETCHED: %s: %s' % (key, type(e).__name__, e))

with io.open(p, 'w', encoding='utf-8') as f:
    json.dump(rep, f, indent=1, ensure_ascii=False)
back = json.load(io.open(p, encoding='utf-8'))
assert back == rep, 'READBACK MISMATCH'
for key, _, _ in ROWS:
    assert 'refetch_url' in back[key]
print('readback OK')
