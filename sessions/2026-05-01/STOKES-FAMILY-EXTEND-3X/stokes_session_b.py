"""
Session B Stokes/Painleve template, shared across QL families.

Given a family spec:
  family_id, an_fn(n,t), bA_fn(n,t), bB_fn(n,t), prior_L0_str, meta
runs the QL15-style 6-step probe:
  S1: identify D-A (gamma scaling) and D-B (root-radius) deformations  [in spec]
  S2: L(t) at 11 t-values to 250 dps, h in {0.05, 0.1}
  S3: S(t) at t in {+/-0.1, +/-0.2, +/-0.3} -- 6 values per deformation
  S4: sigma(t) and derivative growth |L^(k)(0)| for k=1..4
  S5: 2 x 3 Painleve residual matrix (P-III/P-V/P-VI) per family
  S6: PSLQ status carried forward (input string)

Numerics mirror sessions/2026-04-30/QL15-STOKES/ql15_stokes.py exactly so
that the per-family ql02/ql06/ql26 outputs are commensurable with QL15.
"""
import json, hashlib
from mpmath import mp, mpf, log, matrix, lu_solve

# ---------------- recurrence engine ----------------
def compute_limit_at(an_fn, bn_fn, t, depth, target_digits):
    mp.dps = target_digits + 60
    t = mpf(t)
    p_prev = mpf(1)
    p_curr = bn_fn(mpf(0), t)
    q_prev = mpf(0)
    q_curr = mpf(1)
    last6 = []
    for n in range(1, depth + 1):
        an = an_fn(mpf(n), t); bn = bn_fn(mpf(n), t)
        p_new = bn * p_curr + an * p_prev
        q_new = bn * q_curr + an * q_prev
        if q_new == 0:
            return None, 0
        last6.append(p_new / q_new)
        if len(last6) > 6:
            last6.pop(0)
        sc = max(abs(p_curr), abs(q_curr), mpf(1))
        if sc > mpf(10) ** 200:
            p_prev /= sc; p_curr /= sc; q_prev /= sc; q_curr /= sc
            p_new /= sc; q_new /= sc
        p_prev, p_curr = p_curr, p_new
        q_prev, q_curr = q_curr, q_new
    L = last6[-1]
    if len(last6) >= 6:
        gap = abs(last6[-1] - last6[-6])
        stab = float(-mp.log10(gap)) if gap > 0 else target_digits
    else:
        stab = 0.0
    return L, stab


T_LABELS = ["-0.5", "-0.4", "-0.3", "-0.2", "-0.1", "0.0",
            "0.1", "0.2", "0.3", "0.4", "0.5"]
T_VALUES = [mpf(s) for s in T_LABELS]


def tk(t):
    return f"{float(t):+.1f}"


# ---------------- numerical derivatives ----------------
def make_derivs(L_at):
    h = mpf("0.1")
    def Lk(t):
        return L_at[tk(t)]
    INTERIOR = [mpf("-0.3"), mpf("-0.2"), mpf("-0.1"),
                mpf("0.1"),  mpf("0.2"),  mpf("0.3")]
    out = {}
    for t in INTERIOR:
        L = Lk(t)
        Lp5 = (-Lk(t + 2*h) + 8*Lk(t + h) - 8*Lk(t - h) + Lk(t - 2*h)) / (12*h)
        Lpp5 = (-Lk(t + 2*h) + 16*Lk(t + h) - 30*Lk(t) + 16*Lk(t - h) - Lk(t - 2*h)) / (12*h*h)
        try:
            Lp7 = (Lk(t - 3*h) - 9*Lk(t - 2*h) + 45*Lk(t - h) - 45*Lk(t + h) + 9*Lk(t + 2*h) - Lk(t + 3*h)) / (-60*h)
            Lpp7 = (2*Lk(t - 3*h) - 27*Lk(t - 2*h) + 270*Lk(t - h) - 490*Lk(t) + 270*Lk(t + h) - 27*Lk(t + 2*h) + 2*Lk(t + 3*h)) / (180*h*h)
            sd_p  = abs(Lp5 - Lp7)
            sd_pp = abs(Lpp5 - Lpp7)
        except KeyError:
            sd_p = sd_pp = None
        out[tk(t)] = (L, Lp5, Lpp5, sd_p, sd_pp)
    return out, INTERIOR


# ---------------- Painleve ansatz fits ----------------
def fit_PIII(deriv, fit_idx, all_idx, all_t):
    M = matrix(4, 4); v = matrix(4, 1)
    for k, i in enumerate(fit_idx):
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        M[k, 0] = L*L/t; M[k, 1] = mpf(1)/t; M[k, 2] = L*L*L; M[k, 3] = mpf(1)/L
        v[k, 0] = Lpp - (Lp*Lp)/L + Lp/t
    sol = lu_solve(M, v)
    A, B, C, D = sol[0,0], sol[1,0], sol[2,0], sol[3,0]
    max_val = mpf(0)
    for i in all_idx:
        if i in fit_idx: continue
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        rhs = (Lp*Lp)/L - Lp/t + (A*L*L + B)/t + C*L*L*L + D/L
        max_val = max(max_val, abs(Lpp - rhs))
    return (A, B, C, D), max_val


def fit_PV(deriv, fit_idx, all_idx, all_t):
    M = matrix(4, 4); v = matrix(4, 1)
    for k, i in enumerate(fit_idx):
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        M[k, 0] = (L-1)*(L-1)*L/(t*t)
        M[k, 1] = (L-1)*(L-1)/(L*t*t)
        M[k, 2] = L/t
        M[k, 3] = L*(L+1)/(L-1)
        v[k, 0] = Lpp - (mpf(1)/(2*L) + mpf(1)/(L-1))*Lp*Lp + Lp/t
    sol = lu_solve(M, v)
    A, B, C, D = sol[0,0], sol[1,0], sol[2,0], sol[3,0]
    max_val = mpf(0)
    for i in all_idx:
        if i in fit_idx: continue
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        rhs = ((mpf(1)/(2*L) + mpf(1)/(L-1))*Lp*Lp - Lp/t
               + (L-1)*(L-1)*(A*L + B/L)/(t*t) + C*L/t + D*L*(L+1)/(L-1))
        max_val = max(max_val, abs(Lpp - rhs))
    return (A, B, C, D), max_val


def fit_PVI(deriv, fit_idx, all_idx, all_t):
    M = matrix(4, 4); v = matrix(4, 1)
    for k, i in enumerate(fit_idx):
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        kf = L*(L-1)*(L-t)/(t*t*(t-1)*(t-1))
        M[k, 0] = kf * mpf(1)
        M[k, 1] = kf * t/(L*L)
        M[k, 2] = kf * (t-1)/((L-1)*(L-1))
        M[k, 3] = kf * t*(t-1)/((L-t)*(L-t))
        rhs_quad = (mpf(1)/2)*(mpf(1)/L + mpf(1)/(L-1) + mpf(1)/(L-t))*Lp*Lp
        rhs_lin  = -(mpf(1)/t + mpf(1)/(t-1) + mpf(1)/(L-t))*Lp
        v[k, 0] = Lpp - rhs_quad - rhs_lin
    sol = lu_solve(M, v)
    A, B, C, D = sol[0,0], sol[1,0], sol[2,0], sol[3,0]
    max_val = mpf(0)
    for i in all_idx:
        if i in fit_idx: continue
        t = all_t[i]; L, Lp, Lpp, _, _ = deriv[tk(t)]
        kf = L*(L-1)*(L-t)/(t*t*(t-1)*(t-1))
        rhs = ((mpf(1)/2)*(mpf(1)/L + mpf(1)/(L-1) + mpf(1)/(L-t))*Lp*Lp
               - (mpf(1)/t + mpf(1)/(t-1) + mpf(1)/(L-t))*Lp
               + kf*(A + B*t/(L*L) + C*(t-1)/((L-1)*(L-1)) + D*t*(t-1)/((L-t)*(L-t))))
        max_val = max(max_val, abs(Lpp - rhs))
    return (A, B, C, D), max_val


# ---------------- main runner ----------------
def run_session_b(spec, out_json_path, ql01_best=mpf("0.0083960"), depth=1500):
    """
    spec keys:
      family, recurrence (dict of an,bn human strings), Delta, CM_field,
      class_number_disc (int), Heegner (bool),
      heun_roots (str), L0_baseline (str),
      a_fn(n,t),
      b_fns: {"A": fn, "B": fn},
      deformations: {"A": str, "B": str},
      pslq_status (str)
    """
    family = spec["family"]
    PRIOR_L0 = mpf(spec["L0_baseline"])
    a_fn = spec["a_fn"]
    b_fns = spec["b_fns"]

    print("=" * 78)
    print(f"{family} Stokes/Painleve probe -- {spec.get('CM_field', '?')} "
          f"({'Heegner' if spec.get('Heegner') else 'non-Heegner'})")
    print("=" * 78)
    print(f"Base: a_n = {spec['recurrence']['a_n']},  b_n = {spec['recurrence']['b_n']},  "
          f"Delta = {spec['Delta']}")
    print(f"CM field: {spec['CM_field']},  h(disc) = {spec['class_number_disc']}  "
          f"({'Heegner' if spec['Heegner'] else 'non-Heegner'})")
    print(f"Roots of b: {spec['heun_roots']}")
    print(f"Prior L(0) = {PRIOR_L0}  (baseline)")
    print()

    print("=" * 78)
    print(f"Step 2 -- L(t) at 11 deformation points for D-{family}-A and D-{family}-B")
    print("=" * 78)
    deform_data = {}
    for D in ["A", "B"]:
        bn_fn = b_fns[D]
        print(f"\n[D-{family}-{D}]")
        L_at = {}
        for t in T_VALUES:
            L, stab = compute_limit_at(a_fn, bn_fn, t, depth, 250)
            if L is None:
                print(f"  t={mp.nstr(t, 4):>5}  DIVERGED (zero denominator)")
                continue
            L_at[tk(t)] = L
            print(f"  t={mp.nstr(t, 4):>5}  L={mp.nstr(L, 25):<28}  stab={stab:.0f}")
        if tk(mpf(0)) in L_at:
            diff = abs(L_at[tk(mpf(0))] - PRIOR_L0)
            tol_exp = -(len(spec["L0_baseline"].split('.')[-1]) - 3)  # match baseline precision
            ok = "OK" if diff < mpf(10) ** tol_exp else "DRIFT"
            print(f"  L(0) vs prior: diff={mp.nstr(diff, 4)} [{ok}]")
        deform_data[D] = L_at

    print()
    print("=" * 78)
    print("Step 5 -- 2 x 3 residual matrix (deformation x Painleve type)")
    print("=" * 78)
    mp.dps = 200
    matrix_results = {}
    all_t_grid = [mpf("-0.3"), mpf("-0.2"), mpf("-0.1"),
                  mpf("0.1"),  mpf("0.2"),  mpf("0.3")]
    fit_idx = [1, 2, 3, 4]
    all_idx = [0, 1, 2, 3, 4, 5]
    stencil_check = {}

    for D in ["A", "B"]:
        deriv, _ = make_derivs(deform_data[D])
        sd_max = mpf(0)
        for _, val in deriv.items():
            _, _, _, sdp, sdpp = val
            if sdpp is not None:
                sd_max = max(sd_max, sdpp)
        stencil_check[D] = sd_max
        print(f"\n[D-{family}-{D}]  5pt-vs-7pt L'' max diff = {mp.nstr(sd_max, 4)}")
        res = {}
        for name, fit in [("P-III", fit_PIII), ("P-V", fit_PV), ("P-VI", fit_PVI)]:
            try:
                params, max_val = fit(deriv, fit_idx, all_idx, all_t_grid)
                res[name] = (params, max_val)
                verdict = ("HIT" if max_val < mpf(10) ** (-50)
                           else "AMBIG" if max_val < mpf(10) ** (-20)
                           else "FAIL")
                print(f"  {name}: validation max residual = {mp.nstr(max_val, 6):<14} [{verdict}]")
                print(f"        params = ({mp.nstr(params[0], 8)}, {mp.nstr(params[1], 8)},")
                print(f"                  {mp.nstr(params[2], 8)}, {mp.nstr(params[3], 8)})")
            except Exception as ex:
                res[name] = (None, None)
                print(f"  {name}: FAILED  ({ex})")
        matrix_results[D] = res

    print()
    print("=" * 78)
    print("RESIDUAL MATRIX (max validation residual, 4-fit/2-validate, 6-pt overdetermined)")
    print("=" * 78)
    print(f"{'':>14}  {'P-III':>14}  {'P-V':>14}  {'P-VI':>14}")
    for D in ["A", "B"]:
        row = matrix_results[D]
        cells = []
        for k in ["P-III", "P-V", "P-VI"]:
            _, mv = row[k]
            cells.append(mp.nstr(mv, 5) if mv is not None else "fail")
        lab = f"D-{family}-{D}"
        print(f"  {lab:<12}  {cells[0]:>14}  {cells[1]:>14}  {cells[2]:>14}")

    best_res = mpf("1e100"); best_key = None
    for D in ["A", "B"]:
        for k in ["P-III", "P-V", "P-VI"]:
            _, mv = matrix_results[D][k]
            if mv is not None and mv < best_res:
                best_res = mv; best_key = (D, k)
    print()
    print(f"BEST cell: D-{family}-{best_key[0]} + {best_key[1]}, residual {mp.nstr(best_res, 6)}")
    print(f"QL01 best (A2): {mp.nstr(ql01_best, 4)} (D2+P-III)")
    if best_res < ql01_best:
        print(f"  -> {family} best {float(ql01_best/best_res):.2g}x BETTER than QL01")
    else:
        print(f"  -> {family} best {float(best_res/ql01_best):.2g}x WORSE than QL01")

    # ---------------- structural diagnostics ----------------
    print()
    print("=" * 78)
    print("Steps 3-4 -- Stokes / connection / derivative diagnostics")
    print("=" * 78)
    mp.dps = 200
    diagnostics = {}
    for D in ["A", "B"]:
        L_at = deform_data[D]
        L0 = L_at[tk(mpf(0))]
        S_table = {}
        for tval in ["0.1", "0.2", "0.3"]:
            for sign in ["+", "-"]:
                tk_lab = f"{sign}{tval}"
                tt = mpf(("-" if sign == "-" else "") + tval)
                d = abs(L_at[tk(tt)] - L0)
                S = log(d) / log(abs(tt)) if d > 0 else mpf("inf")
                S_table[tk_lab] = S
        h = mpf("0.1")
        Lp0 = (-L_at[tk(2*h)] + 8*L_at[tk(h)] - 8*L_at[tk(-h)] + L_at[tk(-2*h)]) / (12*h)
        Lpp0 = (-L_at[tk(2*h)] + 16*L_at[tk(h)] - 30*L0 + 16*L_at[tk(-h)] - L_at[tk(-2*h)]) / (12*h*h)
        Lppp0 = (L_at[tk(2*h)] - 2*L_at[tk(h)] + 2*L_at[tk(-h)] - L_at[tk(-2*h)]) / (2*h**3)
        Lpppp0 = (L_at[tk(2*h)] - 4*L_at[tk(h)] + 6*L0 - 4*L_at[tk(-h)] + L_at[tk(-2*h)]) / (h**4)
        sigma1 = (L_at[tk(mpf("0.1"))] - L_at[tk(mpf("-0.1"))]) / (2*mpf("0.1")*Lp0)
        sigma2 = (L_at[tk(mpf("0.2"))] - L_at[tk(mpf("-0.2"))]) / (2*mpf("0.2")*Lp0)
        sigma3 = (L_at[tk(mpf("0.3"))] - L_at[tk(mpf("-0.3"))]) / (2*mpf("0.3")*Lp0)
        diagnostics[D] = {
            "S": {k: mp.nstr(v, 8) for k, v in S_table.items()},
            "sigma_t=0.1": mp.nstr(sigma1, 12),
            "sigma_t=0.2": mp.nstr(sigma2, 12),
            "sigma_t=0.3": mp.nstr(sigma3, 12),
            "Lp(0)":  mp.nstr(Lp0, 10),
            "Lpp(0)": mp.nstr(Lpp0, 10),
            "Lppp(0)": mp.nstr(Lppp0, 10),
            "Lpppp(0)": mp.nstr(Lpppp0, 10),
        }
        print(f"\n[D-{family}-{D}]")
        print(f"  Stokes proxy S(t)=log|L(t)-L(0)|/log|t|:")
        for k in ["+0.1", "-0.1", "+0.2", "-0.2", "+0.3", "-0.3"]:
            S = S_table[k]
            flag = " <-- S<1" if S < 1 else ""
            print(f"    S({k}) = {mp.nstr(S, 10)}{flag}")
        print(f"  Connection-coeff proxy sigma(t)=(L(t)-L(-t))/(2t*L'(0)):")
        print(f"    sigma(0.1) = {mp.nstr(sigma1, 12)}")
        print(f"    sigma(0.2) = {mp.nstr(sigma2, 12)}")
        print(f"    sigma(0.3) = {mp.nstr(sigma3, 12)}")
        print(f"  Derivatives at t=0:")
        print(f"    L'(0)    = {mp.nstr(Lp0, 10)}")
        print(f"    L''(0)   = {mp.nstr(Lpp0, 10)}")
        print(f"    L'''(0)  = {mp.nstr(Lppp0, 10)}")
        print(f"    L''''(0) = {mp.nstr(Lpppp0, 10)}")

    # ---------------- final per-family flag ----------------
    print()
    print("=" * 78)
    print("FINAL FLAG")
    print("=" * 78)
    S_below1 = False
    which_def = None
    s_min = mpf("inf"); s_min_str = None
    for D in ["A", "B"]:
        for k, v in diagnostics[D]["S"].items():
            sv = mpf(v)
            if sv < s_min:
                s_min = sv; s_min_str = f"D-{family}-{D} S({k})={v}"
            if sv < 1:
                S_below1 = True
                if which_def is None:
                    which_def = D

    if S_below1:
        print(f"FLAG: {family} STOKES CONFIRMED -- S<1 detected under D-{family}-{which_def}")
        flag = f"{family} STOKES CONFIRMED"
    elif s_min < mpf("1.5"):
        print(f"FLAG: {family} INCONCLUSIVE -- minimum S = {mp.nstr(s_min, 6)} ({s_min_str})")
        flag = f"{family} INCONCLUSIVE"
    else:
        print(f"FLAG: {family} STOKES ABSENT -- min S = {mp.nstr(s_min, 6)} >= 1 under both deformations")
        flag = f"{family} STOKES ABSENT"

    out = {
        "family": family,
        "recurrence": spec["recurrence"],
        "Delta": spec["Delta"],
        "CM_field": spec["CM_field"],
        "class_number_disc": spec["class_number_disc"],
        "Heegner": spec["Heegner"],
        "heun_roots": spec["heun_roots"],
        "L0_baseline": str(PRIOR_L0),
        "deformations": spec["deformations"],
        "stencil_check_5vs7_max": {D: mp.nstr(stencil_check[D], 4) for D in stencil_check},
        "residual_matrix": {
            D: {k: (mp.nstr(matrix_results[D][k][1], 6) if matrix_results[D][k][1] is not None else None)
                for k in ["P-III", "P-V", "P-VI"]}
            for D in ["A", "B"]
        },
        "best_cell": {"deformation": f"D-{family}-{best_key[0]}", "type": best_key[1],
                      "residual": mp.nstr(best_res, 6)},
        "ql01_best_for_comparison": mp.nstr(ql01_best, 6),
        "diagnostics": diagnostics,
        "S_min": mp.nstr(s_min, 10),
        "S_min_locus": s_min_str,
        "S_below_1": S_below1,
        "pslq_status": spec["pslq_status"],
        "final_flag": flag,
    }
    with open(out_json_path, "w") as f:
        json.dump(out, f, indent=2)
    print()
    print(f"Wrote {out_json_path}")
    return out


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()
