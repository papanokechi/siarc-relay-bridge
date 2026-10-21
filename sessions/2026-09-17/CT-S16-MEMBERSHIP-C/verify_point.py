"""CT-S16 - independent verification of the located point (p,q,t,theta_inf).

locate_final.py solved an overdetermined system (5 coefficient equations plus
b1 = 0, in 4 unknowns).  Consistency is meaningful only if the solution is then
checked independently, so here the solution is substituted back into a, b, c and
R is rebuilt with the GENERAL formula

    P = D'/D - b'/b,    Q = a'/D - a b'/(D b) - (a^2 + b c)/D^2,
    R = P^2/4 + P'/2 - Q

(not the b-constant closed form used to derive it), then compared with r_z both
symbolically and numerically at dps 60, as P0 requires.

Also checked: q not in {0,1}, i.e. the point lies in vdPS's chart
U_0 = C x (C \\ {0,1}) of the moduli space M_{t,lambda}.
"""
import mpmath as mp
import sympy as sp

z = sp.Symbol("z")
D = z * (z - 1)

SOLS = [
    dict(
        p=5 * sp.I * (-28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672,
        q=sp.Rational(1, 2) + (-457937 * sp.sqrt(11) * sp.I + 281700 * sp.sqrt(33) * sp.I) / 122408,
        t=-2 * sp.sqrt(33) * sp.I / 9,
        thi=-2 - sp.sqrt(3) / 9,
    ),
    dict(
        p=5 * sp.I * (28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672,
        q=sp.Rational(1, 2) + (-281700 * sp.sqrt(33) * sp.I - 457937 * sp.sqrt(11) * sp.I) / 122408,
        t=2 * sp.sqrt(33) * sp.I / 9,
        thi=-2 + sp.sqrt(3) / 9,
    ),
]

# ---- System C's r_z --------------------------------------------------------
x = sp.Symbol("x")
s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
delta = -sp.sqrt(11) * sp.I / 3
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_x = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
r_z = sp.cancel(sp.expand(delta**2 * r_x.subs(x, s_p + delta * z)))


def build(pv, qv, tv, tiv):
    a = (pv + sp.Rational(1, 2) * (-2 * qv * tv + tv - tiv) * (z - qv)
         - sp.Rational(1, 2) * tv * (z - qv) ** 2)
    c = -(z - qv) / (qv - 1)
    U = pv + sp.Rational(1, 2) * (qv - 1) * qv * tv
    V = pv + sp.Rational(1, 2) * ((qv - 1) * qv * tv + qv * tiv)
    b1 = -(U**2 - (qv - 1) * qv * tiv**2 / 4) / qv
    b0 = -(qv - 1) * V**2 / qv
    return a, sp.together(b1 * z + b0), c, b1


for i, s in enumerate(SOLS, 1):
    print(f"\n================ solution {i} ================")
    a, b, c, b1 = build(s["p"], s["q"], s["t"], s["thi"])

    b1s = sp.radsimp(sp.simplify(sp.expand(b1)))
    print("b1 (coefficient of z in b), must be 0 :", b1s)

    # general formula, not the closed form
    P = sp.diff(D, z) / D - sp.diff(b, z) / b
    Q = sp.diff(a, z) / D - a * sp.diff(b, z) / (D * b) - (a**2 + b * c) / D**2
    R = sp.cancel(sp.together(P**2 / 4 + sp.diff(P, z) / 2 - Q))

    diff = sp.simplify(sp.cancel(sp.together(R - r_z)))
    print("R - r_z simplifies to :", diff)

    # numeric check at dps 60 (P0: never rely on symbolic == alone)
    mp.mp.dps = 60
    fR = sp.lambdify(z, R, "mpmath")
    fr = sp.lambdify(z, r_z, "mpmath")
    worst = mp.mpf(0)
    for zv in ["0.37", "1.9", "-2.4", "0.611", "5.25"]:
        zz = mp.mpf(zv)
        d = abs(fR(zz) - fr(zz))
        rel = d / max(abs(fr(zz)), mp.mpf(1))
        worst = max(worst, rel)
    print("worst relative residual over 5 points, dps 60 :", mp.nstr(worst, 6))

    qn = complex(sp.N(s["q"], 30))
    pn = complex(sp.N(s["p"], 30))
    print(f"q = {qn}   |q| = {abs(qn):.6f}")
    print(f"p = {pn}")
    print("q not in {0,1} (vdPS chart U_0 = C x (C\\{0,1})) :",
          sp.simplify(s["q"]) != 0 and sp.simplify(s["q"]) != 1)
    print("t =", s["t"], " theta_inf =", sp.radsimp(s["thi"]))
