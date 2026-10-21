"""CT-S16 step 2(b), corrected - irreducibility of System C, exactly.

The first version (irreducibility.py) was VOID: it extracted the double-pole
coefficient with sp.cancel(...).subs(x, c), which returns nan for algebraic c.
The admissible-residue list was then empty, the product over it was empty, and
the verdict "irreducible" was reached without any test being performed.  The
reducible-by-construction control caught it.

Here the Laurent coefficient is extracted by substituting x = c + y and reading
polynomial coefficients, and the controls are ASSERTIONS: if a control that is
reducible by construction is reported irreducible, the script aborts.

Argument (unchanged, see irreducibility.py docstring for the derivation):
w in C(x) with w' + w^2 = r must have only simple poles, residue 1 at poles
where r is regular, residue A with A^2 - A = B at a double pole of coefficient
B, and w -> c0 with c0^2 = r(infinity).  Matching the 1/x coefficient gives
    n = r_1/(2 c0) - sum(residues at the double poles)
which must be a non-negative integer.  No admissible n  =>  irreducible.
"""
import itertools
import sympy as sp

x, y = sp.symbols("x y")


def laurent_double_pole_coeff(r, c):
    """Coefficient of (x-c)^-2, extracted by polynomial algebra (not subs)."""
    e = sp.cancel(sp.together(r.subs(x, c + y)))
    num, den = sp.fraction(e)
    pn = sp.Poly(sp.expand(num), y)
    pd = sp.Poly(sp.expand(den), y)
    # den has a zero of order exactly 2 at y = 0
    dc = pd.all_coeffs()[::-1]          # ascending powers
    assert sp.simplify(dc[0]) == 0 and sp.simplify(dc[1]) == 0, "den not a double zero"
    d2 = sp.simplify(dc[2])
    n0 = sp.simplify(pn.all_coeffs()[::-1][0])
    return sp.radsimp(sp.simplify(n0 / d2))


def riccati_obstruction(r, label, verbose=True):
    r = sp.cancel(sp.together(r))
    num, den = sp.fraction(r)
    if verbose:
        print(f"\n=== {label} ===")
        print("  r =", sp.factor(num), "/", sp.factor(den))

    poles = sp.roots(sp.Poly(den, x))
    for c, mult in poles.items():
        assert mult == 2, f"pole at {c} has multiplicity {mult}"

    residue_options = []
    for c, _ in poles.items():
        B = laurent_double_pole_coeff(r, c)
        A = sp.Symbol("A")
        sols = [sp.radsimp(sp.simplify(s)) for s in sp.solve(sp.Eq(A**2 - A, B), A)]
        assert sols, f"no admissible residue at {c} - extraction failed"
        if verbose:
            print(f"  at x={sp.radsimp(c)}: B={B} -> admissible residues {sols}")
        residue_options.append(sols)

    wv = sp.Symbol("wv", positive=True)
    ser = sp.expand(sp.series(r.subs(x, 1 / wv), wv, 0, 2).removeO())
    c0sq = sp.cancel(ser.subs(wv, 0))
    r1 = sp.cancel(sp.diff(ser, wv).subs(wv, 0))
    assert c0sq != 0, "r vanishes at infinity; argument does not apply"
    if verbose:
        print(f"  at infinity: c0^2 = {sp.radsimp(c0sq)}, r_1 = {sp.radsimp(r1)}")

    possible = False
    for c0 in (sp.sqrt(c0sq), -sp.sqrt(c0sq)):
        for combo in itertools.product(*residue_options):
            n = sp.radsimp(sp.simplify(r1 / (2 * c0) - sum(combo)))
            ok = bool(n.is_integer) and bool(n.is_nonnegative)
            if verbose:
                print(f"    c0={sp.radsimp(sp.simplify(c0))}, residues={list(combo)}"
                      f"  ->  n = {n}  integer={n.is_integer}  admissible={ok}")
            possible = possible or ok
    verdict = "reducible NOT excluded" if possible else "IRREDUCIBLE"
    if verbose:
        print("  VERDICT:", verdict)
    return possible


s_p = sp.Rational(-1, 6) + sp.sqrt(11) * sp.I / 6
s_m = sp.Rational(-1, 6) - sp.sqrt(11) * sp.I / 6

# ---- vacuity controls, run FIRST and asserted ------------------------------
print("#### vacuity pre-check (PREREG step 2, H-b) ####")

w0 = sp.Rational(1, 2) / (x - s_p) + sp.Rational(1, 2) / (x - s_m) + sp.Rational(1, 3)
r_red0 = sp.cancel(sp.diff(w0, x) + w0**2)
res0 = riccati_obstruction(r_red0, "CONTROL A: reducible by construction, n = 0")
assert res0, "VACUITY FAILURE: a reducible control was reported irreducible"

w1cand = None
# Build the n = 1 control entirely over Q so that cancellation is reliable:
# double poles at x = 0 and x = 1, extra simple pole of w at x = 2 placed at a
# zero of the rest of w, so that r stays regular there.
h = sp.Rational(1, 2) / x + sp.Rational(1, 2) / (x - 1) + sp.Rational(-3, 4)
assert sp.simplify(h.subs(x, 2)) == 0, "control B: extra pole not at a zero of h"
w1try = h + 1 / (x - 2)
r_try = sp.cancel(sp.together(sp.diff(w1try, x) + w1try**2))
den_try = sp.fraction(r_try)[1]
mults = sp.roots(sp.Poly(den_try, x))
assert mults and sum(mults.values()) == sp.Poly(den_try, x).degree(), \
    "control B: sp.roots did not account for the whole denominator"
assert all(m == 2 for m in mults.values()), f"control B: pole multiplicities {mults}"
print(f"\n(control B: double poles at {sorted(mults, key=str)}, extra pole of w at x=2)")
res1 = riccati_obstruction(r_try, "CONTROL B: reducible by construction, n = 1")
assert res1, "VACUITY FAILURE: a reducible control was reported irreducible"

print("\nvacuity pre-check PASSED: the test returns 'reducible NOT excluded'")
print("for both reducible controls, so a negative verdict is informative.")

# ---- the object ------------------------------------------------------------
print("\n\n#### System C ####")
A_c, C_c = 3 * x**2 + x + 1, -x**2
pc, qc = sp.diff(A_c, x) / A_c, C_c / A_c
r_C = sp.cancel(pc**2 / 4 + sp.diff(pc, x) / 2 - qc)
resC = riccati_obstruction(r_C, "System C")
print("\nSystem C is", "REDUCIBLE (not excluded)" if resC else "IRREDUCIBLE")
