# -*- coding: utf-8 -*-
"""CT-S21 - file the deposit-prep claims, one per adopted finding."""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.basename(HERE) == 'CT-S21-DEPOSIT-PREP', HERE
OUT = os.path.join(HERE, 'claims.jsonl')


def h(rel):
    p = os.path.join(HERE, rel)
    assert os.path.exists(p), 'missing evidence file: ' + rel
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


Q = 'outputs/item2_quotes.md'
C = 'outputs/item4_consistency.md'
R = 'outputs/item1_refetch.json'
B = 'outputs/item1b_resolve.json'
L = 'outputs/item3_licences.json'
D = 'DEPOSIT-READY.md'

rows = [
    ('S21-01', 'item1-refetch',
     'All five external sources the v1.3 notice cites were re-fetched on 2026-09-18, '
     'all HTTP 200. The vdPS AIF PDF, the arXiv 0902.1702v5 PDF, the Jimbo EMS PDF and '
     'the companion v1.2 PDF served by Zenodo are each BYTE-IDENTICAL to the local copy '
     '(sha256 equality). No source was NOT RE-FETCHED. Downloads went to a temp directory '
     'outside the repository: a re-fetch is verification, not acquisition.',
     'VERIFIED', 'computation', None, 'scripts/item1_refetch.py', h(R)),
    ('S21-02', 'item1-zenodo-dois',
     'Companion v1.2 = Zenodo record 20481592, version DOI 10.5281/zenodo.20481592, '
     'CONCEPT DOI 10.5281/zenodo.20455089 - the two differ, so a citation of the exact '
     'text the notice corrects must use the version DOI. metadata.version = "1.2"; the '
     'file checksum Zenodo reports matches the local md5.',
     'VERIFIED', 'computation', None, 'scripts/item1b_resolve.py', h(B)),
    ('S21-03', 'item1-dlmf-version',
     'DLMF section 32.2, cited by v1.2 for the PV normalisation and at 32.2(vi) Eq. 32.2.33 '
     'for the PV->PIII degeneration, was fetched at Version 1.2.8, release date 2026-09-15. '
     'The DLMF is a living document; version and release date must travel with the citation.',
     'VERIFIED', 'computation', None, 'scripts/item1b_resolve.py', h(B)),
    ('S21-04', 'item3-arxiv-licence',
     'The arXiv abstract page for 0902.1702 prints the licence '
     'http://arxiv.org/licenses/nonexclusive-distrib/1.0/ - arXiv\'s DEFAULT licence, which '
     'grants arXiv distribution rights and grants third parties NO redistribution right. '
     'The arXiv PDF therefore may not be committed or deposited. The three Zenodo companion '
     'records print cc-by-4.0. The AIF item page carries no CC string (the PDF title page '
     'prints "tous droits reserves") and the EMS article page could not be read: both stay '
     'NOT CHECKED. No licence determination was made and no exclusion was changed.',
     'INSPECTED', 'file_inspection', None, 'scripts/item3_licences.py', h(L)),
    ('S21-05', 'item2-quotes',
     'Thirteen quote rows checked against page images, one image per message: vdPS pp. 2634, '
     '2635, 2637, 2655; Jimbo p. 1152 including hypothesis (A1)_PV "theta_0, theta_t not in Z"; '
     'companion v1.2 printed pp. 3, 4, 5, 6, 7, 8, 10. All MATCH except the location of family '
     '(4.1). Hypotheses were treated as in scope, not only theorem statements.',
     'VERIFIED', 'file_inspection', None, 'manual page-image reads, tabulated in ' + Q, h(Q)),
    ('S21-06', 'item2-family41-page',
     'DIFFERS: the notice and the vdPS letter both locate the family as "family (4.1) on '
     'p. 2655". The LABEL (4.1) is displayed on p. 2654; only the entries, including the b(z) '
     'being corrected, are printed on p. 2655. The mathematics is unaffected. Recommended '
     'wording: "the entry b(z) of family (4.1) (displayed p. 2654), printed on p. 2655". '
     'Matters more in the letter, which goes to the authors.',
     'VERIFIED', 'file_inspection', None, Q, h(Q)),
    ('S21-07', 'item2-c5-incomplete',
     'C5 states its list of affected passages was "located by a full-text pass over v1.2 and '
     'read from page images" and lists five. Reading the page images found FOUR FURTHER '
     'passages that depend on the apparency claim and appear nowhere in the notice: Theorem '
     '3.1, Remark 3.2 ("the monodromy at the finite singularities is exactly trivial by '
     'algebra"), Remark 4.2 ("theta_1 = theta_2 = 0 (apparent singularities), the standard '
     'connection formula degenerates ... consistent with the failure of all tested PSLQ '
     'identification bases"), and Remark 6.7. Remark 4.2 is load-bearing: it is the '
     'companion\'s explanation of the PSLQ nulls. C5\'s completeness assertion is therefore '
     'not supported as it stands.',
     'STRUCTURAL', 'file_inspection', None, Q, h(Q)),
    ('S21-08', 'item2-theorem31',
     'v1.2 Theorem 3.1 (printed pp. 4-5, read from a rendered page image) ALREADY PROVES C1\'s '
     'local analysis: its Step 1 computes p_0 = a\'(s_k)/a\'(s_k) = 1 and q_0 = 0, giving '
     'I(rho) = rho(rho-1) + p_0 rho + q_0 = rho^2 = 0; Step 3 puts the logarithm in y_2 only; '
     'and Step 4 DISPLAYS THE MONODROMY as [[1, 2*pi*i],[0,1]], which is unipotent and not the '
     'identity. Theorem 3.1(ii) claims only that the EFFECTIVE monodromy on the connection '
     'coefficient M_11 is trivial, because the unipotent action fixes y_1 - a different and '
     'weaker statement than apparency. Consequences: (a) C1 corrects Remark 2.2\'s GENERAL '
     'claim about the roots of chi, not a gap in section 3; (b) the notice as drafted would '
     'lead a reader to take section 3 as collateral damage of C1, which this evidence does not '
     'support. Theorem 3.1(ii)\'s CORRECTNESS was not re-derived and is not asserted here.',
     'STRUCTURAL', 'file_inspection', None, Q, h(Q)),
    ('S21-09', 'item4-consistency',
     'Internal consistency: every claim_id the notice cites exists and is not superseded (PASS); '
     'no sentence asserts anything as author-confirmed that is not, and the hedges "had not been '
     'sent" and "No published erratum is known to us" are intact (PASS). Two failures: S4-06 and '
     'S5B-C6 carry review = None in the corpus while the notice\'s support table shows them cold '
     '- VERIFY-S14.md and _deps_table.md show the cold read did happen by route "D - '
     'corroborated", so the CORPUS rows are stale and the notice is right; and C4 reads "Four '
     'points must accompany this table" then enumerates seven. A vacuity pre-check on injected '
     'bad data confirmed the scan fires.',
     'VERIFIED', 'computation', None, 'scripts/item4_consistency.py', h(C)),
    ('S21-10', 'item4-r1-107-false',
     'CORRECTION TO MY OWN CLAIM R1-107, which stated that after last round\'s .gitignore zero '
     'third-party bytes would be staged. Re-derived in a separate invocation: '
     '"git add -n -A -- sessions/2026-09-17" stages 411 paths, 17 of them image/pdf/html, of '
     'which NINE are third party (vdps_p2634.png, vdps_p2635.png, jimbo_p1152.png, four '
     'CT-S10-COLDREAD2/dlmf_5_11*.html, two CT-S9-PVPARAMS jimbo page images). The other eight '
     'are the operator\'s own CC-BY-4.0 companion pages and this project\'s theorem.pdf. The '
     'CT-S18 and CT-S19 packet images ARE already excluded, sitting under packet/pages/; an '
     'earlier draft of DEPOSIT-READY.md listed them as exposed and re-deriving the count '
     'corrected it. This is a COMMIT blocker, not a deposit blocker. The packet said "change no '
     'exclusion", so .gitignore was not edited. R1-107 needs amendment or supersession.',
     'VERIFIED', 'computation', None, 'git add -n -A, re-derived separately; ' + D, h(D)),
    ('S21-11', 'item2-self-caught-notchecked',
     'SELF-CAUGHT DEFECT: the first draft of item2_quotes.md recorded Remark 6.1 (C5 row 4) as '
     'NOT CHECKED on the stated ground that its page image was unavailable. I had not opened the '
     'image. The page-number mapping I reasoned from (printed = N + 1) was correct and the '
     'conclusion was still wrong: companion_v12_p7.png is printed p. 8 and Remark 6.1 is on it, '
     'quoted verbatim as "derived from the WKB and apparent-singularity data", which MATCHES. A '
     'NOT CHECKED status is only honest when something was attempted and failed; otherwise it '
     'should say not attempted. Recommend an eighth P0 line.',
     'INSPECTED', 'file_inspection', None, Q, h(Q)),
    ('S21-12', 'verdict',
     'VERDICT: the v1.3 notice is NOT READY for deposit on this evidence. Six items must resolve '
     'first (M1 C5 incompleteness and the Theorem 3.1 understatement; M2 the letter-status '
     'placeholder in C3, currently true but false the moment the letter is sent; M3 the stale '
     'review fields; M4 "four" vs seven; M5 the p. 2654/2655 location; M6 the commit-side '
     'exclusion hole). None touches the mathematics of C1-C5. Only M1 requires a judgement '
     'rather than an edit.',
     'INSPECTED', 'file_inspection', None, D, h(D)),
]

assert not os.path.exists(OUT), 'claims.jsonl already exists - refusing to overwrite'
with open(OUT, 'w', encoding='utf-8') as f:
    for cid, tid, claim, label, ev, dps, script, oh in rows:
        f.write(json.dumps({
            'claim_id': cid, 'task_id': tid, 'claim': claim, 'label': label,
            'evidence_type': ev, 'dps': dps, 'reproducible': True,
            'script': script, 'output_hash': oh,
        }, ensure_ascii=False) + '\n')

back = [json.loads(l) for l in open(OUT, encoding='utf-8') if l.strip()]
assert len(back) == len(rows), 'readback: %d written, %d read' % (len(rows), len(back))
ids = [r['claim_id'] for r in back]
assert len(set(ids)) == len(ids), 'duplicate ids'
for r in back:
    assert len(r['output_hash']) == 64, r['claim_id']
print('wrote %d claims: %s .. %s' % (len(back), ids[0], ids[-1]))
print('READBACK OK')
