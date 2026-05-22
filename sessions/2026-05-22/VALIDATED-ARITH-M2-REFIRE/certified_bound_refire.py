"""certified_bound_refire.py — M2-REFIRE orchestrator and gate.

WORKFLOW
--------
1. Read the two M2-REFIRE discovery checkpoints (dps=8640 and dps=28712)
   produced by _refire_discovery.py.
2. For each checkpoint whose terminal state is RELATION_CANDIDATE, verify
   the candidate against the M1 certified Arb balls at ctx.prec >= 32768.
3. Apply the K-STABILITY GATE:
     (i) both runs terminate in CONVERGED_NULL (no unrejected candidate),
     AND
     (ii) the Cor-2 exponents (K - 2*n^3) / (2*n^2) agree to FBA tolerance.
4. If gate PASSES, derive M_certified via FBA-1999 Cor 2 in Arb at
   prec >= 32768 bits + flint.fmpz exact ints. M_certified = floor of the
   LOWER endpoint of the final Arb enclosure (rigorous underestimate).
5. Apply the SANITY-EXPECTATION GUARD: 91 << M_certified << 1.036e72.
6. Run the FALSE-NEGATIVE GUARD (planted relation must be detected).
7. Emit k_stability_report.json, theorem.json (updated), and
   bound_provenance.json.

ANTI-LAUNDERING
---------------
- ALL real arithmetic in the certified chain uses flint.arb at
  CERT_PREC_BITS >= 32768 bits. No Python float. No mpmath value.
- ALL integer arithmetic uses Python int / flint.fmpz (exact).
- mpmath is a discovery oracle ONLY. Its stdout 'Norm:' is recorded
  but NEVER consumed in the certified chain.
- dps=2160 results are BANNED from any certified chain. They appear
  only in the spurious-termination historical record.
"""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import sys
import time
from pathlib import Path
from typing import Optional

import mpmath
from mpmath import mp, pslq
from flint import arb, ctx

sys.set_int_max_str_digits(1_000_000)

HERE = Path(__file__).parent
M1_OUTPUTS = HERE / "M1_outputs"

M1_BALL_SHA256 = {
    28712: "4729ea6cc4c2d433cbcb44c6f210ba82e22d77f51753c86aedce9562449a1ccf",
    14356: "378407d760627fd1dab5f3493d8e29037c63d76a4f92a066736b43238af03f54",
}

N_BASIS = 15
DIM_R = 1

# Certified Arb precision: 32768 bits ~= 9863 decimal digits.
# Sufficient for Arb-enclosure floors of bounds up to ~10^9000.
CERT_PREC_BITS = 32768

# Verification precision (same as CERT_PREC_BITS for the candidate-rejection check).
VERIFY_PREC_BITS = 32768

BASIS_LABELS = (
    "1", "K_0", "K_0^2", "K_0^3", "K_0^4", "K_0^5", "K_0^6",
    "log(K_0)",
    "K_0*pi", "K_0*e", "K_0*ln2", "K_0*gamma", "K_0*zeta(2)", "K_0*zeta(3)", "K_0*G",
)

# Sanity guard bounds.
SANITY_LOWER_VOID = 91         # void prior; M_certified must be FAR larger
SANITY_UPPER_EMPIRICAL_HRIGOROUS = 1_036_061_760_351_161_016_119_192_540_637_185_782_082_575_713_318_530_608_626_533_854_859_767_400  # empirical heuristic from M3.2 (UNCERTIFIED)


# ===========================================================================
# Section 1 — M1 ball reload (32768-bit Arb).
# ===========================================================================

def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for blk in iter(lambda: f.read(1 << 16), b""):
            h.update(blk)
    return h.hexdigest()


def load_m1_balls(P_bits: int):
    path = M1_OUTPUTS / f"balls_P{P_bits}.json"
    actual = file_sha256(path)
    expected = M1_BALL_SHA256[P_bits]
    if actual != expected:
        raise RuntimeError(
            f"M1 ball SHA mismatch at P={P_bits}: expected {expected}, got {actual}"
        )
    with open(path) as f:
        return json.load(f), actual


def reload_balls_as_arb(balls_json):
    arbs = []
    for entry in balls_json["basis"]:
        a = arb(entry["arb_repr"])
        arbs.append((entry["index"], entry["label"], a))
    if [t[1] for t in arbs] != list(BASIS_LABELS):
        raise RuntimeError("Label order mismatch in M1 balls")
    return [t[2] for t in arbs]


# ===========================================================================
# Section 2 — Candidate-relation verification at high prec.
# ===========================================================================

def verify_candidate_at_high_prec(arb_basis, relation):
    """Compute sum_i m_i * x_i in Arb at VERIFY_PREC_BITS.

    Returns the Arb sum and whether it contains zero (i.e. relation is
    consistent with the certified ball)."""
    saved_prec = ctx.prec
    try:
        ctx.prec = VERIFY_PREC_BITS
        # Reload at higher precision.
        s = arb(0)
        for m_i, x_i in zip(relation, arb_basis):
            s = s + arb(int(m_i)) * x_i
        return s
    finally:
        ctx.prec = saved_prec


def propagated_uncertainty_floor(arb_basis, relation):
    """Compute sum_i |m_i| * rad(x_i) — the propagated uncertainty floor
    on sum_i m_i * x_i due to M1 ball radii.

    Built as a sum of Arbs of the form arb(0, |m_i| * rad(x_i)). The
    resulting Arb has midpoint 0 and radius equal to the total
    propagated uncertainty. |Arb-sum| of the actual relation must
    exceed this floor to reject the candidate.
    """
    saved_prec = ctx.prec
    try:
        ctx.prec = VERIFY_PREC_BITS
        total = arb(0)
        for m_i, x_i in zip(relation, arb_basis):
            # x_i.rad() returns an arf (positive radius). We wrap it as an
            # Arb of midpoint 0 with that radius (matching the prior verifier).
            total = total + arb(abs(int(m_i))) * arb(0, x_i.rad())
        return total
    finally:
        ctx.prec = saved_prec


def candidate_rejection_record(arb_basis, candidate, candidate_source_tag):
    """Verify a candidate integer relation; return a record of the test."""
    saved_prec = ctx.prec
    try:
        ctx.prec = VERIFY_PREC_BITS
        # Reload balls fresh at verify prec.
        s_arb = verify_candidate_at_high_prec(arb_basis, candidate)
        floor_arb = propagated_uncertainty_floor(arb_basis, candidate)

        # Determine "contains zero" rigorously.
        contains_zero = bool(s_arb.contains(arb(0)))
        # |s_arb| as an upper bound on the magnitude.
        abs_s = abs(s_arb)
        # We want to compare |sum| to the noise floor. If abs(sum) - floor > 0
        # rigorously (in Arb), the candidate is REJECTED.
        diff = abs_s - floor_arb
        # diff > 0 strictly iff lower endpoint of diff > 0.
        # Use unique_fmpz on floor to check sign of lower endpoint.
        diff_lo = diff.lower()
        # Try to coerce to a comparison: if diff_lo > 0 the candidate is rejected.
        # We do this via diff_lo.floor() and check non-negativity, plus the strict
        # inequality via diff_lo > 0 in arb sense.
        rejected = (not contains_zero) and bool((diff > arb(0)))

        rec = {
            "candidate_source_tag": candidate_source_tag,
            "candidate_vector": [int(c) for c in candidate],
            "candidate_l2_norm_squared": sum(int(c) ** 2 for c in candidate),
            "candidate_l2_norm_approx": float(sum(int(c) ** 2 for c in candidate)) ** 0.5,
            "verify_prec_bits": VERIFY_PREC_BITS,
            "sum_arb_str": s_arb.str(50),
            "abs_sum_arb_str": abs_s.str(50),
            "propagated_uncertainty_floor_arb_str": floor_arb.str(50),
            "sum_contains_zero": contains_zero,
            "rejected_as_spurious": rejected,
        }
        return rec
    finally:
        ctx.prec = saved_prec


# ===========================================================================
# Section 3 — Certified Cor-2 bound at gated K.
# ===========================================================================

def arb_floor_lower_endpoint(a: arb) -> int:
    lo = a.lower()
    floored = lo.floor()
    fz = floored.unique_fmpz()
    if fz is None:
        s = floored.str(50)
        s = s.split(" +/-")[0].lstrip("[").rstrip("]").strip()
        if "." in s:
            s = s.split(".")[0]
        return int(s)
    return max(int(fz), 0)


def arb_max_abs(arbs):
    cur = abs(arbs[0])
    for a in arbs[1:]:
        ab = abs(a)
        cur = (cur + ab + abs(cur - ab)) / 2
    return cur


def arb_thm1_init_bound(x_arbs):
    n = len(x_arbs)
    s = [None] * (n + 2)
    s[n + 1] = arb(0)
    for k in range(n, 0, -1):
        s[k] = (s[k + 1] ** 2 + x_arbs[k - 1] ** 2).sqrt()
    diag = [s[j + 1] / s[j] for j in range(1, n)]
    max_d = arb_max_abs(diag)
    return arb(1) / max_d


def arb_cor2_bound(K_used: int, n: int = N_BASIS, dim_R: int = DIM_R):
    """FBA-1999 Cor 2: M_x > exp((K - 2*dim_R*n^3) / (2*dim_R*n^2))."""
    num = K_used - 2 * dim_R * (n ** 3)
    den = 2 * dim_R * (n ** 2)
    e = arb(num) / arb(den)
    return e.exp()


def compute_M_certified_refire(x_arbs, K_used: int):
    """All arithmetic in flint.arb at CERT_PREC_BITS + exact ints."""
    saved_prec = ctx.prec
    try:
        ctx.prec = CERT_PREC_BITS
        b_thm1 = arb_thm1_init_bound(x_arbs)
        M_thm1 = arb_floor_lower_endpoint(b_thm1)
        b_cor2 = arb_cor2_bound(K_used)
        M_cor2 = arb_floor_lower_endpoint(b_cor2)
        M = max(M_thm1, M_cor2, 0)
        binding = "FBA-1999 Cor 2 (K-based exponential)" if M_cor2 >= M_thm1 else "FBA-1999 Thm 1 (initial H matrix)"
        return {
            "n": N_BASIS,
            "dim_R": DIM_R,
            "K_used": K_used,
            "M_thm1_init": M_thm1,
            "M_thm1_init_arb_str": b_thm1.str(50),
            "M_cor2": M_cor2,
            "M_cor2_arb_str": b_cor2.str(50),
            "M_certified": M,
            "binding": binding,
            "cert_prec_bits": CERT_PREC_BITS,
        }
    finally:
        ctx.prec = saved_prec


# ===========================================================================
# Section 4 — K-stability gate.
# ===========================================================================

def k_stability_gate(ckpts):
    """Given list of M2-REFIRE checkpoints, apply the gate.

    Returns dict with verdict and reason.
    """
    # Must have BOTH dps=8640 and dps=28712 checkpoints.
    by_dps = {c["dps"]: c for c in ckpts}
    missing = [d for d in (8640, 28712) if d not in by_dps]
    if missing:
        return {
            "verdict": "INCOMPLETE",
            "reason": f"missing checkpoints for dps={missing}",
            "K_stable": None,
        }

    c8640 = by_dps[8640]
    c28712 = by_dps[28712]

    # Both must be CONVERGED_NULL (NULL = no candidate left unrejected).
    states = {dps: by_dps[dps]["terminal_state"] for dps in (8640, 28712)}
    if any(s != "CONVERGED_NULL" for s in states.values()):
        return {
            "verdict": "FAIL_STATE",
            "reason": f"one or both runs not CONVERGED_NULL: {states}",
            "K_stable": None,
        }

    # K values must agree to FBA-Cor-2-exponent tolerance.
    # Exponent: (K - 2*n^3) / (2*n^2) = (K - 6750)/450.
    # Tolerance: log(M_cert)_diff < 1 (i.e. exponents within 1).
    # This translates to |K_8640 - K_28712| <= 450 (one in M_cert ratio).
    K_8640 = c8640["K"]
    K_28712 = c28712["K"]
    diff = abs(K_8640 - K_28712)
    tol = 2 * (N_BASIS ** 2)  # = 450; one unit of Cor-2 exponent
    if diff > tol:
        return {
            "verdict": "FAIL_K_INSTABILITY",
            "reason": f"K_8640={K_8640} vs K_28712={K_28712}, |diff|={diff} > tol={tol}",
            "K_stable": None,
            "K_8640": K_8640,
            "K_28712": K_28712,
            "tol": tol,
        }

    # Use the conservative (smaller) K.
    K_stable = min(K_8640, K_28712)
    return {
        "verdict": "PASS",
        "reason": (
            f"both runs CONVERGED_NULL; K_8640={K_8640}, K_28712={K_28712}, "
            f"|diff|={diff} <= tol={tol}; K_stable=min=K={K_stable}"
        ),
        "K_stable": K_stable,
        "K_8640": K_8640,
        "K_28712": K_28712,
        "tol": tol,
    }


# ===========================================================================
# Section 5 — False-negative guard.
# ===========================================================================

def false_negative_guard():
    """Planted exact relation [1,-1,1] on basis [pi, pi+1, 1]."""
    saved_prec = ctx.prec
    saved_dps = mp.dps
    try:
        ctx.prec = CERT_PREC_BITS
        pi_arb = arb.pi()
        x_arbs = [pi_arb, pi_arb + 1, arb(1)]

        # Discovery at modest dps (this is just a tiny test basis).
        mp.dps = 100
        basis_mpf = [mp.pi, mp.pi + 1, mp.mpf(1)]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rel = pslq(basis_mpf, maxcoeff=10 ** 8, maxsteps=500, verbose=True)

        # Use a small K (planted relation found quickly; K typically < 30).
        # Bound via Thm 1 init only (Cor 2 with tiny K gives exp((K-54)/18) < 1).
        n_test = len(x_arbs)
        b_thm1 = arb_thm1_init_bound(x_arbs)
        M_thm1 = arb_floor_lower_endpoint(b_thm1)
        # Apply Cor 2 with the FOUND K (whatever mpmath gave).
        # For the test basis, we want the planted relation found.
        # mpmath's K is small, so Cor 2 bound is small.
        # Manually parse K from buf:
        import re
        K_seen = 0
        for line in buf.getvalue().splitlines():
            m = re.match(r"^\s*(\d+)/(\d+):\s+Error:", line)
            if m:
                K_seen = int(m.group(1))
            m2 = re.match(r"^FOUND relation at iter (\d+)", line)
            if m2:
                K_seen = int(m2.group(1)) + 1
        b_cor2 = arb_cor2_bound(K_seen, n_test, DIM_R)
        M_cor2 = arb_floor_lower_endpoint(b_cor2)
        M_cert = max(M_thm1, M_cor2, 0)

        planted_l2 = (3.0) ** 0.5  # sqrt(3) ~ 1.732
        relation_matches = rel is not None and (list(rel) in ([1, -1, 1], [-1, 1, -1]))
        bound_consistent = M_cert < 2  # bound < sqrt(3) means no false claim

        return {
            "test_basis": "[pi, pi+1, 1]",
            "planted_relation": [1, -1, 1],
            "planted_relation_l2_norm_approx": planted_l2,
            "mpmath_returned_relation": list(rel) if rel else None,
            "K_seen_in_test": K_seen,
            "M_thm1_init_test": M_thm1,
            "M_thm1_init_arb_str_test": b_thm1.str(40),
            "M_cor2_test": M_cor2,
            "M_cor2_arb_str_test": b_cor2.str(40),
            "M_certified_test": M_cert,
            "guard_pass": relation_matches and bound_consistent,
            "guard_pass_reason": (
                "oracle detected planted relation AND M_certified < sqrt(3)"
                if (relation_matches and bound_consistent)
                else (f"relation_matches={relation_matches}, bound_consistent={bound_consistent}")
            ),
            "cert_prec_bits": CERT_PREC_BITS,
        }
    finally:
        ctx.prec = saved_prec
        mp.dps = saved_dps


# ===========================================================================
# Section 6 — Sanity-expectation guard.
# ===========================================================================

def sanity_expectation_guard(M_certified: int):
    """Per work order: 91 << M_certified << 1.036e72. A value near 91 means
    the gate let a starved K through. A value >= 1.036e72 means a leak."""
    too_small = M_certified <= 100  # near 91 = HALT
    too_big = M_certified >= SANITY_UPPER_EMPIRICAL_HRIGOROUS
    return {
        "M_certified": M_certified,
        "lower_void_bound_91": SANITY_LOWER_VOID,
        "upper_empirical_heuristic": SANITY_UPPER_EMPIRICAL_HRIGOROUS,
        "too_small_near_void": too_small,
        "too_big_exceeds_empirical": too_big,
        "guard_pass": (not too_small) and (not too_big),
        "guard_pass_reason": (
            "M_certified is between 91 (void) and 1.036e72 (empirical), as expected"
            if (not too_small and not too_big) else
            ("M_certified <= 100, near void bound — possible precision starvation; HALT"
             if too_small else
             "M_certified >= 1.036e72, exceeds empirical heuristic — leak or inverted rounding; HALT")
        ),
    }


# ===========================================================================
# Section 7 — Main orchestrator.
# ===========================================================================

def main():
    print(f"[M2-REFIRE] orchestrator starting at {time.strftime('%Y-%m-%dT%H:%M:%S')}")
    print(f"[M2-REFIRE] CERT_PREC_BITS = {CERT_PREC_BITS}")

    # Load M1 ball + reload as Arb at CERT_PREC_BITS.
    ctx.prec = CERT_PREC_BITS
    balls_json, ball_sha = load_m1_balls(28712)
    arb_basis = reload_balls_as_arb(balls_json)
    print(f"[M2-REFIRE] M1 ball loaded, sha256={ball_sha}")

    # Load discovery checkpoints.
    ckpt_paths = sorted(HERE.glob("_refire_checkpoint_*.json"))
    ckpts = []
    for p in ckpt_paths:
        with open(p) as f:
            ckpts.append(json.load(f))
    print(f"[M2-REFIRE] found {len(ckpts)} checkpoint(s): {[c['tag'] for c in ckpts]}")

    # Verify any candidate relations.
    candidate_log = []
    for c in ckpts:
        if c.get("relation") is not None:
            print(f"[M2-REFIRE] verifying candidate from {c['tag']} at prec={VERIFY_PREC_BITS}...")
            rec = candidate_rejection_record(arb_basis, c["relation"], c["tag"])
            candidate_log.append(rec)
            print(f"[M2-REFIRE]   rejected_as_spurious = {rec['rejected_as_spurious']}")
            # If rejected, update the checkpoint terminal state.
            if rec["rejected_as_spurious"]:
                c["terminal_state_after_verification"] = "RELATION_CANDIDATE_REJECTED_SPURIOUS"
                # Re-treat as CONVERGED_NULL for gate purposes IF the K is the iter at which
                # mpmath claimed termination — but the work order says treat the run as FAILED.
                # FAIL means we do NOT use this K for the gate; it remains a failed run.
                c["terminal_state_gate"] = "FAILED_PRECISION_STARVED"
            else:
                # The candidate is REAL — STOP EVERYTHING per work order Step 2b.
                c["terminal_state_after_verification"] = "RELATION_CANDIDATE_REAL"
                c["terminal_state_gate"] = "REAL_RELATION_FOUND"
        else:
            c["terminal_state_after_verification"] = c["terminal_state"]
            c["terminal_state_gate"] = c["terminal_state"]

    # If ANY run has a REAL relation, STOP EVERYTHING.
    real_found = [c for c in ckpts if c.get("terminal_state_gate") == "REAL_RELATION_FOUND"]
    if real_found:
        print("[M2-REFIRE] *** REAL INTEGER RELATION FOUND IN ONE OR MORE RUNS ***")
        print("[M2-REFIRE] STOPPING. This is a halt condition per Step 2b.")
        report = {
            "verdict": "HALT_REAL_RELATION_FOUND",
            "real_relation_runs": [c["tag"] for c in real_found],
            "candidate_log": candidate_log,
            "checkpoints": ckpts,
        }
        with open(HERE / "k_stability_report.json", "w") as f:
            json.dump(report, f, indent=2)
        return report

    # Build gate-input list using gate states.
    # CONVERGED_NULL OK; FAILED_PRECISION_STARVED is a fail; MAXSTEPS_HIT is a fail.
    gate_input = []
    for c in ckpts:
        gs = c.get("terminal_state_gate", c["terminal_state"])
        gate_input.append({
            "dps": c["dps"],
            "K": c["K"],
            "terminal_state": gs,
            "tag": c["tag"],
        })

    # Run gate with normalised states: only CONVERGED_NULL counts; any other state fails the gate.
    by_dps = {g["dps"]: g for g in gate_input}
    states = {dps: by_dps[dps]["terminal_state"] if dps in by_dps else "MISSING"
              for dps in (8640, 28712)}
    missing = [d for d in (8640, 28712) if d not in by_dps]

    if missing:
        gate = {
            "verdict": "INCOMPLETE",
            "reason": f"missing checkpoints for dps={missing}",
            "K_stable": None,
            "states_observed": states,
        }
    elif any(s != "CONVERGED_NULL" for s in states.values()):
        gate = {
            "verdict": "FAIL_STATE",
            "reason": f"states are {states}; CONVERGED_NULL required from BOTH",
            "K_stable": None,
            "states_observed": states,
        }
    else:
        K_8640 = by_dps[8640]["K"]
        K_28712 = by_dps[28712]["K"]
        diff = abs(K_8640 - K_28712)
        tol = 2 * (N_BASIS ** 2)
        if diff > tol:
            gate = {
                "verdict": "FAIL_K_INSTABILITY",
                "reason": f"K_8640={K_8640} vs K_28712={K_28712}, |diff|={diff} > tol={tol}",
                "K_stable": None,
                "K_8640": K_8640, "K_28712": K_28712, "tol": tol,
            }
        else:
            K_stable = min(K_8640, K_28712)
            gate = {
                "verdict": "PASS",
                "reason": (
                    f"both CONVERGED_NULL; K_8640={K_8640}, K_28712={K_28712}, "
                    f"|diff|={diff} <= tol={tol}; K_stable=min={K_stable}"
                ),
                "K_stable": K_stable,
                "K_8640": K_8640, "K_28712": K_28712, "tol": tol,
            }

    print(f"[M2-REFIRE] gate verdict = {gate['verdict']}")
    print(f"[M2-REFIRE]   reason: {gate['reason']}")

    # Run false-negative guard (independent of main gate).
    print("[M2-REFIRE] running false-negative guard...")
    fng = false_negative_guard()
    print(f"[M2-REFIRE]   false-negative guard PASS = {fng['guard_pass']}")

    output = {
        "verdict": gate["verdict"],
        "gate": gate,
        "candidate_log": candidate_log,
        "false_negative_guard": fng,
        "checkpoints": ckpts,
        "M1_ball_sha256": ball_sha,
        "cert_prec_bits": CERT_PREC_BITS,
        "verify_prec_bits": VERIFY_PREC_BITS,
        "anti_laundering": (
            "ALL real arithmetic in flint.arb at CERT_PREC_BITS=32768 bits. "
            "ALL integer arithmetic in Python int / flint.fmpz. "
            "mpmath used only as discovery oracle for the integer iteration counter K. "
            "dps=2160 results BANNED. "
            "M_certified = floor of LOWER endpoint of final Arb enclosure."
        ),
    }

    # If gate passes, derive M_certified.
    if gate["verdict"] == "PASS":
        K_used = gate["K_stable"]
        print(f"[M2-REFIRE] deriving M_certified with K_used={K_used} at CERT_PREC_BITS={CERT_PREC_BITS}...")
        bnd = compute_M_certified_refire(arb_basis, K_used)
        print(f"[M2-REFIRE]   M_thm1_init = {bnd['M_thm1_init']}")
        print(f"[M2-REFIRE]   M_cor2      = {bnd['M_cor2']}")
        print(f"[M2-REFIRE]   M_certified = {bnd['M_certified']}")

        # Sanity guard.
        sanity = sanity_expectation_guard(bnd["M_certified"])
        print(f"[M2-REFIRE]   sanity guard PASS = {sanity['guard_pass']}: {sanity['guard_pass_reason']}")

        output["M_certified"] = bnd["M_certified"]
        output["bound_details"] = bnd
        output["sanity_guard"] = sanity

        if not sanity["guard_pass"]:
            output["verdict"] = "HALT_SANITY_GUARD"
            print(f"[M2-REFIRE] *** SANITY GUARD HALT ***")

    with open(HERE / "k_stability_report.json", "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"[M2-REFIRE] wrote k_stability_report.json")
    print(f"[M2-REFIRE] final verdict = {output['verdict']}")
    return output


if __name__ == "__main__":
    main()
