"""CT-S22 - the two algebraic facts behind claims S22-04 and S22-05, proved.

check_invariants.py 1(a) refused PROVEN with evidence_type=file_inspection, and
it was right to: a claim of proof has to carry one.  Both facts below are
established by simplify-to-zero in sympy AND by an independent numeric check at
random complex values, per the session method.

S22-04.  Check A6a as first written was a TAUTOLOGY.
  For M = [[m11,m12],[m21,m22]] with det M = 1 and m11 != 0, setting
      alpha = m11,  f2 = m12/alpha,  f1 = alpha*m21
  gives  (1 + f1 f2)/alpha - m22 = (1 + m12 m21 - m11 m22)/m11 = (1 - det M)/m11,
  which vanishes identically.  The check could not fail for ANY unimodular M,
  so it tested nothing.

S22-05.  Check A7 as first written used the WRONG ORDERING.
  vdPS write   M_inf = diag(a,1/a) * LOWER * UPPER, trace  a + (1+f1 f2)/a.
  This solver computes  e^{2 pi i L} * S_2pi(UPPER) * S_pi(LOWER), whose trace is
  a(1 + f1 f2) + 1/a.  The two differ by (a - 1/a) f1 f2, which is non-zero
  whenever a^2 != 1 and f1 f2 != 0 - so the ordering is not a harmless
  relabelling, and A7's O(1) failure was a mis-derivation, not a solver defect.
"""
import hashlib
from pathlib import Path

import mpmath as mp
import sympy as sp

OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


mp.mp.dps = 50
a, f1, f2, m11, m12, m21, m22 = sp.symbols("alpha f1 f2 m11 m12 m21 m22")

say("=" * 74)
say("CT-S22 - algebraic facts behind S22-04 and S22-05")
say("=" * 74)

# ---------------------------------------------------------------- S22-04
say("\nS22-04  check A6a is a tautology for any unimodular M with m11 != 0")
M = sp.Matrix([[m11, m12], [m21, m22]])
al = m11
g2 = m12 / al
g1 = al * m21
expr = sp.simplify((1 + g1 * g2) / al - m22)
say(f"  (1 + f1 f2)/alpha - m22  simplifies to  {expr}")
say(f"  and equals (1 - det M)/m11:  "
    f"{sp.simplify(expr - (1 - M.det()) / m11)}")
assert sp.simplify(expr - (1 - M.det()) / m11) == 0
onshell = sp.simplify(expr.subs(m22, (1 + m12 * m21) / m11))
say(f"  imposing det M = 1 (m22 = (1 + m12 m21)/m11):  {onshell}")
assert onshell == 0, "S22-04: the expression did not simplify to zero"
say("  [PROVEN symbolically] the check cannot fail, hence tests nothing.")

# independent numeric arm
worst = mp.mpf(0)
for _ in range(20):
    v11, v12, v21 = (mp.mpc(mp.rand(), mp.rand()) * 3 - 1 for _ in range(3))
    v22 = (1 + v12 * v21) / v11
    worst = max(worst, abs((1 + (v11 * v21) * (v12 / v11)) / v11 - v22))
say(f"  [numeric arm] worst residual over 20 random unimodular M: "
    f"{mp.nstr(worst, 6)}")
assert worst < mp.mpf(10) ** -40, "S22-04: numeric arm failed"

# ---------------------------------------------------------------- S22-05
say("\nS22-05  the two orderings give different traces")
D = sp.Matrix([[a, 0], [0, 1 / a]])
LOW = sp.Matrix([[1, 0], [f1, 1]])
UPP = sp.Matrix([[1, f2], [0, 1]])
t_vdps = sp.simplify((D * LOW * UPP).trace())
t_here = sp.simplify((D * UPP * LOW).trace())
say(f"  trace of diag*LOWER*UPPER (vdPS)      = {sp.simplify(t_vdps)}")
say(f"  trace of diag*UPPER*LOWER (this code) = {sp.simplify(t_here)}")
say(f"  vdPS form equals alpha + (1+f1 f2)/alpha ?  "
    f"{sp.simplify(t_vdps - (a + (1 + f1*f2)/a)) == 0}")
say(f"  this form equals alpha(1+f1 f2) + 1/alpha ? "
    f"{sp.simplify(t_here - (a*(1 + f1*f2) + 1/a)) == 0}")
assert sp.simplify(t_vdps - (a + (1 + f1 * f2) / a)) == 0
assert sp.simplify(t_here - (a * (1 + f1 * f2) + 1 / a)) == 0
diff = sp.simplify(sp.factor(t_here - t_vdps))
say(f"  difference = {diff}")
assert sp.simplify(diff - (a - 1 / a) * f1 * f2) == 0, \
    "S22-05: the difference is not (alpha - 1/alpha) f1 f2"
say("  = (alpha - 1/alpha) f1 f2, non-zero unless alpha^2 = 1 or f1 f2 = 0.")
say("  [PROVEN symbolically] the ordering is not a harmless relabelling.")

# independent numeric arm, at the Stage-1 values
av = mp.e ** (1j * mp.pi * mp.mpf(5) / 7 - 2j * mp.pi / 3)
g1v = mp.mpc("-0.341628128662157355261628222118",
             "2.26655453780766178080288766936")
g2v = mp.mpc("0.414666228985028625995025614217",
             "1.34431489688997778336962370307")
tr_target = 2 * mp.cos(mp.pi * mp.mpf(5) / 7)
r_here = abs(av * (1 + g1v * g2v) + 1 / av - tr_target)
r_vdps = abs(av + (1 + g1v * g2v) / av - tr_target)
say(f"  [numeric arm at the Stage-1 values (a,b) = (1/3, 5/7)]")
say(f"    |this ordering  - 2cos(pi b)| = {mp.nstr(r_here, 6)}")
say(f"    |vdPS ordering  - 2cos(pi b)| = {mp.nstr(r_vdps, 6)}")
assert r_here < mp.mpf(10) ** -25, "S22-05: the corrected ordering does not hold"
assert r_vdps > mp.mpf(10) ** -3, "S22-05: the wrong ordering is not distinguished"
say("  The corrected ordering holds; the one A7 originally used is off by O(1),")
say("  reproducing the observed failure exactly.")

say("\n" + "=" * 74)
say("BOTH FACTS PROVEN (symbolic simplify-to-zero + independent numeric arm)")
say("=" * 74)

outp = Path(__file__).resolve().parent.parent / "outputs" / "algebra_checks.out.txt"
text = "\n".join(OUT) + "\n"
outp.write_text(text, encoding="utf-8")
back = outp.read_text(encoding="utf-8")
assert back == text, "read-back of the output file differs from what was written"
print(f"\nwritten {outp}  sha256 {hashlib.sha256(back.encode()).hexdigest()}")
