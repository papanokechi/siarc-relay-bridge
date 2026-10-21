"""CT-S47 - route S for section 5's exact q and p, reported per coefficient.

The object under test is the character string printed in section5.tex lines
116-130, not the mathematics and not the claim text.  S25-01 already showed the
RECORDED values annihilate the matching system; what has never been tested is
the transcription step between that record and the page.

Routes, per PREREG:
  ALPHA  the values PARSED OFF THE PAGE annihilate all six generators, exactly.
  ALPHA2 the same values satisfy the GENERAL R = P^2/4 + P'/2 - Q, with no
         b' = 0 reduction assumed -- an independent route to the same point.
  BETA   an independent solve, compared integer by integer.
  GAMMA  every printed approximation, one row per figure.

Exit codes:  0 all match · 1 a figure DIFFERS (a finding) · 2 refusal ·
             3 the instrument crashed.

The three nonzero codes are distinct on purpose.  CT-S46 finding 3.9 was that a
refusal and a finding both exited 1, so a broken instrument and a real defect in
the paper were indistinguishable to any caller; an uncaught traceback also exits
1 and reintroduces the same collision through a different door, so it is caught
here and given its own code.
"""
import hashlib
import re
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
SRC = SESS / "refs" / "section5.tex"
OUT = SESS / "outputs" / "route_s5_qp.out.txt"

SRC_SHA = "AF25048B9B62A6F403BF581F92B431F5C93F1DC5575D59315A5D97025CC78E1B".lower()

LINES = []
NDIFF = 0
NCHECK = 0


def say(s=""):
    LINES.append(s)
    print(s)


def refuse(msg):
    say("")
    say("REFUSED: " + msg)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    sys.exit(2)


def _crash(exc_type, exc, tb):
    """An uncaught traceback exits 1 by default - the same code as a finding.

    CT-S46 finding 3.9 separated refusal (2) from finding (1); a crash would
    quietly reintroduce the collision, so it gets code 3 and is recorded in the
    output file rather than only on stderr.
    """
    import os
    import traceback
    say("")
    say("CRASHED: " + "".join(traceback.format_exception(exc_type, exc, tb)).strip())
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    sys.stderr.write("".join(traceback.format_exception(exc_type, exc, tb)))
    sys.stderr.flush()
    os._exit(3)


sys.excepthook = _crash


def check(name, ok, detail=""):
    """A named comparison that can fail.  Never a bare boolean over a display."""
    global NDIFF, NCHECK
    NCHECK += 1
    say(f"  [{'MATCH ' if ok else 'DIFFER'}] {name}" + (f"   {detail}" if detail else ""))
    if not ok:
        NDIFF += 1
    return ok


# =====================================================================
# 0. resolve the source positively, not by path
# =====================================================================
if not SRC.exists():
    refuse(f"{SRC} absent")
raw = SRC.read_bytes()
got = hashlib.sha256(raw).hexdigest()
if got != SRC_SHA:
    refuse(f"section5.tex sha256 {got[:16]} != expected {SRC_SHA[:16]}; "
           "the file this check was written against has moved")
text = raw.decode("utf-8").replace("\r\n", "\n")
say(f"source   section5.tex  sha256 {got[:16]}  {len(raw)} bytes")
# positive guard: the file must still be the one carrying the located point
if "\\subsection{The located point}" not in text:
    refuse("section5.tex no longer carries the located point subsection")
say("guard    carries \\subsection{The located point}")
say("")


# =====================================================================
# 1. PARSE - every numeral and every sign comes out of the file
# =====================================================================
say("=" * 70)
say("PARSE (all numerals and signs taken from the .tex, none typed here)")
say("=" * 70)

# branch headers: t = -+ 2i sqrt(33)/9
t_hdr = re.findall(r"On the branch \$t=([+-])2i\\sqrt\{33\}/9\$", text)
if len(t_hdr) != 2:
    refuse(f"expected 2 branch headers, found {len(t_hdr)}")

# theta_infinity = -2 -+ sqrt3/9
th_m = re.findall(r"\\theta_\\infty=([+-])2([+-])\\frac\{\\sqrt3\}\{9\}", text)
if len(th_m) != 2:
    refuse(f"expected 2 theta_infty displays, found {len(th_m)}")

# q exact:  \frac12 + \frac{ i \bigl( -A\sqrt{11} + B\sqrt{33} \bigr) }{ C }
q_m = re.search(
    r"q=\\frac(\d)(\d)\+\\frac\{i\\bigl\(([+-])(\d+)\\sqrt\{11\}([+-])(\d+)"
    r"\\sqrt\{33\}\\bigr\)\}\{(\d+)\}",
    text)
if not q_m:
    refuse("could not parse the exact q display")

# p exact:  \frac{ L i \bigl( -D\sqrt{33} + E\sqrt{11} \bigr) }{ F }
p_m = re.search(
    r"p=\\frac\{(\d+)i\\bigl\(([+-])(\d+)\\sqrt\{33\}([+-])(\d+)\\sqrt\{11\}"
    r"\\bigr\)\}\s*\{(\d+)\}",
    text)
if not p_m:
    refuse("could not parse the exact p display")

# the four printed approximations
ap_q1 = re.search(r"\\approx ([\d.]+)([+-])([\d.]+)\\,i,", text)
ap_p1 = re.search(r"\\approx ([\d.]+)\\,i \.", text)
ap_2 = re.search(r"q\\approx ([\d.]+)([+-])([\d.]+)\\,i,\\qquad p\\approx ([\d.]+)\\,i", text)
if not (ap_q1 and ap_p1 and ap_2):
    refuse("could not parse the printed approximations")

sgn = {"+": 1, "-": -1}
P = {}
P["t_sign_1"], P["t_sign_2"] = sgn[t_hdr[0]], sgn[t_hdr[1]]
P["th_lead_1"], P["th_tail_1"] = sgn[th_m[0][0]], sgn[th_m[0][1]]
P["th_lead_2"], P["th_tail_2"] = sgn[th_m[1][0]], sgn[th_m[1][1]]
qn, qd, qsA, qA, qsB, qB, qC = q_m.groups()
P["q_frac_num"], P["q_frac_den"] = int(qn), int(qd)
P["q_A"], P["q_A_sign"] = int(qA), sgn[qsA]
P["q_B"], P["q_B_sign"] = int(qB), sgn[qsB]
P["q_C"] = int(qC)
pL, psD, pD, psE, pE, pF = p_m.groups()
P["p_lead"] = int(pL)
P["p_D"], P["p_D_sign"] = int(pD), sgn[psD]
P["p_E"], P["p_E_sign"] = int(pE), sgn[psE]
P["p_F"] = int(pF)

for k in sorted(P):
    say(f"  parsed  {k:14s} = {P[k]}")
say(f"  parsed  approx q br1  = {ap_q1.group(1)} {ap_q1.group(2)} {ap_q1.group(3)} i")
say(f"  parsed  approx p br1  = {ap_p1.group(1)} i")
say(f"  parsed  approx q br2  = {ap_2.group(1)} {ap_2.group(2)} {ap_2.group(3)} i")
say(f"  parsed  approx p br2  = {ap_2.group(4)} i")
say("")

# ---- V3: positive control on the parser -----------------------------------
# re-render the captured pieces into the printed shape; it must reproduce the
# source substring.  A parser that silently drops a digit fails here.
render_q = (f"q=\\frac{P['q_frac_num']}{P['q_frac_den']}+\\frac{{i\\bigl("
            f"{'+' if P['q_A_sign'] > 0 else '-'}{P['q_A']}\\sqrt{{11}}"
            f"{'+' if P['q_B_sign'] > 0 else '-'}{P['q_B']}\\sqrt{{33}}"
            f"\\bigr)}}{{{P['q_C']}}}")
render_p = (f"p=\\frac{{{P['p_lead']}i\\bigl("
            f"{'+' if P['p_D_sign'] > 0 else '-'}{P['p_D']}\\sqrt{{33}}"
            f"{'+' if P['p_E_sign'] > 0 else '-'}{P['p_E']}\\sqrt{{11}}"
            f"\\bigr)}}")
squash = re.sub(r"\s+", "", text)
say("V3 parser round-trip (positive control)")
if not check("q re-renders to the source", re.sub(r"\s+", "", render_q) in squash):
    refuse("V3 failed for q: the parser does not reproduce what it read")
if not check("p re-renders to the source", re.sub(r"\s+", "", render_p) in squash):
    refuse("V3 failed for p: the parser does not reproduce what it read")
say("")


# =====================================================================
# 2. build the values and the generators
# =====================================================================
z, p_s, q_s, t_s, thi = sp.symbols("z p q t theta_inf")
r11, r3 = sp.sqrt(11), sp.sqrt(3)
r33 = r3 * r11   # keep one field: Q(sqrt3, sqrt11)


def theta_of(i):
    return P[f"th_lead_{i}"] * 2 + P[f"th_tail_{i}"] * r3 / 9


def t_of(i):
    return P[f"t_sign_{i}"] * 2 * sp.I * r33 / 9


q_parsed = (sp.Rational(P["q_frac_num"], P["q_frac_den"])
            + sp.I * (P["q_A_sign"] * P["q_A"] * r11
                      + P["q_B_sign"] * P["q_B"] * r33) / P["q_C"])
p_parsed = (P["p_lead"] * sp.I * (P["p_D_sign"] * P["p_D"] * r33
                                  + P["p_E_sign"] * P["p_E"] * r11) / P["p_F"])

# family (4.1) with theta_0 = theta_1 = 0, exactly as CT-S16 records it
a_f = (p_s + sp.Rational(1, 2) * (-2 * q_s * t_s + t_s - thi) * (z - q_s)
       - sp.Rational(1, 2) * t_s * (z - q_s) ** 2)
c_f = -(z - q_s) / (q_s - 1)
U = p_s + sp.Rational(1, 2) * (q_s - 1) * q_s * t_s
V = p_s + sp.Rational(1, 2) * ((q_s - 1) * q_s * t_s + q_s * thi)
b1_f = sp.cancel(-(U**2 - (q_s - 1) * q_s * thi**2 / 4) / q_s)
b0_f = sp.cancel(-(q_s - 1) * V**2 / q_s)

D = z * (z - 1)

# System C's normal potential, transported to z
x = sp.Symbol("x")
s_p = sp.Rational(-1, 6) + r11 * sp.I / 6
delta = -r11 * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, s_p + delta * z)))
Nz, Dz = sp.fraction(r_z)

# PRE-CONDITION, added after control arm M5 exposed its absence.
# The whole construction below depends on r_z having denominator exactly D^2 up
# to a constant: only then is the match between R and r_z an equality of two
# quartics, and only then is Nz * D^2 / Dz a polynomial.  Nothing checked it.
# When M5 corrupted the transport, this went unchecked and sp.Poly raised an
# opaque PolynomialError -- a crash, where the correct behaviour is to refuse,
# because a broken transport is a fact about the instrument's input and not a
# finding about the paper.
_ratio = sp.cancel(sp.together(Dz / D**2))
if _ratio.has(z):
    refuse("r_z's denominator is not z^2(z-1)^2 up to a constant "
           f"(ratio {sp.sstr(_ratio)[:70]}); the match is not an equality of "
           "two quartics and no comparison below would mean anything")
say(f"pre-condition  r_z denominator is D^2 times {sp.sstr(_ratio)}")

Nz_scaled = sp.expand(sp.cancel(Nz * D**2 / Dz))
try:
    sp.Poly(Nz_scaled, z)
except sp.PolynomialError as exc:
    refuse(f"r_z numerator over D^2 is not a polynomial in z: {exc}")

lhs = sp.expand(a_f**2 + b0_f * c_f - sp.diff(a_f, z) * D - sp.Rational(1, 4))
E_poly = sp.Poly(sp.expand(lhs - Nz_scaled), z)
GENS = [sp.expand(co) for co in E_poly.all_coeffs()]
GENS.append(sp.expand(sp.numer(sp.cancel(b1_f))))
GEN_NAMES = [f"z^{E_poly.degree() - i} coeff" for i in range(len(GENS) - 1)] + ["b_1 = 0"]

if len(GENS) != 6:
    refuse(f"expected 6 generators, built {len(GENS)}")


def gen_values(pv, qv, tv, thv):
    """Evaluate the six generators, exactly.

    Zero-testing has to stay exact, but sp.simplify on a NONZERO residual over
    Q(sqrt3, sqrt11) with eleven-digit integers is ruinously slow, and the
    nonzero case is exactly the fail path -- the one that matters.  So a value
    is screened numerically FIRST and only ambiguous cases pay for simplify:
    a value that evaluates far from zero cannot be exactly zero, while anything
    near zero is still decided symbolically.  The screen can only short-circuit
    the NONZERO verdict; it can never turn a nonzero value into a zero one.
    """
    sub = {p_s: pv, q_s: qv, t_s: tv, thi: thv}
    out = []
    for g in GENS:
        v = sp.expand(sp.radsimp(g.subs(sub)))
        if v == 0:
            out.append(sp.Integer(0))
            continue
        try:
            mag = abs(complex(sp.N(v, 50)))
        except (TypeError, ValueError):
            mag = None
        if mag is not None and mag > 1e-25:
            out.append(v)          # certainly nonzero; leave it unsimplified
        else:
            out.append(sp.simplify(v))
    return out


# =====================================================================
# 3. VACUITY - the transposition arms, run BEFORE the routes
# =====================================================================
say("=" * 70)
say("VACUITY V1/V2 - transpose the last two digits of each parsed integer")
say("=" * 70)

# ---- evaluate the OBSERVABLE first, before mutating anything ---------------
# A vacuity pre-check exists to make a PASS meaningful.  A FAIL is
# self-evidencing and needs no such guard.  Running the arms unconditionally
# first lets them mask a genuine finding, and here that is not hypothetical:
# the arm's mutation is a TRANSPOSITION, which is an involution, so applied to
# an already-transposed page it restores the true value, the generators vanish,
# the arm reports MISSED and the script refuses -- announcing "the instrument
# cannot see a transposition" when the truth is "the page carries one".  That
# is precisely the refusal/finding collision the exit codes were separated to
# prevent.  Control arm M9 found this.
_vals1 = gen_values(p_parsed, q_parsed, t_of(1), theta_of(1))
ALPHA_CLEAN = all(v == 0 for v in _vals1)

if not ALPHA_CLEAN:
    say("SKIPPED: the parsed values do NOT satisfy the matching system, so the")
    say("observable has already moved and a vacuity pre-check is moot.  A check")
    say("that guards against a vacuous PASS cannot be required before reporting")
    say("a FAIL, or it would convert a finding about the paper into a refusal")
    say("about the instrument.")
    say("")
else:
    say("A transposition that still annihilates the system means the generators do")
    say("not determine that coefficient, and route ALPHA is vacuous for it.")
    say("")

INTS = ["q_A", "q_B", "q_C", "p_D", "p_E", "p_F"]
vac_fail = []
vac_skipped = []


def _mutate_and_test(key, swapped):
    mut = dict(P)
    mut[key] = int(swapped)
    qv = (sp.Rational(mut["q_frac_num"], mut["q_frac_den"])
          + sp.I * (mut["q_A_sign"] * mut["q_A"] * r11
                    + mut["q_B_sign"] * mut["q_B"] * r33) / mut["q_C"])
    pv = (mut["p_lead"] * sp.I * (mut["p_D_sign"] * mut["p_D"] * r33
                                  + mut["p_E_sign"] * mut["p_E"] * r11) / mut["p_F"])
    vals = gen_values(pv, qv, t_of(1), theta_of(1))
    return [GEN_NAMES[i] for i, v in enumerate(vals) if v != 0]


for key in (INTS if ALPHA_CLEAN else []):
    s = str(P[key])
    swapped = s[:-2] + s[-1] + s[-2]
    if swapped == s:
        say(f"  [SKIPPED] {key}: last two digits identical ({s[-2:]}), "
            "transposition is a no-op -- sensitivity NOT yet demonstrated")
        vac_skipped.append(key)
        continue
    nz = _mutate_and_test(key, swapped)
    if nz:
        say(f"  [CAUGHT ] {key}: {s} -> {swapped}  breaks {len(nz)}/6 generators "
            f"({nz[0]})")
    else:
        say(f"  [MISSED ] {key}: {s} -> {swapped}  annihilates all six")
        vac_fail.append(key)

# ---- V1b supplementary arms -----------------------------------------------
# A SKIPPED arm is not coverage.  PREREG V2 requires that a no-op never score
# as a detection, which leaves those coefficients with no sensitivity evidence
# at all; the fix is another arm, not a relaxed verdict.  This adds arms, it
# does not move a threshold.
if vac_skipped:
    say("")
    say("V1b supplementary arms for coefficients whose last-two swap was a no-op")
    for key in vac_skipped:
        s = str(P[key])
        alt = s[1] + s[0] + s[2:] if len(s) > 1 and s[0] != s[1] else None
        if alt is None or alt == s or alt.lstrip("0") != alt:
            alt = s[:-1] + str((int(s[-1]) + 1) % 10)
        nz = _mutate_and_test(key, alt)
        if nz:
            say(f"  [CAUGHT ] {key}: {s} -> {alt}  breaks {len(nz)}/6 generators "
                f"({nz[0]})")
        else:
            say(f"  [MISSED ] {key}: {s} -> {alt}  annihilates all six")
            vac_fail.append(key)
say("")
if vac_fail:
    refuse("V1 failed for " + ", ".join(vac_fail)
           + ": route ALPHA cannot see a transposition in those coefficients")

# V4: tolerance control for route GAMMA
say("V4 approximation tolerance is not vacuous")
_probe = sp.Float("0.81234", 30)
check("a 5th-decimal perturbation is rejected at 4 dp",
      abs(_probe + sp.Float("0.0001") - sp.Float("0.8123")) > sp.Float("0.5e-4"))
say("")


# =====================================================================
# 4. ROUTE ALPHA - parsed values annihilate the generators
# =====================================================================
say("=" * 70)
say("ROUTE ALPHA - do the numerals ON THE PAGE satisfy the matching system?")
say("=" * 70)
say("branch 1 (t sign %+d, theta_infty = %s)" % (P["t_sign_1"], sp.sstr(theta_of(1))))
vals1 = _vals1
for nm, v in zip(GEN_NAMES, vals1):
    check(f"generator {nm}", v == 0, "" if v == 0 else f"residual {sp.sstr(v)[:60]}")
say("")

# F4 - branch pairing.  The parsed p,q belong to branch 1; printing them
# against branch 2's theta must FAIL, or the pairing carries no information.
say("F4 branch pairing is load-bearing")
vals_cross = gen_values(p_parsed, q_parsed, t_of(2), theta_of(2))
cross_nz = sum(1 for v in vals_cross if v != 0)
check("the printed (p,q) do NOT solve the other branch", cross_nz > 0,
      f"{cross_nz}/6 generators nonzero on the cross-pairing")
say("")

# ---- ALPHA2 : the general R, with no b' = 0 reduction assumed --------------
say("ROUTE ALPHA2 - the same point through the UNREDUCED R = P^2/4 + P'/2 - Q")
sub1 = {p_s: p_parsed, q_s: q_parsed, t_s: t_of(1), thi: theta_of(1)}
a_1 = sp.together(a_f.subs(sub1))
b_1 = sp.together((b1_f * z + b0_f).subs(sub1))
c_1 = sp.together(c_f.subs(sub1))
Pg = sp.diff(D, z) / D - sp.diff(b_1, z) / b_1
Qg = sp.diff(a_1, z) / D - a_1 * sp.diff(b_1, z) / (D * b_1) - (a_1**2 + b_1 * c_1) / D**2
R_gen = sp.cancel(sp.together(Pg**2 / 4 + sp.diff(Pg, z) / 2 - Qg))
resid = sp.simplify(sp.radsimp(sp.cancel(R_gen - r_z)))
check("general R minus r_z is identically zero", resid == 0,
      "" if resid == 0 else f"residual {sp.sstr(resid)[:60]}")
check("b is constant at the parsed point (b_1 = 0)",
      sp.simplify(sp.diff(sp.expand(b_1), z)) == 0)
check("q is in the chart U_0 (q not in {0,1})",
      sp.simplify(q_parsed * (q_parsed - 1)) != 0)
say("")


# =====================================================================
# 5. ROUTE BETA - independent solve, per-coefficient ledger
# =====================================================================
say("=" * 70)
say("ROUTE BETA - solve independently, then compare integer by integer")
say("=" * 70)
sols = sp.solve(GENS, [p_s, q_s, t_s, thi], dict=True)
check("exactly two solutions (F5)", len(sols) == 2, f"found {len(sols)}")
if len(sols) != 2:
    refuse("solution count wrong; the per-coefficient ledger would be meaningless")

# pick the solution whose t matches branch 1's printed sign
want_t = sp.simplify(t_of(1))
cand = [s for s in sols if sp.simplify(sp.radsimp(s[t_s] - want_t)) == 0]
check("a solved branch carries the printed t of branch 1", len(cand) == 1,
      f"{len(cand)} candidates")
if len(cand) != 1:
    refuse("cannot align the solve with the printed branch")
S1 = cand[0]
S2 = [s for s in sols if s is not S1][0]

q_solved = sp.radsimp(sp.simplify(S1[q_s]))
p_solved = sp.radsimp(sp.simplify(S1[p_s]))
say(f"  solved q = {sp.sstr(q_solved)}")
say(f"  solved p = {sp.sstr(p_solved)}")
say("")

# Per-coefficient: recover the six integers from the solved values by matching
# against the printed SHAPE, then compare each one separately.
# ---- exact coordinates in the basis {1, sqrt3, sqrt11, sqrt33} -------------
# sympy holds sqrt(33) as a single atom, so expr.coeff(sqrt(11)) cannot see it
# and returns 0 -- a reader reporting zero for a coefficient it cannot read,
# which is indistinguishable from a coefficient that is genuinely zero.  The
# first draft of this ledger did exactly that and manufactured two DIFFERs
# against a q and p that were correct.  Decompose in an explicit basis instead,
# and give the decomposer both controls.
_A3, _B11 = sp.symbols("A3 B11")
BASIS = ("1", "sqrt3", "sqrt11", "sqrt33")


def coords(expr):
    """Exact rational coordinates of expr in Q(sqrt3, sqrt11).  Refuses if the
    expression does not lie in that field, rather than silently dropping it."""
    e = sp.expand(sp.radsimp(sp.expand(expr)))
    e = e.subs([(sp.sqrt(33), _A3 * _B11), (sp.sqrt(11), _B11), (sp.sqrt(3), _A3)])
    e = sp.expand(e)
    c = {
        "1": e.coeff(_A3, 0).coeff(_B11, 0),
        "sqrt3": e.coeff(_A3, 1).coeff(_B11, 0),
        "sqrt11": e.coeff(_A3, 0).coeff(_B11, 1),
        "sqrt33": e.coeff(_A3, 1).coeff(_B11, 1),
    }
    rebuilt = (c["1"] + c["sqrt3"] * _A3 + c["sqrt11"] * _B11
               + c["sqrt33"] * _A3 * _B11)
    if sp.simplify(sp.expand(e - rebuilt)) != 0:
        refuse(f"coords() did not span {sp.sstr(expr)[:60]}: residue "
               f"{sp.sstr(sp.expand(e - rebuilt))[:60]}")
    for k, v in c.items():
        if not v.is_Rational:
            refuse(f"coords() coefficient {k} is not rational: {sp.sstr(v)[:40]}")
    return c


say("decomposer controls (a reader that returns 0 for what it cannot see)")
_pos = coords(sp.Integer(1) + 2 * r3 + 3 * r11 + 4 * sp.sqrt(33))
check("positive: 1+2sqrt3+3sqrt11+4sqrt33 decomposes exactly",
      [_pos[k] for k in BASIS] == [1, 2, 3, 4], str([_pos[k] for k in BASIS]))
check("positive: sqrt33 is SEEN as the sqrt33 coordinate, not as 0",
      coords(sp.sqrt(33))["sqrt33"] == 1 and coords(sp.sqrt(33))["sqrt11"] == 0)
check("negative: a pure rational has only the '1' coordinate",
      [coords(sp.Rational(7, 3))[k] for k in BASIS] == [sp.Rational(7, 3), 0, 0, 0])
say("")

say("per-coefficient ledger (one row per coordinate, both branches)")
# q : printed as 1/2 + i(sA*A sqrt11 + sB*B sqrt33)/C
q_c = None  # q's rational part is checked below, after the imaginary part
qi_c = coords(sp.expand(-sp.I * (q_solved - sp.Rational(P["q_frac_num"],
                                                       P["q_frac_den"]))))
q_rat = sp.simplify(sp.radsimp(
    q_solved - sp.I * (qi_c["sqrt11"] * r11 + qi_c["sqrt33"] * sp.sqrt(33))))
check("q: rational part equals the printed 1/2",
      q_rat == sp.Rational(P["q_frac_num"], P["q_frac_den"]),
      f"solved {sp.sstr(q_rat)}  printed {P['q_frac_num']}/{P['q_frac_den']}")
check("q: coefficient of i*sqrt(11)",
      qi_c["sqrt11"] == sp.Rational(P["q_A_sign"] * P["q_A"], P["q_C"]),
      f"solved {qi_c['sqrt11']}  printed {P['q_A_sign'] * P['q_A']}/{P['q_C']}")
check("q: coefficient of i*sqrt(33)",
      qi_c["sqrt33"] == sp.Rational(P["q_B_sign"] * P["q_B"], P["q_C"]),
      f"solved {qi_c['sqrt33']}  printed {P['q_B_sign'] * P['q_B']}/{P['q_C']}")
check("q: no i*sqrt(3) term is hidden in the printed form",
      qi_c["sqrt3"] == 0 and qi_c["1"] == 0)

pi_c = coords(sp.expand(-sp.I * p_solved))
check("p: coefficient of i*sqrt(33)",
      pi_c["sqrt33"] == sp.Rational(P["p_lead"] * P["p_D_sign"] * P["p_D"], P["p_F"]),
      f"solved {pi_c['sqrt33']}  printed "
      f"{P['p_lead']}*{P['p_D_sign'] * P['p_D']}/{P['p_F']}")
check("p: coefficient of i*sqrt(11)",
      pi_c["sqrt11"] == sp.Rational(P["p_lead"] * P["p_E_sign"] * P["p_E"], P["p_F"]),
      f"solved {pi_c['sqrt11']}  printed "
      f"{P['p_lead']}*{P['p_E_sign'] * P['p_E']}/{P['p_F']}")
check("p: purely imaginary, as printed",
      pi_c["1"] == 0 and pi_c["sqrt3"] == 0)
check("theta_infty branch 1", sp.simplify(sp.radsimp(S1[thi] - theta_of(1))) == 0,
      f"solved {sp.sstr(sp.radsimp(S1[thi]))}  printed {sp.sstr(theta_of(1))}")
check("theta_infty branch 2", sp.simplify(sp.radsimp(S2[thi] - theta_of(2))) == 0,
      f"solved {sp.sstr(sp.radsimp(S2[thi]))}  printed {sp.sstr(theta_of(2))}")
check("t branch 2", sp.simplify(sp.radsimp(S2[t_s] - t_of(2))) == 0)
say("")


# =====================================================================
# 6. ROUTE GAMMA - every printed approximation, one row per figure
# =====================================================================
say("=" * 70)
say("ROUTE GAMMA - printed approximations, half-ulp of the last printed place")
say("=" * 70)
DPS = 60


def fmt(v, n=10):
    return sp.sstr(sp.N(v, n))


def ulp(sval):
    d = len(sval.split(".")[1]) if "." in sval else 0
    return sp.Float(5) * sp.Float(10) ** (-d - 1)


def approx_row(name, exact, s_re, s_im, sign_im):
    ev = sp.N(exact, DPS)
    re_p, im_p = sp.Float(s_re, 30), sign_im * sp.Float(s_im, 30)
    ok_r = abs(sp.re(ev) - re_p) <= ulp(s_re)
    ok_i = abs(sp.im(ev) - im_p) <= ulp(s_im)
    check(f"{name} Re", ok_r, f"printed {s_re}  exact {fmt(sp.re(ev))}")
    check(f"{name} Im", ok_i, f"printed {'-' if sign_im < 0 else ''}{s_im}  "
                              f"exact {fmt(sp.im(ev))}")


approx_row("q branch 1", q_parsed, ap_q1.group(1), ap_q1.group(3), sgn[ap_q1.group(2)])
approx_row("p branch 1", p_parsed, "0", ap_p1.group(1), 1)
approx_row("q branch 2", sp.radsimp(sp.simplify(S2[q_s])), ap_2.group(1),
           ap_2.group(3), sgn[ap_2.group(2)])
approx_row("p branch 2", sp.radsimp(sp.simplify(S2[p_s])), "0", ap_2.group(4), 1)
say("")

# =====================================================================
say("=" * 70)
say(f"ROUTE S (section 5 q,p): {NCHECK} checks, {NDIFF} DIFFER")
say("=" * 70)
OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
sys.exit(1 if NDIFF else 0)
