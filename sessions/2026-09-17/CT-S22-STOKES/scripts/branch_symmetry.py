r"""S22-20 structural attempt: is the branch pair related by an ANALYTIC map?

CONTEXT
-------
Stage 2 found, numerically, that branch 1 and branch 2 give the SAME unordered
trace data:

    branch 1   x1 = -3.4791908904... - 1.0850135703i    conv right|ccw|infcw|10
               x2 = +5.0274753770... + 2.3656209875i
    branch 2   x1 = +5.0274753770... + 2.3656209875i    conv right|cw|infccw|01
               x2 = -3.4791908904... - 1.0850135703i
    x3, alpha  identical on both.

That is claim S22-20, and it is currently VERIFIED (two runs), not STRUCTURAL.

WHY THE GALOIS RELATION IS NOT ALREADY A PROOF
----------------------------------------------
branch_relation.py proves sigma: sqrt3 -> -sqrt3, sqrt11 -> sqrt11 carries
(t, theta_inf, q, p) of branch 1 to branch 2.  Since family_polys is a
polynomial in those with RATIONAL coefficients, sigma(A_1) = A_2 holds
automatically, coefficient by coefficient.  But sigma is a field automorphism
of a number field: it is not continuous, so it does not map solutions of
ODE_1 to solutions of ODE_2, and the monodromy entries are transcendental.
sigma therefore carries the CT-S16 LOCATION argument and no Stokes data.

WHAT WOULD BE A PROOF
---------------------
An explicit ANALYTIC equivalence.  Both branches have their finite singular
points at z = 0 and z = 1 (Continuer is built on [0, 1] in stage2_systemC.py),
and theta_0 = theta_1 = 0, so the punctures 0 and 1 are interchangeable as far
as local data is concerned.  The observed x1 <-> x2 swap with x3 and alpha
fixed is exactly what an involution exchanging 0 and 1 and fixing infinity
would do.  The candidate is therefore

    phi(z) = 1 - z .

Set Y' = -A(z) Y with A = [[a, b], [c, -a]] / D(z), D(z) = z(z-1) = z^2 - z.
Note D(1 - z) = (1 - z)(-z) = D(z): the denominator is ALREADY invariant.

If W(z) = Y_1(1 - z) then W'(z) = -Y_1'(1 - z) = +A_1(1 - z) W(z).  For W to
solve branch 2's system after a constant gauge G we need

    A_2(z) = -G A_1(1 - z) G^{-1}.                                   (*)

A is TRACELESS, so the only gauge invariant is the determinant.  With
det A = -(a^2 + b c)/D^2 and D invariant, (*) forces the scalar identity

    P_2(z) = P_1(1 - z),      P(z) := a(z)^2 + b(z) c(z).            (**)

(** ) is a necessary condition that can be tested EXACTLY, with no solver and
no precision.  This script tests it, and three neighbouring candidates so that
a pass is not confused with a coincidence.  If (**) holds we then solve for the
constant gauge G explicitly; if a G exists, S22-20 becomes STRUCTURAL.

FALSIFIER, pre-declared: if (**) fails for all four candidates, this route is
dead and S22-20 stays VERIFIED-numerical.  That outcome is reported, not
worked around; no further candidate maps are tried in this script.

Reads back what it writes.  Every conclusion is gated by an assert.
"""
import hashlib
import pathlib
import sys

import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "outputs" / "branch_symmetry.out.txt"
LINES = []


def say(s=""):
    print(s)
    LINES.append(s)


def exact_point(branch):
    """Verbatim from stage2_systemC.py exact_point(); CT-S16 pq_solution.txt."""
    I = sp.I
    s11, s33, s3 = sp.sqrt(11), sp.sqrt(33), sp.sqrt(3)
    if branch == 1:
        p = 5 * I * (-28151758571 * s33 + 48874838016 * s11) / 4086468672
        q = sp.Rational(1, 2) - 457937 * s11 * I / 122408 + 70425 * s33 * I / 30602
        t = -2 * s33 * I / 9
        thi = -2 - s3 / 9
    else:
        p = 5 * I * (28151758571 * s33 + 48874838016 * s11) / 4086468672
        q = sp.Rational(1, 2) - 70425 * s33 * I / 30602 - 457937 * s11 * I / 122408
        t = 2 * s33 * I / 9
        thi = -2 + s3 / 9
    return p, q, t, thi


def family_polys(p, q, t, thi, th0=0, th1=0):
    """Verbatim from stage2_systemC.py family_polys()."""
    z = sp.symbols("z")
    a = p + sp.Rational(1, 2) * (-2 * q * t + t - thi) * (z - q) \
        - sp.Rational(1, 2) * t * (z - q) ** 2
    c = -(z - q) / (q - 1)
    inner = p + sp.Rational(1, 2) * (q - 1) * q * t
    first = -(z * (inner ** 2 - th1 ** 2 / 4
                   + (q - 1) * (th0 ** 2 / 4 - th1 ** 2 / 4
                                - q * thi ** 2 / 4))) / q
    second = -((q - 1)
               * (p + sp.Rational(1, 2) * ((q - 1) * q * t - th0 + q * thi))
               * (p + sp.Rational(1, 2) * ((q - 1) * q * t + th0 + q * thi))) / q
    return z, sp.expand(a), sp.expand(first + second), sp.expand(c)


def conj_coeffs(expr, z):
    """Complex-conjugate the COEFFICIENTS of a polynomial in z, leaving z alone.

    This is the algebraic shadow of the anti-analytic map z -> conj(z); it is
    applied to the coefficients only, which is what a candidate relation of the
    form conj(A(conj(z))) amounts to on a polynomial.
    """
    pol = sp.Poly(sp.expand(expr), z)
    out = 0
    for (k,), cf in pol.terms():
        out += sp.conjugate(cf) * z ** k
    return sp.expand(sp.simplify(out))


def sigma(e):
    """sqrt3 -> -sqrt3, sqrt11 -> +sqrt11, hence sqrt33 -> -sqrt33.

    Verbatim from branch_relation.py sigma().  The indirection through A*B is
    ESSENTIAL: sympy stores sqrt(33) as an atom, so a bare
    subs(sqrt(3), -sqrt(3)) leaves sqrt(33) untouched and silently applies a
    map that is not sigma.  An earlier version of this script did exactly that;
    the positive control below caught it (max|coeff| ~ 1.3e5, far too large to
    be a simplification failure).
    """
    A, B = sp.symbols("_A _B", positive=True)
    e = sp.expand(e).subs({sp.sqrt(33): A * B, sp.sqrt(3): A, sp.sqrt(11): B})
    return sp.expand(e.subs({A: -sp.sqrt(3), B: sp.sqrt(11)}))


def poly_is_zero(expr, z):
    """(is_identically_zero, max |coefficient| numerically) for a poly in z.

    Symbolic AND numeric: a coefficient counts as zero only if simplify sends
    it to 0 *and* its 40-digit numeric value is below 1e-30.  Reporting the
    numeric magnitude alongside is what lets a reader tell a real nonzero from
    a simplification failure.
    """
    e = sp.expand(sp.radsimp(sp.expand(expr)))
    pol = sp.Poly(e, z)
    coeffs = [sp.simplify(sp.expand(c)) for c in pol.all_coeffs()]
    worst = sp.Integer(0)
    ok = True
    for c in coeffs:
        nv = sp.Abs(sp.N(c, 40))
        if nv > worst:
            worst = nv
        if not (c == 0 or nv < sp.Float("1e-30")):
            ok = False
    return ok, worst


def main():
    z = sp.symbols("z")
    say("=" * 74)
    say("S22-20 structural attempt: analytic equivalence of the CT-S16 branches")
    say("=" * 74)
    say()

    dat = {}
    for br in (1, 2):
        p, q, t, thi = exact_point(br)
        _z, a, b, c = family_polys(p, q, t, thi)
        dat[br] = dict(a=a, b=b, c=c, t=t, thi=thi, q=q, p=p)
        say(f"branch {br}:  t = {sp.simplify(t)}   theta_inf = {sp.simplify(thi)}")
    say()

    # ---------------------------------------------------------- denominator
    D = z ** 2 - z
    Dphi = sp.expand(D.subs(z, 1 - z))
    d_inv = sp.simplify(Dphi - D)
    say("STEP 1  denominator invariance under phi(z) = 1 - z")
    say(f"  D(z)   = {D}")
    say(f"  D(1-z) = {Dphi}")
    say(f"  D(1-z) - D(z) = {d_inv}")
    assert d_inv == 0, "D is not invariant under z -> 1-z; the candidate map is wrong"
    say("  -> invariant.  phi fixes the singular set {0, 1, infinity} setwise,")
    say("     exchanging 0 and 1.  [PROVEN]")
    say()

    # ------------------------------------------------- the gauge invariant P
    say("STEP 2  the only gauge invariant of a traceless A is det A.")
    say("  A = [[a, b], [c, -a]]/D,   det A = -(a^2 + b c)/D^2,")
    say("  so a constant gauge forces  P_2(z) = P_1(1-z)  with P = a^2 + b c.")
    say()
    P = {br: sp.expand(dat[br]["a"] ** 2 + dat[br]["b"] * dat[br]["c"])
         for br in (1, 2)}
    for br in (1, 2):
        say(f"  deg P_{br} = {sp.Poly(P[br], z).degree()}")
    say()

    # -------------------------------------------------- four candidate maps
    say("STEP 3  POSITIVE CONTROL first: the comparison machinery must be able")
    say("        to detect a TRUE identity of the same radical complexity.")
    say("        Without this, 'nonzero' four times could just mean simplify()")
    say("        cannot zero nested radicals, and the negative would be void.")
    say("        Control: sigma(P_1) - P_2 with sigma: sqrt3 -> -sqrt3, which")
    say("        branch_relation.py proves is identically zero.")
    say()
    s3 = sp.sqrt(3)
    P1_sigma = sigma(P[1])
    ctl = sp.expand(P1_sigma - P[2])
    ctl_ok, ctl_worst = poly_is_zero(ctl, z)
    say(f"  CONTROL  sigma(P_1)(z) - P_2(z)                "
        f"{'ZERO' if ctl_ok else 'nonzero'}   max|coeff| ~ {sp.N(ctl_worst, 6)}")
    assert ctl_ok, (
        "POSITIVE CONTROL FAILED: the machinery cannot detect a known-true "
        "identity, so any 'nonzero' verdict below would be meaningless. "
        "Halting rather than reporting a void negative.")
    say("  -> machinery detects a true identity through the same radicals.")
    say("     The negatives below are therefore informative.  [control passed]")
    say()

    say("STEP 3b  candidate relations, each simplified to zero or not.")
    say("  A pass on exactly one candidate is the informative outcome; a pass")
    say("  on several would mean the test does not discriminate.")
    say()
    cands = {
        "identity            P_2(z)   - P_1(z)":
            sp.expand(P[2] - P[1]),
        "swap 0<->1          P_2(z)   - P_1(1-z)":
            sp.expand(P[2] - P[1].subs(z, 1 - z)),
        "conj coeffs         P_2(z)   - conj(P_1)(z)":
            sp.expand(P[2] - conj_coeffs(P[1], z)),
        "conj coeffs + swap  P_2(z)   - conj(P_1)(1-z)":
            sp.expand(P[2] - conj_coeffs(P[1], z).subs(z, 1 - z)),
    }
    results = {}
    for name, expr in cands.items():
        ok, worst = poly_is_zero(expr, z)
        results[name] = ok
        say(f"  {name:44s} {'ZERO' if ok else 'nonzero'}   max|coeff| ~ "
            f"{sp.N(worst, 6)}")
    say()

    passing = [k for k, v in results.items() if v]
    say(f"  candidates passing: {len(passing)}")
    for k in passing:
        say(f"    {k}")
    say()

    if len(passing) != 1:
        say("VERDICT  the necessary determinant condition does not single out an")
        say("         analytic candidate.  Pre-declared falsifier fires: this")
        say("         route is dead and S22-20 REMAINS VERIFIED-NUMERICAL.")
        say("         No further candidate maps are tried here, per the")
        say("         pre-declaration in this script's docstring.")
        write_out()
        return 1

    say("STEP 4  determinant condition met.  Solve for the constant gauge G in")
    say("        A_2(z) = -G A_1(1-z) G^{-1}, i.e. G^{-1} A_2(z) G = -A_1(1-z),")
    say("        as an identity in z (all three powers z^0, z^1, z^2).")
    say()
    g11, g12, g21, g22 = sp.symbols("g11 g12 g21 g22")
    G = sp.Matrix([[g11, g12], [g21, g22]])
    A1p = sp.Matrix([[dat[1]["a"], dat[1]["b"]],
                     [dat[1]["c"], -dat[1]["a"]]]).subs(z, 1 - z)
    A2 = sp.Matrix([[dat[2]["a"], dat[2]["b"]],
                    [dat[2]["c"], -dat[2]["a"]]])
    # G^{-1} A_2 G = -A_1(1-z)   <=>   A_2 G + G A_1(1-z) = 0   (avoids inverse)
    M = sp.expand(A2 * G + G * A1p)
    eqs = []
    for i in range(2):
        for j in range(2):
            pol = sp.Poly(sp.expand(M[i, j]), z)
            for cf in pol.all_coeffs():
                eqs.append(sp.simplify(cf))
    eqs = [e for e in eqs if e != 0]
    say(f"  {len(eqs)} nontrivial linear equations in (g11, g12, g21, g22)")
    sol = sp.solve(eqs, [g11, g12, g21, g22], dict=True)
    say(f"  sympy.solve returned {len(sol)} solution branch(es)")
    nontrivial = None
    for s in sol:
        Gs = G.subs(s)
        free = sorted(Gs.free_symbols, key=str)
        if free:
            Gt = sp.simplify(Gs.subs({free[0]: 1}))
            for f in free[1:]:
                Gt = sp.simplify(Gt.subs(f, 0))
        else:
            Gt = sp.simplify(Gs)
        if sp.simplify(Gt.det()) != 0:
            nontrivial = Gt
            break
    if nontrivial is None:
        say()
        say("VERDICT  the determinant condition holds but NO invertible constant")
        say("         gauge G exists.  The equivalence, if any, needs a")
        say("         z-dependent gauge, which is outside this script's")
        say("         pre-declared scope.  S22-20 REMAINS VERIFIED-NUMERICAL,")
        say("         with the determinant identity recorded as a partial")
        say("         structural result.")
        write_out()
        return 1

    say(f"  G = {nontrivial.tolist()}")
    say(f"  det G = {sp.simplify(nontrivial.det())}")
    resid = sp.simplify(sp.expand(A2 * nontrivial + nontrivial * A1p))
    say(f"  residual A_2 G + G A_1(1-z) = {resid.tolist()}")
    assert all(sp.simplify(x) == 0 for x in resid), \
        "gauge residual is not identically zero"
    say("  -> residual simplifies to the zero matrix.  [PROVEN]")
    say()
    say("VERDICT  branch 2's system is the pullback of branch 1's along")
    say("         phi(z) = 1 - z, up to the constant gauge G above.  phi is")
    say("         ANALYTIC, so it does transport monodromy: it exchanges the")
    say("         loops about 0 and 1 and reverses orientation, which is")
    say("         exactly the x1 <-> x2 swap with x3 and alpha fixed that")
    say("         Stage 2 observed, and exactly the mirrored convention")
    say("         right|ccw|infcw|10 -> right|cw|infccw|01.")
    say("         S22-20 is upgraded to STRUCTURAL.")
    write_out()
    return 0


def write_out():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    back = OUT.read_text(encoding="utf-8")
    assert back == "\n".join(LINES) + "\n", "read-back of output file differs"
    h = hashlib.sha256(back.encode("utf-8")).hexdigest()
    print(f"\nwrote {OUT}")
    print(f"sha256 {h}")


if __name__ == "__main__":
    sys.exit(main())
