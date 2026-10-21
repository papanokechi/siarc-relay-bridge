# -*- coding: utf-8 -*-
"""Append the macro-damage claims. Composed values only; no escape-bearing text
is embedded as a literal without doubling, and the file is re-read after write.
"""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJ = os.path.join(HERE, 'claims.jsonl')


def h(rel):
    return hashlib.sha256(open(os.path.join(HERE, rel), 'rb').read()).hexdigest()


NEW = [
    dict(claim_id='S21-35',
         claim=("DEFECT FOUND AND REPAIRED IN THE DEPOSIT OBJECT. "
                "DRAFT-COMPANION-v1.3-NOTICE.md carried four occurrences where a "
                "Python source literal turned backslash-t into a TAB, so the "
                "methodology note at lines 524-525 printed 'heta_inf', 'heta_0', "
                "'heta_t' instead of theta. One further site, backslash-b as "
                "BACKSPACE, cost a beta in outputs/item2_quotes.md line 156 "
                "('beta_exp = -1/(3*sqrt(3))'). All five repaired; both scanners "
                "now return zero."),
         label='VERIFIED', evidence_type='build',
         script='scripts/repair_macro_damage.py',
         output_file='outputs/item2_quotes.md'),
    dict(claim_id='S21-36',
         claim=("The R25 scanner MISSED these because it tested only for "
                "backslash-r, -a, -v, -f, omitting -t and -b, which are precisely "
                "the escapes that consume the commonest macros here (theta, tau, "
                "times, beta). Its first fix then under-reported 4 as 2, because "
                "an at-line-start guard added to avoid flagging TAB indentation "
                "suppressed real hits at the start of wrapped prose lines - the "
                "S17-22 'could not fire' shape again, inside the detector written "
                "in response to it. Guard replaced: decisive tails flag "
                "regardless of position."),
         label='VERIFIED', evidence_type='build',
         script='scripts/scan_macro_damage.py',
         output_file='outputs/refs_attribution.md'),
    dict(claim_id='S21-37',
         claim=("DEPOSIT-WALKTHROUGH.md prepared: pre-flight commands, the two "
                "deposit-day confirmations, the four-row citation pass, the "
                "refs/ non-upload rule with its per-file licence basis, Zenodo "
                "new-version mechanics against concept DOI 10.5281/zenodo.20455089 "
                "and v1.2 version DOI 10.5281/zenodo.20481592, five abort "
                "conditions, post-publish record steps, and the Wong-Li buy vs "
                "NOT OBTAINED decision. NOTHING EXECUTED; all steps are operator "
                "actions."),
         label='INSPECTED', evidence_type='file_inspection',
         script='n/a - document',
         output_file='DEPOSIT-WALKTHROUGH.md'),
]

lines = io.open(CJ, encoding='utf-8').read().splitlines()
rows = [json.loads(x) for x in lines if x.strip()]
n0 = len(rows)
have = {r['claim_id'] for r in rows}
for c in NEW:
    assert c['claim_id'] not in have, 'duplicate %s' % c['claim_id']
    c['task_id'] = 'CT-S21-DEPOSIT-PREP'
    c['dps'] = None
    c['reproducible'] = True
    c['output_hash'] = h(c['output_file'])
    rows.append(c)

with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
    for x in rows:
        f.write(json.dumps(x, ensure_ascii=False) + '\n')

back = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
assert len(back) == n0 + len(NEW), 'count %d -> %d' % (n0, len(back))
got = {x['claim_id']: x for x in back}
for c in NEW:
    assert got[c['claim_id']]['claim'] == c['claim']
    assert got[c['claim_id']]['output_hash'] == c['output_hash']
print('claims %d -> %d (+%d)' % (n0, len(back), len(NEW)))
print('READBACK OK')
