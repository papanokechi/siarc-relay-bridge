"""CT-S16 step 2(b) - irreducibility of System C, exactly.

Method (exact, no numerics).  Work with the projective normal form u'' = r u,
r = r_C(x) = (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2).  Reducibility of a rank-2
module over C(x) is equivalent to the existence of a rank-1 submodule, i.e. a
hyperexponential solution u = exp(int w) with w in C(x) satisfying the Riccati
equation w' + w^2 = r.  Ruling out rational w therefore proves irreducibility.

The argument, each step checked below:

 (1) Every pole of w is simple.  If w had a pole of order k >= 2 at c then w^2
     has order 2k and w' has order k+1 < 2k, so r would have a pole of order
     2k >= 4.  r has poles of order exactly 2, so k = 1.
 (2) At a simple pole with residue A, w' + w^2 contributes (A^2 - A)/(x-c)^2.
     At a point where r is regular this forces A^2 - A = 0, so A = 1 (A = 0
     means no pole).  At a double pole of r with coefficient B it forces
     A^2 - A = B.
 (3) w is bounded at infinity: if w ~ d x^m with m >= 1 then r ~ d^2 x^(2m)
     is unbounded, but r is bounded.  So w -> c0 with c0^2 = r(infinity).
 (4) Hence w = c0 + A_+/(x-s_+) + A_-/(x-s_-) + sum_j 1/(x-z_j), and the 1/x
     coefficient of w is A_+ + A_- + n with n = #{z_j} >= 0 an integer.
 (5) Matching the 1/x coefficient of r: r_1 = 2*c0*(A_+ + A_- + n).
     So n = r_1/(2 c0) - A_+ - A_- must be a non-negative integer.

The test is run on System C and on two controls, one reducible by construction
and one irreducible, so that it is shown to separate the two cases.
"""
import sympy as sp

x = sp.Symbol("x")


def riccati_obstruction(r, label):
    print(f"\n=== {label} ===")
    r = sp.cancel(sp.together(r))
    num, den = sp.fraction(r)
    print("  r =", sp.factor(num), "/", sp.factor(den))

    poles = sp.roots(sp.Poly(den, x))
    print("  poles of r (with multiplicity):", {sp.radsimp(k): v for k, v in poles.items()})
    for c, mult in poles.items():
        if mult != 2:
            print(f"  !! pole at {c} has multiplicity {mult} != 2; argument as written does not apply")
            return None

    residues = []
    for c, _ in poles.items():
        B = sp.cancel(sp.cancel((x - c) ** 2 * r).subs(x, c))
        A = sp.symbols("A")
        sols = sp.solve(sp.Eq(A**2 - A, B), A)
        print(f"  at x={sp.radsimp(c)}: double-pole coeff B={sp.radsimp(sp.simplify(B))}"
              f" -> admissible residues {[sp.radsimp(sp.simplify(s)) for s in sols]}")
        residues.append(sols)

    w_ = sp.Symbol("w_", positive=True)
    ser = sp.series(r.subs(x, 1 / w_), w_, 0, 2).removeO()
    c0sq = sp.cancel(sp.expand(ser).subs(w_, 0))
    r1 = sp.cancel(sp.diff(sp.expand(ser), w_).subs(w_, 0))
    print(f"  at infinity: r -> {sp.radsimp(c0sq)} (= c0^2), 1/x coefficient r_1 = {sp.radsimp(r1)}")
    if c0sq == 0:
        print("  !! r vanishes at infinity; argument as written does not apply")
        return None
    c0s = [sp.sqrt(c0sq), -sp.sqrt(c0sq)]

    verdict_possible = False
    import itertools
    for c0 in c0s:
        for combo in itertools.product(*residues):
            n = sp.radsimp(sp.simplify(r1 / (2 * c0) - sum(combo)))
            isint = n.is_integer
            ok = bool(isint) and bool((n >= 0) == True)
            print(f"    c0={sp.radsimp(sp.simplify(c0))}, residues={[sp.radsimp(sp.simplify(v)) for v in combo]}"
                  f"  ->  n = {n}   integer={isint}  admissible={ok}")
            verdict_possible = verdict_possible or ok
    print("  VERDICT:", "reducible NOT excluded" if verdict_possible else "IRREDUCIBLE (no rational Riccati solution)")
    return verdict_possible


# ---- System C -------------------------------------------------------------
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_C = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
riccati_obstruction(r_C, "System C")

# ---- control 1: reducible by construction ---------------------------------
# take w0 rational with simple poles at the same two points (residues 1/2 each,
# forced by the same double-pole coefficient) and a constant term; then
# r = w0' + w0^2 is reducible by construction and the test must NOT exclude it.
s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
s_m = sp.Rational(-1, 6) - sp.sqrt(11) * sp.I / 6
w0 = sp.Rational(1, 2) / (x - s_p) + sp.Rational(1, 2) / (x - s_m) + sp.Rational(1, 3)
r_red = sp.cancel(sp.diff(w0, x) + w0**2)
riccati_obstruction(r_red, "CONTROL (reducible by construction)")

# ---- control 2: known irreducible -----------------------------------------
# a generic perturbation of System C's potential, same pole structure
r_irr = sp.cancel(r_C + sp.Rational(5, 7) / (3 * x**2 + x + 1))
riccati_obstruction(r_irr, "CONTROL (perturbed System C)")
