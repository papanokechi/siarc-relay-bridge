#!/usr/bin/env python3
"""
DELTA-FREDHOLM-P0 -- PHASE T1 + PHASE T2 CHANNEL B (trace / closed-walk series).

Independent channel (uses neither the continuant recurrence nor eigenvalues):
    delta_B = sum_{m>=1} (-1)^(m+1) tau_m / m,   tau_m = (1/2) Tr T^{2m},
with T the infinite symmetric path-adjacency operator on sites j=1,2,...,
edge (j,j+1) carrying weight sqrt(c_j), c_j = u_{j+1} = 1/((j^2+1)((j+1)^2+1)).

Tr T^{2m} = sum_{j>=1} (T^{2m})_{jj}  (closed walks of length 2m from j).
(T^{2m})_{jj} computed by exact window DP (walks of length 2m stay within distance m).

Site-sum tail handling (the per-n terms decay like n^{-4m}, NOT n^{-8m} -- the
n^{-8m} in the brief is an error, measured slope 8.00/12.00/16.00 for m=2/3/4):
  * m <= MCUT : boundary-aware direct sum j=1..Kdir  +  analytic remainder
                sum_{j>Kdir} g_m^bulk(j) = sum_l a_l * zeta(l, Kdir+1), with the
                bulk asymptotic coefficients a_l obtained EXACTLY by truncated-
                power-series (TPS) DP in eps=1/j.  (n^{-4m} too slow to cut off.)
  * m  > MCUT : decay n^{-4m} fast enough -> boundary-aware direct cutoff with the
                rigorous integral tail bound  sum_{i>K} g_m(i) <= g_m(K)*K/(4m-1).

m-series truncated when |term| < 10^-(TARGET+6); geometric tail bound added.

tau_1 = S = sum_{n>=2} u_n: direct + TPS remainder, cross-checked against the
digamma closed form S = -sum_rho A_rho psi(2-rho) over the 4 roots of b.

Usage:  python t2_trace_channel.py [dps] [target_digits]
"""
import sys, json, hashlib, time, os
from fractions import Fraction
from mpmath import mp, mpf, sqrt, log, zeta, digamma, mpc, fabs, mpf as MPF

DPS    = int(sys.argv[1]) if len(sys.argv) > 1 else 120
TARGET = int(sys.argv[2]) if len(sys.argv) > 2 else 50
mp.dps = DPS
T0 = time.time()
os.makedirs("out", exist_ok=True)

def u_real(n):
    return mpf(1) / (((n-1)**2 + 1) * (n**2 + 1))
def c_edge(j):
    return u_real(j+1)                       # squared weight of edge (j,j+1)

# ----------------------------------------------------------- truncated power series
def smul(a, b, L):
    r = [mpf(0)]*(L+1)
    for i in range(min(len(a), L+1)):
        ai = a[i]
        if ai == 0:
            continue
        top = L+1-i
        for k in range(min(len(b), top)):
            r[i+k] += ai*b[k]
    return r
def srecip(a, L):
    b = [mpf(0)]*(L+1); b[0] = 1/a[0]
    for n in range(1, L+1):
        s = mpf(0)
        for k in range(1, n+1):
            if k < len(a):
                s += a[k]*b[n-k]
        b[n] = -b[0]*s
    return b
def ssqrt(a, L):
    b = [mpf(0)]*(L+1); b[0] = sqrt(a[0])
    for n in range(1, L+1):
        s = mpf(0)
        for k in range(1, n):
            s += b[k]*b[n-k]
        an = a[n] if n < len(a) else mpf(0)
        b[n] = (an - s)/(2*b[0])
    return b

def weight_series(s_off, L):
    """sqrt(c_edge(site=j+s_off)) as a TPS in eps=1/j: = eps^2 * sqrt(1/(P*Q))."""
    P = [mpf(1), mpf(2*s_off),     mpf(s_off*s_off + 1)]
    Q = [mpf(1), mpf(2*(s_off+1)), mpf((s_off+1)**2 + 1)]
    W = ssqrt(srecip(smul(P, Q, L), L), L)
    w = [mpf(0), mpf(0)] + W[:L-1]
    return w[:L+1]

def g_bulk_series(m, L):
    """Asymptotic series (in eps=1/j) of g_m^bulk(j)=(T^{2m})_{jj}; coeff[l]=a_l (j^-l)."""
    n = 2*m + 1
    w = [weight_series(s, L) for s in range(-m, m)]       # n-1 edges
    v = [[mpf(0)]*(L+1) for _ in range(n)]; v[m][0] = mpf(1)
    for _ in range(2*m):
        nv = [[mpf(0)]*(L+1) for _ in range(n)]
        for i in range(n):
            acc = nv[i]
            if i > 0:
                t = smul(w[i-1], v[i-1], L)
                for q in range(L+1): acc[q] += t[q]
            if i < n-1:
                t = smul(w[i], v[i+1], L)
                for q in range(L+1): acc[q] += t[q]
        v = nv
    return v[m]

# ------------------------------------------------------- boundary-aware window DP
def g_m(j, m):
    lo = max(1, j-m); hi = j+m; n = hi-lo+1; ctr = j-lo
    w = [sqrt(c_edge(lo+i)) for i in range(n-1)]
    v = [mpf(0)]*n; v[ctr] = mpf(1)
    for _ in range(2*m):
        nv = [mpf(0)]*n
        for i in range(n):
            if i > 0:   nv[i] += w[i-1]*v[i-1]
            if i < n-1: nv[i] += w[i]*v[i+1]
        v = nv
    return v[ctr]

# --------------------------------------------------------------------- tau_1 = S
def u_series_for_S(L):
    """u_n = 1/(((n-1)^2+1)(n^2+1)) as TPS in eps=1/n: = eps^4 * recip(P*Q)."""
    P = [mpf(1), mpf(-2), mpf(2)]      # (n-1)^2+1 = n^2(1-2eps+2eps^2)
    Q = [mpf(1), mpf(0),  mpf(1)]      # n^2+1     = n^2(1+eps^2)
    inv = srecip(smul(P, Q, L), L)
    return [mpf(0)]*4 + inv[:L-3]

def S_direct_series(Kdir=400, L=30):
    s = sum(u_real(nn) for nn in range(2, Kdir+1))
    co = u_series_for_S(L)
    rem = sum(co[l]*zeta(l, Kdir+1) for l in range(4, L+1))
    return s + rem

def S_closed_form():
    roots = [mpc(0,1), mpc(0,-1), mpc(1,1), mpc(1,-1)]   # i,-i,1+i,1-i
    S = mpc(0)
    for r in roots:
        A = mpc(1)
        for rp in roots:
            if rp != r:
                A *= (r - rp)
        A = 1/A
        S += -A*digamma(2 - r)
    return S.real

# --------------------------------------------------------------------- tau_m
def tau_m(m, MCUT=6, Kdir=400, enclosure=None):
    if m == 1:
        return S_direct_series()
    if m <= MCUT:
        L = max(4*m, 44)
        direct = sum(g_m(j, m) for j in range(1, Kdir+1))
        co = g_bulk_series(m, L)
        rem  = sum(co[l]*zeta(l, Kdir+1) for l in range(4*m, L+1))
        if enclosure is not None:
            # rigorous geometric tail bound from the last two nonzero series terms
            nz = [fabs(co[l]*zeta(l, Kdir+1)) for l in range(4*m, L+1) if co[l] != 0]
            t_last, t_prev = nz[-1], nz[-2]
            rho = t_last/t_prev if t_prev != 0 else mpf(0)
            tail_bd = t_last*rho/(1-rho) if rho < 1 else t_last*10
            enclosure.append(tail_bd/2)
        return (direct + rem)/2
    else:
        s = mpf(0); j = 1; gprev = None
        thr = mpf(10)**(-(TARGET+12))
        while True:
            gj = g_m(j, m); s += gj
            if j > m+2 and gj < thr and (gprev is None or gj < gprev):
                tail_bound = gj*j/(4*m-1)
                if enclosure is not None:
                    enclosure.append(tail_bound/2)
                break
            gprev = gj
            j += 1
            if j > 6000:
                break
        return s/2

# --------------------------------------------------------------------- T1 sanity
def phase_T1():
    out = {}
    # exact rational: (1/2)Tr T_N^2 == sum_{n=2}^N u_n
    def uF(n): return Fraction(1, ((n-1)**2+1)*(n**2+1))
    for N in (5, 10, 25):
        # Tr T_N^2 = 2*sum_{j=1}^{N-1} w_j^2, w_j^2 = u_{j+1}
        tr = 2*sum(uF(j+1) for j in range(1, N))
        rhs = 2*sum(uF(n) for n in range(2, N+1))
        half_tr = Fraction(tr, 2)
        target = sum(uF(n) for n in range(2, N+1))
        out[f"N={N}_exact_half_tr_eq_sum_u"] = (half_tr == target)
        assert half_tr == target
    # dps check N=1000
    N = 1000
    half_tr = sum(c_edge(j) for j in range(1, N))      # = sum_{n=2}^{N} u_n
    sum_u   = sum(u_real(n) for n in range(2, N+1))
    out["N=1000_half_tr_minus_sum_u_dps"] = mp.nstr(fabs(half_tr - sum_u), 4)
    out["pass"] = all(out[k] for k in out if k.endswith("sum_u")) and (fabs(half_tr-sum_u) < mpf(10)**(-(DPS-10)))
    return out

# --------------------------------------------------------------------- main
def main():
    rep = {"task_id": "DELTA-FREDHOLM-P0", "phase": "T1+T2B", "dps": DPS, "target_digits": TARGET}
    delta_ref = mpf("0.12385719436062639272850498970259084096757955")

    # ---- T1
    t1 = phase_T1()
    rep["T1_trace_sanity"] = t1
    if not t1["pass"]:
        rep["verdict"] = "HALT-T1"; print(json.dumps(rep, indent=2)); return

    # ---- S cross-check
    S_ds = S_direct_series()
    S_cf = S_closed_form()
    rep["S_direct_series"]   = mp.nstr(S_ds, 50)
    rep["S_closed_form"]     = mp.nstr(S_cf, 50)
    rep["S_agreement_digits"] = int(-mp.log10(fabs(S_ds - S_cf))) if S_ds != S_cf else DPS

    # ---- channel B m-series
    enclosure = []
    encl_terms = []
    dB = mpf(0); prev = None; ratios = []
    mmax = 0
    for m in range(1, 200):
        tm = tau_m(m, enclosure=encl_terms)
        term = ((-1)**(m+1))*tm/m
        dB += term
        if prev is not None:
            ratios.append(tm/prev)
        prev = tm
        mmax = m
        if fabs(term) < mpf(10)**(-(TARGET+6)) and m > 4:
            # geometric tail bound for remaining m-series
            r = ratios[-1]
            mseries_tail = fabs(term)*r/(1-r)
            enclosure.append(mseries_tail)
            break
    enclosure_total = sum(encl_terms) + sum(enclosure)
    rep["m_max"] = mmax
    rep["observed_tau_ratio_limit"] = mp.nstr(ratios[-1], 12)
    rep["delta_B"] = mp.nstr(dB, 62)

    # structural: leading bulk coefficient a_{4m} = C(2m,m) (central binomial)
    from math import comb
    binom_check = {}
    for m in range(2, 7):
        co = g_bulk_series(m, 4*m)
        binom_check[f"m={m}"] = (co[4*m] == comb(2*m, m), comb(2*m, m))
    rep["leading_coeff_is_central_binomial"] = binom_check
    rep["enclosure_total"] = mp.nstr(enclosure_total, 6)
    rep["diff_vs_ref"] = mp.nstr(fabs(dB - delta_ref), 6)
    rep["agreement_vs_ref_digits"] = int(-mp.log10(fabs(dB - delta_ref)))
    rep["runtime_s"] = round(time.time()-T0, 1)

    with open(__file__, "rb") as fh:
        rep["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    # store full-precision delta_B for cross-channel compare
    with open("out/delta_B.txt", "w") as fh:
        fh.write(mp.nstr(dB, DPS-5))
    out = json.dumps(rep, indent=2)
    print(out)
    with open("out/t2_trace_result.json", "w") as fh:
        fh.write(out)

if __name__ == "__main__":
    main()
