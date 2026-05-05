"""T2B-RESONANCE-B67-B6-DISPATCH — b1=6 dispatch (2026-05-05).

Falsification test of the Trans-stratum ratio identity
  a2/b1^2 = -2/9
for degree-(2,1) integer PCFs at b1 = 6 only.

NOTE on prior context (cross-referenced before run):
  The 2026-04-29 session sessions/2026-04-29/T2B-RESONANCE-B67
  (commit 3445d43 + later staged a2={1..50} extension) already
  found a counterexample at b1=6:
    (a2,a1,a0,b1,b0) = (9,0,0,6,3); ratio = +1/4; L = 12/pi.
  Today's b1=6 dispatch is expected to RECONFIRM this finding,
  which constitutes the second independent run required by
  the standing E1 escalation rule.

Coefficient ordering: [a2, a1, a0] for the numerator polynomial
(leading-first, matches f1_base_computation.py / project memory).

Pipeline (matches T2B-B67 prior runs):
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=150, N=600, basis [1, L, L^2, L^3, L^4]
  Stage C : PSLQ dps=150, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]; phantom guard rejects any
            relation with all L-coefficients (indices 1,3,5,7) = 0.

Counterexample protocol:
  Any Trans hit -> deep verify dps=300 N=1500.
  Reconfirm requires residual < 1e-200 AND L-coeff != 0 in the
  deep-verified relation.

Coverage scope:
  a2 in {1..30}        # 30 values (covers a2=9 known C-Ex)
  b1 = 6               # dispatch focus
  a1, a0, b0 in {-5..5}  # 11 values each
  Total: 30 * 1 * 11**3 = 39,930 families
  (within prompt's 10k-50k target window).
"""
import json
import time
import math
import multiprocessing as mp_proc
import hashlib
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

A2_VALUES = list(range(1, 31))           # 1..30
B1_VALUES = [6]
COEFFS_FREE = list(range(-5, 6))         # -5..5

N_STAGEA = 500
TOL_STAGEA = 1e-8
DPS_PSLQ = 150
N_PSLQ = 600
PSLQ_HMAX_RAT = 10**6
PSLQ_HMAX_TRANS = 10**9
RESIDUAL_TOL_RAT = mpf(10) ** (-50)
RESIDUAL_TOL_TRANS = mpf(10) ** (-40)

DPS_DEEP = 300
N_DEEP = 1500

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "results_b6.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"


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
                    "L": mpmath.nstr(K, 30),
                    "relation": [int(c) for c in rel],
                    "residual": mpmath.nstr(residual, 6),
                })
            return (idx, "Alg", {
                "L": mpmath.nstr(K, 30),
                "relation": [int(c) for c in rel],
                "residual": mpmath.nstr(residual, 6),
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
                # Phantom — any relation with no L term is rejected (R3).
                return (idx, "Phantom", {
                    "L": mpmath.nstr(K, 30),
                    "reason": "L-coefficient all zero",
                    "relation": [int(c) for c in rel],
                    "basis": basis_names,
                    "residual": mpmath.nstr(residual, 6),
                })
            uses_log = any(int(rel[i]) != 0 for i in (6, 7))
            uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
            label = "Log" if (uses_log and not uses_pi) else "Trans"
            return (idx, label, {
                "L": mpmath.nstr(K, 30),
                "relation": [int(c) for c in rel],
                "basis": basis_names,
                "residual": mpmath.nstr(residual, 6),
            })
    return (idx, "Desert", {"L": mpmath.nstr(K, 20)})


def deep_verify(coeffs):
    K = eval_pcf_mpmath(coeffs, N_DEEP, DPS_DEEP)
    if K is None:
        return None
    mp.dps = DPS_DEEP
    pi_v = mp.pi
    ln2 = mp.log(2)
    trans_basis = [
        mpf(1), K, pi_v, K * pi_v, pi_v ** 2, K * pi_v ** 2, ln2, K * ln2,
    ]
    rel = mpmath.pslq(trans_basis, maxcoeff=PSLQ_HMAX_TRANS)
    if rel is None:
        return {"L": mpmath.nstr(K, 60), "relation": None}
    residual = abs(sum(r * b for r, b in zip(rel, trans_basis)))
    return {
        "L": mpmath.nstr(K, 60),
        "relation": [int(c) for c in rel],
        "residual": mpmath.nstr(residual, 8),
        "residual_lt_1e_200": residual < mpf(10) ** (-200),
    }


def enumerate_families():
    families = []
    for b1 in B1_VALUES:
        for a2 in A2_VALUES:
            ratio = Fraction(a2, b1 * b1)
            for a1 in COEFFS_FREE:
                for a0 in COEFFS_FREE:
                    for b0 in COEFFS_FREE:
                        families.append((str(ratio), (a2, a1, a0, b1, b0)))
    return families


def run():
    t0 = time.time()
    families = enumerate_families()
    total = len(families)
    print(f"[ENUM] b1={B1_VALUES}  a2={A2_VALUES[0]}..{A2_VALUES[-1]}  "
          f"free={COEFFS_FREE[0]}..{COEFFS_FREE[-1]}  total={total}")

    print(f"[STAGE A] float64 K={N_STAGEA} tol={TOL_STAGEA}")
    t_a = time.time()
    convergent = []
    step = max(1, total // 20)
    for i, (ratio, coeffs) in enumerate(families):
        if i % step == 0:
            print(f"  {100*i//total}%  ({i}/{total})", flush=True)
        L = stage_a_converge_float(coeffs)
        if L is not None:
            convergent.append((ratio, coeffs, L))
    t_a = time.time() - t_a
    print(f"[STAGE A] {len(convergent)}/{total} convergent in {t_a:.1f}s")

    print(f"[STAGE B/C] PSLQ dps={DPS_PSLQ} N={N_PSLQ}  workers...")
    items = [(i, c[1]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"[STAGE B/C] done in {t_bc:.1f}s")

    counts = {}
    by_ratio = {}
    trans_records = []
    log_records = []
    alg_records = []
    rat_records = []
    phantom_records = []
    eval_fail = []
    desert_count = 0
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        by_ratio.setdefault(ratio, {})
        by_ratio[ratio][label] = by_ratio[ratio].get(label, 0) + 1
        rec = {"ratio": ratio, "coeffs": list(coeffs), "L_float": float(L), "info": info}
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
        elif label == "eval_fail":
            eval_fail.append(rec)
        else:
            desert_count += 1

    halt_payload = None
    deep_results = []
    if trans_records:
        print(f"[HALT-CHECK] {len(trans_records)} Trans candidate(s); deep-verify")
        for r in trans_records:
            dv = deep_verify(tuple(r["coeffs"]))
            r["deep_verify"] = dv
            deep_results.append({"coeffs": r["coeffs"], "ratio": r["ratio"],
                                 "deep_verify": dv})
            print(f"  {r['coeffs']}  deep={dv}")
        confirmed = []
        for r in trans_records:
            dv = r["deep_verify"]
            if dv and dv.get("relation"):
                rel = dv["relation"]
                if any(int(rel[i]) != 0 for i in (1, 3, 5, 7)):
                    confirmed.append(r)
        if confirmed:
            halt_payload = {
                "reason": "Trans-stratum hit at positive ratio (counterexample to a2/b1^2 = -2/9)",
                "candidates": confirmed,
                "is_reconfirmation_of_2026_04_29_finding": any(
                    tuple(r["coeffs"]) == (9, 0, 0, 6, 3) for r in confirmed
                ),
            }

    halt_obj = halt_payload if halt_payload else {}
    HALT_FILE.write_text(json.dumps(halt_obj, indent=2))
    DISC_FILE.write_text("{}")
    UNEX_FILE.write_text(json.dumps({
        "log_records": log_records,
        "phantom_records": phantom_records,
    }, indent=2))

    out = {
        "task": "T2B-RESONANCE-B67-B6-DISPATCH",
        "config": {
            "b1_values": B1_VALUES,
            "a2_range": [A2_VALUES[0], A2_VALUES[-1]],
            "free_range": [COEFFS_FREE[0], COEFFS_FREE[-1]],
            "dps_pslq": DPS_PSLQ,
            "n_pslq": N_PSLQ,
            "n_stagea": N_STAGEA,
            "dps_deep": DPS_DEEP,
            "n_deep": N_DEEP,
            "phantom_guard": "L-coefficient (indices 1,3,5,7) must be nonzero (R3)",
            "scope_note": "a2>0 and b1>0 -> ratio>0; conjectured -2/9<0 unreachable, so any Trans hit is a counterexample",
        },
        "total_families": total,
        "total_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "counts": counts,
        "by_ratio": by_ratio,
        "trans_count": len(trans_records),
        "trans_records": trans_records,
        "log_count": len(log_records),
        "log_records": log_records,
        "alg_count": len(alg_records),
        "rat_count": len(rat_records),
        "phantom_count": len(phantom_records),
        "phantom_records": phantom_records,
        "eval_fail_count": len(eval_fail),
        "deep_verifications": deep_results,
        "halt_triggered": bool(halt_payload),
        "alg_records_sample": alg_records[:30],
        "rat_records_sample": rat_records[:30],
        "wall_seconds": round(time.time() - t0, 2),
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {RESULTS_FILE}")
    print(f"Counts: {counts}")
    print(f"Trans={len(trans_records)} Log={len(log_records)} Phantom={len(phantom_records)}")
    print(f"Total wall: {time.time() - t0:.1f}s")

    sha = hashlib.sha256(RESULTS_FILE.read_bytes()).hexdigest()
    print(f"results_b6.json SHA256: {sha}")


if __name__ == "__main__":
    run()
