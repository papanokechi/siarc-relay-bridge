"""CT-S17 - airtight re-check of the suspected typo in vdPS family (4.1)'s b(z).

Transcribed BY LOOKING at two rendered page images:
  * journal Ann. Inst. Fourier 59 (2009) p.2655  (pages/vdps_p2655.png, and the
    8x crop pages/vdps_j2655_bz_LOOK.png)
  * arXiv:0902.1702 v5, p.34                     (pages/arxiv_v5_p34_bz_LOOK.png)
Both print the SAME first term, with no t.

Printed:
  A = z(z-1)(A_inf + A_0/z + A_1/(z-1)) = [[a,b],[c,-a]]
  a(z) = p + (1/2)(-2qt + t - th_inf)(z-q) - (1/2) t (z-q)^2
  b(z) = -[ z( (p + (1/2)(q-1)q)^2 - th1^2/4
              + (q-1)( th0^2/4 - th1^2/4 - q th_inf^2/4 ) ) ] / q
         -[ (q-1)(p + (1/2)((q-1)q t - th0 + q th_inf))
                 (p + (1/2)((q-1)q t + th0 + q th_inf)) ] / q
  c(z) = -(z-q)/(q-1)

Since A(z) = z(z-1)A_inf + (z-1)A_0 + z A_1, we have A(0) = -A_0 and A(1) = A_1,
so the paper's own constraints det A_i = -th_i^2/4 read

    det A(0) = -th0^2/4      and      det A(1) = -th1^2/4.

These are the paper's OWN equations, not an external assumption.  We test the
printed b against them, and the single-character variant with q -> q t in the
first term.
"""
import sympy as sp

p, q, t, th0, th1, thi, z = sp.symbols("p q t theta_0 theta_1 theta_inf z")


def build(first_term):
    a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) \
        - sp.Rational(1, 2) * t * (z - q) ** 2
    b = (-(z * (first_term - th1**2 / 4
                + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1) * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
    c = -(z - q) / (q - 1)
    return sp.Matrix([[a, b], [c, -a]])


READINGS = {
    "AS PRINTED        (p + 1/2 (q-1)q )^2":
        (p + sp.Rational(1, 2) * (q - 1) * q) ** 2,
    "PROPOSED CORRECTION (p + 1/2 (q-1)q t)^2":
        (p + sp.Rational(1, 2) * (q - 1) * q * t) ** 2,
}

for name, ft in READINGS.items():
    A = build(ft)
    print("=" * 70)
    print(name)
    for zv, target, lab in [(0, -th0**2 / 4, "det A(0) = -theta_0^2/4"),
                            (1, -th1**2 / 4, "det A(1) = -theta_1^2/4")]:
        resid = sp.simplify(sp.together(A.subs(z, zv).det() - target))
        resid = sp.factor(sp.cancel(resid))
        ok = resid == 0
        print(f"   {lab:28s} residual = {resid}")
        print(f"   {'':28s} SATISFIED IDENTICALLY: {ok}")

# ---- the residual is not merely 'nonzero-looking': show it is not identically
# zero by exhibiting a rational point where it fails, with th0=th1=0 as for
# System C.
print("=" * 70)
A_printed = build(READINGS["AS PRINTED        (p + 1/2 (q-1)q )^2"])
r1 = sp.cancel(A_printed.subs(z, 1).det() + th1**2 / 4)
pt = {p: sp.Rational(2, 7), q: sp.Rational(5, 3), t: sp.Rational(11, 4),
      th0: 0, th1: 0, thi: sp.Rational(3, 5)}
val = sp.nsimplify(sp.cancel(r1.subs(pt)))
print("printed reading, det A(1) + theta_1^2/4 at an exact rational point:")
print("   point   :", {str(k): str(v) for k, v in pt.items()})
print("   value   :", val, "=", sp.N(val, 20))
print("   nonzero :", val != 0)

# ---- CONTROL: a deliberately wrong 'correction' must NOT satisfy the
# constraint, otherwise the test would accept anything.
print("=" * 70)
A_ctrl = build((p + sp.Rational(1, 2) * (q - 1) * q * t**2) ** 2)
ctrl = sp.cancel(sp.simplify(A_ctrl.subs(z, 1).det() + th1**2 / 4))
print("CONTROL, bogus variant (q-1)q t^2 :")
print("   det A(1) residual identically zero?", ctrl == 0)
assert ctrl != 0, "CONTROL FAILED: the test accepts a wrong variant"
print("   control behaved correctly (test is discriminating)")
