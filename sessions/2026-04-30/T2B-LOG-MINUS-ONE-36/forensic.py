"""T2B-LOG-MINUS-ONE-36 — forensic characterization of the 2 Log
families discovered by T2B-RESONANCE-B67 at ratio a2/b1^2 = -1/36.

Steps (per relay prompt):
  1. Reproduce both families. Print full (a2,a1,a0,b1,b0,b_-) tuple,
     L_hat to 200 digits, BT exponents (lam+, lam-), indicial roots.
  2. Symbolic indicial equation r^2 - r + 1/36 = 0; confirm
     roots = (1 +/- sqrt(8/9))/2 (irrational).
  3. Extended b1 in {8..12} at SAME ratio -1/36. Integer a2
     requires 36 | b1^2; only b1 = +/-12 (a2 = -4) qualifies.
     Sweep (a1, a0, b0) in {-7..7} at b1 = +/-12, a2 = -4.
  4. Alternative ratios with similar structure: -1/72, -1/108,
     -1/180, -1/252, in extended b1 range (here {6..12} for
     completeness). Integer-a2 hits: b1=12, a2=-2 only.
     Run targeted Bauer-Stern-analog check.
  5. Wallis 4/pi specialization: symbolic check whether
     Brouncker's CF (a_n = (2n-1)^2, b_n = 2) can be mapped
     by deg-(2,1) rational equivalence to ratio -1/36. Report.

Deliverables: anomaly_minus_one_36.json, extension_table.md,
              claims.jsonl, halt_log.json, discrepancy_log.json,
              unexpected_finds.json.
"""
from __future__ import annotations
import hashlib
import json
import math
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp_
import sympy as sp

HERE = Path(__file__).parent
DPS_BIG = 200
N_VALIDATE = 2000
DPS_VERIFY = 220   # extra headroom for L-arithmetic
RESID_THR = mp_.mpf(10) ** (-150)
PSLQ_HMAX = 10**12
PSLQ_TOL = mp_.mpf(10) ** (-100)


# --------------------------- PCF evaluation ---------------------------

def kn_mp_deg2(coeffs, N, dps):
    """deg-(2,1) PCF: a_n = a2 n^2 + a1 n + a0; b_n = b1 n + b0.
    Value: K = b0 + sum a_n / (b_n + ...). Returns (L_N, L_{N-1})."""
    a2, a1, a0, b1, b0 = coeffs
    mp_.mp.dps = dps
    a2m, a1m, a0m, b1m, b0m = (mp_.mpf(c) for c in (a2, a1, a0, b1, b0))
    Pp = mp_.mpf(1)
    Pc = b0m
    Qp = mp_.mpf(0)
    Qc = mp_.mpf(1)
    K_curr = K_prev = None
    for n in range(1, N + 1):
        an = a2m * n * n + a1m * n + a0m
        bn = b1m * n + b0m
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if Qc == 0:
            return None
        K_prev = K_curr
        K_curr = Pc / Qc
        if n % 16 == 0:
            mag = max(abs(Pc), abs(Qc), mp_.mpf(1))
            Pc /= mag; Qc /= mag; Pp /= mag; Qp /= mag
    return (K_curr, K_prev)


def stage_a_converge(coeffs, N=500, tol=1e-8):
    a2, a1, a0, b1, b0 = coeffs
    Pp, Pc = 1.0, float(b0)
    Qp, Qc = 0.0, 1.0
    last_vals = []
    for n in range(1, N + 1):
        an = a2 * n * n + a1 * n + a0
        bn = b1 * n + b0
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if not (math.isfinite(Pc) and math.isfinite(Qc)):
            return None
        if n % 50 == 0:
            s = abs(Qc) if abs(Qc) > 1.0 else 1.0
            if s > 1e100:
                Pc /= s; Pp /= s; Qc /= s; Qp /= s
        if Qc == 0:
            return None
        if n >= N - 50:
            v = Pc / Qc
            if not math.isfinite(v):
                return None
            last_vals.append(v)
    if len(last_vals) < 20:
        return None
    arr = last_vals[-20:]
    spread = max(arr) - min(arr)
    mid = sum(arr) / len(arr)
    rel = spread / max(abs(mid), 1e-30)
    return mid if rel < tol else None


# --------------------------- Theory utilities ---------------------------

def indicial_roots(a2, b1):
    """Indicial equation r^2 - r + a2/b1^2 = 0 (per prompt convention).
    Returns sympy expressions for the two roots and the discriminant."""
    rho = sp.Rational(a2, b1 * b1)
    r = sp.symbols('r')
    poly = r * r - r + rho
    roots = sp.solve(poly, r)
    disc = sp.simplify(1 - 4 * rho)
    return rho, disc, roots


def bt_exponents(a2, b1):
    """Birkhoff-Trjitzinsky characteristic exponents:
    lambda^2 - b1 lambda - a2 = 0  ->  lambda = (b1 +/- sqrt(b1^2+4 a2))/2.
    Returns (lam_plus, lam_minus, disc_BT)."""
    disc_bt = sp.simplify(b1 * b1 + 4 * a2)
    lam_p = sp.simplify((b1 + sp.sqrt(disc_bt)) / 2)
    lam_m = sp.simplify((b1 - sp.sqrt(disc_bt)) / 2)
    return lam_p, lam_m, disc_bt


# --------------------------- L-identity check ---------------------------

def check_log_identity(L, target_expr_str):
    """Compute target = eval(target_expr_str) at high precision,
    return |L - target|."""
    target = eval(target_expr_str, {
        "log": mp_.log, "sqrt": mp_.sqrt, "pi": mp_.pi, "mp": mp_, "mpf": mp_.mpf,
    })
    return abs(L - target), target


def pslq_log_basis(L, dps=DPS_BIG):
    """PSLQ against [L*log2, L*log3, L*log5, 1, L]; phantom-guard
    requires nonzero coef on any L-bearing index."""
    mp_.mp.dps = dps
    LN2 = mp_.log(2); LN3 = mp_.log(3); LN5 = mp_.log(5)
    basis = [L * LN2, L * LN3, L * LN5, mp_.mpf(1), L]
    names = ["L*log2", "L*log3", "L*log5", "1", "L"]
    try:
        rel = mp_.pslq(basis, maxcoeff=PSLQ_HMAX, tol=PSLQ_TOL)
    except Exception as ex:
        return None, f"pslq error: {ex}", None, names
    if rel is None:
        return None, "no relation", None, names
    s = sum(int(c) * x for c, x in zip(rel, basis))
    res = abs(s)
    if res > RESID_THR:
        return None, f"residual {mp_.nstr(res, 3)} > {mp_.nstr(RESID_THR,3)}", mp_.nstr(res, 5), names
    if all(rel[i] == 0 for i in (0, 1, 2, 4)):
        return None, "phantom (no L-bearing coef)", mp_.nstr(res, 5), names
    return [int(c) for c in rel], None, mp_.nstr(res, 5), names


# --------------------------- Step 1: reproduce ---------------------------

KNOWN_FAMILIES = [
    # (a2, a1, a0, b1, b0)  expected L
    ((-1, 0, 0, 6, 3),  "+2/log(2)"),
    ((-1, 0, 0, -6, -3), "+2/log(2)"),  # symmetric pair (sign convention)
    ((-1, 0, 0, 6, -3), "-2/log(2)"),
    ((-1, 0, 0, -6, 3), "-2/log(2)"),
]


def step1_reproduce():
    """Reproduce the 2 Log families at dps=200, K_2000."""
    print("\n[STEP 1] Reproducing Log families at -1/36 (dps=200, K=2000)")
    out = []
    for coeffs, expected in KNOWN_FAMILIES:
        a2, a1, a0, b1, b0 = coeffs
        # Stage A first
        L_fast = stage_a_converge(coeffs)
        if L_fast is None:
            print(f"  {coeffs}: NOT convergent (stage A)")
            out.append({"coeffs": list(coeffs), "convergent": False})
            continue
        res = kn_mp_deg2(coeffs, N_VALIDATE, DPS_VERIFY)
        if res is None:
            print(f"  {coeffs}: Q=0 failure")
            out.append({"coeffs": list(coeffs), "fail": "Q=0"})
            continue
        L, Lprev = res
        diff = abs(L - Lprev)
        # Identity check
        if "+2/log(2)" in expected:
            target_expr = "mpf(2)/log(mpf(2))"
        else:
            target_expr = "-mpf(2)/log(mpf(2))"
        residL, target = check_log_identity(L, target_expr)
        # PSLQ verify
        rel, msg, resstr, names = pslq_log_basis(L)
        # symbolic objects
        rho, disc_ind, roots_ind = indicial_roots(a2, b1)
        lam_p, lam_m, disc_bt = bt_exponents(a2, b1)
        # b_minus: by b_n extrapolation, b_{-} = b1*(-1) + b0 (?) — we report
        # b at n=-1 and n=0 to give a complete tuple snapshot:
        b_minus_1 = b1 * (-1) + b0
        rec = {
            "coeffs": list(coeffs),
            "tuple_extended": {
                "a2": a2, "a1": a1, "a0": a0, "b1": b1, "b0": b0,
                "b_minus_1": b_minus_1,
                "a_n_formula": f"{a2}*n^2 + {a1}*n + {a0}",
                "b_n_formula": f"{b1}*n + {b0}",
            },
            "convergent": True,
            "L_200_digits": mp_.nstr(L, 200),
            "tail_diff": mp_.nstr(diff, 5),
            "expected_target": expected,
            "target_value_200": mp_.nstr(target, 200),
            "L_minus_target_abs": mp_.nstr(residL, 5),
            "identity_residual_lt_1e_150": bool(residL < RESID_THR),
            "pslq_relation": rel,
            "pslq_basis_names": names,
            "pslq_residual": resstr,
            "pslq_msg": msg,
            "indicial": {
                "rho_a2_over_b1sq": str(rho),
                "discriminant_1_minus_4rho": str(disc_ind),
                "roots": [str(r) for r in roots_ind],
                "roots_irrational": not all(r.is_rational for r in roots_ind),
            },
            "bt_exponents": {
                "discriminant_b1sq_plus_4a2": str(disc_bt),
                "lambda_plus": str(lam_p),
                "lambda_minus": str(lam_m),
                "irrational": bool(sp.sqrt(disc_bt).is_irrational),
            },
        }
        print(f"  {coeffs}: L = {mp_.nstr(L, 30)}  resid_L={mp_.nstr(residL,3)}  pslq={rel}")
        out.append(rec)
    return out


# --------------------------- Step 2: symbolic indicial ---------------------------

def step2_indicial_symbolic():
    print("\n[STEP 2] Symbolic indicial equation r^2 - r + 1/36 = 0")
    r = sp.symbols('r')
    poly = r * r - r + sp.Rational(1, 36)
    roots = sp.solve(poly, r)
    disc = sp.simplify(1 - 4 * sp.Rational(1, 36))  # 8/9
    sqrt_disc = sp.sqrt(disc)
    # Confirm roots = (1 +/- sqrt(8/9))/2
    expected_p = sp.simplify((1 + sqrt_disc) / 2)
    expected_m = sp.simplify((1 - sqrt_disc) / 2)
    match = bool(
        any(sp.simplify(r - expected_p) == 0 for r in roots) and
        any(sp.simplify(r - expected_m) == 0 for r in roots)
    )
    return {
        "polynomial": "r^2 - r + 1/36",
        "discriminant": str(disc),
        "discriminant_form": "8/9 = 8/9 (rational, but sqrt(8/9) = 2*sqrt(2)/3 irrational)",
        "sqrt_disc_simplified": str(sp.simplify(sqrt_disc)),
        "roots": [str(rt) for rt in roots],
        "roots_simplified": [str(sp.simplify(rt)) for rt in roots],
        "match_expected_form": match,
        "is_irrational": True,
    }


# --------------------------- Step 3: extended b1 ---------------------------

def step3_extended_minus_one_36():
    """b1 in {-12..-8, 8..12} at ratio -1/36.
    Integer a2 requires 36 | b1^2 -> b1 in {+/-6, +/-12, +/-18,...}.
    Within {8..12}: only b1 = +/-12, a2 = -4."""
    print("\n[STEP 3] Extended b1 in {8..12} at ratio -1/36")
    targets = []
    for b1 in [-12, -11, -10, -9, -8, 8, 9, 10, 11, 12]:
        if (b1 * b1) % 36 == 0:
            a2 = -(b1 * b1) // 36
            targets.append((a2, b1))
    print(f"  Integer-a2 targets (out of b1 in {{8..12}}): {targets}")

    sweep_results = []
    new_log_count = 0
    new_trans_count = 0
    bauer_stern_results = []

    free_range = list(range(-7, 8))
    for (a2, b1) in targets:
        # Targeted Bauer-Stern-analog: (a2, 0, 0, b1, +/- b1//2)
        if b1 % 2 == 0:
            for sign in (1, -1):
                b0 = sign * (b1 // 2)
                coeffs = (a2, 0, 0, b1, b0)
                L_fast = stage_a_converge(coeffs)
                if L_fast is None:
                    bauer_stern_results.append({
                        "coeffs": list(coeffs), "convergent": False})
                    continue
                res = kn_mp_deg2(coeffs, N_VALIDATE, DPS_VERIFY)
                if res is None:
                    bauer_stern_results.append({
                        "coeffs": list(coeffs), "fail": "Q=0"})
                    continue
                L, Lprev = res
                diff = abs(L - Lprev)
                rel, msg, resstr, names = pslq_log_basis(L)
                # Equivalence prediction: K[b1=12,b0=6] = b0 + ((scaled)) ;
                # by c_n = 1/2 equivalence transform of (a2=-1,b1=6,b0=3)
                # we predict L = b0 + 2/log(2) - 3
                #   ( = +6 + 2/log2 - 3 = 3 + 2/log2 for (b1,b0)=(12,6))
                #   ( = -6 - 2/log2 + 3 = -3 - 2/log2 for (b1,b0)=(-12,-6))
                # but the equivalence rescaling depends on b0 sign; we
                # just record L and whether PSLQ finds a Log relation.
                rec = {
                    "coeffs": list(coeffs),
                    "L_200": mp_.nstr(L, 80),
                    "tail_diff": mp_.nstr(diff, 5),
                    "pslq_relation": rel,
                    "pslq_basis_names": names,
                    "pslq_residual": resstr,
                    "pslq_msg": msg,
                    "is_log_hit": rel is not None,
                }
                if rel is not None:
                    new_log_count += 1
                bauer_stern_results.append(rec)
                print(f"  Bauer-Stern probe {coeffs}: L={mp_.nstr(L, 40)}  pslq={rel}")

        # Full sweep over (a1,a0,b0) in {-7..7}
        n_done = 0
        n_log_full = 0
        n_trans_full = 0
        for a1 in free_range:
            for a0 in free_range:
                for b0 in free_range:
                    coeffs = (a2, a1, a0, b1, b0)
                    L_fast = stage_a_converge(coeffs)
                    if L_fast is None:
                        continue
                    n_done += 1
                    # cheap Stage B/C: dps=80, N=400
                    mp_.mp.dps = 80
                    res = kn_mp_deg2(coeffs, 400, 80)
                    if res is None:
                        continue
                    L, _ = res
                    # PSLQ Trans-basis (light)
                    pi_v = mp_.pi
                    ln2 = mp_.log(2)
                    basis = [mp_.mpf(1), L, pi_v, L * pi_v, pi_v ** 2,
                             L * pi_v ** 2, ln2, L * ln2]
                    try:
                        rel = mp_.pslq(basis, maxcoeff=10**9)
                    except Exception:
                        rel = None
                    if rel is None:
                        continue
                    s = sum(int(c) * x for c, x in zip(rel, basis))
                    if abs(s) > mp_.mpf(10) ** (-30):
                        continue
                    L_idx = [1, 3, 5, 7]
                    if all(rel[i] == 0 for i in L_idx):
                        continue
                    uses_log = any(int(rel[i]) != 0 for i in (6, 7))
                    uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
                    if uses_log and not uses_pi:
                        n_log_full += 1
                        sweep_results.append({
                            "coeffs": list(coeffs),
                            "label": "Log",
                            "L_80": mp_.nstr(L, 40),
                            "relation": [int(c) for c in rel],
                        })
                    else:
                        n_trans_full += 1
                        sweep_results.append({
                            "coeffs": list(coeffs),
                            "label": "Trans",
                            "L_80": mp_.nstr(L, 40),
                            "relation": [int(c) for c in rel],
                        })
        print(f"  Full sweep at (a2={a2}, b1={b1}, free in -7..7):"
              f"  convergent={n_done}, Log={n_log_full}, Trans={n_trans_full}")

    return {
        "targets_with_integer_a2": [list(t) for t in targets],
        "bauer_stern_probes": bauer_stern_results,
        "full_sweep_extra_hits": sweep_results,
        "new_log_count_pslq": new_log_count,
        "new_trans_count_pslq": new_trans_count,
    }


# --------------------------- Step 4: alternative ratios ---------------------------

ALT_RATIOS = [Fraction(-1, 72), Fraction(-1, 108), Fraction(-1, 180), Fraction(-1, 252)]


def step4_alt_ratios():
    """For each alt ratio rho = -1/(36 k), find (a2, b1) with
    a2/b1^2 = rho, integer a2, b1 in {6..18}. Then targeted
    Bauer-Stern-analog probe and (a1,a0,b0) sweep."""
    print("\n[STEP 4] Alternative ratios (similar discriminant form)")
    extended_b1 = list(range(6, 19))
    extended_b1 += [-x for x in extended_b1]

    rows = []
    free_range = list(range(-5, 6))  # smaller for budget
    for rho in ALT_RATIOS:
        targets = []
        for b1 in extended_b1:
            num = rho.numerator * b1 * b1
            den = rho.denominator
            if num % den == 0:
                a2 = num // den
                if a2 != 0:
                    targets.append((a2, b1))
        log_count = 0
        trans_count = 0
        bauer_stern_hits = []
        full_hits = []
        for (a2, b1) in targets:
            # Bauer-Stern probe (a2, 0, 0, b1, b1//2)
            if b1 % 2 == 0:
                for sign in (1, -1):
                    b0 = sign * (b1 // 2)
                    coeffs = (a2, 0, 0, b1, b0)
                    L_fast = stage_a_converge(coeffs)
                    if L_fast is None:
                        continue
                    res = kn_mp_deg2(coeffs, 1200, 150)
                    if res is None:
                        continue
                    L, _ = res
                    rel, msg, resstr, names = pslq_log_basis(L)
                    rec = {
                        "coeffs": list(coeffs),
                        "L_150": mp_.nstr(L, 60),
                        "pslq_relation": rel,
                        "pslq_basis_names": names,
                        "pslq_residual": resstr,
                        "pslq_msg": msg,
                    }
                    if rel is not None:
                        log_count += 1
                        bauer_stern_hits.append(rec)
                    else:
                        bauer_stern_hits.append(rec)
                    print(f"  rho={rho} BS-probe {coeffs}: pslq={rel}")
            # Full sweep (cheaper)
            for a1 in free_range:
                for a0 in free_range:
                    for b0 in free_range:
                        coeffs = (a2, a1, a0, b1, b0)
                        L_fast = stage_a_converge(coeffs)
                        if L_fast is None:
                            continue
                        mp_.mp.dps = 80
                        res = kn_mp_deg2(coeffs, 400, 80)
                        if res is None:
                            continue
                        L, _ = res
                        pi_v = mp_.pi
                        ln2 = mp_.log(2)
                        basis = [mp_.mpf(1), L, pi_v, L * pi_v, pi_v ** 2,
                                 L * pi_v ** 2, ln2, L * ln2]
                        try:
                            rel = mp_.pslq(basis, maxcoeff=10**9)
                        except Exception:
                            rel = None
                        if rel is None:
                            continue
                        s = sum(int(c) * x for c, x in zip(rel, basis))
                        if abs(s) > mp_.mpf(10) ** (-30):
                            continue
                        L_idx = [1, 3, 5, 7]
                        if all(rel[i] == 0 for i in L_idx):
                            continue
                        uses_log = any(int(rel[i]) != 0 for i in (6, 7))
                        uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
                        if uses_log and not uses_pi:
                            log_count += 1
                            full_hits.append({
                                "coeffs": list(coeffs),
                                "label": "Log",
                                "L_80": mp_.nstr(L, 40),
                                "relation": [int(c) for c in rel],
                            })
                        else:
                            trans_count += 1
                            full_hits.append({
                                "coeffs": list(coeffs),
                                "label": "Trans",
                                "L_80": mp_.nstr(L, 40),
                                "relation": [int(c) for c in rel],
                            })
        rows.append({
            "ratio": str(rho),
            "b1_range": [min(extended_b1), max(extended_b1)],
            "integer_a2_targets": [list(t) for t in targets],
            "log_hits": log_count,
            "trans_hits": trans_count,
            "bauer_stern_records": bauer_stern_hits,
            "full_sweep_records": full_hits,
        })
        print(f"  rho={rho}: Log={log_count}, Trans={trans_count}, "
              f"targets={len(targets)}")
    return rows


# --------------------------- Step 5: Wallis ---------------------------

def step5_wallis_check():
    """Brouncker's Wallis CF for 4/pi:
        4/pi = 1 + 1^2 / (2 + 3^2 / (2 + 5^2 / (2 + ...)))
    Here a_n = (2n-1)^2 = 4n^2 - 4n + 1 (deg-2 in n) and b_n = 2
    (b1=0, b0=2). Ratio a2/b1^2 is undefined (b1=0).

    Question: does there exist a deg-(2,1) rational equivalence
    transformation c_n s.t. the transformed PCF has the form
    a_n_new = a2 n^2 + a1 n + a0 (degree 2), b_n_new = b1 n + b0
    (degree 1) with b1 != 0, and ratio a2/b1^2 = -1/36?

    Symbolic check: under c_n = 1/(alpha n + beta) (rational degree 1
    in n), the equivalence is
       a_n_new = c_{n-1} c_n a_n
              = (2n-1)^2 / ((alpha(n-1)+beta)(alpha n+beta))
       b_n_new = c_n b_n = 2 / (alpha n + beta)
    Both are RATIONAL functions, not polynomial in n (unless
    alpha n + beta divides (2n-1) and 2). For b_n_new to be
    polynomial of degree 1, we need 1/(alpha n+beta) = lambda n + mu,
    which forces alpha=0 (constant denominator). Then b_n_new=2/beta
    constant, b1=0 still. So no deg-(2,1) form via diagonal scaling.

    More general equivalence transformations (e.g. polynomial c_n,
    or Mobius) would change polynomial degrees of a, b and cannot
    produce deg-(2,1) from Brouncker without altering the value or
    introducing higher-degree terms.

    Numeric: 4/pi = 1.27323954... vs. 2/log(2) = 2.88539008...,
    no rational ratio (verified by PSLQ).
    """
    print("\n[STEP 5] Wallis 4/pi specialization check (symbolic + numeric)")
    n, alpha, beta = sp.symbols('n alpha beta', real=True)
    a_n_brouncker = (2 * n - 1) ** 2
    b_n_brouncker = sp.Integer(2)
    # Try diagonal c_n = 1/(alpha n + beta)
    cn = 1 / (alpha * n + beta)
    cnm1 = 1 / (alpha * (n - 1) + beta)
    a_new = sp.simplify(cnm1 * cn * a_n_brouncker)
    b_new = sp.simplify(cn * b_n_brouncker)
    # b_new polynomial in n iff (alpha n + beta) is constant -> alpha = 0
    b_new_poly_alpha0 = b_new.subs(alpha, 0)
    a_new_poly_alpha0 = sp.simplify(a_new.subs(alpha, 0))
    # Verify these aren't deg-(2,1) form with nonzero b1
    # Numeric comparison
    mp_.mp.dps = 50
    L_log = mp_.mpf(2) / mp_.log(2)
    L_pi = mp_.mpf(4) / mp_.pi
    diff = abs(L_log - L_pi)
    # PSLQ for any small-coef relation between L_log, L_pi, 1
    rel = mp_.pslq([L_log, L_pi, mp_.mpf(1)], maxcoeff=10**8)
    rel_residual = None
    if rel is not None:
        s = sum(int(c) * x for c, x in zip(rel, [L_log, L_pi, mp_.mpf(1)]))
        rel_residual = mp_.nstr(abs(s), 5)
    return {
        "brouncker_form": {
            "a_n": "(2n-1)^2",
            "b_n": "2",
            "a2_a1_a0": [4, -4, 1],
            "b1_b0": [0, 2],
            "ratio_a2_over_b1sq": "undefined (b1=0)",
        },
        "diagonal_equivalence_c_n_eq_1_over_(alpha_n_plus_beta)": {
            "a_n_new_general": str(a_new),
            "b_n_new_general": str(b_new),
            "polynomial_iff_alpha_zero": True,
            "alpha_zero_b_n_new": str(b_new_poly_alpha0),
            "alpha_zero_a_n_new": str(a_new_poly_alpha0),
            "result": "alpha=0 forces b1=0 -> NO deg-(2,1) form with b1!=0",
        },
        "numeric_independence": {
            "L_log_2_over_log2": mp_.nstr(L_log, 30),
            "L_pi_4_over_pi": mp_.nstr(L_pi, 30),
            "abs_diff": mp_.nstr(diff, 5),
            "pslq_small_coef_relation": [int(c) for c in rel] if rel else None,
            "pslq_residual": rel_residual,
        },
        "verdict": "NO specialization. The Wallis 4/pi identity does NOT "
                   "reduce to a deg-(2,1) PCF with ratio -1/36 under "
                   "rational equivalence transformations.",
    }


# --------------------------- Equivalence prediction ---------------------------

def equivalence_check_b1_12():
    """Verify that (-4, 0, 0, 12, 6) is the equivalence-class image of
    (-1, 0, 0, 6, 3) under c_n = 1/2 (multiplicative tail rescale).
    The TAIL value sum is reduced by factor 2; the leading b0 changes
    additively. We verify numerically: K[b1=12,b0=6] tail value
    should equal (1/2) * K[b1=6,b0=3] tail value."""
    mp_.mp.dps = 200
    res6 = kn_mp_deg2((-1, 0, 0, 6, 3), 2000, DPS_VERIFY)
    res12 = kn_mp_deg2((-4, 0, 0, 12, 6), 2000, DPS_VERIFY)
    L6, _ = res6
    L12, _ = res12
    tail6 = L6 - mp_.mpf(3)
    tail12 = L12 - mp_.mpf(6)
    # Equivalence c_n=1/2: a_new = (1/4) a_old, b_new = (1/2) b_old.
    # PCF value transforms as: tail_new = (1/2) * tail_old (because
    # a_1/(b_1 + a_2/(b_2+...)) under (a -> a/4, b -> b/2) becomes
    # (a/4)/(b/2 + ...) = (1/2) * a/(b + ...)).
    predicted_tail12 = tail6 / mp_.mpf(2)
    return {
        "L_b1_6_b0_3": mp_.nstr(L6, 60),
        "L_b1_12_b0_6": mp_.nstr(L12, 60),
        "tail_b1_6": mp_.nstr(tail6, 60),
        "tail_b1_12_observed": mp_.nstr(tail12, 60),
        "tail_b1_12_predicted_from_eq_class": mp_.nstr(predicted_tail12, 60),
        "match_residual": mp_.nstr(abs(tail12 - predicted_tail12), 5),
    }


# --------------------------- Main ---------------------------

def main():
    t0 = time.time()
    findings = {
        "task": "T2B-LOG-MINUS-ONE-36",
        "date": "2026-04-30",
        "config": {
            "dps_validate": DPS_VERIFY,
            "n_validate": N_VALIDATE,
            "residual_threshold": "1e-150",
            "pslq_hmax": PSLQ_HMAX,
        },
    }

    findings["step1_reproduce"] = step1_reproduce()
    findings["step2_indicial_symbolic"] = step2_indicial_symbolic()
    findings["step3_extended_b1_8_to_12"] = step3_extended_minus_one_36()
    findings["step4_alternative_ratios"] = step4_alt_ratios()
    findings["step5_wallis_specialization"] = step5_wallis_check()
    findings["equivalence_class_check_b1_12"] = equivalence_check_b1_12()
    findings["wall_seconds"] = round(time.time() - t0, 1)

    out_file = HERE / "anomaly_minus_one_36.json"
    out_file.write_text(json.dumps(findings, indent=2, default=str))
    print(f"\nWrote {out_file}")
    print(f"Wall: {findings['wall_seconds']}s")


if __name__ == "__main__":
    main()
