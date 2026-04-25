"""
T2A-CMAX2-RATIO — Expand degree-(4,2) PCF search to CMAX=2.

Tests whether the ratio a4/b2^2 is structural for Trans-hard families.
At CMAX=1 this ratio is trivially 1 (all leading coeffs are +-1).
At CMAX=2: a4 in {1,2}, b2 in {+-1,+-2}, so ratios {1/4, 1, 4} are
all possible.

Pipeline (same architecture as t2a_degree42_search.py):
  Stage A: float64 prescreen, K_200, |K_200 - K_199| < 1e-6
  Stage B: mpmath dps=50, K_500, |K_500 - K_499| < 1e-25
  Stage C: PSLQ at dps=100 against:
             basis_alg = [1, L, L^2, L^3, L^4]
             basis_log = [1, L, pi, L*pi, pi**2, L*pi**2,
                          log(2), L*log(2), zeta(3)]   (bilinear-pi)
           Phantom-hit defense: L-coefficient must be nonzero in any
           Log/Alg relation (zeta(2)=pi^2/6 trap).

Symmetry: K(a, b) sign symmetry => WLOG a4 > 0.
"""
from __future__ import annotations

import json
import math
import time
from itertools import product
from pathlib import Path

import mpmath as mp


# ── Configuration ────────────────────────────────────────────────────
CMAX = 2
ITER_FLOAT = 200
TOL_FLOAT = 1e-6
ITER_MP   = 500
DPS_CONFIRM = 50
TOL_MP   = mp.mpf("1e-25")
DPS_PSLQ = 100
PSLQ_HMAX = 10**12

OUT_JSON = Path("t2a_cmax2_results.json")


# ── PCF iteration (forward Wallis recurrence) ────────────────────────
def kn_float(a4, a3, a2, a1, a0, b2, b1, b0, N=ITER_FLOAT):
    b_at_0 = float(b0)
    b_at_1 = float(b2 + b1 + b0)
    a_at_1 = float(a4 + a3 + a2 + a1 + a0)
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
        if n % 16 == 0:
            mag = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
            P_curr = P_curr / mag
            Q_curr = Q_curr / mag
            P_prev1 = P_prev1 / mag
            Q_prev1 = Q_prev1 / mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def enumerate_families(cmax: int):
    """a4 > 0 by sign symmetry; b2 != 0 by degree-exactly-2."""
    a4_range = range(1, cmax + 1)
    a_range  = range(-cmax, cmax + 1)
    b2_range = [v for v in range(-cmax, cmax + 1) if v != 0]
    for a4 in a4_range:
        for a3, a2, a1, a0 in product(a_range, repeat=4):
            for b2 in b2_range:
                for b1, b0 in product(a_range, repeat=2):
                    yield (a4, a3, a2, a1, a0, b2, b1, b0)


def total_count(cmax):
    return cmax * (2*cmax+1)**4 * (2*cmax) * (2*cmax+1)**2


# ── Classification with phantom-hit defense ──────────────────────────
TOL_PSLQ = mp.mpf(10) ** (-60)


def _pslq_with_l(basis, l_index):
    """PSLQ requiring nonzero coefficient at l_index. Returns rel or None."""
    rel = mp.pslq(basis, maxcoeff=PSLQ_HMAX, tol=TOL_PSLQ)
    if rel is None:
        return None
    if int(rel[l_index]) == 0:
        return ("PHANTOM", rel)
    return rel


def classify(L_mp):
    """Return (label, relation, phantom_log).
    label in {Rat, Alg, Log-bilin, Trans-candidate}."""
    mp.mp.dps = DPS_PSLQ
    L = mp.mpf(L_mp)
    phantom_log = []

    # Rat: PSLQ on [1, L]; L coef at index 1
    rel = _pslq_with_l([mp.mpf(1), L], l_index=1)
    if rel is not None and not (isinstance(rel, tuple) and rel[0] == "PHANTOM"):
        return ("Rat", rel, phantom_log)
    if isinstance(rel, tuple) and rel[0] == "PHANTOM":
        phantom_log.append(("Rat", [int(x) for x in rel[1]]))

    # Alg: [1, L, L^2, L^3, L^4]; L coef at index 1
    basis_alg = [mp.mpf(1), L, L**2, L**3, L**4]
    rel = _pslq_with_l(basis_alg, l_index=1)
    if rel is not None and not (isinstance(rel, tuple) and rel[0] == "PHANTOM"):
        return ("Alg", rel, phantom_log)
    if isinstance(rel, tuple) and rel[0] == "PHANTOM":
        phantom_log.append(("Alg", [int(x) for x in rel[1]]))

    # Log-bilinear basis (NO zeta(2)/zeta(4) — phantom traps):
    # [L, 1, pi, L*pi, pi^2, L*pi^2, log(2), L*log(2), zeta(3)]
    pi = mp.pi
    log2 = mp.log(2)
    z3 = mp.zeta(3)
    basis_log = [L, mp.mpf(1), pi, L*pi, pi**2, L*pi**2,
                 log2, L*log2, z3]
    rel = _pslq_with_l(basis_log, l_index=0)
    if rel is not None and not (isinstance(rel, tuple) and rel[0] == "PHANTOM"):
        return ("Log-bilin", rel, phantom_log)
    if isinstance(rel, tuple) and rel[0] == "PHANTOM":
        phantom_log.append(("Log-bilin", [int(x) for x in rel[1]]))

    return ("Trans-candidate", None, phantom_log)


# ── Main search ──────────────────────────────────────────────────────
def main():
    cmax = CMAX
    total = total_count(cmax)
    print(f"[T2A-CMAX2] CMAX={cmax}, total={total} families")
    if total > 500_000:
        raise SystemExit(f"HALT: search space {total} > 500000")

    print(f"[T2A-CMAX2] Stage A: float64 K_{ITER_FLOAT}, tol={TOL_FLOAT}")
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
        if seen % 25000 == 0:
            print(f"  [{seen}/{total}] survivors={len(survivors_A)} "
                  f"elapsed={time.time()-t0:.1f}s")
    tA = time.time() - t0
    print(f"[T2A-CMAX2] Stage A done: {seen} scanned, "
          f"{len(survivors_A)} survivors, {tA:.1f}s")

    print(f"[T2A-CMAX2] Stage B: mpmath dps={DPS_CONFIRM} K_{ITER_MP}")
    convergent = []
    t1 = time.time()
    for i, (fam, _) in enumerate(survivors_A):
        try:
            out = kn_mp(*fam, N=ITER_MP, dps=DPS_CONFIRM)
        except Exception:
            continue
        if out is None:
            continue
        Kn, Kn_1 = out
        if Kn_1 is None:
            continue
        diff = abs(Kn - Kn_1)
        if diff < TOL_MP and abs(Kn) < mp.mpf("1e10"):
            convergent.append((fam, Kn, diff))
        if (i+1) % 1000 == 0:
            print(f"  [{i+1}/{len(survivors_A)}] "
                  f"convergent={len(convergent)} "
                  f"elapsed={time.time()-t1:.1f}s")
    tB = time.time() - t1
    print(f"[T2A-CMAX2] Stage B done: {len(convergent)} convergent, "
          f"{tB:.1f}s")

    # ── Dedup by L value (30 sig digits) before Stage C ─────────────
    print(f"[T2A-CMAX2] Stage B->C dedup by L value (30 dp)")
    dedup = {}  # key -> [(fam, Kn, diff), ...]
    for fam, Kn, diff in convergent:
        key = mp.nstr(Kn, 30)
        dedup.setdefault(key, []).append((fam, Kn, diff))
    unique_keys = list(dedup.keys())
    print(f"[T2A-CMAX2] Unique L values: {len(unique_keys)} "
          f"(from {len(convergent)} families)")

    print(f"[T2A-CMAX2] Stage C: PSLQ classify at dps={DPS_PSLQ}")
    results = []
    counts = {"Rat":0, "Alg":0, "Log-bilin":0, "Trans-candidate":0, "ERR":0}
    phantoms_total = 0
    t2 = time.time()
    label_cache = {}  # key -> (label, rel, phlog)
    for i, key in enumerate(unique_keys):
        fams_for_key = dedup[key]
        Kn = fams_for_key[0][1]
        try:
            label, rel, phlog = classify(Kn)
        except Exception as e:
            label, rel, phlog = ("ERR", str(e), [])
        label_cache[key] = (label, rel, phlog)
        # Replicate the result for every family with this L
        for fam, Kn_f, _diff in fams_for_key:
            counts[label] = counts.get(label, 0) + 1
            phantoms_total += len(phlog)
            a4, a3, a2, a1, a0, b2, b1, b0 = fam
            ratio = mp.mpf(a4) / (mp.mpf(b2)**2)
            rec = {
                "coeffs_a": [a4, a3, a2, a1, a0],
                "coeffs_b": [b2, b1, b0],
                "limit": mp.nstr(Kn_f, 30),
                "classification": label,
                "pslq_relation": ([int(x) for x in rel]
                                  if rel and label != "ERR"
                                     and not isinstance(rel, str)
                                  else rel),
                "phantoms_rejected": phlog,
                "a4_b2sq_ratio": float(ratio),
            }
            results.append(rec)
        if (i+1) % 200 == 0:
            print(f"  [unique {i+1}/{len(unique_keys)}] "
                  f"counts={counts} phantoms={phantoms_total} "
                  f"elapsed={time.time()-t2:.1f}s")
    tC = time.time() - t2
    print(f"[T2A-CMAX2] Stage C done: {counts}, "
          f"unique_L={len(unique_keys)}, "
          f"phantoms_rejected={phantoms_total}, {tC:.1f}s")

    summary = {
        "cmax": cmax,
        "total_families": total,
        "stage_a_survivors": len(survivors_A),
        "stage_b_convergent": len(convergent),
        "stage_c_unique_L": len(unique_keys),
        "classification_counts": counts,
        "phantoms_rejected_total": phantoms_total,
        "elapsed_sec": {"A": tA, "B": tB, "C": tC,
                        "total": time.time()-t0},
        "results": results,
    }
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"[T2A-CMAX2] Wrote {OUT_JSON}")
    n_trans = counts.get("Trans-candidate", 0)
    print(f"[T2A-CMAX2] Trans-candidates: {n_trans}")


if __name__ == "__main__":
    main()
