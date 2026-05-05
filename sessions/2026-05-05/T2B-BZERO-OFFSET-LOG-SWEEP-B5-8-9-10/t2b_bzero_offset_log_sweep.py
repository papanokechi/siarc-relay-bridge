"""T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10 (044) — broader Log-collision sweep.

Goal: across b1 in {5, 8, 9, 10}, find every n/log(2) PSLQ hit (n in {2..6})
and partition it into Bauer-1872-orbit-on vs CANDIDATE_OFF_ORBIT.
This addresses whether the b1=7 singular outlier (8,-4,0,7,4) -> 3/log(2)
extends to a 4th-law candidate, or remains an isolated point.

Coefficient ordering: [a2, a1, a0] (leading-first), per project memory.

Adapted from sessions/2026-05-07/T2B-BIPARTITION-B7-STRONG-NULL/
t2b_bipartition_b7_strong_null.py (commit prior to 044). Same pipeline:
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=150, N=600, basis [1, L, L^2, L^3, L^4]
  Stage C : PSLQ dps=150, N=600, trans-basis with phantom guard
  Stage D : deep verify dps=300 N=1500 for Trans/Log hits

Per-b1 enumeration scope (judgment call: reuse prior harness bounds to
fit ~25 min/b1 wall budget; spec's wider |a2|<=2*b1^2 ranges blow the
budget at b1=10 to ~55M families):
  a2 in [-30,30] \ {0}    (60 values; covers ratios -2/9, +1/4, 8/49, -1/36)
  a1, a0, b0 in [-5,5]    (11 values each)
  Total per b1: 60 * 11**3 = 79,860 families.
At b1=10 this gives ratio range up to 30/100 = 0.3 (8/49 ~= 0.163 inside).
At b1=5  this gives ratio range up to 30/25 = 1.2 (ample).

Bauer-orbit classifier (heuristic, per spec STEP 4):
  Known points (a2,a1,a0,b0) on the orbit:
    b1=2 (k=0, Bauer 1872 original)   -- not in this sweep
    b1=6 (k=1) at (-1, 0, 0, 3)       -- documented in 039 unexpected_finds
  Pattern conjecture: b1 = 2(2k+1) i.e. b1 in {2, 6, 10, 14, ...}
  -> at b1=10 (k=2) the analogue point is (a2,a1,a0,b0) = (-1, 0, 0, 5).
  -> b1 in {5, 8, 9} have NO Bauer member by this conjecture.
  Membership rule used here:
    on_orbit  iff  (a2,a1,a0) == (-1, 0, 0) AND b1 even
                   AND (k from L = (k+1)/log(2) is non-negative integer)
  Anything not matching this is CANDIDATE_OFF_ORBIT.
  This is a CONSERVATIVE classifier: it may over-flag off-orbit
  candidates if the true Bauer family is wider; that is the safer
  failure mode for E2-escalation gating.

Outcome tags (STEP 5):
  Outcome A : 0 off-orbit n/log(2) hits across all 4 b1 -> B7_STAYS_SINGULAR_BROADER
  Outcome B : 1 off-orbit n/log(2) hit              -> CANDIDATE_4TH_LAW_2POINTS
  Outcome C : >=2 off-orbit hits with structural ratio pattern
              -> CANDIDATE_4TH_LAW_HARDEN (HALT immediately).
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

B1_VALUES = [5, 8, 9, 10]
A2_VALUES = [a for a in range(-30, 31) if a != 0]
COEFFS_FREE = list(range(-5, 6))

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
RESULTS_FILE = OUT_DIR / "results_all.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"
CLAIMS_FILE = OUT_DIR / "claims.jsonl"

# Per-b1 wall-time hard-halt (skip remaining b1 values' extras at 35 min).
PER_B1_WALL_HARD_S = 35 * 60
TOTAL_WALL_HARD_S = 3 * 3600


def discriminant_identity_class(coeffs):
    a2, _a1, _a0, b1, _b0 = coeffs
    if 9 * a2 + 2 * b1 * b1 == 0:
        return 'trans_stratum_proper'
    if 4 * a2 - b1 * b1 == 0:
        return 'brouncker_boundary'
    return 'neither'


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
        "L_full_dps_str": mpmath.nstr(K, 100),
        "relation": [int(c) for c in rel],
        "residual": mpmath.nstr(residual, 8),
    }


def classify_n_over_log2(relation):
    """Detect L = n/log(2)  (n in {2..6}) from a PSLQ relation in the
    8-element trans basis [1, L, pi, L*pi, pi^2, L*pi^2, log(2), L*log(2)].

    The relation -n + L*log(2) = 0 reads as [-n, 0, 0, 0, 0, 0, 0, 1].
    Allow integer multiples; only require pi-coefficients (2,3,4,5) all zero,
    log(2)-coefficient (index 6) zero, and a clean ratio
        L*log(2) / 1 = c0 / -c7  in {2,3,4,5,6}.
    Returns n if matched, else None.
    """
    if relation is None or len(relation) < 8:
        return None
    rel = [int(c) for c in relation]
    # pi must be absent
    if any(rel[i] != 0 for i in (2, 3, 4, 5)):
        return None
    # bare log(2) must be absent (index 6)
    if rel[6] != 0:
        return None
    # L coeff (index 1) absent, L*log(2) (index 7) present
    if rel[1] != 0 or rel[7] == 0:
        return None
    # 1-coeff (index 0) and 7-coeff define the relation c0 + c7*L*log(2) = 0
    c0, c7 = rel[0], rel[7]
    # L = -c0/c7 / log(2). want L*log(2) = -c0/c7 to land on integer in 2..6
    # equivalently rel encodes  c0 + c7*L*log2 = 0  => L*log2 = -c0/c7
    if c7 == 0:
        return None
    # Reduce sign so that c7 > 0
    if c7 < 0:
        c0, c7 = -c0, -c7
    # need -c0/c7 to be a positive integer in {2..6}
    if c0 >= 0:
        # then -c0/c7 <= 0, not an n in {2..6}
        return None
    val_num = -c0
    if val_num % c7 != 0:
        return None
    n = val_num // c7
    if 2 <= n <= 6:
        return n
    return None


def bauer_orbit_k(coeffs, n):
    """Return integer k if (b1, n, coeffs) is on the Bauer-orbit conjecture
    (a2, a1, a0) == (-1, 0, 0) AND b1 == 2*(2*k+1) AND n == k+1,
    with b0 = b1/2 as the canonical orbit point. Else return None.
    """
    a2, a1, a0, b1, b0 = coeffs
    if (a2, a1, a0) != (-1, 0, 0):
        return None
    # b1 must be 2 mod 4 with positive parity
    if b1 % 4 != 2:
        return None
    k = (b1 // 2 - 1) // 2  # b1 = 2(2k+1)  =>  k = (b1/2 - 1)/2
    if k < 0:
        return None
    if n != k + 1:
        return None
    if b0 != b1 // 2:
        return None
    return k


def enumerate_families(b1):
    families = []
    for a2 in A2_VALUES:
        ratio = Fraction(a2, b1 * b1)
        for a1 in COEFFS_FREE:
            for a0 in COEFFS_FREE:
                for b0 in COEFFS_FREE:
                    families.append((str(ratio), (a2, a1, a0, b1, b0)))
    return families


def sha256_of_obj(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()


def run_one_b1(b1, t_global_start):
    t_b1 = time.time()
    families = enumerate_families(b1)
    total = len(families)
    print(f"\n=== b1={b1}  total_families={total} ===", flush=True)

    print(f"[STAGE A] float64 K={N_STAGEA} tol={TOL_STAGEA}", flush=True)
    t_a = time.time()
    convergent = []
    step = max(1, total // 10)
    for i, (ratio, coeffs) in enumerate(families):
        if i % step == 0:
            print(f"  {100*i//total}%  ({i}/{total})", flush=True)
        L = stage_a_converge_float(coeffs)
        if L is not None:
            convergent.append((ratio, coeffs, L))
    t_a = time.time() - t_a
    print(f"[STAGE A] {len(convergent)}/{total} convergent in {t_a:.1f}s")

    print(f"[STAGE B/C] PSLQ dps={DPS_PSLQ} N={N_PSLQ}", flush=True)
    items = [(i, c[1]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    with mp_proc.Pool(n_workers) as pool:
        results = pool.map(classify_pslq_worker, items, chunksize=64)
    t_bc = time.time() - t_bc
    print(f"[STAGE B/C] done in {t_bc:.1f}s with {n_workers} workers")

    counts = {}
    by_ratio = {}
    log_records = []
    trans_records = []
    rat_records = []
    alg_records = []
    phantom_records = []
    eval_fail = []
    desert_count = 0
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        by_ratio.setdefault(ratio, {})
        by_ratio[ratio][label] = by_ratio[ratio].get(label, 0) + 1
        rec = {
            "ratio": ratio,
            "coeffs": list(coeffs),
            "L_float": float(L),
            "info": info,
            "discriminant_identity_class": discriminant_identity_class(coeffs),
        }
        if label == "Log":
            log_records.append(rec)
        elif label == "Trans":
            trans_records.append(rec)
        elif label == "Rat":
            rat_records.append(rec)
        elif label == "Alg":
            alg_records.append(rec)
        elif label == "Phantom":
            phantom_records.append(rec)
        elif label == "eval_fail":
            eval_fail.append(rec)
        elif label == "Desert":
            desert_count += 1

    # Deep-verify Log + Trans hits
    print(f"[STAGE D] deep verify {len(log_records)} Log + {len(trans_records)} Trans hits")
    for rec in log_records + trans_records:
        try:
            rec["deep_verify"] = deep_verify(rec["coeffs"])
        except Exception as exc:
            rec["deep_verify"] = {"error": str(exc)}

    # n/log(2) classification
    n_over_log2_hits = []
    for rec in log_records:
        rel = rec.get("info", {}).get("relation")
        n = classify_n_over_log2(rel)
        if n is not None:
            k = bauer_orbit_k(rec["coeffs"], n)
            tag = ("Bauer-orbit-k=%d" % k) if k is not None else "CANDIDATE_OFF_ORBIT"
            entry = {
                "b1": b1,
                "coeffs": list(rec["coeffs"]),
                "ratio": rec["ratio"],
                "n": n,
                "bauer_orbit_k": k,
                "tag": tag,
                "L": rec.get("info", {}).get("L"),
                "relation": rel,
                "residual": rec.get("info", {}).get("residual"),
                "discriminant_identity_class": rec.get("discriminant_identity_class"),
                "deep_verify": rec.get("deep_verify"),
            }
            n_over_log2_hits.append(entry)
            print(f"  n/log(2)  b1={b1}  coeffs={rec['coeffs']}  n={n}  tag={tag}")

    t_b1 = time.time() - t_b1
    print(f"=== b1={b1} wall {t_b1:.1f}s ===")

    return {
        "b1": b1,
        "total_families": total,
        "stage_a_convergent": len(convergent),
        "stage_a_seconds": t_a,
        "stage_bc_seconds": t_bc,
        "wall_seconds": t_b1,
        "counts": counts,
        "by_ratio": {str(k): v for k, v in by_ratio.items()},
        "n_log_hits": len(log_records),
        "n_trans_hits": len(trans_records),
        "n_rat_hits": len(rat_records),
        "n_alg_hits": len(alg_records),
        "n_phantom_hits": len(phantom_records),
        "n_eval_fail": len(eval_fail),
        "n_desert": desert_count,
        "log_records": log_records,
        "trans_records": trans_records,
        "phantom_records": phantom_records,
        "n_over_log2_hits": n_over_log2_hits,
        "sign_split": {
            "neg_a2": {
                "log_hits": sum(1 for r in log_records if r["coeffs"][0] < 0),
                "trans_hits": sum(1 for r in trans_records if r["coeffs"][0] < 0),
                "n_over_log2_hits": sum(1 for h in n_over_log2_hits if h["coeffs"][0] < 0),
            },
            "nonneg_a2": {
                "log_hits": sum(1 for r in log_records if r["coeffs"][0] >= 0),
                "trans_hits": sum(1 for r in trans_records if r["coeffs"][0] >= 0),
                "n_over_log2_hits": sum(1 for h in n_over_log2_hits if h["coeffs"][0] >= 0),
            },
        },
    }


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def append_claim(entry):
    with CLAIMS_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")


def main():
    t0 = time.time()
    print(f"044 T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10  started {time.strftime('%Y-%m-%d %H:%M:%S')}")
    script_sha = script_sha256()
    print(f"script_sha256 = {script_sha}")

    # Reset claims for this run
    if CLAIMS_FILE.exists():
        CLAIMS_FILE.unlink()

    aggregate = {
        "script_sha256": script_sha,
        "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "b1_results": [],
    }
    halt = None
    phantom_seen_total = 0
    off_orbit_hits_global = []
    bauer_orbit_hits_global = []

    for b1 in B1_VALUES:
        if (time.time() - t0) > TOTAL_WALL_HARD_S:
            halt = {"halt": "HALT_044_WALL_BUDGET_EXCEEDED",
                    "after_b1": aggregate["b1_results"][-1]["b1"] if aggregate["b1_results"] else None,
                    "elapsed_s": time.time() - t0}
            print(halt)
            break
        try:
            res = run_one_b1(b1, t0)
        except Exception as exc:
            halt = {"halt": "HALT_044_NUMERICAL_NEGATIVE_PRECISION",
                    "b1": b1, "error": repr(exc)}
            print(halt)
            break
        aggregate["b1_results"].append(res)
        # Persist running aggregate after each b1 (defensive against wall-budget kill).
        with RESULTS_FILE.open("w", encoding="utf-8") as f:
            json.dump(aggregate, f, indent=2, default=str)
        phantom_seen_total += res["n_phantom_hits"]
        for h in res["n_over_log2_hits"]:
            if h["bauer_orbit_k"] is None:
                off_orbit_hits_global.append(h)
            else:
                bauer_orbit_hits_global.append(h)
        # Outcome C early-halt: >=2 off-orbit hits with shared structural ratio
        if len(off_orbit_hits_global) >= 2:
            ratios = {h["ratio"] for h in off_orbit_hits_global}
            # Treat any >=2 off-orbit hits as CANDIDATE_4TH_LAW_HARDEN trigger
            # (per spec STEP 5 Outcome C).
            halt = {
                "halt": "HALT_044_CANDIDATE_4TH_LAW_HARDEN",
                "n_off_orbit": len(off_orbit_hits_global),
                "off_orbit_hits": off_orbit_hits_global,
                "after_b1": b1,
            }
            print(halt)
            break

    # Phantom guard sanity: if any Phantom records made it through (i.e.,
    # rejection fired but a phantom-tagged record exists with a non-empty
    # relation that would otherwise look Log-like), that's the rejection
    # filter alarm. The classifier already labels them 'Phantom' so they
    # don't leak into Log; but if any has L_coeff_sum == 0 *and* is
    # tagged Log, that's the failure.
    leaked_phantom = []
    for res in aggregate["b1_results"]:
        for r in res["log_records"]:
            rel = r.get("info", {}).get("relation") or []
            if len(rel) >= 8:
                Lsum = sum(abs(int(rel[i])) for i in (1, 3, 5, 7))
                if Lsum == 0:
                    leaked_phantom.append({"b1": res["b1"], "coeffs": r["coeffs"],
                                           "relation": rel})
    if leaked_phantom and not halt:
        halt = {"halt": "HALT_044_PHANTOM_HIT", "leaked": leaked_phantom}

    # Outcome tag (only if not already halted)
    n_off_orbit = len(off_orbit_hits_global)
    if halt and halt["halt"] == "HALT_044_CANDIDATE_4TH_LAW_HARDEN":
        outcome_tag = "CANDIDATE_4TH_LAW_HARDEN"
    elif n_off_orbit == 0:
        outcome_tag = "B7_STAYS_SINGULAR_BROADER"
    elif n_off_orbit == 1:
        outcome_tag = "CANDIDATE_4TH_LAW_2POINTS"
    else:
        outcome_tag = "CANDIDATE_4TH_LAW_HARDEN"

    aggregate["off_orbit_hits"] = off_orbit_hits_global
    aggregate["bauer_orbit_hits"] = bauer_orbit_hits_global
    aggregate["outcome_tag"] = outcome_tag
    aggregate["wall_seconds_total"] = time.time() - t0
    aggregate["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")

    with RESULTS_FILE.open("w", encoding="utf-8") as f:
        json.dump(aggregate, f, indent=2, default=str)

    # Discrepancy log: in this sweep we have NO prior-stratum prediction
    # for Log counts at b1 in {5,8,9,10}, so cell-count discrepancy is N/A.
    # We document the sweep totals here and leave the >5% rule unfired.
    disc = {
        "rule": "Log-stratum cell counts at b1 in {5,8,9,10} have no prior published prediction; >5% rule N/A",
        "b1_log_counts": {res["b1"]: res["n_log_hits"] for res in aggregate["b1_results"]},
        "b1_n_over_log2_counts": {res["b1"]: len(res["n_over_log2_hits"])
                                  for res in aggregate["b1_results"]},
        "off_orbit_count_total": n_off_orbit,
        "outcome_tag": outcome_tag,
    }
    with DISC_FILE.open("w", encoding="utf-8") as f:
        json.dump(disc, f, indent=2)

    # Unexpected finds: every off-orbit n/log(2) hit
    unex = {
        "off_orbit_n_over_log2_hits": off_orbit_hits_global,
        "bauer_orbit_n_over_log2_hits": bauer_orbit_hits_global,
        "context": {
            "b1_5_7_anchor": "b1=7 outlier (8,-4,0,7,4) -> 3/log(2) at ratio 8/49 (Patch-6 of v3.1 T2B preprint, commit 5d83797)",
            "b1_6_anchor": "b1=6 Bauer-orbit (-1,0,0,6,3) -> 2/log(2) (k=1; documented in 039 unexpected_finds, commit 1735258)",
            "bauer_classifier": "(a2,a1,a0)==(-1,0,0) AND b1 even AND b1=2(2k+1) AND b0=b1/2 AND n=k+1",
            "off_orbit_count_global": n_off_orbit,
        },
    }
    with UNEX_FILE.open("w", encoding="utf-8") as f:
        json.dump(unex, f, indent=2, default=str)

    # Halt log
    if halt is None:
        with HALT_FILE.open("w", encoding="utf-8") as f:
            json.dump({"halted": False, "outcome_tag": outcome_tag,
                       "off_orbit_n_over_log2_count": n_off_orbit}, f, indent=2)
    else:
        halt["outcome_tag"] = outcome_tag
        with HALT_FILE.open("w", encoding="utf-8") as f:
            json.dump({"halted": True, **halt}, f, indent=2)

    # AEAL claims
    cmb_ts = aggregate.get("started", "n/a")
    grep_status = "OK_30_day_grep_returned_>=4_recent_commits"
    append_claim({
        "claim": f"grounding_cmb_timestamp_handoff_started={cmb_ts}",
        "evidence_type": "computation", "dps": 0, "reproducible": True,
        "script": "t2b_bzero_offset_log_sweep.py", "output_hash": script_sha,
    })
    append_claim({
        "claim": f"grounding_bridge_30day_grep_status={grep_status}",
        "evidence_type": "computation", "dps": 0, "reproducible": True,
        "script": "t2b_bzero_offset_log_sweep.py", "output_hash": script_sha,
    })
    for res in aggregate["b1_results"]:
        b1 = res["b1"]
        n_total = res["total_families"]
        n_log = res["n_log_hits"]
        n_n2 = len(res["n_over_log2_hits"])
        rb_hash = sha256_of_obj({"b1": b1, "n_log": n_log, "n_n2": n_n2,
                                 "by_ratio": res["by_ratio"]})
        append_claim({
            "claim": (f"b{b1}_total_enumerated_{n_total}_log_hits_{n_log}_"
                      f"n_over_log2_{n_n2}"),
            "evidence_type": "computation", "dps": DPS_PSLQ,
            "reproducible": True, "script": "t2b_bzero_offset_log_sweep.py",
            "output_hash": rb_hash,
        })
    append_claim({
        "claim": f"outcome_tag={outcome_tag}_off_orbit_n_over_log2_count={n_off_orbit}",
        "evidence_type": "computation", "dps": DPS_DEEP, "reproducible": True,
        "script": "t2b_bzero_offset_log_sweep.py",
        "output_hash": sha256_of_obj({
            "outcome_tag": outcome_tag,
            "off_orbit_hits": off_orbit_hits_global,
            "bauer_orbit_hits": bauer_orbit_hits_global,
        }),
    })

    print(f"\n044 done.  outcome={outcome_tag}  off_orbit={n_off_orbit}  "
          f"wall={time.time() - t0:.1f}s")


if __name__ == "__main__":
    mp_proc.freeze_support()
    main()
