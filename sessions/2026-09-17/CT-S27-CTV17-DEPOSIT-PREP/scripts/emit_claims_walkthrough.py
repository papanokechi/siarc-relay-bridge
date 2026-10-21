"""emit_claims_walkthrough.py -- CT-S27-CTV17-DEPOSIT-PREP

Append-only.  Covers the walkthrough round: the description repairs, the two
check defects found in this session's own checkers, and the offline self-test
of the post-publish readback.

Discipline, per the adopted amendments:
  - every hash is taken FROM DISK, after the artefact was final (B);
  - no existing output file is overwritten -- each re-run wrote a NEW name;
  - the preconditions below are asserted before anything is appended, so a
    claim cannot be written about a run that did not happen (C).
"""

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
OUT = os.path.join(SESSION, "outputs")
CLAIMS = os.path.join(SESSION, "claims.jsonl")
DESC = os.path.join(SESSION, "DESCRIPTION-v1.7-rev2.html")


def sha(p):
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def text(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read().replace("\r\n", "\n")


gen = text(os.path.join(OUT, "make_description_r2.out.txt"))
ver = text(os.path.join(OUT, "verify_description_r4.out.txt"))
gate = text(os.path.join(OUT, "preflight_deposit_rev2_r3.out.txt"))
gate_blocked = text(os.path.join(OUT, "preflight_deposit_rev2_r2.out.txt"))
self1 = text(os.path.join(OUT, "selftest_readback.out.txt"))
self2 = text(os.path.join(OUT, "selftest_readback_r2.out.txt"))

# ---- reader integrity: assert known-present features, one of them non-ASCII,
# before trusting anything absent (Amendment C, as amended).
assert "₀" in text(DESC), "reader integrity: the description did not read as UTF-8"
assert "double-escaped entities        : 0" in gen
assert "unquoted draft-stage language  : 0" in gen
assert "draft-signoff" in gen, "the sign-off exclusion did not run"

assert "checks run     : 14" in ver and "checks failed  : 0" in ver
assert "broken checks  : 0" in ver and "reader controls: 3 of 3 caught" in ver
assert "VERDICT: OK" in ver
assert "X2 no draft-stage language published -- 3 mutant(s) rejected" in ver
assert "T5 no double-escaped entities -- 2 mutant(s) rejected" in ver

assert "GATE: BLOCKED" in gate_blocked
assert "S3 description is the verified revision" in gate_blocked
assert "GATE: PASSED" in gate and "checks failed  : 0" in gate

assert "VERDICT: BROKEN" in self1 and "a load-bearing sentence lost in the paste" in self1
assert "broken           : 0" in self2 and "VERDICT: OK" in self2

DESC_SHA = sha(DESC)
assert DESC_SHA == "0478e3c9d4690c23636c422dfcf39f1a16290c3db60c33b0779620a2d2ca3ebb"
assert DESC_SHA in gen, "the generator output does not record the file on disk"

H_GEN = sha(os.path.join(OUT, "make_description_r2.out.txt"))
H_VER = sha(os.path.join(OUT, "verify_description_r4.out.txt"))
H_GATE = sha(os.path.join(OUT, "preflight_deposit_rev2_r3.out.txt"))
H_SELF1 = sha(os.path.join(OUT, "selftest_readback.out.txt"))
H_SELF2 = sha(os.path.join(OUT, "selftest_readback_r2.out.txt"))

T = "CT-S27-CTV17-DEPOSIT-PREP/walkthrough"

NEW = [
    ("S27-06",
     "THE DESCRIPTION THAT PASSED 13/13 WOULD HAVE PUBLISHED THE LITERAL TEXT "
     "'&mdash;' IN 77 PLACES. Table rows were joined by ' &mdash; ' and only "
     "THEN markup-escaped, so the ampersand became '&amp;' and every row "
     "separator became the double-escaped '&amp;mdash;'. Check T4 could not "
     "see it: '&amp;mdash;' is well-formed HTML4 with no bare ampersand, so "
     "the defect is wrong at the RENDERED layer, not the markup layer. "
     "Repaired by inlining each cell separately and joining after, and a new "
     "check T5 added which tests the rendered text and rejects 2 of 2 mutants. "
     "Found by reading the generated output, not by any check.",
     "VERIFIED", "computation", H_GEN),

    ("S27-07",
     "CHECK X2 PASSED ON A DESCRIPTION ENDING 'Draft only -- no deposit, no "
     "metadata edit.' X2 exists to stop draft-stage language being published. "
     "It matched four literal strings case-sensitively ('DRAFT ONLY', 'Not "
     "deposited', 'no deposit is authorised', 'draft only'); the published "
     "text read 'Draft only', which matches none. ITS MUTANT WAS DRAWN FROM "
     "ITS OWN STRING LIST -- it inserted 'DRAFT ONLY. Not deposited.' -- so "
     "the mutant could only prove the list is consulted, never that the list "
     "is adequate. A mutant built from the constant it tests is not an "
     "independent control. Repaired to a case-insensitive word-boundary "
     "pattern with an explicit quotation allowance, and given three mutants "
     "none of which appears in the pattern; all three are rejected, the first "
     "being verbatim the sentence that got through.",
     "VERIFIED", "computation", H_VER),

    ("S27-08",
     "THE PUBLISHED-DESCRIPTION SIGN-OFF AND ONE TABLE CELL WERE DRAFT-STAGE "
     "TEXT. The notice ends '*End of draft v1.7 notice. Draft only -- no "
     "deposit, no metadata edit.*' and its version table row read '| v1.7 | "
     "-- | -- | this notice, draft |'. Both are correct IN THE NOTICE, which "
     "is and remains a draft, and false in a publication. Handled as a "
     "declared whole-paragraph exclusion and a declared publication-stage "
     "SUBSTITUTION respectively, each asserted present in the notice and "
     "absent from the description, so a rule that stopped matching fails "
     "closed. Four occurrences of 'draft' remain and are allowed: all four sit "
     "in the single v1.6 erratum sentence that QUOTES the watermark "
     "'DRAFT -- NOT DEPOSITED' of the build it repairs.",
     "VERIFIED", "computation", H_VER),

    ("S27-09",
     "THE DEPOSIT GATE REFUSED THE REPAIRED DESCRIPTION, CORRECTLY. Check S3 "
     "pairs the description on disk with the checker output that passed it; "
     "after regeneration it reported 'the description on disk (0478e3c9) is "
     "not the one the checker passed (e8b3f36f)' and returned GATE: BLOCKED. "
     "The gate was repointed at the current output and additionally now "
     "requires 'checks run     : 14', so a stale output from an earlier and "
     "SMALLER check set is rejected rather than accepted. Re-run: 11 checks, "
     "0 failed, 0 broken, 3 of 3 reader controls, GATE: PASSED.",
     "VERIFIED", "computation", H_GATE),

    ("S27-10",
     "THE POST-PUBLISH READBACK WAS SELF-TESTED OFFLINE BEFORE IT COULD BE "
     "NEEDED. postpublish_readback.py runs once, after an irreversible "
     "publish, against a record that does not exist yet, so it cannot be "
     "debugged when it matters. A fixture mode was added and 1 good plus 10 "
     "negative fixtures built from the HELD v1.6 record: files not imported, "
     "a second file, a DRAFT- filename, wrong build bytes, version left at "
     "1.6, a truncated description, a lost load-bearing sentence, affiliation "
     "drift, a dropped keyword, and the concept DOI overwritten. The good "
     "fixture passes and all 10 negatives are rejected, each on its own named "
     "check.",
     "VERIFIED", "computation", H_SELF2),

    ("S27-11",
     "THE SELF-TEST HARNESS COULD NOT READ THE NAME OF ANY CHECK CONTAINING A "
     "HYPHEN, AND REPORTED A WORKING CHECK AS BROKEN. It parsed failures with "
     "r'\\[FAIL\\] ([^-]+?) --', which stops at the first hyphen, so 'the "
     "load-bearing sentences survived' was unreadable; the check fired and the "
     "harness reported BROKEN. Same class as the CRLF reader defect: the "
     "harness's INPUT PATH was wrong, not its logic, and mutant testing cannot "
     "reach it because a broken reader misreads the mutant too. Caught only "
     "because exactly one arm disagreed with the nine that passed. Repaired "
     "to r'\\[FAIL\\] (.+?) -- '; re-run gives 0 broken.",
     "VERIFIED", "computation", H_SELF1),

    ("S27-12",
     "THE v1.7 UPLOAD WALKTHROUGH DEPARTS FROM ZENODO'S OWN GUIDANCE, "
     "DELIBERATELY AND FOR A REASON THE RECORD ITSELF STATES. Zenodo's "
     "manage-versions help says versioning is for updated FILES and that a "
     "metadata-only change should use Edit. An Edit would OVERWRITE v1.6's "
     "description, which is the deposited erratum text this corpus treats as "
     "authoritative -- destroying the primary source in order to publish a "
     "note about it. The v1.6 description itself rules the class: it records "
     "that its defect (1) is 'repaired by a new version rather than by a "
     "metadata edit'. The walkthrough therefore specifies New version plus "
     "Import files, and instructs that Edit must not be clicked. Confirmed "
     "against help.zenodo.org: the controls are named 'New version' and "
     "'Import files', and a new version draft starts with NO files.",
     "INSPECTED", "file_inspection", H_GATE),
]

existing = set()
if os.path.exists(CLAIMS):
    for line in text(CLAIMS).splitlines():
        if line.strip():
            existing.add(json.loads(line)["claim_id"])

lines = []
for cid, claim, label, ev, h in NEW:
    assert cid not in existing, "claim %s already exists: append-only" % cid
    lines.append(json.dumps({
        "claim_id": cid, "task_id": T, "claim": claim, "label": label,
        "evidence_type": ev, "dps": None, "reproducible": True,
        "script": "scripts/make_description.py, scripts/verify_description.py, "
                  "scripts/preflight_deposit_rev2.py, scripts/selftest_readback.py",
        "output_hash": h}, ensure_ascii=False))

with open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(lines) + "\n")

back = [json.loads(l) for l in text(CLAIMS).splitlines() if l.strip()]
ids = [c["claim_id"] for c in back]
assert len(ids) == len(set(ids)), "duplicate claim ids after append"
for cid, _, _, _, _ in NEW:
    assert cid in ids, "%s did not survive the write" % cid

print("claims.jsonl: %d claims total, %d appended" % (len(back), len(NEW)))
for c in back[-len(NEW):]:
    print("  %s  %-10s  %s..." % (c["claim_id"], c["label"], c["claim"][:72]))
print()
print("description on disk: %s" % DESC_SHA)
