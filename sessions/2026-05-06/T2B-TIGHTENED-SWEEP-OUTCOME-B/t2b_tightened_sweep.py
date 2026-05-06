"""T2B-TIGHTENED-SWEEP-OUTCOME-B (relay 044B revised 2026-05-06)

Purpose
-------
Operationalise the structural-coincidence question raised by the 044R
verdict (`OUTCOME_B_AT_H7`, bridge fe15737):

    * b1=7  singular outlier (8, -4, 0, 7, 4)  ratio 8/49   -> L = 3/log(2)
    * b1=10 044R outlier      (-9, 0, 0, 10, 5) ratio -9/100 -> L = 3/log(2)

Both are off-orbit (not Bauer-1872 (-k^2,0,0,+/-6k,+/-3k)), satisfy no
Brouncker-boundary / Trans-stratum-proper identity, and yield n=3.

Plan
----
P5 (precondition): re-verify the b7 singular at dps=300, h<=10^9.
   HALT_044B_B7_RE-VERIFY_FAILED if |L - 3/log(2)| >= 1e-50.

STEP 2A : Sign-orbit of the 044R hit. 8 tuples
          (a2, b1, b0) in {-9,+9} x {-10,+10} x {-5,+5}, a1 = a0 = 0.
          Direct dps=300 PSLQ at h <= 10^9.

STEP 2B : Bauer-shape family. (a2, a1, a0) = (-k^2, 0, 0) for
          k in {1,2,3,4,5} at b1 in B(k) excluding +-6k (and signs),
          b0 in [-7, 7]. Stage A K_500 float screen, Stage B PSLQ
          dps=150 h<=10^7, Stage D deep-verify dps=300 h<=10^9 on
          Log/Trans hits.

STEP 2C : b7 co-anchor re-verify (already done as part of P5).

STEP 3  : Ratio-pattern fit (a2/b1^2 vs b1; degree<=2/denom<=30) and
          n=3 anchor count (number of tuples with n=3 among anchors +
          all hits).

STEP 4  : Classify outcome
            B-T-A : 0 new off-orbit n/log(2) hits
            B-T-B : 1-3 new hits (all n=3) on visible sub-locus
            B-T-C : >=4 hits OR clear structural pattern -> HALT
                    HALT_044B_B-T-C_FIRED.

Coefficient ordering: [a2, a1, a0] (leading-first), per
f1_base_computation.py and project memory.

Anchor provenance
-----------------
Source 044R unexpected_finds.json SHA-256 captured up-front and stored
in claims.jsonl entry 044B-A7.

Wall budget : 3 hr (HALT_044B_WALL_BUDGET).
"""
from __future__ import annotations

import concurrent.futures
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import mpmath
from mpmath import mp, mpf

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# STEP 2A sign-orbit
SIGN_ORBIT_TUPLES = []
for a2 in (-9, 9):
    for b1 in (-10, 10):
        for b0 in (-5, 5):
            SIGN_ORBIT_TUPLES.append((a2, 0, 0, b1, b0))
assert len(SIGN_ORBIT_TUPLES) == 8

# STEP 2B Bauer-shape per relay 044B prompt
BAUER_K_VALUES = [1, 2, 3, 4, 5]
def _Bk(k: int) -> list[int]:
    """B(k): magnitudes of b1 to sweep, excluding the on-orbit |b1|=6k.

    Universe is {2..15} \\ {0, 1, 6}.  We then exclude 6k.
    """
    universe = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    forbidden = 6 * k
    return [b for b in universe if b != forbidden]

# Per relay 044B step 2B explicit listings:
#   k=1: B(1) = {2, 3, 4, 5, 7, 8}                              (|.|<=8 sub-window)
#   k=2: B(2) = {2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15}        (excl +-12)
#   k=3..5: full {3..15}\{forbidden} (forbidden out of range)
# We honour the explicit listings rather than the auto-generated _Bk for k=1.
BK_EXPLICIT = {
    1: [2, 3, 4, 5, 7, 8],
    2: [2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15],
    3: [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    4: [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    5: [3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15],
}
B0_RANGE = list(range(-7, 8))  # both signs and 0; 15 values

# Stage / harness parameters
N_STAGEA = 500
TOL_STAGEA = 1e-8

DPS_STAGE_BC = 150
N_STAGE_BC = 600
PSLQ_HMAX_STAGE_B = 10 ** 7  # Bauer-shape Stage B per prompt
PSLQ_HMAX_DEEP = 10 ** 9     # deep-verify and STEP 2A direct PSLQ
RESIDUAL_TOL_RAT = mpf(10) ** (-50)
RESIDUAL_TOL_TRANS = mpf(10) ** (-40)

DPS_DEEP = 300
N_DEEP = 1500

# 044B-A3 P5 b7 re-verify tolerance
P5_RESIDUAL_TOL = mpf(10) ** (-50)
P5_DPS = 300  # exceeds the prompt's "dps>=60" floor

# Wall guard
WALL_BUDGET_SECONDS = int(3.0 * 3600)

# Source 044R provenance (for STEP 1 and claim 044B-A7)
SOURCE_044R_UFIND = Path(
    __file__
).resolve().parent.parent / "T2B-BZERO-OFFSET-LOG-SWEEP-REFIRE" / "unexpected_finds.json"
EXPECTED_044R_HIT = {
    "b1": 10,
    "coeffs": [-9, 0, 0, 10, 5],
    "ratio": "-9/100",
    "n": 3,
}

# Anchor data points (b7 singular + 044R outlier)
B7_SINGULAR_COEFFS = (8, -4, 0, 7, 4)  # ratio 8/49 -> L = 3/log(2)
B10_044R_COEFFS = (-9, 0, 0, 10, 5)     # ratio -9/100 -> L = 3/log(2)

# n target for n=3 collision counting
N_TARGET = 3
N_MATCH_RANGE = list(range(1, 21))  # for ratio-pattern m/log(2) test

OUT_DIR = Path(__file__).resolve().parent
RESULTS_FILE = OUT_DIR / "results.json"
HALT_FILE = OUT_DIR / "halt_log.json"
DISC_FILE = OUT_DIR / "discrepancy_log.json"
UNEX_FILE = OUT_DIR / "unexpected_finds.json"
CLAIMS_FILE = OUT_DIR / "claims.jsonl"

TASK_ID = "T2B-TIGHTENED-SWEEP-OUTCOME-B"
RELAY_PROMPT = "044B (revised 2026-05-06 post-044R verdict)"


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def script_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_halt(halt_tag: str, extra: dict, exit_code: int = 1) -> None:
    payload = {
        "halt_tag": halt_tag,
        "task_id": TASK_ID,
        "relay_prompt": RELAY_PROMPT,
        "halted_at_local_iso": time.strftime("%Y-%m-%d %H:%M:%S"),
        "halted_at_utc_iso": time.strftime("%Y-%m-%d %H:%M:%S",
                                           time.gmtime()),
        "anchor_044R_commit": "fe15737",
    }
    payload.update(extra or {})
    HALT_FILE.write_text(json.dumps(payload, indent=2, default=str))
    print(f"[HALT] {halt_tag}", flush=True)
    sys.exit(exit_code)


# ---------------------------------------------------------------------------
# PCF evaluation + classification (mirrors 044R harness)
# ---------------------------------------------------------------------------

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


_TRANS_BASIS_NAMES = ["1", "L", "pi", "L*pi", "pi^2", "L*pi^2", "log(2)", "L*log(2)"]


def _trans_basis(K):
    pi_v = mp.pi
    ln2 = mp.log(2)
    return [mpf(1), K, pi_v, K * pi_v, pi_v ** 2, K * pi_v ** 2, ln2, K * ln2]


def classify_pslq(K, dps: int, hmax: int):
    """Run rat-then-trans PSLQ at given dps and h-max. Returns dict."""
    mp.dps = dps
    K = mpf(K)
    rat_basis = [K ** j for j in range(5)]
    try:
        rel = mpmath.pslq(rat_basis, maxcoeff=10 ** 6)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(r * b for r, b in zip(rel, rat_basis)))
        if residual < RESIDUAL_TOL_RAT:
            label = "Rat" if all(int(c) == 0 for c in rel[2:]) else "Alg"
            return {
                "label": label,
                "L": mpmath.nstr(K, 30),
                "relation": [int(c) for c in rel],
                "residual": mpmath.nstr(residual, 6),
            }
    trans_basis = _trans_basis(K)
    try:
        rel = mpmath.pslq(trans_basis, maxcoeff=hmax)
    except Exception:
        rel = None
    if rel is None:
        return {"label": "Desert", "L": mpmath.nstr(K, 30)}
    residual = abs(sum(r * b for r, b in zip(rel, trans_basis)))
    if residual >= RESIDUAL_TOL_TRANS:
        return {"label": "Desert", "L": mpmath.nstr(K, 30),
                "relation": [int(c) for c in rel],
                "residual": mpmath.nstr(residual, 6),
                "note": "residual_above_threshold"}
    L_coeff_indices = [1, 3, 5, 7]
    if sum(abs(int(rel[i])) for i in L_coeff_indices) == 0:
        return {
            "label": "Phantom",
            "L": mpmath.nstr(K, 30),
            "relation": [int(c) for c in rel],
            "basis": _TRANS_BASIS_NAMES,
            "residual": mpmath.nstr(residual, 6),
        }
    uses_log = any(int(rel[i]) != 0 for i in (6, 7))
    uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
    label = "Log" if (uses_log and not uses_pi) else "Trans"
    return {
        "label": label,
        "L": mpmath.nstr(K, 30),
        "relation": [int(c) for c in rel],
        "basis": _TRANS_BASIS_NAMES,
        "residual": mpmath.nstr(residual, 6),
    }


def extract_n_log2(rel: list[int]) -> int | None:
    """Pure n/log(2) signature: only r0 and r7 nonzero, n = -r0/r7 integer."""
    if rel is None or len(rel) != 8:
        return None
    r0, r1, r2, r3, r4, r5, r6, r7 = (int(c) for c in rel)
    if r1 != 0 or r2 != 0 or r3 != 0 or r4 != 0 or r5 != 0 or r6 != 0:
        return None
    if r7 == 0 or r0 == 0:
        return None
    if (-r0) % r7 != 0:
        return None
    return (-r0) // r7


def deep_verify(coeffs):
    K = eval_pcf_mpmath(coeffs, N_DEEP, DPS_DEEP)
    if K is None:
        return None
    info = classify_pslq(K, DPS_DEEP, PSLQ_HMAX_DEEP)
    rel = info.get("relation")
    residual_str = info.get("residual", "1")
    try:
        residual = mpf(residual_str)
    except Exception:
        residual = mpf(1)
    info["residual_lt_1e_200"] = bool(residual < mpf(10) ** (-200))
    info["L_60dps"] = mpmath.nstr(K, 60)
    info["n_log2"] = extract_n_log2(rel) if rel is not None else None
    return info


# ---------------------------------------------------------------------------
# Bauer-orbit / discriminant classifiers (carried from 044R)
# ---------------------------------------------------------------------------

def discriminant_identity_class(coeffs):
    a2, _a1, _a0, b1, _b0 = coeffs
    if 9 * a2 + 2 * b1 * b1 == 0:
        return "trans_stratum_proper"
    if 4 * a2 - b1 * b1 == 0:
        return "brouncker_boundary"
    return "neither"


def known_anchor_class(coeffs):
    """Identify whether a tuple is in the sign-orbit closure of one of the
    two known anchors. The sign-orbit closure of a tuple (a2,a1,a0,b1,b0) is
    taken as {(s_a*a2, s_a*a1, s_a*a0, s_b*b1, s_b*b0) : s_a, s_b in {-1,+1}}
    (a2,a1,a0 flip together since the numerator is a polynomial in n; b1,b0
    flip together since the linear-in-n denominator changes sign uniformly).

    Returns one of:
      "b7_singular_orbit"  -- in the sign-orbit of (8,-4,0,7,4)
      "b10_044r_orbit"     -- in the sign-orbit of (-9,0,0,10,5)
      None                 -- structurally distinct from both anchors
    """
    a2, a1, a0, b1, b0 = coeffs

    def _matches(anchor):
        ra2, ra1, ra0, rb1, rb0 = anchor
        for sa in (-1, 1):
            for sb in (-1, 1):
                if (sa * ra2, sa * ra1, sa * ra0, sb * rb1, sb * rb0) == \
                        (a2, a1, a0, b1, b0):
                    return True
        return False

    if _matches(B7_SINGULAR_COEFFS):
        return "b7_singular_orbit"
    if _matches(B10_044R_COEFFS):
        return "b10_044r_orbit"
    return None


def bauer_orbit_membership(coeffs):
    a2, a1, a0, b1, b0 = coeffs
    if a1 != 0 or a0 != 0:
        return {"on_orbit": False, "k": None, "reason": "a1 or a0 nonzero"}
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
                "reason": f"|b1|={abs(b1)} != 6*k={6 * k}"}
    if abs(b0) != 3 * k:
        return {"on_orbit": False, "k": k,
                "reason": f"|b0|={abs(b0)} != 3*k={3 * k}"}
    return {"on_orbit": True, "k": k,
            "sign_b1": "+" if b1 > 0 else "-",
            "sign_b0": "+" if b0 > 0 else "-",
            "predicted_L": f"{'+' if (b1 > 0) == (b0 > 0) else '-'}{2 * k}/log(2)"}


# ---------------------------------------------------------------------------
# STEP 1 - parse 044R outlier
# ---------------------------------------------------------------------------

def step1_parse_044r() -> dict:
    print("[STEP 1] parse 044R unexpected_finds.json", flush=True)
    if not SOURCE_044R_UFIND.exists():
        write_halt("HALT_044B_044R_OUTCOME_NOT_B_AT_H7",
                   {"reason": "source 044R unexpected_finds.json not found",
                    "path": str(SOURCE_044R_UFIND)})
    sha = file_sha256(SOURCE_044R_UFIND)
    payload = json.loads(SOURCE_044R_UFIND.read_text())
    hits = payload.get("off_orbit_n_log2_hits", [])
    if payload.get("off_orbit_n_log2_hit_count") != 1 or len(hits) != 1:
        write_halt("HALT_044B_OUTLIER_MISMATCH",
                   {"reason": "expected exactly 1 off-orbit n/log(2) hit",
                    "got_count": payload.get("off_orbit_n_log2_hit_count"),
                    "got_hits_len": len(hits)})
    h = hits[0]
    expected = EXPECTED_044R_HIT
    mismatch = []
    if h.get("b1") != expected["b1"]:
        mismatch.append(("b1", h.get("b1"), expected["b1"]))
    if list(h.get("coeffs", [])) != expected["coeffs"]:
        mismatch.append(("coeffs", h.get("coeffs"), expected["coeffs"]))
    if str(h.get("ratio")) != expected["ratio"]:
        mismatch.append(("ratio", h.get("ratio"), expected["ratio"]))
    if h.get("n") != expected["n"]:
        mismatch.append(("n", h.get("n"), expected["n"]))
    if mismatch:
        write_halt("HALT_044B_OUTLIER_MISMATCH",
                   {"reason": "044R hit fields do not match P2 reference",
                    "mismatch": mismatch})
    print(f"[STEP 1] 044R hit confirmed (b1={h['b1']}, "
          f"coeffs={h['coeffs']}, ratio={h['ratio']}, n={h['n']})", flush=True)
    print(f"[STEP 1] source SHA-256 = {sha}", flush=True)
    return {"sha256": sha, "hit": h}


# ---------------------------------------------------------------------------
# P5 b7 re-verify
# ---------------------------------------------------------------------------

def p5_b7_reverify() -> dict:
    print("[P5] re-verify b7 singular (8,-4,0,7,4) at dps=300", flush=True)
    K = eval_pcf_mpmath(B7_SINGULAR_COEFFS, N_DEEP, P5_DPS)
    if K is None:
        write_halt("HALT_044B_B7_RE-VERIFY_FAILED",
                   {"reason": "PCF evaluation returned None"})
    mp.dps = P5_DPS
    target = mpf(3) / mp.log(2)
    diff = abs(mpf(K) - target)
    diff_str = mpmath.nstr(diff, 12)
    print(f"[P5] L = {mpmath.nstr(K, 60)}", flush=True)
    print(f"[P5] |L - 3/log(2)| = {diff_str}", flush=True)
    if diff >= P5_RESIDUAL_TOL:
        write_halt("HALT_044B_B7_RE-VERIFY_FAILED",
                   {"reason": "|L - 3/log(2)| >= 1e-50",
                    "diff": diff_str,
                    "L": mpmath.nstr(K, 60)})
    # Also compute its full PSLQ at h<=1e9 to record relation
    info = classify_pslq(K, DPS_DEEP, PSLQ_HMAX_DEEP)
    rel = info.get("relation")
    n_extracted = extract_n_log2(rel) if rel is not None else None
    record = {
        "coeffs": list(B7_SINGULAR_COEFFS),
        "L_60dps": mpmath.nstr(K, 60),
        "diff_to_3_over_log2": diff_str,
        "diff_lt_1e_50": True,
        "p5_dps": P5_DPS,
        "p5_residual_tol": "1e-50",
        "pslq_relation": rel,
        "pslq_basis": info.get("basis"),
        "pslq_residual": info.get("residual"),
        "n_extracted": n_extracted,
        "ratio": str(Fraction(B7_SINGULAR_COEFFS[0],
                               B7_SINGULAR_COEFFS[3] ** 2)),
    }
    print(f"[P5] PASS  n_extracted={n_extracted} relation={rel}", flush=True)
    return record


# ---------------------------------------------------------------------------
# STEP 2A - sign-orbit
# ---------------------------------------------------------------------------

def step2a_sign_orbit(t_start: float) -> list[dict]:
    print("[STEP 2A] sign-orbit (8 tuples, dps=300, h<=1e9)", flush=True)
    out = []
    for coeffs in SIGN_ORBIT_TUPLES:
        if time.time() - t_start > WALL_BUDGET_SECONDS:
            write_halt("HALT_044B_WALL_BUDGET",
                       {"phase": "STEP 2A",
                        "elapsed_s": time.time() - t_start,
                        "completed_tuples": len(out),
                        "total_tuples": len(SIGN_ORBIT_TUPLES)})
        t_t = time.time()
        K = eval_pcf_mpmath(coeffs, N_DEEP, DPS_DEEP)
        if K is None:
            out.append({"coeffs": list(coeffs), "label": "eval_fail"})
            continue
        info = classify_pslq(K, DPS_DEEP, PSLQ_HMAX_DEEP)
        rel = info.get("relation")
        n_extracted = extract_n_log2(rel) if rel is not None else None
        bauer = bauer_orbit_membership(coeffs)
        disc = discriminant_identity_class(coeffs)
        ratio = Fraction(coeffs[0], coeffs[3] ** 2)
        # off-orbit = NOT on Bauer + NOT brouncker_boundary
        #             + NOT trans_stratum_proper + clean n/log(2) PSLQ
        off_orbit = (
            (not bauer["on_orbit"])
            and disc == "neither"
            and info.get("label") == "Log"
            and n_extracted is not None
        )
        rec = {
            "coeffs": list(coeffs),
            "ratio": str(ratio),
            "ratio_float": float(ratio),
            "L_60dps": mpmath.nstr(K, 60),
            "label": info.get("label"),
            "relation": rel,
            "basis": info.get("basis"),
            "residual": info.get("residual"),
            "n_extracted": n_extracted,
            "bauer_orbit": bauer,
            "discriminant_identity_class": disc,
            "off_orbit_n_log2": off_orbit,
            "elapsed_s": time.time() - t_t,
        }
        out.append(rec)
        print(f"  {coeffs}  ratio={ratio}  label={info.get('label')}  "
              f"n={n_extracted}  off_orbit={off_orbit}", flush=True)
    return out


# ---------------------------------------------------------------------------
# STEP 2B - Bauer-shape family
# ---------------------------------------------------------------------------

def enumerate_bauer_family() -> list[tuple]:
    out = []
    for k in BAUER_K_VALUES:
        for b1_mag in BK_EXPLICIT[k]:
            for b1_sign in (-1, 1):
                b1 = b1_sign * b1_mag
                a2 = -(k * k)
                for b0 in B0_RANGE:
                    out.append((a2, 0, 0, b1, b0))
    return out


def stage_b_worker(item):
    idx, coeffs = item
    try:
        K = eval_pcf_mpmath(coeffs, N_STAGE_BC, DPS_STAGE_BC)
    except Exception as exc:
        return (idx, {"label": "eval_fail", "error": str(exc)})
    if K is None:
        return (idx, {"label": "eval_fail"})
    info = classify_pslq(K, DPS_STAGE_BC, PSLQ_HMAX_STAGE_B)
    return (idx, info)


def step2b_bauer_family(t_start: float) -> dict:
    print("[STEP 2B] Bauer-shape family", flush=True)
    families = enumerate_bauer_family()
    print(f"[STEP 2B] enumerated {len(families)} candidate tuples", flush=True)

    # Stage A : float K_500 screen
    print("[STEP 2B] Stage A K_500 float screen", flush=True)
    t_a = time.time()
    convergent: list[tuple[int, tuple]] = []
    stage_a_records = []
    for i, coeffs in enumerate(families):
        v = stage_a_converge_float(coeffs)
        if v is not None:
            convergent.append((i, coeffs))
            stage_a_records.append({"idx": i, "coeffs": list(coeffs),
                                    "K_float": v})
    print(f"[STEP 2B] Stage A: {len(convergent)}/{len(families)} convergent "
          f"in {time.time() - t_a:.1f}s", flush=True)

    # Stage B / C : PSLQ dps=150 h<=1e7
    print(f"[STEP 2B] Stage B PSLQ dps=150 h<={PSLQ_HMAX_STAGE_B}", flush=True)
    t_b = time.time()
    stage_b_results: list[dict] = []
    workers = max(1, min(7, (os.cpu_count() or 4) - 1))
    tasks = list(enumerate(c for _, c in convergent))
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(stage_b_worker, t): t[0] for t in tasks}
        completed = 0
        for fut in concurrent.futures.as_completed(futures):
            if time.time() - t_start > WALL_BUDGET_SECONDS:
                write_halt("HALT_044B_WALL_BUDGET",
                           {"phase": "STEP 2B Stage B",
                            "elapsed_s": time.time() - t_start,
                            "completed": completed,
                            "total": len(tasks)})
            try:
                idx, info = fut.result()
            except Exception as exc:
                idx = futures[fut]
                info = {"label": "worker_fail", "error": str(exc)}
            base_idx = convergent[idx][0]
            coeffs = convergent[idx][1]
            stage_b_results.append({"idx": base_idx,
                                    "coeffs": list(coeffs),
                                    **info})
            completed += 1
            if completed % 100 == 0:
                print(f"  [Stage B] {completed}/{len(tasks)} "
                      f"({time.time() - t_b:.1f}s)", flush=True)
    print(f"[STEP 2B] Stage B: {len(stage_b_results)} results in "
          f"{time.time() - t_b:.1f}s", flush=True)

    # Stage C : ratio-pattern test for m/log(2) on Log-classified hits
    log_hits = [r for r in stage_b_results if r.get("label") == "Log"]
    trans_hits = [r for r in stage_b_results if r.get("label") == "Trans"]
    phantoms = [r for r in stage_b_results if r.get("label") == "Phantom"]
    print(f"[STEP 2B] Stage C: {len(log_hits)} Log + {len(trans_hits)} Trans + "
          f"{len(phantoms)} Phantom", flush=True)

    # Stage D : deep-verify dps=300 h<=1e9 on Log+Trans hits
    deep_records: list[dict] = []
    for r in log_hits + trans_hits:
        if time.time() - t_start > WALL_BUDGET_SECONDS:
            write_halt("HALT_044B_WALL_BUDGET",
                       {"phase": "STEP 2B Stage D",
                        "elapsed_s": time.time() - t_start,
                        "completed_deep": len(deep_records),
                        "total_deep": len(log_hits) + len(trans_hits)})
        coeffs = tuple(r["coeffs"])
        info = deep_verify(coeffs)
        n_log2 = info.get("n_log2") if info else None
        bauer = bauer_orbit_membership(coeffs)
        disc = discriminant_identity_class(coeffs)
        ratio = Fraction(coeffs[0], coeffs[3] ** 2)
        off_orbit = (
            (not bauer["on_orbit"])
            and disc == "neither"
            and r.get("label") == "Log"
            and n_log2 is not None
            and info is not None
            and info.get("residual_lt_1e_200")
        )
        rec = {
            "coeffs": list(coeffs),
            "stage_b_label": r.get("label"),
            "stage_b_relation": r.get("relation"),
            "deep": info,
            "ratio": str(ratio),
            "ratio_float": float(ratio),
            "n_log2_extracted": n_log2,
            "bauer_orbit": bauer,
            "discriminant_identity_class": disc,
            "off_orbit_n_log2": off_orbit,
        }
        deep_records.append(rec)
        if off_orbit:
            print(f"  [Stage D] OFF-ORBIT  {coeffs} ratio={ratio} n={n_log2}",
                  flush=True)

    return {
        "enumeration_total": len(families),
        "stage_a_convergent": len(convergent),
        "stage_a_records": stage_a_records,
        "stage_b_results": stage_b_results,
        "stage_b_log_count": len(log_hits),
        "stage_b_trans_count": len(trans_hits),
        "stage_b_phantom_count": len(phantoms),
        "stage_d_records": deep_records,
    }


# ---------------------------------------------------------------------------
# STEP 3 - ratio-pattern fit + n=3 anchor count
# ---------------------------------------------------------------------------

def ratio_pattern_fit(anchors: list[dict]) -> dict:
    """Fit a degree<=2 polynomial phi(b1) to the (b1, ratio) anchors.

    Anchors must be a list of {"coeffs": [a2,a1,a0,b1,b0]} dicts.
    Returns dict with fit details. Reports residuals at each anchor.
    """
    pts = [(int(a["coeffs"][3]),
            Fraction(int(a["coeffs"][0]), int(a["coeffs"][3]) ** 2))
           for a in anchors]
    # Deduplicate by b1 (different b1 magnitudes are different anchors;
    # same b1 different a2 should not happen for these anchor families).
    unique = list({(b, r): None for b, r in pts}.keys())
    res = {"anchors": [{"b1": b, "ratio": str(r)} for b, r in unique],
           "n_anchors": len(unique)}
    if len(unique) < 2:
        res["fit"] = "underdetermined (need >=2 anchors)"
        return res
    # Linear (degree 1) fit through first two points (and over-determined
    # check if more than 2)
    (b_a, r_a), (b_b, r_b) = unique[0], unique[1]
    if b_a == b_b:
        res["fit"] = "two anchors at same b1; cannot fit"
        return res
    slope = (r_b - r_a) / (b_b - b_a)
    intercept = r_a - slope * b_a
    res["linear_fit"] = {
        "form": "phi(b1) = slope * b1 + intercept",
        "slope": str(slope),
        "intercept": str(intercept),
    }
    # Residuals at each anchor under this linear fit
    lin_res = []
    for b, r in unique:
        pred = slope * b + intercept
        lin_res.append({"b1": b, "ratio": str(r),
                        "predicted": str(pred),
                        "residual": str(r - pred)})
    res["linear_residuals"] = lin_res
    # Search for an integer relation m*a2 + n*b1 + p = 0 across anchors
    # (solve over the first two anchors; check residual at others)
    a2_vals = [int(a["coeffs"][0]) for a in anchors]
    b1_vals = [int(a["coeffs"][3]) for a in anchors]
    integer_relation = None
    if len(anchors) >= 2:
        a2_a, b1_a = a2_vals[0], b1_vals[0]
        a2_b, b1_b = a2_vals[1], b1_vals[1]
        # Solve m*a2 + n*b1 + p = 0 with m,n,p coprime integers
        # using the two equations: m*a2_a + n*b1_a + p = 0
        #                          m*a2_b + n*b1_b + p = 0
        # Subtract: m*(a2_a - a2_b) + n*(b1_a - b1_b) = 0
        # so (m, n) proportional to (b1_b - b1_a, a2_a - a2_b)
        m = b1_b - b1_a
        n = a2_a - a2_b
        if m != 0 or n != 0:
            g = math.gcd(abs(m), abs(n)) or 1
            m //= g
            n //= g
            p = -(m * a2_a + n * b1_a)
            g2 = math.gcd(math.gcd(abs(m), abs(n)), abs(p)) or 1
            m //= g2
            n //= g2
            p //= g2
            # Compute residual at all anchors
            residuals = [m * a + n * b + p for a, b in zip(a2_vals, b1_vals)]
            integer_relation = {
                "form": "m*a2 + n*b1 + p = 0",
                "m": m, "n": n, "p": p,
                "residuals_at_anchors": residuals,
                "fits_all": all(r == 0 for r in residuals),
                "max_abs_denom": max(abs(m), abs(n), abs(p)),
            }
    res["integer_relation"] = integer_relation
    return res


# ---------------------------------------------------------------------------
# STEP 4 - classify outcome
# ---------------------------------------------------------------------------

def classify_outcome(off_orbit_hits: list[dict],
                     anchors_n3_count: int,
                     fit_residual_le_1e_50: bool,
                     curve_residual_le_1e_200: bool) -> tuple[str, dict]:
    n_hits = len(off_orbit_hits)
    all_n3 = all(int(h.get("n_log2_extracted") or h.get("n_extracted")) == 3
                 for h in off_orbit_hits) if n_hits > 0 else True
    distinct_n = sorted({int(h.get("n_log2_extracted") or h.get("n_extracted"))
                         for h in off_orbit_hits if h.get("n_log2_extracted")
                         or h.get("n_extracted")})
    if n_hits == 0:
        return ("B-T-A", {
            "interpretation": (
                "Zero new off-orbit n/log(2) hits in STEP 2A and 2B. "
                "b7 + b10 044R remain the only two known data points. "
                "n=3 coincidence consistent with isolated outliers at "
                "h <= 10^9. Two known data points at h <= 10^9; bounded "
                "evidence, not absolute."
            ),
            "off_orbit_hit_count": 0,
            "anchors_n3_count": anchors_n3_count,
            "all_n3": True,
            "distinct_n": [3],
        })
    structural = curve_residual_le_1e_200 and (n_hits >= 2)
    if n_hits >= 4 or (structural and len(distinct_n) > 1) or \
       (curve_residual_le_1e_200 and n_hits >= 2 and len(distinct_n) >= 2):
        return ("B-T-C", {
            "interpretation": (
                "STRUCTURAL_4TH_LAW_PROBABLE. >=4 new off-orbit "
                "n/log(2) hits OR clear structural pattern. HALT cascade."
            ),
            "off_orbit_hit_count": n_hits,
            "off_orbit_hits": off_orbit_hits,
            "all_n3": all_n3,
            "distinct_n": distinct_n,
            "curve_fit_residual_le_1e_200": curve_residual_le_1e_200,
        })
    # 1..3 hits with n=3 -> B-T-B
    if 1 <= n_hits <= 3 and all_n3:
        return ("B-T-B", {
            "interpretation": (
                "CANDIDATE_4TH_LAW_HARDEN. 1-3 new off-orbit n/log(2) "
                "hits with n=3. T1 Synthesizer arbitration request "
                "queued for next weekly cadence."
            ),
            "off_orbit_hit_count": n_hits,
            "off_orbit_hits": off_orbit_hits,
            "anchors_n3_count": anchors_n3_count,
            "all_n3": True,
            "distinct_n": [3],
        })
    # Mixed n in [1..3] hits -> upgrade to B-T-C structural cue
    return ("B-T-C", {
        "interpretation": (
            "STRUCTURAL_4TH_LAW_PROBABLE (mixed n at multiple anchors)."
        ),
        "off_orbit_hit_count": n_hits,
        "off_orbit_hits": off_orbit_hits,
        "all_n3": all_n3,
        "distinct_n": distinct_n,
    })


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    t_start = time.time()
    print(f"[INIT] script_sha256 = {script_sha256()}", flush=True)
    print(f"[INIT] task_id       = {TASK_ID}", flush=True)
    print(f"[INIT] relay_prompt  = {RELAY_PROMPT}", flush=True)

    # STEP 1
    step1 = step1_parse_044r()

    # P5 b7 re-verify
    p5 = p5_b7_reverify()

    # STEP 2A
    step2a = step2a_sign_orbit(t_start)

    # STEP 2B
    step2b = step2b_bauer_family(t_start)

    # Aggregate all off-orbit n/log(2) hits found in STEP 2A and STEP 2B,
    # then partition into known-anchor-orbit closures vs structurally new
    # hits. Per the relay 044B prompt, "new off-orbit n/log(2) hits" for
    # STEP 4 outcome classification means tuples NOT in the sign-orbit
    # closure of {b7 singular (8,-4,0,7,4), b10 044R (-9,0,0,10,5)}.
    raw_hits: list[dict] = []
    for r in step2a:
        if r.get("off_orbit_n_log2"):
            raw_hits.append({
                "source": "step2a_sign_orbit",
                "coeffs": r["coeffs"],
                "ratio": r["ratio"],
                "n_log2_extracted": r["n_extracted"],
                "deep_residual": r["residual"],
            })
    for r in step2b["stage_d_records"]:
        if r.get("off_orbit_n_log2"):
            raw_hits.append({
                "source": "step2b_bauer_family",
                "coeffs": r["coeffs"],
                "ratio": r["ratio"],
                "n_log2_extracted": r["n_log2_extracted"],
                "deep_residual": (r["deep"] or {}).get("residual"),
            })

    # Dedupe by tuple (same coeffs from STEP 2A and STEP 2B is one datum).
    deduped: dict[tuple, dict] = {}
    for h in raw_hits:
        key = tuple(h["coeffs"])
        if key in deduped:
            # Merge sources for traceability.
            existing = deduped[key]
            srcs = existing.get("sources", [existing["source"]])
            if h["source"] not in srcs:
                srcs.append(h["source"])
            existing["sources"] = srcs
        else:
            entry = dict(h)
            entry["sources"] = [h["source"]]
            entry["known_anchor_class"] = known_anchor_class(tuple(h["coeffs"]))
            deduped[key] = entry

    deduped_hits = list(deduped.values())
    known_orbit_hits = [h for h in deduped_hits
                        if h["known_anchor_class"] is not None]
    new_off_orbit_hits = [h for h in deduped_hits
                          if h["known_anchor_class"] is None]

    print(f"[AGG] raw_hit_records={len(raw_hits)} "
          f"deduped_unique_tuples={len(deduped_hits)} "
          f"known_anchor_orbit={len(known_orbit_hits)} "
          f"new_off_orbit={len(new_off_orbit_hits)}", flush=True)

    # off_orbit_hits used for STEP 4 outcome classification = NEW only.
    off_orbit_hits = new_off_orbit_hits

    # STEP 3 - ratio-pattern fit
    anchors = [
        {"coeffs": list(B7_SINGULAR_COEFFS),
         "ratio": str(Fraction(B7_SINGULAR_COEFFS[0],
                                B7_SINGULAR_COEFFS[3] ** 2)),
         "n_log2_extracted": 3,
         "source": "b7_singular"},
        {"coeffs": list(B10_044R_COEFFS),
         "ratio": str(Fraction(B10_044R_COEFFS[0],
                                B10_044R_COEFFS[3] ** 2)),
         "n_log2_extracted": 3,
         "source": "b10_044r"},
    ]
    all_anchors = anchors + off_orbit_hits
    fit = ratio_pattern_fit(all_anchors)

    anchors_n3_count = sum(
        1 for a in all_anchors
        if int(a.get("n_log2_extracted") or 0) == 3
    )

    # Curve residual check (degree-2/denom<=30 polynomial fit)
    curve_residual_le_1e_200 = bool(
        fit.get("integer_relation")
        and fit["integer_relation"].get("fits_all")
        and fit["integer_relation"]["max_abs_denom"] <= 30
        and len(all_anchors) >= 3
    )
    fit_residual_le_1e_50 = curve_residual_le_1e_200

    # STEP 4 - classify
    outcome_tag, outcome_details = classify_outcome(
        off_orbit_hits,
        anchors_n3_count,
        fit_residual_le_1e_50,
        curve_residual_le_1e_200,
    )

    wall_total = time.time() - t_start
    if wall_total > WALL_BUDGET_SECONDS:
        # Already would have halted earlier; final guard
        write_halt("HALT_044B_WALL_BUDGET",
                   {"phase": "post-classification",
                    "elapsed_s": wall_total})

    # ----- Write artifacts -----
    results = {
        "task_id": TASK_ID,
        "relay_prompt": RELAY_PROMPT,
        "script_sha256": script_sha256(),
        "anchor_044R_commit": "fe15737",
        "source_044R_unexpected_finds_sha256": step1["sha256"],
        "step1_parse_044r": step1,
        "p5_b7_reverify": p5,
        "step2a_sign_orbit": step2a,
        "step2b_bauer_family_summary": {
            "enumeration_total": step2b["enumeration_total"],
            "stage_a_convergent": step2b["stage_a_convergent"],
            "stage_b_log_count": step2b["stage_b_log_count"],
            "stage_b_trans_count": step2b["stage_b_trans_count"],
            "stage_b_phantom_count": step2b["stage_b_phantom_count"],
            "stage_d_record_count": len(step2b["stage_d_records"]),
            "stage_d_off_orbit_count": sum(
                1 for r in step2b["stage_d_records"]
                if r.get("off_orbit_n_log2")
            ),
        },
        "off_orbit_hits": off_orbit_hits,
        "off_orbit_hits_classification": {
            "raw_hit_record_count": len(raw_hits),
            "deduped_unique_tuple_count": len(deduped_hits),
            "known_anchor_orbit_count": len(known_orbit_hits),
            "known_anchor_orbit_hits": known_orbit_hits,
            "new_off_orbit_count": len(new_off_orbit_hits),
            "new_off_orbit_hits": new_off_orbit_hits,
            "rationale": (
                "STEP 4 outcome classification counts only structurally "
                "new tuples (NOT in the sign-orbit closure of {b7 "
                "singular (8,-4,0,7,4), b10 044R (-9,0,0,10,5)}). "
                "STEP 2A is the sign-orbit closure of b10 044R BY "
                "DEFINITION; any hit inside it is structurally the same "
                "datum. Likewise the Bauer-shape sweep includes the "
                "044R tuple as one of its parameter cells; a re-discovery "
                "there is not a new data point."
            ),
        },
        "ratio_pattern_fit": fit,
        "anchors_n3_count": anchors_n3_count,
        "outcome_tag": outcome_tag,
        "outcome_details": outcome_details,
        "wall_s": wall_total,
        "wall_budget_s": WALL_BUDGET_SECONDS,
        "completed_at_local_iso": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    # Full per-record stage_d records as a separate artifact key
    results["step2b_stage_d_records"] = step2b["stage_d_records"]
    # Stage A records: large; keep only summary count to save space
    results["step2b_stage_a_records_count"] = len(step2b["stage_a_records"])

    RESULTS_FILE.write_text(json.dumps(results, indent=2, default=str))

    # unexpected_finds.json
    unex = {
        "new_off_orbit_n_log2_hit_count": len(off_orbit_hits),
        "new_off_orbit_n_log2_hits": off_orbit_hits,
        "known_anchor_orbit_hit_count": len(known_orbit_hits),
        "known_anchor_orbit_hits": known_orbit_hits,
        "deduped_unique_tuple_count": len(deduped_hits),
        "raw_hit_record_count": len(raw_hits),
        "anchors_n3_count": anchors_n3_count,
        "outcome_tag": outcome_tag,
        "ratio_pattern_fit_summary": {
            "integer_relation": fit.get("integer_relation"),
            "linear_fit": fit.get("linear_fit"),
        },
        "dedup_rationale": (
            "new_off_orbit count excludes the sign-orbit closure of the "
            "two known anchors {b7 singular (8,-4,0,7,4), b10 044R "
            "(-9,0,0,10,5)}."
        ),
    }
    UNEX_FILE.write_text(json.dumps(unex, indent=2, default=str))

    # discrepancy_log: empty unless 044R outlier mismatched (we already
    # halted in STEP 1 if that were the case)
    DISC_FILE.write_text(json.dumps({}, indent=2))

    # halt_log: empty if no halt
    if not HALT_FILE.exists():
        HALT_FILE.write_text(json.dumps({}, indent=2))

    # claims.jsonl (>=8 entries)
    claims = build_claims(
        step1=step1, p5=p5, step2a=step2a, step2b=step2b,
        off_orbit_hits=off_orbit_hits, anchors_n3_count=anchors_n3_count,
        fit=fit, outcome_tag=outcome_tag,
        outcome_details=outcome_details,
        raw_hits=raw_hits, deduped_hits=deduped_hits,
        known_orbit_hits=known_orbit_hits,
    )
    with CLAIMS_FILE.open("w", encoding="utf-8", newline="\n") as fh:
        for c in claims:
            fh.write(json.dumps(c, default=str) + "\n")

    # Final summary print
    print("=" * 60, flush=True)
    print(f"[DONE] outcome_tag = {outcome_tag}", flush=True)
    print(f"[DONE] off_orbit_hit_count = {len(off_orbit_hits)}", flush=True)
    print(f"[DONE] anchors_n3_count = {anchors_n3_count}", flush=True)
    print(f"[DONE] wall = {wall_total:.1f}s "
          f"(budget {WALL_BUDGET_SECONDS}s)", flush=True)
    print("=" * 60, flush=True)

    # If outcome is B-T-C, halt explicitly
    if outcome_tag == "B-T-C":
        write_halt("HALT_044B_B-T-C_FIRED",
                   {"reason": "STEP 4 outcome B-T-C",
                    "off_orbit_hit_count": len(off_orbit_hits),
                    "off_orbit_hits": off_orbit_hits,
                    "anchors_n3_count": anchors_n3_count})


def build_claims(*, step1, p5, step2a, step2b, off_orbit_hits,
                 anchors_n3_count, fit, outcome_tag, outcome_details,
                 raw_hits, deduped_hits, known_orbit_hits):
    """Build the >=8 AEAL claims required by relay 044B STEP 5."""
    out_hash = lambda obj: hashlib.sha256(
        json.dumps(obj, sort_keys=True, default=str).encode()
    ).hexdigest()

    claims = []

    # 044B-A1 sign-orbit closure (8 tuples)
    a1_payload = {
        "tuples": [r["coeffs"] for r in step2a],
        "labels": [r["label"] for r in step2a],
        "L_60dps": [r.get("L_60dps") for r in step2a],
        "relations": [r.get("relation") for r in step2a],
    }
    claims.append({
        "claim_id": "044B-A1",
        "claim": ("Sign-orbit of 044R hit closed: 8 tuples "
                  "(a2,b1,b0)=(+/-9,+/-10,+/-5),a1=a0=0 evaluated at "
                  "dps=300 with PSLQ at h<=1e9; per-tuple labels and "
                  "relations recorded."),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a1_payload),
        "step": "STEP 2A",
    })

    # 044B-A2 Bauer-shape family enumeration
    a2_payload = {
        "enumeration_total": step2b["enumeration_total"],
        "stage_a_convergent": step2b["stage_a_convergent"],
        "stage_b_log_count": step2b["stage_b_log_count"],
        "stage_b_trans_count": step2b["stage_b_trans_count"],
        "stage_b_phantom_count": step2b["stage_b_phantom_count"],
        "stage_d_off_orbit_hits": [
            r for r in step2b["stage_d_records"]
            if r.get("off_orbit_n_log2")
        ],
        "k_values": BAUER_K_VALUES,
        "BK_explicit": BK_EXPLICIT,
        "b0_range": [B0_RANGE[0], B0_RANGE[-1]],
    }
    claims.append({
        "claim_id": "044B-A2",
        "claim": ("Bauer-shape family ((-k^2,0,0,b1,b0)) enumerated for "
                  "k in {1..5} at b1 in B(k)\\{+/-6k}, b0 in [-7,7]; "
                  "Stage A K_500 convergence + Stage B PSLQ dps=150 "
                  "h<=1e7 + Stage D deep-verify dps=300 h<=1e9 on "
                  "Log/Trans hits; off-orbit n/log(2) hit list reported."),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a2_payload),
        "step": "STEP 2B",
    })

    # 044B-A3 b7 re-verify
    a3_payload = {
        "coeffs": list(B7_SINGULAR_COEFFS),
        "L_60dps": p5["L_60dps"],
        "diff_to_3_over_log2": p5["diff_to_3_over_log2"],
        "diff_lt_1e_50": p5["diff_lt_1e_50"],
        "p5_dps": p5["p5_dps"],
        "n_extracted": p5["n_extracted"],
    }
    claims.append({
        "claim_id": "044B-A3",
        "claim": ("b7 singular (8,-4,0,7,4) re-verified: L = 3/log(2) at "
                  "dps=300 with |L - 3/log(2)| < 1e-50; n_extracted=3 "
                  "from PSLQ relation in 8-element transcendental basis."),
        "evidence_type": "computation",
        "dps": p5["p5_dps"],
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a3_payload),
        "step": "P5 / STEP 2C",
    })

    # 044B-A4 ratio-pattern fit
    a4_payload = {
        "anchors": fit.get("anchors"),
        "linear_fit": fit.get("linear_fit"),
        "linear_residuals": fit.get("linear_residuals"),
        "integer_relation": fit.get("integer_relation"),
        "n_anchors": fit.get("n_anchors"),
    }
    claims.append({
        "claim_id": "044B-A4",
        "claim": ("Ratio-pattern phi(b1) fit through anchors b7 (a2=8,b1=7) "
                  "and b10 (a2=-9,b1=10) plus all new off-orbit hits; "
                  "linear and integer-relation fits with per-anchor "
                  "residuals reported. NOTE: residuals reported with "
                  "no claim of structural identity (T1 Synthesizer "
                  "question)."),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a4_payload),
        "step": "STEP 3",
    })

    # 044B-A5 n=3 anchor count
    a5_payload = {
        "anchors_n3_count": anchors_n3_count,
        "all_anchors_summary": [
            {"coeffs": list(B7_SINGULAR_COEFFS), "n": 3, "source": "b7_singular"},
            {"coeffs": list(B10_044R_COEFFS), "n": 3, "source": "b10_044r"},
        ] + [
            {"coeffs": h["coeffs"],
             "n": h["n_log2_extracted"],
             "source": h["source"]}
            for h in off_orbit_hits
        ],
    }
    claims.append({
        "claim_id": "044B-A5",
        "claim": (f"n=3 anchor count among all anchors + new hits: "
                  f"{anchors_n3_count}. The n=3 collision is an EMPIRICAL "
                  "observation; structural identity (Brouncker-Stieltjes-"
                  "Wallis triangle, Bauer-Forrester pencil, or other) is "
                  "a T1 Synthesizer question, not a 044B claim."),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a5_payload),
        "step": "STEP 3",
    })

    # 044B-A6 outcome
    a6_payload = {
        "outcome_tag": outcome_tag,
        "outcome_details": outcome_details,
        "new_off_orbit_hit_count": len(off_orbit_hits),
        "new_off_orbit_hits": off_orbit_hits,
        "raw_hit_record_count": len(raw_hits),
        "deduped_unique_tuple_count": len(deduped_hits),
        "known_anchor_orbit_count": len(known_orbit_hits),
        "known_anchor_orbit_hits": known_orbit_hits,
    }
    claims.append({
        "claim_id": "044B-A6",
        "claim": (f"044B outcome classification: {outcome_tag}. "
                  f"new_off_orbit_hit_count = {len(off_orbit_hits)}; "
                  f"deduped_unique_tuple_count = {len(deduped_hits)}; "
                  f"known_anchor_orbit_hits (excluded from new count) = "
                  f"{len(known_orbit_hits)}. Full lists in results.json. "
                  "h-bound qualifiers h<=1e9 (sign-orbit + deep-verify) "
                  "and h<=1e7 (Bauer-shape Stage B) carried."),
        "evidence_type": "computation",
        "dps": DPS_DEEP,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": out_hash(a6_payload),
        "step": "STEP 4",
    })

    # 044B-A7 source 044R unexpected_finds.json provenance
    a7_payload = {
        "source_path": str(SOURCE_044R_UFIND.relative_to(SOURCE_044R_UFIND.parents[3])),
        "sha256": step1["sha256"],
        "hit": step1["hit"],
    }
    claims.append({
        "claim_id": "044B-A7",
        "claim": ("Source 044R unexpected_finds.json SHA-256 captured: "
                  f"{step1['sha256']}. Provenance anchor for off-orbit "
                  "outlier (10,5,-9,0,0,-9/100,3) referenced throughout "
                  "044B."),
        "evidence_type": "provenance",
        "dps": 0,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": step1["sha256"],
        "step": "STEP 1",
    })

    # 044B-A8 sweep script SHA
    a8_sha = script_sha256()
    claims.append({
        "claim_id": "044B-A8",
        "claim": (f"044B sweep script SHA-256: {a8_sha}. Script defines "
                  "the deterministic harness for sign-orbit + Bauer-shape "
                  "family + co-anchor analysis."),
        "evidence_type": "provenance",
        "dps": 0,
        "reproducible": True,
        "script": "t2b_tightened_sweep.py",
        "output_hash": a8_sha,
        "step": "STEP 5 / harness",
    })

    return claims


if __name__ == "__main__":
    main()
