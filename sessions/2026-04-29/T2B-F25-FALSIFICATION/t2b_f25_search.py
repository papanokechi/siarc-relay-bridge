"""T2B-F25-FALSIFICATION — Search F(2,5) for Trans-stratum families.

Pipeline:
  Stage A: float64 convergence filter, K=500, tol=1e-8
  Stage B: mpmath PSLQ at dps=100 against rat basis [1, L, L^2, L^3, L^4]
  Stage C: mpmath PSLQ at dps=100 against bilinear-pi basis
           [1, L, pi, L*pi, pi^2, L*pi^2, log(2), L*log(2)]
           Mandatory L-coefficient != 0 (phantom-hit prevention)

Reproducibility: dps and bases logged; runtime configurable via env.
"""
import json
import time
import math
import multiprocessing as mp_proc
from itertools import product
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

D = 5
COEFFS_NONZERO = [c for c in range(-D, D+1) if c != 0]
COEFFS_FULL = list(range(-D, D+1))
N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 100
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10)**(-40)
RESIDUAL_TOL_TRANS = mpf(10)**(-30)

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "t2b_f25_results.json"


def stage_a_converge_float(coeffs):
    """Iterate the PCF in float64 with rescaling. Returns L (float) if
    the value of P_n/Q_n stabilizes to within TOL_STAGEA over the last 50
    terms, else None.
    """
    a2, a1, a0, b1, b0 = coeffs
    Pp, Pc = 1.0, float(b0)
    Qp, Qc = 0.0, 1.0
    last_vals = []
    for n in range(1, N_STAGEA + 1):
        an = a2 * n * n + a1 * n + a0
        bn = b1 * n + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if not (math.isfinite(Pc) and math.isfinite(Qc)):
            return None
        if n % 50 == 0:
            s = abs(Qc) if abs(Qc) > 1.0 else 1.0
            if s > 1e100:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s
        if Qc == 0:
            return None
        if n >= N_STAGEA - 50:
            v = Pc / Qc
            if not math.isfinite(v):
                return None
            last_vals.append(v)
    if len(last_vals) < 20:
        return None
    arr = np.array(last_vals[-20:])
    spread = float(np.max(arr) - np.min(arr))
    mid = float(np.mean(arr))
    rel = spread / max(abs(mid), 1e-30)
    if rel < TOL_STAGEA:
        return mid
    return None


def eval_pcf_mpmath(coeffs, N, dps):
    mp.dps = dps + 50
    a2, a1, a0, b1, b0 = (mpf(c) for c in coeffs)
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    for n in range(1, N + 1):
        an = a2 * n * n + a1 * n + a0
        bn = b1 * n + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 50 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10) ** 20:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


def classify_pslq_worker(item):
    """Stage B + C. Input: (idx, coeffs_tuple). Returns (idx, label, info)."""
    idx, coeffs = item
    try:
        K = eval_pcf_mpmath(coeffs, N_PSLQ, DPS_PSLQ)
    except Exception as exc:
        return (idx, "eval_fail", {"error": str(exc)})
    if K is None:
        return (idx, "eval_fail", {})
    mp.dps = DPS_PSLQ
    K = mpf(K)

    # Stage B: rational basis [1, L, L^2, L^3, L^4]
    rat_basis = [K**j for j in range(5)]
    try:
        rel = mpmath.pslq(rat_basis, maxcoeff=PSLQ_HMAX_RAT)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, rat_basis)))
        if residual < RESIDUAL_TOL_RAT:
            # If only [1, L] relation present (rel[2:]=0) → pure Rat
            if all(int(c) == 0 for c in rel[2:]):
                return (idx, "Rat", {
                    "relation": [int(c) for c in rel],
                    "residual": float(residual),
                })
            # Higher-degree algebraic over Q
            return (idx, "Alg", {
                "relation": [int(c) for c in rel],
                "residual": float(residual),
            })

    # Stage C: bilinear-pi + log(2) basis with mandatory L-coefficient != 0
    pi_v = mp.pi
    ln2 = mp.log(2)
    trans_basis = [
        mpf(1), K, pi_v, K * pi_v, pi_v ** 2, K * pi_v ** 2, ln2, K * ln2,
    ]
    basis_names = ["1", "L", "pi", "L*pi", "pi^2", "L*pi^2", "log(2)", "L*log(2)"]
    try:
        rel = mpmath.pslq(trans_basis, maxcoeff=PSLQ_HMAX_TRANS)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, trans_basis)))
        if residual < RESIDUAL_TOL_TRANS:
            L_coeff_indices = [1, 3, 5, 7]  # indices with L factor
            L_coeff_sum = sum(abs(int(rel[i])) for i in L_coeff_indices)
            if L_coeff_sum == 0:
                return (idx, "Phantom", {
                    "reason": "L-coefficient all zero",
                    "relation": [int(c) for c in rel],
                    "basis": basis_names,
                    "residual": float(residual),
                })
            # Genuine relation expressing L as algebraic over {1, pi, pi^2, log2}
            # If only L coefficient (idx 1) and constant (idx 0) nonzero with
            # no log(2): classify as Log/Trans by which transcendentals appear
            uses_log = any(int(rel[i]) != 0 for i in (6, 7))
            uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
            if uses_log and not uses_pi:
                label = "Log"
            else:
                label = "Trans"
            return (idx, label, {
                "relation": [int(c) for c in rel],
                "basis": basis_names,
                "residual": float(residual),
            })

    return (idx, "Desert", {})


def stage_a_runner(coeffs_list):
    """Single-process Stage A; very fast in pure float64."""
    out = []
    for coeffs in coeffs_list:
        L = stage_a_converge_float(coeffs)
        if L is not None:
            out.append((coeffs, L))
    return out


def run():
    t0 = time.time()
    families = [
        (a2, a1, a0, b1, b0)
        for a2 in COEFFS_NONZERO
        for a1 in COEFFS_FULL
        for a0 in COEFFS_FULL
        for b1 in COEFFS_NONZERO
        for b0 in COEFFS_FULL
    ]
    total = len(families)
    print(f"Total candidate families: {total}")

    # Stage A
    t_a = time.time()
    convergent = []
    for coeffs in families:
        L = stage_a_converge_float(coeffs)
        if L is not None:
            convergent.append((coeffs, L))
    t_a = time.time() - t_a
    print(f"Stage A done: {len(convergent)}/{total} convergent in {t_a:.1f}s")

    if len(convergent) > 1_000_000:
        raise RuntimeError("HALT: > 1M convergent families")
    if len(convergent) == 0:
        raise RuntimeError("HALT: 0 convergent families")

    # Stage B + C: parallel PSLQ
    items = [(i, c[0]) for i, c in enumerate(convergent)]
    print(f"Stage B/C: PSLQ on {len(items)} families at dps={DPS_PSLQ}...")
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"Stage B/C done in {t_bc:.1f}s")

    # Aggregate
    counts = {}
    trans_records = []
    log_records = []
    alg_records = []
    phantom_records = []
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        coeffs, L = convergent[idx]
        rec = {"coeffs": list(coeffs), "L": float(L), "info": info,
               "ratio": str(Fraction(coeffs[0], coeffs[3] * coeffs[3]))}
        if label == "Trans":
            trans_records.append(rec)
        elif label == "Log":
            log_records.append(rec)
        elif label == "Alg":
            alg_records.append(rec)
        elif label == "Phantom":
            phantom_records.append(rec)

    out = {
        "task": "T2B-F25-FALSIFICATION",
        "D": D,
        "total_families": total,
        "stage_a_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "dps_pslq": DPS_PSLQ,
        "n_pslq": N_PSLQ,
        "counts": counts,
        "trans_count": len(trans_records),
        "trans_records": trans_records,
        "log_count": len(log_records),
        "log_records": log_records,
        "alg_count": len(alg_records),
        "alg_records": alg_records,
        "phantom_count": len(phantom_records),
        "phantom_records": phantom_records,
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_FILE}")
    print(f"Counts: {counts}")
    print(f"Total wall time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    run()
