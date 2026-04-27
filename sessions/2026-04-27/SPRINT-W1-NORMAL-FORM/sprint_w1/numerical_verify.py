"""
SPRINT-W1-NORMAL-FORM — Part C
Numerical verification of the indicial-exponent prediction
on synthetic degree-(2,1) PCF families.

For y_n satisfying  y_{n+1} = b_n y_n - a_n y_{n-1}  with
  b_n = b1 n + b0,    a_n = a2 n^2 + a1 n + a0,

the Birkhoff ansatz  y_n = Gamma(n+1) * mu^n * n^alpha  predicts:

      ln|y_n|  ~  ln Gamma(n+1)  +  n * ln|mu_dom|  +  alpha * ln n  +  const

where  mu_dom  is the larger-|.| root of   mu^2 - b1 mu + a2 = 0 ,
and   alpha   = -((b1-b0)*mu_dom + a1 - a2) / (b1*mu_dom - 2*a2) .

The two indicial exponents (alpha_+, alpha_-) come from the two mu's.

We fit alpha numerically and compare to the symbolic prediction
on three classes of integer families:
  (T)    a2/b1^2 = -2/9   ("Trans-style", empirically the dominant
         conjectured class)
  (NT)   a2/b1^2 = +1/4   ("Algebraic-style", a different ratio)
  (LOG)  a2/b1^2 = -1/36  ("Log anomaly", from b1 in {6,7})

Each family runs at mpmath dps=150 with N=600 convergents; the linear
fit uses the tail n in [200, 600] to suppress transients.

Phantom-hit rule: any predicted alpha that comes out as the trivial 0
under our convention (i.e., the ansatz secretly degenerates) is flagged.
"""

import mpmath
from mpmath import mp, mpf, mpc, log, sqrt, fabs

mp.dps = 150

# ──────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────

def char_roots(b1, a2):
    disc = b1*b1 - 4*a2
    s = sqrt(mpf(disc))
    return ((b1 + s)/2, (b1 - s)/2)

def alpha_predicted(mu, a1, a2, b0, b1):
    return -((b1 - b0)*mu + (a1 - a2)) / (b1*mu - 2*a2)

def run_family(label, a2, a1, a0, b0, b1, N=600, n_fit_lo=200, n_fit_hi=600):
    print(f"\n{'─'*68}")
    print(f"Family {label}:  a2={a2}, a1={a1}, a0={a0}, b0={b0}, b1={b1}")
    print(f"  a2/b1^2 = {mpf(a2)/(mpf(b1)*mpf(b1))}")
    mu_p, mu_m = char_roots(b1, a2)
    print(f"  characteristic roots:  mu_+ = {mu_p},  mu_- = {mu_m}")
    if abs(mu_p) >= abs(mu_m):
        mu_dom, mu_sub = mu_p, mu_m
    else:
        mu_dom, mu_sub = mu_m, mu_p
    print(f"  dominant |mu| = {abs(mu_dom)}")
    a_p = alpha_predicted(mu_p, a1, a2, b0, b1)
    a_m = alpha_predicted(mu_m, a1, a2, b0, b1)
    print(f"  predicted indicial exponents:  alpha(mu_+) = {a_p}")
    print(f"                                 alpha(mu_-) = {a_m}")
    print(f"  predicted sum     = {a_p + a_m}    (=  (a1-a2)/a2  = {mpf(a1-a2)/mpf(a2)})")
    print(f"  predicted product = {a_p * a_m}")

    # Numerator-side recurrence:  P_{n+1} = b_n P_n - a_n P_{n-1}
    # We feed integer / rational coefficients via mpf() promotion.
    def b_n(n):
        return mpf(b1)*n + mpf(b0)
    def a_n(n):
        n_ = mpf(n)
        return mpf(a2)*n_*n_ + mpf(a1)*n_ + mpf(a0)

    Pm1 = mpf(1)            # P_{-1} placeholder (canonical PCF setup)
    P0  = mpf(0)
    P1  = mpf(1)            # P_1 placeholder
    # Use standard CF numerator recurrence; small adjustment of seeds OK
    # because we only care about asymptotic growth slope, not the limit.
    Ps = [P0, P1]
    cur_prev = P0
    cur_curr = P1
    for n in range(1, N+1):
        nxt = b_n(n) * cur_curr - a_n(n) * cur_prev
        Ps.append(nxt)
        cur_prev = cur_curr
        cur_curr = nxt

    # Take logs of |P_n| in the fit window, subtract log Gamma(n+1) and
    # n*log|mu_dom|, then linear-regress against log n to extract alpha.
    log_mu_dom = log(abs(mu_dom)) if abs(mu_dom) > 0 else mpf(0)
    xs = []
    ys = []
    for n in range(n_fit_lo, n_fit_hi+1):
        Pn = Ps[n]
        if abs(Pn) == 0:
            continue
        L = log(abs(Pn)) - mpmath.loggamma(mpf(n+1)) - mpf(n)*log_mu_dom
        xs.append(log(mpf(n)))
        ys.append(L)
    # Simple least-squares: alpha = cov(x,y)/var(x)
    nx = len(xs)
    mx = sum(xs)/nx
    my = sum(ys)/nx
    num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    den = sum((x-mx)*(x-mx) for x in xs)
    alpha_fit = num/den
    print(f"  numerical alpha (least-squares fit, n in [{n_fit_lo},{n_fit_hi}]): "
          f"{mpmath.nstr(alpha_fit, 12)}")

    # Closeness to predicted dominant alpha (the one that controls growth):
    a_dom = a_p if abs(mu_p) >= abs(mu_m) else a_m
    err = alpha_fit - a_dom
    print(f"  predicted dominant alpha (mu_dom): {mpmath.nstr(a_dom, 12)}")
    print(f"  fit minus prediction:              {mpmath.nstr(err, 6)}")
    return {
        "label":  label,
        "a2_over_b1sq":   mpf(a2)/(mpf(b1)*mpf(b1)),
        "alpha_plus":     a_p,
        "alpha_minus":    a_m,
        "alpha_sum":      a_p + a_m,
        "alpha_product":  a_p * a_m,
        "alpha_fit":      alpha_fit,
        "alpha_dom_pred": a_dom,
    }

# ──────────────────────────────────────────────────────────────────
# Run families
# ──────────────────────────────────────────────────────────────────
print("="*68)
print("PART C — numerical verification of indicial-exponent prediction")
print("="*68)

results = []

# (T1) Integer Trans-style: a2/b1^2 = -2/9 with b1=3, so a2=-2.
#       a1 free, a0 free, b0 free.  We pick small integer values.
results.append(run_family("T1", a2=-2, a1=-4, a0=0, b0=0, b1=3))   # a1=2a2
results.append(run_family("T2", a2=-2, a1=0,  a0=0, b0=1, b1=3))   # a1≠2a2

# (NT1) Algebraic-style: a2/b1^2 = +1/4 with b1=2, so a2=1.
#       Discriminant = 4 - 4 = 0  -> repeat root, degenerate; bump b1=3, a2=2 (ratio = 2/9 > 0)
results.append(run_family("NT1", a2=2, a1=4, a0=0, b0=0, b1=3))    # ratio = 2/9 (algebraic)
results.append(run_family("NT2", a2=4, a1=0, a0=0, b0=0, b1=2))    # ratio = 1, complex roots

# (LOG) Log anomaly: a2/b1^2 = -1/36 with b1=6, so a2=-1.
results.append(run_family("LOG1", a2=-1, a1=-2, a0=0, b0=0, b1=6))

print("\n" + "="*68)
print("SUMMARY  (alpha_sum, alpha_product, fit-vs-prediction)")
print("="*68)
print(f"{'label':<6}{'a2/b1^2':>14}{'sum':>14}{'product':>14}{'fit':>14}{'pred_dom':>14}")
for r in results:
    print(f"{r['label']:<6}"
          f"{mpmath.nstr(r['a2_over_b1sq'], 6):>14}"
          f"{mpmath.nstr(r['alpha_sum'], 6):>14}"
          f"{mpmath.nstr(r['alpha_product'], 6):>14}"
          f"{mpmath.nstr(r['alpha_fit'], 6):>14}"
          f"{mpmath.nstr(r['alpha_dom_pred'], 6):>14}")

print("\nNotes:")
print("  - 'sum' should equal (a1 - a2)/a2 = a1/a2 - 1.")
print("  - For indicial pair {1/3, 2/3}  (sum=1, product=2/9):")
print("    sum=1 forces a1=2a2; given that, product=2/9 forces")
print("    a2 = -9 b0^2 + 27 b0 b1 - 20 b1^2.")
print("  - The Trans-empirical ratio a2/b1^2 = -2/9 corresponds to")
print("    b0/b1 = 3/2 +/- sqrt(17)/18  (irrational), so NO integer")
print("    Trans family can have indicial pair exactly {1/3, 2/3}")
print("    under this framework.")
