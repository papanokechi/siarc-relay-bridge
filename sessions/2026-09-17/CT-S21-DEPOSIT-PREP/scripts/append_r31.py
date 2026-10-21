# -*- coding: utf-8 -*-
"""Append R31 and its claims."""
import hashlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUD = os.path.join(os.path.dirname(HERE), 'CT-R1-AUDIT', 'AUDIT.md')

spec = importlib.util.spec_from_file_location(
    'app', os.path.join(HERE, 'scripts', 'append_r27_and_p0.py'))
mod = importlib.util.module_from_spec(spec)
sys.argv = ['x']
try:
    spec.loader.exec_module(mod)
except SystemExit:
    pass

add = open(os.path.join(HERE, 'outputs', 'r31_section.md'), 'rb').read().replace(b'\r\n', b'\n')
before = open(AUD, 'rb').read()
if add in before:
    print('SKIP present')
else:
    open(AUD, 'ab').write(add)
    after = open(AUD, 'rb').read()
    assert after[:len(before)] == before and after[len(before):] == add
    assert not mod.bad_chars(after)
    print('AUDIT %d -> %d lines, clean' % (before.count(b'\n'), after.count(b'\n')))

fh = hashlib.sha256(open(os.path.join(HERE, 'DEPOSIT-FORM.md'), 'rb').read()).hexdigest()
CJ = os.path.join(HERE, 'claims.jsonl')
rows = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
n0 = len(rows)
have = {r['claim_id'] for r in rows}

NEW = [
    ('S21-55',
     'DEPOSIT SHAPE CHANGED ON OPERATOR RULING: the paper stays in the record. A2 previously '
     'read Deposit: the notice only, which would have made the concept DOI resolve to a record '
     'where the companion itself is absent. Zenodo New version carries previous files over by '
     'default, so keeping the paper is the default and notice-only would have required actively '
     'deleting vquad_resurgence.pdf from the draft. Verified that the held copy '
     'refs/vquad_resurgence_v1.2_zenodo-20481592.pdf is byte-identical to the deposited file: '
     '612719 bytes and md5 4d1e4d59072cad0db8edc86280af45a1, matching the record checksum field, '
     'so a hand re-upload could not alter the paper.'),
    ('S21-56',
     'THE NOTICE FILENAME BEGINS DRAFT- AND ZENODO PUBLISHES THE UPLOADED FILENAME. Sixth '
     'instance of author-addressed scaffolding inside the deposited object and the first that is '
     'not text: no scan over file contents could have found it, because the defect is in the name. '
     'A copy renamed vquad_resurgence_v1.3_correction_notice.md is staged under upload/ and '
     'verified byte-identical to the notice at sha256 '
     'c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c.'),
    ('S21-57',
     'TWO KNOCK-ONS OF THE SHAPE RULING, recorded in DEPOSIT-FORM.md. The record title should now '
     'probably stay byte-identical to v1.2 (new Option C, recommended), since options A and B were '
     'written for a notice-only record that would otherwise misdescribe itself, whereas with the '
     'paper retained the companion title still describes the record and citations resolve to a '
     'record titled as cited. And the sheet own pre-publish table wrongly required the form title '
     'to match the notice H1: the record title and the document H1 are different objects. Row '
     'corrected.'),
]
for cid, txt in NEW:
    assert cid not in have, cid
    rows.append(dict(claim_id=cid, task_id='CT-S21-DEPOSIT-PREP', claim=txt,
                     label='VERIFIED', evidence_type='file_inspection', dps=None,
                     reproducible=True, script='scripts/set_deposit_shape.py',
                     output_hash=fh))
with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
    for x in rows:
        f.write(json.dumps(x, ensure_ascii=False) + '\n')
back = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
assert len(back) == n0 + len(NEW)
print('claims %d -> %d  READBACK OK' % (n0, len(back)))
