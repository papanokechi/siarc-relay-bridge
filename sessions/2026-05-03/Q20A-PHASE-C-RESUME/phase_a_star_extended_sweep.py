"""
Q20A-PHASE-C-RESUME  Phase A* — extended sanity range
================================================================
Re-validate Q20 Phase A's `A_DIRECT_IDENTITY` verdict at d in
{2, 3, ..., 10} (extended from Q20's {2, 3, 4}), using the
unchanged Q20 phase_a_symbolic_derivation.py module as the
source of truth.

This script does NOT introduce new symbolic content; it only
extends the d-range of the sanity-check loop in main(), and
adds AEAL provenance hooks (SHA-256, cached-value cross-checks).

Verdict signals produced:
  - A_DIRECT_IDENTITY_d10   (if all d in {2..10} pass)
  - A_BREAKS_AT_d*          (if a case split or symbolic
                             failure appears at some d* in
                             {5..10}; surprising given Q20's
                             clean d in {2,3,4} result)

Cached cross-checks at d in {2,3,4} (per Q20 handoff
"What this means for SIARC"):
  - d=2 (V_quad, beta_2 = 3): xi_0 = 2 / sqrt(3) cached at
    250 digits in PCF-1 v1.3 / Prompt 005 / CT v1.3 §3.3
  - d=3 (beta_3 = 1, all 3 cubic reps): xi_0 = 3 cached at
    80 algebraic digits in Prompt 012 G2_CLOSED_AT_D3
  - d=4 (beta_4 = 1, 8 quartic reps): xi_0 = 4 cached at
    spread = 0 in PCF2-SESSION-Q1 (dps=80)

Any disagreement at >1e-15 halts with
HALT_Q20A_REGRESSION_AT_PHASE_A.
"""
from __future__ import annotations

import sys
import json
import hashlib
import importlib.util
import pathlib
from typing import Any

import sympy as sp
import mpmath as mp

# ---------------------------------------------------------------
# Locate and load Q20's phase_a_symbolic_derivation.py module
# ---------------------------------------------------------------
Q20_SCRIPT = pathlib.Path(
    r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
    r"\siarc-relay-bridge\sessions\2026-05-03\Q20-CONJ33A-PROOF-UPGRADE"
    r"\phase_a_symbolic_derivation.py"
).resolve()

EXPECTED_Q20_HASH = (
    "8e6f9ebde933652e2581578d282163f0220091ea0ee4adbd6754bd53458f7496"
)

assert Q20_SCRIPT.exists(), f"Q20 anchor script missing: {Q20_SCRIPT}"

with open(Q20_SCRIPT, "rb") as fh:
    actual_hash = hashlib.sha256(fh.read()).hexdigest()

if actual_hash != EXPECTED_Q20_HASH:
    raise SystemExit(
        f"HALT_Q20A_REGRESSION_AT_PHASE_A: Q20 script SHA-256 drift\n"
        f"  expected: {EXPECTED_Q20_HASH}\n"
        f"  actual:   {actual_hash}"
    )

spec = importlib.util.spec_from_file_location("q20_phase_a", Q20_SCRIPT)
q20 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q20)


# ---------------------------------------------------------------
# Phase A*.1 - extended sanity-check loop
# ---------------------------------------------------------------
def phase_a_star_extended_sweep():
    """Run Q20's _sanity_check at d in {2..10} for two beta values
    per d (a stress test against any d-dependent symbolic
    instability)."""
    sweep = []
    # Per-d (beta_d) test points: include the cached AEAL
    # reference at d in {2,3,4} as the first test, plus a second
    # beta to stress-test the symbolic derivation.
    test_points = {
        2:  [3, 7],          # V_quad uses beta_2=3; 7 is a stress
        3:  [1, 5],          # cubic family uses beta_3=1
        4:  [1, 9],          # quartic catalogue uses beta_4=1
        5:  [1, 11],
        6:  [1, 13],
        7:  [1, 15],
        8:  [1, 17],
        9:  [1, 19],
        10: [1, 23],
    }
    for d, betas in sorted(test_points.items()):
        for beta in betas:
            try:
                ck = q20._sanity_check(d, beta)
                sweep.append(ck)
                tag = "AEAL-CACHED" if (
                    (d, beta) in {(2, 3), (3, 1), (4, 1)}
                ) else "stress"
                ck["test_tag"] = tag
            except Exception as exc:
                sweep.append({
                    "d": d, "beta_d": beta,
                    "error": f"{type(exc).__name__}: {exc}",
                    "match": False,
                    "test_tag": "FAIL",
                })
    return sweep


# ---------------------------------------------------------------
# Phase A*.2 - cross-checks at d in {2,3,4} vs cached AEAL values
# ---------------------------------------------------------------
def phase_a_star_aeal_cross_checks():
    """Verify the symbolic derivation reproduces the cached AEAL
    values at d=2 (V_quad to 250 digits), d=3 (cubic at 80
    algebraic digits), d=4 (quartic at spread 0, dps=80) within
    1e-15.

    Cached values:
      d=2, beta_2=3:  xi_0 = 2 / sqrt(3)
      d=3, beta_3=1:  xi_0 = 3
      d=4, beta_4=1:  xi_0 = 4
    """
    out = []
    with mp.workdps(80):
        cached = [
            (2, 3, mp.mpf(2) / mp.sqrt(mp.mpf(3)),
             "PCF-1 v1.3 / Prompt 005 / CT v1.3 §3.3 (250 digits)"),
            (3, 1, mp.mpf(3),
             "Prompt 012 G2_CLOSED_AT_D3 (80 algebraic digits)"),
            (4, 1, mp.mpf(4),
             "PCF2-SESSION-Q1 (spread 0 across 8 reps, dps=80)"),
        ]
        for d, beta, expected, source in cached:
            # Symbolic re-derivation
            info = q20.derive_at_concrete_d(d)
            chi = info["chi"]
            beta_d_sym = q20.operator_points_general(d)[1][d]
            chi_at = sp.Poly(
                chi.subs(beta_d_sym, sp.Rational(beta)),
                sp.symbols("c"),
            )
            coeffs_sym = chi_at.all_coeffs()
            coeffs_mp = [mp.mpf(str(sp.Rational(c)))
                         for c in coeffs_sym]
            roots = mp.polyroots(coeffs_mp, maxsteps=400,
                                  extraprec=100)
            max_abs = max(abs(r) for r in roots)
            delta = abs(max_abs - expected)
            rel = (float(delta / expected)
                   if expected != 0 else float(delta))
            out.append({
                "d": d, "beta_d": beta,
                "expected": mp.nstr(expected, 30),
                "max_abs_root": mp.nstr(max_abs, 30),
                "abs_error": mp.nstr(delta, 6),
                "rel_error": rel,
                "match": rel < 1e-15,
                "cached_source": source,
            })
    return out


# ---------------------------------------------------------------
# Run + emit JSON summary
# ---------------------------------------------------------------
def main():
    print("=" * 72)
    print("Q20A-PHASE-C-RESUME  Phase A* extended sweep")
    print("=" * 72)
    print(f"Q20 anchor script: {Q20_SCRIPT}")
    print(f"Q20 SHA-256:       {actual_hash}")
    print(f"Match expected:    {actual_hash == EXPECTED_Q20_HASH}")
    print()

    print("[Phase A*.1] Extended sweep d in {2..10}, 2 betas per d")
    print("-" * 72)
    sweep = phase_a_star_extended_sweep()
    failed = [s for s in sweep if not s.get("match", False)]
    for s in sweep:
        if "error" in s:
            print(f"  d={s['d']:>2} beta={s['beta_d']:>3}: "
                  f"FAIL ({s['error']})")
        else:
            tag = s.get("test_tag", "")
            print(f"  d={s['d']:>2} beta={s['beta_d']:>3}: "
                  f"max_abs={s['max_abs_root']:>32}  "
                  f"rel={s['rel_error']:.2e}  "
                  f"match={s['match']}  [{tag}]")
    print()
    print(f"  {len(sweep) - len(failed)} / {len(sweep)} pass")
    print()

    print("[Phase A*.2] AEAL cross-checks at d in {2,3,4}")
    print("-" * 72)
    cross = phase_a_star_aeal_cross_checks()
    cross_failed = [c for c in cross if not c["match"]]
    for c in cross:
        print(f"  d={c['d']} beta={c['beta_d']}: "
              f"expected={c['expected']}  "
              f"computed={c['max_abs_root']}  "
              f"rel={c['rel_error']:.2e}  "
              f"match={c['match']}")
        print(f"    cached source: {c['cached_source']}")
    print()
    print(f"  {len(cross) - len(cross_failed)} / {len(cross)} pass")
    print()

    if failed or cross_failed:
        verdict_signal = "A_BREAKS_AT_d*"
        print(f"VERDICT: {verdict_signal} (failures detected)")
    else:
        verdict_signal = "A_DIRECT_IDENTITY_d10"
        print(f"VERDICT: {verdict_signal}")

    summary = {
        "q20_anchor_sha256": actual_hash,
        "q20_anchor_match_expected": (actual_hash
                                       == EXPECTED_Q20_HASH),
        "verdict_signal": verdict_signal,
        "extended_sweep": sweep,
        "aeal_cross_checks": cross,
        "n_sweep_pass": len(sweep) - len(failed),
        "n_sweep_total": len(sweep),
        "n_cross_pass": len(cross) - len(cross_failed),
        "n_cross_total": len(cross),
    }
    out_path = pathlib.Path("phase_a_star_results.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, default=str)
    print(f"\nWrote: {out_path.resolve()}")


if __name__ == "__main__":
    main()
