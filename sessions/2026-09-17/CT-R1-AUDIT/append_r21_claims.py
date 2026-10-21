"""R21: append the seventh-amendment claim to CT-R1-AUDIT/claims.jsonl.
Backs up, writes, reads back, fails loudly.
"""
import json
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
CL = os.path.join(BASE, 'claims.jsonl')
BAK = CL + '.bak-r21'

NEW = [
    {"claim_id": "R1-102", "task_id": "R21-p0-seventh-amendment",
     "claim": "P0 SEVENTH AMENDMENT adopted (operator review #19): before a negative "
              "result is reported as a finding, establish that the test could have come "
              "out positive; state what input would have made it pass, and either "
              "exhibit one or say why none exists. This is the mirror of the standing "
              "rule that a control must be able to fail, and is a DISTINCT failure mode: "
              "a step that cannot fail is empty and quiet, while a step that cannot "
              "succeed is empty and assertive, arriving as a confident negative verdict "
              "that reads as a discovery. Origin S17-22: CT-S18 compared System C "
              "against the c-route reduction, whose residual -1/(z-q) has no zero in z, "
              "so the comparison could return only mismatch at every sample point and "
              "every parameter value; its ERROR verdict carried no information yet read "
              "as a real defect for two rounds and cost two further cold packets to "
              "clear. Diagnostic: ask what the test would have returned had the claim "
              "been true, and if the answer is the same thing, the test has not been "
              "run. Scope: refutations, falsifier arms, and any pre-registered threshold "
              "reported as breached.",
     "label": "STRUCTURAL", "evidence_type": "file_inspection", "dps": None,
     "reproducible": True, "script": "CT-R1-AUDIT/P0-CITATION-RULE.md, seventh amendment",
     "output_hash": None},
    {"claim_id": "R1-103", "task_id": "R21-commit-readiness",
     "claim": "COMMIT READINESS, reported not executed: the session tree "
              "sessions/2026-09-17/ remains a single untracked directory at HEAD "
              "08aa0e2381b3dc37ee54a3200b7272755ca11d59, holding 337 claims in 21 files. "
              "Committing it is an operator action under P0 and was NOT performed. The "
              "two things standing between the record and an accidental loss are the "
              "manifest route and the backups in C:/LocalWork/_siarc-session-backups/, "
              "each with a sha256 sidecar stored OUTSIDE its archive. refs/ is excluded "
              "mandatorily under the licence hold (fourth amendment) and lean/.lake/ for "
              "size; both exclusions were re-verified at this round's backup, which "
              "included 454 files and skipped 124116 excluded paths.",
     "label": "INSPECTED", "evidence_type": "file_inspection", "dps": None,
     "reproducible": True, "script": "CT-R1-AUDIT/make_backup.py", "output_hash": None},
]

with open(CL, encoding='utf-8') as f:
    rows = [json.loads(l) for l in f if l.strip()]
before = len(rows)
shutil.copyfile(CL, BAK)
assert os.path.exists(BAK), 'backup not written'

have = {r['claim_id'] for r in rows}
for n in NEW:
    assert n['claim_id'] not in have, 'duplicate ' + n['claim_id']
    have.add(n['claim_id'])
    rows.append(n)

with open(CL, 'w', encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

with open(CL, encoding='utf-8') as f:
    back = [json.loads(l) for l in f if l.strip()]
ids = [r['claim_id'] for r in back]
assert len(back) == before + len(NEW), 'count wrong %d -> %d' % (before, len(back))
assert len(ids) == len(set(ids)), 'duplicate ids after write'
for n in NEW:
    assert n['claim_id'] in ids, 'missing ' + n['claim_id']
    assert [r for r in back if r['claim_id'] == n['claim_id']][0]['claim'] == n['claim']
print('rows %d -> %d; appended %s' % (before, len(back), ', '.join(n['claim_id'] for n in NEW)))
print('backup:', BAK)
print('READBACK OK')
