"""CT-S47 - emit claims.jsonl, validating the BUFFER before writing.

Rules carried forward, each of which has caught a real defect earlier in this
run:

  * validate the in-memory buffer BEFORE writing; a post-write assertion still
    leaves the corrupt artefact on disk;
  * every figure quoted in a claim must resolve to a LINE of its evidence file
    that also carries an anchor phrase -- a bare digit search passes on a line
    number;
  * every output_hash must hash the file it names, recomputed here;
  * a supersession never edits the superseded record.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTDIR = SESS / "outputs"
TARGET = SESS / "claims.jsonl"

LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"}

RS5 = "route_s5_qp.out.txt"
RMU = "mutants_route_s5_qp.out.txt"
R18 = "check_r18_sign.out.txt"

C = []


def add(cid, task, claim, label, ev, script, out_file, figures=(), **kw):
    C.append(dict(claim_id=cid, task_id=task, claim=claim, label=label,
                  evidence_type=ev, dps=kw.pop("dps", None), reproducible=True,
                  script=script, output_file=out_file,
                  output_hash=None, _figures=figures, **kw))


# ---------------------------------------------------------------- claims ---
add("S47-01", "S5-QP-SOURCE",
    "The object under test is resolved positively, not by path. section5.tex is "
    "identified by sha256 af25048b9b62a6f4 and by a positive guard that it still "
    "carries the subsection 'The located point'; the check refuses rather than "
    "compares if either fails. This is the standing form for 'which tree am I "
    "measuring', after S44-16 and S38-07.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("af25048b9b62a6f4", RS5, "sha256"),))

add("S47-02", "S5-QP-ALPHA",
    "ROUTE ALPHA. The numerals PRINTED IN section5.tex lines 116-130 -- parsed "
    "out of the file, not retyped and not taken from any claim text -- satisfy "
    "the vdPS family-(4.1) matching system exactly. All six generators (five "
    "coefficients of a quartic in z, plus the no-apparent-singularity condition "
    "b_1 = 0) evaluate to symbolic zero, not to numerical smallness, at the "
    "parsed (p, q, t, theta_infinity) on the branch t = -2i sqrt(33)/9. The "
    "whole run is 36 checks with 0 DIFFER.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("36", RS5, "checks"), ("0", RS5, "DIFFER")))

add("S47-03", "S5-QP-ALPHA2",
    "ROUTE ALPHA2, an independent route to the same point. Substituting the "
    "parsed values into the UNREDUCED R = P^2/4 + P'/2 - Q -- with no b' = 0 "
    "reduction assumed anywhere -- gives R - r_z identically zero. Independently, "
    "b is constant at that point (so b_1 = 0 is genuinely satisfied rather than "
    "imposed) and q(q-1) is nonzero, placing the point in the chart U_0.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("0", RS5, "DIFFER"),))

add("S47-04", "S5-QP-BETA",
    "ROUTE BETA, per coefficient rather than per display. An independent solve "
    "returns exactly two solutions. Decomposed in the basis {1, sqrt3, sqrt11, "
    "sqrt33} of Q(sqrt3, sqrt11), every printed coordinate matches exactly: q's "
    "rational part 1/2; q's i*sqrt(11) coordinate -457937/122408; q's i*sqrt(33) "
    "coordinate 281700/122408; p's i*sqrt(33) coordinate 5*(-28151758571)/"
    "4086468672; p's i*sqrt(11) coordinate 5*48874838016/4086468672; and both "
    "theta_infinity values and both t branches. q carries no hidden i*sqrt(3) "
    "term and p carries no rational part.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("-457937/122408", RS5, "sqrt(11)"),
             ("281700/122408", RS5, "sqrt(33)")))

add("S47-05", "S5-QP-GAMMA",
    "ROUTE GAMMA. All eight printed approximation figures agree with the exact "
    "values at dps 60, each within half a unit in its own last printed place, "
    "reported one row per figure: q branch 1 Re 0.5 and Im 0.8123 (exact "
    "0.8123496088), p branch 1 Im 0.4649 (exact 0.4648985440), q branch 2 Im "
    "-25.6278 (exact -25.62780622), p branch 2 Im 396.2089 (exact 396.2088861).",
    "VERIFIED", "computation", "route_s5_qp.py", RS5, dps=60,
    figures=(("0.8123496088", RS5, "printed 0.8123"),
             ("396.2088861", RS5, "printed 396.2089")))

add("S47-06", "S5-QP-VACUITY",
    "The vacuity pre-check is the defect class itself, not a generic "
    "perturbation: transposing the last two digits of each printed integer must "
    "break the system. Five of six were CAUGHT, each breaking 3 of 6 generators. "
    "The sixth, q_B = 281700, ends in two identical digits, so its transposition "
    "is a NO-OP; it was reported SKIPPED and explicitly NOT counted as coverage, "
    "and a supplementary arm (281700 -> 821700) was added to demonstrate "
    "sensitivity. A no-op mutation scoring as a detection would be a false "
    "control; adding an arm is not moving a threshold.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("821700", RS5, "CAUGHT"),))

add("S47-07", "S5-QP-READER",
    "A reader defect manufactured two DIFFERs against correct material. sympy "
    "holds sqrt(33) as a single atom, so expr.coeff(sqrt(11)) cannot see it and "
    "returns 0 -- a coefficient the reader could not read is indistinguishable "
    "from a coefficient that is genuinely zero. The first ledger therefore "
    "reported q's i*sqrt(33) coordinate and p's i*sqrt(33) coordinate as DIFFER "
    "while the solved q and p printed identically to the page. Diagnosed against "
    "the raw output before any edit to the paper; repaired by decomposing in an "
    "explicit basis, with the decomposer given a positive control (sqrt33 must "
    "be SEEN, not returned as 0) and a refusal when an expression does not lie "
    "in the field. This is the fourth appearance in the run of a check reporting "
    "absence its reader could not see.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("0", RS5, "DIFFER"),))

add("S47-08", "S5-QP-EXITCODE",
    "CT-S46 finding 3.9 separated refusal (exit 2) from finding (exit 1) so that "
    "a broken instrument and a real defect in the paper are distinguishable to a "
    "caller. An UNCAUGHT TRACEBACK reintroduces the same collision through a "
    "different door, because Python exits 1 on an unhandled exception; this "
    "session hit it on an AttributeError and the run reported exit 1 with no "
    "output file. Repaired with an excepthook giving a crash its own code 3, and "
    "the control harness treats a crash as MISSED rather than as a detection.",
    "VERIFIED", "computation", "mutants_route_s5_qp.py", RMU,
    figures=(("0", RMU, "MISSED"),))

add("S47-09", "S5-QP-ARMS",
    "The instrument was shown able to fail, on the defects that matter. Nine "
    "control arms in three expectation kinds -- five that must make it REFUSE "
    "(coords blind to sqrt33, generators that always vanish, a moved source "
    "digest, a parser that drops a digit, a corrupted transport), three that "
    "must make it report a DIFFER (a collapsed approximation tolerance, a branch "
    "pairing compared against its own branch, and a transposed digit planted in "
    "section5.tex itself), and one negative arm in which a neutral edit must "
    "change nothing. A baseline assertion requires the unmutated script to "
    "report 36 checks and 0 DIFFER first, and every arm runs in a scratch tree "
    "so that no arm can write the output file the claims cite. The baseline "
    "assertion fired once during development, refusing to report any arm result "
    "while the script itself was crashing.",
    "VERIFIED", "computation", "mutants_route_s5_qp.py", RMU,
    figures=(("9", RMU, "CAUGHT"),))

add("S47-10", "S5-QP-SCOPE",
    "SCOPE LIMIT, stated in PREREG before running. This session re-derives only "
    "section 5's exact q and p (claim S16-12). The other twelve route-S-corpus "
    "displays identified by CT-S46 remain routed-to-a-claim and NOT re-derived: "
    "nothing here licenses any statement about S1-04, S26-01, S3B-02, S4-03, "
    "S6-C18, S16-03, S17-10 or S22-12.",
    "STRUCTURAL", "file_inspection", "(scope fixed in PREREG.md section 6)", RS5)

add("S47-11", "JIMBO-MARKER",
    "The filename jimbo_p1152.png denotes TWO DIFFERENT PAGES in this tree, and "
    "is correct in one location and wrong in another. Folios read off each image: "
    "CT-S21-DEPOSIT-PREP/pages/jimbo_p1152.png (sha256 05fecc96632ca6d4) carries "
    "printed folio 1153, running head 'BOUNDARY CONDITION FOR PAINLEVE "
    "EQUATIONS', containing (3.4)-(3.7), the Stokes multipliers and (A2)/(A3), "
    "and NO PV parameter dictionary. jimbo_printed1152.png (42fffb7b09ff60b5) "
    "carries printed folio 1152, running head 'MICHIO JIMBO', and does carry "
    "alpha, beta, gamma, delta and (A1). A third file, "
    "CT-R1-AUDIT/coldpackets/jimbo_p1152.png (84f548ceadd8d4a0), is a DIFFERENT "
    "image that genuinely is folio 1152 and is correctly named. Per operator "
    "ruling the images are NOT renamed, because earlier sessions cite them by "
    "hash; a README.md was ADDED beside them recording the folios and the rule "
    "that no claim may cite jimbo_p1152.png for content on folio 1152. Adding a "
    "sibling file strands no digest and edits no earlier session.",
    "INSPECTED", "file_inspection", "(page images read directly)", RS5)

add("S47-12", "R18-SUPERSEDE",
    "SUPERSEDES S16-R18-02. The sign error CT-S45 found is present in the CLAIM "
    "TEXT of S16-R18-02 itself, not only in appendixA.tex's typeset display. "
    "That claim states one quantity twice and the two statements differ by "
    "exactly a sign: its unfactored form z(4pqt - 4pq - 4pt + 4p + q^3 t^2 - q^3 "
    "- 2q^2 t^2 + 2q^2 + q t^2 - q)/4 is CORRECT, while its factored form, given "
    "as -z(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4, carries the wrong sign; the "
    "true factorisation is +z(q-1)(t-1)(4p + q^2 t + q^2 - qt - q)/4. Verified "
    "here by factoring the unfactored form directly, with two rejecting controls "
    "(a sign flip on the last term, and a denominator 2 for 4). The RESULT of "
    "S16-R18-02 is unaffected: the corrected reading still makes b(z)'s first "
    "term exactly z*B_1[1,2] and the printed reading still does not, and the "
    "agreement with the det A(1) residual still holds, up to the factor of -z "
    "that S45-03 diagnosed as the cause. The label therefore remains PROVEN: "
    "what was defective is the recorded display, not the mathematics. The "
    "original record is left UNEDITED, per the append-only rule.",
    "PROVEN", "computation", "check_r18_sign.py", R18,
    supersedes="S16-R18-02")

add("S47-13", "S5-QP-PRECOND",
    "A control arm exposed a missing pre-condition rather than a defective arm. "
    "The whole construction depends on r_z having denominator exactly D^2 = "
    "z^2(z-1)^2 up to a constant -- only then is matching R against r_z an "
    "equality of two quartics, and only then is Nz*D^2/Dz a polynomial -- and "
    "nothing checked it. In the unmutated run it holds (the ratio is the "
    "constant 108), so the dependency was invisible. When arm M5 corrupted "
    "System C's s_+, sympy raised an opaque PolynomialError and the run "
    "CRASHED where it should have refused. Repaired in the script by asserting "
    "the denominator identity and refusing with a diagnosis; the arm was "
    "reclassified from 'must report a DIFFER' to 'must refuse', because a "
    "broken transport is a fact about the instrument's input and not a finding "
    "about the paper. The harness scoring a crash as MISSED rather than CAUGHT "
    "is what made the cause visible instead of letting 7-of-8 read as 8-of-8.",
    "VERIFIED", "computation", "route_s5_qp.py", RS5,
    figures=(("108", RS5, "pre-condition"),))

add("S47-14", "S5-QP-GUARDGAP",
    "A guard that makes a class of mutation impossible also prevents anyone "
    "from testing what lies behind it. Every arm in the first harness mutated "
    "the SCRIPT; none mutated section5.tex, because the source-digest guard "
    "would refuse any altered .tex and the arm would only re-test the guard. "
    "The consequence was that no arm asked the one question the formula pass "
    "exists to answer: does route ALPHA report a DIFFER when the PAGE carries a "
    "wrong digit? Arm M9 now plants a genuine transposition in section5.tex "
    "(457937 -> 457973) and updates the expected digest in the same step, so "
    "that it tests detection rather than the digest guard that arm M3 already "
    "covers.",
    "VERIFIED", "computation", "mutants_route_s5_qp.py", RMU,
    figures=(("457973", RMU, "M9"),))

add("S47-15", "S5-QP-VACUITY-ORDER",
    "A vacuity pre-check guards a PASS, not a FAIL, and running it first let it "
    "mask the finding it exists to make meaningful. A transposition is an "
    "INVOLUTION: the vacuity arm transposes the last two digits of each parsed "
    "integer, so on a page already carrying 457973 it restores the true 457937, "
    "the generators vanish, the arm reports MISSED, and the script refuses with "
    "'route ALPHA cannot see a transposition in q_A' -- while the actual state "
    "of affairs is that the page carries one. A wrong digit would have been "
    "announced as a broken instrument. This is the refusal/finding collision of "
    "CT-S46 finding 3.9 reappearing at the level of ORDERING rather than of exit "
    "codes. Found by control arm M9, which returned exit 2 where exit 1 was "
    "required. Repaired by evaluating the observable before mutating anything: "
    "if the parsed values already fail, the vacuity block is reported SKIPPED as "
    "moot and the DIFFER stands. No threshold was moved.",
    "VERIFIED", "computation", "mutants_route_s5_qp.py", RMU,
    figures=(("457973", RMU, "M9"),))

# ------------------------------------------------------------ validation ---
errs = []
seen = set()

for c in C:
    cid = c["claim_id"]
    if not re.fullmatch(r"S47-\d\d", cid):
        errs.append(f"{cid}: malformed claim id")
    if cid in seen:
        errs.append(f"{cid}: duplicate claim id")
    seen.add(cid)
    if c["label"] not in LABELS:
        errs.append(f"{cid}: label {c['label']} outside the five")
    if not c["claim"].strip():
        errs.append(f"{cid}: empty claim text")
    if len(c["claim"]) < 80:
        errs.append(f"{cid}: claim text suspiciously short")

    of = OUTDIR / c["output_file"]
    if not of.exists():
        errs.append(f"{cid}: evidence file {c['output_file']} absent")
        continue
    c["output_hash"] = hashlib.sha256(of.read_bytes()).hexdigest()

    # anchored-figure rule: the number and the anchor must share a LINE
    body = of.read_text(encoding="utf-8")
    for num, fname, anchor in c.pop("_figures"):
        src = (OUTDIR / fname).read_text(encoding="utf-8") if fname != c["output_file"] else body
        hit = [ln for ln in src.splitlines() if num in ln and anchor in ln]
        if not hit:
            errs.append(f"{cid}: figure {num!r} with anchor {anchor!r} "
                        f"does not resolve to a line of {fname}")

for c in C:
    c.pop("_figures", None)

if errs:
    print("REFUSED - nothing written:")
    for e in errs:
        print("  " + e)
    sys.exit(2)

# build the buffer and validate the BUFFER, not the file
buf = "\n".join(json.dumps(c, ensure_ascii=True) for c in C) + "\n"
if "\r" in buf:
    print("REFUSED: buffer contains a carriage return")
    sys.exit(2)
try:
    reparsed = [json.loads(l) for l in buf.strip().split("\n")]
except Exception as exc:
    print(f"REFUSED: buffer does not re-parse: {exc}")
    sys.exit(2)
if len(reparsed) != len(C):
    print("REFUSED: buffer line count does not match claim count")
    sys.exit(2)
if any(r["output_hash"] is None or len(r["output_hash"]) != 64 for r in reparsed):
    print("REFUSED: a re-parsed claim has no usable output_hash")
    sys.exit(2)

TARGET.write_bytes(buf.encode("utf-8"))
print(f"wrote {TARGET.name}: {len(C)} claims, "
      f"sha256 {hashlib.sha256(TARGET.read_bytes()).hexdigest()}")
for c in C:
    sup = f"  supersedes {c['supersedes']}" if "supersedes" in c else ""
    print(f"  {c['claim_id']}  {c['label']:11s} {c['task_id']}{sup}")
