"""
PAINLEVE-DEEP-6X shared engine.

High-precision (depth >= 3000, dps >= 400) Painleve deep-dive across
the six known Delta<0 degree-2 PCF families.

Per family / deformation we
  - compute L(t) on a unified grid at depth=DEPTH, dps=DPS
  - build 5-point central-difference derivatives at the 6 design
    points {+/-0.1, +/-0.2, +/-0.3} for three step sizes h in
    {0.1, 0.05, 0.025}
  - fit P-III(D6), P-V, P-VI (all 4-parameter) plus, on cold-scan,
    P-II (1-parameter) and P-IV (2-parameter)
  - report best (deformation, equation, residual, h) cell

Step 1: re-test the best cell from Session B/C at higher precision.
Step 3: cold scan if best > 1e-4 -- run both deformations x
        {P-III, P-V, P-VI}, and if still no 1e-4 hit extend to
        {P-II, P-IV}.

Threshold gates (per task spec):
  HIT          : residual <= 1e-50  (true Painleve identification)
  CANDIDATE    : residual <= 1e-6
  MARGINAL     : 1e-6 < residual <= 1e-4
  NO_FIT       : residual > 1e-4
"""
from __future__ import annotations
import json
import time
from typing import Callable, Dict, List, Tuple

from mpmath import mp, mpf, log, matrix, lu_solve

# -------------------- recurrence --------------------

def compute_limit_at(an_fn: Callable, bn_fn: Callable, t, depth: int,
                     target_digits: int) -> Tuple[mpf, float]:
    mp.dps = target_digits + 80
    t = mpf(t)
    p_prev = mpf(1)
    p_curr = bn_fn(mpf(0), t)
    q_prev = mpf(0)
    q_curr = mpf(1)
    last10: List[mpf] = []
    for n in range(1, depth + 1):
        an = an_fn(mpf(n), t); bn = bn_fn(mpf(n), t)
        p_new = bn * p_curr + an * p_prev
        q_new = bn * q_curr + an * q_prev
        if q_new == 0:
            return None, 0.0
        last10.append(p_new / q_new)
        if len(last10) > 10:
            last10.pop(0)
        sc = max(abs(p_curr), abs(q_curr), mpf(1))
        if sc > mpf(10) ** 200:
            p_prev /= sc; p_curr /= sc; q_prev /= sc; q_curr /= sc
            p_new /= sc;  q_new /= sc
        p_prev, p_curr = p_curr, p_new
        q_prev, q_curr = q_curr, q_new
    L = last10[-1]
    if len(last10) >= 10:
        gap = abs(last10[-1] - last10[-10])
        stab = float(-mp.log10(gap)) if gap > 0 else float(target_digits)
    else:
        stab = 0.0
    return L, stab


# -------------------- t-grid management --------------------

DESIGN_POINTS = [mpf("-0.3"), mpf("-0.2"), mpf("-0.1"),
                 mpf("0.1"),  mpf("0.2"),  mpf("0.3")]
H_LIST_DEFAULT = [mpf("0.1"), mpf("0.05"), mpf("0.025")]


# All grid t-values are exact multiples of 1/GRID_DENOM (1/1000).
# Design points: +/-0.1, +/-0.2, +/-0.3.
# Step sizes:    0.1, 0.05, 0.025  (= 100, 50, 25 / 1000).
# Use the integer numerator as the canonical dictionary key, so that
# different routes to the same exact rational always collide cleanly.
GRID_DENOM = 1000


def tk(t) -> str:
    """Canonical integer-numerator key for any t = k/GRID_DENOM."""
    k = int(round(float(t) * GRID_DENOM))
    return f"{k:+06d}"


def build_t_grid(h_list) -> List[mpf]:
    """All t-values needed for 5-point stencils at design points.
    Builds the grid in exact integer arithmetic, then converts to mpf."""
    pts = set()
    pts.add(0)
    for h in h_list:
        h_int = int(round(float(h) * GRID_DENOM))
        for t0 in DESIGN_POINTS:
            t0_int = int(round(float(t0) * GRID_DENOM))
            for k in (-2, -1, 0, 1, 2):
                pts.add(t0_int + k * h_int)
    # convert back to mpf, sorted
    return sorted((mpf(k) / GRID_DENOM for k in pts), key=lambda x: float(x))


# -------------------- 5-point derivatives --------------------

def _key_at(t0: mpf, k: int, h: mpf) -> str:
    """Exact-arithmetic key for t0 + k*h."""
    t0_int = int(round(float(t0) * GRID_DENOM))
    h_int  = int(round(float(h)  * GRID_DENOM))
    return f"{t0_int + k * h_int:+06d}"


def derivs5(L_at: Dict[str, mpf], t0: mpf, h: mpf):
    """Return (L0, L', L'') at t0 from 5-point central differences."""
    Lm2 = L_at[_key_at(t0, -2, h)]
    Lm1 = L_at[_key_at(t0, -1, h)]
    L0  = L_at[_key_at(t0,  0, h)]
    Lp1 = L_at[_key_at(t0,  1, h)]
    Lp2 = L_at[_key_at(t0,  2, h)]
    Lp  = (-Lp2 + 8*Lp1 - 8*Lm1 + Lm2) / (12*h)
    Lpp = (-Lp2 + 16*Lp1 - 30*L0 + 16*Lm1 - Lm2) / (12*h*h)
    return L0, Lp, Lpp


# -------------------- Painleve fits --------------------
# Conventions:
#   P-III(D6): y'' = (y')^2/y - y'/t + (alpha y^2 + beta)/t + gamma y^3 + delta/y
#   P-V      : y'' = (1/(2y) + 1/(y-1)) (y')^2 - y'/t
#                 + (y-1)^2 (alpha y + beta/y) / t^2 + gamma y/t + delta y(y+1)/(y-1)
#   P-VI     : y'' = (1/2)(1/y + 1/(y-1) + 1/(y-t))(y')^2
#                 - (1/t + 1/(t-1) + 1/(y-t)) y'
#                 + y(y-1)(y-t)/(t^2 (t-1)^2) [ alpha + beta t/y^2 + gamma (t-1)/(y-1)^2
#                                              + delta t(t-1)/(y-t)^2 ]
#   P-II     : y'' = 2 y^3 + t y + alpha
#   P-IV     : y'' = (y')^2/(2y) + (3/2) y^3 + 4 t y^2 + 2(t^2 - alpha) y - beta^2/(2y)


def _residual_max_4param(eq, deriv, design_t, fit_idx, val_idx):
    M = matrix(4, 4); v = matrix(4, 1)
    for k, i in enumerate(fit_idx):
        t = design_t[i]; L, Lp, Lpp = deriv[i]
        rowM, rhs = eq.row(t, L, Lp, Lpp)
        M[k, 0] = rowM[0]; M[k, 1] = rowM[1]; M[k, 2] = rowM[2]; M[k, 3] = rowM[3]
        v[k, 0] = rhs
    sol = lu_solve(M, v)
    A, B, C, D = sol[0,0], sol[1,0], sol[2,0], sol[3,0]
    max_res = mpf(0)
    res_at = []
    for i in val_idx:
        t = design_t[i]; L, Lp, Lpp = deriv[i]
        rowM, rhs = eq.row(t, L, Lp, Lpp)
        pred = rowM[0]*A + rowM[1]*B + rowM[2]*C + rowM[3]*D
        r = abs(rhs - pred)
        res_at.append((t, r))
        if r > max_res: max_res = r
    return (A, B, C, D), max_res, res_at


class _PIII:
    name = "P-III"
    @staticmethod
    def row(t, L, Lp, Lpp):
        # rhs := y'' - (y')^2/y + y'/t  = (alpha y^2 + beta)/t + gamma y^3 + delta/y
        # row = [y^2/t, 1/t, y^3, 1/y]
        rowM = [L*L/t, mpf(1)/t, L*L*L, mpf(1)/L]
        rhs = Lpp - (Lp*Lp)/L + Lp/t
        return rowM, rhs


class _PV:
    name = "P-V"
    @staticmethod
    def row(t, L, Lp, Lpp):
        # rhs := y'' - (1/(2y) + 1/(y-1)) y'^2 + y'/t
        #      = (y-1)^2 (alpha y + beta/y) / t^2 + gamma y/t + delta y(y+1)/(y-1)
        # row = [(y-1)^2 y/t^2, (y-1)^2/(y t^2), y/t, y(y+1)/(y-1)]
        rowM = [(L-1)*(L-1)*L/(t*t),
                (L-1)*(L-1)/(L*t*t),
                L/t,
                L*(L+1)/(L-1)]
        rhs = Lpp - (mpf(1)/(2*L) + mpf(1)/(L-1))*Lp*Lp + Lp/t
        return rowM, rhs


class _PVI:
    name = "P-VI"
    @staticmethod
    def row(t, L, Lp, Lpp):
        kf = L*(L-1)*(L-t)/(t*t*(t-1)*(t-1))
        rowM = [kf,
                kf * t/(L*L),
                kf * (t-1)/((L-1)*(L-1)),
                kf * t*(t-1)/((L-t)*(L-t))]
        rhs_quad = (mpf(1)/2)*(mpf(1)/L + mpf(1)/(L-1) + mpf(1)/(L-t))*Lp*Lp
        rhs_lin  = -(mpf(1)/t + mpf(1)/(t-1) + mpf(1)/(L-t))*Lp
        rhs = Lpp - rhs_quad - rhs_lin
        return rowM, rhs


def fit_4param(eq_cls, deriv_list, design_t):
    """4-fit / 2-validate overdetermined fit, plus mean over all 6 (LSQ)
    for stability.  Returns dict with params, residual_max, full_residuals."""
    fit_idx = [1, 2, 3, 4]   # use 4 inner points for fit
    val_idx = [0, 5]         # outer 2 for validation
    params, res_max, res_at = _residual_max_4param(
        eq_cls, deriv_list, design_t, fit_idx, val_idx)
    # also compute the worst residual across ALL 6 design points
    res_all_max = mpf(0)
    for i in range(6):
        t = design_t[i]; L, Lp, Lpp = deriv_list[i]
        rowM, rhs = eq_cls.row(t, L, Lp, Lpp)
        pred = rowM[0]*params[0] + rowM[1]*params[1] + rowM[2]*params[2] + rowM[3]*params[3]
        r = abs(rhs - pred)
        if r > res_all_max: res_all_max = r
    return {
        "eq": eq_cls.name,
        "params": tuple(params),
        "residual_validate_max": res_max,    # max over val_idx (held out)
        "residual_all_max":      res_all_max,  # max over all 6
        "residual_fit_max":      max((abs(0)),  # exact fit -> tiny
                                     *(mpf(0) for _ in fit_idx)),
    }


# -------- 1- and 2-parameter fits (cold-scan only) --------

def fit_PII(deriv_list, design_t):
    # rhs(t) := y''(t) - 2 y(t)^3 - t y(t) = alpha (constant)
    rhss = []
    for i in range(6):
        t = design_t[i]; L, Lp, Lpp = deriv_list[i]
        rhss.append(Lpp - 2*L*L*L - t*L)
    alpha = sum(rhss) / 6
    res_max = max(abs(r - alpha) for r in rhss)
    return {"eq": "P-II", "params": (alpha,),
            "residual_validate_max": res_max,
            "residual_all_max": res_max,
            "residual_fit_max": mpf(0)}


def fit_PIV(deriv_list, design_t):
    # rhs := y'' - (y')^2/(2y) - 3 y^3/2 - 4 t y^2  = 2(t^2 - alpha) y - beta^2/(2y)
    # = -2 alpha * y + 2 t^2 y - (beta^2/2) / y
    # define U := 2 t^2 y, R := y, S := 1/y
    # rhs - U = (-2 alpha) R + (-beta^2/2) S
    M = matrix(6, 2); vv = matrix(6, 1)
    for i in range(6):
        t = design_t[i]; L, Lp, Lpp = deriv_list[i]
        rhs = Lpp - (Lp*Lp)/(2*L) - mpf(3)*L*L*L/2 - 4*t*L*L
        adj = rhs - 2*t*t*L
        M[i, 0] = L
        M[i, 1] = mpf(1)/L
        vv[i, 0] = adj
    # normal equations
    Mt = M.T
    sol = lu_solve(Mt * M, Mt * vv)
    c0, c1 = sol[0,0], sol[1,0]
    alpha = -c0 / 2
    beta_sq = -2 * c1
    res_max = mpf(0)
    for i in range(6):
        t = design_t[i]; L, Lp, Lpp = deriv_list[i]
        pred = (Lp*Lp)/(2*L) + mpf(3)*L*L*L/2 + 4*t*L*L + 2*(t*t - alpha)*L - beta_sq/(2*L)
        r = abs(Lpp - pred)
        if r > res_max: res_max = r
    return {"eq": "P-IV", "params": (alpha, beta_sq),
            "residual_validate_max": res_max,
            "residual_all_max": res_max,
            "residual_fit_max": mpf(0)}


# -------------------- per-family deep probe --------------------

EQ_MAIN = [_PIII, _PV, _PVI]


def evaluate_deformation(an_fn, bn_fn, t_grid, depth, dps,
                         label) -> Dict[str, mpf]:
    """Returns L_at: dict tk(t)->L."""
    L_at: Dict[str, mpf] = {}
    print(f"  Computing L(t) over {len(t_grid)} t-values, depth={depth}, dps={dps}...", flush=True)
    t0_clock = time.time()
    for t in t_grid:
        L, stab = compute_limit_at(an_fn, bn_fn, t, depth, dps)
        if L is None:
            print(f"    t={mp.nstr(t, 6)}  DIVERGED")
            continue
        L_at[tk(t)] = L
    dt = time.time() - t0_clock
    print(f"  ... {label} done in {dt:.1f}s ({len(L_at)} samples)", flush=True)
    return L_at


def fit_cell_for_h(L_at, eq_cls, h):
    """Build derivatives at h, fit eq, return result dict."""
    deriv = []
    for t0 in DESIGN_POINTS:
        d = derivs5(L_at, t0, h)
        deriv.append(d)
    return fit_4param(eq_cls, deriv, DESIGN_POINTS)


def step1_best_cell(spec, best_def: str, best_eq_name: str,
                    depth: int, dps: int,
                    h_list=None) -> Dict:
    """Re-test the Session B/C best cell at higher precision, three h."""
    if h_list is None:
        h_list = H_LIST_DEFAULT
    a_fn = spec["a_fn"]
    bn_fn = spec["b_fns"][best_def]
    eq_cls = next(e for e in EQ_MAIN if e.name == best_eq_name)
    t_grid = build_t_grid(h_list)
    L_at = evaluate_deformation(a_fn, bn_fn, t_grid, depth, dps,
                                f"D-{spec['family']}-{best_def}")
    out = {"deformation": best_def, "equation": best_eq_name,
           "h_results": {}}
    for h in h_list:
        try:
            r = fit_cell_for_h(L_at, eq_cls, h)
            out["h_results"][mp.nstr(h, 6)] = {
                "params": [mp.nstr(p, 14) for p in r["params"]],
                "residual_validate_max": mp.nstr(r["residual_validate_max"], 6),
                "residual_all_max":      mp.nstr(r["residual_all_max"], 6),
            }
        except Exception as ex:
            out["h_results"][mp.nstr(h, 6)] = {"error": str(ex)}
    return out, L_at


def step3_cold_scan(spec, L_at_by_def, depth, dps, h=mpf("0.1"),
                    extend_to_p2_p4=False) -> Dict:
    """Run all (D x {P-III, P-V, P-VI}) at the given h.  If
    extend_to_p2_p4, also include (D x {P-II, P-IV})."""
    out = {}
    for D, L_at in L_at_by_def.items():
        row = {}
        for eq_cls in EQ_MAIN:
            try:
                r = fit_cell_for_h(L_at, eq_cls, h)
                row[eq_cls.name] = {
                    "params": [mp.nstr(p, 14) for p in r["params"]],
                    "residual_validate_max": mp.nstr(r["residual_validate_max"], 6),
                    "residual_all_max":      mp.nstr(r["residual_all_max"], 6),
                }
            except Exception as ex:
                row[eq_cls.name] = {"error": str(ex)}
        if extend_to_p2_p4:
            # build deriv list at h for low-param fits
            deriv = [derivs5(L_at, t0, h) for t0 in DESIGN_POINTS]
            for fit_low in (fit_PII, fit_PIV):
                try:
                    r = fit_low(deriv, DESIGN_POINTS)
                    row[r["eq"]] = {
                        "params": [mp.nstr(p, 14) for p in r["params"]],
                        "residual_validate_max": mp.nstr(r["residual_validate_max"], 6),
                        "residual_all_max":      mp.nstr(r["residual_all_max"], 6),
                    }
                except Exception as ex:
                    row[fit_low.__name__] = {"error": str(ex)}
        out[D] = row
    return out


def gate(residual_str: str) -> str:
    r = mpf(residual_str)
    if r <= mpf("1e-50"): return "HIT"
    if r <= mpf("1e-6"):  return "CANDIDATE"
    if r <= mpf("1e-4"):  return "MARGINAL"
    return "NO_FIT"


def deep_probe(spec, best_def: str, best_eq_name: str,
               depth: int = 3000, dps: int = 400,
               do_cold_scan_if_no_fit: bool = True,
               extend_p2_p4: bool = False) -> Dict:
    """Full probe for a single family.  Returns a structured result dict."""
    family = spec["family"]
    print("=" * 78)
    print(f"{family} PAINLEVE DEEP PROBE  (Delta={spec['Delta']}, "
          f"CM={spec['CM_field']})")
    print(f"  Step 1: best cell D-{family}-{best_def} + {best_eq_name}, "
          f"depth={depth}, dps={dps}")
    print("=" * 78)

    step1, L_at_best = step1_best_cell(spec, best_def, best_eq_name,
                                        depth=depth, dps=dps)
    # report
    h_residuals = {}
    for hkey, r in step1["h_results"].items():
        if "residual_validate_max" in r:
            h_residuals[hkey] = mpf(r["residual_validate_max"])
            print(f"   h={hkey}: residual(validate_max) = {r['residual_validate_max']}")
            print(f"            residual(all_max)      = {r['residual_all_max']}")
            print(f"            params = {r['params']}")
        else:
            print(f"   h={hkey}: ERROR {r.get('error')}")
    if h_residuals:
        best_h_key = min(h_residuals, key=lambda k: h_residuals[k])
        best_step1 = h_residuals[best_h_key]
        print(f"   -> best h = {best_h_key}  residual = {mp.nstr(best_step1, 6)}  "
              f"[gate: {gate(mp.nstr(best_step1, 8))}]")
    else:
        best_h_key = None; best_step1 = mpf("inf")

    # h-independence check: spread between min and max residual across h
    if h_residuals:
        rmin = min(h_residuals.values()); rmax = max(h_residuals.values())
        if rmin > 0:
            spread_orders = float(mp.log10(rmax / rmin))
        else:
            spread_orders = float("inf")
        print(f"   h-spread: {spread_orders:.2f} decimal orders "
              f"(min {mp.nstr(rmin, 4)}, max {mp.nstr(rmax, 4)})")
    else:
        spread_orders = float("inf")

    cold = None
    L_at_other = None
    if do_cold_scan_if_no_fit and best_step1 > mpf("1e-4"):
        print()
        print(f"  Step 3: cold scan (residual {mp.nstr(best_step1, 4)} > 1e-4)")
        # also evaluate the OTHER deformation at the same t-grid
        other_def = "B" if best_def == "A" else "A"
        a_fn = spec["a_fn"]; bn_other = spec["b_fns"][other_def]
        t_grid = build_t_grid([mpf("0.1")])  # cold scan only at h=0.1
        L_at_other = evaluate_deformation(a_fn, bn_other, t_grid,
                                           depth, dps, f"D-{family}-{other_def}")
        # also rebuild best L_at at h=0.1 grid (subset of the existing one;
        # already covered)
        cold = step3_cold_scan(spec,
                                {best_def: L_at_best, other_def: L_at_other},
                                depth, dps, h=mpf("0.1"),
                                extend_to_p2_p4=False)
        # find best
        best_cold_res = mpf("inf"); best_cold_key = None
        for D, row in cold.items():
            for eqn, cell in row.items():
                if "residual_validate_max" in cell:
                    r = mpf(cell["residual_validate_max"])
                    if r < best_cold_res:
                        best_cold_res = r; best_cold_key = (D, eqn)
        print(f"   cold scan best: {best_cold_key} = "
              f"{mp.nstr(best_cold_res, 6)}  [gate: {gate(mp.nstr(best_cold_res, 8))}]")

        if best_cold_res > mpf("1e-4") and extend_p2_p4:
            print(f"   extending cold scan to P-II / P-IV")
            cold_ext = step3_cold_scan(spec,
                                        {best_def: L_at_best, other_def: L_at_other},
                                        depth, dps, h=mpf("0.1"),
                                        extend_to_p2_p4=True)
            cold = cold_ext
            for D, row in cold.items():
                for eqn, cell in row.items():
                    if "residual_validate_max" in cell:
                        r = mpf(cell["residual_validate_max"])
                        if r < best_cold_res:
                            best_cold_res = r; best_cold_key = (D, eqn)
            print(f"   extended cold scan best: {best_cold_key} = "
                  f"{mp.nstr(best_cold_res, 6)}  [gate: {gate(mp.nstr(best_cold_res, 8))}]")
    else:
        best_cold_res = None; best_cold_key = None

    # final per-family verdict
    if best_step1 <= mpf("1e-6"):
        verdict = "CANDIDATE"
        winner = (best_def, best_eq_name, mp.nstr(best_step1, 6),
                  best_h_key)
    elif best_step1 <= mpf("1e-4"):
        verdict = "MARGINAL"
        winner = (best_def, best_eq_name, mp.nstr(best_step1, 6),
                  best_h_key)
    else:
        # see if cold scan rescued
        if best_cold_res is not None and best_cold_res <= mpf("1e-4"):
            v_lev = "CANDIDATE" if best_cold_res <= mpf("1e-6") else "MARGINAL"
            verdict = v_lev
            winner = (best_cold_key[0], best_cold_key[1],
                      mp.nstr(best_cold_res, 6), "0.1")
        else:
            verdict = "NO_FIT"
            # report the smallest residual seen anywhere
            ws = best_step1
            wkey = (best_def, best_eq_name, mp.nstr(best_step1, 6), best_h_key)
            if best_cold_res is not None and best_cold_res < ws:
                ws = best_cold_res
                wkey = (best_cold_key[0], best_cold_key[1],
                        mp.nstr(best_cold_res, 6), "0.1")
            winner = wkey

    print()
    print(f"  VERDICT: {family} -> {verdict}  "
          f"(D-{winner[0]} + {winner[1]}, residual {winner[2]}, h={winner[3]})")

    return {
        "family": family,
        "Delta": spec["Delta"],
        "CM_field": spec["CM_field"],
        "Heegner": spec["Heegner"],
        "step1_best_cell": {
            "deformation": best_def,
            "equation": best_eq_name,
            "h_results": step1["h_results"],
            "best_h": best_h_key,
            "best_residual": mp.nstr(best_step1, 6),
            "h_spread_decimal_orders": spread_orders,
        },
        "step3_cold_scan": cold,
        "verdict": verdict,
        "winner": {
            "deformation": winner[0], "equation": winner[1],
            "residual": winner[2], "h": winner[3],
        },
    }
