"""emit_claims_s42.py -- write CT-S42-DRAFT-D/claims.jsonl.

TWO RULES THIS SCRIPT EXISTS TO OBEY.

1. VALIDATE THE IN-MEMORY BUFFER BEFORE WRITING.  A post-write assertion
   still leaves the corrupt artefact on disk (CT-S28 6.3, CT-S32 M6).  Every
   check below runs against `buf`; the file is opened only after all of them
   pass.

2. THE THREE-PASS PROCEDURE.  The gate's [self-exclusion] line reports whether
   this session's claims.jsonl EXISTS.  Emitting it changes that line, so the
   digest recorded by pass 1 would be stale.  Procedure:
        pass 1  python scripts/emit_claims_s42.py
        pass 2  python scripts/check_group_d.py > outputs/check_group_d.out.txt
        pass 3  python scripts/emit_claims_s42.py
   After pass 3 the output is stable, because the line depends only on the
   file's EXISTENCE and the file COUNT, never on its contents.  Pass 3 must
   leave the gate output byte-identical, and that is checked separately.

NON-VACUITY ON THE NUMERATOR.  Every count this script prints is asserted
non-zero before it is printed (operator ruling, CT-S41 review: "a count
printed as a fraction with zero numerator and a nonzero denominator is the
signature").
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parents[1]
SESSIONS = HERE.parents[1]
OUT = HERE / "claims.jsonl"
TASK = "CT-S42-DRAFT-D"


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


G = "outputs/check_group_d.out.txt"
A = "outputs/check_assembly.out.txt"
M = "outputs/mutants_assembly.out.txt"
B = "outputs/build2.txt"

C = [
 dict(claim_id="S42-01", label="INSPECTED", evidence_type="file_inspection",
      script="section7.tex",
      claim="Section 7 'Monodromy, Stokes data, and the character variety' is "
            "drafted as paper prose in five subsections from the claim texts "
            "of S22-01 through S22-14, dumped in full to outputs/claims_s7.txt "
            "and read there rather than from the outline's paraphrase. The "
            "trace coordinates x1 = tr(B2 B3), x2 = tr(B1 B3), x3 = tr(B1 B2) "
            "with a_i = tr(B_i) = 2 are restated in the section, discharging "
            "the outline's repair R-(d).",
      review_note="S22-04 and S22-05 are kept OUT of the main text, as the "
                  "outline directs: both were vacuous as first written, and "
                  "the corrected form of the second is a DEPENDENT restatement "
                  "of checks already counted. Section 7 defers them to the "
                  "methods appendix, which Group E owes."),
 dict(claim_id="S42-02", label="INSPECTED", evidence_type="file_inspection",
      script="section8.tex",
      claim="Section 8 'Transport along the leaf, and the second branch' is "
            "drafted as paper prose in six subsections from the claim texts of "
            "S22-15 through S22-20, S22-23, S22-24 and S25-02, dumped in full "
            "to outputs/claims_s8.txt."),
 dict(claim_id="S42-03", label="VERIFIED", evidence_type="build",
      script="scripts/check_group_d.py", output_hash=None, _hash=G,
      claim="The Group D drafting gate PASSES: 23 distinct claim ids audited, "
            "98 numeric literals audited against a floor of 20, 3 stub labels "
            "tested, 0 failures, and 11 of 11 control arms CAUGHT. 21 of the "
            "23 citations carry a label in the prose and every one matches the "
            "corpus.",
      review_note="The arms include the deliberately wrong label the standing "
                  "rule requires: S22-15 relabelled PROVEN. It is chosen "
                  "because S22-15's own text says the agreement 'is not a "
                  "proof of leaf membership', so relabelling it PROVEN is the "
                  "exact error the paper must not make."),
 dict(claim_id="S42-04", label="VERIFIED", evidence_type="build",
      script="preamble.tex", _hash=B,
      claim="Operator ruling 2 is applied: preamble.tex is the single "
            "authoritative preamble, loading hyperref exactly once, and "
            "combined_0to8.tex \\inputs it and declares no package of its own. "
            "No per-group wrapper is written in this session. The defect this "
            "closes is that Group A's wrapper did not load hyperref while "
            "Group B's did, so the two gates were passing on two different "
            "documents, neither of which was the assembled one."),
 dict(claim_id="S42-05", label="INSPECTED", evidence_type="file_inspection",
      script="scripts/check_group_d.py", _hash=G,
      claim="Operator ruling 1 is applied: the gate prints the corpus census "
            "(453 claims.jsonl files, 1434 unique ids) TOGETHER WITH a "
            "fingerprint, a sha256 over the sorted list of the 453 walked "
            "paths, and states in its own output that no claim of "
            "byte-reproducibility across sessions is made. A differing count "
            "with a differing fingerprint is a different input, not a "
            "disagreement."),
 dict(claim_id="S42-06", label="VERIFIED", evidence_type="build",
      script="combined_0to8.tex", _hash=A,
      claim="Sections 0 through 8 assemble: 29 pages, 0 errors, 0 undefined "
            "references, 0 multiply-defined labels; 103 labels defined, 70 "
            "referenced targets all resolving, 3 stub entries none of which "
            "collides with a drafted section. check_assembly.py PASSES and "
            "mutants_assembly.py catches 7 of 7 arms."),
 dict(claim_id="S42-07", label="PROVEN", evidence_type="computation",
      script="scripts/check_group_d.py", _hash=G,
      claim="The gate's first run failed with one D6 hit and one arm SKIPPED, "
            "and BOTH were defects in the reader, not in the prose. (i) The "
            "hazard needle 'is the output of' did not match prose reading 'is "
            "therefore the output of'. (ii) Arm D6b could not reach its "
            "mutation site because arms mutate RAW text while the rules "
            "compare SQUASHED text, and the needle straddled a line break. "
            "Both were diagnosed against the raw prose BEFORE anything was "
            "edited; the prose asserted both hazards correctly and was not "
            "touched.",
      review_note="(ii) is the CT-S41 S41-05 class. It is legible only because "
                  "the harness reports 'SKIPPED (mutation site absent)' "
                  "explicitly; reported as MISSED it would have been "
                  "indistinguishable from a rule that does not work."),
 dict(claim_id="S42-08", label="VERIFIED", evidence_type="build",
      script="scripts/check_group_d.py", _hash=G,
      claim="All nine pre-declared transcription hazards are positively "
            "present in the drafted prose and each is exercised by an arm that "
            "removes it. The three named in PREREG section 5 are: S22-15 "
            "carries its own 'not a proof of leaf membership' disclaimer "
            "alongside its VERIFIED label; S22-20 is stated to remain VERIFIED "
            "on two independent runs and is not upgraded; and the S25-02 "
            "upgrade is stated to concern the PARAMETERS and explicitly not "
            "the Stokes data, with the sentence that it is not thereby proved "
            "at the level of the character variety."),
 dict(claim_id="S42-09", label="VERIFIED", evidence_type="file_inspection",
      script="scripts/claim_index.py", _hash=G,
      claim="Label census for the 22 outline-assigned ids of sections 7 and 8: "
            "S22-01 VERIFIED, S22-02 STRUCTURAL, S22-03 STRUCTURAL, S22-04 "
            "PROVEN, S22-05 PROVEN, S22-06 to S22-09 VERIFIED, S22-10 "
            "STRUCTURAL, S22-11 to S22-18 VERIFIED, S22-19 PROVEN, S22-20 "
            "VERIFIED, S22-23 PROVEN, S22-24 PROVEN. All 22 resolve, none is "
            "superseded, none is duplicated. Totals: 6 PROVEN, 13 VERIFIED, 3 "
            "STRUCTURAL."),
 dict(claim_id="S42-10", label="INSPECTED", evidence_type="file_inspection",
      script="section8.tex",
      claim="A tenth notation collision is found and REPORTED, not repaired: "
            "S22-24's invariant P = a^2 + b c collides with the P of the "
            "trace-free normal form d^2 + P d + Q used in sections 3 and 6. "
            "Section 8 avoids introducing the collision by writing the "
            "invariant as -det A, which it equals for a traceless A, and "
            "naming it rather than lettering it.",
      review_note="This is a genuine collision and not the section 3 / section "
                  "6 R item, which the operator ruled is one construction at "
                  "two specialisations and wants unified. This one wants "
                  "separating. Both belong to the second notation pass after "
                  "Group E."),
 dict(claim_id="S42-11", label="VERIFIED", evidence_type="file_inspection",
      script="scripts/emit_claims_s42.py",
      claim="Operator ruling 4 is applied at source: OUTLINE.md's ambiguous "
            "outline-internal subsection references are disambiguated in five "
            "places and a numbering-convention note is added, so that a "
            "reference which resolves and builds clean can no longer say "
            "something false. OUTLINE.md now hashes to "
            "9177ca5c2a8188c6beb535b3ecc321d711b0323145823daa4fec4f70c5389d32 "
            "at 52435 bytes, and carries the Revision 6 marker. The pre-edit "
            "digest, recorded as the prefix b8d85626, appears in NO "
            "claims.jsonl anywhere in the corpus, so the edit stranded no "
            "citation. The search is shown non-vacuous by a positive control: "
            "the string 0b94a7fc IS found, being the digest by which S24-01 "
            "and S24-08 cite OUTLINE.md at REVISION 2 -- four revisions stale "
            "before this session began, and so not stranded by this session "
            "either.",
      review_note="This claim was FIRST WRITTEN asserting that no claim in the "
                  "corpus cites any digest of OUTLINE.md. That was false, and "
                  "the assertion was caught by this script's own pre-write "
                  "check, before the buffer was written. The claim was "
                  "rewritten to a verifiable statement rather than the check "
                  "relaxed. LIMIT: no pre-edit copy of OUTLINE.md was "
                  "retained, so this session's before-state is not "
                  "reproducible; only the prefix search is available, and it "
                  "is what is claimed."),
 dict(claim_id="S42-13", label="PROVEN", evidence_type="computation",
      script="scripts/emit_claims_s42.py",
      claim="TWO successive forms of the S42-11 pre-write check were wrong in "
            "OPPOSITE directions, and neither could have been right. The "
            "first bounded the gap between 'OUTLINE.md' and a digest at 80 "
            "characters; S24-01 separates them by about 105, so it reported 1 "
            "citing line where there are 2. The second harvested every "
            "64-hex string on any line naming the file, and reported 15 "
            "'OUTLINE.md digests' of which all but one were the claims' own "
            "output_hash values. Proximity in a line does not decide whether "
            "a digest is a digest OF a named file, and no bound on it can. "
            "The check was replaced by the decidable question -- does the "
            "pre-edit digest appear anywhere in the corpus -- carrying a "
            "positive control, so that absence cannot be confused with a "
            "reader that could not see.",
      review_note="The first reader was right about the substance and wrong "
                  "about the count, which is the harder case: a count is not "
                  "evidence of its own completeness, and the bound that made "
                  "it cheap is what made it wrong. Fourth and fifth instances "
                  "this run of a reader that cannot see what it reports on."),
 dict(claim_id="S42-12", label="STRUCTURAL", evidence_type="file_inspection",
      script="scripts/check_group_d.py", _hash=G,
      claim="WHAT THIS SESSION'S PASS DOES NOT ESTABLISH. The gate is a "
            "transcription test. It verifies that cited ids resolve and are "
            "unsuperseded, that asserted labels match the corpus, and that "
            "every significant numeric literal appears in the text of a claim "
            "cited in the same subsection. It does NOT re-derive any displayed "
            "formula. A transposed digit inside a formula that appears in no "
            "claim text passes every rule here and builds clean. This is the "
            "standing gap recorded at CT-S40 and CT-S41 and scoped by the "
            "operator for a pass after Group E; it is restated so that this "
            "PASS is not read as more than it is."),
]


def build_buffer():
    buf = []
    for c in C:
        c = dict(c)
        h = c.pop("_hash", None)
        c.setdefault("task_id", TASK)
        c.setdefault("dps", None)
        c.setdefault("reproducible", True)
        c["output_hash"] = sha(HERE / h) if h else None
        buf.append(json.dumps(c, ensure_ascii=False, sort_keys=False))
    return buf


def validate(buf):
    """EVERY check here runs on the in-memory buffer, BEFORE any write."""
    errs = []
    recs = [json.loads(b) for b in buf]

    # -- non-vacuity on the numerator, before any count is printed
    if not recs:
        errs.append("buffer is empty: a validator with nothing to validate "
                    "passes vacuously")
        return errs, recs

    ids = [r["claim_id"] for r in recs]
    if len(set(ids)) != len(ids):
        errs.append("duplicate claim_id in the buffer")
    for r in recs:
        if not re.fullmatch(r"S42-\d\d", r["claim_id"]):
            errs.append("%s: malformed claim_id" % r["claim_id"])
        if r.get("label") not in ("PROVEN", "VERIFIED", "STRUCTURAL",
                                  "INSPECTED", "CONJECTURED"):
            errs.append("%s: label %r is not one of the five"
                        % (r["claim_id"], r.get("label")))
        if not str(r.get("claim", "")).strip():
            errs.append("%s: empty claim text" % r["claim_id"])
        if not str(r.get("script", "")).strip():
            errs.append("%s: no script" % r["claim_id"])
        s = HERE / r["script"]
        if not s.exists():
            errs.append("%s: script %s does not exist" % (r["claim_id"],
                                                          r["script"]))
        oh = r.get("output_hash")
        if oh is not None and not re.fullmatch(r"[0-9a-f]{64}", oh):
            errs.append("%s: output_hash is not a sha256" % r["claim_id"])

    # -- every output_hash must be the hash of a file that is on disk NOW
    have = {}
    for p in HERE.rglob("*"):
        if p.is_file() and p.name != "claims.jsonl":
            try:
                have[sha(p)] = p
            except OSError:
                pass
    nres = 0
    for r in recs:
        oh = r.get("output_hash")
        if oh is None:
            continue
        if oh not in have:
            errs.append("%s: output_hash resolves to no file in this session"
                        % r["claim_id"])
        else:
            nres += 1
    if nres == 0:
        errs.append("0 output_hash values were resolved: a count of zero "
                    "tests is not a result")

    # -- the gate must have PASSED, read from its own output
    g = (HERE / G).read_text(encoding="utf-8")
    if "GATE: PASSED" not in g:
        errs.append("the gate output does not say PASSED")
    if "11/11 CAUGHT" not in g:
        errs.append("the gate output does not report 11/11 arms CAUGHT")
    if "checks failed : 0" not in g:
        errs.append("the gate output does not report 0 failures")
    a = (HERE / A).read_text(encoding="utf-8")
    if "VERDICT: PASS" not in a:
        errs.append("check_assembly did not PASS")
    m = (HERE / M).read_text(encoding="utf-8")
    if "7/7 arms CAUGHT" not in m:
        errs.append("mutants_assembly did not catch 7/7")

    # -- S42-11, checked rather than believed.  TWO earlier forms of this
    # check were wrong in opposite directions (S42-13): one bounded the gap
    # between "OUTLINE.md" and the digest and under-counted, the other
    # harvested every digest on any line naming the file and over-counted.
    # Neither can decide which digest is a digest OF OUTLINE.md.  The
    # decidable question is substituted: does the PRE-EDIT digest appear
    # anywhere in the corpus?  With a positive control, so that "absent"
    # cannot be confused with "my reader could not see it".
    PRE = "b8d85626"        # pre-edit OUTLINE.md, prefix as recorded
    CTRL = "0b94a7fc"       # revision 2, cited by S24-01 and S24-08
    nfiles = 0
    pre_hits, ctrl_hits = [], []
    for p in SESSIONS.rglob("claims.jsonl"):
        if p.resolve() == OUT.resolve():
            continue
        nfiles += 1
        t = p.read_text(encoding="utf-8-sig", errors="replace")
        if PRE in t:
            pre_hits.append(p.parent.name)
        if CTRL in t:
            ctrl_hits.append(p.parent.name)
    if nfiles < 400:
        errs.append("the corpus search covered only %d files; it cannot "
                    "support a statement of absence" % nfiles)
    if not ctrl_hits:
        errs.append("POSITIVE CONTROL FAILED: %s is known to be cited and the "
                    "search did not find it, so 'absent' here would mean "
                    "'my reader could not see it'" % CTRL)
    if pre_hits:
        errs.append("S42-11 says the pre-edit OUTLINE.md digest is cited "
                    "nowhere, but %s appears in %s"
                    % (PRE, ", ".join(sorted(set(pre_hits)))))
    outline = SESSIONS / "2026-09-17" / "CT-S24-PAPER-OUTLINE" / "OUTLINE.md"
    if not outline.exists():
        errs.append("OUTLINE.md not found; S42-11 cannot be checked")
    else:
        txt = outline.read_text(encoding="utf-8", errors="replace")
        if "Revision 6" not in txt:
            errs.append("OUTLINE.md does not carry the Revision 6 marker "
                        "S42-11 relies on")
        if sha(outline) != ("9177ca5c2a8188c6beb535b3ecc321d711b03231"
                            "45823daa4fec4f70c5389d32"):
            errs.append("OUTLINE.md's digest is not the one S42-11 states")
    return errs, recs


def main():
    buf = build_buffer()
    errs, recs = validate(buf)
    print("emit_claims_s42 -- %d records in the buffer" % len(recs))
    if errs:
        print("REFUSING TO WRITE. %d pre-write check(s) failed:" % len(errs))
        for e in errs:
            print("   " + e)
        return 1
    nchecks = 8 + 6 * len(recs)
    print("pre-write checks: %d, 0 failed  (buffer validated BEFORE opening "
          "the file)" % nchecks)
    OUT.write_text("\n".join(buf) + "\n", encoding="utf-8")
    print("wrote %s  %d bytes  sha256 %s"
          % (OUT.name, OUT.stat().st_size, sha(OUT)[:32]))
    labs = {}
    for r in recs:
        labs[r["label"]] = labs.get(r["label"], 0) + 1
    print("labels: " + ", ".join("%s %d" % kv for kv in sorted(labs.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
