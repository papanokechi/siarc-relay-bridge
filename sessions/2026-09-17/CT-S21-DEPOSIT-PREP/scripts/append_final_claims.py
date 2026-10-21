# -*- coding: utf-8 -*-
"""Final CT-S21 claims: the detector defects, their controls, and the revised verdict."""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.basename(HERE) == 'CT-S21-DEPOSIT-PREP', HERE
D = os.path.join(HERE, 'DEPOSIT-READY.md')
C = os.path.join(HERE, 'outputs', 'item4_consistency.md')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


more = [
    ('S21-21', 'detector-defects',
     'Three defects in the CT-S21 consistency checker ITSELF, all found by reading its '
     'output rather than its exit code. '
     '(1) FALSE NEGATIVE FROM HARD WRAPPING: it reported the hedge "No published erratum '
     'is known to us" as missing. The sentence is present; it wraps across a blockquote '
     'line as "No published" / "> erratum is known to us". Trusting the checker would have '
     'prompted a repair to a sentence that was already correct. Phrase tests now run on '
     'text with blockquote markers stripped and whitespace collapsed. '
     '(2) A CHECK THAT COULD NO LONGER FAIL: the C4 test hardcoded the literal "Four '
     'points", so correcting the notice to "Seven" left it matching nothing and reporting '
     '0 enumerated items with no verdict - passing silently. This is the seventh '
     'amendment\'s failure mode arising inside the gate built to catch it. It now parses '
     'the count word, maps it to a number, compares it against the enumerated items, and '
     'asserts the sentence exists at all. '
     '(3) A SUBSTRING SEARCH WITH NO POLARITY: the pattern author-confirmed matched the '
     'notice\'s own sentence "nothing here is author-confirmed", which asserts the '
     'opposite. Negated contexts are now separated and listed, never silently dropped.',
     'INSPECTED', 'computation', None, 'scripts/item4_consistency.py', h(C)),
    ('S21-22', 'detector-controls',
     'Controls for the patched detectors. scripts/control_item4.py mutates the notice, runs '
     'the REAL checker, restores the file and verifies the restore by sha256 '
     '(f3ac6d41a1ed779b...). All three fired: a count word disagreeing with the enumerated '
     'items produced MISMATCH; a genuine non-negated "The authors have confirmed this" '
     'produced an asserting F7 hit; a re-wrapped hedge was still found. Had any failed to '
     'fire, the corresponding detector would have been certifying nothing.',
     'VERIFIED', 'computation', None, 'scripts/control_item4.py', h(C)),
    ('S21-23', 'verdict-round2',
     'VERDICT REVISED: the v1.3 notice is READY to deposit, subject to two deposit-day '
     'confirmations - that no author reply has arrived, so C3\'s sentence still holds, and '
     'the standing citation checklist in the notice\'s final section. All six M-items are '
     'resolved: M1 by a C1 scope limitation plus the C5 second pass, with Remark 3.2 added '
     'and Remarks 4.2, 6.7 and Theorem 3.1 excluded with stated reasons; M2, M3 and M4 by '
     'edit and write-back; M5 left uncorrected by operator ruling; M6 by a default-deny '
     'exclusion verified by effect. Final state: support rows agree, cited ids exist and '
     'are unsuperseded, C4 says seven and enumerates seven, F7 has 0 asserting hits and 1 '
     'negated, and both hedges are present.',
     'INSPECTED', 'file_inspection', None, D, h(D)),
]

p = os.path.join(HERE, 'claims.jsonl')
rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
have = {r['claim_id'] for r in rows}
assert not (have & {c[0] for c in more}), 'duplicate ids'
with open(p, 'a', encoding='utf-8') as f:
    for cid, tid, cl, lab, ev, dps, sc, oh in more:
        f.write(json.dumps({
            'claim_id': cid, 'task_id': tid, 'claim': cl, 'label': lab,
            'evidence_type': ev, 'dps': dps, 'reproducible': True,
            'script': sc, 'output_hash': oh,
        }, ensure_ascii=False) + '\n')

back = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
assert len(back) == len(rows) + len(more), 'readback count mismatch'
ids = [r['claim_id'] for r in back]
assert len(set(ids)) == len(ids), 'duplicate ids after append'
print('claims %d -> %d  (%s .. %s)' % (len(rows), len(back), ids[0], ids[-1]))
print('READBACK OK')
