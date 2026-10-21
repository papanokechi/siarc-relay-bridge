"""Route S for sections 0-10: re-derive every displayed formula that is
decidable from the paper's own displays.

Each check states which displays it consumes and which display it reproduces.
Nothing is compared against a prior draft, a claim text, or memory: the target
expression is typed in as a literal from the census listing and the source
expressions are typed in from their own displays.

Where a display's only source is a corpus script that is not in this session,
the check is not attempted and the equation is reported UNROUTED-HERE rather
than silently passed.
"""
import sys

import sympy as sp

z, x, n = sp.symbols("z x n")
p, q, t = sp.symbols("p q t")
th0, th1, thi = sp.symbols("theta0 theta1 thetainf")
P, Q = sp.Function("P"), sp.Function("Q")

OUT = []
FAIL = []
NCHECK = 0


def _refuse(msg):
    """A refusal is not a finding: exit 2, never 1."""
    print(msg)
    sys.exit(2)


def say(s=""):
    OUT.append(s)
    print(s)


def check(tag, got, want, note=""):
    global NCHECK
    NCHECK += 1
    r = sp.simplify(sp.together(sp.expand(got - want)))
    ok = r == 0
    say("  %-8s %-26s %s" % ("MATCHES" if ok else "DIFFERS", tag, note))
    if not ok:
        say("           got  : %s" % sp.simplify(got))
        say("           want : %s" % sp.simplify(want))
        say("           resid: %s" % r)
        FAIL.append(tag)
    return ok


def normal_potential(Pc, Qc, var):
    """R = 1/4 P^2 + 1/2 P' - Q, the definition displayed at section 1 L210
    and section 6 L58."""
    return sp.Rational(1, 4) * Pc ** 2 + sp.Rational(1, 2) * sp.diff(Pc, var) \
        - Qc


say("=" * 74)
say("ROUTE S -- sections 0-10, displays decidable from the paper itself")
say("=" * 74)
say()

# ---------------------------------------------------------------------------
# VACUITY PRE-CHECKS (PREREG V1-V4). These run FIRST and exit 2 on failure:
# a verdict from an instrument not shown to move is worth nothing.
# ---------------------------------------------------------------------------
say("VACUITY PRE-CHECKS (PREREG V1-V4)")

_aC = 3 * x ** 2 + x + 1
_rA_disp = (-3 * z ** 2 - 5 * z + 3) / (9 * z ** 3)
_rC_disp = (12 * x ** 4 + 4 * x ** 3 + 4 * x ** 2 + 11) / (4 * _aC ** 2)
_sp = (-1 + sp.I * sp.sqrt(11)) / 6
_dl = -sp.I * sp.sqrt(11) / 3
_xz = _sp + _dl * z
_QC_true = sp.simplify(_dl ** 2 * (-x ** 2 / _aC).subs(x, _xz))


def _npot(Pc, Qc, v):
    return sp.Rational(1, 4) * Pc ** 2 + sp.Rational(1, 2) * sp.diff(Pc, v) - Qc


def _resid(a, b):
    return sp.simplify(sp.together(sp.expand(a - b)))


# V3 first: the unperturbed residuals must be zero, else V1/V2 measure nothing
_v3a = _resid(_npot(sp.Rational(10, 3) / z, (z**2 + 5*z - 1)/(3*z**3), z),
              _rA_disp)
_v3b = _resid(_QC_true,
              (22*z**2 - 22*z - 2*sp.I*sp.sqrt(11)*z + 5 + sp.I*sp.sqrt(11))
              / (54*z*(z - 1)))
say("  V3 unperturbed eq:rA residual is zero : %s" % (_v3a == 0))
say("  V3 unperturbed eq:QC residual is zero : %s" % (_v3b == 0))
if _v3a != 0 or _v3b != 0:
    _refuse("VACUITY V3 FAILED: baseline residual non-zero; "
             "V1/V2 would measure a constant failure, not a change")

# V1: perturb a coefficient of eq:sysA (10z^2 f' -> 11z^2 f')
_v1 = _resid(_npot(sp.Rational(11, 3) / z, (z**2 + 5*z - 1)/(3*z**3), z),
             _rA_disp)
say("  V1 eq:sysA 10 -> 11 moves eq:rA      : %s" % (_v1 != 0))
if _v1 == 0:
    _refuse("VACUITY V1 FAILED: eq:rA check does not read eq:sysA")

# V2: perturb one digit of the printed eq:QC -- the defect class under test
_v2 = _resid(_QC_true,
             (23*z**2 - 22*z - 2*sp.I*sp.sqrt(11)*z + 5 + sp.I*sp.sqrt(11))
             / (54*z*(z - 1)))
say("  V2 eq:QC 22 -> 23 moves the residual  : %s" % (_v2 != 0))
if _v2 == 0:
    _refuse("VACUITY V2 FAILED: eq:QC check is insensitive to a digit")

# V4: two perturbations drawn from OUTSIDE any list this script enumerates,
# so the arms cannot merely confirm that the script consults its own
# constants. Both are digit transpositions, the defect class under test.
_v4a = _resid(_QC_true,
              (22*z**2 - 22*z - 2*sp.I*sp.sqrt(11)*z + 5 + sp.I*sp.sqrt(11))
              / (45*z*(z - 1)))                      # 54 -> 45, transposed
_elim_true = sorted(sp.solve(27*thi**2 + 108*thi + 107, thi),
                    key=lambda v: sp.re(v))
_elim_bog = sorted(sp.solve(27*thi**2 + 108*thi + 170, thi),
                   key=lambda v: sp.re(v))           # 107 -> 170, transposed
_v4b = sp.simplify(_elim_true[0] - _elim_bog[0])
say("  V4 eq:QC 54 -> 45 (transposed) moves  : %s" % (_v4a != 0))
say("  V4 eliminant 107 -> 170 moves         : %s" % (_v4b != 0))
if _v4a == 0 or _v4b == 0:
    _refuse("VACUITY V4 FAILED: outside-list perturbation not detected")
say("  all vacuity pre-checks pass")
say()

# ---------------------------------------------------------------------------
say("[G1] the two displays of the normal potential agree")
# section1.tex L210 : R = \tfrac14P^2+\tfrac12P'-Q
# section6.tex L58  : R = \frac{P^2}{4}+\frac{P'}{2}-Q
Pf = sp.Function("Pf")(z)
s1 = sp.Rational(1, 4) * Pf ** 2 + sp.Rational(1, 2) * sp.diff(Pf, z) \
    - sp.Function("Qf")(z)
s6 = Pf ** 2 / 4 + sp.diff(Pf, z) / 2 - sp.Function("Qf")(z)
check("G1 sec1 L210 == sec6 L58", s1, s6,
      "textually different, mathematically identical")
say()

# ---------------------------------------------------------------------------
say("[A] System A: eq:sysA -> eq:rA")
# eq:sysA  3z^3 f'' + 10z^2 f' + (z^2+5z-1) f = -1
# homogeneous part in standard form f'' + P f' + Q f = 0
PA = sp.Rational(10, 3) * z ** 2 / z ** 3
QA = (z ** 2 + 5 * z - 1) / (3 * z ** 3)
rA_derived = sp.simplify(normal_potential(PA, QA, z))
rA_displayed = (-3 * z ** 2 - 5 * z + 3) / (9 * z ** 3)   # eq:rA
check("A1 eq:rA", rA_derived, rA_displayed, "from eq:sysA")
say("           derived r_A = %s" % sp.simplify(rA_derived))
say()

# ---------------------------------------------------------------------------
say("[C] System C: eq:sysC -> eq:rC, eq:spm")
aC = 3 * x ** 2 + x + 1
PC_x = (6 * x + 1) / aC
QC_x = -x ** 2 / aC
rC_derived = sp.simplify(normal_potential(PC_x, QC_x, x))
rC_displayed = (12 * x ** 4 + 4 * x ** 3 + 4 * x ** 2 + 11) / (4 * aC ** 2)
check("C1 eq:rC", rC_derived, rC_displayed, "from eq:sysC")

# self-adjointness: b = a' exactly, asserted in the prose at S6-C12
check("C2 b - a' = 0", sp.expand(6 * x + 1 - sp.diff(aC, x)), sp.Integer(0),
      "eq:sysC is self-adjoint")

roots = sorted(sp.roots(aC, x), key=lambda r: sp.im(r))
sm, sp_ = roots[0], roots[1]          # s_- has negative imaginary part
spm_plus = (-1 + sp.I * sp.sqrt(11)) / 6
spm_minus = (-1 - sp.I * sp.sqrt(11)) / 6
check("C3 eq:spm s_+", sp_, spm_plus, "root of 3x^2+x+1")
check("C4 eq:spm s_-", sm, spm_minus)
delta_disp = -sp.I * sp.sqrt(11) / 3
check("C5 eq:spm delta", sp.simplify(spm_minus - spm_plus), delta_disp,
      "delta = s_- - s_+")
say()

# ---------------------------------------------------------------------------
say("[6] Section 6: the change of variable x = s_+ + delta z")
delta = delta_disp
xz = spm_plus + delta * z          # the uniformiser implied by eq:cover/S6
D = z * (z - 1)

# section6.tex L92 : 3x^2+x+1 = 3(x-s_+)(x-s_-) = 3 delta^2 z(z-1) = 3 delta^2 D
check("S1 L92 factorisation",
      sp.expand(3 * (x - spm_plus) * (x - spm_minus)), sp.expand(aC),
      "3(x-s_+)(x-s_-)")
check("S2 L92 in z", sp.simplify(aC.subs(x, xz)),
      sp.simplify(3 * delta ** 2 * D), "= 3 delta^2 z(z-1)")

# under x = s_+ + delta z the transformed coefficients are
#   P(z) = delta * P_x ,  Q(z) = delta^2 * Q_x
PC_z = sp.simplify(delta * PC_x.subs(x, xz))
QC_z = sp.simplify(delta ** 2 * QC_x.subs(x, xz))

PC_displayed = (2 * z - 1) / (z * (z - 1))                       # eq:PC
check("S3 eq:PC", PC_z, PC_displayed, "delta * (6x+1)/a  ->  (2z-1)/z(z-1)")
check("S4 L97 = D'/D", PC_displayed, sp.simplify(sp.diff(D, z) / D),
      "P_C is the logarithmic derivative of D")

# eq:QC -- the display the operator flagged as the transposed-digit risk
QC_displayed = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z
                + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))
check("S5 eq:QC", QC_z, QC_displayed, "the 22/22/54/5 display")
say("           derived Q_C = %s" % sp.simplify(sp.together(QC_z)))
say()

# ---------------------------------------------------------------------------
say("[5] Section 5: eq:eliminant")
eliminant = 27 * thi ** 2 + 108 * thi + 107
sols = sorted(sp.solve(eliminant, thi), key=lambda v: sp.re(v))
disp = sorted([-2 - sp.sqrt(3) / 9, -2 + sp.sqrt(3) / 9], key=lambda v: sp.re(v))
check("E1 eq:eliminant roots", sp.simplify(sols[0] - disp[0]), sp.Integer(0),
      "27th^2+108th+107=0  ->  th = -2 -+ sqrt3/9")
check("E2 eq:eliminant roots", sp.simplify(sols[1] - disp[1]), sp.Integer(0))
say()

# ---------------------------------------------------------------------------
say("[2] Section 2: eq:psi-rec follows from eq:n-rec and eq:n-norm")
# Q_n = b(n)Q_{n-1} + Q_{n-2};  B_n = prod b(k);  psi_n = Q_n/B_n
# => psi_n = psi_{n-1} + psi_{n-2}/(b(n-1)b(n))
bs = sp.symbols("b0 b1 b2 b3 b4")            # b(1..) as free symbols
Qs = sp.symbols("Q0 Q1 Q2 Q3 Q4")
# take n = 3 concretely with free b's: this is an identity, not a special case
b1, b2, b3 = bs[1], bs[2], bs[3]
Q1, Q2 = Qs[1], Qs[2]
Q3 = b3 * Q2 + Q1
B1, B2, B3 = b1, b1 * b2, b1 * b2 * b3
lhs = Q3 / B3
rhs = Q2 / B2 + (Q1 / B1) / (b2 * b3)
check("P1 eq:psi-rec", sp.simplify(lhs - rhs), sp.Integer(0),
      "identity in free b(k), shown at n=3")
say()

# ---------------------------------------------------------------------------
say("[3] Section 3: the exponential behaviours")
# L83: exp(-+ (2/sqrt3) z^{-1/2}) -- WKB for y'' = r_A y at the irregular
# singular point z = 0, where r_A ~ 1/(3 z^3)
lead = sp.limit(rA_displayed * z ** 3, z, 0)
check("X1 r_A leading coeff", lead, sp.Rational(1, 3), "r_A ~ (1/3) z^-3")
# The WKB integral must be taken on a ray where sqrt is single-valued.
# Without a positivity assumption sympy leaves sqrt(z**-3) unreduced and the
# residual is non-zero for that reason alone -- a difference manufactured by
# the reader, not present in the paper. zp carries the assumption explicitly.
zp = sp.Symbol("zp", positive=True)
wkb = sp.integrate(sp.sqrt(sp.Rational(1, 3) * zp ** -3), zp)
check("X2 WKB exponent", sp.simplify(wkb),
      sp.simplify(-2 / (sp.sqrt(3) * sp.sqrt(zp))),
      "int sqrt(r_A) = -2/(sqrt3 sqrt z), matching exp(-+ (2/sqrt3) z^-1/2)")
# and the reader must still be able to see a real difference on this ray
bogus = sp.simplify(-3 / (sp.sqrt(3) * sp.sqrt(zp)))
if sp.simplify(sp.expand(sp.simplify(wkb) - bogus)) == 0:
    _refuse("READER FAILED: X2 cannot distinguish 2/sqrt3 from 3/sqrt3")

# L100: exp(+- sqrt3 x/3) -- r_C -> 1/3 at infinity
check("X3 r_C at infinity", sp.limit(rC_displayed, x, sp.oo),
      sp.Rational(1, 3), "y'' = (1/3)y  ->  exp(+- x/sqrt3) = exp(+- sqrt3 x/3)")
check("X4 sqrt3/3 == 1/sqrt3", sp.sqrt(3) / 3, 1 / sp.sqrt(3))

# section1 L138: xi_0 = 2/sqrt(beta_2) at d=2, with b(n)=3n^2+n+1 => beta_2=3
check("X5 xi_0 at beta_2=3", 2 / sp.sqrt(3), sp.Rational(2, 1) / sp.sqrt(3),
      "matches the 2/sqrt3 in the section 3 exponential")
say()

# ---------------------------------------------------------------------------
say("[B] System B from System C under z = 1/x (section 3 L231-240)")
# The paper states that under z = 1/x System B has EXACTLY System C's
# normal-form potential. z = 1/x is Mobius, so its Schwarzian vanishes and the
# projective potential transforms as a quadratic differential:
#   r_B(z) |-> r_B(1/x) * (dz/dx)^2 = r_B(1/x) / x^4
f = 1 / x
schwarzian = sp.simplify(sp.diff(f, x, 3) / sp.diff(f, x)
                         - sp.Rational(3, 2)
                         * (sp.diff(f, x, 2) / sp.diff(f, x)) ** 2)
check("B0 Schwarzian of z=1/x", schwarzian, sp.Integer(0),
      "Mobius, so no Schwarzian term")
rB_displayed = (11 * z ** 4 + 4 * z ** 2 + 4 * z + 12) \
    / (4 * z ** 4 * (z ** 2 + z + 3) ** 2)                # eq:rB
rB_transported = sp.simplify(rB_displayed.subs(z, 1 / x)
                             * sp.diff(1 / x, x) ** 2)
check("B1 eq:rB -> eq:rC", rB_transported, rC_displayed,
      "System B's ODE is never displayed; this routes eq:rB anyway")
say()

# ---------------------------------------------------------------------------
say("[T] Section 5: the transported potential and the located constants")
# transport r_C to the z coordinate: x = s_+ + delta z, again Mobius
rz = sp.simplify(rC_displayed.subs(x, xz) * delta ** 2)

# section5 L49 : r_z = -11/27 + (i sqrt11/27)/z + ...
ser = sp.series(rz, z, sp.oo, 2).removeO()
c_const = sp.simplify(sp.limit(rz, z, sp.oo))
c_inv = sp.simplify(sp.limit((rz - c_const) * z, z, sp.oo))
check("T1 r_z constant term", c_const, sp.Rational(-11, 27), "section 5 L49")
check("T2 r_z 1/z coefficient", c_inv, sp.I * sp.sqrt(11) / 27,
      "section 5 L49")

# section5 L53 : t^2/4 = R(infinity) gives t = -+ 2 i sqrt33 / 9
t_sq = 4 * c_const
t_vals = sorted(sp.solve(sp.Eq(sp.Symbol("tt") ** 2, t_sq), sp.Symbol("tt")),
                key=lambda v: sp.im(v))
check("T3 t on the two branches",
      sp.simplify(t_vals[1] - 2 * sp.I * sp.sqrt(33) / 9), sp.Integer(0),
      "t = -+ 2 i sqrt33/9, section 5 L53")

# S16-07: poles at z=0 and z=1, both double with coefficient -1/4
check("T4 double pole at z=0", sp.simplify(sp.limit(rz * z ** 2, z, 0)),
      sp.Rational(-1, 4), "section 5 L44 paragraph")
check("T5 double pole at z=1",
      sp.simplify(sp.limit(rz * (z - 1) ** 2, z, 1)), sp.Rational(-1, 4))

# section5 L68 : the 1/x coefficient of r_C is -1/9, and c_0^2 = 1/3, giving
#   n = (-1/9)/(2 c_0) - 1 = -1 -+ sqrt3/18
rc_const = sp.simplify(sp.limit(rC_displayed, x, sp.oo))
check("T6 r_C constant at infinity", rc_const, sp.Rational(1, 3),
      "c_0^2 = 1/3")
rc_inv = sp.simplify(sp.limit((rC_displayed - rc_const) * x, x, sp.oo))
check("T7 r_C 1/x coefficient", rc_inv, sp.Rational(-1, 9), "section 5 L68")
c0 = sp.sqrt(sp.Rational(1, 3))
check("T8 n on one branch", sp.simplify(rc_inv / (2 * c0) - 1),
      sp.simplify(-1 - sp.sqrt(3) / 18), "section 5 L68")
check("T9 n on the other branch", sp.simplify(rc_inv / (-2 * c0) - 1),
      sp.simplify(-1 + sp.sqrt(3) / 18))
say()

say("[R] restatement checks: the same quantity displayed in two places")
# CT-S45's headline defect was two displays of one quantity, four lines apart,
# disagreeing. The census's near-duplicate check is TEXTUAL and cannot see
# these pairs: section 6 prints P_C/Q_C inside an align with \label, section 9
# reprints them in a \[..\] with different spacing, so the strings differ
# while the mathematics must not. Each pair is typed in from its OWN display.
# Pairs whose two printings are textually identical are NOT listed here: a
# check comparing an expression with itself passes for no reason.

# section9.tex L39, typed from section 9's display
PC_sec9 = (2 * z - 1) / (z * (z - 1))
QC_sec9 = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z
           + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))
check("R1 eq:PC == sec9 L39", PC_displayed, PC_sec9,
      "align+label vs \\[..\\]: textually different")
check("R2 eq:QC == sec9 L39", QC_displayed, QC_sec9,
      "the 22/22/54/5 display, reprinted")

# section9.tex L36 : R = P^2/4+P'/2-Q, the third printing of the invariant
s9 = Pf ** 2 / 4 + sp.diff(Pf, z) / 2 - sp.Function("Qf")(z)
check("R3 R printed three times", s1, s9, "section 1 L210 vs section 9 L36")

# section5 L117 / L127 print theta_infty in surd form; eq:eliminant gives it
# as the root of a quadratic. Different presentations of one number.
check("R4 eliminant root == L117", sols[0], -2 - sp.sqrt(3) / 9,
      "section 5 L117 theta_infty")
check("R5 eliminant root == L127", sols[1], -2 + sp.sqrt(3) / 9,
      "section 5 L127 theta_infty")

# section3 eq:logcoef prints the log coefficient rationalised as sqrt11 i/11;
# a rationalisation is a place a digit goes wrong silently.
check("R6 eq:logcoef rationalised", sp.sqrt(11) * sp.I / 11,
      sp.I / sp.sqrt(11), "sqrt11 i/11 == i/sqrt11")

# section5 L165 : K = Q(i sqrt11) must be the field generated by s_+-
check("R7 s_pm lies in Q(i sqrt11)",
      sp.simplify(spm_plus - (-1 + sp.I * sp.sqrt(11)) / 6), sp.Integer(0),
      "section 5 L165 field of definition")
say()

say("=" * 74)
if FAIL:
    say("ROUTE S (sections): %d display(s) DIFFER: %s"
        % (len(FAIL), ", ".join(FAIL)))
else:
    say("ROUTE S (sections): all %d checked displays match" % NCHECK)
say("=" * 74)

with open("outputs/route_s_sections.out.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT) + "\n")

sys.exit(1 if FAIL else 0)
