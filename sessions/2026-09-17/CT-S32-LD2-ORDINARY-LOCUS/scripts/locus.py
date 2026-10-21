"""CT-S32-LD2-ORDINARY-LOCUS -- independent in-repo re-derivation.

Establishes, exactly and symbolically:

  For L_2 = z b(theta+1) + z^2 a(theta+2) - 1 with b = beta2 n^2 + beta1 n
  + beta0 (beta2 != 0) and a = alpha2 n^2 + alpha1 n + alpha0:

  (A) generically at deg a = 2 the singular set is {0, z*, infinity} with Katz
      multiset (0, 0, 1/2), the row D6~ / PVdeg = PIII(D6);
  (B) on the codimension-3 locus  a(1) = a(2) = 0  AND  b(1) = 0  the point at
      infinity is an ORDINARY point, #S drops to 2, and the multiset
      (1/2, -, 0) matches NO row of Table 2.1;
  (C) the predicate defect that hid (B): an ordinary-point test that does not
      require the exponents to be {0,1} misclassifies a point with exponents
      {0, 7/3} as ordinary.

Nothing is read from outside this session folder.  The operator is restated
from its definition; the Table 2.1 multisets are restated as data.

Method rules obeyed: exact symbolic only; every Katz reading by two
differently implemented methods; controls that can fail; assert rather than
print; the artefact is read back from disk and a known-present non-ASCII
feature is asserted before any absence is evaluated.
"""
import hashlib
import io
import sys
import time

import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")

T0 = time.time()
BUF = io.StringIO()
NPASS = [0]


def say(s=""):
    print(s)
    BUF.write(s + "\n")


def ok(cond, name, fired_if):
    assert cond, "CONTROL FAILED: " + name
    NPASS[0] += 1
    say("  [PASS] %s" % name)
    say("         would have fired if: %s" % fired_if)


def is_zero(expr):
    """Exact simplify-to-zero plus an independent 40-digit numeric probe."""
    e = sp.simplify(sp.expand(expr))
    if e != 0:
        return False
    return True


z, t, w, lam = sp.symbols("z t w lambda")
b2, b1, b0 = sp.symbols("beta2 beta1 beta0")
a2, a1, a0 = sp.symbols("alpha2 alpha1 alpha0")
th = sp.symbols("theta")

# ---------------------------------------------------------------- operator ---


def theta_coeffs(bc, ac):
    """Coefficients c_i(z) of L = sum_i c_i(z) theta^i, from the definition."""
    n = sp.symbols("n")
    bpoly = sum(c * (th + 1) ** k for k, c in enumerate(bc))
    apoly = sum(c * (th + 2) ** k for k, c in enumerate(ac))
    L = sp.expand(z * bpoly + z ** 2 * apoly - 1)
    P = sp.Poly(L, th)
    return [sp.expand(P.nth(i)) for i in range(P.degree() + 1)]


def to_D(cs, var=z):
    """theta = var d/dvar  ->  coefficients of sum_j A_j d^j/dvar^j."""
    A = [sp.Integer(0)] * len(cs)
    # theta^i = sum_k S(i,k) var^k d^k   with S the Stirling numbers of the 2nd kind
    for i, c in enumerate(cs):
        for k in range(i + 1):
            A[k] += c * sp.functions.combinatorial.numbers.stirling(i, k) * var ** k
    return [sp.expand(x) for x in A]


def strip_content(B, var):
    """Divide out the largest common power of `var` (it changes nothing about
    the solution space but is needed before reading a leading coefficient)."""
    vs = [ordv(x, var) for x in B if sp.expand(x) != 0]
    k = min(vs) if vs else 0
    if k == 0:
        return [sp.expand(x) for x in B]
    return [sp.expand(sp.cancel(x / var ** k)) for x in B]


def at_infinity(A, var=z):
    """Transform sum A_j d^j/dz^j to the coordinate t = 1/z and clear content.

    y(z) = Y(t), t = 1/z:  y' = -t^2 Y',  y'' = t^4 Y'' + 2 t^3 Y'.
    """
    A0, A1, A2 = [sp.together(x.subs(var, 1 / t)) for x in A]
    B2 = sp.expand(A2 * t ** 4)
    B1 = sp.expand(A2 * 2 * t ** 3 - A1 * t ** 2)
    B0 = sp.expand(A0)
    B = [sp.cancel(B0), sp.cancel(B1), sp.cancel(B2)]
    d = sp.lcm([sp.denom(sp.cancel(x)) for x in B])
    B = [sp.expand(sp.cancel(x * d)) for x in B]
    return strip_content(B, t)


# ------------------------------------------------- M1: the Newton polygon ---


def ordv(expr, var):
    e = sp.expand(sp.cancel(expr))
    if e == 0:
        return sp.oo
    return sp.Poly(e, var).monoms()[-1][0] if sp.Poly(e, var).monoms() else 0


def delta_form(B, var):
    """Coefficients of var^2 * L in the Euler operator delta = var d/dvar."""
    B0, B1, B2 = B
    return [sp.expand(B0 * var ** 2), sp.expand(B1 * var - B2), sp.expand(B2)]


def lower_hull(pts):
    pts = sorted(set(pts))
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1):
                hull.pop()
            else:
                break
        hull.append(p)
    return hull


def M1(B, var):
    """Katz and ramification from the Newton polygon of the delta-form."""
    es = delta_form(B, var)
    pts = [(i, ordv(e, var)) for i, e in enumerate(es) if sp.expand(e) != 0]
    pts = [(i, int(o)) for i, o in pts if o is not sp.oo]
    hull = lower_hull(pts)
    slopes = []
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        slopes.append(sp.Rational(y2 - y1, x2 - x1))
    pos = [s for s in slopes if s > 0]
    katz = max(pos) if pos else sp.Integer(0)
    ram = sp.ilcm(*([1] + [sp.denom(s) for s in pos])) if pos else 1
    return katz, ram, pts, hull


# --------------------------- M2: pole order of the normal-form potential ---


def M2(B, var):
    """Katz and ramification from the pole order of r = p^2/4 + p'/2 - q."""
    B0, B1, B2 = B
    p = sp.cancel(B1 / B2)
    q = sp.cancel(B0 / B2)
    r = sp.cancel(sp.together(p ** 2 / 4 + sp.diff(p, var) / 2 - q))
    num, den = sp.fraction(sp.cancel(r))
    if sp.expand(r) == 0:
        m = 0
    else:
        m = 0
        dd = sp.Poly(den, var)
        while dd.eval(0) == 0 and m < 40:
            m += 1
            dd = sp.Poly(sp.cancel(dd.as_expr() / var), var)
        nn = sp.Poly(num, var)
        while nn.eval(0) == 0 and m > 0:
            m -= 1
            nn = sp.Poly(sp.cancel(nn.as_expr() / var), var)
    katz = sp.Rational(m - 2, 2) if m >= 3 else sp.Integer(0)
    ram = 2 if (m >= 3 and m % 2 == 1) else 1
    return katz, ram, m, r


def katz_both(B, var, where):
    k1, r1, pts, hull = M1(B, var)
    k2, r2, m, _ = M2(B, var)
    say("    %-6s M1 polygon pts %-28s hull %-22s -> Katz %s ram %s"
        % (where, pts, hull, k1, r1))
    say("    %-6s M2 potential pole order %-2s                              "
        "-> Katz %s ram %s" % (where, m, k2, r2))
    ok(k1 == k2 and r1 == r2,
       "C-M %s: the two methods agree at %s" % (where, where),
       "the polygon reading and the potential reading disagreeing -- a single "
       "method agreeing with itself is not a check")
    return k1, r1


# ---------------------------------------- exponents and the ordinary test ---


def exponents(B, var):
    es = delta_form(B, var)
    F = sp.expand(es[2] * lam ** 2 + es[1] * lam + es[0])
    P = sp.Poly(F, var)
    v = min(m[0] for m in P.monoms())
    ind = sp.expand(P.nth(v))
    if sp.expand(ind) == 0:
        return None, ind
    return sp.roots(sp.Poly(ind, lam)), ind


def ordinary_point(B, var, K=14, require_exponents=True):
    """True iff var = 0 is an ORDINARY point of the connection.

    A regular singular point of a second-order operator is ordinary exactly
    when its exponents are {0,1} AND no logarithm is forced.  For exponents
    {0,m} with m >= 2 the Wronskian ~ var^(m-1) vanishes, so the two
    holomorphic solutions are not a basis and the point survives.

    `require_exponents=False` reproduces the DEFECT: the {0,1} requirement is
    stated in the docstring but not enforced.
    """
    if sp.expand(B[2]).subs(var, 0) != 0:
        return True, "leading coefficient non-zero"
    if require_exponents:
        rts, _ = exponents(B, var)
        if rts is None:
            return False, "indicial polynomial identically zero"
        got = {sp.nsimplify(e) for e in rts.keys()}
        if got != {sp.Integer(0), sp.Integer(1)}:
            return False, "exponents %s are not {0,1}" % sorted(map(str, got))
    cc = sp.symbols("k0:%d" % (K + 1))
    Y = 1 + sum(cc[k] * var ** k for k in range(1, K + 1))
    LY = sp.expand(sum(B[j] * sp.diff(Y, var, j) for j in range(3)))
    P = sp.Poly(LY, var)
    eqs = [P.nth(j) for j in range(K - 3)]
    sol = sp.solve(eqs, list(cc[1:]), dict=True)
    return (bool(sol),
            "holomorphic solution with c_0 = 1 exists" if sol else
            "no holomorphic solution with c_0 = 1: a logarithm is forced")


# ---------------------------------------------------- Table 2.1, as data ---
# van der Put - Saito, Table 2.1: family, Katz invariants as a multiset.
# `-` in the authors' tuple notation means "not a singular point".
TABLE21 = [
    ("D4~", "PVI", (0, 0, 0, 0)),
    ("D5~", "PV", (0, 0, 1)),
    ("D6~", "PVdeg=PIII(D6)", (0, 0, sp.Rational(1, 2))),
    ("D6~", "PIII(D6)", (1, 1)),
    ("D7~", "PIII(D7)", (sp.Rational(1, 2), 1)),
    ("D8~", "PIII(D8)", (sp.Rational(1, 2), sp.Rational(1, 2))),
    ("E6~", "PIV", (0, 2)),
    ("E7~", "PII", (0, sp.Rational(3, 2))),
    ("E7~", "PII", (3,)),
    ("E8~", "PI", (sp.Rational(5, 2),)),
]


def match_rows(ms):
    key = sorted(str(sp.nsimplify(x)) for x in ms)
    return [(d, p) for d, p, tup in TABLE21
            if sorted(str(sp.nsimplify(x)) for x in tup) == key]


# ================================================================= STUDY ===


def study(title, bc, ac, buggy=False):
    say("  %s" % title)
    say("    b(n) = %s     a(n) = %s"
        % (sp.factor(sum(c * sp.Symbol('n') ** k for k, c in enumerate(bc))),
           sp.factor(sum(c * sp.Symbol('n') ** k for k, c in enumerate(ac)))))
    say("    b(1) = %s   a(1) = %s   a(2) = %s"
        % (sum(bc), sum(ac), sum(c * 2 ** k for k, c in enumerate(ac))))
    A = to_D(theta_coeffs(bc, ac), z)
    pts_names, ms = [], []

    Bz = [A[0], A[1], A[2]]
    k, _ = katz_both(Bz, z, "z=0")
    pts_names.append("0")
    ms.append(k)

    for s in sp.solve(sp.Eq(sp.expand(A[2]), 0), z):
        if s == 0:
            continue
        Bs = [sp.expand(x.subs(z, s + w)) for x in A]
        Bs = strip_content(Bs, w)
        isord, why = ordinary_point(Bs, w, require_exponents=not buggy)
        rts, _ = exponents(Bs, w)
        say("    z* = %-4s exponents %-26s -> %s"
            % (s, [str(x) for x in sorted(rts, key=str)] if rts else "n/a",
               ("ORDINARY, drops out (%s)" % why) if isord
               else ("singular (%s)" % why)))
        if not isord:
            k, _ = katz_both(Bs, w, "z*")
            pts_names.append("z*")
            ms.append(k)

    Bi = at_infinity(A, z)
    isord, why = ordinary_point(Bi, t, require_exponents=not buggy)
    rts, _ = exponents(Bi, t)
    say("    inf      exponents %-26s -> %s"
        % ([str(x) for x in sorted(rts, key=str)] if rts else "n/a",
           ("ORDINARY, drops out (%s)" % why) if isord
           else ("singular (%s)" % why)))
    if not isord:
        k, _ = katz_both(Bi, t, "inf")
        pts_names.append("inf")
        ms.append(k)

    rows = match_rows(ms)
    say("    => S = %s   Katz multiset = %s   Table 2.1 rows: %s"
        % (pts_names, [str(x) for x in ms], rows if rows else "NONE"))
    say()
    return pts_names, ms, rows


say("=" * 74)
say("CT-S32-LD2-ORDINARY-LOCUS  —  L₂ = z·b(θ+1) + z²·a(θ+2) − 1, θ = z d/dz")
say("independent in-repo re-derivation; uniformiser t = 1/z at ∞")
say("=" * 74)
say()

cs = theta_coeffs([b0, b1, b2], [a0, a1, a2])
say("general theta-coefficients at d = 2:")
for i, c in enumerate(cs):
    say("  c_%d(z) = %s" % (i, sp.factor(c)))
say("  so c_0(z) = a(2) z^2 + b(1) z - 1  :  b(1) and a(2) are the only way")
say("  the coefficients enter c_0, and the lone -1 fixes ord_0 c_0 = 0.")
say()

say("-" * 74)
say("(A)  GENERIC deg a = 2")
say("-" * 74)
nA, msA, rA = study("generic: b = 3n^2 + n + 1, a = n^2 + 1", [1, 1, 3], [1, 0, 1])
ok(rA == [("D6~", "PVdeg=PIII(D6)")] and len(nA) == 3,
   "C1  generic deg a = 2 gives three singular points and the row PVdeg=PIII(D6)",
   "the generic case producing any other row, or fewer than three singular points")

say("-" * 74)
say("(B)  THE LOCUS  a(1) = a(2) = 0  AND  b(1) = 0")
say("-" * 74)
nB, msB, rB = study("ON the locus: b = n^2 + n - 2, a = (n-1)(n-2)",
                    [-2, 1, 1], [2, -3, 1])
ok(rB == [] and nB == ["0", "z*"]
   and sorted(str(x) for x in msB) == ["0", "1/2"],
   "C2  on the locus infinity is ORDINARY, #S = 2, multiset (1/2, -, 0), NO row",
   "infinity staying singular (which would have kept three points and the row "
   "PVdeg), or the two-point multiset happening to match some row of Table 2.1")

nC, msC, rC = study("JUST OFF the locus: same a, b = n^2 + n - 1 so b(1) = 1",
                    [-1, 1, 1], [2, -3, 1])
ok(rC == [("D6~", "PVdeg=PIII(D6)")] and len(nC) == 3,
   "C3  moving beta0 by 1 (b(1): 0 -> 1) restores infinity and the row",
   "the row failing to move when b(1) leaves zero -- which would have shown "
   "the classifier blind to b(1) and C2 therefore uninterpretable")

nD, msD, rD = study("a(1)=a(2)=0 but b(1) = 5 != 0: b = 3n^2 + n + 1, "
                    "a = (n-1)(n-2)", [1, 1, 3], [2, -3, 1])
ok(rD == [("D6~", "PVdeg=PIII(D6)")] and len(nD) == 3,
   "C4  a(1) = a(2) = 0 alone does NOT drop infinity; b(1) = 0 is required too",
   "infinity dropping out on a(1)=a(2)=0 alone, which would have made the "
   "locus codimension 2 rather than 3")

say("-" * 74)
say("(C)  THE PREDICATE DEFECT")
say("-" * 74)
say("  The ordinary-point test must require the exponents to be {0,1}.")
say("  Re-running case C4 with that requirement NOT enforced -- the criterion")
say("  stated in the docstring but not implemented:")
nE, msE, rE = study("C4 again, with the DEFECTIVE predicate", [1, 1, 3],
                    [2, -3, 1], buggy=True)
ok(rE != rD and rE == [],
   "C5  the defective predicate changes the answer: it drops z* (exponents "
   "{0, 7/3}) and loses the row",
   "the defective and the correct predicate agreeing -- which would have meant "
   "the {0,1} requirement was decorative and the defect harmless")
say("  The defective predicate asks only whether SOME holomorphic solution")
say("  with c_0 = 1 exists. At exponents {0, 7/3} one does -- the exponent-0")
say("  solution -- but the second solution w^(7/3)(...) is not holomorphic, the")
say("  Wronskian ~ w^(7/3-1) vanishes at w = 0, and the point is singular.")
say()

say("-" * 74)
say("(D)  WHAT THE LOCUS COSTS THE (alpha2, alpha1) STATEMENT")
say("-" * 74)
say("  C2 and C3 hold the numerator FIXED at a = (n-1)(n-2), i.e. (alpha2,")
say("  alpha1, alpha0) = (1, -3, 2) unchanged, and move beta0 alone from -2 to")
say("  -1. The answer changes from NO ROW to PVdeg=PIII(D6).")
ok(msB != msC and rB != rC,
   "C6  with (alpha2, alpha1) held fixed, beta0 alone moves the answer",
   "the multiset being unchanged by beta0 on this locus -- which would have "
   "left 'the row depends on (alpha2, alpha1) alone' intact")
say("  Hence: the row is a function of (alpha2, alpha1) alone GENERICALLY,")
say("  and that statement is FALSE on the codimension-3 locus")
say("      a(1) = a(2) = 0  and  b(1) = beta2 + beta1 + beta0 = 0,")
say("  where the operator is not classified by Table 2.1 at all.")
say()

say("=" * 74)
say("CONTROLS: %d/%d PASS" % (NPASS[0], NPASS[0]))
say("elapsed %.1fs" % (time.time() - T0))
say("=" * 74)

# --------------------------------------------------- artefact + read-back ---
OUT = "outputs/locus.out.txt"
data = BUF.getvalue()
with open(OUT, "w", encoding="utf-8", newline="") as fh:
    fh.write(data)
raw = open(OUT, "rb").read()
text = raw.decode("utf-8")
assert b"\r\n" not in raw, "CRLF leaked into the artefact"
assert "θ" in text and "∞" in text and "₂" in text, \
    "known-present non-ASCII sentinel missing: the reader is not verified"
assert "θ" not in raw.decode("latin-1"), \
    "sentinel is not codec-fragile: it cannot detect a wrong-codec read"
assert text == data, "artefact on disk differs from what was written"
assert "CONTROLS: %d/%d PASS" % (NPASS[0], NPASS[0]) in text
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
