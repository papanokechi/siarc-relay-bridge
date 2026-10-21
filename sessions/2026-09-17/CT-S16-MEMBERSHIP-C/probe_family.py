"""CT-S16 - probe the vdPS (0,0,1) family with concrete parameter values to
establish its local-data dictionary, then invert it for System C.

Fully symbolic reduction in six symbols was intractable.  Instead: evaluate the
family at random EXACT rational parameters, compute the projective normal
potential R(z), and read off
    - the double-pole coefficients at z = 0 and z = 1,
    - the value and 1/z coefficient of R at infinity,
comparing each with a candidate formula in (theta_0, theta_1, theta_inf, t).
Several independent parameter draws must agree, otherwise the formula is wrong.

This is a dictionary check, not a fit: each candidate formula is stated first
and then tested.
"""
import sympy as sp

z = sp.Symbol("z")


def family(pv, qv, tv, t0, t1, ti):
    a = (pv + sp.Rational(1, 2) * (-2 * qv * tv + tv - ti) * (z - qv)
         - sp.Rational(1, 2) * tv * (z - qv) ** 2)
    c = -(z - qv) / (qv - 1)
    b = (-(z * ((pv + sp.Rational(1, 2) * (qv - 1) * qv * tv) ** 2 - t1**2 / 4
                + (qv - 1) * (t0**2 / 4 - t1**2 / 4 - qv * ti**2 / 4))) / qv
         - ((qv - 1)
            * (pv + sp.Rational(1, 2) * ((qv - 1) * qv * tv - t0 + qv * ti))
            * (pv + sp.Rational(1, 2) * ((qv - 1) * qv * tv + t0 + qv * ti))) / qv)
    return sp.cancel(a), sp.cancel(b), sp.cancel(c)


def normal_potential(a, b, c):
    D = z * (z - 1)
    bp, ap, Dp = sp.diff(b, z), sp.diff(a, z), sp.diff(D, z)
    c2 = sp.cancel(D * (-D) * b)
    c1 = sp.cancel(D * ((-Dp - a) * b + D * bp) + a * b * D)
    c0 = sp.cancel(D * (-ap * b + a * bp) + b**2 * c + a**2 * b)
    P = sp.cancel(c1 / c2)
    Q = sp.cancel(c0 / c2)
    return sp.cancel(sp.together(P**2 / 4 + sp.diff(P, z) / 2 - Q))


def local_data(R):
    """double-pole coeffs at 0 and 1; R(inf) and its 1/z coefficient."""
    d0 = sp.cancel(sp.cancel(z**2 * R).subs(z, 0))
    d1 = sp.cancel(sp.cancel((z - 1) ** 2 * R).subs(z, 1))
    w = sp.Symbol("w")
    ser = sp.series(R.subs(z, 1 / w), w, 0, 2).removeO()
    e0 = sp.cancel(ser.subs(w, 0))
    e1 = sp.cancel(sp.diff(sp.expand(ser), w).subs(w, 0))
    return d0, d1, e0, e1


DRAWS = [
    (sp.Rational(2, 3), sp.Rational(5, 7), sp.Rational(3, 2), sp.Rational(1, 5), sp.Rational(4, 3), sp.Rational(2, 7)),
    (sp.Rational(-1, 2), sp.Rational(3, 4), sp.Rational(-5, 3), sp.Rational(7, 2), sp.Rational(-1, 3), sp.Rational(5, 6)),
    (sp.Integer(3), sp.Rational(-2, 5), sp.Rational(1, 4), sp.Rational(-2, 3), sp.Rational(1, 2), sp.Rational(-3, 4)),
]

print("candidate dictionary:")
print("   double-pole coeff at z=0  ==  (theta_0^2 - 1)/4")
print("   double-pole coeff at z=1  ==  (theta_1^2 - 1)/4")
print("   R(infinity)               ==  t^2/4")
print("   1/z coefficient at infty  ==  t*theta_inf/2")
print()

for i, (pv, qv, tv, t0, t1, ti) in enumerate(DRAWS, 1):
    a, b, c = family(pv, qv, tv, t0, t1, ti)
    R = normal_potential(a, b, c)
    d0, d1, e0, e1 = local_data(R)
    print(f"draw {i}: p={pv} q={qv} t={tv} th0={t0} th1={t1} thinf={ti}")
    print(f"   d0 = {d0}   predicted {(t0**2 - 1)/4}   ok={sp.simplify(d0 - (t0**2 - 1)/4) == 0}")
    print(f"   d1 = {d1}   predicted {(t1**2 - 1)/4}   ok={sp.simplify(d1 - (t1**2 - 1)/4) == 0}")
    print(f"   R(inf) = {e0}   predicted {tv**2/4}   ok={sp.simplify(e0 - tv**2/4) == 0}")
    print(f"   1/z coeff = {e1}   predicted {tv*ti/2}   ok={sp.simplify(e1 - tv*ti/2) == 0}")
    print()
