# -*- coding: utf-8 -*-
"""M6 - amend R1-107 in place (R20 precedent) and file the CT-S21 M-round claims."""
import hashlib
import json
import os
import shutil

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.basename(HERE) == 'CT-S21-DEPOSIT-PREP', HERE
SESS = os.path.dirname(HERE)
AUD = os.path.join(SESS, 'CT-R1-AUDIT', 'claims.jsonl')

NEW = ('AMENDED AT CT-S21 (M6). The original text claimed that after the R21 '
       '.gitignore, zero third-party bytes would be staged by a commit. That was '
       'FALSE, and false because the patterns covered refs/ and pages/ only: '
       'page images and saved pages also live in coldpackets/, in session roots '
       'and in outputs/. Re-derived in a separate invocation, '
       '"git add -n -A -- sessions/2026-09-17" staged 411 paths, 17 of them '
       'image/pdf/html, of which NINE were third party (vdps_p2634.png, '
       'vdps_p2635.png, jimbo_p1152.png, four CT-S10-COLDREAD2/dlmf_5_11*.html, '
       'and two CT-S9-PVPARAMS jimbo page images). The CT-S18/CT-S19 packet '
       'images were already excluded, sitting under packet/pages/. Closed at '
       'CT-S21 by extending .gitignore to default-deny **/*.png, *.jpg, *.jpeg, '
       '*.pdf, *.html across the session tree, verified BY EFFECT with '
       '"git add -n": media stageable fell 17 -> 0, non-media 411 -> 399, with '
       'nothing actually staged. The default-deny also excludes the operator own '
       'CC-BY-4.0 companion pages and theorem.pdf, deliberately: re-admit by name '
       'after each REFS-MANIFEST.md row is checked.')

rows = [json.loads(l) for l in open(AUD, encoding='utf-8') if l.strip()]
tgt = [r for r in rows if r['claim_id'] == 'R1-107']
assert len(tgt) == 1, 'expected exactly one R1-107, got %d' % len(tgt)
assert 'AMENDED AT CT-S21' not in tgt[0]['claim'], 'already amended'
shutil.copyfile(AUD, AUD + '.bak-s21m6')
tgt[0]['claim_before_s21'] = tgt[0]['claim']
tgt[0]['claim'] = NEW
tgt[0]['amended_in'] = 'CT-S21-DEPOSIT-PREP'
with open(AUD, 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

chk = [json.loads(l) for l in open(AUD, encoding='utf-8') if l.strip()]
r = next(x for x in chk if x['claim_id'] == 'R1-107')
assert r['claim'].startswith('AMENDED AT CT-S21') and r.get('claim_before_s21')
print('R1-107 amended in place; .bak-s21m6 written')

# --- M-round claims -------------------------------------------------------
OUT = os.path.join(HERE, 'claims.jsonl')


def h(rel):
    p = os.path.join(HERE, rel) if not os.path.isabs(rel) else rel
    assert os.path.exists(p), rel
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


NOTICE = os.path.join(SESS, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md')
GI = os.path.join(SESS, '.gitignore')

more = [
    ('S21-13', 'm1-theta-survives',
     'The formal monodromy exponents theta_1 = theta_2 = 0 SURVIVE C1. They record the '
     'difference of the local exponents at each finite singularity, and both exponents are '
     '0 by the double root of the indicial equation rho^2 = 0 - which is precisely what C1 '
     'establishes and what v1.2 Theorem 3.1(i) had already computed and certified '
     'numerically at dps=150. Apparency is not required for theta = 0; theta = 0 is exactly '
     'the resonant case in which logarithms occur. Consequently every passage of v1.2 whose '
     'operative premise is theta_1 = theta_2 = 0 is untouched by this notice, including C2, '
     'which relies on those values.',
     'STRUCTURAL', 'file_inspection', None, 'page images of v1.2 printed pp. 5, 6; ' + NOTICE, h(NOTICE)),
    ('S21-14', 'm1-remark42-excluded',
     'Remark 4.2 does NOT belong in C5. Its operative premise is theta_1 = theta_2 = 0, not '
     'apparency: what degenerates is the Jimbo connection formula, through gamma functions '
     'at the formal monodromy exponents. The phrase "(apparent singularities)" is a '
     'parenthetical gloss. Decisive internal evidence: v1.2 states the SAME fact without any '
     'gloss at section 7.1 item 3, "The standard Jimbo connection formula degenerates at '
     'theta_1 = theta_2 = 0, leaving no known closed-form expression." Since theta = 0 '
     'survives C1 (S21-13), the PSLQ-null explanation is unaffected.',
     'STRUCTURAL', 'file_inspection', None, 'page images of v1.2 printed pp. 7, 10', h(NOTICE)),
    ('S21-15', 'm1-remark67-excluded',
     'Remark 6.7 does NOT belong in C5, and not for the same reason as Remark 4.2. It rests '
     'on Theorem 3.1(ii), not on apparency and not on the theta values: the printed '
     'parenthetical glosses "apparent" as "trivial local monodromy ON M_11 = V_quad; Theorem '
     '3.1", and the consequence drawn is likewise about M_11 ("by any monodromy-based '
     'argument"). Theorem 3.1(ii) is unadjudicated in this work, so no verdict is recorded '
     'and the passage is listed among the deliberate exclusions with its reason.',
     'STRUCTURAL', 'file_inspection', None, 'page image of v1.2 printed p. 10', h(NOTICE)),
    ('S21-16', 'm1-remark32-included',
     'Remark 3.2 DOES belong in C5. Verbatim from the page image: "the monodromy at the '
     'finite singularities is exactly trivial by algebra" - stated flatly, WITHOUT the M_11 '
     'qualifier that Theorem 3.1(ii) carries, so it asserts apparency. Per the operator '
     'ruling the C5 line records the dependency only; this notice takes no position on '
     'whether the sentence is correct, not having checked it.',
     'INSPECTED', 'file_inspection', None, 'page image of v1.2 printed p. 6', h(NOTICE)),
    ('S21-17', 'm1-c1-scope',
     'C1 now carries a scope limitation (point 3): the general assertion in Remark 2.2 is '
     'false, the computation in section 3 is not affected, and section 3 already exhibits '
     'the unipotent monodromy [[1, 2*pi*i],[0,1]] that refutes the general claim. C5 records '
     'the second pass, adds the Remark 3.2 row, and states the three deliberate exclusions '
     'with their reasons. No verdict is offered on Theorem 3.1(ii).',
     'INSPECTED', 'file_inspection', None, NOTICE, h(NOTICE)),
    ('S21-18', 'm2-m4-fixed',
     'M2: C3 letter-status placeholder replaced - the authors have now been notified by '
     'email, no reply had been received when the notice was finalised, and the sentence '
     '"it had not been sent" no longer appears anywhere in the notice (verified by readback). '
     'M4: "Four points must accompany this table" corrected to "Seven", the enumerated items '
     'having been counted programmatically at seven. M3: review="cold" written back to S4-06 '
     '(CT-S4-FORMAL-TYPE) and S5B-C6 (CT-S5B-COVER) with review_note and .bak-s21m3, under '
     'the R20 in-place precedent.',
     'INSPECTED', 'computation', None, 'scripts/fix_m3_review.py; ' + NOTICE, h(NOTICE)),
    ('S21-19', 'm6-closed',
     'M6 closed. .gitignore extended to default-deny **/*.png, *.jpg, *.jpeg, *.pdf and '
     '*.html across the session tree, with the reason recorded in the file. Verified BY '
     'EFFECT, not by git check-ignore, which prints negation patterns while exiting 0: '
     '"git add -n -A -- sessions/2026-09-17" now stages 399 paths, ZERO of them '
     'image/pdf/html, down from 411 with 17. Nothing was actually staged. R1-107 amended in '
     'place with .bak-s21m6.',
     'VERIFIED', 'computation', None, 'git add -n -A, re-derived separately; ' + GI, h(GI)),
    ('S21-20', 'm5-letter-sent',
     'M5 stands uncorrected by decision, not by oversight. The vdPS letter, already sent, '
     'says "family (4.1) on p. 2655"; the label (4.1) is displayed on p. 2654 and only the '
     'entries, including the b(z) at issue, are on p. 2655. The quoted entries are on the '
     'page the letter names, so the slip cannot mislead the recipients. Operator ruling: '
     'correct it in passing if a reply comes; do not send a correction for it alone. The '
     'notice itself has not been changed on this point.',
     'INSPECTED', 'file_inspection', None, 'operator ruling; page image vdPS p. 2654', h(NOTICE)),
]

rows = [json.loads(l) for l in open(OUT, encoding='utf-8') if l.strip()]
have = {r['claim_id'] for r in rows}
assert not (have & {c[0] for c in more}), 'duplicate claim ids'
with open(OUT, 'a', encoding='utf-8') as f:
    for cid, tid, claim, label, ev, dps, script, oh in more:
        f.write(json.dumps({
            'claim_id': cid, 'task_id': tid, 'claim': claim, 'label': label,
            'evidence_type': ev, 'dps': dps, 'reproducible': True,
            'script': script, 'output_hash': oh,
        }, ensure_ascii=False) + '\n')

back = [json.loads(l) for l in open(OUT, encoding='utf-8') if l.strip()]
assert len(back) == len(rows) + len(more), 'readback count mismatch'
ids = [r['claim_id'] for r in back]
assert len(set(ids)) == len(ids)
print('claims.jsonl %d -> %d  (%s .. %s)' % (len(rows), len(back), ids[0], ids[-1]))
print('READBACK OK')
