#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 1.4 — Hankel-thimble period of B-hat at -xi0,
# numerical evaluation of the Gamma-factor mechanism that produces C.
#
# Geometry (corrected, VQUAD-002): B-hat(xi) has its dominant Borel branch at
# xi = -xi0 = -2/sqrt3, local form  B-hat(xi) ~ A (xi+xi0)^{-(1+beta)},
# branch exponent -(1+beta) = -1+sqrt3/9 (operator indicial root).
#
# The rapid-decay Hankel thimble gamma wraps the cut (-inf,-xi0] (e^{+xi} decays as
# Re xi -> -inf). Its LEADING (alien-derivative) contribution is, in closed form,
#   P_lead = A * 2i sin(pi(1+beta)) * e^{-xi0} * Gamma(-beta).
# Using  Gamma(1+beta)Gamma(-beta) = -pi/sin(pi beta)  and  A = (S/2pi i)Gamma(1+beta),
# this collapses EXACTLY to  P_lead = S * e^{-xi0}   (verified below, symbolic+numeric).
# Stripping the action e^{-xi0} (FJ normalisation f=-(xi+xi0)) gives the period = S;
# the connection coefficient is the same datum reweighted:  C = (|Gamma(beta)|/2pi) S.
#
# This script extracts the branch amplitude A from the large-order Borel coefficients
# b_m = a_{m+1}/m!  (a_n via the deposited REPRODUCE_stokes_2piK recursion, INDEPENDENT
# of the Q3 port), Richardson-accelerates A_m -> A, and checks every Gamma-factor
# relation to high precision.
import json
import mpmath as mp

mp.mp.dps = 260

# ---- deposited constants (numerical-check.md T1; stokes_2piK_results.json) ----
K_DEP = mp.mpf("0.0728781025518669641294423633296525128045556892")
S_DEP = mp.mpf("0.457906623169017636119097842548225837962395135")
C_DEP = mp.mpf("0.437705286193537221230739749794369589981725597")

r3   = mp.sqrt(3)
xi0  = 2 / r3
beta = -1 / (3 * r3)             # -0.19245008972987526...
onep = 1 + beta                  # 1+beta = 0.807549910...   (so -(1+beta) is the branch exp)

def a_n_mpmath(order):
    sigma = -1 / mp.sqrt(mp.mpf(3))
    O = order + 12
    c = [mp.mpf(0)] * (O + 1); c[0] = sigma; c[1] = -1 - sigma / 6
    d = [mp.mpf(0)] * (O + 1); d[0] = c[0] ** 2; d[1] = 2 * c[0] * c[1]
    for k in range(2, O + 1):
        known = mp.fsum(c[i] * c[k - i] for i in range(1, k))
        rest = 3 * (known - (k - 1) * c[k - 1]) + d[k - 1] + d[k - 2] + 6 * c[k - 1] + c[k - 2]
        c[k] = -rest / (6 * c[0])
        d[k] = 2 * c[0] * c[k] + known - (k - 1) * c[k - 1]
    f = [mp.mpf(0)] * (order + 1)
    for k in range(1, order + 1):
        if k + 1 < len(c):
            f[k] = -c[k + 1] / k
    a = [mp.mpf(0)] * (order + 1); a[0] = mp.mpf(1)
    for n in range(1, order + 1):
        a[n] = mp.fsum(k * f[k] * a[n - k] for k in range(1, n + 1)) / n
    return a

def neville_at_zero(xs, ys):
    """Polynomial extrapolation (Neville) of (xs->ys) evaluated at x=0."""
    m = len(xs); T = [list(ys)]
    for k in range(1, m):
        row = []
        for i in range(m - k):
            num = (0 - xs[i + k]) * T[k - 1][i] - (0 - xs[i]) * T[k - 1][i + 1]
            row.append(num / (xs[i] - xs[i + k]))
        T.append(row)
    return T[-1][0]

def main():
    ORDER = 820
    a = a_n_mpmath(ORDER)
    # b_m = a_{m+1}/m!
    fact = [mp.factorial(m) for m in range(ORDER + 1)]
    b = [a[m + 1] / fact[m] for m in range(ORDER - 1)]

    # A_m = b_m (-1)^m Gamma(1+beta) m! xi0^{m+1+beta} / Gamma(m+1+beta)  ->  A=K*Gamma(1+beta)
    G1pb = mp.gamma(onep)
    def A_m(m):
        return (b[m] * mp.power(-1, m) * G1pb * fact[m]
                * mp.power(xi0, m + 1 + beta) / mp.gamma(m + 1 + beta))

    # Richardson/Neville over 1/m using a window near the top order
    ms = list(range(ORDER - 40 - 2, ORDER - 2))           # ~40 nodes
    xs = [mp.mpf(1) / m for m in ms]
    ys = [A_m(m) for m in ms]
    A_inf = neville_at_zero(xs, ys)

    # convergence estimate: compare to a shorter window
    ms2 = list(range(ORDER - 70 - 2, ORDER - 30 - 2))
    A_inf2 = neville_at_zero([mp.mpf(1) / m for m in ms2], [A_m(m) for m in ms2])
    conv_digits = (mp.inf if A_inf == A_inf2
                   else -mp.log10(abs(A_inf - A_inf2) / abs(A_inf)))

    # ---- relation 1: |A| == K * Gamma(1+beta) ----
    A_pred = K_DEP * G1pb
    rel_A = abs(A_inf - A_pred) / abs(A_pred)

    # ---- relation 2 (closed form): leading Hankel period magnitude == S*e^{-xi0} ----
    # |P_lead| = 2 A sin(pi(1+beta))... (A>0); use extracted A_inf
    P_lead_over_action = 2 * A_inf * abs(mp.sin(mp.pi * onep)) * mp.gamma(-beta)  # = |P_lead|/e^{-xi0}
    S_from_period = P_lead_over_action
    rel_S = abs(S_from_period - S_DEP) / S_DEP

    # symbolic collapse check: 2 K Gamma(1+beta) Gamma(-beta) |sin pi(1+beta)| == 2 pi K == S
    collapse = 2 * K_DEP * G1pb * mp.gamma(-beta) * abs(mp.sin(mp.pi * onep))
    rel_collapse = abs(collapse - S_DEP) / S_DEP

    # ---- relation 3: C == |A|/|beta|  and  C == (|Gamma(beta)|/2pi) S ----
    C_from_A = A_inf / abs(beta)
    rel_C1 = abs(C_from_A - C_DEP) / C_DEP
    C_from_S = abs(mp.gamma(beta)) / (2 * mp.pi) * S_DEP
    rel_C2 = abs(C_from_S - C_DEP) / C_DEP

    out = {
        "dps": mp.mp.dps, "order": ORDER,
        "beta": mp.nstr(beta, 30), "xi0": mp.nstr(xi0, 30),
        "branch_exponent_-(1+beta)": mp.nstr(-onep, 30),
        "A_extracted": mp.nstr(A_inf, 50),
        "A_predicted_K*Gamma(1+beta)": mp.nstr(A_pred, 50),
        "A_self_convergence_digits": mp.nstr(conv_digits, 6),
        "rel_err_|A|=K*Gamma(1+beta)": mp.nstr(rel_A, 6),
        "S_reconstructed_from_period": mp.nstr(S_from_period, 50),
        "rel_err_leadingHankel=S": mp.nstr(rel_S, 6),
        "rel_err_symbolic_collapse_2piK": mp.nstr(rel_collapse, 6),
        "C_from_A=|A|/|beta|": mp.nstr(C_from_A, 50),
        "rel_err_C=|A|/|beta|": mp.nstr(rel_C1, 6),
        "C_from_S=(|Gamma(beta)|/2pi)S": mp.nstr(C_from_S, 50),
        "rel_err_C=(|Gamma(beta)|/2pi)S": mp.nstr(rel_C2, 6),
        "leading_Hankel_period": "P_lead = S * e^{-xi0}  (action-stripped period = S; C = (|Gamma(beta)|/2pi) S)",
    }
    # gate: skeleton reproduced to < 1e-40 ?
    worst = max(rel_A, rel_S, rel_collapse, rel_C1, rel_C2)
    out["worst_relative_error"] = mp.nstr(worst, 6)
    out["HALT_GATE_1_skeleton"] = "PASS (<1e-40)" if worst < mp.mpf(10) ** (-40) else f"precision {mp.nstr(-mp.log10(worst),4)} digits"

    path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
            r"\PERIOD-REP-VQUAD-003\scripts\stage1_hankel_results.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
    for k, v in out.items():
        print(f"  {k}: {v}")
    print("[wrote]", path)

if __name__ == "__main__":
    main()
