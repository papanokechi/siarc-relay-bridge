"""Emit the revision-3 claims for CT-S26-CTV17-DRAFT.

Append-only.  Refuses to run if any id already exists.  Asserts the revision-3
checker's verdict and counts FROM ITS OUTPUT FILE ON DISK, and cross-checks the
notice hash recorded there against the notice as it now stands, so a claim can
never point at a checker run of a different revision.  Reads back and re-asserts.
"""

import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)

CLAIMS = os.path.join(SESSION, "claims.jsonl")
NOTICE = os.path.join(SESSION, "NOTICE-v1.7.md")
REV3_OUT = os.path.join(SESSION, "outputs", "verify_notice_rev3.out.txt")
AMEND_OUT = os.path.join(SESSION, "outputs", "amend_s3a06.out.txt")

TASK = "CT-S26-CTV17-DRAFT"

EXPECT = {
    "checks run": 26,
    "checks failed": 0,
    "broken checks": 0,
}


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read_text(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw.decode("utf-8").replace("\r\n", "\n")


def main():
    for p in (CLAIMS, NOTICE, REV3_OUT, AMEND_OUT):
        if not os.path.exists(p):
            print("FATAL: missing %s" % p)
            return 2

    out = read_text(REV3_OUT)

    # ---- reader integrity: assert known-present structure before judging it
    for sentinel in ("SECTION 1 -- CHECKS AGAINST THE NOTICE AS WRITTEN",
                     "SECTION 4 -- R9, checked against the corpus record"):
        if sentinel not in out:
            print("FATAL: checker output lacks %r -- read is suspect" % sentinel)
            return 2

    if "VERDICT (rev3): OK" not in out:
        print("FATAL: revision-3 checker output does not carry VERDICT (rev3): OK")
        return 2

    for key, want in EXPECT.items():
        m = re.search(re.escape(key) + r"\s*:\s*(\d+)", out)
        if not m:
            print("FATAL: %r not found in checker output" % key)
            return 2
        got = int(m.group(1))
        if got != want:
            print("FATAL: %s = %d, expected %d" % (key, got, want))
            return 2

    m = re.search(r"controls fired\s*:\s*(\d+) of (\d+)", out)
    if not m or m.group(1) != m.group(2) or int(m.group(2)) != EXPECT["checks run"]:
        print("FATAL: controls-fired line does not read 26 of 26")
        return 2
    if "reader controls     : 3 of 3 caught" not in out:
        print("FATAL: reader controls did not all fire")
        return 2

    # ---- the output must describe THIS notice, not an earlier revision
    notice_hash = sha256_file(NOTICE)
    m = re.search(r"sha256 : ([0-9a-f]{64})", out)
    if not m:
        print("FATAL: no notice sha256 recorded in the checker output")
        return 2
    if m.group(1) != notice_hash:
        print("FATAL: checker output records notice %s but the notice on disk is %s"
              % (m.group(1)[:16], notice_hash[:16]))
        return 2

    rev3_hash = sha256_file(REV3_OUT)
    amend_hash = sha256_file(AMEND_OUT)

    new = [
        {
            "claim_id": "S26C-18",
            "task_id": TASK,
            "claim": (
                "Revision 3 of NOTICE-v1.7.md implements the operator's five rulings of "
                "2026-09-19 and the associated watch item, and passes the revision-3 "
                "checker: 26 checks, 0 failed, 26 of 26 can-fail controls fired, 0 broken, "
                "3 of 3 reader controls caught, VERDICT OK. The revision-3 checker imports "
                "revision 2 rather than reimplementing it, so all 21 revision-2 checks, "
                "their mutants and the three reader controls run unchanged. Notice sha256 "
                + notice_hash + "."
            ),
            "evidence_type": "build",
            "dps": 0,
            "reproducible": True,
            "script": "sessions/2026-09-17/CT-S26-CTV17-DRAFT/scripts/verify_notice_rev3.py",
            "output_hash": rev3_hash,
            "label": "INSPECTED",
        },
        {
            "claim_id": "S26C-19",
            "task_id": TASK,
            "claim": (
                "Ruling 8 applied: the Stage-5B negative for S_{zeta*} is filed under a new "
                "tag op:cc-szeta-closed-form, declared new at v1.7, and is NOT filed under "
                "op:cc-stokes-closed-form. The two problems are distinct: the v1.5 tag, "
                "inherited from the demoted Theorem 3.7(iii), asks whether the CC-channel "
                "connection-coefficient RATIO MATCHES the Riemann-Hilbert datum of "
                "P_V/D_5^(1) at the V_quad tau-parameter; the new tag asks whether one "
                "number admits a multiplicative closed form in a stated basis. The notice "
                "states the non-implication in both directions -- C could have a closed form "
                "with the identification false, and the identification could hold with C "
                "outside every Gamma basis -- and forbids citing the negative as evidence "
                "about the other tag. Checked by check_szeta_tag_separate with 3 mutants."
            ),
            "evidence_type": "file_inspection",
            "dps": 0,
            "reproducible": True,
            "script": "sessions/2026-09-17/CT-S26-CTV17-DRAFT/scripts/verify_notice_rev3.py",
            "output_hash": rev3_hash,
            "label": "STRUCTURAL",
        },
        {
            "claim_id": "S26C-20",
            "task_id": TASK,
            "claim": (
                "Ruling 9 applied: claim S3A-06 is narrowed, not retracted, to the artefact "
                "actually inspected. The string 'Proposition 3.3.A' occurs 4 times in each of "
                "the four held deposited descriptions (v1.3 10.5281/zenodo.19972394, v1.4 "
                "10.5281/zenodo.20585624, v1.5 10.5281/zenodo.22717792, v1.6 "
                "10.5281/zenodo.22782807) and zero times in the v1.3.1 LaTeX source at commit "
                "08aa0e2381b3dc37ee54a3200b7272755ca11d59. Per v1.6 erratum (4) the two "
                "artefacts disagree by construction. The label is unchanged at INSPECTED, the "
                "superseded text is retained verbatim in claim_before_s26c, the CT-R1-AUDIT/R2 "
                "amendment trail is preserved, and a pre-amendment copy of the file is held at "
                "outputs/CT-S3A-ZETA-AUDIT.claims.jsonl.pre-s26c-amend. 9 of 9 checks passed."
            ),
            "evidence_type": "file_inspection",
            "dps": 0,
            "reproducible": True,
            "script": "sessions/2026-09-17/CT-S26-CTV17-DRAFT/scripts/amend_s3a06.py",
            "output_hash": amend_hash,
            "label": "INSPECTED",
        },
        {
            "claim_id": "S26C-21",
            "task_id": TASK,
            "claim": (
                "DISCLOSED LOOSENING. The revision-2 check 'every op:/rem: tag exists in the "
                "deposited record' was replaced at revision 3 so that a tag the notice declares "
                "new at v1.7 is admitted, because ruling 8 requires v1.7 to create a tag, as "
                "v1.6 created op:xi0-singularity-type. The requirement is otherwise unchanged: a "
                "tag neither present in the held deposited text nor declared new still fails. "
                "Per the standing rule the loosening arrives with extra can-fail controls in the "
                "same edit -- 3 mutants where revision 2 had 1, including a tag invented without "
                "declaration and the removal of the declaration that legitimises the new tag. "
                "All 3 fire. Revision 2's script and output file are left untouched."
            ),
            "evidence_type": "file_inspection",
            "dps": 0,
            "reproducible": True,
            "script": "sessions/2026-09-17/CT-S26-CTV17-DRAFT/scripts/verify_notice_rev3.py",
            "output_hash": rev3_hash,
            "label": "INSPECTED",
        },
        {
            "claim_id": "S26C-22",
            "task_id": TASK,
            "claim": (
                "Two further P0 amendments are PROPOSED in "
                "sessions/2026-09-17/CT-S26-CTV17-DRAFT/P0-AMENDMENT.md, lettered consecutively "
                "after the two still pending in CT-S22-STOKES: Amendment C, a check that reads a "
                "file must verify it read it (known-present sentinel before any absence "
                "judgement, plus defective-reader controls, because mutant testing verifies a "
                "check's logic and not its input path); and Amendment D, deposited text is "
                "authoritative and the working tree may be behind it (fetch every version you "
                "characterise, treat the record as right where the two disagree, and never "
                "report repository absence as corpus absence). Both are operator-gated and "
                "neither is in force."
            ),
            "evidence_type": "file_inspection",
            "dps": 0,
            "reproducible": True,
            "script": "sessions/2026-09-17/CT-S26-CTV17-DRAFT/P0-AMENDMENT.md",
            "output_hash": sha256_file(os.path.join(SESSION, "P0-AMENDMENT.md")),
            "label": "INSPECTED",
        },
    ]

    existing = read_text(CLAIMS)
    have = {json.loads(l)["claim_id"] for l in existing.split("\n") if l.strip()}
    clash = sorted({c["claim_id"] for c in new} & have)
    if clash:
        print("FATAL: these ids already exist, refusing to append: " + ", ".join(clash))
        return 2

    before = len(have)
    with open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
        for c in new:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    # ---- read back from disk
    after_rows = [json.loads(l) for l in read_text(CLAIMS).split("\n") if l.strip()]
    after = {c["claim_id"]: c for c in after_rows}
    if len(after_rows) != before + len(new):
        print("FATAL: expected %d claims, found %d" % (before + len(new), len(after_rows)))
        return 2
    for c in new:
        g = after[c["claim_id"]]
        assert g["claim"] == c["claim"], c["claim_id"]
        assert g["label"] in ("INSPECTED", "STRUCTURAL", "VERIFIED", "PROVEN", "CONJECTURED")
        assert re.fullmatch(r"[0-9a-f]{64}", g["output_hash"]), c["claim_id"]
        if g["label"] == "PROVEN" and g["evidence_type"] == "file_inspection":
            print("FATAL: %s violates invariant 1(a)" % c["claim_id"])
            return 2
        print("  [ok] %-9s %-11s %s" % (g["claim_id"], g["label"], g["output_hash"][:16]))

    print()
    print("appended %d claims; claims.jsonl now holds %d" % (len(new), len(after_rows)))
    print("claims.jsonl sha256 (from disk): %s" % sha256_file(CLAIMS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
