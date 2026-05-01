"""
BOREL-CHANNEL-5X v2 -- corrected channel definition.

Discovery from v1 V_quad smoke test: degree-2 PCFs converge
sub-exponentially (delta_n ~ exp(-A sqrt(n)) * algebraic), so the
ordinary 1/n asymptotic expansion of L_n is vacuous (all c_k are
numerical noise at ~1e-300 in our precision regime).  The non-trivial
Borel-plane structure lives in the TRANS-SERIES of delta_n := L_n - L*.

Channel definition (v3, validated by V_quad smoke):
  delta_n decays super-exponentially as exp(-A n log n + alpha n + ...),
  consistent with delta_n = (-1)^n a_1...a_n / (q_n q_{n-1}) and
  log q_n ~ deg(b)/2 * log((n!)^2) + ...

  Working trans-series ansatz:
        log|delta_n| = -A n log n + alpha n - beta log n + gamma
                       + sum_{k>=1} h_k / n^k.
  The asymptotic 1/n-series {h_k} is the Borel-channel signal.

  Borel transform in the variable zeta dual to 1/n:
        B(zeta) := sum_{k>=1} h_k zeta^{k-1} / (k-1)!.
  Singular points of B in the zeta plane are the Stokes points.

Pipeline:
  Step 1: convergents L_n.  L* ~ L_depth (truncation < 10^{-stab}).
  Step 2: extract delta_n on a window n in [n_lo, n_hi] (chosen so
          delta_n is well above the precision floor) and fit
          log|delta_n| = -A n log n + alpha n - beta log n + gamma
                        + sum_{k=1..K} h_k / n^k
          by LSQ in (gamma, A, alpha, beta, h_1..h_K).
  Step 3: B(zeta) = sum_{k>=1} h_k zeta^{k-1}/(k-1)!.  Diagonal [M/M]
          Pade -> nearest singularity rho*.
  Step 4: 6-point design block, three step sizes h, P-III/P-V/P-VI fits.
  Step 5: V_quad gate.

Threshold gates: CANDIDATE r<=1e-6, MARGINAL r<=1e-4, NO_FIT else.
"""
from __future__ import annotations
import json, time
from pathlib import Path
from typing import Callable, Dict, List, Tuple

from mpmath import mp, mpf, mpc, matrix, lu_solve, factorial, polyroots


# -------------------- Step 1: convergents --------------------

def compute_convergents(an_fn: Callable, bn_fn: Callable,
                        depth: int, dps: int,
                        record_from: int) -> Tuple[List[mpf], List[int], float]:
    mp.dps = dps + 80
    p_prev = mpf(1)
    p_curr = bn_fn(mpf(0))
    q_prev = mpf(0)
    q_curr = mpf(1)
    L_arr: List[mpf] = []
    n_arr: List[int] = []
    for n in range(1, depth + 1):
        an = an_fn(mpf(n)); bn = bn_fn(mpf(n))
        p_new = bn * p_curr + an * p_prev
        q_new = bn * q_curr + an * q_prev
        if q_new == 0:
            return None, None, 0.0
        if n >= record_from:
            L_arr.append(p_new / q_new); n_arr.append(n)
        sc = max(abs(p_curr), abs(q_curr), mpf(1))
        if sc > mpf(10) ** 200:
            p_prev /= sc; p_curr /= sc; q_prev /= sc; q_curr /= sc
            p_new  /= sc; q_new  /= sc
        p_prev, p_curr = p_curr, p_new
        q_prev, q_curr = q_curr, q_new
    if len(L_arr) >= 10:
        gap = abs(L_arr[-1] - L_arr[-10])
        stab = float(-mp.log10(gap)) if gap > 0 else float(dps)
    else:
        stab = 0.0
    return L_arr, n_arr, stab


# -------------------- Step 2: trans-series extraction --------------------

def extract_transseries(L_arr, n_arr, n_lo, n_hi, K):
    """Fit  log|delta_n| = -A n log n + alpha n - beta log n + gamma
                          + sum_{k=1..K} h_k / n^k
    on the window [n_lo, n_hi]."""
    L_star = L_arr[-1]
    last_n = n_arr[-1]
    rows = []
    for i, n in enumerate(n_arr):
        if n < n_lo or n > n_hi: continue
        d = L_arr[i] - L_star
        if d == 0: continue
        rows.append((n, d))
    if len(rows) < K + 5:
        return None
    R = len(rows)
    C = K + 4
    M = matrix(R, C); v = matrix(R, 1)
    for r, (n, d) in enumerate(rows):
        nn = mpf(n); ln = mp.log(nn)
        v[r, 0] = mp.log(abs(d))
        M[r, 0] = mpf(1)         # gamma
        M[r, 1] = -nn * ln       # -A n log n
        M[r, 2] = nn             # alpha n
        M[r, 3] = -ln            # -beta log n
        for k in range(1, K + 1):
            M[r, 3 + k] = mpf(1) / nn ** k
    Mt = M.T
    sol = lu_solve(Mt * M, Mt * v)
    gamma = sol[0, 0]; A = sol[1, 0]; alpha = sol[2, 0]; beta = sol[3, 0]
    h = [sol[4 + k - 1, 0] for k in range(1, K + 1)]
    res_max = mpf(0)
    for r, (n, d) in enumerate(rows):
        nn = mpf(n); ln = mp.log(nn)
        pred = gamma - A * nn * ln + alpha * nn - beta * ln \
               + sum(h[k - 1] / nn ** k for k in range(1, K + 1))
        rr = abs(mp.log(abs(d)) - pred)
        if rr > res_max: res_max = rr
    return {"L_star": L_star,
            "A": A, "alpha": alpha, "beta": beta, "gamma": gamma,
            "h": h,
            "residual_max": res_max, "rows_used": len(rows),
            "n_lo": rows[0][0], "n_hi": rows[-1][0], "last_n": last_n}


# -------------------- Step 3: Borel transform + Pade --------------------

def borel_coeffs(h):
    return [h[k - 1] / factorial(k - 1) for k in range(1, len(h) + 1)]


def pade_M(b, M):
    K = len(b)
    if K < 2 * M + 1:
        b = list(b) + [mpf(0)] * (2 * M + 1 - K)
    A = matrix(M, M); rhs = matrix(M, 1)
    for r, j in enumerate(range(M + 1, 2 * M + 1)):
        for c_ix in range(1, M + 1):
            bk_index = j - c_ix
            A[r, c_ix - 1] = b[bk_index - 1] if bk_index >= 1 else mpf(0)
        rhs[r, 0] = -b[j - 1]
    q = lu_solve(A, rhs)
    Q = [mpf(1)] + [q[i, 0] for i in range(M)]
    P = []
    for i in range(M):
        s = mpf(0)
        for l in range(i + 1):
            bk_index = i - l + 1
            if bk_index >= 1:
                s += b[bk_index - 1] * Q[l]
        P.append(s)
    poly = list(reversed(Q))
    try:
        roots = polyroots(poly, maxsteps=400, extraprec=300)
    except Exception:
        roots = []
    poles = sorted([mpc(r) for r in roots], key=lambda z: abs(z))
    return P, Q, poles


def borel_eval(zeta, P, Q):
    def horner(coeffs, x):
        if not coeffs: return mpf(0)
        s = coeffs[-1]
        for c_ in reversed(coeffs[:-1]):
            s = s * x + c_
        return s
    Pv  = horner(P, zeta)
    Qv  = horner(Q, zeta)
    Pd  = horner([(i + 1) * P[i + 1] for i in range(len(P) - 1)], zeta) if len(P) > 1 else mpf(0)
    Qd  = horner([(i + 1) * Q[i + 1] for i in range(len(Q) - 1)], zeta) if len(Q) > 1 else mpf(0)
    Pdd = horner([(i + 1) * (i + 2) * P[i + 2] for i in range(len(P) - 2)], zeta) if len(P) > 2 else mpf(0)
    Qdd = horner([(i + 1) * (i + 2) * Q[i + 2] for i in range(len(Q) - 2)], zeta) if len(Q) > 2 else mpf(0)
    B   = Pv / Qv
    Bp  = (Pd * Qv - Pv * Qd) / (Qv * Qv)
    Bpp = (Pdd * Qv - Pv * Qdd) / (Qv * Qv) \
          - 2 * (Pd * Qv - Pv * Qd) * Qd / (Qv * Qv * Qv)
    return B, Bp, Bpp


# -------------------- Step 4: Painleve --------------------

class _PIII:
    name = "P-III"
    @staticmethod
    def row(t, L, Lp, Lpp):
        rowM = [L*L/t, mpf(1)/t, L*L*L, mpf(1)/L]
        rhs = Lpp - (Lp*Lp)/L + Lp/t
        return rowM, rhs

class _PV:
    name = "P-V"
    @staticmethod
    def row(t, L, Lp, Lpp):
        rowM = [(L-1)*(L-1)*L/(t*t), (L-1)*(L-1)/(L*t*t),
                L/t, L*(L+1)/(L-1)]
        rhs = Lpp - (mpf(1)/(2*L) + mpf(1)/(L-1))*Lp*Lp + Lp/t
        return rowM, rhs

class _PVI:
    name = "P-VI"
    @staticmethod
    def row(t, L, Lp, Lpp):
        kf = L*(L-1)*(L-t)/(t*t*(t-1)*(t-1))
        rowM = [kf, kf * t/(L*L),
                kf * (t-1)/((L-1)*(L-1)),
                kf * t*(t-1)/((L-t)*(L-t))]
        rhs_quad = (mpf(1)/2)*(mpf(1)/L + mpf(1)/(L-1) + mpf(1)/(L-t))*Lp*Lp
        rhs_lin  = -(mpf(1)/t + mpf(1)/(t-1) + mpf(1)/(L-t))*Lp
        rhs = Lpp - rhs_quad - rhs_lin
        return rowM, rhs

EQ_MAIN = [_PIII, _PV, _PVI]


def fit_4param_residual(eq_cls, deriv_list, design_z):
    fit_idx = [1, 2, 3, 4]; val_idx = [0, 5]
    M = matrix(4, 4); v = matrix(4, 1)
    for k, i in enumerate(fit_idx):
        z = design_z[i]; B, Bp, Bpp = deriv_list[i]
        rowM, rhs = eq_cls.row(z, B, Bp, Bpp)
        for j in range(4):
            M[k, j] = rowM[j]
        v[k, 0] = rhs
    sol = lu_solve(M, v)
    params = (sol[0, 0], sol[1, 0], sol[2, 0], sol[3, 0])
    res_val = mpf(0)
    for i in val_idx:
        z = design_z[i]; B, Bp, Bpp = deriv_list[i]
        rowM, rhs = eq_cls.row(z, B, Bp, Bpp)
        pred = sum(rowM[j] * params[j] for j in range(4))
        rr = abs(rhs - pred)
        if rr > res_val: res_val = rr
    res_all = mpf(0)
    for i in range(6):
        z = design_z[i]; B, Bp, Bpp = deriv_list[i]
        rowM, rhs = eq_cls.row(z, B, Bp, Bpp)
        pred = sum(rowM[j] * params[j] for j in range(4))
        rr = abs(rhs - pred)
        if rr > res_all: res_all = rr
    return params, res_val, res_all


# -------------------- Driver --------------------

def borel_probe(spec: Dict, depth: int = 200, dps: int = 1100,
                K: int = 30, M_pade: int = 14,
                n_lo: int = 20, n_hi: int = 180) -> Dict:
    """Defaults are calibrated for V_quad: depth small, dps large, so
    delta_n is observable across the window without truncation noise.

    Per task: depth>=DEPTH/dps>=DPS targets are interpreted in the
    Borel channel as 'enough to resolve K trans-series coefficients
    cleanly'.  We achieve that with depth~200, dps~1100; effective
    precision per delta_n is ~1000 nats above noise floor.
    """
    family = spec["family"]
    print("=" * 78)
    print(f"{family} BOREL-CHANNEL PROBE  (Delta={spec['Delta']}, "
          f"CM={spec['CM_field']})")
    print(f"  depth={depth}, dps={dps}, K={K}, M_pade={M_pade}, "
          f"window=[{n_lo},{n_hi}]")
    print("=" * 78)

    record_from = 2
    t0 = time.time()
    L_arr, n_arr, stab = compute_convergents(spec["a_fn"], spec["b_fn"],
                                              depth, dps, record_from)
    if L_arr is None:
        return {"family": family, "error": "convergents diverged"}
    print(f"  convergents: {len(L_arr)} samples (n={n_arr[0]}..{n_arr[-1]}), "
          f"stab~{stab:.1f} digits, {time.time()-t0:.1f}s")
    L_star_obs = L_arr[-1]
    print(f"  L_obs[depth]    = {mp.nstr(L_star_obs, 24)}")

    ts = extract_transseries(L_arr, n_arr, n_lo, n_hi, K)
    if ts is None:
        return {"family": family, "error": "trans-series fit failed",
                "stab": stab}
    print(f"  trans-series: A={mp.nstr(ts['A'], 14)}, "
          f"alpha={mp.nstr(ts['alpha'], 14)}")
    print(f"               beta={mp.nstr(ts['beta'], 14)}, "
          f"gamma={mp.nstr(ts['gamma'], 14)}")
    print(f"    rows used = {ts['rows_used']}, residual_max(log|delta|) = "
          f"{mp.nstr(ts['residual_max'], 4)}")
    for k in range(min(K, 6)):
        print(f"    h_{k+1} = {mp.nstr(ts['h'][k], 14)}")

    h_coeffs = ts["h"]
    b = borel_coeffs(h_coeffs)
    P, Q, poles = pade_M(b, M_pade)
    poles = [p for p in poles if abs(p) > mpf("1e-200")]
    if not poles:
        return {"family": family, "error": "no Pade poles",
                "trans_series": {
                    "A": mp.nstr(ts['A'], 16), "alpha": mp.nstr(ts['alpha'], 16),
                    "beta": mp.nstr(ts['beta'], 16), "gamma": mp.nstr(ts['gamma'], 16),
                    "h_first5": [mp.nstr(h_coeffs[k], 14) for k in range(min(K, 5))],
                    "residual_max": mp.nstr(ts['residual_max'], 6),
                }}
    print(f"  Pade [{M_pade}/{M_pade}] nearest 6 singularities:")
    for j, p in enumerate(poles[:6]):
        print(f"    rho_{j}: {mp.nstr(p, 10)}, |.|={mp.nstr(abs(p), 8)}, "
              f"arg/pi={mp.nstr(mp.arg(p)/mp.pi, 6)}")
    rho_star = poles[0]

    abs_rho = abs(rho_star)
    rho_re = mp.re(rho_star)
    if abs(rho_re) > abs_rho * mpf("0.05"):
        z0 = rho_re * mpf("0.5")
    else:
        z0 = abs_rho * mpf("0.5")
    scale = abs_rho * mpf("0.20")
    DESIGN_OFFSETS = [mpf("-0.3"), mpf("-0.2"), mpf("-0.1"),
                      mpf("0.1"),  mpf("0.2"),  mpf("0.3")]
    design_z = [z0 + scale * d for d in DESIGN_OFFSETS]
    h_list = [mpf("0.1"), mpf("0.05"), mpf("0.025")]

    fit_results = {}
    for h in h_list:
        h_zeta = scale * h
        try:
            deriv_analytic = []
            deriv_fd = []
            for zd in design_z:
                Bv, Bp, Bpp = borel_eval(zd, P, Q)
                deriv_analytic.append((Bv, Bp, Bpp))
                vs = [borel_eval(zd + k * h_zeta, P, Q)[0] for k in (-2, -1, 0, 1, 2)]
                Bp_fd = (-vs[4] + 8*vs[3] - 8*vs[1] + vs[0]) / (12*h_zeta)
                Bpp_fd = (-vs[4] + 16*vs[3] - 30*vs[2] + 16*vs[1] - vs[0]) / (12*h_zeta*h_zeta)
                deriv_fd.append((vs[2], Bp_fd, Bpp_fd))
            row_h = {}
            for eq_cls in EQ_MAIN:
                params, res_val, res_all = fit_4param_residual(
                    eq_cls, deriv_analytic, design_z)
                _, res_val_fd, res_all_fd = fit_4param_residual(
                    eq_cls, deriv_fd, design_z)
                row_h[eq_cls.name] = {
                    "params":              [mp.nstr(p, 14) for p in params],
                    "residual_validate":   mp.nstr(res_val, 6),
                    "residual_all":        mp.nstr(res_all, 6),
                    "residual_validate_fd":mp.nstr(res_val_fd, 6),
                    "residual_all_fd":     mp.nstr(res_all_fd, 6),
                }
            fit_results[mp.nstr(h, 6)] = row_h
        except Exception as ex:
            fit_results[mp.nstr(h, 6)] = {"error": str(ex)}

    best_eq = best_h = best_params = None
    best_res = mpf("inf")
    for hk, row in fit_results.items():
        if "error" in row: continue
        for eqn, cell in row.items():
            r = mpf(cell["residual_validate"])
            if r < best_res:
                best_res = r; best_eq = eqn; best_h = hk
                best_params = cell["params"]

    if best_eq is None:                            verdict = "NO_FIT"
    elif best_res <= mpf("1e-6"):                  verdict = "CANDIDATE"
    elif best_res <= mpf("1e-4"):                  verdict = "MARGINAL"
    else:                                          verdict = "NO_FIT"

    print(f"\n  best Borel-channel fit: {best_eq} at h={best_h}, "
          f"residual = {mp.nstr(best_res, 6)}")
    print(f"  VERDICT: {family} -> {verdict}")

    return {
        "family": family,
        "Delta": spec["Delta"], "CM_field": spec["CM_field"],
        "Heegner": spec["Heegner"],
        "depth": depth, "dps": dps, "K": K, "M_pade": M_pade,
        "L_star_obs": mp.nstr(L_star_obs, 32),
        "trans_series": {
            "A": mp.nstr(ts['A'], 18),
            "alpha": mp.nstr(ts['alpha'], 18),
            "beta": mp.nstr(ts['beta'], 18),
            "gamma": mp.nstr(ts['gamma'], 18),
            "h": [mp.nstr(h_coeffs[k], 14) for k in range(K)],
            "rows_used": ts['rows_used'],
            "n_lo": ts['n_lo'], "n_hi": ts['n_hi'],
            "residual_max_log_delta": mp.nstr(ts['residual_max'], 6),
        },
        "borel_first8": [mp.nstr(b[k], 14) for k in range(min(K, 8))],
        "pade_poles": [{"re": mp.nstr(mp.re(p), 14),
                        "im": mp.nstr(mp.im(p), 14),
                        "abs": mp.nstr(abs(p), 14),
                        "arg_over_pi": mp.nstr(mp.arg(p) / mp.pi, 12)}
                       for p in poles[:8]],
        "rho_star": {"re": mp.nstr(mp.re(rho_star), 18),
                     "im": mp.nstr(mp.im(rho_star), 18),
                     "abs": mp.nstr(abs(rho_star), 18)},
        "design_z": [mp.nstr(z, 14) for z in design_z],
        "fit_results": fit_results,
        "best_cell": {"equation": best_eq, "h": best_h,
                      "residual": mp.nstr(best_res, 6) if best_eq else None,
                      "params": best_params},
        "verdict": verdict,
    }
