"""CT-S16 - check the printed b(z) of vdPS p.2655 against its own constraints.

Read from the page image at 7x magnification:

  a(z) = p + (1/2)(-2qt + t - th_inf)(z-q) - (1/2) t (z-q)^2
  b(z) = -[ z( (p + (1/2)(q-1)q)^2 - th1^2/4
              + (q-1)(th0^2/4 - th1^2/4 - q*th_inf^2/4) ) ] / q
         -[ (q-1)(p + (1/2)((q-1)q t - th0 + q th_inf))
                 (p + (1/2)((q-1)q t + th0 + q th_inf)) ] / q
  c(z) = -(z-q)/(q-1)

The first term of b(z) prints `(p + 1/2 (q-1)q)^2` with NO t, while the second
prints `(q-1)q t`.  The paper's own constraints are

  A_0 = -A(0),  A_1 = A(1),  det A_0 = -th0^2/4,  det A_1 = -th1^2/4,
  th_inf = (A_0 + A_1)_{11},      det A(z) = -a(z)^2 - b(z) c(z).

det A(0) is independent of the disputed term, so the test is det A(1).
Both readings are tried; neither is assumed.
"""
import sympy as sp

z, p, q, t, th0, th1, thi = sp.symbols("z p q t theta_0 theta_1 theta_inf")

a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) - sp.Rational(1, 2) * t * (z - q) ** 2
c = -(z - q) / (q - 1)

second = -((q - 1)
           * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
           * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q


def make_b(inner):
    first = -(z * (inner ** 2 - th1**2 / 4
                   + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
    return first + second


READINGS = {
    "as printed:  (p + 1/2 (q-1)q)^2 ": p + sp.Rational(1, 2) * (q - 1) * q,
    "with a t:    (p + 1/2 (q-1)q t)^2": p + sp.Rational(1, 2) * (q - 1) * q * t,
}

for name, inner in READINGS.items():
    b = make_b(inner)
    detA = -a**2 - b * c
    d0 = sp.simplify(detA.subs(z, 0) + th0**2 / 4)
    d1 = sp.simplify(detA.subs(z, 1) + th1**2 / 4)
    A0 = -sp.Matrix([[a, b], [c, -a]]).subs(z, 0)
    A1 = sp.Matrix([[a, b], [c, -a]]).subs(z, 1)
    dth = sp.simplify((A0 + A1)[0, 0] - thi)
    print(f"\n=== {name} ===")
    print("  det A(0) + th0^2/4  ->", d0)
    print("  det A(1) + th1^2/4  ->", d1)
    print("  (A_0+A_1)_11 - th_inf ->", sp.simplify(sp.expand(dth)))
