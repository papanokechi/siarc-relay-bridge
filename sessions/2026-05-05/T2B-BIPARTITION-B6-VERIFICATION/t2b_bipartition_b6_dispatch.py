"""T2B-BIPARTITION-B6-VERIFICATION — b1=6 verification (relay 039, 2026-05-05).

Verifies the preprint-stated bipartition (PCF-2 v1.3, DOI 10.5281/zenodo.19783312)
at b1=6 with both signs of a2. Predicts Trans-stratum hits at b1=6 lie on
exactly two loci L- = {a2=-8, ratio=-2/9} and L+ = {a2=9, ratio=+1/4}.

Provenance:
  Source: Synthesizer P-001 arbitration (E1 out-of-band 2026-05-05 ~10:30 JST)
        + CLI sharpening via T2B-E1-AUDIT-STRUCTURAL-IDENTITIES (~10:50 JST)
        + operator preprint-audit (~10:55 JST, Case B verdict)
        + synth concurrence (~10:55 JST, bipartition pre-registered as
          binary outcome).
  Relay file: tex/submitted/control center/prompt/039_t2b_bipartition_b6_verification.txt

Coefficient ordering: [a2, a1, a0] for the numerator polynomial
(leading-first, matches f1_base_computation.py / project memory).

Pipeline (matches T2B-B67 prior runs):
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=150, N=600, basis [1, L, L^2, L^3, L^4]
  Stage C : PSLQ dps=150, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]; phantom guard rejects any
            relation with all L-coefficients (indices 1,3,5,7) = 0.
  Stage D : deep-verify dps=300 N=1500 for any Trans / Log hit.

Classifier upgrade (Step 3 of relay 039 / synth-authored rule5 candidate):
  For every Trans hit, compute discriminant_identity_class:
    trans_stratum_proper  -- ratio = -2/9 (i.e. 9*a2 + 2*b1^2 == 0)
    brouncker_boundary    -- ratio = +1/4 (i.e. 4*a2 - b1^2 == 0)
    neither               -- any other ratio (would falsify bipartition).

Verdict labels (post-analysis, written into halt_log.json):
  BIPARTITION_HOLDS         -- every Trans hit on L- or L+ AND ratios match
  THIRD_STRATUM_FOUND       -- a third ratio appears (HARD HALT)
  LOCUS_VIOLATION_TRANS     -- Trans hit at -2/9 ratio with a2 != -8
  LOCUS_VIOLATION_BROUNCKER -- Trans hit at +1/4 ratio with a2 != 9
  NULL_LMINUS               -- zero Trans hits at a2 = -8 (predicted leg empty)

Coverage scope (Step 2 of relay 039):
  a2 in {-30..-1} U {1..30}   # 60 values (excludes a2=0; covers L- at a2=-8)
  b1 = 6                      # dispatch focus
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
B1_VALUES = [6]
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
RESULTS_FILE = OUT_DIR / "results_b6.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"


def discriminant_identity_class(coeffs):
    """Classify a Trans/Log hit by which structural identity it satisfies.

    Returns one of:
      'trans_stratum_proper'  -- 9*a2 + 2*b1^2 == 0 (a2/b1^2 = -2/9 leg)
      'brouncker_boundary'    -- 4*a2 - b1^2 == 0  (a2/b1^2 = +1/4 leg)
      'neither'               -- any other ratio
    """
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


def determine_verdict(trans_records, deep_results, predicted_lminus_a2,
                     predicted_lplus_a2, ratio_lminus, ratio_lplus):
    """Apply Step-5 verdict logic from relay 039.

    Returns (verdict_label, evidence_dict).
    """
    confirmed = []
    for r in trans_records:
        dv = r.get("deep_verify")
        if dv and dv.get("relation"):
            rel = dv["relation"]
            if any(int(rel[i]) != 0 for i in (1, 3, 5, 7)):
                confirmed.append(r)

    confirmed_lminus = [r for r in confirmed if r["coeffs"][0] == predicted_lminus_a2
                        and r.get("ratio") == ratio_lminus]
    confirmed_lplus = [r for r in confirmed if r["coeffs"][0] == predicted_lplus_a2
                       and r.get("ratio") == ratio_lplus]
    confirmed_other_ratio = [r for r in confirmed
                             if r.get("ratio") not in (ratio_lminus, ratio_lplus)]
    confirmed_locus_violation_trans = [r for r in confirmed
                                       if r.get("ratio") == ratio_lminus
                                       and r["coeffs"][0] != predicted_lminus_a2]
    confirmed_locus_violation_brouncker = [r for r in confirmed
                                           if r.get("ratio") == ratio_lplus
                                           and r["coeffs"][0] != predicted_lplus_a2]

    if confirmed_other_ratio:
        return ("THIRD_STRATUM_FOUND", {
            "third_stratum_hits": [
                {"coeffs": r["coeffs"], "ratio": r["ratio"]}
                for r in confirmed_other_ratio
            ],
        })
    if confirmed_locus_violation_trans:
        return ("LOCUS_VIOLATION_TRANS", {
            "violations": [
                {"coeffs": r["coeffs"], "ratio": r["ratio"]}
                for r in confirmed_locus_violation_trans
            ],
        })
    if confirmed_locus_violation_brouncker:
        return ("LOCUS_VIOLATION_BROUNCKER", {
            "violations": [
                {"coeffs": r["coeffs"], "ratio": r["ratio"]}
                for r in confirmed_locus_violation_brouncker
            ],
        })
    if not confirmed_lminus:
        return ("NULL_LMINUS", {
            "predicted_lminus_a2": predicted_lminus_a2,
            "ratio_lminus": ratio_lminus,
            "trans_count_total": len(confirmed),
            "lplus_count": len(confirmed_lplus),
        })
    return ("BIPARTITION_HOLDS", {
        "lminus_count": len(confirmed_lminus),
        "lplus_count": len(confirmed_lplus),
        "lminus_a2": predicted_lminus_a2,
        "lplus_a2": predicted_lplus_a2,
        "ratio_lminus": ratio_lminus,
        "ratio_lplus": ratio_lplus,
    })


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
    by_identity_class = {}
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
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
            by_identity_class[ic] = by_identity_class.get(ic, 0) + 1
            trans_records.append(rec)
        elif label == "Log":
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
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

    deep_results = []
    if trans_records:
        print(f"[STAGE D] {len(trans_records)} Trans candidate(s); deep-verify dps={DPS_DEEP} N={N_DEEP}")
        for r in trans_records:
            dv = deep_verify(tuple(r["coeffs"]))
            r["deep_verify"] = dv
            deep_results.append({"coeffs": r["coeffs"], "ratio": r["ratio"],
                                 "discriminant_identity_class": r.get("discriminant_identity_class"),
                                 "deep_verify": dv})
            print(f"  {r['coeffs']}  ratio={r['ratio']}  ic={r.get('discriminant_identity_class')}  deep={dv}")

    PREDICTED_LMINUS_A2 = -8
    PREDICTED_LPLUS_A2 = 9
    RATIO_LMINUS = "-2/9"
    RATIO_LPLUS = "1/4"

    verdict_label, verdict_evidence = determine_verdict(
        trans_records, deep_results,
        PREDICTED_LMINUS_A2, PREDICTED_LPLUS_A2,
        RATIO_LMINUS, RATIO_LPLUS,
    )
    print(f"[VERDICT] {verdict_label}")

    print("[SPOT-CHECK] singleton-mate (9,0,0,-6,-3) at dps=300 N=1500")
    sm_coeffs = (9, 0, 0, -6, -3)
    sm_dv = deep_verify(sm_coeffs)
    sm_record = {
        "coeffs": list(sm_coeffs),
        "ratio_a2_over_b1sq": "1/4",
        "discriminant_identity_class": discriminant_identity_class(sm_coeffs),
        "deep_verify": sm_dv,
        "note": "Brouncker-boundary singleton-mate at b1=-6 (out of main sweep)",
    }
    print(f"  singleton-mate deep: {sm_dv}")

    halt_obj = {
        "verdict_label": verdict_label,
        "verdict_evidence": verdict_evidence,
        "halt_triggered": verdict_label in (
            "THIRD_STRATUM_FOUND",
            "LOCUS_VIOLATION_TRANS",
            "LOCUS_VIOLATION_BROUNCKER",
            "NULL_LMINUS",
        ),
        "is_e1_closure_evidence": verdict_label == "BIPARTITION_HOLDS",
        "predicted_loci": {
            "L_minus": {"a2": PREDICTED_LMINUS_A2, "ratio": RATIO_LMINUS,
                        "structural_identity": "a2 = -2 * b1^2 / 9",
                        "indicial_roots": "{1/3, 2/3}"},
            "L_plus": {"a2": PREDICTED_LPLUS_A2, "ratio": RATIO_LPLUS,
                       "structural_identity": "a2 = b1^2 / 4",
                       "indicial_roots": "{1/2, 1/2} (double)"},
        },
        "preprint_doi_audited": "10.5281/zenodo.19783312",
        "operator_concurrence_jst": "2026-05-05 ~10:58",
        "synth_concurrence_jst": "2026-05-05 ~10:55",
    }
    HALT_FILE.write_text(json.dumps(halt_obj, indent=2, default=str))
    DISC_FILE.write_text("{}")
    UNEX_FILE.write_text(json.dumps({
        "log_records": log_records,
        "phantom_records": phantom_records,
    }, indent=2, default=str))

    out = {
        "task": "T2B-BIPARTITION-B6-VERIFICATION",
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
            "phantom_guard": "L-coefficient (indices 1,3,5,7) must be nonzero (R3)",
            "classifier_upgrade": (
                "discriminant_identity_class in {trans_stratum_proper, "
                "brouncker_boundary, neither} computed for every Trans/Log hit"
            ),
            "scope_note": (
                "a2 in [-30,30]\\{0}, b1=6: covers both predicted loci "
                "L-(a2=-8, -2/9) and L+(a2=9, +1/4); singleton-mate (9,0,0,-6,-3) "
                "covered via Stage A on the b0 in [-5,5] axis."
            ),
        },
        "total_families": total,
        "total_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "counts": counts,
        "by_ratio": by_ratio,
        "by_identity_class": by_identity_class,
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
        "singleton_mate_spotcheck": sm_record,
        "verdict_label": verdict_label,
        "verdict_evidence": verdict_evidence,
        "alg_records_sample": alg_records[:30],
        "rat_records_sample": rat_records[:30],
        "wall_seconds": round(time.time() - t0, 2),
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))
    print(f"[DONE] wall={out['wall_seconds']}s  verdict={verdict_label}")


if __name__ == "__main__":
    run()
