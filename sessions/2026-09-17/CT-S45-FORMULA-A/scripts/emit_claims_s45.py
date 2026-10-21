"""Emit the CT-S45-FORMULA-A claim record.

This emitter implements the standing rule adopted after S44-17: a figure is
confirmed by resolving it to the SPECIFIC LINE that reports it, identified by
an anchor that must also occur on that line.  Searching an evidence file for a
digit string anywhere is not sufficient -- at CT-S44 that accepted a figure
solely because the same digits appeared as a line number.

The buffer is validated in full before anything is written.  A post-write
assertion leaves the corrupt artefact on disk.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
O = "outputs/"
S = "scripts/"

RS = O + "route_s.out.txt"
RP = O + "route_p.out.txt"
RM = O + "mutants_route_s.out.txt"
RV = O + "verify_repair.out.txt"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"}

CLAIMS = []


def add(cid, claim, label, ev, script, out, figures=(), supersedes=None):
    """figures: tuple of (number-as-written, evidence-file, anchor-substring).

    The number must occur on a line of the evidence file that also contains
    the anchor.  The anchor names the display that reports the figure.
    """
    r = {
        "claim_id": cid,
        "task_id": "CT-S45-FORMULA-A",
        "claim": claim,
        "label": label,
        "evidence_type": ev,
        "dps": "exact (symbolic over QQ)" if ev == "computation" else "n/a",
        "reproducible": True,
        "script": script,
        "output_file": out,
        "figures": [list(f) for f in figures],
    }
    if supersedes:
        r["supersedes"] = supersedes
    CLAIMS.append(r)


# ---------------------------------------------------------------------------
add("S45-01",
    "Appendix A's expressions reach it by two different routes, and the "
    "appendix's own closing scope note denied this. The note asserted that no "
    "formula in it had been re-derived from a computation 'because there is "
    "no such computation'. The det A(1) residual of S16-20 and the difference "
    "polynomial of S16-R18-02 are exact symbolic computations, and S16-20 "
    "already carried evidence_type computation. The note has been rewritten "
    "to state both routes and which expressions take which.",
    "INSPECTED", "file_inspection", S + "route_s.py", RS)

add("S45-02",
    "The factored form of the difference between the printed and corrected "
    "readings, displayed in S16-R18-02 under a PROVEN label, carried the "
    "WRONG SIGN. The appendix printed minus one quarter z(q-1)(t-1)(4p + "
    "q^2 t + q^2 - qt - q); the true factorisation is plus one quarter of the "
    "same product. The appendix's own unfactored form, which begins 4pqt - "
    "4pq - 4pt + 4p, is correct and is inconsistent with the factored form "
    "printed four lines below it. Corrected in this session.",
    "VERIFIED", "computation", S + "route_s.py", RS)

add("S45-03",
    "The cause of the sign error is diagnosable rather than arbitrary. The "
    "difference between the readings is exactly -z times the det A(1) "
    "residual, and the residual genuinely carries a leading minus one "
    "quarter. The sign was copied across from the residual without the flip "
    "the factor -z introduces. The appendix's claim that the two independent "
    "tests 'agree on the correction term for term' is correct, and is what "
    "made the wrong sign look right.",
    "VERIFIED", "computation", S + "route_s.py", RS)

add("S45-04",
    "The re-derivation is not vacuous. Under the corrected reading det A(1) + "
    "theta1^2/4 vanishes identically; under the printed reading it does not; "
    "det A(0) + theta0^2/4 vanishes for BOTH readings, so that test does not "
    "discriminate, exactly as the appendix states. Five bogus variants of the "
    "bracket were rejected, of which two -- t/2 and t-1 -- were drawn from "
    "outside the appendix's own list of three, so the test is not merely "
    "consulting a list it was built from.",
    "VERIFIED", "computation", S + "route_s.py", RS,
    figures=(("5", RS, "bogus"),))

add("S45-05",
    "Every other computational display in Appendix A re-derives exactly. The "
    "det A(1) residual matches; its value at the stated exact rational point "
    "p=2/7, q=5/3, t=11/4, theta0=theta1=0, thetainf=3/5 is -223/144 as "
    "printed; the corrected first term of b(z) equals z times the (1,2) entry "
    "of B_1 identically; the unfactored difference matches; the residual "
    "vanishes at t=1; the two readings coincide at t=1; and c(0) = q/(q-1). "
    "Only the factored form differed.",
    "VERIFIED", "computation", S + "route_s.py", RS,
    figures=(("-223/144", RS, "appendix says"),))

add("S45-06",
    "The symbolic checker was shown able to fail, on the defect class it "
    "found. Eight control arms all CAUGHT: five plant known-wrong appendix "
    "literals including a sign flip of the residual and a transposed exponent, "
    "two corrupt the transcription of a(z) and c(z) and must make the script "
    "HALT on its vacuity pre-checks rather than compare literals against a "
    "meaningless baseline, and one is a negative arm in which a neutral edit "
    "must leave the verdict unchanged. The harness also asserts a baseline: "
    "the unmutated script must report exactly the one known defect.",
    "VERIFIED", "computation", S + "mutants_route_s.py", RM,
    figures=(("8", RM, "CAUGHT"),))

add("S45-07",
    "The repair verifies against a control that discriminates. verify_repair "
    "parses the displayed LaTeX into sympy and compares it mathematically, so "
    "an equivalent rewriting would also pass and a transposed digit would "
    "not. The repaired appendix MATCHES; the pre-repair file at refs/ is "
    "REJECTED by the same check. A checker that passed only the repaired text "
    "would prove that it can read, not that it can discriminate.",
    "VERIFIED", "computation", S + "verify_repair.py", RV)

add("S45-08",
    "The LaTeX reader in verify_repair failed on its first run and said so, "
    "rather than concluding. It could not parse whitespace-separated implicit "
    "multiplication and reported READER FAILED for both the repaired and the "
    "pre-repair file, returning no verdict. Had it instead silently parsed "
    "part of the expression it would have compared something that was not the "
    "display. The repair was one rule covering both spellings of implicit "
    "multiplication, not a special case for the string that failed.",
    "INSPECTED", "file_inspection", S + "verify_repair.py", RV)

add("S45-09",
    "Journal page 2655 was confirmed by folio read off the page, fixed by the "
    "running head MODULI FOR DIFFERENTIAL AND PAINLEVE EQUATIONS and the "
    "footer TOME 59 (2009), FASCICULE 7. The page shows the misprint exactly "
    "as S16-18 records it: b(z)'s first squared bracket prints without t "
    "while the neighbouring term carries (q-1)qt in both factors, and the "
    "same bracket prints WITH t in the (1,2) entry of B_1 a few lines below. "
    "S17-17's quotation matches the page word for word.",
    "INSPECTED", "file_inspection", S + "route_p.py", RP,
    figures=(("2655", RP, "folio"),))

add("S45-10",
    "The source's determinant constraint is narrower than the appendix "
    "quoted it. Journal page 2637, folio read off the page, states that "
    "-theta_i^2/4 is the determinant of A_i FOR i = 0, 1, and normalises "
    "A_infinity separately as t/2 times diag(-1,1), giving det A_infinity = "
    "-t^2/4 with no theta_infinity in it. The appendix had quoted the "
    "constraint unrestricted, which would be false at i = infinity. Only i = "
    "0 and i = 1 are used, so no result depends on it; the restriction has "
    "been added.",
    "INSPECTED", "file_inspection", S + "route_p.py", RP,
    figures=(("2637", RP, "folio"),))

add("S45-11",
    "The misprint persists in arXiv:0902.1702v5, page 34, folio read off the "
    "page and fixed by the author line MARIUS VAN DER PUT AND MASA-HIKO "
    "SAITO. The first squared bracket prints without t, identically to the "
    "journal text, while B_1 on the same page prints it with t. Both of "
    "S16-19's and S16-R18-01's readings are confirmed.",
    "INSPECTED", "file_inspection", S + "route_p.py", RP,
    figures=(("34", RP, "folio"),))

add("S45-12",
    "A quotation in S16-18 was transcribed with the wrong relation. Both the "
    "journal page and the arXiv page print the open set as U_0 CONG C x (C "
    "minus {0,1}); the appendix had it as U_0 = C x (C minus {0,1}) inside "
    "quotation marks. An isomorphism reported as an equality is a small "
    "error, but it is inside quoted material, and it was corrected.",
    "INSPECTED", "file_inspection", S + "route_p.py", RP)

add("S45-13",
    "What this pass does not establish. Route P is inspection of a rendered "
    "image by eye and is labelled INSPECTED throughout; it is not a "
    "machine-checked transcription and a second reader could disagree. Route "
    "S proves that the appendix's computational displays follow from MY "
    "transcription of the page; it does not independently establish that the "
    "printed page is itself correct, which is the very thing the appendix "
    "disputes for one entry. The pass covers Appendix A only; the remaining "
    "displayed formulas of the paper are not yet routed.",
    "INSPECTED", "file_inspection", S + "route_s.py", RS)


add("S45-14",
    "The repaired appendix builds. The full paper, assembled from CT-S44's "
    "repaired sections with this session's repaired Appendix A substituted, "
    "compiles over four passes at 39 pages with no errors, no undefined "
    "control sequences, no unresolved references and no multiply-defined "
    "labels. The page count is unchanged from CT-S44, so the repairs altered "
    "no pagination. A LaTeX repair that does not compile is not a repair.",
    "VERIFIED", "build", S + "route_s.py", O + "paper_build.out.txt",
    figures=(("39", O + "paper_build.out.txt", "pages"),))


# ---------------------------------------------------------------------------
# Pre-write validation.  Nothing below opens the output file.
# ---------------------------------------------------------------------------
def fail(msg):
    sys.exit("REFUSING TO WRITE: %s" % msg)


def validate():
    checks = 0
    seen = set()
    for r in CLAIMS:
        cid = r["claim_id"]
        checks += 1
        if cid in seen:
            fail("%s: duplicate claim id" % cid)
        seen.add(cid)

        checks += 1
        if r["label"] not in LABELS:
            fail("%s: label %r is not one of the five" % (cid, r["label"]))

        checks += 1
        if r["evidence_type"] == "computation" and r["label"] == "INSPECTED":
            fail("%s: a computation labelled INSPECTED" % cid)

        checks += 1
        if r["evidence_type"] == "file_inspection" and r["label"] == "PROVEN":
            fail("%s: file inspection cannot be PROVEN" % cid)

        for key in ("script", "output_file"):
            checks += 1
            pth = HERE / r[key]
            if not pth.exists() or pth.stat().st_size == 0:
                fail("%s: %s %s missing or empty" % (cid, key, r[key]))

        # the standing rule: resolve each figure to the line that reports it
        for num, evf, anchor in r["figures"]:
            checks += 1
            pth = HERE / evf
            if not pth.exists():
                fail("%s: figure evidence %s missing" % (cid, evf))
            lines = pth.read_text(encoding="utf-8",
                                  errors="replace").splitlines()
            hits = [ln for ln in lines if num in ln and anchor in ln]
            if not hits:
                fail("%s: figure %r does not occur on any line of %s that "
                     "also contains the anchor %r -- a match elsewhere in the "
                     "file is not evidence" % (cid, num, evf, anchor))
            checks += 1
            if r["label"] == "CONJECTURED":
                fail("%s: a CONJECTURED claim should not carry figures" % cid)

        checks += 1
        if r.get("supersedes", "").startswith("S45-"):
            fail("%s: supersedes a same-session claim" % cid)

    # the buffer must round-trip through JSON before anything is written
    checks += 1
    body = "\n".join(json.dumps(r, ensure_ascii=True, sort_keys=True)
                     for r in CLAIMS) + "\n"
    for line in body.strip().splitlines():
        json.loads(line)

    # ...and the BYTES that will actually be written must round-trip too.
    # write_text() applies platform newline translation on Windows, so a
    # digest taken over the LF buffer does not describe the file on disk.
    # Checking this before the write is the point: a post-write assertion
    # still leaves the corrupt artefact there.
    checks += 1
    raw = body.encode("utf-8")
    if b"\r" in raw:
        fail("buffer contains CR before writing")
    checks += 1
    if "\n".join(json.dumps(json.loads(ln), ensure_ascii=True, sort_keys=True)
                 for ln in raw.decode("utf-8").strip().splitlines()) \
            + "\n" != body:
        fail("buffer does not round-trip through its own encoding")
    return checks, raw


def main():
    checks, raw = validate()
    digest = hashlib.sha256(raw).hexdigest()
    # write_bytes, not write_text: no newline translation
    (HERE / "claims.jsonl").write_bytes(raw)

    # read-back, after the pre-write validation, not instead of it
    back = (HERE / "claims.jsonl").read_bytes()
    if hashlib.sha256(back).hexdigest() != digest:
        sys.exit("WROTE, BUT READ-BACK DIFFERS -- artefact is suspect")

    print("%d claims, %d pre-write checks, sha256 %s"
          % (len(CLAIMS), checks, digest))
    for r in CLAIMS:
        print("  %-8s %-12s %s" % (r["claim_id"], r["label"],
                                   r["claim"][:64]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
