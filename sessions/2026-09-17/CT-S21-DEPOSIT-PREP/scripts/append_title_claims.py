# -*- coding: utf-8 -*-
"""Final record for the title application."""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJ = os.path.join(HERE, 'claims.jsonl')
NOTICE = os.path.join(os.path.dirname(HERE), 'CT-R1-AUDIT',
                      'DRAFT-COMPANION-v1.3-NOTICE.md')
nh = hashlib.sha256(open(NOTICE, 'rb').read()).hexdigest()

NEW = [
    ('S21-53',
     'DRAFT SCAFFOLDING REMOVED AND TITLE APPLIED, option A. The notice H1 is now the '
     'v1.2 record title verbatim followed by an em dash and v1.3 correction notice, and '
     'the STATUS: DRAFT FOR THE OPERATOR block is gone; zero occurrences of DRAFT remain '
     'in the object. Applied rather than left open because a local file edit is reversible '
     'and the prior bytes are kept at DRAFT-COMPANION-v1.3-NOTICE.md.bak-a9a938f7. FINAL '
     'sha256 c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c, 35918 bytes. '
     'Gates re-run on these bytes: item4_consistency clean, all three controls fire, macro '
     'scan 0, no control characters.'),
    ('S21-54',
     'THE TITLE SCRIPT ASCII-FIED THE TITLE, caught immediately after applying it. '
     'apply_title.py carried its two candidate titles as Python literals typed by hand, '
     'rendering Painleve without the acute accent and an ASCII hyphen for the em dash - so '
     'option A produced an H1 that did NOT match the v1.2 record title, which is the exact '
     'form-versus-record drift DEPOSIT-FORM.md was written to prevent, committed by the tool '
     'written to prevent it. Repaired by rebuilding the H1 from the stored record metadata, '
     'and apply_title.py now derives BOTH options from that record rather than from retyped '
     'literals; option B verified to produce the accented form.'),
]

rows = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
n0 = len(rows)
have = {r['claim_id'] for r in rows}
for cid, txt in NEW:
    assert cid not in have, cid
    rows.append(dict(claim_id=cid, task_id='CT-S21-DEPOSIT-PREP', claim=txt,
                     label='VERIFIED', evidence_type='build', dps=None,
                     reproducible=True, script='scripts/apply_title.py',
                     output_hash=nh))
with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
    for x in rows:
        f.write(json.dumps(x, ensure_ascii=False) + '\n')
back = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
assert len(back) == n0 + 2
print('claims %d -> %d  READBACK OK' % (n0, len(back)))
print('notice sha256 %s' % nh)
print('backup of prior bytes exists:',
      os.path.exists(NOTICE + '.bak-a9a938f7'))
