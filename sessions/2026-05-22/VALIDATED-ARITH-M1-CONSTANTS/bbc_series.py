"""
harness_certified/bbc_series.py — BBC 1997 eq. (1) implementation with rigorous tail bound.

CITATION
========
Bailey, D. H., Borwein, J. M., Crandall, R. E. (1997).
"On the Khintchine Constant." Math. Comp. 66 (217), 417-431.
DOI: 10.1090/S0025-5718-97-00800-4.

Local cache:        harness_certified/_lit_cache/khinchin.pdf
SHA-256:            7DD18D84B93A36B85F4F94D23671A202258CB6517CCBAA5794EDEADD0E793793
Equation:           (1) on page 2, with A_s defined in Lemma 1(a) on page 3.

The identity (verbatim):

    log(K_0) * log(2) = sum_{s=1}^{infty} (zeta(2s) - 1) / s * A_s,

where

    A_s := sum_{m=1}^{2s-1} (-1)^(m-1) / m.

HONESTY NOTE (per work-order Milestone 1 directive):
    The Arb enclosure of K_0 produced here is rigorous *conditional on BBC 1997 eq. (1)*.
    We are certifying the arithmetic, not re-deriving the identity.

RIGOROUS TAIL BOUND (proof in BBC_FORMULA_VERIFIED.md §3):
    For each s >= 1, zeta(2s) - 1 <= 4^(1-s) * (zeta(2) - 1), and |A_s| <= 1, hence

        |T_N|  =  |sum_{s>N} (zeta(2s)-1)/s * A_s|
              <=  (4 * (zeta(2) - 1) / (3 * (N+1))) * 4^(-N).

    Dividing by log 2 (since the LHS of eq.(1) is log(K_0) * log(2)):

        |tail of log K_0|  <=  (4 * (zeta(2)-1) / (3*(N+1)*log(2))) * 4^(-N).

API
===
    bbc_logK0_logL2_partial_sum(N, prec)  -> Arb ball for the partial sum (s=1..N)
    bbc_tail_bound(N, prec)               -> Arb ball [0 +/- B] enclosing the absolute tail
                                             of log(K_0)*log(2), rigorously above |T_N|
    certified_log_K0(N, prec)             -> Arb ball for log K_0 with tail-inflated radius
    certified_K0(N, prec)                 -> Arb ball for K_0 = exp(log K_0)
"""

from __future__ import annotations
from flint import arb, ctx

# Guard bits added to the requested target precision to absorb Arb's per-operation
# rounding accumulation across ~N partial-sum steps. With N <= ~30k terms,
# log2(N) <= 15, and each arb op contributes at most a few bits of radius growth.
# 128 guard bits is well above log2(N_max) + per-op factor for any precision in the ladder.
GUARD_BITS = 128


def _ensure_prec(prec: int) -> None:
    if ctx.prec < prec:
        ctx.prec = prec


def required_N_for_precision(P_bits: int, safety_bits: int = 64) -> int:
    """Truncation N sufficient for tail < 2^{-P_bits} per the closed-form bound.

    Bound:    tail_logK0 <= (4(z2-1) / (3(N+1) log 2)) * 4^{-N}.
    Since the prefactor is < 1 for N >= 1, requiring 2N >= P_bits + safety is sufficient.
    """
    return (P_bits + safety_bits + 1) // 2 + 1


def bbc_logK0_logL2_partial_sum(N: int, prec: int) -> arb:
    """Arb partial sum S_N = sum_{s=1..N} (zeta(2s)-1)/s * A_s.

    A_s is computed iteratively as an Arb ball via the recurrence
        A_1 = 1
        A_{s+1} = A_s - 1/(2s) + 1/(2s+1).

    Internal precision is `prec + GUARD_BITS` to absorb per-operation rounding.
    """
    if N < 1:
        raise ValueError("N must be >= 1")
    _ensure_prec(prec + GUARD_BITS)

    S = arb(0)
    # A_1 = 1
    A_s = arb(1)
    for s in range(1, N + 1):
        zeta_2s_minus_1 = arb(2 * s).zeta() - 1
        term = zeta_2s_minus_1 / s * A_s
        S = S + term
        # Update A_s -> A_{s+1} for next iteration (only if there is one)
        if s < N:
            A_s = A_s - arb(1) / (2 * s) + arb(1) / (2 * s + 1)
    return S


def bbc_tail_bound(N: int, prec: int) -> arb:
    """Rigorous Arb ball enclosing |T_N| for the BBC eq.(1) series.

    Returns a NON-NEGATIVE Arb ball B such that |T_N| <= B is guaranteed
    (modulo Arb correctness, which is the load-bearing assumption).

    Bound formula:  B = (4 * (zeta(2) - 1) / (3 * (N + 1))) * 4^{-N}.
    """
    _ensure_prec(prec + GUARD_BITS)
    z2m1 = arb(2).zeta() - 1                 # tight ball, certified by Arb
    prefactor = arb(4) * z2m1 / (arb(3) * (N + 1))
    # 4^{-N} = 2^{-2N}. Compute as arb(2)**(-2N) for rigorous power.
    four_to_minus_N = arb(2) ** (-2 * N)
    return prefactor * four_to_minus_N


def certified_logK0_times_log2(N: int, prec: int) -> tuple[arb, arb, arb]:
    """Returns (S_N, B_N, certified_ball) where certified_ball encloses log(K_0)*log(2).

    The certified ball is constructed by widening S_N's radius by the upper endpoint
    of the tail bound (rigorous since |T_N| <= B_N).
    """
    _ensure_prec(prec + GUARD_BITS)
    S_N = bbc_logK0_logL2_partial_sum(N, prec)
    B_N = bbc_tail_bound(N, prec)
    # B_N is non-negative; widen S_N by adding the symmetric interval [-B_N, +B_N].
    # In Arb, we add the ball arb(0, B_N.upper()) which has midpoint 0 and radius
    # >= |B_N|.
    B_upper = B_N.upper()  # Arb's "upper" returns an arb ball that itself bounds the upper
                           # endpoint; we extract a magnitude via .above_abs() if needed.
    # The cleanest construction: union of (S_N - B_N) and (S_N + B_N) — both Arb balls.
    lo = S_N - B_N
    hi = S_N + B_N
    certified = lo.union(hi)
    return S_N, B_N, certified


def certified_log_K0(N: int, prec: int) -> tuple[arb, dict]:
    """Returns (log_K0_ball, audit_dict)."""
    _ensure_prec(prec + GUARD_BITS)
    S_N, B_N, certified_x_log2 = certified_logK0_times_log2(N, prec)
    log2_ball = arb(2).log()
    log_K0 = certified_x_log2 / log2_ball
    audit = {
        "N_truncation": N,
        "prec_bits": prec,
        "S_N_midpoint": str(S_N.mid()),
        "S_N_radius": str(S_N.rad()),
        "tail_bound_B_N_upper": str(B_N.upper()),
        "logK0_x_log2_midpoint": str(certified_x_log2.mid()),
        "logK0_x_log2_radius": str(certified_x_log2.rad()),
        "log2_midpoint": str(log2_ball.mid()),
        "log2_radius": str(log2_ball.rad()),
        "logK0_midpoint": str(log_K0.mid()),
        "logK0_radius": str(log_K0.rad()),
    }
    return log_K0, audit


def certified_K0(N: int, prec: int) -> tuple[arb, arb, dict]:
    """Returns (K0_ball, logK0_ball, audit_dict)."""
    log_K0, audit = certified_log_K0(N, prec)
    K0 = log_K0.exp()
    audit["K0_midpoint"] = str(K0.mid())
    audit["K0_radius"] = str(K0.rad())
    return K0, log_K0, audit


if __name__ == "__main__":
    import json, sys, time
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 7178
    N = required_N_for_precision(P, safety_bits=64)
    print(f"# BBC eq.(1) at P_bits={P}, truncation N={N}")
    t0 = time.time()
    K0, logK0, audit = certified_K0(N, P)
    t1 = time.time()
    audit["elapsed_seconds"] = round(t1 - t0, 4)
    print(json.dumps(audit, indent=2))
