"""T2C Layer 5 — Precision Escalation Monitor

Discriminate genuine Trans CF limits (slope of log(residual) vs dps ≈ -1)
from spurious near-hits (slope ≈ 0).

PCF convention used throughout:
    a(n) = a2 * n^2 + a1 * n + a0
    b(n) = b1 * n + b0           (b2 = 0 for all Trans families considered)
    L    = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...))

Coefficient ordering for stored tuples in this script: (a2, a1, a0, b1, b0).
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass, asdict
from pathlib import Path

import mpmath as mp

OUT_DIR = Path(__file__).resolve().parent
RESULTS_JSON = OUT_DIR / "precision_escalation_results.json"

DPS_LEVELS = [50, 100, 150, 200, 250, 300]


# -----------------------------------------------------------------------------
# 24 Trans families (a2, a1, a0, b1, b0) — from F1-TRANS-STRUCTURE catalogue.
# Stored as [a2, a1, a0] / [0, b1, b0] in the original dataset; b2 = 0 always.
# -----------------------------------------------------------------------------
TRANS_FAMILIES = [
    ("T01_116433", (-2, -3, -1, -3, -4)),
    ("T02_116447", (-2, -3, -1,  3,  4)),
    ("T03_118473", (-2, -3,  2, -3, -4)),
    ("T04_118474", (-2, -3,  2, -3, -3)),
    ("T05_118486", (-2, -3,  2,  3,  3)),
    ("T06_118487", (-2, -3,  2,  3,  4)),
    ("T07_130100", (-2, -1,  1, -3, -4)),
    ("T08_130101", (-2, -1,  1, -3, -3)),
    ("T09_130102", (-2, -1,  1, -3, -2)),
    ("T10_130116", (-2, -1,  1,  3,  2)),
    ("T11_130117", (-2, -1,  1,  3,  3)),
    ("T12_130118", (-2, -1,  1,  3,  4)),
    ("T13_143930", (-2,  1,  3, -3, -4)),
    ("T14_143931", (-2,  1,  3, -3, -3)),
    ("T15_143932", (-2,  1,  3, -3, -2)),
    ("T16_143933", (-2,  1,  3, -3, -1)),
    ("T17_143934", (-2,  1,  3, -3,  0)),
    ("T18_143948", (-2,  1,  3,  3,  0)),
    ("T19_143949", (-2,  1,  3,  3,  1)),
    ("T20_143950", (-2,  1,  3,  3,  2)),
    ("T21_143951", (-2,  1,  3,  3,  3)),
    ("T22_143952", (-2,  1,  3,  3,  4)),
    ("T23_321561", ( 1,  2,  1, -2, -3)),
    ("T24_321601", ( 1,  2,  1,  2,  3)),
]


# -----------------------------------------------------------------------------
# Control families.
# Log-class: a=[0,0,-1], b=[0,b1,b0] with b1=±6, b0=±3 → L = ±2/log(2).
# Alg-class: simple periodic CFs with known algebraic limits.
# -----------------------------------------------------------------------------
LOG_FAMILIES = [
    ("L01_log_p63", ( -1,  0,  0,  6,  3)),  # L =  2/log(2)
    ("L02_log_n63", ( -1,  0,  0, -6, -3)),  # L = -2/log(2)
    ("L03_log_p7",  ( -1,  0,  0,  7,  0)),  # b1=7 control, ratio -1/49 (off -1/36)
]

# Simple algebraic-limit periodic CFs (a constant, b constant; b1=0 here).
# These are NOT in the deg-(2,1) Trans search space but provide a clean Alg
# control: PSLQ should latch onto sqrt(2), golden ratio, sqrt(13).
ALG_FAMILIES = [
    # a(n)=1, b(n)=2 → L = 2 + 1/(2 + ...) = 1 + sqrt(2). PSLQ relation: L - sqrt(2) - 1.
    ("A01_1psqrt2", ( 0,  0,  1,  0,  2)),
    # a(n)=1, b(n)=1 → L = (1+sqrt(5))/2. PSLQ: 2L - sqrt(5) - 1.
    ("A02_phi",     ( 0,  0,  1,  0,  1)),
    # a(n)=2, b(n)=2 → x = 2 + 2/x → x = 1 + sqrt(3). PSLQ: L - sqrt(3) - 1.
    ("A03_1psqrt3", ( 0,  0,  2,  0,  2)),
]


# -----------------------------------------------------------------------------
# Continued fraction evaluation (backward recurrence).
# -----------------------------------------------------------------------------
def cf_limit(coeffs, dps: int, depth: int) -> mp.mpf:
    """Evaluate L = b(0) + a(1)/(b(1) + a(2)/(b(2) + ...)) at given dps & depth.

    coeffs = (a2, a1, a0, b1, b0).
    """
    a2, a1, a0, b1, b0 = coeffs
    mp.mp.dps = dps + 20
    a2m, a1m, a0m = mp.mpf(a2), mp.mpf(a1), mp.mpf(a0)
    b1m, b0m = mp.mpf(b1), mp.mpf(b0)

    # Backward recurrence from depth N down to 1.
    # tail_n = a(n) / (b(n) + tail_{n+1}); start tail_{N+1} = 0.
    tail = mp.mpf(0)
    for n in range(depth, 0, -1):
        an = a2m * n * n + a1m * n + a0m
        bn = b1m * n + b0m
        if bn + tail == 0:
            # Avoid division by zero: shift slightly via larger depth on retry.
            return mp.nan
        tail = an / (bn + tail)
    return b0m + tail


def cf_limit_stable(coeffs, dps: int) -> mp.mpf:
    """Compute L with depth chosen so the tail change between two depths is below 10^-(dps+10)."""
    base_depth = max(800, 12 * dps)
    L1 = cf_limit(coeffs, dps, base_depth)
    L2 = cf_limit(coeffs, dps, base_depth + 400)
    if mp.isnan(L1) or mp.isnan(L2):
        return mp.nan
    diff = abs(L2 - L1)
    # Iterate until stable.
    depth = base_depth + 400
    while diff > mp.mpf(10) ** (-(dps + 10)) and depth < 30000:
        depth += 800
        L1 = L2
        L2 = cf_limit(coeffs, dps, depth)
        diff = abs(L2 - L1)
    return L2


# -----------------------------------------------------------------------------
# PSLQ with phantom-hit rule.
# -----------------------------------------------------------------------------
def basis_at_dps(L: mp.mpf, dps: int):
    mp.mp.dps = dps
    return [
        mp.mpf(L),
        mp.sqrt(2),
        mp.sqrt(3),
        mp.sqrt(5),
        mp.sqrt(17),
        mp.pi,
        mp.log(2),
        mp.zeta(3),
        mp.mpf(1),
    ]


def pslq_residual(L: mp.mpf, dps: int):
    """Run PSLQ and return (residual, relation_or_None, accepted_flag).

    accepted_flag is True iff the relation is non-phantom (L-coeff != 0).
    If PSLQ returns no relation, residual = 10^-dps and relation = None.
    """
    mp.mp.dps = dps
    B = basis_at_dps(L, dps)
    # PSLQ tolerance: 10^(-dps + 5) — slightly above eps to avoid spurious convergence.
    tol = mp.mpf(10) ** (-(dps - 5))
    try:
        rel = mp.pslq(B, tol=tol, maxcoeff=10 ** max(8, dps // 10))
    except Exception:
        rel = None

    if rel is None:
        # No relation found at this precision.
        return mp.mpf(10) ** (-dps), None, False

    # Phantom hit rule: reject if L-coefficient is zero.
    if rel[0] == 0:
        return mp.mpf(10) ** (-dps), rel, False

    # Compute |sum rel[i] * B[i]| as residual.
    s = mp.mpf(0)
    for c, x in zip(rel, B):
        s += c * x
    res = abs(s)
    # Cap residual at 10^-dps (the "PSLQ-found-something" floor) so a true
    # algebraic relation does not produce arbitrarily steep slopes via numerical
    # cancellation. This keeps slope <= -1 in absolute value and lets the
    # SPURIOUS case (residual stays flat above 10^-dps across dps) emerge cleanly.
    if res < mp.mpf(10) ** (-dps):
        res = mp.mpf(10) ** (-dps)
    return res, rel, True


# -----------------------------------------------------------------------------
# Main per-family precision escalation.
# -----------------------------------------------------------------------------
@dataclass
class FamilyResult:
    name: str
    coeffs: tuple
    a2_over_b1sq: float
    L_string: str
    residuals: dict           # dps -> log10(residual)
    relations: dict           # dps -> relation list (None if rejected/missing)
    accepted: dict            # dps -> bool (true if non-phantom L-bearing relation)
    slope: float
    intercept: float
    classification: str       # GENUINE / SPURIOUS / AMBIGUOUS


def linear_fit(xs, ys):
    n = len(xs)
    sx = sum(xs); sy = sum(ys)
    sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
    denom = n * sxx - sx * sx
    if denom == 0:
        return 0.0, 0.0
    m = (n * sxy - sx * sy) / denom
    b = (sy - m * sx) / n
    return m, b


def classify(slope: float) -> str:
    if slope < -0.8:
        return "GENUINE"
    if slope > -0.2:
        return "SPURIOUS"
    return "AMBIGUOUS"


def run_family(name: str, coeffs: tuple) -> FamilyResult:
    a2, a1, a0, b1, b0 = coeffs
    ratio = a2 / (b1 * b1) if b1 != 0 else float("nan")

    # Compute L once at maximum precision; reuse truncated form per dps.
    max_dps = max(DPS_LEVELS)
    L_full = cf_limit_stable(coeffs, max_dps + 30)

    residuals = {}
    relations = {}
    accepted = {}
    log_res_for_fit = []
    dps_for_fit = []

    for d in DPS_LEVELS:
        mp.mp.dps = d
        L_d = +L_full   # snapshot at current dps
        try:
            res, rel, acc = pslq_residual(L_d, d)
        except Exception as exc:
            res, rel, acc = mp.mpf(10) ** (-d), None, False
            print(f"    [WARN] PSLQ exception {name} dps={d}: {exc}")
        residuals[d] = float(mp.log10(res))
        relations[d] = list(rel) if rel is not None else None
        accepted[d] = bool(acc)
        log_res_for_fit.append(float(mp.log10(res)))
        dps_for_fit.append(float(d))

    slope, intercept = linear_fit(dps_for_fit, log_res_for_fit)
    cls = classify(slope)

    mp.mp.dps = 30
    L_str = mp.nstr(L_full, 40)

    return FamilyResult(
        name=name,
        coeffs=coeffs,
        a2_over_b1sq=ratio,
        L_string=L_str,
        residuals=residuals,
        relations=relations,
        accepted=accepted,
        slope=slope,
        intercept=intercept,
        classification=cls,
    )


def main():
    t0 = time.time()
    all_families = (
        [("Trans", n, c) for n, c in TRANS_FAMILIES] +
        [("Log",   n, c) for n, c in LOG_FAMILIES] +
        [("Alg",   n, c) for n, c in ALG_FAMILIES]
    )

    results = []
    for stratum, name, coeffs in all_families:
        t_fam = time.time()
        try:
            fr = run_family(name, coeffs)
        except Exception as exc:
            print(f"[ERR] {name}: {exc}")
            continue
        elapsed = time.time() - t_fam
        results.append({"stratum": stratum, **asdict(fr)})
        print(
            f"[{stratum:5s}] {name:18s} ratio={fr.a2_over_b1sq:+.6f} "
            f"slope={fr.slope:+.4f} cls={fr.classification:9s} ({elapsed:.1f}s)"
        )

    # Aggregate stats per stratum.
    def stats(stratum):
        slopes = [r["slope"] for r in results if r["stratum"] == stratum]
        if not slopes:
            return {}
        return {
            "n": len(slopes),
            "mean": sum(slopes) / len(slopes),
            "std": (sum((s - sum(slopes) / len(slopes)) ** 2 for s in slopes) / len(slopes)) ** 0.5,
            "min": min(slopes),
            "max": max(slopes),
        }

    summary = {
        "trans": stats("Trans"),
        "log": stats("Log"),
        "alg": stats("Alg"),
    }
    if summary["trans"] and summary["log"]:
        gap = summary["trans"]["min"] - summary["log"]["max"]
    else:
        gap = None
    summary["separation_gap_trans_min_minus_log_max"] = gap
    summary["wall_seconds"] = time.time() - t0

    out = {"results": results, "summary": summary, "dps_levels": DPS_LEVELS}
    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nSaved {RESULTS_JSON}")
    print(f"Wall: {summary['wall_seconds']:.1f}s")
    print(f"Trans: {summary['trans']}")
    print(f"Log:   {summary['log']}")
    print(f"Alg:   {summary['alg']}")
    print(f"Separation gap (min Trans slope - max Log slope): {gap}")


if __name__ == "__main__":
    main()
