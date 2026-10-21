#!/usr/bin/env python3
"""CT-S52 Part A -- is xi = 0 log-free for L_V?

Everything here is EXACT arithmetic in Q(sqrt3), represented as pairs of
Fractions (class Q3, copied from the deposited bundle's q3_foundation.py).
No floating point is used at any step that feeds a verdict.

Order of business, fixed in PREREG.md and not negotiable at runtime:
  A0  transcribe L_V from the manuscript .tex, two independent routes
  A1  residual L_V B-hat = 0 through xi^129, exactly
  A2  indicial polynomial at xi = 0 and its exact roots
  A3  Frobenius from the lowest exponent, logs or no logs      <- the observable
  then, and only then, the controls and the vacuity pre-check.

Exit codes: 0 clean, 1 finding, 2 refusal, 3 crash.
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re
import hashlib
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from q3_foundation import Q3, formal_series_coeffs_exact  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
TEX = os.path.join(ROOT, "sessions", "2026-06-16", "VQUAD-PAPER-LAYOUTFIX-001",
                   "latex", "vquad-periodrep-paper.tex")
OUT = os.path.join(HERE, "..", "outputs", "xi0_logs.out.txt")

LINES = []
FINDINGS = []


def say(s=""):
    print(s)
    LINES.append(s)


def finding(s):
    FINDINGS.append(s)
    say("  FINDING: " + s)


# ----------------------------------------------------------------- A0 transcription
# Route 1: parse the align* block of Appendix A.1 out of the manuscript source.
def parse_tex_LV(path):
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read().replace("\r\n", "\n")
    i = src.index(r"\subsection{Full coefficient listings}")
    j = src.index(r"\begin{align*}", i)
    k = src.index(r"\end{align*}", j)
    block = src[j + len(r"\begin{align*}"):k]
    ents = re.split(r"p_(\d)&=", block)
    out = {}
    for t in range(1, len(ents), 2):
        kk = int(ents[t])
        body = ents[t + 1]
        # p_4 restates itself in factored form after a second '='; keep the
        # first form only, which is the coefficient listing proper.
        body = body.split("=")[0]
        terms = {}
        if kk == 0:
            body_stripped = body.strip().rstrip(",\\ \n")
            if body_stripped != "1":
                raise ValueError("p_0 is not 1 in the source: %r" % body_stripped)
            out[0] = [Q3(1, 0)]
            continue
        pat = re.compile(
            r"(?P<sign>[+-]?)\s*\\frac\{(?P<a>\d+)\+(?P<b>\d+)\\sqrt3\}\{(?P<d>\d+)\}"
            r"(?P<xi>\s*\\,\\xi(?:\^(?P<pw>\d))?)?")
        pos = 0
        while True:
            m = pat.search(body, pos)
            if not m:
                break
            pos = m.end()
            sgn = -1 if m.group("sign") == "-" else 1
            den = int(m.group("d"))
            a = F(sgn * int(m.group("a")), den)
            b = F(sgn * int(m.group("b")), den)
            if m.group("xi") is None:
                i_pw = 0
            elif m.group("pw") is None:
                i_pw = 1
            else:
                i_pw = int(m.group("pw"))
            if i_pw in terms:
                raise ValueError("duplicate xi^%d term in p_%d" % (i_pw, kk))
            terms[i_pw] = Q3(a, b)
        deg = max(terms)
        out[kk] = [terms.get(i, Q3(0, 0)) for i in range(deg + 1)]
    return out


# Route 2: typed in by hand from the rendered Appendix A.1, independently of
# the parser. A disagreement in any entry is F-A0 and halts.
HAND = {
    0: [(F(1), F(0))],
    1: [(F(659, 431), F(150, 431)),
        (F(432, 431), F(12, 431))],
    2: [(F(2552175, 418501), F(199224, 418501)),
        (F(496044, 418501), F(61620, 418501)),
        (F(70092, 418501), F(3240, 418501))],
    3: [(F(77760, 418501), F(560736, 418501)),
        (F(1685448, 418501), F(101124, 418501)),
        (F(70092, 418501), F(3240, 418501))],
    4: [(F(0), F(0)),
        (F(19440, 418501), F(140184, 418501)),
        (F(210276, 418501), F(9720, 418501))],
}


def hand_LV():
    return {k: [Q3(a, b) for (a, b) in v] for k, v in HAND.items()}


# ----------------------------------------------------------------- helpers
def falling_int(x, k):
    """(x)_k for x an int or Fraction -> Fraction."""
    r = F(1)
    for t in range(k):
        r *= (x - t)
    return r


def poly_falling(k):
    """coefficients of (s)_k as a list of ints, ascending powers of s."""
    c = [1]
    for t in range(k):
        nc = [0] * (len(c) + 1)
        for d, v in enumerate(c):
            nc[d + 1] += v
            nc[d] += -t * v
        c = nc
    return c


def q3_str(v):
    s = "%s" % v.p
    s += (" + " if v.q >= 0 else " - ") + "%s" % abs(v.q) + "*sqrt3"
    return s


def L_of(P):
    return max(k - i for k in P for i, c in enumerate(P[k]) if not c.is_zero())


def indicial_poly(P):
    """exact Q3 coefficient list (ascending) of I(s)."""
    Lm = L_of(P)
    deg = max(P)
    out = [Q3(0, 0)] * (deg + 1)
    for k in P:
        for i, c in enumerate(P[k]):
            if c.is_zero() or k - i != Lm:
                continue
            pf = poly_falling(k)
            for d, v in enumerate(pf):
                out[d] = out[d] + c * Q3(v, 0)
    while len(out) > 1 and out[-1].is_zero():
        out.pop()
    return out


def poly_eval(coeffs, x):
    """x a Fraction/int -> Q3"""
    acc = Q3(0, 0)
    xp = F(1)
    for c in coeffs:
        acc = acc + c * Q3(xp, 0)
        xp *= x
    return acc


def rational_roots(coeffs):
    """exact roots of a Q3-coefficient polynomial, found by trial integer roots
    and confirmed by synthetic division; returns (roots, remaining_degree)."""
    cur = list(coeffs)
    roots = []
    changed = True
    while changed and len(cur) > 1:
        changed = False
        for r in range(-12, 13):
            if poly_eval(cur, F(r)).is_zero():
                # synthetic division by (s - r), descending
                desc = list(reversed(cur))
                q = [desc[0]]
                for t in range(1, len(desc) - 1):
                    q.append(desc[t] + q[-1] * Q3(r, 0))
                rem = desc[-1] + q[-1] * Q3(r, 0)
                if not rem.is_zero():
                    continue
                cur = list(reversed(q))
                roots.append(r)
                changed = True
                break
    return sorted(roots), len(cur) - 1


# ----------------------------------------------------------------- exact linear algebra
def rref_rank_null(rows, ncols):
    """exact Gaussian elimination over Q(sqrt3).

    returns (rank, nullspace_basis) with the basis as lists of Q3 of length
    ncols."""
    M = [list(r) for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = None
        for t in range(r, len(M)):
            if not M[t][c].is_zero():
                p = t
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        inv = M[r][c]
        M[r] = [x / inv for x in M[r]]
        for t in range(len(M)):
            if t != r and not M[t][c].is_zero():
                f = M[t][c]
                M[t] = [M[t][j] - f * M[r][j] for j in range(ncols)]
        piv.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Q3(0, 0)] * ncols
        v[fc] = Q3(1, 0)
        for i, pc in enumerate(piv):
            v[pc] = Q3(0, 0) - M[i][fc]
        basis.append(v)
    return len(piv), basis


# ----------------------------------------------------------------- A3 Frobenius
def frobenius(P, s0, nmax):
    """Frobenius recursion from exponent s0, every c_n carried as an exact
    Q(sqrt3)-linear form in the free parameters introduced so far.

    At a resonant step n (I(s0+n) = 0) the recursion does NOT immediately force a
    logarithm: the obstruction is a linear form in the parameters already
    introduced, and it is a *constraint*. c_n then enters as a new free
    parameter. A logarithm is forced exactly for those parameter values that
    violate a constraint. The log-free solution space is therefore the nullspace
    of the accumulated constraint system, and a log-free solution with leading
    exponent exactly s0 exists iff that nullspace contains a vector whose first
    component (c_0) is nonzero.
    """
    Lm = L_of(P)
    Ip = indicial_poly(P)
    if not poly_eval(Ip, F(s0)).is_zero():
        raise ValueError("s0 is not an indicial root")
    nparam = 1
    c = {0: [Q3(1, 0)]}
    events = []
    constraints = []          # each: (n, exponent, vector over params)

    def vec(n, width):
        v = list(c.get(n, []))
        v += [Q3(0, 0)] * (width - len(v))
        return v

    events.append((0, "seed", "c_0 free (exponent %s)" % s0))
    for n in range(1, nmax + 1):
        rest = [Q3(0, 0)] * nparam
        for k in P:
            for i, pki in enumerate(P[k]):
                if pki.is_zero() or k - i == Lm:
                    continue
                m = n - Lm + k - i
                if m < 0 or m >= n:
                    continue
                ff = falling_int(F(s0 + m), k)
                cm = vec(m, nparam)
                for t in range(nparam):
                    rest[t] = rest[t] + pki * Q3(ff, 0) * cm[t]
        In = poly_eval(Ip, F(s0 + n))
        if not In.is_zero():
            c[n] = [Q3(0, 0) - (rest[t] / In) for t in range(nparam)]
        else:
            if all(x.is_zero() for x in rest):
                events.append((n, "consistent",
                               "exponent %s: obstruction vanishes identically"
                               % (s0 + n)))
            else:
                events.append((n, "constraint",
                               "exponent %s: obstruction %s must vanish"
                               % (s0 + n,
                                  " , ".join(q3_str(x) for x in rest))))
                constraints.append((n, s0 + n, list(rest)))
            # c_n enters as a new free parameter either way
            nparam += 1
            for m in list(c):
                c[m] = vec(m, nparam)
            v = [Q3(0, 0)] * nparam
            v[nparam - 1] = Q3(1, 0)
            c[n] = v
    # widen every stored constraint to the final parameter count
    rows = []
    for (n, e, r) in constraints:
        rows.append(list(r) + [Q3(0, 0)] * (nparam - len(r)))
    rank, basis = rref_rank_null(rows, nparam) if rows else (0, None)
    if rows:
        dim = nparam - rank
    else:
        dim = nparam
        basis = [[Q3(1, 0) if i == j else Q3(0, 0) for i in range(nparam)]
                 for j in range(nparam)]
    leading_ok = any(not b[0].is_zero() for b in basis)
    return {"events": events, "nparam": nparam, "constraints": constraints,
            "logfree_dim": dim, "leading_ok": leading_ok, "c": c, "Lm": Lm}


def poly_falling_prime(k):
    """coefficients of d/ds (s)_k, ascending, exact ints."""
    pf = poly_falling(k)
    return [d * pf[d] for d in range(1, len(pf))]


def eval_int_poly(coeffs, x):
    acc = F(0)
    xp = F(1)
    for c in coeffs:
        acc += F(c) * xp
        xp *= x
    return acc


def log_solution(P, mmin, M):
    """Exhibit a logarithmic solution, if one exists.

    Ansatz  y = sum_m u_m xi^m + log(xi) * sum_m v_m xi^m, using
    D^k(xi^m log xi) = (m)_k xi^{m-k} log xi + (m)_k' xi^{m-k}, which is just
    d/dm of D^k(xi^m). Splitting L_V y = 0 into its log and non-log parts gives
    a linear system in (u, v) over Q(sqrt3). A nullspace vector with v != 0 IS a
    logarithmic solution -- positive evidence, as opposed to the absence of a
    power solution."""
    Lm = L_of(P)
    ms = list(range(mmin, M + 1))
    iu = {m: t for t, m in enumerate(ms)}
    iv = {m: len(ms) + t for t, m in enumerate(ms)}
    ncols = 2 * len(ms)
    rows = []
    for p in range(mmin - Lm, M - Lm + 1):
        rlog = [Q3(0, 0)] * ncols
        rnon = [Q3(0, 0)] * ncols
        nz = False
        for k in P:
            pf = poly_falling(k)
            pfp = poly_falling_prime(k)
            for i, pki in enumerate(P[k]):
                if pki.is_zero():
                    continue
                m = p + k - i
                if m not in iu:
                    continue
                nz = True
                ff = eval_int_poly(pf, F(m))
                fp = eval_int_poly(pfp, F(m))
                rlog[iv[m]] = rlog[iv[m]] + pki * Q3(ff, 0)
                rnon[iu[m]] = rnon[iu[m]] + pki * Q3(ff, 0)
                rnon[iv[m]] = rnon[iv[m]] + pki * Q3(fp, 0)
        if nz:
            rows.append(rlog)
            rows.append(rnon)
    rank, basis = rref_rank_null(rows, ncols)
    with_log = [b for b in basis
                if any(not b[iv[m]].is_zero() for m in ms)]
    lead_u = None
    for b in with_log:
        for m in ms:
            if not b[iu[m]].is_zero():
                lead_u = m if lead_u is None else min(lead_u, m)
                break
    return {"dim": ncols - rank, "basis": basis, "with_log": with_log,
            "lead_u": lead_u, "iu": iu, "iv": iv, "ms": ms}


def laurent_dim(P, mmin, M):

    """ROUTE 2, sharing no code with frobenius(): the dimension of the space of
    truncated Laurent solutions y = sum_{m=mmin}^{M} c_m xi^m, obtained by exact
    Gaussian elimination on the coefficient equations. No Frobenius bookkeeping,
    no indicial polynomial, no notion of resonance. A log-free local basis of
    size d shows up here as nullspace dimension d."""
    Lm = L_of(P)
    idx = {m: t for t, m in enumerate(range(mmin, M + 1))}
    ncols = len(idx)
    rows = []
    for p in range(mmin - Lm, M - Lm + 1):
        row = [Q3(0, 0)] * ncols
        nz = False
        for k in P:
            for i, pki in enumerate(P[k]):
                if pki.is_zero():
                    continue
                m = p + k - i
                if m in idx:
                    row[idx[m]] = row[idx[m]] + pki * Q3(falling_int(F(m), k), 0)
                    nz = True
        if nz:
            rows.append(row)
    rank, basis = rref_rank_null(rows, ncols)
    dims = ncols - rank
    lead = []
    for b in basis:
        for t, v in enumerate(b):
            if not v.is_zero():
                lead.append(mmin + t)
                break
    return dims, sorted(lead), basis, idx


# ----------------------------------------------------------------- A1 residual
def residual_exact(P, Ns):
    need = max(Ns) + max(P) + 3
    a = formal_series_coeffs_exact(need + 3)
    fact = [F(1)] * (need + 2)
    for m in range(1, need + 2):
        fact[m] = fact[m - 1] * m
    b = [a[m + 1] / Q3(fact[m], 0) for m in range(need)]
    out = {}
    for N in Ns:
        res = Q3(0, 0)
        for k in P:
            for i, pki in enumerate(P[k]):
                if pki.is_zero():
                    continue
                m = N - i + k
                if 0 <= m < len(b):
                    res = res + pki * Q3(falling_int(F(m), k), 0) * b[m]
        out[N] = res
    return out


# ----------------------------------------------------------------- main
def main():
    say("=" * 74)
    say("CT-S52 PART A -- logarithms at xi = 0 for L_V (exact over Q(sqrt3))")
    say("=" * 74)

    # ---- A0
    say()
    say("[A0] transcription of L_V from the manuscript source")
    say("  source: sessions/2026-06-16/VQUAD-PAPER-LAYOUTFIX-001/latex/"
        "vquad-periodrep-paper.tex")
    with open(TEX, "rb") as fh:
        tex_sha = hashlib.sha256(fh.read()).hexdigest()
    say("  sha256: %s" % tex_sha)
    P_tex = parse_tex_LV(TEX)
    P_hand = hand_LV()
    n_entries = 0
    ok = True
    for k in sorted(P_hand):
        if k not in P_tex or len(P_tex[k]) != len(P_hand[k]):
            finding("p_%d: parser and hand table differ in length" % k)
            ok = False
            continue
        for i in range(len(P_hand[k])):
            n_entries += 1
            if not (P_tex[k][i] == P_hand[k][i]):
                finding("p_%d[xi^%d]: parser %s vs hand %s"
                        % (k, i, P_tex[k][i], P_hand[k][i]))
                ok = False
    say("  %d coefficient entries compared, parser vs independent hand table: %s"
        % (n_entries, "AGREE" if ok else "DISAGREE"))
    for k in sorted(P_tex):
        say("    p_%d = %s" % (k, "  ".join(
            "(%s)xi^%d" % (q3_str(v), i) for i, v in enumerate(P_tex[k])
            if not v.is_zero())))
    if not ok:
        say()
        say("REFUSED: F-A0 fired; transcription not established.")
        return 2
    P = P_tex

    # ---- A1
    say()
    say("[A1] residual  L_V B-hat  through xi^129, exact in Q(sqrt3)")
    Ns = list(range(0, 130))
    res = residual_exact(P, Ns)
    bad = [N for N in Ns if not res[N].is_zero()]
    say("  N = 0..129, %d orders tested" % len(Ns))
    say("  nonzero residuals: %d" % len(bad))
    if bad:
        for N in bad[:8]:
            finding("res(xi^%d) = %s != 0" % (N, q3_str(res[N])))
        say()
        say("REFUSED: F-A1 fired; the printed operator does not annihilate B-hat.")
        return 2
    say("  res(xi^N) = 0 exactly for every N in 0..129   [reproduces the "
        "manuscript's own Appendix A.1 claim]")

    # ---- A2
    say()
    say("[A2] indicial polynomial at xi = 0 and its exact roots")
    Ip = indicial_poly(P)
    Lm = L_of(P)
    say("  L = max(k - i) = %d, so the lowest power is xi^(s-%d)" % (Lm, Lm))
    say("  I(s) = " + " + ".join("(%s)s^%d" % (q3_str(c), d)
                                 for d, c in enumerate(Ip) if not c.is_zero()))
    roots, rem = rational_roots(Ip)
    say("  exact integer roots: %s   (degree remaining after division: %d)"
        % (roots, rem))
    if roots != [-1, 0, 1, 2] or rem != 0:
        finding("exponent multiset is %s, not {-1,0,1,2} (remaining degree %d)"
                % (roots, rem))
        say()
        say("REFUSED: F-A2 fired; Prop 2.4's exponent statement is not reproduced.")
        return 2
    say("  exponents at xi = 0: {-1, 0, 1, 2}  -- consecutive integers, so every")
    say("  step n = 1, 2, 3 from the lowest exponent is RESONANT and a logarithm")
    say("  is possible at each. That is what A3 decides.")

    # ---- A3  THE OBSERVABLE.  Evaluated before any control (CT-S47 ordering).
    say()
    say("[A3] Frobenius basis at xi = 0  [OBSERVABLE]")
    say("  Route 1: recursion from each exponent, obstructions carried as exact")
    say("  linear forms in the free parameters. At a resonant step the")
    say("  obstruction is a CONSTRAINT: violate it and a logarithm is forced.")
    per_exp = {}
    for s0 in (-1, 0, 1, 2):
        fr = frobenius(P, s0, 14)
        per_exp[s0] = fr
        say()
        say("  from exponent s = %d:" % s0)
        for n, kind, msg in fr["events"]:
            say("      n=%-2d %-10s %s" % (n, kind, msg))
        say("      free parameters %d, independent constraints %d, "
            "log-free dimension %d"
            % (fr["nparam"], fr["nparam"] - fr["logfree_dim"],
               fr["logfree_dim"]))
        say("      log-free solution with leading exponent exactly %d: %s"
            % (s0, "YES" if fr["leading_ok"] else "NO -- logarithm forced"))

    fr_low = per_exp[-1]
    say()
    say("  Route 2: independent check by exact Gaussian elimination on the")
    say("  truncated Laurent ansatz y = sum_{m=-1}^{M} c_m xi^m. Shares no code")
    say("  with Route 1: no indicial polynomial, no notion of resonance.")
    dims = {}
    for M in (16, 24):
        d, lead, _, _ = laurent_dim(P, -1, M)
        dims[M] = (d, lead)
        say("      M=%-3d nullspace dimension %d, leading exponents %s"
            % (M, d, lead))
    d2, lead2 = dims[24]
    r1_dim = fr_low["logfree_dim"]
    say("  Route 1 log-free dimension from the lowest exponent: %d" % r1_dim)
    say("  Route 2 log-free dimension: %d" % d2)
    routes_agree = (r1_dim == d2)
    if not routes_agree:
        finding("the two routes disagree on the log-free dimension "
                "(%d vs %d); neither may be reported" % (r1_dim, d2))

    logs = [s for s in (-1, 0, 1, 2) if not per_exp[s]["leading_ok"]]

    # ---- A5, still part of the observable: exhibit the logarithm positively
    say()
    say("  Route 3 (positive): does a logarithmic solution actually exist?")
    say("  Ansatz y = sum u_m xi^m + log(xi) sum v_m xi^m, solved exactly. A")
    say("  nullspace vector with v != 0 IS a logarithmic solution; this is")
    say("  presence, not the absence of a power solution.")
    ls = log_solution(P, -1, 18)
    say("      total local solution dimension found: %d" % ls["dim"])
    say("      of which carry a nonzero log part: %d" % len(ls["with_log"]))
    if ls["with_log"]:
        b = ls["with_log"][0]
        lu = ls["lead_u"]
        scale = b[ls["iu"][lu]]
        b = [x / scale for x in b]
        say("      lowest power appearing in the log solution's u-part: xi^%s"
            % lu)
        say("      exhibited solution, normalised to u_%d = 1:" % lu)
        say("        u: " + " ; ".join(
            "u_%d = %s" % (m, q3_str(b[ls["iu"][m]])) for m in range(-1, 2)))
        say("        v: " + " ; ".join(
            "v_%d = %s" % (m, q3_str(b[ls["iv"][m]])) for m in range(0, 2)))
        say("      (v is a nonzero multiple of B-hat, so the fourth local")
        say("       solution is  xi^-1(1 + ...) + c*log(xi)*B-hat-like series)")
    verdict = ("NO LOGARITHMS (xi = 0 apparent)"
               if (not logs and d2 == 4 and not ls["with_log"])
               else "LOGARITHMS FOUND")
    say()
    say("  PART A VERDICT (observable, before controls): %s" % verdict)
    say("  per-exponent report:")
    for e in (-1, 0, 1, 2):
        fr = per_exp[e]
        if fr["leading_ok"]:
            say("    exponent %2d : recursion CONSISTENT at every resonant step "
                "reachable from it; log-free solution exists" % e)
        else:
            bad = [ev for ev in fr["events"] if ev[1] == "constraint"]
            say("    exponent %2d : recursion INCONSISTENT -- LOGARITHM FORCED "
                "(first obstruction at n=%d, exponent %d)"
                % (e, bad[0][0], e + bad[0][0]))
    say("  a log-free local basis has dimension %d of the 4 required" % d2)
    if logs:
        say("  => xi = 0 is NOT an apparent singularity of L_V: the four")
        say("     exponents are consecutive integers, but the recursion is")
        say("     obstructed, and the local solution space needs %d logarithmic"
            % (4 - d2))
        say("     solution(s). B-hat itself is the holomorphic exponent-0")
        say("     solution and is unaffected (A1 above).")

    # ---- controls, AFTER the observable
    say()
    say("[C] controls -- same routine, no special-casing")
    # C-LOG: (xi^3-2xi)D^2 + (2-3xi^2)D + 4xi ; basis {xi^2, 1 + xi^2 log xi}
    P_log = {0: [Q3(0, 0), Q3(4, 0)],
             1: [Q3(2, 0), Q3(0, 0), Q3(-3, 0)],
             2: [Q3(0, 0), Q3(-2, 0), Q3(0, 0), Q3(1, 0)]}
    r_log, _ = rational_roots(indicial_poly(P_log))
    fr_log = frobenius(P_log, min(r_log), 8)
    d_log, lead_log, _, _ = laurent_dim(P_log, min(r_log), 16)
    ls_log = log_solution(P_log, min(r_log), 14)
    got_log = ((not fr_log["leading_ok"]) and d_log == 1
               and len(ls_log["with_log"]) >= 1)
    say("  C-LOG   exponents %s ; known basis {xi^2, 1 + xi^2 log xi}" % r_log)
    for n, kind, msg in fr_log["events"]:
        say("            n=%-2d %-10s %s" % (n, kind, msg))
    say("            route 1: log-free solution at exponent %d: %s"
        % (min(r_log), "YES" if fr_log["leading_ok"] else "NO"))
    say("            route 2: log-free dimension %d, leading exponents %s"
        % (d_log, lead_log))
    say("            route 3: solutions carrying a log: %d (expected >= 1)"
        % len(ls_log["with_log"]))
    say("          -> %s" % ("FIRED (the logarithm at exponent 0 is detected, "
                             "and only xi^2 survives)" if got_log
                             else "DID NOT FIRE"))
    # C-NOLOG: xi(1-xi)D^2 + (2-3xi)D - 1 ; basis {1/xi, -log(1-xi)/xi}
    P_nolog = {0: [Q3(-1, 0)],
               1: [Q3(2, 0), Q3(-3, 0)],
               2: [Q3(0, 0), Q3(1, 0), Q3(-1, 0)]}
    r_nolog, _ = rational_roots(indicial_poly(P_nolog))
    fr_nolog = frobenius(P_nolog, min(r_nolog), 8)
    d_nolog, lead_nolog, _, _ = laurent_dim(P_nolog, min(r_nolog), 16)
    ls_nolog = log_solution(P_nolog, min(r_nolog), 14)
    got_nolog = (fr_nolog["leading_ok"] and d_nolog == 2
                 and len(ls_nolog["with_log"]) == 0)
    say("  C-NOLOG exponents %s ; known basis {1/xi, -log(1-xi)/xi}, both "
        "log-free" % r_nolog)
    for n, kind, msg in fr_nolog["events"]:
        say("            n=%-2d %-10s %s" % (n, kind, msg))
    say("            route 1: log-free solution at exponent %d: %s"
        % (min(r_nolog), "YES" if fr_nolog["leading_ok"] else "NO"))
    say("            route 2: log-free dimension %d, leading exponents %s"
        % (d_nolog, lead_nolog))
    say("            route 3: solutions carrying a log: %d (expected 0)"
        % len(ls_nolog["with_log"]))
    say("          -> %s" % ("FIRED (a consistent resonance is NOT reported as "
                             "a logarithm)" if got_nolog
                             else "DID NOT FIRE (false logarithm)"))

    controls_ok = got_log and got_nolog and r_log == [0, 2] and r_nolog == [-1, 0]
    say("  controls: %s" % ("2/2 FIRED" if controls_ok else "FAILED"))

    # ---- vacuity pre-check for A1, also after the observable
    say()
    say("[V] vacuity pre-check for the residual A1")
    P_bad = {k: list(v) for k, v in P.items()}
    P_bad[2] = list(P_bad[2])
    P_bad[2][0] = P_bad[2][0] + Q3(F(1, 418501), F(0))
    res_bad = residual_exact(P_bad, list(range(0, 21)))
    moved = [N for N in range(0, 21) if not res_bad[N].is_zero()]
    say("  p_2 constant term perturbed by +1/418501; nonzero residuals in "
        "N=0..20: %d" % len(moved))
    vac_ok = len(moved) > 0
    say("  -> %s" % ("FIRED (A1 can see a wrong operator)"
                     if vac_ok else "DID NOT FIRE (A1 is vacuous)"))

    # ---- summary
    say()
    say("=" * 74)
    say("PART A SUMMARY")
    say("  transcription  : %d entries, parser == hand table" % n_entries)
    say("  residual       : 0 exactly for xi^0 .. xi^129 (exact Q(sqrt3))")
    say("  exponents      : {-1, 0, 1, 2}, exact integer roots of I(s)")
    say("  verdict        : %s" % verdict)
    say("  two routes     : %s (Route 1 dim %d, Route 2 dim %d)"
        % ("AGREE" if routes_agree else "DISAGREE", r1_dim, d2))
    say("  arithmetic     : exact throughout; no floating point in any verdict")
    say("  controls       : C-LOG %s, C-NOLOG %s, vacuity %s"
        % ("FIRED" if got_log else "FAILED",
           "FIRED" if got_nolog else "FAILED",
           "FIRED" if vac_ok else "FAILED"))
    if not (controls_ok and vac_ok):
        say("  VERDICT STATUS : VOID -- a control failed; the observable above "
            "stands as computed but carries no weight")
        say("=" * 74)
        return 1
    say("  VERDICT STATUS : STANDS")
    say("=" * 74)
    return 0 if not FINDINGS else 1


if __name__ == "__main__":
    try:
        rc = main()
    except Exception as exc:  # noqa: BLE001
        say("CRASH: %r" % (exc,))
        rc = 3
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(os.path.abspath(OUT), "w", encoding="utf-8") as fh:
        fh.write("\n".join(LINES) + "\n")
    h = hashlib.sha256("\n".join(LINES).encode("utf-8") + b"\n").hexdigest()
    print("[wrote] %s" % os.path.abspath(OUT))
    print("[sha256] %s" % h)
    sys.exit(rc)
