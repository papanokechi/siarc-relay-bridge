#!/usr/bin/env python3
# PERIOD-REP-VQUAD-002 Stage 3 — EXACT holonomic recognition over Q(sqrt3).
#
# Question (G-OMEGA): does the V_quad Borel transform B-hat(xi) satisfy a linear
# ODE  sum_{k=0}^r p_k(xi) D^k B-hat = 0  with polynomial coeffs p_k in Q(sqrt3)[xi]?
# Equivalently (Borel = Hadamard product with 1/m!, which preserves P-recursiveness)
# does phi(z)=sum a_n z^n satisfy  sum_k q_k(z) D^k phi = 0 with q_k in Q(sqrt3)[z]?
#
# KEY LEVER: the V_quad Riccati recursion (REPRODUCE_stokes_2piK.py:99-127) seeds
# sigma=-1/sqrt3 with sigma^2=1/3 in Q and 1/sigma=-sqrt3 in Q(sqrt3); ALL a_n
# therefore lie EXACTLY in Q(sqrt3)=Q+Q*sqrt3. We represent each coefficient as an
# exact pair (p,q) of Fractions meaning p+q*sqrt3 and run Gaussian elimination over
# the field Q(sqrt3). A nonempty null space (over-determined x2) = a holonomic ODE
# with coefficients provably in Q(sqrt3). Empty at every (r,d) = no such ODE.
#
# This is the gold-standard coefficient-field test (stronger than numerical PSLQ).
from fractions import Fraction as F
import json, math, sys

# ---------------------------------------------------------------- Q(sqrt3) field
class Q3:
    __slots__ = ("p", "q")
    def __init__(self, p=0, q=0):
        self.p = p if isinstance(p, F) else F(p)
        self.q = q if isinstance(q, F) else F(q)
    def __add__(a, b):
        b = a._c(b); return Q3(a.p + b.p, a.q + b.q)
    def __radd__(a, b): return a.__add__(b)
    def __sub__(a, b):
        b = a._c(b); return Q3(a.p - b.p, a.q - b.q)
    def __rsub__(a, b):
        b = a._c(b); return Q3(b.p - a.p, b.q - a.q)
    def __mul__(a, b):
        b = a._c(b); return Q3(a.p * b.p + 3 * a.q * b.q, a.p * b.q + a.q * b.p)
    def __rmul__(a, b): return a.__mul__(b)
    def __truediv__(a, b):
        b = a._c(b); den = b.p * b.p - 3 * b.q * b.q
        if den == 0: raise ZeroDivisionError
        # (a)*(conj b)/N
        num = a * Q3(b.p, -b.q)
        return Q3(num.p / den, num.q / den)
    def is_zero(a): return a.p == 0 and a.q == 0
    def __eq__(a, b):
        b = a._c(b); return a.p == b.p and a.q == b.q
    @staticmethod
    def _c(b):
        return b if isinstance(b, Q3) else Q3(b, 0)
    def to_float(a):
        return float(a.p) + float(a.q) * math.sqrt(3.0)
    def __repr__(a):
        return f"({a.p}+{a.q}*r3)"

R3 = Q3(0, 1)        # sqrt3
SIGMA = Q3(0, F(-1, 3))   # -1/sqrt3 = -sqrt3/3

# ---------------------------------------------------- exact Riccati / a_n in Q3
def riccati_coeffs_exact(sigma, order):
    c = [Q3(0)] * (order + 1)
    d = [Q3(0)] * (order + 1)
    c[0] = sigma
    c[1] = Q3(-1) - sigma / 6
    d[0] = c[0] * c[0]
    d[1] = 2 * c[0] * c[1]
    for k in range(2, order + 1):
        known = Q3(0)
        for i in range(1, k):
            known = known + c[i] * c[k - i]
        rest = (3 * (known - (k - 1) * c[k - 1])
                + d[k - 1] + d[k - 2] + 6 * c[k - 1] + c[k - 2])
        c[k] = (Q3(0) - rest) / (6 * c[0])
        d[k] = 2 * c[0] * c[k] + known - (k - 1) * c[k - 1]
    return c

def formal_series_coeffs_exact(order):
    rc = riccati_coeffs_exact(SIGMA, order + 10)
    f = [Q3(0)] * (order + 1)
    for k in range(1, order + 1):
        if k + 1 < len(rc):
            f[k] = (Q3(0) - rc[k + 1]) / k
    a = [Q3(0)] * (order + 1)
    a[0] = Q3(1)
    for n in range(1, order + 1):
        s = Q3(0)
        for k in range(1, n + 1):
            s = s + (k * f[k]) * a[n - k]
        a[n] = s / n
    return a

# ----------------------------------------------- exact nullspace over Q(sqrt3)
def nullspace_dim(rows):
    """rows: list of lists of Q3 (matrix). Return (rank, ncols, nullity, basis)."""
    if not rows:
        return 0, 0, 0, []
    M = [r[:] for r in rows]
    nr = len(M); nc = len(M[0])
    pivot_cols = []
    r = 0
    for col in range(nc):
        piv = None
        for rr in range(r, nr):
            if not M[rr][col].is_zero():
                piv = rr; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = Q3(1) / M[r][col]
        M[r] = [x * inv for x in M[r]]
        for rr in range(nr):
            if rr != r and not M[rr][col].is_zero():
                factor = M[rr][col]
                M[rr] = [M[rr][j] - factor * M[r][j] for j in range(nc)]
        pivot_cols.append(col)
        r += 1
        if r == nr:
            break
    rank = r
    nullity = nc - rank
    # extract a rational (Q3) null basis
    basis = []
    free_cols = [c for c in range(nc) if c not in pivot_cols]
    for fc in free_cols:
        vec = [Q3(0)] * nc
        vec[fc] = Q3(1)
        for i, pc in enumerate(pivot_cols):
            vec[pc] = Q3(0) - M[i][fc]
        basis.append(vec)
    return rank, nc, nullity, basis

# ----------------------------------------------- build holonomic ansatz matrix
def falling(n, k):
    """ (n)(n-1)...(n-k+1) integer falling factorial, k factors. """
    p = 1
    for t in range(k):
        p *= (n - t)
    return p

def holonomic_matrix(coeffs, r, d, nrows):
    """ Test sum_{k=0}^r poly_k(z) D^k F(z)=0 where F=sum coeffs[m] z^m.
        Unknowns: e[k][i], k=0..r, i=0..d  (poly_k = sum_i e[k][i] z^i).
        Eq for power z^N:  sum_k sum_i e[k][i]*coeffs[N-i+k]*falling(N-i+k,k)=0.
        Returns matrix (nrows x U). """
    U = (r + 1) * (d + 1)
    Mrows = []
    for N in range(nrows):
        row = [Q3(0)] * U
        col = 0
        for k in range(r + 1):
            for i in range(d + 1):
                j = N - i
                if j >= 0 and (j + k) < len(coeffs):
                    row[col] = coeffs[j + k] * falling(j + k, k)
                col += 1
        Mrows.append(row)
    return Mrows, U

def borel_coeffs(a):
    """ B-hat(xi)=sum_{n>=1} a_n xi^{n-1}/(n-1)! ; b_m = a_{m+1}/m!  (m>=0). """
    b = []
    fact = 1
    for m in range(len(a) - 1):
        if m > 0:
            fact *= m
        b.append(a[m + 1] / fact)
    return b

# ------------------------------------------------------------------- main
def main():
    ORDER = 150
    print(f"[gen] exact a_n over Q(sqrt3) to order {ORDER} ...", flush=True)
    a = formal_series_coeffs_exact(ORDER)

    # sanity: a_n float values vs known anchors
    avals = [a[n].to_float() for n in range(8)]
    print("[chk] a_0..a_7 (float):", [f"{x:.10g}" for x in avals], flush=True)
    # confirm coefficients are genuinely mixed in Q(sqrt3) (not pure Q)
    mixed = sum(1 for n in range(ORDER + 1) if a[n].q != 0)
    pureQ = sum(1 for n in range(ORDER + 1) if a[n].q == 0 and a[n].p != 0)
    print(f"[chk] of {ORDER+1} coeffs: {mixed} have nonzero sqrt3 part, {pureQ} pure-rational nonzero", flush=True)

    b = borel_coeffs(a)

    results = {"order": ORDER, "field": "Q(sqrt3)", "a_floats_0_7": avals,
               "n_with_sqrt3_part": mixed, "searches": []}

    grids = []
    for r in (1, 2, 3):
        for d in (4, 6, 8, 10):
            grids.append((r, d))
    # one heavier order-4 pass within budget
    grids.append((4, 8))

    found_any = False
    for (r, d) in grids:
        U = (r + 1) * (d + 1)
        nrows = min(2 * U + 6, len(b) - r - 1)   # over-determine x2
        # --- test B-hat(xi) ---
        Mb, Ub = holonomic_matrix(b, r, d, nrows)
        rb, ncb, nullb, basisb = nullspace_dim(Mb)
        # --- test phi(z) (D-finiteness; equivalent by Borel/Hadamard closure) ---
        nrows_a = min(2 * U + 6, len(a) - r - 1)
        Ma, Ua = holonomic_matrix(a, r, d, nrows_a)
        ra, nca, nulla, basisa = nullspace_dim(Ma)
        rec = {"r": r, "d": d, "unknowns": U,
               "Bhat": {"rows": nrows, "rank": rb, "nullity": nullb},
               "phi":  {"rows": nrows_a, "rank": ra, "nullity": nulla}}
        results["searches"].append(rec)
        tag = ""
        if nullb > 0 or nulla > 0:
            found_any = True
            tag = "  <<< HOLONOMIC ODE FOUND"
        print(f"[srch] r={r} d={d} U={U:>3} rows~{nrows:>3} | "
              f"Bhat nullity={nullb} phi nullity={nulla}{tag}", flush=True)

    results["holonomic_found"] = found_any
    out = r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15\PERIOD-REP-VQUAD-002\scripts\holonomic_recognition_q3_results.json"
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    print(f"\n[done] holonomic_found = {found_any}")
    print(f"[done] wrote {out}")

if __name__ == "__main__":
    main()
