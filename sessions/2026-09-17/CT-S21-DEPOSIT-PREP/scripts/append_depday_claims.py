# -*- coding: utf-8 -*-
"""Claims from the deposit-day citation pass."""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJ = os.path.join(HERE, 'claims.jsonl')


def h(rel):
    return hashlib.sha256(open(os.path.join(HERE, rel), 'rb').read()).hexdigest()


NEW = [
    dict(claim_id='S21-38',
         claim=("DEPOSIT-DAY CITATION PASS RUN, all four rows RE-FETCHED OK on "
                "2026-09-18. van der Put-Saito sha256 1666bd6b... and Jimbo "
                "255d4f07... are byte-identical to the held copies and to "
                "REFS-MANIFEST.md. Zenodo record 20481592 returns version 1.2, "
                "doi 10.5281/zenodo.20481592 and conceptdoi "
                "10.5281/zenodo.20455089 - read from the API, still distinct - "
                "with file vquad_resurgence.pdf at 612719 bytes matching the "
                "held copy a5d9e264... DLMF section 32.2 is Version 1.2.8, "
                "release date 2026-09-15, unchanged from what the notice cites."),
         label='VERIFIED', evidence_type='computation',
         script='scripts/depday_citation_pass.py',
         output_file='outputs/depday_citation_pass.json'),
    dict(claim_id='S21-39',
         claim=("Rows 1 and 2 were first recorded NOT RE-FETCHED on the "
                "assumption that paywalling left no fetch route. That was wrong: "
                "REFS-MANIFEST.md records working URLs for both, and paywalled-to-"
                "redistribute is not unreachable-to-fetch. Corrected in the same "
                "round by actually re-fetching; the rule asks for a re-fetch, not "
                "a licence judgement."),
         label='VERIFIED', evidence_type='computation',
         script='scripts/depday_refetch_12.py',
         output_file='outputs/depday_citation_pass.json'),
    dict(claim_id='S21-40',
         claim=("PAGE IMAGES RE-READ BY EYE, all four MATCH what the notice "
                "quotes. vdPS printed 2634 carries the strong-Riemann-Hilbert "
                "restriction ('positive answer, except possibly for (1/2,-,1/2) "
                "and (-,-,5/2)'); printed 2635 carries Table 2.1 with the D5-tilde/"
                "PV row r(0)=0, r(1)=0, r(inf)=1, r(t)=-, dim P=3; printed 2637 "
                "prints '-theta_i^2/4 is the determinant of A_i for i=0,1 and "
                "theta_inf is the (1,1) entry of A_0+A_1' with A_inf = "
                "(t/2)diag(-1,1); Jimbo printed 1152 prints (3.1) with constant "
                "matrix diag(1,0), (A1)_PV as 'theta_0, theta_t not in Z' with no "
                "theta_inf, and the PV dictionary alpha=(1/8)(th0-tht+thinf)^2, "
                "beta=-(1/8)(th0-tht-thinf)^2, gamma=1-th0-tht, delta=-1/2."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/depday_citation_pass.py',
         output_file='DEPOSIT-DAY-PASS.md'),
    dict(claim_id='S21-41',
         claim=("C2's central claim is legible on the source page: Jimbo's "
                "dictionary gives gamma = 1 - theta_0 - theta_t, so at "
                "theta_0 = theta_t = 0 it yields gamma = 1 directly, which is what "
                "refutes Conjecture 4.1's stated beta = gamma = 0."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/depday_citation_pass.py',
         output_file='DEPOSIT-DAY-PASS.md'),
    dict(claim_id='S21-42',
         claim=("MY OWN RENDERER WAS OFF BY ONE, caught by the eye read. It used "
                "printed = pdf_index + 2611 for van der Put-Saito and index 16 for "
                "Jimbo; the true offsets are +2610 and index 15. The file written "
                "as 'p2635' showed printed 2634 and the Jimbo render showed 1153. "
                "The automated 'page number visible in text' check returned false "
                "for all four pages and was nearly passed over. Mislabelled renders "
                "deleted. The NOTICE's page numbers were correct throughout."),
         label='VERIFIED', evidence_type='file_inspection',
         script='scripts/depday_citation_pass.py',
         output_file='DEPOSIT-DAY-PASS.md'),
    dict(claim_id='S21-43',
         claim=("PACKET DEFECT, OPEN FOR THE OPERATOR. "
                "CT-R1-AUDIT/coldpackets/jimbo_p1152.png is printed page 1153, not "
                "1152: it is byte-identical (84f548ce...) to a render of PDF index "
                "16, while printed 1152 is index 15. The vdPS packet images were "
                "checked and are correctly labelled. No adopted claim is wrong - "
                "every Jimbo quote in the notice matches the true printed 1152 - "
                "but the notice's methodology note attributes CT-S15's two rejected "
                "transcriptions to OCR when they follow substantially from this "
                "packet-labelling error: printed 1153 carries (A3)_PV, which does "
                "constrain theta_inf, and does not carry (3.1) at all. NOT EDITED; "
                "a replacement paragraph is proposed in DEPOSIT-DAY-PASS.md for the "
                "operator to accept or redraft."),
         label='VERIFIED', evidence_type='file_inspection',
         script='scripts/depday_citation_pass.py',
         output_file='DEPOSIT-DAY-PASS.md'),
    dict(claim_id='S21-44',
         claim=("A0 pre-flight re-run at deposit time: check_invariants OK; "
                "scan_macro_damage 0; scan_escape_damage confined to raw PDF "
                "extractions; item4_consistency passes with C4 count word 7 vs 7 "
                "enumerated, F7 0 asserting / 1 negated, both hedges present; "
                "control_item4 restored the notice to sha256 aba11232... and ALL "
                "THREE controls fired."),
         label='VERIFIED', evidence_type='build',
         script='scripts/control_item4.py',
         output_file='outputs/item4_consistency.md'),
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
print('claims %d -> %d (+%d)' % (n0, len(back), len(NEW)))
print('READBACK OK')
