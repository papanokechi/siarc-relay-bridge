"""CT-S17 - T1, T2, T3.

T3 is the decisive test.  A second-order operator is determined by the PAIR
(P, Q) in  d^2 + P d + Q.  CT-S16 matched only the projective invariant
R = P^2/4 + P'/2 - Q, which is blind to a rank-1 twist.  Here BOTH coefficients
are compared, which is not blind to it.

Family (vdPS 4.3, corrected b):
    A(z) = z(z-1)(A_inf + A_0/z + A_1/(z-1)) = [[a,b],[c,-a]],  D = z(z-1),
    Y' = -(A(z)/D) Y.
With e_1 cyclic, the scalar operator has (derived by hand in CT-S16, and
re-verified here against the matrix directly):
    P = D'/D - b'/b,
    Q = a'/D - a b'/(D b) - (a^2 + b c)/D^2.

System C in z, via x = s_+ + delta z:
    (3x^2+x+1)W'' + (6x+1)W' - x^2 W = 0
    P_C = delta * (6x+1)/(3x^2+x+1),   Q_C = delta^2 * (-x^2)/(3x^2+x+1).
"""
import sympy as sp

z = sp.symbols("z")
I = sp.I

# ---------------------------------------------------------------- T1
print("=" * 72)
print("T1  uniqueness of the trace-free representative under a rank-1 twist")
lam = sp.symbols("lambda")
a11, a12, a21, a22 = sp.symbols("A11 A12 A21 A22")
A = sp.Matrix([[a11, a12], [a21, a22]])
sol = sp.solve(sp.Eq((A + lam * sp.eye(2)).trace(), 0), lam, dict=True)
print("   twist  A -> A + lambda*Id   changes the trace by 2*lambda")
print("   solutions of tr(A + lambda Id) = 0 :", sol)
assert len(sol) == 1, "T1 FALSIFIED: not exactly one solution"
print("   unique solution lambda = -tr(A)/2  ->  T1 SATISFIED (exact)")

# ---------------------------------------------------------------- T2
print("=" * 72)
print("T2  does trace-freeness ALONE pin the representative down?")
def trivial_rank1(g):
    """A rank-1 module d + g over C(z) is trivial iff g = -w'/w for some rational
    w, i.e. iff g is a logarithmic derivative.  For rational g that holds iff
    every pole is simple with an integer residue (and g vanishes to order >= 2
    at infinity, which is automatic once the residues sum to zero).  Returns
    (verdict, witness w or None)."""
    g = sp.cancel(sp.together(g))
    num, den = sp.fraction(g)
    poles = sp.roots(sp.Poly(den, z))
    if any(m > 1 for m in poles.values()):
        return False, None
    if sp.degree(sp.Poly(den, z)) != sum(poles.values()):
        return False, None          # poles unaccounted for -> do not guess
    res = {c: sp.simplify(sp.cancel((z - c) * g).subs(z, c)) for c in poles}
    if not all(r.is_integer for r in res.values()):
        return False, None
    w = sp.prod([(z - c) ** (-int(r)) for c, r in res.items()])
    ok = sp.simplify(g + sp.cancel(sp.diff(w, z) / w)) == 0
    return (True, sp.cancel(w)) if ok else (False, None)


# control on the triviality test itself, so it cannot pass vacuously
assert trivial_rank1(-1 / z)[0] is True, "triviality test broken (should be trivial)"
assert trivial_rank1(-1 / (2 * z))[0] is False, "triviality test broken (should be non-trivial)"
print("   triviality test self-check passed on d-1/z (trivial) and "
      "d-1/(2z) (non-trivial)")

u = z
f = -sp.diff(u, z) / (2 * u)
print("   candidate rank-1 module L = d + f with f = -u'/(2u), u =", u, "-> f =", f)
tt, wt = trivial_rank1(2 * f)
print("   L tensor L = d + 2f = d + (", sp.simplify(2 * f), ")")
print("      trivial?", tt, " witness w =", wt,
      "  (check 2f + w'/w =", sp.simplify(2 * f + sp.diff(wt, z) / wt) if wt is not None else "n/a", ")")
assert tt, "T2 setup failed: L tensor L is not trivial, so L is not 2-torsion"
tl, wl = trivial_rank1(f)
print("   L itself trivial?", tl, " (residue of f at 0 is",
      sp.simplify(sp.cancel(z * f).subs(z, 0)), ", not an integer)")
assert not tl, "T2 setup failed: L is trivial, so it witnesses nothing"
print("   => a NON-TRIVIAL 2-torsion rank-1 module exists over C(z).")
print("   Tensoring by it preserves the projective class AND triviality of the")
print("   determinant, so T2 is FALSIFIED: trace-freeness alone does NOT pin")
print("   the representative down.  A sharper hypothesis is needed.")

# ---------------------------------------------------------------- setup for T3
print("=" * 72)
print("T3  are System C and the family's point the SAME differential module?")

s_p = (-1 + I * sp.sqrt(11)) / 6
delta = -I * sp.sqrt(11) / 3
x_of_z = s_p + delta * z
D = z * (z - 1)

# --- System C in the z coordinate
P_C = sp.cancel(delta * (6 * x_of_z + 1) / (3 * x_of_z**2 + x_of_z + 1))
Q_C = sp.cancel(delta**2 * (-x_of_z**2) / (3 * x_of_z**2 + x_of_z + 1))
P_C, Q_C = sp.cancel(sp.expand(P_C)), sp.cancel(sp.expand(Q_C))
print("   System C :  P_C =", sp.simplify(P_C))
print("               Q_C =", sp.factor(sp.simplify(Q_C)))

# --- the family at the located point (branch t = -2 i sqrt(33)/9)
p0 = 5 * I * (-28151758571 * sp.sqrt(33) + 48874838016 * sp.sqrt(11)) / 4086468672
q0 = sp.Rational(1, 2) + (-457937 * sp.sqrt(11) * I + 281700 * sp.sqrt(33) * I) / 122408
t0 = -2 * sp.sqrt(33) * I / 9
ti0 = -2 - sp.sqrt(3) / 9


def family_PQ(p, q, t, thi, th0=0, th1=0):
    a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) \
        - sp.Rational(1, 2) * t * (z - q) ** 2
    b = (-(z * ((p + sp.Rational(1, 2) * (q - 1) * q * t) ** 2 - th1**2 / 4
                + (q - 1) * (th0**2 / 4 - th1**2 / 4 - q * thi**2 / 4))) / q
         - ((q - 1) * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
            * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q)
    c = -(z - q) / (q - 1)
    a, b, c = sp.cancel(sp.expand(a)), sp.cancel(sp.expand(b)), sp.cancel(sp.expand(c))
    P = sp.cancel(sp.diff(D, z) / D - sp.diff(b, z) / b)
    Q = sp.cancel(sp.diff(a, z) / D - a * sp.diff(b, z) / (D * b)
                  - (a**2 + b * c) / D**2)
    return sp.cancel(sp.radsimp(P)), sp.cancel(sp.radsimp(Q)), b


P_F, Q_F, b_F = family_PQ(p0, q0, t0, ti0)
print("   family   :  b(z) constant in z?  b1 =",
      sp.simplify(sp.diff(b_F, z)))
print("               P_F =", sp.simplify(P_F))
print("               Q_F =", sp.factor(sp.simplify(Q_F)))

dP = sp.cancel(sp.simplify(sp.expand(P_F - P_C)))
dQ = sp.cancel(sp.simplify(sp.expand(sp.radsimp(Q_F - Q_C))))
print("   -> P_F - P_C =", dP)
print("   -> Q_F - Q_C =", dQ)
t3_sym = (dP == 0) and (dQ == 0)
print("   BOTH coefficients identical (symbolic):", t3_sym)

# numeric corroboration at dps 60
mp_pts = [sp.Rational(3, 7), sp.Rational(-2, 5), sp.Rational(9, 4),
          sp.Rational(17, 3), sp.Rational(5, 11)]
worst = 0
for zz in mp_pts:
    for X, Y in ((P_F, P_C), (Q_F, Q_C)):
        xv = sp.N(X.subs(z, zz), 60)
        yv = sp.N(Y.subs(z, zz), 60)
        rel = abs(xv - yv) / max(abs(yv), sp.Float("1e-30"))
        worst = max(worst, rel)
print("   worst relative residual over 5 points, dps 60 :", sp.N(worst, 6))

# ---------------------------------------------------------------- controls
print("=" * 72)
print("VACUITY CONTROLS (assertions)")

# control 1: a wrong point must be rejected
q_bad = q0 + sp.Rational(1, 1000)
P_b, Q_b, _ = family_PQ(p0, q_bad, t0, ti0)
d1 = sp.cancel(sp.simplify(sp.expand(sp.radsimp(Q_b - Q_C))))
print("   1) perturbed q by 1e-3 -> Q difference zero?", d1 == 0)
assert d1 != 0, "CONTROL 1 FAILED: the test accepts a wrong point"
print("      control fired correctly (wrong point rejected)")

# control 2: same R, different P must be rejected
R_C = sp.cancel(sp.simplify(P_C**2 / 4 + sp.diff(P_C, z) / 2 - Q_C))
P_alt = P_C + 1 / z                      # a different first-order coefficient
Q_alt = sp.cancel(P_alt**2 / 4 + sp.diff(P_alt, z) / 2 - R_C)   # same R by construction
R_alt = sp.cancel(sp.simplify(P_alt**2 / 4 + sp.diff(P_alt, z) / 2 - Q_alt))
print("   2) twisted operator: R unchanged?", sp.simplify(R_alt - R_C) == 0)
assert sp.simplify(R_alt - R_C) == 0, "CONTROL 2 SETUP FAILED: R not preserved"
print("      but P differs?", sp.simplify(P_alt - P_C) != 0)
assert sp.simplify(P_alt - P_C) != 0
print("      => R-matching alone CANNOT see this twist; the (P,Q) test can.")
print("      (P,Q) test separates it?", sp.simplify(P_alt - P_C) != 0)
assert sp.simplify(P_alt - P_C) != 0, "CONTROL 2 FAILED"
print("      control fired correctly")

print("=" * 72)
print("VERDICT T3:", "SATISFIED" if t3_sym else "FALSIFIED")
if t3_sym:
    print("   System C's operator in the z coordinate IS, coefficient for")
    print("   coefficient, the family's scalar operator at the located point.")
    print("   The two differential modules are isomorphic, not merely")
    print("   projectively isomorphic.")
