"""R20: amend S17-09 to carry the sign convention, and append the CT-S20B
adjudication claims.  Backs up first, then reads back and fails loudly.
"""
import json
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(BASE)
CL = os.path.join(SESS, 'CT-S17-TRACEFREE-NORM', 'claims.jsonl')
BAK = CL + '.bak-r20'

H1 = '44782d21690243f817a8efec1b85d1d737d78c60b3bb4556664d695ef922f77e'
H2 = 'b7e7eb792ae326a9e449c0a35b2e45fa03b585dc5ad942a4b892d5fe7439d878'
H2B = '00eacc7e8876012366c27590266a4f9c5acaebeabd2ce992ed74e1aabab34929'
H3 = 'af73261b0668fc22c7b9ecc9e893d41b3c44f91f456df9babad1bed6bf923b6c'
T = 'adjudicate-CT-S20B'

S17_09_NEW = (
    "A rank-2 first-order system Y' = N Y admits TWO scalar reductions, the ODEs "
    "satisfied by its two components. Derived generically by elimination with no "
    "formula assumed: route 1 (for y1) has P = -tr N - n12'/n12, route 2 (for y2) "
    "has P = -tr N - n21'/n21. SIGN CONVENTION: route 1 MINUS route 2 equals "
    "+d/dz log(c/b), i.e. P_route1 - P_route2 = c'/c - b'/b. PROVISO: the "
    "route difference is d/dz log(n21/n12) in general, and equals d/dz log(c/b) "
    "only because the convention N = -A/D divides both off-diagonal entries by "
    "the same D. Both routes are correct; neither is \"the\" scalar equation of "
    "the connection. [Sign convention and proviso added at R20 on CT-S20B; the "
    "prior text, which stated the magnitude only, is in claims.jsonl.bak-r20.]"
)

NEW = [
    ("S17-20", "CT-S20B-COMPONENT, isolated from CT-S16/S17/S18/S19 and from both "
     "adjudication scripts, re-derived the two scalar reductions from a generic "
     "Y' = N Y by elimination and obtained P_b - P_c = d/dz log(n21/n12), equal to "
     "d/dz log(c/b) under the N = -A/D convention, exact. It added two things S17-09 "
     "lacked: the orientation, b-route MINUS c-route carrying the + sign, and the "
     "proviso that identifying n21/n12 with c/b uses the common denominator D. Its "
     "controls: one would have fired had the difference collapsed to zero "
     "identically, one had the routes differed outside the logarithmic-derivative "
     "term; neither fired.",
     "PROVEN", "computation", 40, "CT-S20B-COMPONENT/scripts/task1.py", H1),
    ("S17-21", "At the point supplied to CT-S20B, the b-route reduction reproduces "
     "System C exactly: P_b - P_C = 0 and Q_b - Q_C = 0 by cancel over "
     "Q(i,sqrt3,sqrt11), with numeric residuals 2.0e-177 and 2.5e-175 at dps 40 over "
     "four sample z. The c-route misses by exactly P_c - P_C = -1/(z-q), numerically "
     "1.45, with Q_c - Q_C nonzero, numerically 8.1. This independently confirms "
     "S17-10 by a different exact mechanism, one that never compares radicals with "
     "==. Control: the same test rejected a deliberately wrong point q -> q+1.",
     "PROVEN", "computation", 40, "CT-S20B-COMPONENT/scripts/task2.py", H2),
    ("S17-22", "The c-route residual -1/(z-q) is the simple zero of c(z) = -(z-q)/(q-1) "
     "at z = q, which is what the route difference d/dz log(c/b) predicts when b is "
     "constant at the point. Because -1/(z-q) has no zero in z, a comparison made "
     "against the c-route returns a mismatch at every sample point and at every "
     "parameter value: CT-S18's test could not have returned a match under any "
     "circumstance. CT-S20B reached the residual without being told to expect it.",
     "PROVEN", "computation", 40, "CT-S20B-COMPONENT/scripts/task2.py", H2),
    ("S17-23", "thi = -2 - sqrt(3)/9 as supplied is consistent with System C's local "
     "data at infinity. The leading matrix at infinity is diag(t/2, -t/2) with "
     "distinct entries, so the rate +t/2 branch has eigenvector e1 + O(1/z) and its "
     "first component carries exponent N11_1 = thi/2 with no shift for any thi; "
     "System C demands -1 - sqrt(3)/18, forcing thi = -2 - sqrt(3)/9 with residual 0 "
     "at dps 40. The subdominant branch was predicted from ord_inf(N12) = 2 and "
     "matched exactly. SCOPE: since S17-21 gives P_b = P_C and Q_b = Q_C identically, "
     "agreement of every local datum follows; this is corroboration by a second "
     "route, not an independent constraint.",
     "PROVEN", "computation", 40, "CT-S20B-COMPONENT/scripts/task2b.py", H2B),
    ("S17-24", "ADJUDICATION of CT-S20B-COMPONENT: verdict CORRECT, tasks 1, 2, 2b and "
     "3 all ADOPTED. The contested step, which scalar reduction to compare, is now "
     "resolved independently of both CT-S18 and CT-S19 and of the adjudication "
     "scripts, so the C3 moduli-space membership support row moves to cold. LIMITS, "
     "recorded: CT-S20B was not independent of inputs.md, which this agent wrote, "
     "and it was handed the point rather than locating its own, so it is not a "
     "second independent location of a point of U_0; CT-S19 is that. It tested the "
     "disputed step and nothing else, which is what it was commissioned to do.",
     "STRUCTURAL", "file_inspection", None,
     "CT-S20B-COMPONENT/VERIFY-S20B.md", H3),
    ("S17-25", "Two method defects self-caught inside CT-S20B, recorded as findings "
     "about method and NOT adopted as claims about the mathematics: (i) keeping thi "
     "symbolic inside the scalar reduction and reading heads at infinity is unsound "
     "because deg_z b drops from 1 to 0 at exactly the thi of interest, so the heads "
     "are discontinuous there; (ii) mu(+) - mu(-) is not gauge-invariant between the "
     "system and a scalar reduction, the branches carrying powers 0 and -2. Defect "
     "(ii) returned the verdict inconsistent and the value thi = sqrt(3)/9, wrong by "
     "exactly the shift 2, and was caught by an arithmetic control: the scalar "
     "exponents must sum to -P1, and they summed to -1 against System C's -2. This "
     "is the converse of the recurring family in the record: a control that DID fire, "
     "on a real defect, inside a check that would otherwise have returned a confident "
     "wrong answer.",
     "PROVEN", "computation", 40, "CT-S20B-COMPONENT/scripts/task2b.py", H2B),
    ("S17-26", "S17-09 amended in place at R20, per operator review #18, to carry the "
     "sign convention (route 1 minus route 2 equals +d/dz log(c/b)) and the "
     "denominator proviso, so that a future reader cannot rederive the orientation "
     "backwards. Label unchanged at PROVEN; the mathematics is unchanged; the prior "
     "text is preserved verbatim in CT-S17-TRACEFREE-NORM/claims.jsonl.bak-r20 and "
     "quoted in AUDIT.md section R20.",
     "STRUCTURAL", "file_inspection", None,
     "CT-S17-TRACEFREE-NORM/claims.jsonl.bak-r20", None),
]

with open(CL, encoding='utf-8') as f:
    rows = [json.loads(l) for l in f if l.strip()]
before = len(rows)
shutil.copyfile(CL, BAK)
assert os.path.exists(BAK), 'backup not written'

old_09 = None
for r in rows:
    if r['claim_id'] == 'S17-09':
        old_09 = r['claim']
        r['claim'] = S17_09_NEW
assert old_09 is not None, 'S17-09 not found'

have = {r['claim_id'] for r in rows}
for cid, claim, label, ev, dps, script, h in NEW:
    assert cid not in have, 'duplicate id ' + cid
    have.add(cid)
    rows.append({"claim_id": cid, "task_id": T, "claim": claim, "label": label,
                 "evidence_type": ev, "dps": dps, "reproducible": True,
                 "script": script, "output_hash": h})

with open(CL, 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# read back
with open(CL, encoding='utf-8') as f:
    back = [json.loads(l) for l in f if l.strip()]
ids = [r['claim_id'] for r in back]
assert len(back) == before + len(NEW), 'count wrong: %d -> %d' % (before, len(back))
assert len(ids) == len(set(ids)), 'duplicate ids after write'
assert 'SIGN CONVENTION' in [r for r in back if r['claim_id'] == 'S17-09'][0]['claim']
for cid, *_ in NEW:
    assert cid in ids, 'missing ' + cid
print('OLD S17-09:\n' + old_09)
print('\nrows %d -> %d, appended %s' % (before, len(back), ', '.join(c for c, *_ in NEW)))
print('backup:', BAK)
print('READBACK OK')
