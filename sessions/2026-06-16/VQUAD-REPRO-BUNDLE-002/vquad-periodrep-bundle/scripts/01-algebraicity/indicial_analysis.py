#!/usr/bin/env python3
# PERIOD-REP-VQUAD-002 Stage 4b — indicial exponents of L_V at its finite singular
# points, exact over Q(sqrt3). Resolves Stage-4 checks 4.2 (singular locus, with the
# sign of xi0) and 4.3 (local exponent vs branch exponent beta=-1/(3 sqrt3)).
import sys as _sys  # bundle portability: force UTF-8 console output
try:
    _sys.stdout.reconfigure(encoding="utf-8")
    _sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from holonomic_recognition_q3 import (Q3, formal_series_coeffs_exact, borel_coeffs,
                                      holonomic_matrix, nullspace_dim, falling)
from extract_verify_operators import extract_operator, clear_denoms, q3_to_mp
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 80

def taylor_shift_poly(pk, xs):
    """Given poly pk = [c0,c1,...] (in Q3) meaning sum c_i xi^i, return Taylor coeffs
       in t = xi - xs:  pk(xs+t)= sum_j d_j t^j, d_j in Q3."""
    d = len(pk) - 1
    out = [Q3(0)] * (d + 1)
    # binomial expansion: xi^i = (xs+t)^i = sum_{j<=i} C(i,j) xs^{i-j} t^j
    from math import comb
    for i, c in enumerate(pk):
        if c.is_zero(): continue
        xspow = [Q3(1)] * (i + 1)
        for e in range(1, i + 1):
            xspow[e] = xspow[e-1] * xs
        for j in range(i + 1):
            out[j] = out[j] + c * comb(i, j) * xspow[i - j]
    return out

def indicial_poly_roots(polys, xs):
    """Indicial polynomial at regular singular point xs of operator sum_k p_k D^k.
       Returns (mu, indicial coeffs as poly in rho via falling factorials, numeric roots)."""
    r = len(polys) - 1
    taylors = [taylor_shift_poly(pk, xs) for pk in polys]
    # nu_k = order of vanishing of p_k at xs
    nu = []
    for tk in taylors:
        v = None
        for j, c in enumerate(tk):
            if not c.is_zero():
                v = j; break
        nu.append(v if v is not None else 10**9)
    mu = max(k - nu[k] for k in range(r + 1) if nu[k] < 10**9)
    # indicial polynomial I(rho) = sum_{k: k-nu_k=mu} p_{k,nu_k} * falling(rho,k)
    # represent as numeric polynomial in rho
    def falling_poly(k):
        # returns list of coeffs (low->high) of rho(rho-1)...(rho-k+1)
        poly = [1.0]
        for t in range(k):
            # multiply by (rho - t)
            new = [0.0]*(len(poly)+1)
            for i,c in enumerate(poly):
                new[i+1] += c        # rho*c
                new[i]   += -t*c     # -t*c
            poly = new
        return poly
    maxdeg = r
    I = [0.0]*(maxdeg+1)
    contributing = []
    for k in range(r+1):
        if nu[k] < 10**9 and (k - nu[k]) == mu:
            coef = float(q3_to_mp(taylors[k][nu[k]]))
            fp = falling_poly(k)
            for i,c in enumerate(fp):
                I[i] += coef*c
            contributing.append(k)
    import numpy as np
    # roots: numpy wants high->low
    Ihi = I[::-1]
    # strip leading zeros
    while len(Ihi) > 1 and abs(Ihi[0]) < 1e-14:
        Ihi = Ihi[1:]
    roots = list(np.roots(Ihi)) if len(Ihi) > 1 else []
    return mu, contributing, [complex(z) for z in roots]

def main():
    a = formal_series_coeffs_exact(150)
    b = borel_coeffs(a)
    dV, polys_V, _ = extract_operator(b, 4, 8)
    polys_V = clear_denoms(polys_V)

    r3 = math.sqrt(3.0)
    beta = -1.0/(3*r3)
    xi0 = 2.0/r3
    out = {"beta": beta, "xi0": xi0}

    # exact singular points: roots of leading coeff p4 = ξ*(linear). Build them exactly.
    # leading coeff is polys_V[4]; we KNOW analytically roots {0, -2/sqrt3}; verify -2/sqrt3.
    xs_neg = Q3(0, F(-2,3))   # -2/sqrt3
    # verify leading coeff vanishes there exactly
    lc = polys_V[4]
    val = Q3(0)
    xp = Q3(1)
    for i,c in enumerate(lc):
        val = val + c*xp
        xp = xp*xs_neg
    out["leading_coeff_at_minus_xi0_is_zero"] = val.is_zero()
    print(f"[exact] leading coeff p4(-2/sqrt3) == 0 : {val.is_zero()}")

    # indicial at xs = -xi0
    mu, contrib, roots = indicial_poly_roots(polys_V, xs_neg)
    realroots = sorted([z.real for z in roots if abs(z.imag) < 1e-9])
    print(f"[indicial @ -xi0] contributing orders k={contrib}, mu={mu}")
    print(f"[indicial @ -xi0] exponents (real): {[f'{x:.10f}' for x in realroots]}")
    out["indicial_at_minus_xi0"] = {"mu": mu, "contributing_k": contrib,
                                     "real_exponents": realroots,
                                     "all_roots": [[z.real, z.imag] for z in roots]}
    # compare to branch predictions: -(1+beta), -beta, etc.
    preds = {"-(1+beta)": -(1+beta), "-beta": -beta, "1+beta": 1+beta, "beta": beta,
             "-(1+beta)+integers": None}
    print(f"[indicial @ -xi0] beta={beta:.10f}, -(1+beta)={-(1+beta):.10f}, -beta={-beta:.10f}")
    # find which prediction matches a root (mod 1, since Frobenius exponents differ by ints)
    matches = []
    for x in realroots:
        for nm, val2 in (("-(1+beta)", -(1+beta)), ("-beta", -beta), ("beta", beta), ("1+beta", 1+beta)):
            if abs(((x - val2) % 1.0)) < 1e-6 or abs(((x - val2) % 1.0) - 1.0) < 1e-6:
                matches.append((round(x,8), nm, round(x-val2,6)))
    out["exponent_matches_mod1"] = matches
    print(f"[indicial @ -xi0] exponent matches to beta-family (mod 1): {matches}")

    # numeric local exponent of B-hat at -xi0 via corrected ratio test (sing at -xi0):
    bm = [q3_to_mp(x) for x in b]
    ests = []
    for m in range(len(bm)//2, len(bm)-1):
        rr = bm[m+1]/bm[m]*mp.mpf(-xi0)   # -> 1 at -xi0
        ests.append(m*(rr-1))
    s_est = float(mp.fsum(ests[-25:])/25) + 1
    out["numeric_local_exponent_Bhat_at_minus_xi0"] = s_est
    print(f"[ratio @ -xi0] numeric B-hat local exponent: {s_est:.8f}  (predicted -(1+beta)={-(1+beta):.8f})")

    # indicial at xs=0 (the apparent/regular point) for completeness
    mu0, contrib0, roots0 = indicial_poly_roots(polys_V, Q3(0,0))
    rr0 = sorted([z.real for z in roots0 if abs(z.imag)<1e-9])
    out["indicial_at_0"] = {"mu": mu0, "real_exponents": rr0}
    print(f"[indicial @ 0] exponents: {[f'{x:.6f}' for x in rr0]}")

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "indicial_results.json"),"w",encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print("[done] wrote indicial_results.json")

if __name__ == "__main__":
    main()
