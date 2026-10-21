#!/usr/bin/env python3
"""emit_claims_s39.py -- AEAL claim record for CT-S39-DRAFT-A.

Validates the in-memory buffer BEFORE writing, so a failed validation leaves
no corrupt artefact on disk.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
OUT = os.path.join(SESS, "outputs")
ART = os.path.join(SESS, "claims.jsonl")
TASK = "CT-S39-DRAFT-A"

LABELS = {"PROVEN", "VERIFIED", "INSPECTED", "STRUCTURAL", "CONJECTURED"}

CHK = "check_group_a.out.txt"
BLD = os.path.join("build", "pass2.log")


def sha_file(name):
    p = os.path.join(OUT, name)
    try:
        with open(p, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError as exc:
        print("READER INTEGRITY FAILED: cannot hash %s (%s)" % (p, exc))
        sys.exit(4)


C = [
    ("S39-01", "VERIFIED",
     "Every citation made by section 2.0 was verified against the HELD page "
     "image or PDF named beside it, not against OUTLINE.md and not against a "
     "claim text. Nine sources resolve to held artefacts in the corpus: "
     "Gautschi 1967 at folios 31 and 35, Odlyzko Asymptotic Enumeration "
     "Methods at folio 77, DLMF 2.9 and 3.6 and 5.11, the DLMF bibliography "
     "entry identifying Wong-Li II, Birkhoff-Trjitzinsky 1933, and Nemes "
     "2026. 102 checks pass with 0 failures and 16 control arms are CAUGHT. "
     "The controls that carry the weight are the decoy-page arms, which "
     "require each fragment to be ABSENT from the leaf before and the leaf "
     "after its own page, and the impossible-folio arm: without them the "
     "check degenerates into 'the fragment is somewhere in the book', which "
     "is not what a page citation asserts.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-02", "VERIFIED",
     "A READER DEFECT IN THE GATE ITSELF, found on its first run and "
     "repaired. Folio resolution originally scanned a 120-character "
     "header/footer band for the folio digits. For Odlyzko folio 77 that band "
     "matched THREE pages: index 63, whose text carries the bibliography "
     "reference '[77, 78, 79]'; index 67, which carries the equation number "
     "'(8.77)'; and index 76, the true page. The scan returned the FIRST, so "
     "the check reported 'folio 77 located' while reading page 64. The "
     "failure surfaced only because the three long quoted fragments were then "
     "absent from that page; shorter or more generic fragments could have "
     "matched on the wrong page and the citation would have been certified "
     "against text it does not contain. Repaired by requiring the folio to "
     "stand alone as the first or last whitespace token of the page's first "
     "or last non-empty line, AND by requiring the resolution to be UNIQUE, "
     "so that two markers are reported as ambiguous rather than silently "
     "resolved to the first. The repaired resolver returns index 76, which "
     "agrees with the offset of -1 recorded independently by CT-S24's "
     "verify_odlyzko_p77.py. Arms A8, A8' and A9 now exercise exactly this: "
     "A8 asserts the band scan IS defective, A8' that the strict resolver "
     "returns the single index 76, A9 that an ambiguous folio resolves to "
     "None.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-03", "INSPECTED",
     "A CLAIM WHOSE TEXT CONTRADICTS ITS OWN LABEL. S1-04, the paper's growth "
     "law, carries the corpus label PROVEN, but its claim text in "
     "CT-S1-THEOREM/claims.jsonl still ends 'Steps 3,4 rest on Gap G1 ... "
     "Hence STRUCTURAL, not PROVEN.' The label is correct and current: "
     "theorem.tex lines 40-46 and 427-436 record that Gap G1 was CLOSED in "
     "audit round R1, and CT-S1-THEOREM/REPORT.md line 8 records the upgrade "
     "STRUCTURAL -> PROVEN explicitly. It is the claim TEXT that is stale, "
     "left behind when the label was raised. Consequences for drafting, both "
     "taken: section 2 states Theorem thm:growth as PROVEN, matching the "
     "label; and it names at the point of use the one classical input that "
     "the closure leaves imported, the normalisation h_infinity = 1 from DLMF "
     "(5.11.12), rather than absorbing it silently. NOT REPAIRED HERE: "
     "amending S1-04's text means editing an earlier session's claims.jsonl, "
     "whose digest later claims cite. Reported for an operator ruling. Note "
     "that CT-S1-THEOREM/REPORT.md also retains three pre-upgrade STRUCTURAL "
     "rows at lines 44, 61 and 239, which are stale for the same reason.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-04", "VERIFIED",
     "THE OUTLINE'S OWN QUOTATION OF ODLYZKO p.77 NEEDED TWO CORRECTIONS, "
     "found by comparing it against the page rather than copying it. (i) The "
     "outline renders the sequence as 'a_n' inside a quoted sentence; the "
     "page sets it as a subscripted symbol, so the paper typesets it as maths "
     "inside the quotation rather than reproducing an underscore. (ii) The "
     "outline's second quotation ends 'in the complicated proofs.' where the "
     "page reads 'in the complicated proofs [211, 383].' -- the quotation "
     "silently dropped two reference numbers and closed the sentence early. "
     "The drafted text restores them. Both were invisible to any check that "
     "compares the draft with the outline, and visible immediately to one "
     "that compares the draft with the page. The substantive content the "
     "page forces is confirmed unchanged: the 'up to a multiplicative "
     "constant' half is Odlyzko REPORTING Wimp and Zeilberger, his reference "
     "[384], and only the following sentence is his own; and the same page "
     "carries the objection that the Birkhoff-Trjitzinsky results 'may not be "
     "rigorous'.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-05", "STRUCTURAL",
     "Section 0 is drafted as paper prose. It states the recurrence, the "
     "growth result and the leaf result, and states BOTH limits in the "
     "introduction rather than in a closing section: leaf membership is a "
     "numerical agreement and is not proven, and no Painleve label is "
     "asserted for the recurrence, the classification question being "
     "addressed only by excluding one row. The method paragraph is written to "
     "the standing ruling: it leads with the exact recurrence and its "
     "absolutely summable increments, and mentions Pincherle only afterwards "
     "and only to say the interpretation is not used. That ordering is "
     "enforced by check F6c, which compares the POSITION of the two phrases "
     "inside the paragraph rather than scanning a fixed-length window; the "
     "first version of that check used a 420-character window and failed on "
     "correct prose, because section 0 must mention Pincherle in order to "
     "disclaim it.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-06", "VERIFIED",
     "Section 2 is drafted with the attribution subsection PLACED FIRST, "
     "which check F6d asserts positionally rather than trusting the heading. "
     "Every claim id cited resolves to exactly one corpus claim and every "
     "label printed in the prose equals the corpus label, checked against the "
     "corpus at draft time and not from memory: S1-01, S1-02, S1-03, S1-04, "
     "S26-01 and S3B-03 PROVEN; S26-04, S2-01, S3B-02, S3B-08 and S3B-09 "
     "VERIFIED; S1-05 STRUCTURAL; the CT-S8-LITCHECK and S24 readings "
     "INSPECTED. The deliberately wrong label required as a control is arm "
     "A5, which mutates S1-05 from STRUCTURAL to PROVEN and is CAUGHT. Five "
     "further prohibitions are machine-checked: no Painleve label for the "
     "recurrence, Proposition U carrying S26-01 and not S1-02, Wong-Li II "
     "stated NOT OBTAINED, the Wimp-Zeilberger attribution split stated, and "
     "DLMF 5.11.12 named at the point of use.",
     "file_inspection", CHK, "check_group_a.py"),
    ("S39-07", "VERIFIED",
     "The Group A standalone builds at 9 pages with ZERO undefined "
     "references, over sections 0, 1 and 2. Sections 3-10 do not exist yet, "
     "so eight forward references could not resolve; rather than weaken the "
     "prose to avoid them, a build-only stub declares those eight labels at "
     "the section numbers OUTLINE.md revision 6 assigns. The stub is a "
     "hazard of exactly the kind this corpus has been repairing, because a "
     "number that drifted from the outline would print a WRONG cross-"
     "reference with no warning, so check F7 resolves all eight against the "
     "outline's own headings, asserts the stub is inputted by the standalone "
     "wrapper alone and by no section file, and arm A10 fires when a stub "
     "number is drifted. Arm A11 reads the RENDERED PDF and confirms the "
     "attribution material reaches the page -- a check on the .tex alone "
     "cannot distinguish 'written' from 'rendered' -- and confirms the stub's "
     "own warning text does not.",
     "build", CHK, "check_group_a.py"),
    ("S39-08", "INSPECTED",
     "REQUIRED ACTIONS FOR THE GROUP B RE-RUN, now unblocked because section "
     "2 exists. (1) Remove the CT- alias from CT-S37-DRAFT-B/scripts/"
     "draft_check.py, which was retained only because OUTLINE.md cited the "
     "bare short form; that citation was repaired at S38-18, so the alias is "
     "now a workaround for a defect that no longer exists. (2) Invert mutant "
     "M7 in mutants_draft_check.py: it currently expects the bare short form "
     "to RESOLVE, and once the alias is gone the short form must FAIL. (3) "
     "Correct the hardcoded NOTE at draft_check.py lines 195-196, which "
     "prints 'OUTLINE.md cites this family as S9-PVPARAMS-*' and is now "
     "FALSE. All three belong in the same edit, and re-running draft_check.py "
     "changes its output digest, which is why they were not done from this "
     "session.",
     "file_inspection", CHK, "check_group_a.py"),
]


def main():
    rows = []
    for cid, label, text, ev, outfile, script in C:
        rows.append({
            "claim_id": cid,
            "task_id": TASK,
            "claim": text,
            "label": label,
            "evidence_type": ev,
            "dps": None,
            "reproducible": True,
            "script": "scripts/" + script,
            "output_hash": sha_file(outfile),
            "output_file": "outputs/" + outfile,
        })
    rows[2]["review_note"] = (
        "S39-03 reports a defect in an EARLIER session's record and does not "
        "repair it. Re-derivable from theorem.tex and CT-S1-THEOREM/REPORT.md "
        "directly; needs an operator ruling before any edit, because the file "
        "carries digests that later claims cite."
    )

    buf = "\n".join(json.dumps(r, ensure_ascii=True) for r in rows) + "\n"

    print("emit_claims_s39 -- pre-write validation")
    parsed = [json.loads(l) for l in buf.strip().split("\n")]
    checks = [
        ("every line parses as JSON", len(parsed) == len(C)),
        ("claim ids unique",
         len({r["claim_id"] for r in parsed}) == len(parsed)),
        ("every label is one of the five (P0 amendment F)",
         all(r["label"] in LABELS for r in parsed)),
        ("every claim text is substantive",
         all(len(r["claim"].strip()) > 120 for r in parsed)),
        ("every output_hash is 64 hex",
         all(len(r["output_hash"]) == 64 for r in parsed)),
        ("every output_hash resolves to its file on disk",
         all(r["output_hash"] == sha_file(r["output_file"][len("outputs/"):])
             for r in parsed)),
        ("every script exists",
         all(os.path.exists(os.path.join(SESS, r["script"]))
             for r in parsed)),
        ("S39-02 records the folio reader defect and its repair",
         any(r["claim_id"] == "S39-02" and "index 76" in r["claim"]
             and "bibliography reference" in r["claim"] for r in parsed)),
        ("S39-03 carries the review_note marking it unrepaired",
         parsed[2].get("review_note", "").startswith("S39-03 reports")),
        ("no claim asserts a Painleve label for the recurrence",
         not any("V_quad is PV" in r["claim"] for r in parsed)),
    ]
    bad = 0
    for label, good in checks:
        print("  %-56s %s" % (label, "ok" if good else "FAILED"))
        bad += 0 if good else 1
    if bad:
        print("HALT: %d pre-write check(s) failed; nothing written." % bad)
        sys.exit(1)

    blob = buf.encode("utf-8")
    assert b"\r" not in blob
    with open(ART, "wb") as fh:
        fh.write(blob)
    with open(ART, "rb") as fh:
        disk = fh.read()
    if hashlib.sha256(disk).hexdigest() != hashlib.sha256(blob).hexdigest():
        print("HALT: read-back does not match the validated buffer")
        sys.exit(1)

    print()
    print("  claims written : %d" % len(parsed))
    print("  checks run     : %d" % len(checks))
    print("  checks failed  : 0")
    print("  claims.jsonl   : %d B  sha256 %s"
          % (len(blob), hashlib.sha256(blob).hexdigest()))
    print("  VERDICT: CLAIMS EMITTED")


if __name__ == "__main__":
    main()
