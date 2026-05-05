"""T2B-BIPARTITION-B7-STRONG-NULL — b1=7 strong-null falsification dispatch.

Wednesday 2026-05-07 (Day 3 of W19). Pre-registered binary outcome:
the preprint-stated bipartition (PCF-2 v1.3, DOI 10.5281/zenodo.19783312)
predicts ZERO Trans-stratum hits at b1=7 in either L- or L+ locus,
since neither L- (a2 = -2 b1^2 / 9 = -98/9) nor L+ (a2 = b1^2 / 4 = 49/4)
admits an integer-coefficient family at b1=7 (9 nmid 49 and 4 nmid 49).

Provenance:
  Source: synth concurrence 2026-05-05 ~10:55 JST ("Wed b1=7 strong-null
        dispatch active... cleanest experiment of the week").
  Template: T2B-BIPARTITION-B6-VERIFICATION (commit 1735258), single
        change b1=6 -> b1=7 plus verdict logic redirected to strong-null.

Coefficient ordering: [a2, a1, a0] for the numerator polynomial
(leading-first, matches f1_base_computation.py / project memory).

Pipeline (mirrors b6):
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=150, N=600, basis [1, L, L^2, L^3, L^4]
  Stage C : PSLQ dps=150, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]; phantom guard rejects any
            relation with all L-coefficients (indices 1,3,5,7) = 0.
  Stage D : deep-verify dps=300 N=1500 for any Trans / Log hit.

Classifier upgrade carried over from b1=6 dispatch:
  For every Trans/Log hit, compute discriminant_identity_class:
    trans_stratum_proper  -- 9*a2 + 2*b1^2 == 0  (a2/b1^2 = -2/9)
    brouncker_boundary    -- 4*a2 -   b1^2 == 0  (a2/b1^2 = +1/4)
    neither               -- any other ratio
  At b1=7 with integer a2 in [-30,30], NEITHER identity can fire
  (98/9 and 49/4 are non-integer), so the strong-null prediction
  is: zero Trans hits total. ANY Trans hit at b1=7 lands in
  'neither' and is candidate falsification.

Verdict labels (post-analysis, written into halt_log.json):
  STRONG_NULL_HOLDS   -- n_trans_total == 0; bipartition gets third
                         independent confirmation across b1 in {5,6,7}.
  WEAK_TRANS_FOUND    -- n_trans_total >= 1, every Trans hit has
                         dps=300 residual >= 1e-200 (marginal).
  STRONG_NULL_FAILED  -- n_trans_total >= 1, at least one Trans hit
                         has dps=300 residual < 1e-200. HARD HALT;
                         pre-registered binary outcome falsified.

U1-class collision diagnostic (informational, not verdict-bearing):
  If a Log hit and a Trans hit at b1=7 share the same numerical L
  value AND the same PSLQ relation, log to unexpected_finds.json.

Coverage scope:
  a2 in {-30..-1} U {1..30}   # 60 values (excludes a2=0)
  b1 = 7                      # dispatch focus
  a1, a0, b0 in {-5..5}       # 11 values each
  Total: 60 * 1 * 11**3 = 79,860 families
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

A2_VALUES = [a for a in range(-30, 31) if a != 0]
B1_VALUES = [7]
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
RESIDUAL_HARD_FAIL = mpf(10) ** (-200)  # falsification threshold

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "results_b7.json"
PARTITION_FILE = OUT_DIR / "identity_partition_table.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"
CLAIMS_FILE = OUT_DIR / "claims.jsonl"


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
        "residual_lt_1e_200": bool(residual < RESIDUAL_HARD_FAIL),
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


def determine_verdict(trans_records):
    """Strong-null verdict logic for b1=7.

    STRONG_NULL_HOLDS    : n_trans_total == 0
    WEAK_TRANS_FOUND     : >=1 Trans hit, all dps=300 residuals >= 1e-200
    STRONG_NULL_FAILED   : >=1 Trans hit with dps=300 residual < 1e-200
    """
    n = len(trans_records)
    if n == 0:
        return "STRONG_NULL_HOLDS", {"n_trans_total": 0}
    confirmed = []
    marginal = []
    for r in trans_records:
        dv = r.get("deep_verify") or {}
        if dv.get("residual_lt_1e_200"):
            confirmed.append(r)
        else:
            marginal.append(r)
    if confirmed:
        return "STRONG_NULL_FAILED", {
            "n_trans_total": n,
            "n_confirmed_lt_1e_200": len(confirmed),
            "confirmed_hits": [
                {
                    "coeffs": r["coeffs"],
                    "ratio": r["ratio"],
                    "discriminant_identity_class": r.get("discriminant_identity_class"),
                    "deep_verify": r.get("deep_verify"),
                }
                for r in confirmed
            ],
        }
    return "WEAK_TRANS_FOUND", {
        "n_trans_total": n,
        "n_marginal": len(marginal),
        "marginal_hits": [
            {
                "coeffs": r["coeffs"],
                "ratio": r["ratio"],
                "discriminant_identity_class": r.get("discriminant_identity_class"),
                "deep_verify": r.get("deep_verify"),
            }
            for r in marginal
        ],
    }


def detect_u1_collisions(trans_records, log_records, tol_dps=20):
    """Identify Log/Trans pairs that share the same L value AND PSLQ relation.

    Returns list of collision dicts.
    """
    collisions = []
    mp.dps = 60
    # Build comparable signature: numeric L (mpf at dps=60) + sorted relation tuple.
    def parse(rec):
        info = rec.get("info", {})
        L_str = info.get("L")
        rel = tuple(info.get("relation") or [])
        try:
            L = mpf(L_str) if L_str is not None else None
        except Exception:
            L = None
        return L, rel
    for tr in trans_records:
        L_t, rel_t = parse(tr)
        if L_t is None:
            continue
        for lr in log_records:
            L_l, rel_l = parse(lr)
            if L_l is None:
                continue
            if rel_t and rel_l and rel_t == rel_l:
                if abs(L_t - L_l) < mpf(10) ** (-tol_dps):
                    collisions.append({
                        "trans_pcf": tr["coeffs"],
                        "trans_ratio": tr["ratio"],
                        "log_pcf": lr["coeffs"],
                        "log_ratio": lr["ratio"],
                        "shared_relation": list(rel_t),
                        "shared_L": mpmath.nstr(L_t, 30),
                    })
    return collisions


def sha256_of_obj(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()


def run():
    t0 = time.time()
    families = enumerate_families()
    total = len(families)
    print(f"[ENUM] b1={B1_VALUES}  a2={A2_VALUES[0]}..{A2_VALUES[-1]} (excl 0)  "
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
    print(f"[STAGE B/C] done in {t_bc:.1f}s with {n_workers} workers")

    counts = {}
    by_ratio = {}
    by_identity_class_trans = {}
    by_identity_class_log = {}
    trans_records = []
    log_records = []
    alg_records = []
    rat_records = []
    phantom_records = []
    eval_fail = []
    desert_count = 0
    max_residual = mpf(0)
    for (idx, label, info) in results:
        counts[label] = counts.get(label, 0) + 1
        ratio, coeffs, L = convergent[idx]
        by_ratio.setdefault(ratio, {})
        by_ratio[ratio][label] = by_ratio[ratio].get(label, 0) + 1
        rec = {"ratio": ratio, "coeffs": list(coeffs), "L_float": float(L), "info": info}
        if "residual" in info:
            try:
                r_v = mpf(info["residual"])
                if r_v > max_residual:
                    max_residual = r_v
            except Exception:
                pass
        if label == "Trans":
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
            by_identity_class_trans[ic] = by_identity_class_trans.get(ic, 0) + 1
            trans_records.append(rec)
        elif label == "Log":
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
            by_identity_class_log[ic] = by_identity_class_log.get(ic, 0) + 1
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

    deep_results_trans = []
    if trans_records:
        print(f"[STAGE D] {len(trans_records)} Trans candidate(s); deep-verify dps={DPS_DEEP} N={N_DEEP}")
        for r in trans_records:
            dv = deep_verify(tuple(r["coeffs"]))
            r["deep_verify"] = dv
            deep_results_trans.append({
                "coeffs": r["coeffs"], "ratio": r["ratio"],
                "discriminant_identity_class": r.get("discriminant_identity_class"),
                "deep_verify": dv,
            })
            print(f"  TRANS {r['coeffs']}  ratio={r['ratio']}  ic={r.get('discriminant_identity_class')}  deep={dv}")

    deep_results_log = []
    if log_records:
        print(f"[STAGE D-LOG] {len(log_records)} Log candidate(s) (diagnostic); deep-verify dps={DPS_DEEP} N={N_DEEP}")
        for r in log_records:
            dv = deep_verify(tuple(r["coeffs"]))
            r["deep_verify"] = dv
            deep_results_log.append({
                "coeffs": r["coeffs"], "ratio": r["ratio"],
                "discriminant_identity_class": r.get("discriminant_identity_class"),
                "deep_verify": dv,
            })
            print(f"  LOG   {r['coeffs']}  ratio={r['ratio']}  ic={r.get('discriminant_identity_class')}  deep={dv}")

    # U1-class collision detection (b1=7 analogue of b1=6 U1 anomaly)
    collisions = detect_u1_collisions(trans_records, log_records)

    # Counters per Step 5 of relay
    n_trans_total = len(trans_records)
    n_trans_on_L_minus = by_identity_class_trans.get('trans_stratum_proper', 0)
    n_trans_on_L_plus = by_identity_class_trans.get('brouncker_boundary', 0)
    n_trans_on_other = by_identity_class_trans.get('neither', 0)

    verdict_label, verdict_evidence = determine_verdict(trans_records)
    print(f"[VERDICT] {verdict_label}")
    print(f"  n_trans_total={n_trans_total}")
    print(f"  n_trans_on_L_minus={n_trans_on_L_minus} (predicted 0)")
    print(f"  n_trans_on_L_plus ={n_trans_on_L_plus} (predicted 0)")
    print(f"  n_trans_on_other  ={n_trans_on_other}")
    print(f"  n_log_total       ={len(log_records)}")
    print(f"  n_u1_collisions   ={len(collisions)}")

    # ---- Identity partition table (verdict summary) ----
    partition_table = {
        "task": "T2B-BIPARTITION-B7-STRONG-NULL",
        "b1": 7,
        "n_trans_total": n_trans_total,
        "n_trans_on_L_minus": n_trans_on_L_minus,
        "n_trans_on_L_plus": n_trans_on_L_plus,
        "n_trans_on_other": n_trans_on_other,
        "n_log_total": len(log_records),
        "n_u1_collisions": len(collisions),
        "verdict_label": verdict_label,
        "predicted_loci_at_b1_eq_7": {
            "L_minus": {"required_a2": "-98/9", "integer": False},
            "L_plus":  {"required_a2": "49/4",  "integer": False},
        },
        "strong_null_prediction": "n_trans_total == 0 (no integer-coefficient family at b1=7 hits either locus)",
        "epistemic_note": (
            "STRONG_NULL_HOLDS is consistent with the bipartition claim and "
            "supports its extension to b1=7; it does not 'prove' or 'establish' "
            "the bipartition (R7/_RULES.txt §D)."
        ),
    }
    PARTITION_FILE.write_text(json.dumps(partition_table, indent=2, default=str))

    # ---- halt_log.json ----
    if verdict_label == "STRONG_NULL_FAILED":
        halt_obj = {
            "verdict_label": verdict_label,
            "halt_triggered": True,
            "halt_code": "H3_STRONG_NULL_FAILED",
            "verdict_evidence": verdict_evidence,
            "n_trans_total": n_trans_total,
            "n_trans_on_L_minus": n_trans_on_L_minus,
            "n_trans_on_L_plus": n_trans_on_L_plus,
            "n_trans_on_other": n_trans_on_other,
            "preprint_doi_audited": "10.5281/zenodo.19783312",
        }
    else:
        halt_obj = {}
    HALT_FILE.write_text(json.dumps(halt_obj, indent=2, default=str))
    DISC_FILE.write_text("{}")

    # ---- unexpected_finds.json (always emitted) ----
    UNEX_FILE.write_text(json.dumps({
        "u1_class_collisions": collisions,
        "log_records": log_records,
        "phantom_records": phantom_records,
        "note": (
            "Log records logged as diagnostic per relay 040 Step 4. "
            "U1-class collision = Log+Trans share L value AND PSLQ relation."
        ),
    }, indent=2, default=str))

    # ---- results_b7.json ----
    out = {
        "task": "T2B-BIPARTITION-B7-STRONG-NULL",
        "config": {
            "b1_values": B1_VALUES,
            "a2_range": [A2_VALUES[0], A2_VALUES[-1]],
            "a2_excludes_zero": True,
            "a2_count": len(A2_VALUES),
            "free_range": [COEFFS_FREE[0], COEFFS_FREE[-1]],
            "dps_pslq": DPS_PSLQ,
            "n_pslq": N_PSLQ,
            "n_stagea": N_STAGEA,
            "dps_deep": DPS_DEEP,
            "n_deep": N_DEEP,
            "residual_hard_fail_threshold": "1e-200",
            "phantom_guard": "L-coefficient (indices 1,3,5,7) must be nonzero (R3)",
            "classifier_upgrade": (
                "discriminant_identity_class in {trans_stratum_proper, "
                "brouncker_boundary, neither} computed for every Trans/Log hit"
            ),
            "scope_note": (
                "a2 in [-30,30]\\{0}, b1=7: neither L- (a2=-98/9) nor L+ "
                "(a2=49/4) is integer-realizable; strong-null predicts "
                "zero Trans hits."
            ),
        },
        "total_families": total,
        "total_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "max_residual_stage_bc": mpmath.nstr(max_residual, 6),
        "counts": counts,
        "by_ratio": by_ratio,
        "by_identity_class_trans": by_identity_class_trans,
        "by_identity_class_log": by_identity_class_log,
        "trans_count": n_trans_total,
        "trans_records": trans_records,
        "log_count": len(log_records),
        "log_records": log_records,
        "alg_count": len(alg_records),
        "rat_count": len(rat_records),
        "phantom_count": len(phantom_records),
        "phantom_records": phantom_records,
        "eval_fail_count": len(eval_fail),
        "desert_count": desert_count,
        "deep_verifications_trans": deep_results_trans,
        "deep_verifications_log": deep_results_log,
        "u1_class_collisions": collisions,
        "n_trans_on_L_minus": n_trans_on_L_minus,
        "n_trans_on_L_plus": n_trans_on_L_plus,
        "n_trans_on_other": n_trans_on_other,
        "verdict_label": verdict_label,
        "verdict_evidence": verdict_evidence,
        "alg_records_sample": alg_records[:30],
        "rat_records_sample": rat_records[:30],
        "wall_seconds": round(time.time() - t0, 2),
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))

    # ---- claims.jsonl (>= 6 entries per R6) ----
    claims = []
    claims.append({
        "claim": (
            f"b1=7 strong-null sweep: {total} families enumerated "
            f"(a2 in [-30,30]\\{{0}}, b1=7, free a1/a0/b0 in [-5,5]); "
            f"{len(convergent)} convergent at Stage A (float64 K=500 tol=1e-8); "
            f"counts={counts}; classifier upgrade applied to all Trans/Log hits."
        ),
        "evidence_type": "computation",
        "dps": DPS_PSLQ,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({"counts": counts, "total": total,
                                      "convergent": len(convergent)}),
    })
    claims.append({
        "claim": (
            f"n_trans_total={n_trans_total}; verdict={verdict_label}; "
            f"max Stage B/C residual={mpmath.nstr(max_residual, 6)}; "
            f"deep-verify residuals at dps=300 N=1500 recorded in "
            f"deep_verifications_trans."
        ),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({
            "verdict": verdict_label,
            "n_trans": n_trans_total,
            "deep": deep_results_trans,
        }),
    })
    claims.append({
        "claim": (
            f"Discriminant-identity counters at b1=7: "
            f"n_trans_on_L_minus={n_trans_on_L_minus} (predicted 0; nonzero falsifies); "
            f"n_trans_on_L_plus={n_trans_on_L_plus} (predicted 0; nonzero falsifies); "
            f"n_trans_on_other={n_trans_on_other} (diagnostic). "
            f"At b1=7, neither identity 9*a2+2*b1^2=0 nor 4*a2-b1^2=0 admits "
            f"integer a2 (98/9 and 49/4 non-integer)."
        ),
        "evidence_type": "computation",
        "dps": DPS_PSLQ,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({
            "n_L_minus": n_trans_on_L_minus,
            "n_L_plus": n_trans_on_L_plus,
            "n_other": n_trans_on_other,
        }),
    })
    claims.append({
        "claim": (
            f"Log-stratum hits at b1=7: count={len(log_records)}; "
            f"discriminant_identity_class distribution={by_identity_class_log}; "
            f"diagnostic only (not verdict-bearing) per U1-collision carry-over."
        ),
        "evidence_type": "computation",
        "dps": DPS_PSLQ,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({
            "n_log": len(log_records),
            "by_ic_log": by_identity_class_log,
            "log_pcfs": [r["coeffs"] for r in log_records],
        }),
    })
    claims.append({
        "claim": (
            f"Wall-time={round(time.time()-t0,2)}s on {n_workers}-worker pool; "
            f"max Stage-B/C PSLQ residual over Trans+Log hits was "
            f"{mpmath.nstr(max_residual, 6)}; classifier-upgrade label "
            f"distribution Trans={by_identity_class_trans}, Log={by_identity_class_log}."
        ),
        "evidence_type": "computation",
        "dps": DPS_PSLQ,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({
            "wall": round(time.time()-t0, 2),
            "workers": n_workers,
            "max_residual": mpmath.nstr(max_residual, 6),
        }),
    })
    claims.append({
        "claim": (
            f"Strong-null verdict at b1=7: {verdict_label}. "
            "STRONG_NULL_HOLDS is consistent with / supports / does not falsify "
            "the bipartition-only-loci claim of PCF-2 v1.3 sec.4 at b1=7; "
            "WEAK_TRANS_FOUND defers verdict to dps=500 follow-up; "
            "STRONG_NULL_FAILED falsifies the strong-null prediction "
            "(R7-compliant epistemic phrasing per _RULES.txt §D)."
        ),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_bipartition_b7_strong_null.py",
        "output_hash": sha256_of_obj({
            "verdict": verdict_label,
            "evidence": verdict_evidence,
        }),
    })
    if collisions:
        claims.append({
            "claim": (
                f"U1-class limit collisions at b1=7: {len(collisions)} "
                f"Log+Trans pair(s) share both L value and PSLQ relation; "
                f"flagged in unexpected_finds.json for synth follow-up."
            ),
            "evidence_type": "computation",
            "dps": DPS_PSLQ,
            "reproducible": True,
            "script": "t2b_bipartition_b7_strong_null.py",
            "output_hash": sha256_of_obj({"collisions": collisions}),
        })
    with CLAIMS_FILE.open("w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c, default=str) + "\n")

    print(f"[DONE] wall={out['wall_seconds']}s  verdict={verdict_label}  "
          f"trans={n_trans_total}  log={len(log_records)}  collisions={len(collisions)}")


if __name__ == "__main__":
    run()
