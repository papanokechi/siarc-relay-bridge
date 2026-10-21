"""emit_claims_s36.py -- AEAL claim record for CT-S36-DRAFT-NOTATION.

Validation order (per the standing rule): build the exact BYTES destined for
disk, validate those bytes, and only then write.  A post-write assertion leaves
the corrupt artefact on disk.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
OUT = HERE / "claims.jsonl"


def h(rel):
    p = HERE / rel
    if not p.exists():
        print("MISSING artefact: %s" % rel)
        sys.exit(1)
    return hashlib.sha256(p.read_bytes()).hexdigest()


C = [
 dict(claim_id="S36-01", task_id="CT-S36/1",
      claim="Proposition U (upper bound on q_infinity in the positive case) is "
            "folded into theorem.tex immediately after prop:positive, as "
            "prop:upper with displays (U-finite) and (U-limit), transcribed "
            "from CT-S26-UPPER-BOUND/PROOF.md and claim S26-01.",
      label="STRUCTURAL", evidence_type="file_inspection", dps=None,
      reproducible=True, script="scripts/verify_artefacts.py",
      output_hash=h("outputs/verify_artefacts.out.txt"),
      review_note="The proposition itself is PROVEN at S26-01; this claim is "
                  "only that it has been transcribed faithfully into the paper "
                  "file, which is a file-inspection matter, not a proof."),
 dict(claim_id="S36-02", task_id="CT-S36/1",
      claim="The edited theorem.tex compiles under pdflatex in two passes with "
            "exit 0 and produces an 8-page PDF; the log contains no 'There "
            "were undefined references'. The only warning (OT1/cmr/bx/sc font "
            "shape) is present in the baseline build of the unedited file and "
            "is therefore pre-existing.",
      label="VERIFIED", evidence_type="build", dps=None, reproducible=True,
      script="outputs/build_propU_2.log", output_hash=h("theorem.pdf")),
 dict(claim_id="S36-03", task_id="CT-S36/1",
      claim="theorem.tex sha256 before edit "
            "74b6a6354403f9c9d057ef76b9d4406afc9c5b1b8aff68adf62c91fc9048d577, "
            "after edit "
            "3d66d72fe1dfc5eba461ea1355ac10a1392457b9aaf78c82cfa9744daddb2695. "
            "The CT-S1 PDF artefact (efb8773d...) does not reproduce "
            "byte-for-byte on this MiKTeX install, so the honest 'old' PDF for "
            "comparison is the baseline rebuild of the UNEDITED file, "
            "49e58762c81c73e45add6fb6e1d79127587de80ed37b51b9d9c0d180e9b5369e.",
      label="VERIFIED", evidence_type="file_inspection", dps=None,
      reproducible=True, script="outputs/build_baseline_2.log",
      output_hash=h("refs/theorem-baseline-rebuild.pdf"),
      review_note="Reporting the non-reproducing original rather than quoting "
                  "the CT-S1 hash as if this toolchain had produced it."),
 dict(claim_id="S36-04", task_id="CT-S36/2",
      claim="Section 1, 'Notation and standing conventions', is drafted as "
            "paper prose in section1.tex (13660 bytes, 9 subsections) and "
            "compiles standalone to a 4-page PDF with no undefined references.",
      label="VERIFIED", evidence_type="build", dps=None, reproducible=True,
      script="outputs/build_section1_2.log", output_hash=h("section1.tex")),
 dict(claim_id="S36-05", task_id="CT-S36/3",
      claim="Of the 171 used-before-defined items reported by the isolated "
            "reader of CT-S23, section 1 as drafted defines 40; 5 are defined "
            "elsewhere in the assembled material; 126 remain STILL UNDEFINED. "
            "The 126 are the session's output and no threshold is placed on "
            "them.",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/check_171.py",
      output_hash=h("outputs/check_171.out.txt")),
 dict(claim_id="S36-06", task_id="CT-S36/3",
      claim="The pre-registered control, item 054 'apparent singularity', "
            "deliberately left undefined in section 1, is reported STILL "
            "UNDEFINED. Separately, all 30 definitions the session task names "
            "explicitly resolve to verified anchors in section1.tex.",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/check_171.py",
      output_hash=h("outputs/check_171.out.txt")),
 dict(claim_id="S36-07", task_id="CT-S36/3",
      claim="check_171.py is sensitive to the material it rules on: 8 of 8 "
            "mutant arms are CAUGHT with exit 1 for the stated reason and no "
            "traceback. Arms M1-M4 damage section 1 by prose heading, drawn "
            "from outside the check's own anchor list (P0 Amendment E).",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/mutants_171.py",
      output_hash=h("outputs/mutants_171.out.txt")),
 dict(claim_id="S36-08", task_id="CT-S36/3",
      claim="The check failed on its first complete run, on two of its own "
            "rulings: items 024 and 035 were ruled DEFINED IN SECTION 1 with "
            "anchors written as raw strings containing a literal backslash-n, "
            "two characters rather than a line break, so whitespace flattening "
            "could not match them and the anchors were absent. The rulings "
            "were corrected, not the check.",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/check_171.py",
      output_hash=h("outputs/check_171.out.txt"),
      review_note="This is the check doing the job the task asked of it: a "
                  "ruling of 'defined' that is not true is reported as ANCHOR "
                  "MISSING and exits 1."),
 dict(claim_id="S36-09", task_id="CT-S36/3",
      claim="Three of eight mutant arms initially reported MISSED, exposing "
            "two instrument defects in check_171.py: (i) an integrity "
            "assertion fingerprinting section 1 by an exact subsection count "
            "of 9, which fired before the anchor stage on M1 and M3 and would "
            "also have failed on any legitimate edit; (ii) an undecodable "
            "input raising UnicodeDecodeError before integrity ran, so M7 "
            "crashed rather than reporting a reader failure. Repaired to a "
            "non-vacuity bound and to a read that reports an undecodable file "
            "in the same words as any other failure to see the content.",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/mutants_171.py",
      output_hash=h("outputs/mutants_171.out.txt"),
      review_note="Both defects would have left the check passing while blind "
                  "to the thing it was built to detect; neither was visible by "
                  "reading the code."),
 dict(claim_id="S36-10", task_id="CT-S36/3",
      claim="The check surfaced three defects in section 1 itself: "
            "'indicial exponent' was used in section 1.4 without being defined "
            "there (repaired, item 170 now DEFINED IN SECTION 1); the "
            "uniformiser u = sqrt(z) is named without its branch (item 171, "
            "left undefined and deferred by section 1.9); and the branch of "
            "zeta = w^(1/d) is likewise deferred (item 014).",
      label="VERIFIED", evidence_type="computation", dps=None,
      reproducible=True, script="scripts/check_171.py",
      output_hash=h("outputs/check_171.out.txt")),
 dict(claim_id="S36-11", task_id="CT-S36/2",
      claim="The three r-objects are renamed in the paper as q_n (normalised "
            "denominator sequence), q_infinity (its limit) and lambda_1..."
            "lambda_d (roots of b), with exactly one footnote giving the "
            "correspondence to the deposited names r_n, r_infinity, r_1...r_d. "
            "The ruling at S24-08 requires a renaming and one footnote but "
            "does not fix the new names; these are the drafter's choice.",
      label="CONJECTURED", evidence_type="file_inspection", dps=None,
      reproducible=True, script="scripts/verify_artefacts.py",
      output_hash=h("outputs/verify_artefacts.out.txt"),
      review_note="Operator decision outstanding: the letters themselves are "
                  "not ruled on. rho was avoided for the limit because rho is "
                  "already the Borel-plane exponent."),
 dict(claim_id="S36-12", task_id="CT-S36/2",
      claim="Section 1 records a fourth object written with the letter r that "
            "the CT-S23 audit did not list: van der Put-Saito's Katz invariant "
            "r(c), whose Table 2.1 columns are r(0), r(1), r(infinity), r(t). "
            "It is unrelated to the three r-objects and is one further reason "
            "for the renaming.",
      label="STRUCTURAL", evidence_type="file_inspection", dps=None,
      reproducible=True, script="scripts/verify_artefacts.py",
      output_hash=h("outputs/verify_artefacts.out.txt")),
]

def main():
    ids = [c["claim_id"] for c in C]
    assert len(ids) == len(set(ids)), "duplicate claim_id"
    allowed = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED"}
    for c in C:
        assert c["label"] in allowed, "bad label in %s" % c["claim_id"]
        assert c["claim"].strip() and len(c["claim"]) > 40, c["claim_id"]
        assert c["evidence_type"] in {"file_inspection", "computation", "build"}
        assert len(c["output_hash"]) == 64, c["claim_id"]
        assert c["script"].strip(), c["claim_id"]

    blob = "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in C).encode("utf-8")
    # validate the exact bytes destined for disk, BEFORE writing
    assert b"\r" not in blob, "CR in output bytes"
    assert blob.count(b"\n") == len(C), "line count mismatch"
    for line in blob.decode("utf-8").splitlines():
        json.loads(line)
    OUT.write_bytes(blob)

    got = hashlib.sha256(OUT.read_bytes()).hexdigest()
    assert got == hashlib.sha256(blob).hexdigest(), "disk does not match buffer"
    print("wrote %s" % OUT)
    print("claims: %d" % len(C))
    print("sha256: %s" % got)
    for c in C:
        print("  %-8s %-12s %s" % (c["claim_id"], c["label"], c["claim"][:74]))


if __name__ == "__main__":
    main()
