# -*- coding: utf-8 -*-
"""Claims for the reference round (R24)."""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.basename(HERE) == 'CT-S21-DEPOSIT-PREP', HERE
SESS = os.path.dirname(HERE)
V = os.path.join(HERE, 'outputs', 'refs_verify.json')
MAN = os.path.join(SESS, 'CT-R1-AUDIT', 'REFS-MANIFEST.md')
REQ = os.path.join(SESS, 'CT-R1-AUDIT', 'AUTHOR-REQUEST-WONGLI.md')


def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


more = [
    ('S21-24', 'wongli-doi-confirmed',
     'Purchase target confirmed by DOI content negotiation on 2026-09-18, HTTP 200: '
     'DOI 10.1002/sapm1992874289 resolves to R. Wong and H. Li, "Asymptotic Expansions for '
     'Second-Order Linear Difference Equations, II", Studies in Applied Mathematics 87(4), '
     '289-324, issued 1992-11. This matches the citation table in P0-CITATION-RULE.md '
     'exactly, including the numeral II and the word "linear" whose omission was the trap '
     'recorded at R1-61. The article itself remains NOT OBTAINED (R1-46 stands); nothing '
     'was purchased.',
     'VERIFIED', 'computation', None, 'scripts/verify_refs.py', h(V)),
    ('S21-25', 'refs-acquired-ccby',
     'Two references acquired into CT-R1-AUDIT/refs/ after checking the licence printed on '
     'the source, and ONLY because it cleared: arXiv:2204.09305 = R. Wong, Yu-Qiu Zhao, '
     '"Recent Advances in Asymptotic Analysis", Anal. Appl. 20 (2022) 1103-1146, DOI '
     '10.1142/S0219530522400012 (464879 bytes, sha256 123ab322619c723c...); and '
     'arXiv:2306.05930 = Alaa Ibrahim, Bruno Salvy, "Positivity certificates for linear '
     'recurrences", SODA 2024, DOI 10.1137/1.9781611977912.37 (720492 bytes, sha256 '
     '36e9d025c89b6fa0...). BOTH print http://creativecommons.org/licenses/by/4.0/ on the '
     'arXiv abstract page, so both carry a redistribution right - unlike arXiv:0902.1702, '
     'whose default nonexclusive-distrib/1.0 grants none. These are the first third-party '
     'files in refs/ cleared for redistribution on evidence rather than left NOT CHECKED. '
     'The acquisition script refuses to download if the licence check does not pass.',
     'VERIFIED', 'computation', None, 'scripts/acquire_refs.py', h(MAN)),
    ('S21-26', 'salvy-content-unverified',
     'FLAG, NOT A FINDING. The operator describes arXiv:2306.05930 as stating that the '
     'leading coefficient of a linear recurrence dominant solution is not computable '
     'exactly in general. The IDENTIFIER is verified and the paper is real - Ibrahim and '
     'Salvy, "Positivity certificates for linear recurrences", SODA 2024 - but its title is '
     'about positivity certificates and does not obviously name that result, and the '
     'CONTENT CLAIM HAS NOT BEEN CHECKED against the PDF in this session. It is plausible '
     'that such a statement appears there, and equally possible the attribution belongs to '
     'a different source. It must be located and quoted before it is used to frame the '
     'contribution for K and r_infinity in v1.7. Recorded so the attribution does not '
     'travel unchecked; the same applies to the Wong-Zhao section 3 reading, which is the '
     'operator own and is not independently confirmed here.',
     'CONJECTURED', 'file_inspection', None, 'scripts/verify_refs.py', h(V)),
    ('S21-27', 'wongli-letter-superseded',
     'AUTHOR-REQUEST-WONGLI.md marked SUPERSEDED - do not send, at its head. The '
     'correspondence route is dropped by operator ruling (R. Wong retired 2019, emeritus); '
     'the plan is purchase. The file is retained because the title trap it caught (R1-61) '
     'is still live: "Wong & Li 1992a" alone retrieves the wrong paper, and both "linear" '
     'and "II" are load-bearing. Correcting my own closing summary, which wrongly listed a '
     '"Wong-Li letter" and a pending Springer-contents check among the remaining queue: the '
     'letter is dropped, the contents check is done, and the letter that was actually sent '
     'was the vdPS typo report.',
     'INSPECTED', 'file_inspection', None, REQ, h(REQ)),
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
assert len(back) == len(rows) + len(more)
ids = [r['claim_id'] for r in back]
assert len(set(ids)) == len(ids)
print('claims %d -> %d  (%s .. %s)' % (len(rows), len(back), ids[0], ids[-1]))
print('READBACK OK')
