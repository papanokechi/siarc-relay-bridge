#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
emit_claims_rev2.py -- append claims S26C-09..S26C-17 to claims.jsonl.

Appends only.  Refuses to run if any id it is about to write already exists, and
refuses to run unless the rev-2 checker output on disk carries VERDICT: OK with
the expected counts AND the sha256 of the notice as it now stands.  Every hash
is taken from disk after the artefact is final -- never from an in-memory
string -- because a claim's hash must point at the bytes a reader will fetch.
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
OUT = os.path.join(SESSION, "outputs", "verify_notice_rev2.out.txt")
REFS = os.path.join(SESSION, "refs")


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    for p in (CLAIMS, NOTICE, OUT):
        if not os.path.exists(p):
            print("FATAL: missing %s" % p)
            return 2

    out = open(OUT, "rb").read().decode("utf-8").replace("\r\n", "\n")
    # reader integrity for THIS script too: assert a known-present feature
    # before trusting any absence-sensitive assertion below.
    assert "SECTION 3 -- READER CONTROLS" in out, "checker output not read correctly"
    assert "VERDICT: OK" in out, "the rev-2 checker did not return OK"
    assert "checks failed       : 0" in out, "the rev-2 run has failing checks"
    assert "controls fired      : 21 of 21" in out, "not all mutant controls fired"
    assert "broken checks       : 0" in out, "the rev-2 run has broken checks"
    assert "reader controls     : 3 of 3 caught" in out, "a reader control escaped"

    notice_hash = sha256(NOTICE)
    m = re.search(r"sha256 : ([0-9a-f]{64})", out)
    assert m, "the checker output carries no notice hash"
    assert m.group(1) == notice_hash, (
        "the checker output was produced against a DIFFERENT notice "
        "(%s on disk, %s in the output) -- re-run the checker" % (notice_hash, m.group(1)))

    out_hash = sha256(OUT)

    def ref(name):
        p = os.path.join(REFS, name)
        assert os.path.exists(p), "missing ref %s" % name
        return sha256(p)

    z16 = ref("zenodo_22782807.json")
    z16d = ref("zenodo_22782807.description.txt")
    dcc = ref("datacite_concept.json")

    rows = [
        ("S26C-09", "fetch",
         "THE CHANNEL THEORY VERSION MAP IS READ FROM LIVE RECORDS, NOT RECONSTRUCTED. "
         "v1.1 = 10.5281/zenodo.19941679, v1.2 = 19951331, v1.3 = 19972394 (2026-05-02), "
         "v1.4 = 20585624 (2026-06-07), v1.5 = 22717792 (2026-09-12), "
         "v1.6 = 22782807 (2026-09-16). v1.5 and v1.6 were read from zenodo.org/api/records; "
         "v1.3 and v1.4 from api.datacite.org after zenodo.org began returning HTTP 504 on "
         "every further request. DataCite lists exactly six HasVersion identifiers for the "
         "concept DOI and no v1.0 version DOI appears among them; that is reported as read "
         "and is not explained here.",
         "INSPECTED", "file_inspection", dcc),
        ("S26C-10", "fetch",
         "THE CONCEPT DOI AND THE VERSION NUMBER ARE CONFIRMED AGAINST THE LIVE RECORD. "
         "10.5281/zenodo.19941678 was read from the conceptdoi field of record 22782807 and "
         "independently from DataCite -- never from a record number. The concept record "
         "currently resolves to version 1.6, so v1.7 is the correct next number. This closes "
         "the version-number limb of REPORT.md section 6 question 1.",
         "INSPECTED", "file_inspection", z16),
        ("S26C-11", "fetch",
         "op:xi0-singularity-type AND rem:d3-vacuous ARE REAL, AND op:xi0-d3-direct IS "
         "WITHDRAWN, NOT SUBSUMED. All three were introduced at v1.6: op:xi0-d3-direct is "
         "withdrawn as VACUOUS (the observable does not depend on the structure it was posed "
         "to probe), op:xi0-singularity-type replaces it, and rem:d3-vacuous records the "
         "withdrawal. An earlier finding in this session reported op:xi0-singularity-type as "
         "having zero occurrences; that was true OF THE REPOSITORY and false of the corpus. "
         "A repo-wide search establishes absence from the repo, not absence from the record.",
         "INSPECTED", "file_inspection", z16d),
        ("S26C-12", "fetch",
         "v1.6's VACUITY EVIDENCE IS AN EMPIRICAL SWEEP, QUOTED HERE AND NOT RECOMPUTED. "
         "Holding beta_3 fixed and varying beta_2, beta_1, beta_0 over -1000..+999 moves xi_0 "
         "by 6.85e-18, while varying beta_3 alone moves it by 1.26e-1. NOTICE-v1.7.md section 5 "
         "derives the same phenomenon for every d and for xi_0 AND rho from two proved "
         "statements with no sweep, and retains the sweep as independent confirmation. Whether "
         "S_zeta* passes v1.6's analogous pre-check is NOT settled: S_zeta* is a different "
         "object and nothing in section 5 decides it.",
         "INSPECTED", "file_inspection", z16d),
        ("S26C-13", "fetch",
         "THE PAINLEVE TARGET WAS CORRECTED IN THE RECORD TWO VERSIONS AGO. v1.4 (2026-06-07) "
         "replaced P-III(D6) throughout -- body, keywords and description -- by the Painleve V "
         "transcendent on the Sakai surface D5^(1) (W(A3^(1)), delta = -1/2 != 0); v1.5 marked "
         "that identification CONJECTURAL, citing companion Conjecture 4.1 "
         "(10.5281/zenodo.20455089, read at v1.2). Working material in this repository still "
         "says P-III(D6) and is stale. v1.5 also demoted Theorem 3.7(iii) to "
         "op:cc-stokes-closed-form, and recorded the same ~1.7 percent unexplained residual "
         "and explicit halving that CT-S3A located independently in the code.",
         "INSPECTED", "file_inspection", z16d),
        ("S26C-14", "fetch",
         "THE EBR GROUNDING IS SUPERSEDED IN SCOPE, NOT WITHDRAWN. The v1.4 grounding "
         "(10.5281/zenodo.20564079 section 3; D-finite G, leading coefficient "
         "a_2d(s) = d^d s^2d (d^d - beta_d s), roots {0, R}, Pringsheim) proves the xi_0 "
         "identity only for positivity families b(n) > 0, only for the physical "
         "generating-function object, with a Lean-checked algebraic layer at d = 2..5, and by "
         "its own section 8 is NOT a symbolic-degree formal proof. The Perron-Kreuser plus "
         "Pincherle route stated at v1.7 needs no positivity hypothesis, is not restricted to "
         "the physical object, and has no degree ceiling. The EBR argument remains valid on "
         "its own narrower scope.",
         "INSPECTED", "file_inspection", z16d),
        ("S26C-15", "fetch",
         "THE v1.5 AND v1.6 PDFs WERE NOT OBTAINED, SO NO FALSIFIER TEXT IS QUOTED. Both file "
         "endpoints returned HTTP 504 (api/records/.../files/.../content and the classic "
         "records/.../files/...?download=1), retried. Expected sizes and md5s are read from the "
         "records' own files[] entries (609300 B / aa56a94a9354b5533b04c89461950eb1 for v1.6; "
         "620544 B / a197906025f6428173f30b2c912a5dc4 for v1.5) and are NOT hashes of files "
         "held. Consequence: section 9 of both PDFs -- the open-problems section carrying the "
         "v1.6 falsifier statements and their numeric thresholds -- has not been read, and "
         "NOTICE-v1.7.md section 6.3 says so rather than restating a falsifier it cannot see.",
         "INSPECTED", "file_inspection", z16),
        ("S26C-16", "revision",
         "NOTICE-v1.7.md AT REVISION 2 PASSES 21 OF 21 CHECKS WITH 21 OF 21 MUTANT CONTROLS "
         "FIRING AND 0 BROKEN. Revision 2 fills the v1.3-v1.6 erratum rows from the deposited "
         "descriptions, corrects the Painleve target, scopes the EBR supersession, generalises "
         "rem:d3-vacuous, adds op:cc-stokes-closed-form and op:xi0-singularity-type to the "
         "open-problem table, and corrects this session's own repo-absence finding in place. "
         "Six checks are new, including one asserting that every op:/rem: tag the notice names "
         "occurs in a held deposited text, so no obligation tag can be invented.",
         "INSPECTED", "file_inspection", out_hash),
        ("S26C-17", "control",
         "A CHECK THAT READS A FILE MUST ALSO VERIFY THAT IT READ IT, AND THAT CONTROL CLASS IS "
         "NOW IMPLEMENTED. Mutant testing verifies a check's LOGIC, not its INPUT PATH: a broken "
         "reader rejects the mutant too, for the same wrong reason, so the can-fail control "
         "fires while the check reports a false absence -- exactly the rev-1 CRLF defect. "
         "verify_notice_rev2.py therefore asserts known-PRESENT sentinels (title line, at least "
         "four fence-plus-newline markers, four non-ASCII characters, no CR) before any check "
         "evaluates a known-absent feature, and SECTION 3 re-reads the file through three "
         "deliberately defective readers -- binary without CRLF normalisation, latin-1, and "
         "silently truncated. All three are caught, 3 of 3.",
         "STRUCTURAL", "file_inspection", out_hash),
    ]

    existing = set()
    for line in open(CLAIMS, encoding="utf-8"):
        line = line.strip()
        if line:
            existing.add(json.loads(line).get("claim_id"))
    clash = [r[0] for r in rows if r[0] in existing]
    if clash:
        print("FATAL: refusing to overwrite existing ids: %s" % ", ".join(clash))
        return 2

    with open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
        for cid, task, claim, label, ev, oh in rows:
            rec = {
                "claim_id": cid,
                "task_id": "CT-S26-CTV17-DRAFT/" + task,
                "claim": claim,
                "label": label,
                "evidence_type": ev,
                "dps": None,
                "reproducible": True,
                "script": "scripts/verify_notice_rev2.py",
                "output_hash": oh,
            }
            fh.write(json.dumps(rec, ensure_ascii=True) + "\n")

    # read back what was written, from disk
    got = {}
    for line in open(CLAIMS, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            got[r["claim_id"]] = r
    for cid, _t, _c, label, _e, oh in rows:
        assert cid in got, "%s was not written" % cid
        assert got[cid]["label"] == label, "%s label mismatch on read-back" % cid
        assert got[cid]["output_hash"] == oh, "%s hash mismatch on read-back" % cid
        assert len(got[cid]["output_hash"]) == 64, "%s hash is not a sha256" % cid

    print("appended %d claims; claims.jsonl now holds %d" % (len(rows), len(got)))
    print("notice sha256 : %s" % notice_hash)
    print("output sha256 : %s" % out_hash)
    for cid, _t, _c, label, _e, oh in rows:
        print("  %s  %-10s  %s" % (cid, label, oh[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
