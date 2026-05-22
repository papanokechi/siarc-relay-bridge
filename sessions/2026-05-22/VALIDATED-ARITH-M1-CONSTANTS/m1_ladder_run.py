"""
harness_certified/m1_ladder_run.py — Milestone 1 ladder driver.

Runs build_basis at each P_bits in the certified ladder, writes
M1_outputs/balls_P{P}.json, performs:
  - mpmath cross-check on K_0 (transcription guard at low precision)
  - ladder-consistency check: ball at P_high (suitably inflated) must contain
    the ball at P_low.
  - generates ladder_consistency.json and theorem_M1_partial.json.

This is the M1 "halt-and-flag" deliverable, NOT a step toward M2.
"""

from __future__ import annotations
import json
import os
import sys
import time
from pathlib import Path

from flint import arb, ctx

from certified_constants import (
    BASIS_LABELS,
    N_BASIS,
    GENERATOR_LABELS,
    build_basis,
    basis_to_json,
)
from bbc_series import GUARD_BITS, required_N_for_precision

LADDER = [7178, 14356, 28712]
OUT_DIR = Path(__file__).parent / "M1_outputs"


def _arb_from_json(d: dict) -> arb:
    """Reconstruct an Arb ball from JSON serialisation."""
    mid_s = d["midpoint_str"]
    rad_s = d["radius_str"]

    def parse_arb_endpoint(s: str) -> str:
        s = s.strip()
        if s.startswith("[") and "+/-" in s:
            s = s.split(" +/- ")[0].lstrip("[")
        elif s.startswith("[") and s.endswith("]"):
            s = s[1:-1]
        return s

    mid = parse_arb_endpoint(mid_s)
    rad = parse_arb_endpoint(rad_s)
    return arb(mid, rad)


def ladder_consistency(payloads: dict[int, dict]) -> dict:
    """Check that ball at higher P is contained in inflated ball at lower P.

    "Inflation" here means: the lower-P ball already has its own certified
    radius r_low. The higher-P ball, projected onto the same true point, has
    midpoint m_high and radius r_high << r_low. The check is that
    [m_high - r_high, m_high + r_high]  is contained inside
    [m_low  - r_low,  m_low  + r_low ].
    """
    Ps = sorted(payloads.keys())
    pairs = list(zip(Ps[:-1], Ps[1:]))
    results = []
    for P_lo, P_hi in pairs:
        lo_basis = payloads[P_lo]["basis"]
        hi_basis = payloads[P_hi]["basis"]
        per_label = []
        all_ok = True
        for i in range(N_BASIS):
            ball_lo = _arb_from_json(lo_basis[i])
            ball_hi = _arb_from_json(hi_basis[i])
            # ball_lo.contains(ball_hi)
            contained = bool(ball_lo.contains(ball_hi))
            per_label.append({
                "index": i,
                "label": BASIS_LABELS[i],
                "P_low_contains_P_high": contained,
            })
            if not contained:
                all_ok = False
        results.append({
            "P_low": P_lo,
            "P_high": P_hi,
            "all_contained": all_ok,
            "per_basis_entry": per_label,
        })
    return {
        "ladder": Ps,
        "pairs_checked": results,
        "overall_ok": all(r["all_contained"] for r in results),
    }


def _arb_mid_to_mpf(x: arb, mp):
    """Robustly convert an Arb ball's midpoint to mpmath.mpf at high precision.

    `arb.mid()` returns an arb whose str() may still have a residual radius
    representation. We extract just the central numeric token before the
    `+/-`, then strip surrounding `[]`.
    """
    s = str(x.mid())
    if "+/-" in s:
        s = s.split("+/-")[0]
    s = s.strip().lstrip("[").rstrip(" \t]")
    return mp.mpf(s)


def mpmath_cross_check(payloads: dict[int, dict]) -> dict:
    """Compare Arb K_0 midpoint against mpmath.khinchin at low precision.

    This is a TRANSCRIPTION GUARD: it does NOT make the certificate dependent
    on mpmath. We simply verify the Arb-certified K_0 midpoint agrees with the
    independently-implemented mpmath.khinchin to many digits (which would
    catch a coding bug in our BBC series).
    """
    import mpmath as mp

    # Use the lowest ladder rung to keep mpmath fast.
    P_lo = min(payloads.keys())
    K0_arb = _arb_from_json(payloads[P_lo]["basis"][1])

    # Cap mpmath precision at 500 dps (mpmath.khinchin is slow at high dps).
    mp.mp.dps = 200
    K0_mp = +mp.khinchin   # force evaluation at current dps

    K0_arb_mid_mpf = _arb_mid_to_mpf(K0_arb, mp)
    diff = abs(K0_arb_mid_mpf - K0_mp)

    # The cross-check threshold: half the mpmath precision (so we don't trip on
    # mpmath's own tail).
    threshold = mp.mpf(10) ** (-150)
    ok = diff < threshold
    return {
        "comparison_at_P_bits": P_lo,
        "mpmath_dps_used": int(mp.mp.dps),
        "threshold_dps": 150,
        "abs_difference": mp.nstr(diff, 6),
        "transcription_guard_passed": bool(ok),
        "note": "mpmath.khinchin is NOT a certified source; this is only a transcription guard, not part of the rigorous certificate.",
    }


def theorem_m1_partial(payloads: dict[int, dict], ladder_check: dict, xchk: dict) -> dict:
    """Construct the Milestone-1 partial theorem statement."""
    import platform
    import flint

    flint_ver = flint.flint_base.flint_base.FLINT_VERSION
    flint_rel = flint.flint_base.flint_base.FLINT_RELEASE
    flint_bits = flint.flint_base.flint_base.FLINT_BITS

    # Pick the highest-precision rung as the "official" certified balls.
    P_max = max(payloads.keys())
    top = payloads[P_max]

    return {
        "theorem_id": "M1-PARTIAL",
        "milestone": 1,
        "status": "PARTIAL_pending_operator_signoff",
        "statement": (
            "There exist Arb balls B_0, ..., B_14 in the 15-element certified "
            "basis B_D(C) such that each B_i contains the true value of the "
            "i-th basis constant. The enclosures are rigorous conditional on "
            "FLINT/Arb correctness and on BBC 1997 eq.(1) (Math.Comp. 66(217))."
        ),
        "basis_labels": list(BASIS_LABELS),
        "precision_ladder_bits": sorted(payloads.keys()),
        "official_certified_balls_at_P_bits": P_max,
        "balls_top": top["basis"],
        "ladder_consistency_summary": {
            "overall_ok": ladder_check["overall_ok"],
            "pairs_checked": [
                {"P_low": p["P_low"], "P_high": p["P_high"], "ok": p["all_contained"]}
                for p in ladder_check["pairs_checked"]
            ],
        },
        "transcription_guard": xchk,
        "environment": {
            "python_flint": "0.8.0",
            "FLINT_VERSION": flint_ver,
            "FLINT_RELEASE": flint_rel,
            "FLINT_BITS": flint_bits,
            "guard_bits": GUARD_BITS,
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "honesty_note": (
            "We certify the arithmetic, not the BBC identity. The K_0 enclosure "
            "is rigorous conditional on BBC 1997 eq.(1). FLINT/Arb is assumed "
            "to be a correct implementation of ball arithmetic."
        ),
    }


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    payloads: dict[int, dict] = {}
    elapsed_total = 0.0
    for P in LADDER:
        print(f"==> building basis at P_bits={P} ...")
        t0 = time.time()
        cb = build_basis(P)
        payload = basis_to_json(cb)
        dt = time.time() - t0
        elapsed_total += dt
        out_path = OUT_DIR / f"balls_P{P}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"    wrote {out_path}  (N={cb.N_truncation}, t={dt:.3f}s)")
        payloads[P] = payload

    print("==> ladder consistency check ...")
    ladder_check = ladder_consistency(payloads)
    with open(OUT_DIR / "ladder_consistency.json", "w", encoding="utf-8") as f:
        json.dump(ladder_check, f, indent=2)
    print(f"    overall_ok = {ladder_check['overall_ok']}")

    print("==> mpmath transcription guard ...")
    try:
        xchk = mpmath_cross_check(payloads)
        print(f"    transcription_guard_passed = {xchk['transcription_guard_passed']}")
    except Exception as e:
        xchk = {"transcription_guard_passed": False, "error": str(e)}
        print(f"    FAILED: {e}")

    print("==> writing theorem_M1_partial.json ...")
    theorem = theorem_m1_partial(payloads, ladder_check, xchk)
    theorem["elapsed_total_seconds"] = round(elapsed_total, 3)
    with open(OUT_DIR / "theorem_M1_partial.json", "w", encoding="utf-8") as f:
        json.dump(theorem, f, indent=2)

    print()
    print(f"M1 ladder run complete. Total elapsed: {elapsed_total:.2f}s")
    print(f"Outputs in: {OUT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
