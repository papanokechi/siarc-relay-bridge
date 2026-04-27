"""
SPRINT-W2-TRANS-INDICIAL-SURVEY -- Part A
================================================================

Indicial survey of 50 Trans families (a2/b1^2 = -2/9) and 20
non-Trans (10 Log-style + 10 Alg-style).

For each family compute:
  (a) characteristic roots mu+- of  mu^2 - b1 mu + a2 = 0
      and modulus ratio |mu+/mu-|
  (b) symbolic indicial exponent (W1 closed form)
        alpha(mu) = -((b1-b0)*mu + a1 - a2) / (b1*mu - 2*a2)
      evaluated at mu = mu+ and mu = mu-
  (c) sum  S = alpha(mu+) + alpha(mu-)
      product  P = alpha(mu+) * alpha(mu-)
      discriminant  D = (alpha(mu+) - alpha(mu-))^2 = S^2 - 4P
  (d) numerical alpha_fit from the convergent recurrence
        y_{n+1} = b_n y_n - a_n y_{n-1}
      via least-squares on  log|y_n| - log Gamma(n+1) - n log|mu_dom|
      vs log n, n in [100, 500], dps=150.

Phantom Hit Rule: Part C runs PSLQ on candidate invariants;
relations with L-coefficient = 0 are rejected.

Trans families
---------------
For a2/b1^2 = -2/9 to have integer a2, b1 we need 9 | 2*b1^2,
hence 3 | b1.  We use b1 in {3, 6, 9, 12, 15} so that a2 ranges
in {-2, -8, -18, -32, -50}.

Non-Trans families
-------------------
- Log-style:  a2/b1^2 chosen rational and != -2/9 (e.g. -1/4, -1/9,
  +1/9, -1/16) so that the characteristic discriminant b1^2-4 a2
  remains positive and the dominant CF growth mimics a Log law.
- Alg-style:  characteristic roots equal or in modulus ratio
  exactly 1 (b1^2 - 4 a2 <= 0 or a2 = 0), so the CF limit is
  algebraic.
"""

import json
import os
import mpmath
from mpmath import mp, mpf, mpc, log, sqrt, pi

mp.dps = 150

# ---------------------------------------------------------------
# Family generators
# ---------------------------------------------------------------

def make_trans_families():
    """50 integer Trans families with a2/b1^2 = -2/9."""
    fams = []
    for b1 in (3, 6, 9, 12, 15):
        a2 = -2 * (b1 // 3) ** 2          # = -2 b1^2 / 9
        # vary b0, a1, a0 over small integers
        for b0 in (-2, -1, 0, 1, 2):
            for a1 in (-2 * a2, 0, 2 * a2):   # include a1 = 2 a2 (W1 C1 locus)
                for a0 in (0, 1):
                    fams.append((a0, a1, a2, b0, b1))
                    if len(fams) >= 50:
                        return fams
    return fams[:50]

def make_log_families():
    """10 Log-style families; a2/b1^2 != -2/9."""
    return [
        # (a0, a1, a2, b0, b1) ; ratio noted in comments
        (0,  0, -1, 0, 2),    # -1/4
        (0,  1, -1, 1, 2),    # -1/4
        (0,  0, -1, 0, 3),    # -1/9
        (0,  2, -1, 1, 3),    # -1/9
        (0,  0,  1, 0, 3),    # +1/9
        (0,  3,  1, 1, 3),    # +1/9
        (0,  0, -1, 0, 4),    # -1/16
        (0,  1, -1, 1, 4),    # -1/16
        (0,  0, -2, 0, 5),    # -2/25
        (0,  4, -2, 2, 5),    # -2/25
    ]

def make_alg_families():
    """10 Alg-style families: degenerate or complex characteristic."""
    return [
        # discriminant <= 0 (complex/repeated mu) or a2 = 0
        (0,  0,  1, 0, 2),    # mu^2 - 2 mu + 1 = 0  (repeated root mu=1)
        (0,  1,  1, 1, 2),    # ditto
        (0,  0,  4, 0, 3),    # b1^2 - 4 a2 = 9 - 16 = -7 (complex)
        (0,  2,  4, 1, 3),
        (0,  0,  9, 0, 4),    # 16 - 36 = -20 (complex)
        (0,  4,  9, 2, 4),
        (0,  0,  0, 0, 2),    # a2=0 -> mu in {0, b1}; degenerate
        (0,  1,  0, 1, 2),
        (0,  0,  0, 0, 3),
        (0,  2,  0, 1, 3),
    ]

# ---------------------------------------------------------------
# Per-family computation
# ---------------------------------------------------------------

def char_roots(b1, a2):
    disc = mpf(b1) * b1 - 4 * mpf(a2)
    s = sqrt(disc)            # real or imaginary
    return ((mpf(b1) + s) / 2, (mpf(b1) - s) / 2)

def alpha_W1(mu, a1, a2, b0, b1):
    """Closed-form indicial exponent from W1.  Returns None if denominator vanishes."""
    den = mpf(b1) * mu - 2 * mpf(a2)
    if abs(den) == 0:
        return None
    return -((mpf(b1) - b0) * mu + (mpf(a1) - a2)) / den

def numerical_alpha_fit(a0, a1, a2, b0, b1, N=520, n_lo=100, n_hi=500):
    """Fit log|P_n| - logGamma(n+1) - n*log|mu_dom|  vs log n."""
    mu_p, mu_m = char_roots(b1, a2)
    if abs(mu_p) >= abs(mu_m):
        mu_dom = mu_p
    else:
        mu_dom = mu_m
    if abs(mu_dom) == 0:
        return None
    log_mu_dom = log(abs(mu_dom))

    def b_n(n):
        return mpf(b1) * n + mpf(b0)
    def a_n(n):
        nf = mpf(n)
        return mpf(a2) * nf * nf + mpf(a1) * nf + mpf(a0)

    P_prev = mpf(0)
    P_curr = mpf(1)
    Ps = [P_prev, P_curr]
    for n in range(1, N + 1):
        nxt = b_n(n) * P_curr - a_n(n) * P_prev
        Ps.append(nxt)
        P_prev = P_curr
        P_curr = nxt

    xs, ys = [], []
    for n in range(n_lo, n_hi + 1):
        Pn = Ps[n]
        if abs(Pn) == 0:
            continue
        L = log(abs(Pn)) - mpmath.loggamma(mpf(n + 1)) - mpf(n) * log_mu_dom
        xs.append(log(mpf(n)))
        ys.append(L)
    if len(xs) < 5:
        return None
    nx = len(xs)
    mx = sum(xs) / nx
    my = sum(ys) / nx
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    return num / den

def survey_family(label, fam):
    a0, a1, a2, b0, b1 = fam
    mu_p, mu_m = char_roots(b1, a2)
    a_p = alpha_W1(mu_p, a1, a2, b0, b1)
    a_m = alpha_W1(mu_m, a1, a2, b0, b1)
    if a_p is None or a_m is None:
        S = P = D = None
    else:
        S = a_p + a_m
        P = a_p * a_m
        D = (a_p - a_m) ** 2
    if abs(mu_m) > 0:
        ratio = abs(mu_p / mu_m)
    else:
        ratio = mpf('inf')
    a_fit = numerical_alpha_fit(a0, a1, a2, b0, b1)
    return {
        "label":    label,
        "fam":      list(fam),
        "a2_b1sq":  mpf(a2) / (mpf(b1) ** 2),
        "mu_plus":  mu_p,
        "mu_minus": mu_m,
        "mu_ratio_abs": ratio,
        "alpha_plus":   a_p,
        "alpha_minus":  a_m,
        "alpha_sum":    S,
        "alpha_product":P,
        "alpha_disc":   D,
        "alpha_fit":    a_fit,
    }

# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

def to_str(x):
    if x is None:
        return "None"
    if isinstance(x, mpc):
        return f"({mpmath.nstr(x.real, 10)}{'+' if x.imag>=0 else '-'}{mpmath.nstr(abs(x.imag),10)}j)"
    if isinstance(x, mpf):
        return mpmath.nstr(x, 12)
    return str(x)

def main():
    trans = make_trans_families()
    logs = make_log_families()
    algs = make_alg_families()
    print(f"Trans families: {len(trans)}")
    print(f"Log   families: {len(logs)}")
    print(f"Alg   families: {len(algs)}")

    out = {"Trans": [], "Log": [], "Alg": []}
    for i, f in enumerate(trans, 1):
        r = survey_family(f"T{i:02d}", f)
        out["Trans"].append(r)
    for i, f in enumerate(logs, 1):
        r = survey_family(f"L{i:02d}", f)
        out["Log"].append(r)
    for i, f in enumerate(algs, 1):
        r = survey_family(f"A{i:02d}", f)
        out["Alg"].append(r)

    # ----- Part A2 / A3 prints -----
    print("\n" + "="*78)
    print("Part A2 - per-family indicial summary (Trans, first 10)")
    print("="*78)
    print(f"{'lab':<5}{'a2/b1^2':>10}{'|mu+/mu-|':>14}{'sum':>16}{'product':>16}{'disc':>16}{'fit':>14}")
    for r in out["Trans"][:10]:
        print(f"{r['label']:<5}"
              f"{to_str(r['a2_b1sq']):>10}"
              f"{to_str(r['mu_ratio_abs']):>14}"
              f"{to_str(r['alpha_sum']):>16}"
              f"{to_str(r['alpha_product']):>16}"
              f"{to_str(r['alpha_disc']):>16}"
              f"{to_str(r['alpha_fit']):>14}")

    print("\nFull Trans table (50):")
    print(f"{'lab':<5}{'sum':>16}{'product':>16}{'disc':>16}{'|mu+/mu-|':>14}")
    for r in out["Trans"]:
        print(f"{r['label']:<5}"
              f"{to_str(r['alpha_sum']):>16}"
              f"{to_str(r['alpha_product']):>16}"
              f"{to_str(r['alpha_disc']):>16}"
              f"{to_str(r['mu_ratio_abs']):>14}")

    print("\n" + "="*78)
    print("Non-Trans tables")
    print("="*78)
    for tag in ("Log", "Alg"):
        print(f"\n{tag}:")
        print(f"{'lab':<5}{'a2/b1^2':>10}{'|mu+/mu-|':>14}{'sum':>16}{'product':>16}{'disc':>16}")
        for r in out[tag]:
            print(f"{r['label']:<5}"
                  f"{to_str(r['a2_b1sq']):>10}"
                  f"{to_str(r['mu_ratio_abs']):>14}"
                  f"{to_str(r['alpha_sum']):>16}"
                  f"{to_str(r['alpha_product']):>16}"
                  f"{to_str(r['alpha_disc']):>16}")

    # ----- Part A3 invariant test -----
    print("\n" + "="*78)
    print("Part A3 -- is any of {sum, product, disc, |mu_ratio|} constant across Trans?")
    print("="*78)
    def spread(values):
        # values can be mpf or mpc
        rs = [v.real if isinstance(v, mpc) else v for v in values]
        is_ = [v.imag if isinstance(v, mpc) else mpf(0) for v in values]
        return {
            "min_re": min(rs),
            "max_re": max(rs),
            "max_abs_im": max(abs(i) for i in is_),
        }

    for key in ("alpha_sum", "alpha_product", "alpha_disc", "mu_ratio_abs"):
        vals = [r[key] for r in out["Trans"] if r[key] is not None]
        if not vals:
            print(f"  Trans {key:<14}:  (all None)")
            continue
        sp = spread(vals)
        print(f"  Trans {key:<14}:  re in [{to_str(sp['min_re'])}, {to_str(sp['max_re'])}]    "
              f"max|im|={to_str(sp['max_abs_im'])}")

    # ----- Save to JSON for downstream parts -----
    def serialise(x):
        if isinstance(x, mpc):
            return {"_type": "mpc", "re": str(x.real), "im": str(x.imag)}
        if isinstance(x, mpf):
            return {"_type": "mpf", "v": str(x)}
        if x is None:
            return None
        return x

    serialised = {tag: [{k: serialise(v) for k, v in r.items()} for r in lst]
                  for tag, lst in out.items()}
    with open("indicial_survey.json", "w") as f:
        json.dump(serialised, f, indent=2)
    print("\nWrote indicial_survey.json")


if __name__ == "__main__":
    main()
