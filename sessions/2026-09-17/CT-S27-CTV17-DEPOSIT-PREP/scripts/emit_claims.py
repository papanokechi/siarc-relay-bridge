"""emit_claims.py -- CT-S27-CTV17-DEPOSIT-PREP

Append-only.  Asserts the gate verdict and the staged hash FROM DISK before
writing anything, then reads the file back.  Per proposed Amendment B, the
output hashes are taken from the files on disk after those files were final.
"""

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
OUT_R1 = os.path.join(SESSION, "outputs", "preflight_deposit.out.txt")
OUT_R2 = os.path.join(SESSION, "outputs", "preflight_deposit_r2.out.txt")
CLAIMS = os.path.join(SESSION, "claims.jsonl")
STAGED = os.path.join(SESSION, "upload", "channel_theory_v1.7_version_notice.md")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def text(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


r1, r2 = text(OUT_R1), text(OUT_R2)
assert "GATE: BLOCKED" in r1, "run 1 is not the blocked run"
assert "checks failed  : 2" in r1, "run 1 does not record the two failures"
assert "GATE: PASSED" in r2, "run 2 did not pass"
assert "checks failed  : 0" in r2 and "broken checks  : 0" in r2
assert "reader controls: 3 of 3 caught" in r2
assert "DEPOSIT READY: NO." in r1 and "DEPOSIT READY: NO." in r2

staged = sha(STAGED)
assert staged == "75cd3476b89d18c13460e835f19d92f92c4db2b84a7548093ca9a82cf4f50872"
assert staged in r2, "the staged hash in run 2 is not the file on disk"

H1, H2 = sha(OUT_R1), sha(OUT_R2)
T = "CT-S27-CTV17-DEPOSIT-PREP/preflight"

CLAIMS_NEW = [
    {
        "claim_id": "S27-01",
        "task_id": T,
        "claim": (
            "THE v1.7 DEPOSIT PACKET IS INTERNALLY CONSISTENT AND THE DEPOSIT IS "
            "STILL BLOCKED. scripts/preflight_deposit.py runs 12 gate checks over the "
            "staged artefact and DEPOSIT-FORM.md against the held v1.6 record "
            "(refs/zenodo_22782807.json): publishable filename with no DRAFT prefix, no "
            "embedded record id and no browser suffix; exactly one file staged under "
            "exactly the declared name; staged bytes byte-identical to the source "
            "notice; the declared sha256 equal to the hash of the staged file ON DISK; "
            "the staged file identical to the revision the rev-3 content checker passed; "
            "title, creator, affiliation, licence and keyword count byte-equal to the "
            "record; version 1.7 over a record at 1.6; the concept DOI read from the "
            "conceptdoi FIELD and distinct from the version DOI; and the form naming no "
            "file it does not hold. Result 12 of 12 pass, 0 broken, with 19 artefact "
            "mutants rejected, 1 tree control and 3 of 3 reader controls caught. "
            "GATE: PASSED. DEPOSIT READY: NO -- the gate certifies the packet, not the "
            "deposit; every deposit shape remains blocked on material absent from this "
            "repository."),
        "label": "VERIFIED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/preflight_deposit.py",
        "output_hash": H2,
    },
    {
        "claim_id": "S27-02",
        "task_id": T,
        "claim": (
            "THE DEPOSIT FORM WAS STALE AGAINST THE DEPOSITED RECORD, AND THE GATE "
            "CAUGHT IT. DEPOSIT-FORM.md declared keywords_count: 28, carried forward "
            "from an earlier version and never checked against the deposited text. The "
            "held v1.6 record (record 22782807) carries 27 keywords. Check C4 compared "
            "the declared count against len(metadata.keywords) in the record and FAILED "
            "on the first run (outputs/preflight_deposit.out.txt, GATE: BLOCKED). The "
            "form was corrected to 27 and the check was left untouched. This is the "
            "same class as the version-notice round's stale-repository finding, arriving "
            "in metadata rather than prose and in the same direction: the working copy "
            "was behind the record."),
        "label": "VERIFIED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/preflight_deposit.py",
        "output_hash": H1,
    },
    {
        "claim_id": "S27-03",
        "task_id": T,
        "claim": (
            "AN ASCII-ONLY SENTINEL SET CANNOT DETECT A WRONG-CODEC READ. The reader "
            "controls required by proposed Amendment C initially scored 2 of 3: the "
            "latin-1 misread was NOT caught, because all four known-present sentinels "
            "were ASCII and survive a wrong-codec decode unchanged -- the mojibake lands "
            "only in the non-ASCII text, which no sentinel covered. Repaired by adding "
            "the non-ASCII sentinel 'xi_0 = 2/sqrt(beta_2)' from the title line; the "
            "control then fired, 3 of 3. Recorded as a defect in the CHECK, not in the "
            "artefact, and offered as a sub-clause of Amendment C."),
        "label": "VERIFIED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/preflight_deposit.py",
        "output_hash": H1,
    },
    {
        "claim_id": "S27-04",
        "task_id": T,
        "claim": (
            "CHECK D2 FIRST CONFIRMED ITS OWN HYPOTHESIS FOR THE WRONG REASON, AND ITS "
            "READER-INTEGRITY CLAUSE CAUGHT THAT. D2 asserts the blocker -- that no "
            "v1.4-v1.6 Channel Theory LaTeX source exists, so the outline cannot be "
            "rebuilt at v1.7. The first implementation walked sessions/2026-09-17/ "
            "only, found zero Channel Theory sources, and would have reported the "
            "blocker CONFIRMED had it not been required to assert a known-present "
            "feature first; it instead failed with 'no Channel Theory source found at "
            "all: the read is suspect'. Re-rooted at sessions/, it finds 9 sources, "
            "newest v1.3.1, and no v1.4-v1.6 source. The blocker holds, but it now "
            "holds on evidence rather than on an empty search."),
        "label": "VERIFIED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/preflight_deposit.py",
        "output_hash": H2,
    },
    {
        "claim_id": "S27-05",
        "task_id": T,
        "claim": (
            "NO DEPOSIT SHAPE IS EXECUTABLE FROM THIS REPOSITORY. The v1.6 record "
            "publishes exactly one file, channel_theory_outline.pdf (609300 bytes, md5 "
            "aa56a94a9354b5533b04c89461950eb1). Shape A (description-only, re-uploading "
            "the v1.6 PDF) and shape B (that PDF plus the notice) both require the v1.6 "
            "PDF, which is NOT HELD -- both v1.5 and v1.6 PDF fetches returned HTTP 504. "
            "Shape C (rebuild the outline at v1.7) requires v1.4-v1.6 LaTeX sources, "
            "which are ABSENT from the tree; rebuilding from the newest held source, "
            "v1.3.1, would silently revert two versions of corrections. DEPOSIT-FORM.md "
            "records deposit_shape: UNDECIDED and the pre-flight verifies the form names "
            "no file it does not hold. This is an operator decision and no check can "
            "make it pass."),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/preflight_deposit.py",
        "output_hash": H2,
    },
]

with open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
    for c in CLAIMS_NEW:
        fh.write(json.dumps(c, ensure_ascii=True) + "\n")

back = [json.loads(l) for l in open(CLAIMS, encoding="utf-8") if l.strip()]
assert len(back) == len(CLAIMS_NEW), "claims.jsonl holds %d lines" % len(back)
for w, r in zip(CLAIMS_NEW, back):
    assert w == r, "read-back differs at %s" % w["claim_id"]

print("claims written and read back: %d" % len(back))
for c in back:
    print("  %s  %-10s  %s" % (c["claim_id"], c["label"], c["output_hash"][:16]))
print()
print("staged sha256 (from disk) : %s" % staged)
print("preflight r1 out sha256   : %s" % H1)
print("preflight r2 out sha256   : %s" % H2)
