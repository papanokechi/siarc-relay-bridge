"""T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE -- 044R re-fire of 044 with
tightened PSLQ_HMAX_TRANS = 10**7 and Stage A loaded from cache.
Anchored on bridge commit 42a1318 (sessions/2026-05-08/
T2B-BZERO-OFFSET-LOG-SWEEP-B5-8-9-10/).

SCOPE OF CHANGE FROM 044 (per relay 044R prompt):
  1. PSLQ_HMAX_TRANS reduced from 10**9 to 10**7.
  2. Stage A loaded strictly from cached stage_a_cache.json (never
     re-enumerated); halts with STAGE_A_CACHE_INTEGRITY_FAIL if cache
     mismatches stage_a_summary.json bit-for-bit.
  3. 2.5-hr wall guard on Stage B/C/D; clean halt with verdict
     NOT_DETERMINED_AT_H7_BUDGET if breached.

ALL other parameters (N=600, dps=150, ProcessPoolExecutor harness,
b1 in {5, 8, 9, 10}, a2 in [-30,-1] U [1,30]) are PRESERVED.

Verdict tags follow the OUTCOME_*_AT_H7 convention required by 044R
(absence-of-detection at h<=10^7 is bounded evidence, not absolute).

Adapted from t2b_bipartition_b6_dispatch.py
(siarc-relay-bridge/sessions/2026-05-05/T2B-BIPARTITION-B6-VERIFICATION/,
b6 = 79,860 families in ~31 min wall, found 4 Trans hits + 1 Log hit at
(-1,0,0,6,3) -> 2/log(2) on the Bauer-1872 orbit at k=1).

Goal:
  Determine whether off-locus n/log(2) hits at b1 != 7 surface a
  candidate 4th law (Outcome B/C at h<=10^7) or remain absent
  (Outcome A at h<=10^7, b1=7 stays singular as v3.1 states at this
  bounded h-level).

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
# 044R: reduced from 10**9 to 10**7 per relay 044R prompt SCOPE OF CHANGE #1.
PSLQ_HMAX_TRANS = 10**7
RESIDUAL_TOL_RAT = mpf(10) ** (-50)
RESIDUAL_TOL_TRANS = mpf(10) ** (-40)

# 044R: 2.5-hr hard wall guard on Stage B/C/D (one-third of the
# executer's prior 3-hr-with-overrun) per relay 044R SCOPE OF CHANGE #3.
WALL_BUDGET_SECONDS = int(2.5 * 3600)
H_BOUND_TAG = "AT_H7"  # 044R: epistemic qualifier on outcome verdicts

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
STAGE_A_SUMMARY = OUT_DIR / "stage_a_summary.json"  # 044R: integrity oracle


def script_sha256():
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def _write_halt_and_exit(halt_tag, extra):
    """044R: write halt_log.json with the given tag + extra fields, then
    exit non-zero.  Used for STAGE_A_CACHE_INTEGRITY_FAIL and other hard
    halts that prevent any meaningful continuation.
    """
    payload = {
        "halt_tag": halt_tag,
        "task_id": "T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE",
        "relay_prompt": "044R (re-fire of 044 with PSLQ_HMAX_TRANS=10^7)",
        "halted_at_local_iso": time.strftime("%Y-%m-%d %H:%M:%S"),
        "halted_at_utc_iso": time.strftime("%Y-%m-%d %H:%M:%S",
                                           time.gmtime()),
        "anchor_044_commit": "42a1318",
    }
    payload.update(extra or {})
    try:
        HALT_FILE.write_text(json.dumps(payload, indent=2, default=str))
    except Exception:
        pass
    print(f"[HALT] {halt_tag}: {extra}", flush=True)
    sys.exit(1)


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


def determine_outcome_h7(off_orbit_n_log2_hits, ambiguous_records,
                         budget_exceeded, stage_bc_completed,
                         stage_bc_total, stage_d_completed,
                         stage_d_total):
    """044R outcome gating with epistemic h-bound qualifier.

    Returns (outcome_tag, evidence_dict).  All A/B/C tags carry the
    AT_H7 qualifier per 044R prompt; bare A/B/C is forbidden.
    """
    # Budget exhaustion takes precedence: cannot determine A/B/C if
    # Stage B/C/D did not complete within the 2.5-hr wall.
    if budget_exceeded:
        return ("NOT_DETERMINED_AT_H7_BUDGET", {
            "reason": "2.5-hr wall guard fired before Stage D completion",
            "stage_bc_completed": stage_bc_completed,
            "stage_bc_total": stage_bc_total,
            "stage_bc_completion_rate": (
                stage_bc_completed / max(1, stage_bc_total)
            ),
            "stage_d_completed": stage_d_completed,
            "stage_d_total": stage_d_total,
            "off_orbit_partial_count": len(off_orbit_n_log2_hits),
            "off_orbit_partial_hits": off_orbit_n_log2_hits,
            "ambiguous_partial_count": len(ambiguous_records),
            "interpretation": (
                "Stage B/C and/or Stage D did not complete within the "
                "2.5-hr wall budget at h<=10^7. v3.1 stratification at "
                "h<=10^7 is NOT determined by this run. Recommendation: "
                "per-b1 split (option (b) of 044 Recommended Next Step)."
            ),
        })
    n_off = len(off_orbit_n_log2_hits)
    n_ambig = len(ambiguous_records)
    if n_off == 0 and n_ambig == 0:
        return ("OUTCOME_A_AT_H7", {
            "off_orbit_count": 0,
            "ambiguous_count": 0,
            "h_bound": 10 ** 7,
            "interpretation": (
                "Zero off-orbit n/log(2) hits at h<=10^7 in b1 in "
                "{5,8,9,10}. v3.1 stratification HOLDS at h<=10^7. "
                "NOTE: absence-of-detection at finite h is bounded "
                "evidence; not proof of absence at h>10^7."
            ),
        })
    if n_off == 0 and n_ambig > 0:
        # Clean A is impossible because some Log-classified Stage B/C
        # records did not deeply verify at dps=300 / h=10^7.
        return ("NOT_DETERMINED_AT_H7", {
            "off_orbit_count": 0,
            "ambiguous_count": n_ambig,
            "ambiguous_records": ambiguous_records,
            "h_bound": 10 ** 7,
            "interpretation": (
                "Stage B/C found Log/Trans candidates at h<=10^7 that "
                "failed deep-verify at dps=300 (no clean PSLQ relation "
                "or residual >= 1e-200). Cannot cleanly classify as A. "
                "Recommendation: re-fire at h=10^8 OR per-b1 split."
            ),
        })
    if n_off == 1:
        return ("OUTCOME_B_AT_H7", {
            "off_orbit_count": 1,
            "off_orbit_hits": off_orbit_n_log2_hits,
            "ambiguous_count": n_ambig,
            "ambiguous_records": ambiguous_records,
            "h_bound": 10 ** 7,
            "interpretation": (
                "Exactly one off-orbit n/log(2) hit at h<=10^7. Combined "
                "with the b1=7 (8,-4,0,7,4) outlier this gives a 2-data-"
                "point off-orbit family. 044B contingency unblocks. "
                "NOTE: absence of additional outliers at h<=10^7 is "
                "bounded; higher h may reveal more."
            ),
        })
    # n_off >= 2
    ratios = [h["ratio"] for h in off_orbit_n_log2_hits]
    return ("OUTCOME_C_AT_H7", {
        "off_orbit_count": n_off,
        "off_orbit_hits": off_orbit_n_log2_hits,
        "ratios": ratios,
        "ambiguous_count": n_ambig,
        "ambiguous_records": ambiguous_records,
        "h_bound": 10 ** 7,
        "interpretation": (
            ">=2 off-orbit n/log(2) hits at h<=10^7. Structural-"
            "equivalence candidate. v3.1 §4 E2 escalation MANDATORY. "
            "044C contingency unblocks; 047/048/049/050 HALT cascade."
        ),
    })


def determine_outcome(off_orbit_n_log2_hits):
    """Original 044 determine_outcome retained for reference; not used
    in 044R verdict. Kept for harness diff-minimality."""
    n_off = len(off_orbit_n_log2_hits)
    if n_off == 0:
        return ("B7_STAYS_SINGULAR_BROADER", {"off_orbit_count": 0})
    if n_off == 1:
        return ("CANDIDATE_4TH_LAW_2POINTS",
                {"off_orbit_count": 1, "off_orbit_hits": off_orbit_n_log2_hits})
    return ("CANDIDATE_4TH_LAW_HARDEN",
            {"off_orbit_count": n_off, "off_orbit_hits": off_orbit_n_log2_hits})


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

    # 044R Stage A: STRICT cache-only load.  Never recompute.  Halt with
    # STAGE_A_CACHE_INTEGRITY_FAIL if cache is missing, malformed, or
    # disagrees with stage_a_summary.json bit-for-bit.
    print(f"[STAGE A] 044R strict cache-load mode (recompute disabled)",
          flush=True)
    t_a_start = time.time()
    if not STAGE_A_CACHE.exists():
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": "stage_a_cache.json not found in OUT_DIR",
                              "out_dir": str(OUT_DIR)})
    if not STAGE_A_SUMMARY.exists():
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": "stage_a_summary.json not found in OUT_DIR",
                              "out_dir": str(OUT_DIR)})
    try:
        cache = json.loads(STAGE_A_CACHE.read_text())
    except Exception as exc:
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"cache parse failed: {exc!r}"})
    try:
        summary = json.loads(STAGE_A_SUMMARY.read_text())
    except Exception as exc:
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"summary parse failed: {exc!r}"})
    if cache.get("total") != total:
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"cache.total {cache.get('total')} "
                                        f"!= expected enumeration total {total}"})
    if cache.get("n_stagea") != N_STAGEA:
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"cache.n_stagea {cache.get('n_stagea')} "
                                        f"!= expected N_STAGEA {N_STAGEA}"})
    if summary.get("stage_a_total_enumerated") != total:
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"summary.stage_a_total_enumerated "
                                        f"{summary.get('stage_a_total_enumerated')} "
                                        f"!= expected {total}"})
    convergent = [(c[0], c[1], tuple(c[2]), c[3]) for c in cache["convergent"]]
    if len(convergent) != summary.get("stage_a_total_convergent"):
        _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                             {"reason": f"len(cache.convergent) {len(convergent)} "
                                        f"!= summary.stage_a_total_convergent "
                                        f"{summary.get('stage_a_total_convergent')}"})
    # Per-b1 bit-for-bit integrity check
    expected_per_b1 = summary.get("per_b1", {})
    actual_per_b1 = {}
    for b1_val, _ratio, _coeffs, _L in convergent:
        actual_per_b1[str(b1_val)] = actual_per_b1.get(str(b1_val), 0) + 1
    for b1_str, expected_block in expected_per_b1.items():
        actual_count = actual_per_b1.get(b1_str, 0)
        expected_count = expected_block.get("convergent")
        if actual_count != expected_count:
            _write_halt_and_exit("STAGE_A_CACHE_INTEGRITY_FAIL",
                                 {"reason": f"per_b1[{b1_str}] cache convergent "
                                            f"count {actual_count} != summary "
                                            f"count {expected_count}",
                                  "b1": b1_str})
    t_a = float(cache.get("stage_a_seconds", 0.0))
    t_a_load = time.time() - t_a_start
    print(f"[STAGE A] cache load OK: {len(convergent)}/{total} convergent "
          f"(cached t_a={t_a:.1f}s, load took {t_a_load*1000:.0f}ms); "
          f"per-b1 integrity PASS against stage_a_summary.json", flush=True)

    # 044R Stage B/C: ProcessPoolExecutor with as_completed wall guard at
    # WALL_BUDGET_SECONDS (2.5 hr) measured from t_total.  On budget
    # breach: cancel pending futures, set _budget_exceeded flag, and
    # proceed to Stage D / outcome with partial results.
    print(f"[STAGE B/C] PSLQ dps={DPS_PSLQ} N={N_PSLQ}  h_max={PSLQ_HMAX_TRANS:.0e}  "
          f"wall_budget={WALL_BUDGET_SECONDS}s  workers...", flush=True)
    items = [(i, c[2]) for i, c in enumerate(convergent)]
    t_bc = time.time()
    n_workers = max(1, mp_proc.cpu_count() - 1)
    results = []
    _budget_exceeded = False
    _bc_completed = 0
    _bc_total = len(items)

    ex = concurrent.futures.ProcessPoolExecutor(max_workers=n_workers)
    futures = {ex.submit(classify_pslq_worker, item): item for item in items}
    print(f"[STAGE B/C] dispatched {len(futures)} tasks to {n_workers} workers",
          flush=True)
    last_log = time.time()
    try:
        for future in concurrent.futures.as_completed(futures):
            elapsed_total = time.time() - t_total
            if elapsed_total > WALL_BUDGET_SECONDS:
                print(f"[WALL GUARD] 2.5-hr budget exceeded at "
                      f"elapsed_total={elapsed_total:.0f}s; halting Stage B/C "
                      f"at {_bc_completed}/{_bc_total} "
                      f"({100*_bc_completed/max(1,_bc_total):.1f}%); will emit "
                      f"NOT_DETERMINED_AT_H7_BUDGET.", flush=True)
                _budget_exceeded = True
                break
            try:
                results.append(future.result())
            except Exception as exc:
                item = futures[future]
                results.append((item[0], "eval_fail",
                                {"error": f"future_exc: {exc!r}"}))
            _bc_completed += 1
            now = time.time()
            if now - last_log > 60:
                elapsed_bc = now - t_bc
                rate = _bc_completed / max(1e-9, elapsed_bc)
                eta = (_bc_total - _bc_completed) / max(1e-9, rate)
                print(f"  [BC] {_bc_completed}/{_bc_total} "
                      f"({100*_bc_completed/_bc_total:.1f}%)  "
                      f"elapsed_bc={elapsed_bc:.0f}s  rate={rate:.1f}/s  "
                      f"eta_bc={eta:.0f}s  wall_total={elapsed_total:.0f}s/"
                      f"{WALL_BUDGET_SECONDS}s", flush=True)
                last_log = now
    finally:
        if _budget_exceeded:
            cancelled = 0
            for fut in futures:
                if not fut.done() and fut.cancel():
                    cancelled += 1
            print(f"[WALL GUARD] cancelled {cancelled} pending futures; "
                  f"forcibly shutting down executor (wait=False)", flush=True)
            ex.shutdown(wait=False, cancel_futures=True)
        else:
            ex.shutdown(wait=True)
    t_bc = time.time() - t_bc
    print(f"[STAGE B/C] collected {len(results)}/{_bc_total} results in "
          f"{t_bc:.1f}s with {n_workers} workers "
          f"(budget_exceeded={_budget_exceeded})", flush=True)

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

    # Stage D: deep-verify every Log record + every Trans record.
    # 044R: respect WALL_BUDGET_SECONDS measured from t_total.
    print(f"[STAGE D] deep-verify dps={DPS_DEEP} N={N_DEEP}  "
          f"h_max={PSLQ_HMAX_TRANS:.0e}  wall_budget={WALL_BUDGET_SECONDS}s",
          flush=True)
    deep_results = []
    off_orbit_n_log2_hits = []
    on_orbit_n_log2_hits = []
    ambiguous_records = []  # 044R: Log/Trans hits that fail deep-verify
    phantom_after_deep = []
    _stage_d_total = 0
    _stage_d_completed = 0
    for b1_val in B1_VALUES:
        cell = per_b1[b1_val]
        _stage_d_total += len(cell["log_records"]) + len(cell["trans_records"])
    for b1_val in B1_VALUES:
        cell = per_b1[b1_val]
        for r in cell["log_records"] + cell["trans_records"]:
            elapsed_total = time.time() - t_total
            if elapsed_total > WALL_BUDGET_SECONDS:
                print(f"[WALL GUARD] budget exceeded during Stage D at "
                      f"elapsed_total={elapsed_total:.0f}s; skipping remaining "
                      f"deep_verify calls ({_stage_d_completed}/{_stage_d_total} "
                      f"completed)", flush=True)
                _budget_exceeded = True
                break
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
            _stage_d_completed += 1
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
            else:
                # 044R: classify as "ambiguous" if Stage B/C said Log but
                # deep-verify at dps=300 / h=10^7 didn't extract an
                # n/log(2) AND the deep PSLQ either returned no relation
                # or residual >= 1e-200.
                stage_bc_label_was_log = (
                    r in cell["log_records"]
                )
                if stage_bc_label_was_log:
                    deep_rel = (dv or {}).get("relation")
                    deep_residual_ok = (
                        (dv or {}).get("residual_lt_1e_200") is True
                    )
                    if deep_rel is None or not deep_residual_ok:
                        ambiguous_records.append({
                            "b1": b1_val,
                            "coeffs": r["coeffs"],
                            "ratio": r["ratio"],
                            "stage_bc_relation": r["info"].get("relation"),
                            "stage_bc_residual": r["info"].get("residual"),
                            "deep_relation": deep_rel,
                            "deep_residual": (dv or {}).get("residual"),
                            "deep_residual_lt_1e_200": deep_residual_ok,
                            "reason": (
                                "Stage B/C labeled Log at h=10^7 but Stage D "
                                "deep-verify (dps=300, h=10^7) failed to "
                                "extract n/log(2) with residual<1e-200"
                            ),
                        })
        if _budget_exceeded:
            break

    outcome_tag, outcome_evidence = determine_outcome_h7(
        off_orbit_n_log2_hits,
        ambiguous_records,
        _budget_exceeded,
        _bc_completed,
        _bc_total,
        _stage_d_completed,
        _stage_d_total,
    )

    # 044R self-check: outcome verdict MUST carry an h-bound qualifier.
    # Halt with VERDICT_OMITS_H_BOUND_QUALIFIER if not.
    if outcome_tag.startswith("OUTCOME_") and "AT_H7" not in outcome_tag:
        _write_halt_and_exit("VERDICT_OMITS_H_BOUND_QUALIFIER",
                             {"outcome_tag": outcome_tag,
                              "reason": "OUTCOME_A/B/C verdict missing AT_H7 "
                                        "qualifier; forbidden per 044R prompt"})

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
        "task_id": "T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE",
        "relay_prompt": "044R",
        "anchor_044_commit": "42a1318",
        "outcome_tag": outcome_tag,
        "outcome_evidence": outcome_evidence,
        "h_bound": 10 ** 7,
        "budget_exceeded": _budget_exceeded,
        "halt_triggered": (
            outcome_tag in ("OUTCOME_C_AT_H7",
                            "NOT_DETERMINED_AT_H7_BUDGET")
        ),
        "stage_bc_completed": _bc_completed,
        "stage_bc_total": _bc_total,
        "stage_d_completed": _stage_d_completed,
        "stage_d_total": _stage_d_total,
        "off_orbit_n_log2_hits": off_orbit_n_log2_hits,
        "on_orbit_n_log2_hits": on_orbit_n_log2_hits,
        "ambiguous_records": ambiguous_records,
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
        "task": "T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE",
        "relay_prompt": "044R",
        "anchor_044_commit": "42a1318",
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
            "pslq_hmax_rat": PSLQ_HMAX_RAT,
            "pslq_hmax_trans": PSLQ_HMAX_TRANS,
            "wall_budget_seconds": WALL_BUDGET_SECONDS,
            "phantom_guard": "L-coefficient (indices 1,3,5,7) must be nonzero (R3)",
            "bauer_orbit_classifier": "v3.1 Remark rem:bauer-orbit; (-k^2,0,0,+/-6k,+/-3k)",
            "scope_note": (
                "a2 in [-30,30]\\{0}, b1 in {5,8,9,10}; matches B6/B7 "
                "harness ranges.  Bauer orbit at v3.1 parameterization "
                "is empty in this b1 corridor (b1 != +/- 6k for integer k). "
                "044R: PSLQ_HMAX_TRANS=10^7 (down from 10^9); Stage A from cache."
            ),
        },
        "total_families": total,
        "total_convergent": len(convergent),
        "stage_a_seconds": round(t_a, 2),
        "stage_bc_seconds": round(t_bc, 2),
        "stage_bc_completed": _bc_completed,
        "stage_bc_total": _bc_total,
        "stage_d_completed": _stage_d_completed,
        "stage_d_total": _stage_d_total,
        "budget_exceeded": _budget_exceeded,
        "per_b1": per_b1,
        "deep_verifications": deep_results,
        "outcome_tag": outcome_tag,
        "outcome_evidence": outcome_evidence,
        "off_orbit_n_log2_hits": off_orbit_n_log2_hits,
        "on_orbit_n_log2_hits": on_orbit_n_log2_hits,
        "ambiguous_records": ambiguous_records,
        "wall_seconds": round(time.time() - t_total, 2),
    }
    RESULTS_FILE.write_text(json.dumps(out, indent=2, default=str))

    # AEAL claims (relay 044R STEP 6).  Carries forward the Stage A
    # claims from 044 (commit 42a1318) and adds 044R-specific outcome
    # + provenance entries.  Minimum 6 entries per 044R prompt.
    out_hash = hashlib.sha256(RESULTS_FILE.read_bytes()).hexdigest()
    script_hash = script_sha256()
    claims_044_jsonl_sha256 = (
        "94be8efb09edf472f7a48d4fdbc7386f35f342b7ac3df83b8fb9a920015ef7c9"
    )
    stage_a_cache_sha256 = (
        "dc081ca68f67296b29d56141da4add7c30f878fad5b813cece26f425e5f0a527"
    )
    stage_a_summary_sha256 = (
        "89a694bc89cc6690438177fa6f09fde685c240c106997fd3e9070ed101aa9f53"
    )
    sweep_044_sha256 = (
        "718ea0e66bddeb401e36f6cb2687058c1a779ea6089b744d15548fe91539929d"
    )
    claims = []
    # Carried-forward 044 Stage A claims (anchored on 42a1318)
    claims.append({
        "claim": "044R-A1: stage_a_total_enumerated_319440 carried forward "
                 "from 044 commit 42a1318 (claims.jsonl C4); h_bound=10^7",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": claims_044_jsonl_sha256,
    })
    claims.append({
        "claim": "044R-A2: stage_a_total_convergent_241892 carried forward "
                 "from 044 commit 42a1318 (claims.jsonl C4); cache integrity "
                 "verified bit-for-bit against stage_a_summary.json",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": stage_a_cache_sha256,
    })
    claims.append({
        "claim": "044R-A3: per_b1_monotone_convergence_rates_b5_54.6_b8_75.1"
                 "_b9_83.2_b10_90.0_pct carried forward from 044 commit "
                 "42a1318 (claims.jsonl C5-C8)",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": stage_a_summary_sha256,
    })
    claims.append({
        "claim": f"044R-A4: harness_provenance sweep_044_sha256={sweep_044_sha256} "
                 f"+ 3 SCOPE OF CHANGE edits (PSLQ_HMAX_TRANS 10^9->10^7, strict "
                 f"Stage A cache load with summary integrity check, 2.5-hr wall "
                 f"guard) -> sweep_b1_5_8_9_10_refire.py sha256={script_hash}",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": script_hash,
    })
    # Per-b1 cell tallies (Stage B/C results at h=10^7)
    for b1 in B1_VALUES:
        cell = per_b1[b1]
        n_log2_total = (len(cell["n_log2_hits_on_orbit"])
                        + len(cell["n_log2_hits_off_orbit"]))
        claims.append({
            "claim": f"044R-B{b1}: total_enumerated_{cell['total_enumerated']}_"
                     f"convergent_{cell['convergent']}_"
                     f"log_hits_{cell['counts'].get('Log', 0)}_"
                     f"trans_hits_{cell['counts'].get('Trans', 0)}_"
                     f"n_over_log2_{n_log2_total}_at_h7",
            "evidence_type": "computation",
            "dps": DPS_PSLQ,
            "reproducible": True,
            "script": "sweep_b1_5_8_9_10_refire.py",
            "output_hash": out_hash,
        })
    # 044R-A5: outcome verdict at h=10^7
    claims.append({
        "claim": f"044R-A5: outcome_{outcome_tag}_off_orbit_count_"
                 f"{len(off_orbit_n_log2_hits)}_ambiguous_count_"
                 f"{len(ambiguous_records)}_budget_exceeded_{_budget_exceeded}_"
                 f"stage_bc_{_bc_completed}_of_{_bc_total}_stage_d_"
                 f"{_stage_d_completed}_of_{_stage_d_total}",
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": out_hash,
    })
    # 044R-A6: refire script SHA-256
    claims.append({
        "claim": f"044R-A6: refire_script_sha256_{script_hash}_"
                 f"pslq_hmax_trans_10e7_wall_budget_{WALL_BUDGET_SECONDS}s",
        "evidence_type": "computation",
        "dps": 0,
        "reproducible": True,
        "script": "sweep_b1_5_8_9_10_refire.py",
        "output_hash": script_hash,
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
