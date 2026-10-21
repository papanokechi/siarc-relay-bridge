# -*- coding: utf-8 -*-
"""R22: claims for the pre-send letter check. Writes, reads back, asserts."""
import json
import os
import shutil

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'claims.jsonl')
BAK = P + '.bak-r22'
rows = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
before = len(rows)
shutil.copy2(P, BAK)

NEW = [
    {
        "claim_id": "R1-109",
        "task_id": "R22-letter-presend-check",
        "claim": (
            "PRE-SEND CHECK of the vdPS typo letter, requested at operator review #20. The "
            "operator's pasted text and CT-S16-MEMBERSHIP-C/LETTER-vdPS-DRAFT.md were diffed "
            "mechanically with difflib rather than by eye, and every formula in the repo draft "
            "was string-matched against TYPO-EVIDENCE.md. All seven checks agree: the printed "
            "bracket (p + 1/2(q-1)q)^2, the corrected bracket (p + 1/2(q-1)q t)^2, the full "
            "residual factorisation -(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4, the B1[1,2] "
            "corroboration, the det A(0) non-discrimination remark, the arXiv:0902.1702v5 p. 34 "
            "locator, and the absence of a published erratum. The two texts differ in four "
            "places and the repo version is stronger or more exact at each: the operator's "
            "[FILL IN] placeholder is filled from TYPO-EVIDENCE.md section 2; the residual is "
            "given in full rather than as (q-1)(t-1)(...)/4; the B1[1,2] corroboration is "
            "absent from the paste and in the repo version LEADS the letter, since it appeals "
            "only to the authors' own page and not to the correctness of any constraint; and "
            "the det A(0) sentence is absent from the paste. No place was found where the "
            "paste is better. Salutation, closing, ORCID and the paper's title string are "
            "byte-identical. Recommendation: send the repo version. NOTHING WAS SENT."
        ),
        "label": "VERIFIED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/letter_diff_r22.py",
        "output_hash": None,
    },
    {
        "claim_id": "R1-110",
        "task_id": "R22-letter-open-items",
        "claim": (
            "TWO ITEMS REMAIN OPEN ON THE LETTER, both the operator's. (i) "
            "LETTER-vdPS-DRAFT.md is a BODY: it carries a Subject line but no To or Cc field, "
            "so the instruction at review #20 - one email, both coauthors in To, rather than "
            "two letters - is not yet expressed anywhere in the artefact and must be applied "
            "at the mail client. (ii) The draft's condition table still reads 'Confirm the "
            "authors' current address from a university page, not the paper - operator's, not "
            "done by this session', while operator review #19 stated the two addresses were "
            "'now confirmed'. The record and the operator's statement disagree on whether that "
            "condition is discharged, and no page-verified source for either address exists in "
            "the session tree. The CT-S16 file was NOT edited from this session to resolve the "
            "disagreement, since it belongs to an earlier packet; it is reported instead. The "
            "Wong-Li request is a separate letter to a different recipient and is not affected."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "CT-S16-MEMBERSHIP-C/LETTER-vdPS-DRAFT.md",
        "output_hash": None,
    },
    {
        "claim_id": "R1-111",
        "task_id": "R22-self-caught-extraction",
        "claim": (
            "SELF-CAUGHT DEFECT in the diff artefact itself, first pass: the letter body was "
            "extracted with draft.split('---', 1), which split at the first literal '---' in "
            "the file - the separator row of a MARKDOWN TABLE, |---|---| - not at the horizontal "
            "rule. Fifteen rows of the draft's condition table were therefore diffed as though "
            "they were letter text. The output was still readable and the verdict unaffected, "
            "which is why it would have shipped. Caught by looking at the artefact rather than "
            "at the exit code, consistent with the fifth amendment. Repaired with a line-anchored "
            "regex plus two assertions that the extracted body starts at 'Subject:' and ends at "
            "the ORCID, so the failure cannot recur silently; diff line count fell from 65 to 50."
        ),
        "label": "INSPECTED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/letter_diff_r22.py",
        "output_hash": None,
    },
]
ids = {r['claim_id'] for r in rows}
for n in NEW:
    assert n['claim_id'] not in ids, 'duplicate %s' % n['claim_id']
rows.extend(NEW)
with open(P, 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

back = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
assert len(back) == before + len(NEW), 'count %d' % len(back)
by = {r['claim_id']: r for r in back}
for n in NEW:
    assert by[n['claim_id']]['claim'] == n['claim'], 'mismatch %s' % n['claim_id']
assert len({r['claim_id'] for r in back}) == len(back)
print('rows %d -> %d; appended %s' % (before, len(back), ', '.join(n['claim_id'] for n in NEW)))
print('READBACK OK')
