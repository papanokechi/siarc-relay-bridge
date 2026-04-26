"""T2B-RESONANCE-B67 — Extended resonance search at b1 in {-7,-6,6,7}.

Sequel to T2B-RESONANCE-SEARCH (b1 in {±4,±5}). Tests degree-(2,1)
integer PCFs with a2 in {-7,...,-1,1,...,7}, b1 in {-7,-6,6,7},
and a1,a0,b0 in {-7,...,7} for Trans/Log stratum membership.

Theoretically motivated targets (1+4*a2/b1^2 a rational square):
  b1=6, a2=-8: ratio -2/9 (already known) — out of a2 range here.
  b1=7, a2=-6: ratio -6/49, indicial roots {1/7, 6/7}.

Pipeline: same as T2B-RESONANCE-SEARCH:
  Stage A : float64 K_500 convergence filter (rel tol 1e-8)
  Stage B : PSLQ dps=100, N=600, basis [1, L, ..., L^4]  (Rat / Alg)
  Stage C : PSLQ dps=100, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]  (Trans / Log)
            mandatory L-coefficient != 0 (phantom prevention)

Phantom hit prevention: any PSLQ relation with the L-coefficient
zero is REJECTED. Logged as label="Phantom".

Halt conditions (per copilot-instructions.md):
  * Total enumerated > 500,000 -> abort.
  * Any Trans-class hit at ratio != -2/9 in Stage 2 -> log
    discrepancy and continue (deep-validate in Step 4 before
    declaring a counterexample).
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

# Sweep configuration
A2_VALUES = [v for v in range(-7, 8) if v != 0]          # 14 values
B1_VALUES = [-7, -6, 6, 7]                                # 4 values
COEFFS_FREE = list(range(-7, 8))                          # 15 values

N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 100
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10) ** (-40)
RESIDUAL_TOL_TRANS = mpf(10) ** (-30)

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "t2b_resonance_b67_results.json"


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
                Pc /= s
                Pp /= s
                Qc /= s
                Qp /= s
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
                Pc /= s
                Pp /= s
                Qc /= s
                Qp /= s
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

    rat_basis = [K ** j for j in range(5)]
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
    """Step 1: enumerate all (a2, a1, a0, b1, b0) in target ranges."""
    families = []
    for a2 in A2_VALUES:
        for b1 in B1_VALUES:
            for a1 in COEFFS_FREE:
                for a0 in COEFFS_FREE:
                    for b0 in COEFFS_FREE:
                        ratio = Fraction(a2, b1 * b1)
                        families.append((str(ratio), (a2, a1, a0, b1, b0)))
    return families


def run():
    t0 = time.time()
    families = enumerate_families()
    total = len(families)
    print(f"[STEP 1] Enumeration:")
    print(f"  a2 in {A2_VALUES}")
    print(f"  b1 in {B1_VALUES}")
    print(f"  a1,a0,b0 in {COEFFS_FREE[0]}..{COEFFS_FREE[-1]}")
    print(f"  TOTAL: {total} families")
    if total > 500_000:
        raise RuntimeError("HALT: > 500k families")

    # Stage A
    print(f"\n[STEP 2A] Stage A convergence filter (float64, K={N_STAGEA})")
    t_a = time.time()
    convergent = []
    last_pct = -1
    for i, (ratio, coeffs) in enumerate(families):
        if i % max(1, total // 20) == 0:
            pct = int(100 * i / total)
            if pct != last_pct:
                print(f"  Stage A progress: {pct}% ({i}/{total})", flush=True)
                last_pct = pct
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

    counts = {}
    trans_records = []
    log_records = []
    alg_records = []
    rat_records = []
    phantom_records = []
    by_b1 = {}
    by_ratio = {}

    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        b1 = coeffs[3]
        by_b1.setdefault(b1, {})
        by_b1[b1][label] = by_b1[b1].get(label, 0) + 1
        by_ratio.setdefault(ratio, {})
        by_ratio[ratio][label] = by_ratio[ratio].get(label, 0) + 1
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
        elif label == "Rat":
            rat_records.append(rec)
        elif label == "Phantom":
            phantom_records.append(rec)

    out = {
        "task": "T2B-RESONANCE-B67",
        "config": {
            "a2_values": A2_VALUES,
            "b1_values": B1_VALUES,
            "free_range": [COEFFS_FREE[0], COEFFS_FREE[-1]],
            "dps_pslq": DPS_PSLQ,
            "n_pslq": N_PSLQ,
            "n_stagea": N_STAGEA,
        },
        "total_families": total,
        "total_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "counts": counts,
        "by_b1": {str(k): v for k, v in by_b1.items()},
        "by_ratio": by_ratio,
        "trans_count": len(trans_records),
        "trans_records": trans_records,
        "log_count": len(log_records),
        "log_records": log_records,
        "alg_count": len(alg_records),
        "rat_count": len(rat_records),
        "phantom_count": len(phantom_records),
        "phantom_records": phantom_records,
        # Keep alg/rat as counts only to avoid bloat; sample first 50.
        "alg_records_sample": alg_records[:50],
        "rat_records_sample": rat_records[:50],
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_FILE}")
    print(f"Counts: {counts}")
    print(f"By b1: {out['by_b1']}")
    if trans_records:
        print(f"\nTrans candidates ({len(trans_records)}):")
        for r in trans_records[:20]:
            print(f"  ratio={r['ratio']}  coeffs={r['coeffs']}  L={r['L']:.6g}")
    if log_records:
        print(f"\nLog candidates ({len(log_records)}):")
        for r in log_records[:20]:
            print(f"  ratio={r['ratio']}  coeffs={r['coeffs']}  L={r['L']:.6g}")
    print(f"Total wall time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    run()
