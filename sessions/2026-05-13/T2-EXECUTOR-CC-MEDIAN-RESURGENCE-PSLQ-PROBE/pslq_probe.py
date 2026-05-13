#!/usr/bin/env python3
"""
CC-MEDIAN-RESURGENCE-PSLQ-PROBE
================================

PSLQ probe for closed-form recognition of the Stokes amplitude C extracted from
V_quad (a_n = 1, b_n = 3n^2 + n + 1) via median resurgence at zeta_* = 4/sqrt(3).

Source value (from sessions/2026-05-02/CC-MEDIAN-RESURGENCE-EXECUTE/
              S_zeta_star_digits.txt, reproduced bit-identically 2026-05-13):

  C = 8.127336795495072367112578732023583182264542722338793442962779422864942...

PSLQ tests for integer relations among {C, 1, pi, pi^2, pi*sqrt(3), log(2),
log(3), log(5), Gamma(1/3), Gamma(2/3), zeta(3), Catalan, sqrt(3), 1/pi},
escalating precision and maxcoeff until either a relation is found or the
search budget is exhausted.

Output:
- pslq_results.json     (one entry per basis tried)
- pslq_run.log          (human-readable trace)
- claims.jsonl          (AEAL audit-class claims)
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

import mpmath

HERE = Path(__file__).resolve().parent

C_DIGITS = (
    "8.127336795495072367112578732023583182264542722338793442962779422864942"
    "231170962684449206434528015595926628489359285274597689303260224562689447"
    "523320604495880664420774981598810033884197092823557473226911652785400664"
    "208096248862807283043517884864891234"
)

DPS_LEVELS = [100, 200]
MAXCOEFF_LEVELS = [int(1e30), int(1e60), int(1e90)]


def _verify_relation_includes_C(rel, names):
    """Reject 'relations' that don't involve the constant under investigation.
    PSLQ over a linearly-dependent basis returns trivial algebraic identities
    (e.g. -3*(pi/sqrt3) + 1*(pi*sqrt3) = 0). Those are not what we want."""
    c_idx = names.index("C")
    return int(rel[c_idx]) != 0


def _log(line, log_file):
    print(line)
    log_file.write(line + "\n")
    log_file.flush()


def _build_basis(label, include_C=True):
    pi = mpmath.pi
    if label == "B1_minimal":
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("sqrt3", mpmath.sqrt(3)),
            ("pi_times_sqrt3", pi * mpmath.sqrt(3)),
        ]
    elif label == "B2_powers_pi":
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("pi2", pi**2),
            ("pi3", pi**3),
            ("pi_inv", 1/pi),
            ("sqrt3", mpmath.sqrt(3)),
        ]
    elif label == "B3_logs_and_special":
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("log5", mpmath.log(5)),
            ("zeta3", mpmath.zeta(3)),
            ("Catalan", mpmath.catalan),
            ("sqrt3", mpmath.sqrt(3)),
        ]
    elif label == "B4_gamma_1over3":
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("Gamma_1_3", mpmath.gamma(mpmath.mpf(1)/3)),
            ("Gamma_2_3", mpmath.gamma(mpmath.mpf(2)/3)),
            ("Gamma_1_3_cubed", mpmath.gamma(mpmath.mpf(1)/3)**3),
            ("sqrt3", mpmath.sqrt(3)),
            ("pi_times_sqrt3", pi * mpmath.sqrt(3)),
        ]
    elif label == "B5_rich":
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("pi2", pi**2),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("zeta3", mpmath.zeta(3)),
            ("Catalan", mpmath.catalan),
            ("sqrt3", mpmath.sqrt(3)),
            ("Gamma_1_3", mpmath.gamma(mpmath.mpf(1)/3)),
        ]
    elif label == "B6_log_of_C":
        # Try linear relation among log(C), 1, log(pi), log(sqrt(3)), log(2), log(3), log(Gamma(1/3))
        basis = [
            ("1", mpmath.mpf(1)),
            ("log_pi", mpmath.log(pi)),
            ("log_sqrt3", mpmath.log(mpmath.sqrt(3))),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("log_Gamma_1_3", mpmath.log(mpmath.gamma(mpmath.mpf(1)/3))),
            ("log_Gamma_2_3", mpmath.log(mpmath.gamma(mpmath.mpf(2)/3))),
        ]
    elif label == "B7_C_squared":
        # Maybe C^2 has a cleaner relation (e.g. C^2 = a*pi^2 + b*log^2)
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("pi2", pi**2),
            ("pi3", pi**3),
            ("zeta3", mpmath.zeta(3)),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("sqrt3", mpmath.sqrt(3)),
        ]
    elif label == "B8_ratios":
        # Test if C / (pi * sqrt(3)) has a clean rational/simple closed form
        # We give PSLQ the ratio directly via the constant override flag.
        basis = [
            ("1", mpmath.mpf(1)),
            ("pi", pi),
            ("log2", mpmath.log(2)),
            ("log3", mpmath.log(3)),
            ("sqrt3", mpmath.sqrt(3)),
        ]
    else:
        raise ValueError(f"Unknown basis {label}")
    if include_C:
        return [("C", mpmath.mpf(C_DIGITS))] + basis
    return basis


def _attempt(basis_label, dps, maxcoeff, log_file):
    mpmath.mp.dps = dps
    pairs = _build_basis(basis_label, include_C=True)
    # Apply per-basis transformations on the test constant.
    if basis_label == "B6_log_of_C":
        # Replace "C" with log(C)
        pairs = [("log_C", mpmath.log(pairs[0][1]))] + pairs[1:]
    elif basis_label == "B7_C_squared":
        # Replace "C" with C^2
        pairs = [("C_squared", pairs[0][1]**2)] + pairs[1:]
    elif basis_label == "B8_ratios":
        # Replace "C" with C / (pi * sqrt(3))
        pi = mpmath.pi
        pairs = [("C_over_pi_sqrt3", pairs[0][1] / (pi * mpmath.sqrt(3)))] + pairs[1:]
    vec = [v for (_, v) in pairs]
    names = [n for (n, _) in pairs]
    # Sentinel name for the constant being tested (always at index 0)
    target_name = names[0]
    _log(f"\n[ATTEMPT] basis={basis_label} dps={dps} maxcoeff={maxcoeff:.2e} size={len(vec)}", log_file)
    _log(f"  names = {names}", log_file)
    t0 = time.time()
    try:
        rel = mpmath.pslq(vec, maxcoeff=maxcoeff, tol=mpmath.mpf(10)**(-int(dps*0.6)))
    except Exception as exc:
        _log(f"  EXCEPTION: {exc}", log_file)
        return {
            "basis": basis_label, "dps": dps, "maxcoeff": maxcoeff,
            "names": names, "found": False, "exception": str(exc),
            "elapsed_sec": time.time() - t0,
        }
    elapsed = time.time() - t0
    if rel is None:
        _log(f"  RESULT: no relation (elapsed {elapsed:.2f}s)", log_file)
        return {
            "basis": basis_label, "dps": dps, "maxcoeff": maxcoeff,
            "names": names, "found": False, "relation": None,
            "elapsed_sec": elapsed,
        }
    s = mpmath.mpf(0)
    for (c, v) in zip(rel, vec):
        s += mpmath.mpf(int(c)) * v
    residual = abs(s)
    coeffs_int = [int(c) for c in rel]
    involves_target = coeffs_int[0] != 0
    tag = "FOUND" if involves_target else "FOUND-TRIVIAL"
    _log(f"  RESULT: relation {tag} in {elapsed:.2f}s", log_file)
    _log(f"    coeffs = {coeffs_int}", log_file)
    _log(f"    residual = {mpmath.nstr(residual, 5)}", log_file)
    _log("    relation: " + " + ".join(f"({int(c)}) * {n}" for c, n in zip(rel, names) if int(c) != 0) + " = 0", log_file)
    return {
        "basis": basis_label, "dps": dps, "maxcoeff": maxcoeff,
        "names": names,
        "found": involves_target,
        "found_trivial": (not involves_target),
        "target": target_name,
        "relation": coeffs_int,
        "residual": mpmath.nstr(residual, 10),
        "elapsed_sec": elapsed,
    }


def main():
    log_path = HERE / "pslq_run.log"
    results_path = HERE / "pslq_results.json"
    claims_path = HERE / "claims.jsonl"
    with open(log_path, "w", encoding="utf-8") as log_file:
        _log("CC-MEDIAN-RESURGENCE-PSLQ-PROBE", log_file)
        _log(f"Python {sys.version.split()[0]} / mpmath {mpmath.__version__}", log_file)
        _log(f"C = {C_DIGITS[:80]}...", log_file)
        bases = ["B1_minimal", "B2_powers_pi", "B3_logs_and_special",
                 "B4_gamma_1over3", "B5_rich",
                 "B6_log_of_C", "B7_C_squared", "B8_ratios"]
        results = []
        any_found = False
        for basis in bases:
            for dps in DPS_LEVELS:
                for maxcoeff in MAXCOEFF_LEVELS:
                    r = _attempt(basis, dps, maxcoeff, log_file)
                    results.append(r)
                    if r.get("found"):
                        any_found = True
                        break
                if r.get("found"):
                    break
        _log("\n=== SUMMARY ===", log_file)
        for r in results:
            tag = "FOUND" if r.get("found") else "no"
            _log(f"  [{tag}] basis={r['basis']} dps={r['dps']} maxcoeff={r['maxcoeff']:.2e}", log_file)
        if not any_found:
            _log("\nNo integer relation found in any tested basis x (dps, maxcoeff) grid.", log_file)
            _log("This is a NEGATIVE PSLQ result, not a closed-form proof of absence.", log_file)
        with open(results_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        results_hash = hashlib.sha256(json.dumps(results, sort_keys=True).encode()).hexdigest()
        with open(claims_path, "w", encoding="utf-8") as f:
            f.write(json.dumps({
                "claim_id": "PSLQ-PROBE-1",
                "claim": (f"PSLQ probe of C = 8.1273367954950723671... across 5 bases x 2 dps levels "
                          f"x 3 maxcoeff levels found {'a candidate relation; see results' if any_found else 'NO integer relation'} "
                          "(does not prove absence; only bounds maxcoeff under tested basis)"),
                "evidence_type": "computation",
                "dps": max(DPS_LEVELS),
                "reproducible": True,
                "script": "pslq_probe.py",
                "output_hash": results_hash,
                "any_found": any_found,
            }) + "\n")
            f.write(json.dumps({
                "claim_id": "PSLQ-PROBE-2",
                "claim": "C extracted from V_quad median resurgence at zeta_* = 4/sqrt(3) (commit ed61428 2026-05-02; reproduced bit-identically commit a4fe865 2026-05-13)",
                "evidence_type": "audit",
                "dps": 250,
                "reproducible": True,
                "script": "(median_resurgence.py source)",
                "output_hash": "0b9e656f08b5b1dae67ebaffa5456e3625594b8e4c1904b4d0b2487ab30687cd",
            }) + "\n")
        _log(f"\nResults: {results_path}", log_file)
        _log(f"Claims:  {claims_path}", log_file)


if __name__ == "__main__":
    main()
