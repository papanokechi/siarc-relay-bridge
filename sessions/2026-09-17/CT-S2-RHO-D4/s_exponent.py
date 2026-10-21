"""CT-S2-RHO-D4 : growth exponent s for Q_n = b(n)Q_{n-1} + Q_{n-2}.

Tests  Q_n / Gamma(dn+1) ~ K (beta_d/d^d)^n n^s ,  s = beta_{d-1}/beta_d + (d-1)/2.

Pre-registered in PREREG.md.  Estimator, ladder, precision and the 1e-6
falsifier threshold are all fixed there and are NOT tuned here.
"""
import json
import sys
import time

from mpmath import mp, mpf, loggamma, log, nstr
import sympy as sp

DPS = 80
N_MAX = 20000
LADDER = [1250, 2500, 5000, 10000, 20000]
FALSIFIER = mpf("1e-6")

mp.dps = DPS


def b_value(beta, n):
    """beta[k] is the coefficient of n^k.  Horner, exact in mpf."""
    acc = mpf(0)
    for k in range(len(beta) - 1, -1, -1):
        acc = acc * n + beta[k]
    return acc


def root_precheck(beta):
    """b(k) != 0 for integer k >= 1, and no root of b is a positive integer."""
    n = sp.Symbol("n")
    poly = sum(sp.Integer(int(c)) * n**k for k, c in enumerate(beta))
    roots = sp.Poly(poly, n).all_roots()
    bad = [str(r) for r in roots if r.is_real and r.is_integer and r > 0]
    return {
        "roots": [str(r) for r in roots],
        "positive_integer_roots": bad,
        "ok": len(bad) == 0,
    }


def log_abs_Q(beta, N):
    """Cumulative log|Q_n| for n = 0..N, with per-step rescaling.

    Returns (L, zero_hits, sign_changes_in_b).
    """
    d = len(beta) - 1
    prev, cur = mpf(0), mpf(1)          # Q_{-1}, Q_0
    scale = mpf(0)
    L = [mpf(0)] * (N + 1)              # L[0] = log|Q_0| = 0
    zero_hits = []
    b_signs = []
    for n in range(1, N + 1):
        bn = b_value(beta, mpf(n))
        if bn == 0:
            zero_hits.append(n)
        b_signs.append(1 if bn > 0 else (-1 if bn < 0 else 0))
        prev, cur = cur, bn * cur + prev
        m = abs(cur)
        if m == 0:
            zero_hits.append(("Q", n))
            L[n] = mpf("-inf")
            continue
        prev /= m
        cur /= m
        scale += log(m)
        L[n] = scale
    sign_changes = sum(
        1 for i in range(1, len(b_signs)) if b_signs[i] * b_signs[i - 1] < 0
    )
    return L, zero_hits, sign_changes


def richardson(vals):
    """Ratio-2 Richardson for an expansion in 1/n.  Returns all levels."""
    levels = [list(vals)]
    cur = list(vals)
    j = 1
    while len(cur) > 1:
        nxt = []
        f = mpf(2) ** j
        for i in range(len(cur) - 1):
            nxt.append((f * cur[i + 1] - cur[i]) / (f - 1))
        levels.append(nxt)
        cur = nxt
        j += 1
    return levels


def s_measure(beta, N=N_MAX, ladder=None):
    ladder = ladder or LADDER
    d = len(beta) - 1
    L, zero_hits, sign_changes = log_abs_Q(beta, N)
    A = log(mpf(d) ** d / beta[d])

    def logc(n):
        return L[n] - loggamma(d * mpf(n) + 1) + n * A

    t = [(logc(n) - logc(n // 2)) / log(mpf(2)) for n in ladder]
    levels = richardson(t)
    deepest = levels[-1][0]
    drift = abs(levels[-2][0] - deepest) if len(levels) >= 2 else None
    s_pred = mpf(beta[d - 1]) / mpf(beta[d]) + mpf(d - 1) / 2
    return {
        "s_measured": deepest,
        "s_predicted": s_pred,
        "residual": abs(deepest - s_pred),
        "richardson_drift": drift,
        "levels": [[nstr(v, 25) for v in lv] for lv in levels],
        "zero_hits": zero_hits,
        "b_sign_changes": sign_changes,
    }


def r_infinity(beta, N=N_MAX):
    """r_n = Q_n / prod_{k<=n} b(k);  r_n = r_{n-1} + r_{n-2}/(b(n-1)b(n))."""
    r_prev, r_cur = mpf(1), mpf(1)      # r_0, r_1
    bs = {k: b_value(beta, mpf(k)) for k in (1,)}

    def bval(k):
        if k not in bs:
            bs[k] = b_value(beta, mpf(k))
        return bs[k]

    half = None
    for n in range(2, N + 1):
        r_prev, r_cur = r_cur, r_cur + r_prev / (bval(n - 1) * bval(n))
        if n == N // 2:
            half = r_cur
    return r_cur, half


def analyse(label, beta, N=N_MAX, ladder=None, with_rinf=True):
    t0 = time.time()
    pre = root_precheck(beta)
    out = {"label": label, "beta_low_to_high": [int(x) for x in beta],
           "precheck": pre}
    if not pre["ok"]:
        out["halt"] = "positive integer root of b; Gamma(1-r_i) singular"
        return out
    res = s_measure(beta, N=N, ladder=ladder)
    out["s_measured"] = nstr(res["s_measured"], 25)
    out["s_predicted"] = nstr(res["s_predicted"], 25)
    out["residual"] = nstr(res["residual"], 6)
    out["residual_float"] = float(res["residual"])
    out["richardson_drift"] = nstr(res["richardson_drift"], 6)
    out["richardson_levels"] = res["levels"]
    out["b_sign_changes"] = res["b_sign_changes"]
    out["zero_hits"] = [str(z) for z in res["zero_hits"]]
    if with_rinf:
        r_N, r_half = r_infinity(beta, N=N)
        out["r_inf"] = nstr(r_N, 30)
        out["r_inf_at_half_N"] = nstr(r_half, 30)
        out["r_inf_halfN_vs_N_agreement_digits"] = (
            float(-log(abs((r_N - r_half) / r_N), 10)) if r_N != 0 and r_N != r_half
            else None
        )
        out["r_inf_nonzero"] = bool(abs(r_N) > mpf("1e-40"))
    out["elapsed_s"] = round(time.time() - t0, 1)
    out["falsifier_fired"] = bool(
        out.get("r_inf_nonzero", True) and res["residual"] > FALSIFIER
    )
    return out


REPRESENTATIVES = [
    # label, [a4,a3,a2,a1,a0] from newton_d4_results.json -> reversed to low->high
    ("mixed_S_4_smallD", [1, -3, -3, 1, 1]),
    ("mixed_S_4_largeD", [1, -3, -3, -3, 3]),
    ("mixed_D_4", [1, -3, -3, -3, 1]),
    ("+_real_D_4", [1, -3, -3, 3, 1]),
    ("anchor_x4_minus_2_D_4", [1, 0, 0, 0, -2]),
    ("anchor_x4_plus_1_V_4", [1, 0, 0, 0, 1]),
    ("anchor_x4_minus_x_minus_1", [1, 0, 0, -1, -1]),
    ("alpha4_eq_7_synthetic", [7, 0, 0, 1, 0]),
]


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    results = {"dps": DPS, "N_max": N_MAX, "ladder": LADDER,
               "falsifier": "1e-6", "generated": time.strftime("%Y-%m-%dT%H:%M:%S")}

    if which in ("all", "reps"):
        rows = []
        for label, coeffs in REPRESENTATIVES:
            beta = list(reversed(coeffs))          # low -> high
            row = analyse(label, beta)
            rows.append(row)
            print(f"{label:28s} s={row.get('s_measured','-'):<28s} "
                  f"res={row.get('residual','-'):<12s} "
                  f"r_inf={row.get('r_inf','-')[:14]:<14s} "
                  f"F1={row.get('falsifier_fired')}", flush=True)
        results["representatives"] = rows
        with open("s_table.json", "w") as f:
            json.dump(results, f, indent=2)

    if which in ("all", "vacuity"):
        NV, LV = 8000, [500, 1000, 2000, 4000, 8000]
        arm_i, arm_ii = [], []
        for b2 in (-3, 0, 1, 5):
            for b1 in (-3, 1):
                for b0 in (-3, 1):
                    beta = [b0, b1, b2, -3, 1]
                    r = analyse(f"i_b2{b2}_b1{b1}_b0{b0}", beta, N=NV,
                                ladder=LV, with_rinf=False)
                    arm_i.append(r)
                    print("  (i)", r["label"], r.get("s_measured"), flush=True)
        for b3 in (-4, -3, -2, -1, 0, 1, 2, 3, 4):
            beta = [1, 1, -3, b3, 1]
            r = analyse(f"ii_b4_1_b3{b3}", beta, N=NV, ladder=LV,
                        with_rinf=False)
            arm_ii.append(r)
            print("  (ii)", r["label"], r.get("s_measured"), flush=True)
        for b3 in (0, 1, 7, 14):
            beta = [1, 1, -3, b3, 7]
            r = analyse(f"ii_b4_7_b3{b3}", beta, N=NV, ladder=LV,
                        with_rinf=False)
            arm_ii.append(r)
            print("  (ii)", r["label"], r.get("s_measured"), flush=True)

        sp_i = [x["residual_float"] for x in arm_i if "residual_float" in x]
        vals_i = [mpf(x["s_measured"]) for x in arm_i if "s_measured" in x]
        spread_i = float(max(vals_i) - min(vals_i)) if vals_i else None
        worst_ii = max((x["residual_float"] for x in arm_ii
                        if "residual_float" in x), default=None)
        vac = {
            "N": NV, "ladder": LV,
            "arm_i_insensitivity": arm_i,
            "arm_ii_sensitivity": arm_ii,
            "arm_i_s_spread": spread_i,
            "arm_i_max_residual": max(sp_i) if sp_i else None,
            "arm_i_PASS": bool(spread_i is not None and spread_i <= 1e-6),
            "arm_ii_max_residual": worst_ii,
            "arm_ii_PASS": bool(worst_ii is not None and worst_ii <= 1e-6),
        }
        with open("vacuity.json", "w") as f:
            json.dump(vac, f, indent=2)
        print("arm(i) spread", spread_i, "PASS", vac["arm_i_PASS"])
        print("arm(ii) max residual", worst_ii, "PASS", vac["arm_ii_PASS"])


if __name__ == "__main__":
    main()
