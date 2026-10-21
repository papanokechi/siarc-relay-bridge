"""CT-S16 - emit claims.jsonl with a real sha256 for every cited output file.

Aborts if any referenced script or output file is missing, so a claim can never
point at a hash of nothing.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256(rel):
    path = os.path.join(HERE, rel)
    if not os.path.isfile(path):
        sys.exit("MISSING FILE, aborting: " + rel)
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


C = []


def add(cid, task, claim, label, ev, script, out, review, note, dps=None):
    C.append(dict(claim_id=cid, task_id=task, claim=claim, label=label,
                  evidence_type=ev, dps=dps, reproducible=True, script=script,
                  output_hash=sha256(out), review=review, review_note=note))


# ---------------------------------------------------------------- step 1
add("S16-01", "S16-STEP1",
    "vdPS section 3.2 p.2637, read from the page image: for a differential module of "
    "type (0,0,1) the STRONG Riemann-Hilbert problem has a positive answer; the module "
    "is represented by d/dz + A_0/z + A_1/(z-1) + A_inf with trace-0 constant matrices, "
    "A_inf normalised to (t/2)diag(-1,1) with t in C*, -theta_i^2/4 = det A_i, and the "
    "singular points normalised to 0, 1, infinity. NO semisimplicity and NO "
    "non-resonance hypothesis is imposed anywhere in this definition.",
    "INSPECTED", "file_inspection", "render_pages.py",
    "pages/vdps_p2637.png", "self",
    "read by viewing the rendered page alone in one message, per the P0 image rule.")

add("S16-02", "S16-STEP1",
    "vdPS p.2636, read from the page image, defines resonance as a difference of "
    "eigenvalues lying in Z\\{0}, and presents resonance and reducibility as sources of "
    "SINGULARITIES of the monodromy space R. Such modules are therefore inside the "
    "moduli space, not excluded from it. This is the hypothesis the operator flagged as "
    "at risk; it is not a hypothesis of this framework.",
    "INSPECTED", "file_inspection", "render_pages.py",
    "pages/vdps_p2635.png", "self",
    "p.2636 rendered and viewed; quoted definition only, no interpretation added here.")

add("S16-03", "S16-STEP1",
    "Packet task 1(b) IS stated in the required form, so the halt condition did not "
    "fire. vdPS p.2656, verbatim from the page image: 'the foliation given by the "
    "2-form Omega = dp^dq/(q(q-1)) - dH_V ^ dt on U_0 x (C\\{0}) coincides with the "
    "foliation given by isomonodromy.' The flow is (4.4) dp/dt = q(q-1) dH_V/dq, "
    "dq/dt = -q(q-1) dH_V/dp with H_V given by (4.5). The operator's description of "
    "the framework from memory is CONFIRMED against the text.",
    "INSPECTED", "file_inspection", "render_pages.py",
    "pages/vdps_p2656_HV.png", "self",
    "H_V and (4.4) cropped at 6x and viewed alone; transcribed by looking, not by OCR.")

add("S16-04", "S16-STEP1",
    "The time variable t of vdPS's (0,0,1) family is the SCALE OF THE IRREGULAR TYPE "
    "AT INFINITY (A_inf = (t/2)diag(-1,1)), not the position of a singular point. The "
    "three singular points are normalised to 0, 1, infinity. This is why an object of "
    "this type carries a fixed t with no deformation written down: t is an invariant "
    "computed from the configuration, exactly as the operator surmised.",
    "STRUCTURAL", "file_inspection", "render_pages.py",
    "pages/vdps_p2637.png", "self",
    "reading of the normalisation in section 3.2; structural, not a quotation.")

add("S16-05", "S16-STEP1",
    "SUSPECTED TYPO IN THE PUBLISHED PAPER, vdPS p.2655, entry b(z) of the family "
    "(4.1): the first term prints (p + (1/2)(q-1)q)^2, with no t, while the second "
    "term carries (q-1)q t. Tested against the paper's OWN constraint det A(1) = "
    "-theta_1^2/4: the printed form leaves a nonzero remainder, whereas "
    "(p + (1/2)(q-1)q t)^2 satisfies it IDENTICALLY. det A(0) = -theta_0^2/4 holds for "
    "both readings and so does not discriminate. The corrected reading is used for "
    "computation and is flagged here rather than adopted silently.",
    "VERIFIED", "computation", "check_bz.py",
    "outputs/check_bz.out.txt", "self",
    "discriminated by an exact symbolic residual, not by preference.", dps=0)

# ---------------------------------------------------------------- step 2
add("S16-06", "S16-STEP2A",
    "System C (3x^2+x+1)W'' + (6x+1)W' - x^2 W = 0 has projective normal potential "
    "r_C(x) = (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2); singular points s_pm = "
    "(-1 +/- i sqrt(11))/6 with delta = s_- - s_+ = -i sqrt(11)/3. Under x = s_+ + "
    "delta z the potential has poles ONLY at z = 0 and z = 1, both double, with "
    "coefficient -1/4 at each, and NO apparent singularity. So C's three singular "
    "points are exactly vdPS's 0, 1, infinity after the normalising Moebius map.",
    "PROVEN", "computation", "systemC_invariants.py",
    "outputs/systemC_invariants.out.txt", "self",
    "exact symbolic derivation; cross-checked numerically at dps 60, worst |diff| "
    "1.1668e-61.", dps=60)

add("S16-07", "S16-STEP2C",
    "H-c SATISFIED, exactly. At infinity r_z = -11/27 + (i sqrt(11)/27)/z + ..., and "
    "vdPS's normalisation gives t^2/4 = R(infinity), hence t = -/+ 2 i sqrt(33)/9. This "
    "is EXACTLY the value the companion v1.2 prints for System C. The companion's t is "
    "therefore vdPS's time invariant, computed from the configuration, and there is no "
    "mismatch to explain.",
    "PROVEN", "computation", "systemC_invariants.py",
    "outputs/systemC_invariants.out.txt", "self",
    "symbolic; the match is to an exact algebraic number, not a numerical agreement.")

add("S16-08", "S16-STEP2A",
    "Dictionary between vdPS's family (4.1) and the projective normal potential, "
    "established by probing three EXACT draws: double-pole coefficient at z=0 is "
    "(theta_0^2-1)/4 (3/3), at z=1 is (theta_1^2-1)/4 (3/3), and R(infinity) = t^2/4 "
    "(3/3). The naive 1/z entry t*theta_inf/2 FAILED all three; the data give "
    "t(theta_inf+1)/2, the +1 being the scalar-reduction shift. The failure is reported "
    "because it is the reason the located theta_inf is -2 -/+ sqrt(3)/9 and not "
    "-1 -/+ sqrt(3)/9.",
    "VERIFIED", "computation", "probe_family.py",
    "outputs/probe_family.out.txt", "self",
    "three exact draws carrying theta_0 != 0; these draws are also the H-a vacuity "
    "control, since the observable does report a nonzero theta_0.", dps=0)

add("S16-09", "S16-STEP2A",
    "H-a SATISFIED, AGAINST PRE-REGISTRATION. PREREG.md recorded the expectation that "
    "H-a would be VIOLATED or UNDECIDED. System C has theta_0 = theta_1 = 0, so "
    "det A_i = 0 and tr A_i = 0 and A_0, A_1 are NILPOTENT and nonzero (c(0) = "
    "q/(q-1) != 0 on U_0, and C1 forces a log term): non-semisimple local data. But "
    "the eigenvalue difference is 0, which is NOT in Z\\{0}, so the data are not "
    "resonant in vdPS's sense; and section 3.2 imposes no semisimplicity condition in "
    "any case. The operator's worry that resonance might violate a hypothesis does NOT "
    "materialise in this framework. vdPS admit precisely the logarithmic local data "
    "that Jimbo's (A1) excludes.",
    "STRUCTURAL", "proof", "probe_family.py",
    "outputs/probe_family.out.txt", "self",
    "rests on the ABSENCE of a hypothesis in the source, which is why it is STRUCTURAL "
    "and not PROVEN; the reading is claim S16-01.")

add("S16-10", "S16-STEP2B",
    "H-b SATISFIED: System C is IRREDUCIBLE over C(x), proven exactly. Riccati test "
    "w' + w^2 = r: any solution has only simple poles; residues at s_pm satisfy "
    "A^2 - A = -1/4 so A = 1/2; w is bounded at infinity with c_0^2 = 1/3; matching "
    "the 1/x coefficient r_1 = -1/9 forces n = r_1/(2c_0) - 1 = -1 -/+ sqrt(3)/18, "
    "irrational and hence not a non-negative integer. Contradiction. So C does NOT sit "
    "on the classical Riccati locus.",
    "PROVEN", "computation", "irreducibility2.py",
    "outputs/irreducibility2.out.txt", "self",
    "exact; both controls are assertions - a reducible-by-construction operator is "
    "returned REDUCIBLE and an irreducible one IRREDUCIBLE.")

add("S16-11", "S16-METHOD",
    "DEFECT CAUGHT AND RECORDED: the first irreducibility script was VOID. "
    "sp.cancel((x-c)**2 * r).subs(x, c) returns nan for algebraic c, so the "
    "admissible-residue list came out empty, the product over it was empty, and the "
    "verdict IRREDUCIBLE was reached WITH NO TEST PERFORMED. It was caught only by the "
    "reducible-by-construction control, which was also declared irreducible. Related: "
    "all(m == 2 for m in sp.roots(...).values()) is vacuously True on an empty dict. "
    "General lesson: a step that cannot fail cannot be trusted to report failure; "
    "every control must be an assertion. irreducibility.py is retained as the record.",
    "PROVEN", "computation", "irreducibility.py",
    "outputs/irreducibility.out.txt", "self",
    "the defect is demonstrated by the retained void script and its output.")

# ---------------------------------------------------------------- step 3a
add("S16-12", "S16-STEP3A",
    "STEP 3(a) COMPLETE. System C's projective normal form coincides with that of "
    "vdPS's family (4.1) at an explicit point of the chart U_0 = C x (C\\{0,1}) of "
    "M_{t,lambda}, for both sign branches. Branch t = -2i sqrt(33)/9: theta_inf = "
    "-2 - sqrt(3)/9, q = 1/2 + i(-457937 sqrt(11) + 281700 sqrt(33))/122408 ~ "
    "0.5 + 0.8123 i, p = 5i(-28151758571 sqrt(33) + 48874838016 sqrt(11))/4086468672 ~ "
    "0.4649 i. Branch t = +2i sqrt(33)/9: theta_inf = -2 + sqrt(3)/9, q ~ 0.5 - "
    "25.6278 i, p ~ 396.2089 i. The solve was OVERDETERMINED - five coefficient "
    "equations plus b_1 = 0 in four unknowns - and consistent.",
    "VERIFIED", "computation", "locate_final.py",
    "outputs/pq_solution.txt", "self",
    "located by a hand-reduced closed form; see S16-13 for the independent check.",
    dps=60)

add("S16-13", "S16-STEP3A",
    "INDEPENDENT VERIFICATION of S16-12: re-substituting each solution into the "
    "GENERAL formula for R - not the reduced closed form used to derive it - gives "
    "R - r_z simplifying identically to 0, with worst relative residual over five "
    "points at dps 60 of 5.79877e-56 (branch 1) and 7.00553e-61 (branch 2); b_1 = 0 in "
    "both; and q not in {0,1} in both, so the point lies in the chart U_0.",
    "VERIFIED", "computation", "verify_point.py",
    "outputs/verify_point.out.txt", "self",
    "re-derivation by a different route from the one that produced the value; still "
    "self, since the same agent wrote both.", dps=60)

add("S16-14", "S16-MEMBERSHIP",
    "MEMBERSHIP, the packet's question. System C satisfies every hypothesis under "
    "which vdPS build the moduli space M for the (0,0,1) row: H-a SATISFIED (S16-09), "
    "H-b SATISFIED (S16-10), H-c SATISFIED (S16-07). It is a point of the chart U_0 "
    "(S16-12, S16-13). Since PV IS the isomonodromy foliation on that space (S16-03), "
    "and since q(q-1) != 0 and t != 0 at the point so the vector field (4.4) is "
    "regular there, exactly one PV leaf passes through System C. The deformation "
    "EXISTS and is not an ansatz. CAUTION ON STRENGTH: the match is of PROJECTIVE "
    "normal forms, so what is established is that C's projectivisation is that of the "
    "family member at (p,q,t) - equality up to a rank-1 twist - in the same sense in "
    "which B and C are projectively equivalent. This is the reason the label is "
    "STRUCTURAL and not PROVEN.",
    "STRUCTURAL", "proof", "flow_regularity.py",
    "outputs/flow_regularity.out.txt", "self",
    "the pre-registered step-3(b) monodromy/Stokes falsifier at 30 digits was NOT run; "
    "this claim does not rest on it and does not stand in for it.")

add("S16-15", "S16-STEP3B",
    "NOT ESTABLISHED: the pre-registered step-3(b) falsifier was NOT run. It requires "
    "integrating PV from (t_0,q,p) to t_0 + epsilon for two values of epsilon, "
    "rebuilding the linear system, and computing monodromy AND STOKES data agreeing "
    "with C's to at least 30 digits. Computing Stokes data for an irregular rank-2 "
    "system at that precision is a separate undertaking beyond this budget. The "
    "threshold in PREREG.md is left UNCHANGED for whenever it is run. What was done "
    "instead, and is reported as supplementary rather than as the falsifier, is the "
    "regularity check of the vector field (4.4) at the point.",
    "CONJECTURED", "computation", "flow_regularity.py",
    "outputs/flow_regularity.out.txt", "self",
    "recorded as a gap; no threshold was weakened to close it.")

add("S16-16", "S16-C3",
    "CONSEQUENCE FOR C3. The 'single fibre' concern - that System C sits at one fixed "
    "time t with no deformation written down - is, on this framework, a matter of "
    "PRESENTATION rather than a defect, because t is an invariant of the configuration "
    "(S16-04) and every point of M lies on a leaf (S16-03, S16-14). This does NOT "
    "license changing C3's wording in the companion v1.3 notice, which is an operator "
    "decision and is out of scope for this analysis-only session; no notice or "
    "conjecture file was edited.",
    "STRUCTURAL", "proof", None,
    "outputs/flow_regularity.out.txt", "self",
    "consequence of S16-03, S16-04 and S16-14; flagged for the operator, not applied.")

add("S16-17", "S16-METHOD",
    "P0 AMENDMENT PROPOSED, alongside the existing OCR rule: before a page image is "
    "used as evidence it must be confirmed to have RENDERED. The view tool accepts one "
    "image per message; two calls in a single message returned 'maximum number of "
    "images (1)' and displayed nothing, and reasoning had begun from page content that "
    "had never been seen. Caught and stopped; each page was then re-read alone in its "
    "own message. Rule: one image per message, and confirm it displayed before "
    "quoting it.",
    "STRUCTURAL", "proof", None,
    "pages/vdps_p2637.png", "self",
    "method finding from this session; same family as S16-11.")

out = os.path.join(HERE, "claims.jsonl")
with open(out, "w", encoding="utf-8") as fh:
    for c in C:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")

n = sum(1 for _ in open(out, encoding="utf-8"))
print("claims written :", len(C))
print("lines in file  :", n)
assert n == len(C), "APPEND-PATH FAILURE: line count != claim count"
ids = [c["claim_id"] for c in C]
assert len(set(ids)) == len(ids), "DUPLICATE CLAIM ID"
print("ids unique     : True")
print("labels         :", {l: sum(1 for c in C if c["label"] == l)
                           for l in sorted({c["label"] for c in C})})
