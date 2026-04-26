"""T2B-RESONANCE-B8-12 — extend resonance search to b1 in {8..12}.

Sequel to T2B-RESONANCE-B67. Tests degree-(2,1) integer PCFs at
larger b1 magnitudes. Theoretically motivated target: b1=12,
a2=-35 (ratio -35/144, indicial roots {5/12, 7/12}, discriminant
25/144 a perfect rational square).

Pipeline matches T2B-RESONANCE-B67:
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=100, N=600, basis [1, L, L^2, L^3, L^4]
  Stage C : PSLQ dps=100, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]
            mandatory L-coefficient != 0 (phantom guard)

Halt conditions:
  * total enumerated > 500,000 -> abort
  * any Trans-class hit at ratio != -2/9 -> log + continue
    (deep-validate before declaring counterexample)

Coefficient envelope (REDUCED from prompt to satisfy halt rule):
  a2 in {-floor(b1^2/2), ..., floor(b1^2/2)} \ {0}
  b1 in {-12,-11,-10,-9,-8, 8,9,10,11,12}
  a1, a0, b0 in {-3, ..., 3}            <-- reduced from {-5..5}
  Total: 1016 (a2,b1) pairs * 7^3 = 348,488 families.
  (Original spec {-5..5} would give 1,352,296 -> blows halt cap.)
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

B1_MAGNITUDES = [8, 9, 10, 11, 12]
B1_VALUES = [-b for b in B1_MAGNITUDES] + B1_MAGNITUDES
COEFFS_FREE = list(range(-3, 4))  # 7 values; reduced from {-5..5}

N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 100
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10) ** (-40)
RESIDUAL_TOL_TRANS = mpf(10) ** (-30)

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "t2b_resonance_b8_12_results.json"
TARGETS_FILE = OUT_DIR / "t2b_resonance_b8_12_targets.json"


def enumerate_motivated_targets():
    """Step 1 — for each b1, find a2 with 1+4*(a2/b1^2) a rational square."""
    out = {}
    for b1 in B1_MAGNITUDES:
        amax = b1 * b1 // 2
        targets = []
        for a2 in range(-amax, amax + 1):
            if a2 == 0:
                continue
            disc = Fraction(b1 * b1 + 4 * a2, b1 * b1)
            num = disc.numerator
            den = disc.denominator
            # rational square iff numerator and denominator both squares
            # and disc >= 0
            if num < 0:
                continue
            sn = math.isqrt(num)
            sd = math.isqrt(den)
            if sn * sn == num and sd * sd == den:
                root_plus = Fraction(1, 2) + Fraction(sn, sd) / 2
                root_minus = Fraction(1, 2) - Fraction(sn, sd) / 2
                ratio = Fraction(a2, b1 * b1)
                targets.append({
                    "a2": a2,
                    "ratio": str(ratio),
                    "discriminant": str(disc),
                    "indicial_roots": [str(root_plus), str(root_minus)],
                    "worpitzky_interior": -Fraction(1, 4) < ratio < Fraction(1, 4),
                })
        out[b1] = targets
    return out


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
    families = []
    for b1 in B1_VALUES:
        amax = b1 * b1 // 2
        for a2 in range(-amax, amax + 1):
            if a2 == 0:
                continue
            for a1 in COEFFS_FREE:
                for a0 in COEFFS_FREE:
                    for b0 in COEFFS_FREE:
                        ratio = Fraction(a2, b1 * b1)
                        families.append((str(ratio), (a2, a1, a0, b1, b0)))
    return families


def run():
    t0 = time.time()
    targets = enumerate_motivated_targets()
    print("[STEP 1] Theoretically motivated targets (1+4r a rational square):")
    for b1, ts in targets.items():
        print(f"  b1={b1}: {len(ts)} target(s)")
        for t in ts:
            print(f"    a2={t['a2']:>5d}  ratio={t['ratio']:>8s}  "
                  f"disc={t['discriminant']:>8s}  roots={t['indicial_roots']}  "
                  f"worp_interior={t['worpitzky_interior']}")
    TARGETS_FILE.write_text(json.dumps(targets, indent=2, default=str))
    print(f"  Wrote {TARGETS_FILE}")

    families = enumerate_families()
    total = len(families)
    print(f"\n[STEP 2] Enumeration:")
    print(f"  b1 in {B1_VALUES}")
    print(f"  a2 in [-floor(b1^2/2), floor(b1^2/2)] nonzero")
    print(f"  a1,a0,b0 in {COEFFS_FREE[0]}..{COEFFS_FREE[-1]}")
    print(f"  TOTAL: {total} families")
    if total > 500_000:
        raise RuntimeError(f"HALT: > 500k families ({total})")

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

    print(f"\n[STEP 2B/C] PSLQ classification (dps={DPS_PSLQ}, N={N_PSLQ})")
    items = [(i, c[1]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"  Done in {t_bc:.1f}s")

    counts = {}
    by_b1 = {}
    by_ratio = {}
    trans_records = []
    log_records = []
    alg_records = []
    rat_records = []
    phantom_records = []
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        b1 = coeffs[3]
        by_b1.setdefault(b1, {})[label] = by_b1.get(b1, {}).get(label, 0) + 1
        by_ratio.setdefault(ratio, {})[label] = by_ratio.get(ratio, {}).get(label, 0) + 1
        rec = {"ratio": ratio, "coeffs": list(coeffs), "L": float(L), "info": info}
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
        "task": "T2B-RESONANCE-B8-12",
        "config": {
            "b1_values": B1_VALUES,
            "free_range": [COEFFS_FREE[0], COEFFS_FREE[-1]],
            "a2_range_per_b1": "[-floor(b1^2/2), floor(b1^2/2)] nonzero",
            "dps_pslq": DPS_PSLQ,
            "n_pslq": N_PSLQ,
            "n_stagea": N_STAGEA,
            "scope_reduction_note": "free range reduced from {-5..5} to {-3..3} to satisfy 500k halt cap",
        },
        "motivated_targets": targets,
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
        "alg_records_sample": alg_records[:50],
        "rat_records_sample": rat_records[:50],
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_FILE}")
    print(f"Counts: {counts}")
    print(f"By b1: {out['by_b1']}")
    if trans_records:
        print(f"\nTrans candidates ({len(trans_records)}):")
        for r in trans_records[:30]:
            print(f"  ratio={r['ratio']}  coeffs={r['coeffs']}  L={r['L']:.6g}")
    if log_records:
        print(f"\nLog candidates ({len(log_records)}):")
        for r in log_records[:30]:
            print(f"  ratio={r['ratio']}  coeffs={r['coeffs']}  L={r['L']:.6g}")
    print(f"Total wall time: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    run()
