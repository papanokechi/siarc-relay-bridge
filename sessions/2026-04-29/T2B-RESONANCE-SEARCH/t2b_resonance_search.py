"""T2B-RESONANCE-SEARCH — targeted falsification test for the
a2/b1^2 = -2/9 structural conjecture.

Targets (rationals r = a2/b1^2 with 1+4r a rational square, so the
indicial roots {x_+, x_-} are rational, like {1/3, 2/3} for r=-2/9):
    r = -3/16   b1 in {-4, +4}, a2 = -3   roots {1/4, 3/4}
    r = -4/25   b1 in {-5, +5}, a2 = -4   roots {1/5, 4/5}
    r = -6/25   b1 in {-5, +5}, a2 = -6   roots {2/5, 3/5}

Pipeline:
  Stage A: float64 K_500, tol=1e-8
  Stage B: PSLQ dps=100 vs rat basis [1,L,L^2,L^3,L^4]
  Stage C: PSLQ dps=100 vs bilinear-pi+log(2) basis,
           mandatory L-coefficient != 0
"""
import json
import time
import math
import multiprocessing as mp_proc
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

# Targets (a2, b1) with each (a2,b1) inducing the labelled ratio
TARGETS = {
    Fraction(-3, 16): [(-3, -4), (-3, 4)],
    Fraction(-4, 25): [(-4, -5), (-4, 5)],
    Fraction(-6, 25): [(-6, -5), (-6, 5)],
}

# Sweep ranges for the unconstrained slots
COEFFS_FULL = list(range(-5, 6))          # a1, a0, b0
N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 100
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10)**(-40)
RESIDUAL_TOL_TRANS = mpf(10)**(-30)

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "t2b_resonance_results.json"


def stage_a_converge_float(coeffs):
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
    idx, coeffs = item
    try:
        K = eval_pcf_mpmath(coeffs, N_PSLQ, DPS_PSLQ)
    except Exception as exc:
        return (idx, "eval_fail", {"error": str(exc)})
    if K is None:
        return (idx, "eval_fail", {})
    mp.dps = DPS_PSLQ
    K = mpf(K)

    rat_basis = [K**j for j in range(5)]
    try:
        rel = mpmath.pslq(rat_basis, maxcoeff=PSLQ_HMAX_RAT)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, rat_basis)))
        if residual < RESIDUAL_TOL_RAT:
            if all(int(c) == 0 for c in rel[2:]):
                return (idx, "Rat", {
                    "relation": [int(c) for c in rel],
                    "residual": float(residual),
                })
            return (idx, "Alg", {
                "relation": [int(c) for c in rel],
                "residual": float(residual),
            })

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
            L_coeff_indices = [1, 3, 5, 7]
            L_coeff_sum = sum(abs(int(rel[i])) for i in L_coeff_indices)
            if L_coeff_sum == 0:
                return (idx, "Phantom", {
                    "reason": "L-coefficient all zero",
                    "relation": [int(c) for c in rel],
                    "basis": basis_names,
                    "residual": float(residual),
                })
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


def enumerate_families():
    """Step 1: targeted enumeration."""
    families = []   # list of (ratio_str, coeffs)
    per_ratio_count = {}
    for ratio, ab_pairs in TARGETS.items():
        cnt = 0
        for (a2, b1) in ab_pairs:
            for a1 in COEFFS_FULL:
                for a0 in COEFFS_FULL:
                    for b0 in COEFFS_FULL:
                        families.append((str(ratio), (a2, a1, a0, b1, b0)))
                        cnt += 1
        per_ratio_count[str(ratio)] = cnt
    return families, per_ratio_count


def run():
    t0 = time.time()
    families, per_ratio = enumerate_families()
    total = len(families)
    print(f"[STEP 1] Targeted enumeration:")
    for r, c in per_ratio.items():
        print(f"  ratio {r:>6s}: {c} families")
    print(f"  TOTAL: {total} families")
    if total > 500_000:
        raise RuntimeError("HALT: > 500k families")

    # Stage A
    print(f"\n[STEP 2A] Stage A convergence filter (float64, K={N_STAGEA})")
    t_a = time.time()
    convergent = []
    for ratio, coeffs in families:
        L = stage_a_converge_float(coeffs)
        if L is not None:
            convergent.append((ratio, coeffs, L))
    t_a = time.time() - t_a
    print(f"  {len(convergent)}/{total} convergent in {t_a:.1f}s")

    # Stage B/C parallel
    print(f"\n[STEP 2B/C] PSLQ classification (dps={DPS_PSLQ}, N={N_PSLQ})")
    items = [(i, c[1]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"  Done in {t_bc:.1f}s")

    # Aggregate
    counts = {}
    by_ratio = {}
    trans_records = []
    log_records = []
    alg_records = []
    phantom_records = []
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        by_ratio.setdefault(ratio, {}).update({
            label: by_ratio.get(ratio, {}).get(label, 0) + 1
        })
        rec = {
            "ratio": ratio,
            "coeffs": list(coeffs),
            "L": float(L),
            "info": info,
        }
        if label == "Trans":
            trans_records.append(rec)
        elif label == "Log":
            log_records.append(rec)
        elif label == "Alg":
            alg_records.append(rec)
        elif label == "Phantom":
            phantom_records.append(rec)

    # Recompute proper by_ratio breakdown
    by_ratio = {r: {} for r in per_ratio}
    for (idx, label, info) in results:
        ratio = convergent[idx][0]
        by_ratio[ratio][label] = by_ratio[ratio].get(label, 0) + 1
    # add convergent count per ratio
    convergent_per_ratio = {r: 0 for r in per_ratio}
    for ratio, _, _ in convergent:
        convergent_per_ratio[ratio] += 1

    out = {
        "task": "T2B-RESONANCE-SEARCH",
        "targets": {str(k): v for k, v in TARGETS.items()},
        "per_ratio_total": per_ratio,
        "per_ratio_convergent": convergent_per_ratio,
        "per_ratio_breakdown": by_ratio,
        "total_families": total,
        "total_convergent": len(convergent),
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
    print(f"Per-ratio breakdown:")
    for r, brk in by_ratio.items():
        print(f"  {r:>6s}: {brk}")
    print(f"Total wall time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    run()
