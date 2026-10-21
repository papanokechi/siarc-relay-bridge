"""emit_claims_s41.py -- write CT-S41-DRAFT-C/claims.jsonl.

The buffer is validated IN MEMORY before anything is written, so a refusal
never leaves a corrupt artefact on disk.

Three-pass procedure, inherited from CT-S40 and required again here: the
gate prints a [self-exclusion] line whose text depends on whether this file
EXISTS.  So run emit -> re-run the gate -> emit again.  The line depends only
on existence and on the number of files walked, never on contents, so the
digest is stable from the second emission onward.
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parents[1]
OUT = HERE / "claims.jsonl"
LABELS = ("PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED")


def h(rel):
    p = HERE / rel
    if not p.exists():
        raise SystemExit(f"REFUSED: cited output {rel} does not exist")
    return hashlib.sha256(p.read_bytes()).hexdigest()


GATE = "outputs/check_group_c.out.txt"
ASM = "outputs/check_assembly.out.txt"
MUT = "outputs/mutants_assembly.out.txt"
LOG = "outputs/build/combined_0to6.log"

C = [
    dict(claim_id="S41-01", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="build", output=GATE, claim=(
             "Section 5, 'Locating the point', is drafted as paper prose in five "
             "subsections: the dictionary and the entry that failed, the three "
             "hypotheses at System C, the located point, exhaustiveness, and the "
             "membership verdict. It cites S16-06 through S16-14 and S25-01, "
             "S25-02, S25-03, S25-06, together with S16-01, S16-03, S17-07 and "
             "S22-20 as supporting reads. Every cited id was resolved against the "
             "corpus AT WRITING TIME by scripts/claim_index.py, not from memory.")),

    dict(claim_id="S41-02", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="build", output=GATE, claim=(
             "Section 6, 'Removing the projective ambiguity', is drafted as paper "
             "prose in five subsections: trace-freeness is insufficient, the (P,Q) "
             "comparison, the structural reason no twist is needed, which scalar "
             "reduction, and the withdrawal of the caveat. It cites S17-01 to "
             "S17-06, S17-09 to S17-11 and S17-20 to S17-26.")),

    dict(claim_id="S41-03", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="build", output=GATE, claim=(
             "GATE PASSED. 33 distinct cited ids audited across the two sections; "
             "30 carry a label asserted in the prose and 3 are bare citations; 31 "
             "numeric literals audited; 0 failures. Nine control arms, each "
             "mutating an in-memory COPY and required to fire FOR THE NAMED RULE: "
             "wrong label, PROVEN asserted for a STRUCTURAL claim, transposed "
             "digit, wrong exponent, unresolvable id, structurally superseded id, "
             "the field hazard, the gauge hazard, and an emptied section. 9 of 9 "
             "CAUGHT.")),

    dict(claim_id="S41-04", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="computation", output=GATE, claim=(
             "READER DEFECT, caught by the gate's own first run and repaired "
             "before any conclusion was drawn from it. C5 reported that the "
             "literal 10^{-3} in section 6.2 traced to no claim cited there. The "
             "prose was correct: S17-04 records 'a q perturbed by 1e-3 is "
             "rejected'. The value lives in that claim's review_note field, and "
             "the checker's pool was built from the claim field ALONE, so the "
             "check was narrower than the rule PREREG.md F2 states ('the text of "
             "a claim'). This is a false positive of exactly the shape the record "
             "already carries twice - a check reporting ABSENCE when its reader "
             "could not see the content - and it was diagnosed by reading the raw "
             "claim record before editing anything. Repaired by widening the pool "
             "to claim + review_note, which is the pre-registered scope; the two "
             "C5 arms still fire, since a transposed digit is in neither field.")),

    dict(claim_id="S41-05", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="computation", output=GATE, claim=(
             "TWO ARMS WERE MIS-BUILT and reported MISSED for a staging reason "
             "rather than a detection reason; both are recorded rather than "
             "quietly fixed. A-control searched for the citation form "
             "'\\\\textbf{PROVEN} (\\\\texttt{S16-07})' while section 5 writes the "
             "id first, so the mutation site was absent and the arm scored MISSED "
             "on a rule that was never exercised - the arm reported 'SKIPPED "
             "(mutation site absent)' only because that state was made explicit "
             "in the harness. A-bounds commented out \\\\section, which does not "
             "shorten the file, so the byte floor did not move. Repaired to the "
             "actual citation form and to a truncation respectively; both then "
             "CAUGHT. An arm that cannot reach its mutation site is a control "
             "that cannot fire, and is indistinguishable in a summary line from a "
             "rule that does not work.")),

    dict(claim_id="S41-06", label="VERIFIED", script="scripts/check_assembly.py",
         evidence_type="build", output=ASM, claim=(
             "ASSEMBLY 0-6 CLEAN. combined_0to6.tex builds in two passes to 23 "
             "pages with 0 errors, 0 undefined references and 0 multiply-defined "
             "references. 89 distinct labels defined, 62 distinct targets "
             "referenced, all resolving. The forward-reference stub was shrunk "
             "from six entries to four: sec:point and sec:projective are now "
             "defined by sections 5 and 6 themselves, and R2 fails automatically "
             "if a stub entry collides with a drafted section - the rule that "
             "makes the CT-S39 sec:local defect unrepeatable. 7 of 7 assembly "
             "mutant arms CAUGHT after the harness was repointed at this "
             "session's file names; as first copied it died in stage() before "
             "judging anything, which is the copied-harness path-pinning failure "
             "the record already carries.")),

    dict(claim_id="S41-07", label="STRUCTURAL", script="scripts/check_group_c.py",
         evidence_type="file_inspection", output=GATE, claim=(
             "BOTH PRE-DECLARED DRAFTING HAZARDS ARE HONOURED, and each is "
             "checked positively rather than by absence of a wrong phrase. (i) "
             "Section 5.4 names the base field as Q(i sqrt 11), gives the reason - "
             "it is the field in which the matching equations' own coefficients "
             "live, via s+ and delta - and states what pre-adjoining sqrt 3 would "
             "destroy: a degree-2 ideal would present as two degree-1 components "
             "and the Galois statement would evaporate. (ii) The Galois-conjugacy "
             "remark states explicitly that it does NOT close the z-dependent "
             "gauge question, names that question as S17-07 (CONJECTURED) in "
             "section 10, and warns the reader not to infer a connection between "
             "two sqrt-3-flavoured statements. C6 resolves six markers "
             "positively; two arms remove one marker each and both fire.")),

    dict(claim_id="S41-08", label="STRUCTURAL", script="scripts/check_group_c.py",
         evidence_type="file_inspection", output=GATE, claim=(
             "CORRECTION TO THE COMMISSIONING TEXT, recorded rather than silently "
             "resolved. OUTLINE.md revision 6 twice says the Galois conjugacy "
             "'does not close the gauge question (section 4.1)'. Section 4.1 in "
             "that sentence is the outline's OWN open-questions numbering - "
             "OUTLINE.md line 678, '4.1 The z-dependent gauge, and uniqueness of "
             "the representative' - and it becomes the PAPER's section 10, not "
             "the paper's section 4, which is the moduli space. A drafter "
             "following the cross-reference literally would have pointed section "
             "5 at the moduli-space section, producing a reference that resolves, "
             "builds clean and says something false. The drafted prose points at "
             "sec:open. Two numbering schemes share the string 'section 4.1' in "
             "one document; this is the CT-S26 ambiguity in a different guise.")),

    dict(claim_id="S41-09", label="VERIFIED", script="scripts/claim_index.py",
         evidence_type="file_inspection", output=GATE, claim=(
             "LABEL CENSUS OF THE GROUP C CITATIONS, resolved at writing time. "
             "Of the 29 ids the outline assigns to sections 5 and 6: 20 PROVEN, 4 "
             "VERIFIED, 5 STRUCTURAL, 0 INSPECTED, 0 CONJECTURED, 0 superseded, 0 "
             "duplicated, 0 unresolved. The four supporting reads carry INSPECTED "
             "(S16-01, S16-03), VERIFIED (S22-20) and CONJECTURED (S17-07), so "
             "all five labels of Amendment F appear in the two sections. Not one "
             "label was taken from the outline or from memory.")),

    dict(claim_id="S41-10", label="STRUCTURAL", script="scripts/check_group_c.py",
         evidence_type="file_inspection", output=GATE, claim=(
             "WHAT THIS GATE CANNOT SEE, stated as a limit rather than left for a "
             "reader to discover. C5 is a TRANSCRIPTION test: it confirms that a "
             "numeral printed in the prose occurs in the text of a claim cited in "
             "the same subsection. It cannot see a value that is wrong in the "
             "corpus, and it cannot see a transposition inside a numeral of fewer "
             "than three digits - which includes every coefficient of Q_C in "
             "section 6.2 (22, 22, 54, 5) and every digit of the eliminant's 27. "
             "A transposed digit there would pass 33 citation checks, 31 literal "
             "checks and a clean 23-page build. Closing it needs a pass that "
             "re-derives the printed formulas from the corpus scripts, which is "
             "out of this session's scope and is the right task once all sections "
             "exist.")),

    dict(claim_id="S41-11", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="computation", output=GATE, claim=(
             "THE SELF-EXCLUSION CLOSES THE CORPUS-WALK TRAP WITHIN A SESSION "
             "BUT NOT ACROSS SESSIONS. Emitting this session's claims.jsonl "
             "changed the output of CT-S40's draft_check.py, whose gate walks "
             "sessions/ and PRINTS the census: 451 files / 1411 ids became 452 / "
             "1421, on two lines. CT-S40's claims cite the digest of its recorded "
             "output file, and that file on disk is untouched, so no citation is "
             "stranded - all 11 CT-S40 and all 8 CT-S39 output_hash values still "
             "resolve to a file in their own session. What is lost is "
             "REPRODUCIBILITY of the recorded bytes: re-running CT-S40's gate "
             "today no longer reproduces the output its claims cite. Verdict, "
             "failure count and every substantive line are unchanged, and both "
             "upstream gates still exit 0; the diff is exactly the two census "
             "lines. Recorded, not repaired: repairing it would mean either "
             "editing CT-S40's recorded output, which is append-only, or removing "
             "the census from the gate's output, which is the non-vacuity "
             "statement that makes its self-exclusion check readable.")),

    dict(claim_id="S41-12", label="VERIFIED", script="scripts/check_group_c.py",
         evidence_type="computation", output=GATE, claim=(
             "A VACUOUS READER OF MY OWN, caught in this session while checking "
             "S41-11. The first attempt to confirm that CT-S39's and CT-S40's "
             "cited digests still resolved iterated their claim rows, read an "
             "'output' field, and skipped any row lacking one. Neither session's "
             "schema HAS an output field - they carry script and output_hash "
             "only - so every row was skipped and the script printed '0/11 cited "
             "digests still resolve', which reads as total failure and is in fact "
             "a count of zero tests performed. It is S16-11's defect in a new "
             "place: a loop whose body never executes reports whatever its "
             "initialised counter says. Repaired by resolving each output_hash "
             "against a hash of every file in the session tree, which needs no "
             "schema assumption; 8/8, 11/11 and 10/10 then resolved. The false "
             "alarm and the true answer are recorded together because the false "
             "alarm is the more instructive of the two.")),
]


def validate(rows, text):
    """Every check runs against the IN-MEMORY buffer, before any write."""
    p = []

    def ck(name, cond, detail=""):
        p.append((name, bool(cond), detail))

    ids = [r["claim_id"] for r in rows]
    ck("1 ids unique", len(set(ids)) == len(ids))
    ck("2 ids well formed", all(re.fullmatch(r"S41-\d\d", i) for i in ids))
    ck("3 labels in the five", all(r["label"] in LABELS for r in rows))
    ck("4 every row has a script", all(r.get("script") for r in rows))
    ck("5 every row has an output hash",
       all(re.fullmatch(r"[0-9a-f]{64}", r["output_hash"]) for r in rows))
    ck("6 every cited output resolves on disk",
       all(h(r["output"]) == r["output_hash"] for r in rows))
    ck("7 claims non-trivial", all(len(r["claim"]) > 200 for r in rows))
    ck("8 evidence_type legal",
       all(r["evidence_type"] in ("file_inspection", "computation", "build")
           for r in rows))
    ck("9 reproducible flag set", all(r["reproducible"] is True for r in rows))
    ck("10 no label upgraded in prose",
       "PROVEN" not in [r["label"] for r in rows if "not fully" in r["claim"]])
    ck("11 buffer parses as jsonl",
       all(json.loads(l) for l in text.strip().splitlines()))
    ck("12 buffer line count matches", len(text.strip().splitlines()) == len(rows))
    ck("13 gate output records PASSED",
       "GATE: PASSED" in (HERE / GATE).read_text(encoding="utf-8"))
    ck("14 gate output records 0 failures",
       "checks failed : 0" in (HERE / GATE).read_text(encoding="utf-8"))
    ck("15 gate output records 9/9 arms",
       "arms: 9/9 CAUGHT" in (HERE / GATE).read_text(encoding="utf-8"))
    ck("16 assembly output records PASS",
       "VERDICT: PASS" in (HERE / ASM).read_text(encoding="utf-8"))
    ck("17 assembly mutants 7/7",
       "7/7 arms CAUGHT" in (HERE / MUT).read_text(encoding="utf-8"))
    ck("18 build log is the 0-6 build",
       "combined_0to6" in (HERE / LOG).read_text(encoding="utf-8",
                                                 errors="replace"))
    ck("19 defect claims are not silently absent",
       {"S41-04", "S41-05", "S41-08", "S41-10", "S41-11",
        "S41-12"} <= set(ids))
    ck("20 no claim asserts the gauge question is closed",
       not any(re.search(r"gauge question is (now )?(closed|settled)",
                         r["claim"]) for r in rows))

    bad = [(n, d) for n, ok, d in p if not ok]
    for n, ok, d in p:
        print(f"  {'ok  ' if ok else 'FAIL'} {n}{(' -- ' + d) if d else ''}")
    print(f"\n  {len(p) - len(bad)}/{len(p)} pre-write checks passed")
    if bad:
        raise SystemExit("REFUSED: buffer not written; " +
                         "; ".join(n for n, _ in bad))


def main():
    rows = []
    for c in C:
        r = dict(c)
        r["task_id"] = "CT-S41-DRAFT-C"
        r["dps"] = None
        r["reproducible"] = True
        r["review"] = "self"
        r["output_hash"] = h(r["output"])
        rows.append(r)

    order = ["claim_id", "task_id", "claim", "label", "evidence_type", "dps",
             "reproducible", "script", "output", "output_hash", "review"]
    text = "".join(json.dumps({k: r[k] for k in order if k in r},
                              ensure_ascii=True) + "\n" for r in rows)

    print(f"emit_claims_s41 -- {len(rows)} rows, {len(text)} bytes buffered\n")
    validate(rows, text)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    d = hashlib.sha256(OUT.read_bytes()).hexdigest()
    print(f"\n  written: {OUT.name}  {OUT.stat().st_size} B  sha256 {d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
