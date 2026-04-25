"""
T2A-DEGREE42-SEARCH — Exhaustive search for Trans families at degree
profile (4,2) in F(4,3).

a(n) = a4*n^4 + a3*n^3 + a2*n^2 + a1*n + a0   (degree 4, a4 != 0)
b(n) = b2*n^2 + b1*n + b0                      (degree 2, b2 != 0)

Conjecture (2k-degree): Trans families at degree-(2k, k) profile have
a(n)/b(n)^2 -> const. For k=1, F(2,4) has 24 Trans families with
a2/b1^2 = -2/9 (or 1/4 for two exceptions). Predict: degree-(4,2)
Trans families with limits possibly involving pi^2 (Apery-like).

Classification (per task spec):
  Rat   - PSLQ finds rational L
  Alg   - PSLQ relation in {1, L, L^2, L^3, L^4} with L irrational
  Log   - PSLQ relation in {1, log2, log3, pi, pi^2, ...}
  Trans - no PSLQ hit in any of the above

Pipeline:
  Stage A: float64 cheap pre-screen, K_100, |K_100 - K_99| < 1e-4
  Stage B: mpmath dps=50, K_500, |K_500 - K_499| < 1e-8
  Stage C: PSLQ at dps=100 on survivors

Sign symmetry: K(a, b) negation symmetry => WLOG a4 > 0.
"""
from __future__ import annotations

import json
import math
import time
from itertools import product
from pathlib import Path

import mpmath as mp


# ── Configuration ────────────────────────────────────────────────────
CMAX = 1                   # |coeff| <= CMAX (stage 1 of CMAX-ladder)
ITER_FLOAT = 200           # cheap float64 pre-screen iterations
TOL_FLOAT = 1e-6
ITER_MP   = 500            # confirmation iterations at dps=50
DPS_CONFIRM = 50
TOL_MP   = mp.mpf("1e-25")
DPS_PSLQ = 100
PSLQ_HMAX = 10**12

OUT_JSON = Path("t2a_degree42_results.json")


# ── PCF iteration (forward recurrence, Lentz-Wallis) ─────────────────
def kn_float(a4, a3, a2, a1, a0, b2, b1, b0, N=ITER_FLOAT):
    """Compute K_N at float precision. Returns (K_N, K_{N-1}) or None
    on overflow / division-by-zero."""
    # b(0) = b0;  b(1) = b2+b1+b0;  a(1) = a4+a3+a2+a1+a0
    b_at_0 = float(b0)
    b_at_1 = float(b2 + b1 + b0)
    a_at_1 = float(a4 + a3 + a2 + a1 + a0)
    # P_0 = b(0), Q_0 = 1
    # P_1 = b(1)*b(0) + a(1),  Q_1 = b(1)
    P_prev2, P_prev1 = b_at_0, b_at_1 * b_at_0 + a_at_1
    Q_prev2, Q_prev1 = 1.0, b_at_1
    K_prev = K_curr = None
    for n in range(2, N + 1):
        an = a4*n*n*n*n + a3*n*n*n + a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        P_curr = bn * P_prev1 + an * P_prev2
        Q_curr = bn * Q_prev1 + an * Q_prev2
        try:
            mag = max(abs(P_curr), abs(Q_curr), 1.0)
            # rescale to avoid overflow
            if mag > 1e150:
                P_curr /= mag; Q_curr /= mag
                P_prev1 /= mag; Q_prev1 /= mag
            if Q_curr == 0.0:
                return None
            K_prev = K_curr
            K_curr = P_curr / Q_curr
        except (OverflowError, ZeroDivisionError):
            return None
        if not math.isfinite(K_curr):
            return None
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def kn_mp(a4, a3, a2, a1, a0, b2, b1, b0, N, dps):
    mp.mp.dps = dps
    b_at_0 = mp.mpf(b0)
    b_at_1 = mp.mpf(b2 + b1 + b0)
    a_at_1 = mp.mpf(a4 + a3 + a2 + a1 + a0)
    P_prev2 = b_at_0
    P_prev1 = b_at_1 * b_at_0 + a_at_1
    Q_prev2 = mp.mpf(1)
    Q_prev1 = b_at_1
    K_prev = K_curr = None
    for n in range(2, N + 1):
        an = a4*n*n*n*n + a3*n*n*n + a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        P_curr = bn * P_prev1 + an * P_prev2
        Q_curr = bn * Q_prev1 + an * Q_prev2
        if Q_curr == 0:
            return None
        K_prev = K_curr
        K_curr = P_curr / Q_curr
        # periodic rescaling
        if n % 16 == 0:
            mag = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
            P_curr = P_curr / mag
            Q_curr = Q_curr / mag
            P_prev1 = P_prev1 / mag
            Q_prev1 = Q_prev1 / mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


# ── Enumeration with symmetry: a4 > 0 ────────────────────────────────
def enumerate_families(cmax: int):
    a4_range = range(1, cmax + 1)                     # > 0 by symmetry
    a_range  = range(-cmax, cmax + 1)
    b2_range = [v for v in range(-cmax, cmax + 1) if v != 0]
    for a4 in a4_range:
        for a3, a2, a1, a0 in product(a_range, repeat=4):
            for b2 in b2_range:
                for b1, b0 in product(a_range, repeat=2):
                    yield (a4, a3, a2, a1, a0, b2, b1, b0)


def total_count(cmax):
    return cmax * (2*cmax+1)**4 * (2*cmax) * (2*cmax+1)**2


# ── Classification via PSLQ ──────────────────────────────────────────
def classify(L_mp):
    """Return (label, relation). Tries Rat, Alg, Log bases."""
    mp.mp.dps = DPS_PSLQ
    L = mp.mpf(L_mp)

    # Rat: PSLQ on [1, L]
    rel = mp.pslq([mp.mpf(1), L], maxcoeff=PSLQ_HMAX, tol=mp.mpf(10)**(-60))
    if rel is not None:
        return ("Rat", rel)

    # Alg: PSLQ on [1, L, L^2, L^3, L^4]
    basis_alg = [mp.mpf(1), L, L**2, L**3, L**4]
    rel = mp.pslq(basis_alg, maxcoeff=PSLQ_HMAX, tol=mp.mpf(10)**(-60))
    if rel is not None:
        # Confirm not a degenerate (e.g. L=0) hit
        return ("Alg", rel)

    # Log: PSLQ on [1, pi, pi^2, log2, log3, zeta3, Catalan]
    basis_log = [
        mp.mpf(1), mp.pi, mp.pi**2,
        mp.log(2), mp.log(3),
        mp.zeta(3), mp.catalan,
    ]
    # First check L itself in this basis
    rel = mp.pslq([L] + basis_log, maxcoeff=PSLQ_HMAX, tol=mp.mpf(10)**(-60))
    if rel is not None:
        return ("Log", rel)

    return ("Trans", None)


# ── Main search ──────────────────────────────────────────────────────
def main():
    cmax = CMAX
    total = total_count(cmax)
    print(f"[T2A] CMAX={cmax}, total={total} families")
    print(f"[T2A] Stage A: float64 prescreen K_{ITER_FLOAT}, tol={TOL_FLOAT}")

    t0 = time.time()
    survivors_A = []
    seen = 0
    for fam in enumerate_families(cmax):
        seen += 1
        out = kn_float(*fam)
        if out is None:
            continue
        Kn, Kn_1 = out
        if Kn_1 is None:
            continue
        if abs(Kn - Kn_1) < TOL_FLOAT and abs(Kn) < 1e6:
            survivors_A.append((fam, Kn))
        if seen % 20000 == 0:
            print(f"  [{seen}/{total}] survivors={len(survivors_A)} "
                  f"elapsed={time.time()-t0:.1f}s")

    tA = time.time() - t0
    print(f"[T2A] Stage A done: {seen} scanned, "
          f"{len(survivors_A)} survivors, {tA:.1f}s")

    # Stage B: mpmath confirmation
    print(f"[T2A] Stage B: mpmath dps={DPS_CONFIRM}, K_{ITER_MP}, tol={TOL_MP}")
    convergent = []
    t1 = time.time()
    for i, (fam, _Kfloat) in enumerate(survivors_A):
        try:
            out = kn_mp(*fam, N=ITER_MP, dps=DPS_CONFIRM)
        except Exception as e:
            print(f"  [B err] {fam}: {e}")
            continue
        if out is None:
            continue
        Kn, Kn_1 = out
        if Kn_1 is None:
            continue
        diff = abs(Kn - Kn_1)
        if diff < TOL_MP and abs(Kn) < mp.mpf("1e10"):
            convergent.append((fam, Kn, diff))
        if (i+1) % 500 == 0:
            print(f"  [{i+1}/{len(survivors_A)}] "
                  f"convergent={len(convergent)} "
                  f"elapsed={time.time()-t1:.1f}s")
    tB = time.time() - t1
    print(f"[T2A] Stage B done: {len(convergent)} convergent, {tB:.1f}s")

    # Stage C: classification
    print(f"[T2A] Stage C: PSLQ at dps={DPS_PSLQ}")
    results = []
    counts = {"Rat":0, "Alg":0, "Log":0, "Trans":0}
    t2 = time.time()
    for i, (fam, Kn, _diff) in enumerate(convergent):
        try:
            label, rel = classify(Kn)
        except Exception as e:
            label, rel = ("ERR", str(e))
        counts[label] = counts.get(label, 0) + 1
        a4, a3, a2, a1, a0, b2, b1, b0 = fam
        ratio = mp.mpf(a4) / (mp.mpf(b2)**2) if b2 != 0 else None
        rec = {
            "coeffs_a": [a4, a3, a2, a1, a0],
            "coeffs_b": [b2, b1, b0],
            "limit": mp.nstr(Kn, 30),
            "classification": label,
            "pslq_relation": [int(x) for x in rel] if rel and label != "ERR" else rel,
            "a_b2_ratio": mp.nstr(ratio, 20) if ratio is not None else None,
        }
        results.append(rec)
        if (i+1) % 200 == 0:
            print(f"  [{i+1}/{len(convergent)}] {counts} "
                  f"elapsed={time.time()-t2:.1f}s")
    tC = time.time() - t2
    print(f"[T2A] Stage C done: {counts}, {tC:.1f}s")

    summary = {
        "cmax": cmax,
        "total_families": total,
        "stage_a_survivors": len(survivors_A),
        "stage_b_convergent": len(convergent),
        "classification_counts": counts,
        "elapsed_sec": {"A": tA, "B": tB, "C": tC, "total": time.time()-t0},
        "results": results,
        "trans_families": [r for r in results if r["classification"] == "Trans"],
    }

    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"[T2A] Wrote {OUT_JSON} "
          f"({len(summary['trans_families'])} Trans families)")


if __name__ == "__main__":
    main()
