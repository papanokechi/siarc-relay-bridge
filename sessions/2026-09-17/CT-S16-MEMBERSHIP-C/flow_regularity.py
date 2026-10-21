"""CT-S16 - regularity of the PV foliation at System C's point.

vdPS p.2656, read from the page image:

  "the foliation given by the 2-form Omega = dp^dq/(q(q-1)) - dH_V ^ dt on
   U_0 x (C \\ {0}) coincides with the foliation given by isomonodromy."

  (4.4)   dp/dt =  q(q-1) dH_V/dq ,   dq/dt = -q(q-1) dH_V/dp
  (4.5)   H_V(p,q,t) = -p^2/((q-1)q t) - th0^2/(4 q t) + th1^2/(4(q-1)t)
                        + (1/4) q (q t - t + 2 th_inf - 2)

If q(q-1) != 0 and t != 0 at our point, the vector field v = d/dt + v_p d/dp
+ v_q d/dq is regular there, so exactly one leaf passes through it.  That is
what makes the deformation exist; it is not an ansatz.

This is NOT the pre-registered step-3(b) falsifier, which requires monodromy and
Stokes data agreeing to 30 digits.  That falsifier was NOT run; see REPORT.md.
"""
import sympy as sp

p, q, t, th0, th1, thi = sp.symbols("p q t theta_0 theta_1 theta_inf")

H = (-p**2 / ((q - 1) * q * t) - th0**2 / (4 * q * t) + th1**2 / (4 * (q - 1) * t)
     + sp.Rational(1, 4) * q * (q * t - t + 2 * thi - 2))

vp = sp.cancel(q * (q - 1) * sp.diff(H, q))
vq = sp.cancel(-q * (q - 1) * sp.diff(H, p))
print("general flow:")
print("  dq/dt =", sp.simplify(vq))
print("  dp/dt =", sp.factor(sp.simplify(vp)))

SOL = dict(
    p=5 * sp.I * (-28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672,
    q=sp.Rational(1, 2) + (-457937 * sp.sqrt(11) * sp.I + 281700 * sp.sqrt(33) * sp.I) / 122408,
    t=-2 * sp.sqrt(33) * sp.I / 9,
    thi=-2 - sp.sqrt(3) / 9,
)
sub = {p: SOL["p"], q: SOL["q"], t: SOL["t"], thi: SOL["thi"], th0: 0, th1: 0}

qv, tv = SOL["q"], SOL["t"]
print("\nat System C's point (branch t = -2i sqrt(33)/9):")
print("  q       =", complex(sp.N(qv, 30)))
print("  q - 1   =", complex(sp.N(qv - 1, 30)))
print("  q(q-1)  =", complex(sp.N(sp.expand(qv * (qv - 1)), 30)))
print("  t       =", complex(sp.N(tv, 30)))
print("  q(q-1) != 0 :", sp.simplify(qv * (qv - 1)) != 0)
print("  t != 0      :", sp.simplify(tv) != 0)

print("\n  H_V  =", complex(sp.N(sp.simplify(H.subs(sub)), 30)))
print("  dq/dt=", complex(sp.N(sp.simplify(vq.subs(sub)), 30)))
print("  dp/dt=", complex(sp.N(sp.simplify(vp.subs(sub)), 30)))
print("\nall finite -> the isomonodromy vector field is regular at the point,")
print("so exactly one PV leaf passes through it.")
