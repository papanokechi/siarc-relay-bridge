"""R21b: correct R1-103 in place and append the manifest findings.
Backs up, writes, reads back, asserts. Exit code is not evidence.
"""
import json
import os
import shutil

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'claims.jsonl')
BAK = P + '.bak-r21b'

rows = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
before = len(rows)
shutil.copy2(P, BAK)

PRIOR = next(r for r in rows if r['claim_id'] == 'R1-103')['claim']

AMENDED = (
    "COMMIT READINESS, reported not executed: the session tree sessions/2026-09-17/ "
    "remains a single untracked directory at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59. "
    "Committing it is an operator action under P0 and was NOT performed. The two things "
    "standing between the record and an accidental loss are REFS-MANIFEST.md and the backups "
    "in C:/LocalWork/_siarc-session-backups/, each with a sha256 sidecar stored OUTSIDE its "
    "archive. [AMENDED AT R21b, self-caught: the original text of this claim asserted that "
    "refs/ is excluded from the backup and that both exclusions were re-verified at this "
    "round's backup. That was FALSE and was never relied upon. make_backup.py excludes only "
    "{.lake, __pycache__, .git}; the archive contains 34 refs/ entries. That is correct and "
    "intended - the licence hold governs REDISTRIBUTION, i.e. commit and deposit, not local "
    "retention, and a backup that omitted the reference bytes would defeat its own purpose. "
    "The exclusion that was missing is the one on the COMMIT side, which did not exist at all "
    "until R21b; see R1-105 and R1-107. Prior text is quoted in AUDIT.md section R21 and "
    "preserved in claims.jsonl.bak-r21b.]"
)
for r in rows:
    if r['claim_id'] == 'R1-103':
        r['claim'] = AMENDED

NEW = [
    {
        "claim_id": "R1-104",
        "task_id": "R21b-amend-r1-103",
        "claim": (
            "SELF-CAUGHT DEFECT, amended in place: R1-103 as first written claimed that refs/ "
            "is excluded from the backup under the licence hold and that the exclusion was "
            "re-verified at this round's backup. Neither was true. The claim was checked only "
            "because it named a mechanism, and naming a mechanism invites reading it: "
            "make_backup.py line EXCLUDE_DIRS = {'.lake','__pycache__','.git'} contains no "
            "refs entry, and the archive listing returns 34 refs/ paths. The defect is a "
            "conflation of two different holds - retain locally versus do not redistribute - "
            "and it is the same class as the one the fourth amendment already covers, reached "
            "from the opposite direction: there the risk was publishing held bytes, here the "
            "text claimed a protection that did not exist. Amended under the R20 precedent "
            "(backup first, prior text quoted in AUDIT, provenance note inside the claim, "
            "label unchanged, amendment itself claimed). No downstream claim had cited it."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/make_backup.py, CT-R1-AUDIT/append_r21b_claims.py",
        "output_hash": None,
    },
    {
        "claim_id": "R1-105",
        "task_id": "R21b-manifest-route",
        "claim": (
            "FINDING, the manifest route was a decision and not an artefact: REFS-LICENCE-REVIEW.md "
            "recommended committing a manifest of hashes in place of the reference bytes, the "
            "recommendation was adopted in prose and cited in later rounds as though it were in "
            "force, and it was described to the operator as one of the two things standing between "
            "the record and a bad git clean. No manifest file existed anywhere under "
            "sessions/2026-09-17/ (glob for MANIFEST returned nothing), the repository has no "
            "root .gitignore, and the only mechanical exclusion in the tree was "
            "CT-S1-THEOREM/lean/.gitignore covering the Lean build directory. A git add of the "
            "session tree on the morning of R21b would therefore have staged every one of the 69 "
            "files under refs/ and pages/, including the whole-page Annales de l'Institut Fourier "
            "renders and the Gautschi page image, the two items the review names explicitly as DO "
            "NOT COMMIT. The hold was carried entirely by the intention of whoever next typed the "
            "command. REFS-MANIFEST.md was built at R21b with path, byte length and full sha256 "
            "for all 69."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/make_refs_manifest.py",
        "output_hash": None,
    },
    {
        "claim_id": "R1-106",
        "task_id": "R21b-inventory-gap",
        "claim": (
            "FINDING, the licence inventory was incomplete: REFS-LICENCE-REVIEW.md holds a "
            "per-file table and the deposit gate reads that table, but 40 of the 69 third-party "
            "files under refs/ and pages/ have no row in it. Among them are six complete "
            "third-party articles rather than page regions (gautschi1967.pdf, perron1913.pdf, "
            "nemes2025.pdf, wang_jat2014.pdf, polycf.pdf, jimbo_1982_prims.pdf, with bt1933.pdf), "
            "their extracted-text derivatives, and fifteen page images under "
            "CT-S16-MEMBERSHIP-C/pages/. The whole of CT-S8-LITCHECK/refs/ and CT-S9-PVPARAMS/refs/ "
            "had never been enumerated. The hold's wording covers them, since it reads 'everything "
            "under any refs/ directory', so nothing was exposed; what failed is that the wording "
            "and the inventory diverged and only the inventory is machine-readable. Every one of "
            "the 40 is recorded in REFS-MANIFEST.md as NOT CHECKED. No licence determination was "
            "made for any file in this round."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/make_refs_manifest.py",
        "output_hash": None,
    },
    {
        "claim_id": "R1-107",
        "task_id": "R21b-gitignore-mechanism",
        "claim": (
            "sessions/2026-09-17/.gitignore written at R21b and verified by effect, not by "
            "existence. Patterns exclude directory contents rather than the directories "
            "(**/refs/* and **/pages/*) so that a negation can re-admit session-produced scripts "
            "(!**/refs/*.py). Verified with git add --dry-run over the whole session tree, which "
            "stages nothing and is reversible: 391 paths would be added, of which exactly one lies "
            "under refs/ or pages/, namely CT-R1-AUDIT/refs/parse_dlmf.py, written in this run and "
            "re-admitted by the negation; git ls-files --others --ignored reports 97 ignored paths. "
            "Zero third-party bytes would be staged. This is preparatory and reversible and no "
            "commit was made. Note that git check-ignore -v was NOT sufficient evidence here: it "
            "printed the negation pattern for parse_dlmf.py while still exiting 0, which read as "
            "IGNORED and was the opposite of the truth; the dry run settled it."
        ),
        "label": "VERIFIED",
        "evidence_type": "build",
        "dps": None,
        "reproducible": True,
        "script": "git add -n -- sessions/2026-09-17/",
        "output_hash": None,
    },
    {
        "claim_id": "R1-108",
        "task_id": "R21b-count-readback",
        "claim": (
            "METHOD FINDING extending the P0 readback rule from writes to counts: a PowerShell "
            "pipeline that invoked git add -n twice in one statement and counted the second "
            "invocation reported would-add total: 7 for a tree whose true count is 391. The "
            "command exited 0, the number was plausible enough to reason from, and it would have "
            "supported the conclusion that almost nothing was stageable, which is the opposite of "
            "the finding in R1-105. It was caught only by re-running the enumeration alone and "
            "printing every line. Two counts stated to the operator in this round were also wrong "
            "before checking: 71 files under refs/, pages/ and packet/, against a true 69 under "
            "refs/ and pages/. The rule to carry: a count that will be reasoned from is read back "
            "by re-deriving it in a separate invocation, and a count interpolated into a shell "
            "pipeline alongside other commands is not evidence."
        ),
        "label": "INSPECTED",
        "evidence_type": "computation",
        "dps": None,
        "reproducible": True,
        "script": "CT-R1-AUDIT/append_r21b_claims.py",
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

# ---- read back -------------------------------------------------------------
back = [json.loads(l) for l in open(P, encoding='utf-8') if l.strip()]
assert len(back) == before + len(NEW), 'row count %d != %d' % (len(back), before + len(NEW))
by = {r['claim_id']: r for r in back}
assert 'AMENDED AT R21b' in by['R1-103']['claim'], 'R1-103 amendment absent'
assert by['R1-103']['label'] == 'INSPECTED', 'label changed'
for n in NEW:
    assert by[n['claim_id']]['claim'] == n['claim'], 'mismatch %s' % n['claim_id']
assert len({r['claim_id'] for r in back}) == len(back), 'duplicate ids'
with open(BAK, encoding='utf-8') as f:
    assert PRIOR in f.read(), 'prior text not in backup'
print('rows %d -> %d' % (before, len(back)))
print('R1-103 amended; appended', ', '.join(n['claim_id'] for n in NEW))
print('READBACK OK')
