"""T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10 -- broader Log-collision sweep
at b1 in {5, 8, 9, 10}; relay 044 (2026-05-08, W19).

Adapted from t2b_bipartition_b6_dispatch.py
(siarc-relay-bridge/sessions/2026-05-05/T2B-BIPARTITION-B6-VERIFICATION/,
b6 = 79,860 families in ~31 min wall, found 4 Trans hits + 1 Log hit at
(-1,0,0,6,3) -> 2/log(2) on the Bauer-1872 orbit at k=1).

Goal:
  Determine whether off-locus n/log(2) hits at b1 != 7 surface a
  candidate 4th law (Outcome B/C) or remain absent (Outcome A,
  b1=7 stays singular as v3.1 states).

Bauer-1872 orbit (T2B v3.1 Remark rem:bauer-orbit, commit 5d83797):
  (a2, a1, a0, b1, b0) = (-k^2, 0, 0, +/- 6k, +/- 3k)
                                       -> L = +/- 2k/log 2
  Verified for k = 1, 2, 3 (b1 = 6, 12, 18).
  Range here (b1 in {5, 8, 9, 10}): NONE is +/- 6k for integer k,
  so the orbit is empty in this sweep.  ANY n/log(2) hit at
  b1 in {5, 8, 9, 10} is automatically OFF-orbit by the v3.0
  parameterization, and is a candidate-4th-law data point.

Coefficient ordering: [a2, a1, a0] for the numerator polynomial
(leading-first; matches f1_base_computation.py / project memory).

Pipeline (matches B6 / B7 prior):
  Stage A : float64 K_500 convergence filter (rel-tol 1e-8)
  Stage B : PSLQ dps=150, N=600, basis [1, L, L^2, L^3, L^4]
            (Rat / Alg classification only)
  Stage C : PSLQ dps=150, N=600, basis [1, L, pi, L*pi, pi^2,
            L*pi^2, log2, L*log2]; phantom guard rejects any
            relation with all L-coefficients (indices 1, 3, 5, 7)
            zero (i.e. effective L-coefficient = 0).
  Stage D : deep-verify dps=300 N=1500 for any Trans / Log hit,
            then n/log(2) extraction at dps=300 for clean cases.

Stratum filter:
  This sweep is for n/log(2) collisions; Trans hits are recorded
  for completeness but the primary deliverable is the Log-stratum
  count broken down by (b1, sign(a2), n).

Total enumerated families: 4 b1 values * 79,860 = 319,440.
Wall budget: ~125 min nominal (3 hr hard halt; matches relay 044).
"""
import json
import os
import sys
import time
import math
import multiprocessing as mp_proc
import concurrent.futures
import hashlib
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

A2_VALUES = [a for a in range(-30, 31) if a != 0]   # 60 values, matches b6
B1_VALUES = [5, 8, 9, 10]                             # the 044 corridor
COEFFS_FREE = list(range(-5, 6))                     # 11 values for a1, a0, b0

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

# The four "n in {2, 3, 4, 5, 6}" target n/log(2) values for outcome
# classification.  Hit on any of these (with effective L-coef == n,
# all other basis coefs either 0 or balancing the +1 on log(2)) is
# what we count.
N_LOG2_TARGETS = [2, 3, 4, 5, 6]

OUT_DIR = Path(__file__).parent
RESULTS_FILE = OUT_DIR / "results_b5_8_9_10.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"
CLAIMS_FILE = OUT_DIR / "claims.jsonl"
STAGE_A_CACHE = OUT_DIR / "stage_a_cache.json"


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


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


def bauer_orbit_membership(coeffs):
    """Per v3.1 Remark rem:bauer-orbit (commit 5d83797), the Bauer 1872
    orbit is parameterized as

      (a2, a1, a0, b1, b0) = (-k^2, 0, 0, +/- 6k, +/- 3k)  ->  +/- 2k/log 2

    Returns dict with 'on_orbit': bool, 'k': int or None,
    'sign_b1': '+' / '-', 'sign_b0': '+' / '-'.
    """
    a2, a1, a0, b1, b0 = coeffs
    if a1 != 0 or a0 != 0:
        return {"on_orbit": False, "k": None,
                "reason": "a1 or a0 nonzero"}
    if a2 >= 0:
        return {"on_orbit": False, "k": None,
                "reason": "a2 not negative integer (-k^2)"}
    k_sq = -a2
    k_root = int(round(math.isqrt(k_sq))) if k_sq >= 0 else -1
    if k_root <= 0 or k_root * k_root != k_sq:
        return {"on_orbit": False, "k": None,
                "reason": f"a2={a2} is not -k^2 for integer k"}
    k = k_root
    if abs(b1) != 6 * k:
        return {"on_orbit": False, "k": k,
                "reason": f"|b1|={abs(b1)} != 6*k=6*{k}={6*k}"}
    if abs(b0) != 3 * k:
        return {"on_orbit": False, "k": k,
                "reason": f"|b0|={abs(b0)} != 3*k=3*{k}={3*k}"}
    return {"on_orbit": True, "k": k,
            "sign_b1": "+" if b1 > 0 else "-",
            "sign_b0": "+" if b0 > 0 else "-",
            "predicted_L": f"{'+' if (b1 > 0) == (b0 > 0) else '-'}{2*k}/log(2)"}


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


def extract_n_over_log2(deep_record):
    """Given a deep_verify record, extract n if the relation is of the form
    L = n / log(2), i.e. trans_basis coefficients are
       [r0, r1, 0, 0, 0, 0, r6, r7]  with r1*L + r6*log(2) + r0 = 0
    and r0 == 0 and r6 == -n*r1 (or any rational reduction yielding L = n/log(2)).

    Returns int n in {2, 3, 4, 5, 6} or None if the relation does not match.
    """
    if deep_record is None:
        return None
    rel = deep_record.get("relation")
    if rel is None or len(rel) != 8:
        return None
    r0, r1, r2, r3, r4, r5, r6, r7 = (int(c) for c in rel)
    # Pure n/log(2): only the L coefficient (idx 1) and log(2) coefficient
    # (idx 6) nonzero, plus possibly r0 for a constant offset.
    # Form: r1 * L + r6 * log(2) + r0 = 0  =>  L = -r0/r1 - (r6/r1) * log(2)
    # For L = n/log(2) we need pi coefs = 0, L*log(2) coef = 0, L*pi coefs = 0.
    if r2 != 0 or r3 != 0 or r4 != 0 or r5 != 0 or r7 != 0:
        return None
    # L = (-r0 - r6 * log(2)) / r1.  For L = n/log(2) we'd need
    # the constant + log term combination to equal n/log(2), which
    # mpmath.pslq cannot find with only basis [1, L, log(2)]; it would
    # need 1/log(2).  So a "pure n/log(2)" relation in this basis
    # actually shows up as a relation involving L*log(2), i.e. r7 != 0
    # with the form  r1 * L + r7 * L*log(2) + r6 * log(2) + r0 = 0.
    # Let's instead look for the L*log(2) signature.
    return None


def extract_n_over_log2_v2(deep_record):
    """Correct extractor: L = n/log(2) means L*log(2) = n, so the relation
    should look like  r7 * L*log(2) + r0 = 0  with r0 = -n*r7 (sign aside),
    and all other coefficients zero.
    Returns (n_int, sign_int) or None.
    """
    if deep_record is None:
        return None
    rel = deep_record.get("relation")
    if rel is None or len(rel) != 8:
        return None
    r0, r1, r2, r3, r4, r5, r6, r7 = (int(c) for c in rel)
    # Pure n/log(2) signature: only r0 and r7 nonzero.
    if r1 != 0 or r2 != 0 or r3 != 0 or r4 != 0 or r5 != 0 or r6 != 0:
        return None
    if r7 == 0 or r0 == 0:
        return None
    # r7 * L*log(2) + r0 = 0  =>  L = -r0/(r7 * log(2))  =>  n = -r0/r7
    if (-r0) % r7 != 0:
        return None
    n = (-r0) // r7
    return n


def enumerate_families():
    families = []
    for b1 in B1_VALUES:
        for a2 in A2_VALUES:
            ratio = Fraction(a2, b1 * b1)
            for a1 in COEFFS_FREE:
                for a0 in COEFFS_FREE:
                    for b0 in COEFFS_FREE:
                        families.append((b1, str(ratio), (a2, a1, a0, b1, b0)))
    return families


def determine_outcome(off_orbit_n_log2_hits):
    """Apply STEP 5 outcome gating from relay 044.

    Returns (outcome_tag, evidence_dict).
    """
    n_off = len(off_orbit_n_log2_hits)
    if n_off == 0:
        return ("B7_STAYS_SINGULAR_BROADER", {
            "off_orbit_count": 0,
            "interpretation": "v3.1 stands; b1=7 remains the only off-orbit "
                              "n/log(2) data point in the b1 in {5,6,7,8,9,10} range.",
        })
    if n_off == 1:
        return ("CANDIDATE_4TH_LAW_2POINTS", {
            "off_orbit_count": 1,
            "off_orbit_hits": off_orbit_n_log2_hits,
            "interpretation": "One off-orbit hit found; combined with "
                              "the b1=7 outlier this gives a 2-data-point "
                              "family.  Synthesizer arbitration required.",
        })
    # n_off >= 2: check structural ratio pattern
    ratios = [h["ratio"] for h in off_orbit_n_log2_hits]
    return ("CANDIDATE_4TH_LAW_HARDEN", {
        "off_orbit_count": n_off,
        "off_orbit_hits": off_orbit_n_log2_hits,
        "ratios": ratios,
        "interpretation": ">=2 off-orbit hits; structural-equivalence "
                          "candidate.  E2 escalation MANDATORY.",
    })


def write_claims(claims, sweep_results):
    """Write claims.jsonl in standard format."""
    with CLAIMS_FILE.open("w", encoding="utf-8", newline="\n") as fh:
        for c in claims:
            fh.write(json.dumps(c, default=str) + "\n")


def run():
    t_total = time.time()
    print(f"[INIT] script_sha256 = {script_sha256()}")
    families = enumerate_families()
    total = len(families)
    print(f"[ENUM] b1 in {B1_VALUES}  a2 in {A2_VALUES[0]}..{A2_VALUES[-1]} (excl 0)  "
          f"free in {COEFFS_FREE[0]}..{COEFFS_FREE[-1]}  total={total}")

    print(f"[STAGE A] float64 K={N_STAGEA} tol={TOL_STAGEA}")
    t_a = time.time()
    convergent = None
    if STAGE_A_CACHE.exists():
        try:
            cache = json.loads(STAGE_A_CACHE.read_text())
            if cache.get("total") == total and cache.get("n_stagea") == N_STAGEA:
                convergent = [(c[0], c[1], tuple(c[2]), c[3]) for c in cache["convergent"]]
                t_a = float(cache.get("stage_a_seconds", 0.0))
                print(f"[STAGE A] loaded from cache: {len(convergent)}/{total} "
                      f"convergent in {t_a:.1f}s (cached)", flush=True)
        except Exception as exc:
            print(f"[STAGE A] cache load failed ({exc}); recomputing", flush=True)
            convergent = None
    if convergent is None:
        convergent = []
        step = max(1, total // 20)
        for i, (b1_val, ratio, coeffs) in enumerate(families):
            if i % step == 0:
                elapsed = time.time() - t_a
                print(f"  {100*i//total}%  ({i}/{total})  elapsed_a={elapsed:.1f}s",
                      flush=True)
            L = stage_a_converge_float(coeffs)
            if L is not None:
                convergent.append((b1_val, ratio, coeffs, L))
        t_a = time.time() - t_a
        print(f"[STAGE A] {len(convergent)}/{total} convergent in {t_a:.1f}s",
              flush=True)
        try:
            STAGE_A_CACHE.write_text(json.dumps({
                "total": total,
                "n_stagea": N_STAGEA,
                "tol": TOL_STAGEA,
                "stage_a_seconds": round(t_a, 2),
                "convergent": [[c[0], c[1], list(c[2]), c[3]] for c in convergent],
            }))
            print(f"[STAGE A] cache written -> {STAGE_A_CACHE.name}", flush=True)
        except Exception as exc:
            print(f"[STAGE A] cache write failed: {exc}", flush=True)

    print(f"[STAGE B/C] PSLQ dps={DPS_PSLQ} N={N_PSLQ}  workers...", flush=True)
    items = [(i, c[2]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    results = None
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_workers) as ex:
            results = list(ex.map(classify_pslq_worker, items, chunksize=64))
        print(f"[STAGE B/C] ProcessPoolExecutor map ok", flush=True)
    except Exception as exc:
        print(f"[STAGE B/C] ProcessPoolExecutor failed: {exc!r}; "
              f"falling back to serial map", flush=True)
        results = None
    if results is None:
        results = []
        report_step = max(1, len(items) // 40)
        for j, item in enumerate(items):
            if j % report_step == 0:
                el = time.time() - t_bc
                print(f"  serial {100*j//max(1,len(items))}%  ({j}/{len(items)})  "
                      f"elapsed_bc={el:.1f}s", flush=True)
            results.append(classify_pslq_worker(item))
    t_bc = time.time() - t_bc
    print(f"[STAGE B/C] done in {t_bc:.1f}s with {n_workers} workers",
          flush=True)

    # Per-b1 cell tallies
    per_b1 = {b1: {
        "total_enumerated": 0,
        "convergent": 0,
        "counts": {},
        "by_sign_a2_neg": {},
        "by_sign_a2_pos": {},
        "trans_records": [],
        "log_records": [],
        "alg_records": [],
        "rat_records": [],
        "phantom_records": [],
        "eval_fail": [],
        "desert_count": 0,
        "n_log2_hits_on_orbit": [],
        "n_log2_hits_off_orbit": [],
    } for b1 in B1_VALUES}

    for b1_val, _ratio, _coeffs in [(f[0], f[1], f[2]) for f in families]:
        per_b1[b1_val]["total_enumerated"] += 1
    for b1_val, _ratio, _coeffs, _L in convergent:
        per_b1[b1_val]["convergent"] += 1

    for (idx, label, info) in results:
        b1_val, ratio, coeffs, L = convergent[idx]
        cell = per_b1[b1_val]
        cell["counts"][label] = cell["counts"].get(label, 0) + 1
        sign_key = "by_sign_a2_neg" if coeffs[0] < 0 else "by_sign_a2_pos"
        cell[sign_key][label] = cell[sign_key].get(label, 0) + 1
        rec = {"b1": b1_val, "ratio": ratio, "coeffs": list(coeffs),
               "L_float": float(L), "info": info}
        if label == "Trans":
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
            cell["trans_records"].append(rec)
        elif label == "Log":
            ic = discriminant_identity_class(coeffs)
            rec["discriminant_identity_class"] = ic
            cell["log_records"].append(rec)
        elif label == "Alg":
            cell["alg_records"].append(rec)
        elif label == "Rat":
            cell["rat_records"].append(rec)
        elif label == "Phantom":
            cell["phantom_records"].append(rec)
        elif label == "eval_fail":
            cell["eval_fail"].append(rec)
        else:
            cell["desert_count"] += 1

    # Stage D: deep-verify every Log record + every Trans record
    print(f"[STAGE D] deep-verify dps={DPS_DEEP} N={N_DEEP}")
    deep_results = []
    off_orbit_n_log2_hits = []
    on_orbit_n_log2_hits = []
    phantom_after_deep = []
    for b1_val in B1_VALUES:
        cell = per_b1[b1_val]
        for r in cell["log_records"] + cell["trans_records"]:
            dv = deep_verify(tuple(r["coeffs"]))
            r["deep_verify"] = dv
            n_extracted = extract_n_over_log2_v2(dv) if dv else None
            r["n_log2_extracted"] = n_extracted
            bauer = bauer_orbit_membership(tuple(r["coeffs"]))
            r["bauer_orbit"] = bauer
            deep_results.append({
                "b1": b1_val,
                "coeffs": r["coeffs"],
                "ratio": r["ratio"],
                "label_pslq": r["info"].get("relation"),
                "discriminant_identity_class": r.get("discriminant_identity_class"),
                "deep_verify": dv,
                "n_log2_extracted": n_extracted,
                "bauer_orbit": bauer,
            })
            print(f"  b1={b1_val} {r['coeffs']}  ratio={r['ratio']}  "
                  f"n={n_extracted}  bauer_on_orbit={bauer.get('on_orbit')}  "
                  f"residual={dv.get('residual') if dv else 'N/A'}")
            if n_extracted is not None and n_extracted in N_LOG2_TARGETS:
                hit = {
                    "b1": b1_val,
                    "coeffs": r["coeffs"],
                    "ratio": r["ratio"],
                    "n": n_extracted,
                    "bauer_on_orbit": bauer.get("on_orbit"),
                    "bauer_k": bauer.get("k"),
                    "deep_verify_residual": dv.get("residual") if dv else None,
                    "deep_verify_residual_lt_1e_200": dv.get("residual_lt_1e_200") if dv else None,
                }
                if bauer.get("on_orbit"):
                    on_orbit_n_log2_hits.append(hit)
                    cell["n_log2_hits_on_orbit"].append(hit)
                else:
                    off_orbit_n_log2_hits.append(hit)
                    cell["n_log2_hits_off_orbit"].append(hit)

    outcome_tag, outcome_evidence = determine_outcome(off_orbit_n_log2_hits)

    # Pre-screen discrepancy check: at b1 in {5, 8, 9, 10} the v3.0
    # parameterization predicts ZERO Bauer-orbit hits.  Any on_orbit
    # hits would be a discrepancy.
    discrepancy_records = []
    if on_orbit_n_log2_hits:
        discrepancy_records.append({
            "type": "BAUER_ORBIT_HIT_AT_NON_6K_B1",
            "expected": 0,
            "actual": len(on_orbit_n_log2_hits),
            "hits": on_orbit_n_log2_hits,
            "interpretation": "v3.1 parameterization predicts orbit empty "
                              "at b1 in {5,8,9,10}; actual hit indicates "
                              "either a parameterization gap or a bug.",
        })

    halt_obj = {
        "outcome_tag": outcome_tag,
        "outcome_evidence": outcome_evidence,
        "halt_triggered": outcome_tag == "CANDIDATE_4TH_LAW_HARDEN",
        "off_orbit_n_log2_hits": off_orbit_n_log2_hits,
        "on_orbit_n_log2_hits": on_orbit_n_log2_hits,
        "discrepancy_records": discrepancy_records,
        "anchor_known_outliers_excluded_from_sweep": [
            {"label": "b6_bauer_k1", "coeffs": [-1, 0, 0, 6, 3], "L": "2/log(2)",
             "note": "On Bauer orbit (k=1); not in this sweep range."},
            {"label": "b7_singular", "coeffs": [8, -4, 0, 7, 4], "L": "3/log(2)",
             "ratio": "8/49", "note": "Off all three laws; not in this sweep range."},
        ],
        "v3_1_commit": "5d83797",
        "raci_install_anchor": "177bfd7 (RACI-V2026-05-08-INSTALL re-fire)",
    }
    HALT_FILE.write_text(json.dumps(halt_obj, indent=2, default=str))
    DISC_FILE.write_text(json.dumps(
        {"discrepancy_count": len(discrepancy_records),
         "discrepancies": discrepancy_records},
        indent=2, default=str))
    UNEX_FILE.write_text(json.dumps({
        "off_orbit_n_log2_hit_count": len(off_orbit_n_log2_hits),
        "off_orbit_n_log2_hits": off_orbit_n_log2_hits,
        "phantom_records_per_b1": {
            str(b1): per_b1[b1]["phantom_records"] for b1 in B1_VALUES
        },
        "log_records_per_b1": {
            str(b1): per_b1[b1]["log_records"] for b1 in B1_VALUES
        },
    }, indent=2, default=str))

    out = {
        "task": "T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10",
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
            "bauer_orbit_classifier": "v3.1 Remark rem:bauer-orbit; (-k^2,0,0,+/-6k,+/-3k)",
            "scope_note": (
                "a2 in [-30,30]\\{0}, b1 in {5,8,9,10}; matches B6/B7 "
                "harness ranges.  Bauer orbit at v3.1 parameterization "
                "is empty in this b1 corridor (b1 != +/- 6k for integer k)."
            ),
        },
        "total_families": total,
        "total_convergent": sum(c[0] is not None for c in convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "per_b1": per_b1,
        "deep_verifications": deep_results,
        "outcome_tag": outcome_tag,
        "outcome_evidence": outcome_evidence,
        "off_orbit_n_log2_hits": off_orbit_n_log2_hits,
        "on_orbit_n_log2_hits": on_orbit_n_log2_hits,
        "wall_seconds": round(time.time() - t_total, 2),
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))

    # AEAL claims (relay 044 STEP 6)
    out_hash = hashlib.sha256(RESULTS_FILE.read_bytes()).hexdigest()
    script_hash = script_sha256()
    claims = []
    claims.append({
        "claim": "rule5 grounding evidence captured pre-run "
                 "(CMB header timestamp + 30-day bridge listing + cli_log)",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10.py",
        "output_hash": out_hash,
    })
    for b1 in B1_VALUES:
        cell = per_b1[b1]
        n_log2_total = len(cell["n_log2_hits_on_orbit"]) + len(cell["n_log2_hits_off_orbit"])
        claims.append({
            "claim": f"b{b1}_total_enumerated_{cell['total_enumerated']}_"
                     f"convergent_{cell['convergent']}_"
                     f"log_hits_{cell['counts'].get('Log', 0)}_"
                     f"trans_hits_{cell['counts'].get('Trans', 0)}_"
                     f"n_over_log2_{n_log2_total}",
            "evidence_type": "computation",
            "dps": DPS_PSLQ,
            "reproducible": True,
            "script": "sweep_b1_5_8_9_10.py",
            "output_hash": out_hash,
        })
    claims.append({
        "claim": f"outcome_{outcome_tag}_off_orbit_n_log2_count_{len(off_orbit_n_log2_hits)}",
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10.py",
        "output_hash": out_hash,
    })
    claims.append({
        "claim": f"script_sha256_{script_hash}",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10.py",
        "output_hash": out_hash,
    })
    write_claims(claims, out)

    print(f"[DONE] wall={out['wall_seconds']}s  outcome={outcome_tag}")
    print(f"[OUT] {RESULTS_FILE}")
    print(f"[CLAIMS] {len(claims)} entries -> {CLAIMS_FILE}")
    return outcome_tag


def _redirect_to_logfile():
    """Self-redirect stdout+stderr to run.log when invoked without external
    redirection (avoids Windows multiprocessing parent_pid handle bug
    triggered by Start-Process -RedirectStandardOutput).  Re-entrant safe.
    """
    log_path = OUT_DIR / "run.log"
    if os.environ.get("SWEEP_LOG_REDIRECTED") == "1":
        return
    fh = open(log_path, "a", buffering=1, encoding="utf-8", newline="\n")
    sys.stdout = fh
    sys.stderr = fh
    os.environ["SWEEP_LOG_REDIRECTED"] = "1"


if __name__ == "__main__":
    if "--no-redirect" not in sys.argv:
        _redirect_to_logfile()
    # Force spawn (Windows default; explicit for safety)
    try:
        mp_proc.set_start_method("spawn", force=True)
    except RuntimeError:
        pass
    run()
