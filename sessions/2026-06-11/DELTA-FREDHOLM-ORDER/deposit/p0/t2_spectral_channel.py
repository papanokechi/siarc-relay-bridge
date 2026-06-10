#!/usr/bin/env python3
"""
DELTA-FREDHOLM-P0 -- PHASE T2 CHANNEL A (spectral / Hadamard product).

Headline value uses the Hadamard product form  prod_{s>0}(1+s_k^2) = R_N  i.e.
    delta_A = log R_N  +  Tail(N),
where R_k = R_{k-1} + u_k R_{k-2}  (R_0=R_1=1)  is the locked continuant/independence
polynomial, equal to det(I+T_N^2)^{1/2}, and

    Tail(N) = sum_{k>N} log(rho_k),   rho_k = R_k/R_{k-1} = 1 + u_k/rho_{k-1}.

rho_k is the depth-D backward continued fraction in u_k, u_{k-1}, ...; the boundary
transient is suppressed by prod u_j (< 10^-2000 by k=2000) so the bulk asymptotic
series of log(rho_k) in eps=1/k is exact.  Coefficients c_l obtained EXACTLY by
truncated-power-series (TPS) arithmetic (CF built in series; log of series);
Tail(N) = sum_l c_l * zeta(l, N+1)  (Hurwitz zeta).

SPECTRAL CONFIRMATION: at moderate N the actual eigenvalues s_k of T_N are computed
by Rayleigh-quotient iteration (numpy double seeds, refined at high dps on the exact
tridiagonal), and  sum_{s_k>0} log(1+s_k^2)  is checked against log R_N -- exhibiting
the eigenvalues and confirming the spectral = determinant = continuant identity.

Enclosure: vary CF depth D in {6,7,8}, series cutoff jhi, and N in {2000,4000}.

Usage:  python t2_spectral_channel.py [dps]
"""
import sys, json, hashlib, time, os
from mpmath import mp, mpf, log, zeta, sqrt, fabs, matrix, mpc
import numpy as np

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 120
mp.dps = DPS
T0 = time.time()
os.makedirs("out", exist_ok=True)

def u_real(n):
    return mpf(1) / (((n-1)**2 + 1) * (n**2 + 1))

# ----------------------------------------------------------------- log R_N
def logR(N):
    Rm2, Rm1 = mpf(1), mpf(1)          # R_0, R_1
    for k in range(2, N+1):
        Rk = Rm1 + u_real(k)*Rm2
        Rm2, Rm1 = Rm1, Rk
    return log(Rm1)

# ----------------------------------------------------------- TPS helpers
def smul(a, b, L):
    r = [mpf(0)]*(L+1)
    for i in range(min(len(a), L+1)):
        ai = a[i]
        if ai == 0: continue
        for k in range(min(len(b), L+1-i)):
            r[i+k] += ai*b[k]
    return r
def srecip(a, L):
    b = [mpf(0)]*(L+1); b[0] = 1/a[0]
    for n in range(1, L+1):
        s = mpf(0)
        for k in range(1, n+1):
            if k < len(a): s += a[k]*b[n-k]
        b[n] = -b[0]*s
    return b
def slog1(a, L):
    """log of TPS a with a[0]=1."""
    Lg = [mpf(0)]*(L+1)
    for n in range(1, L+1):
        s = mpf(0)
        for k in range(1, n):
            s += k*Lg[k]*a[n-k]
        Lg[n] = a[n] - s/n
    return Lg

def u_shift_series(i, L):
    """u(k-i) as TPS in eps=1/k: eps^4 * recip( ((k-i-1)^2+1)/k^2 * ((k-i)^2+1)/k^2 )."""
    P = [mpf(1), mpf(-2*(i+1)), mpf((i+1)**2 + 1)]
    Q = [mpf(1), mpf(-2*i),     mpf(i*i + 1)]
    inv = srecip(smul(P, Q, L), L)
    return [mpf(0)]*4 + inv[:L-3]

def logrho_series(D, L):
    """Asymptotic series (eps=1/k) of log(rho_star), rho_star = depth-D backward CF."""
    r = [mpf(1)] + [mpf(0)]*L            # innermost = 1
    for i in range(D-1, -1, -1):
        num = u_shift_series(i, L)        # u(k-i)
        r = smul(num, srecip(r, L), L)
        r[0] += 1                         # 1 + u/(...)
    return slog1(r, L)                    # c_l, leading l=4

def tail(N, D, jhi, L):
    c = logrho_series(D, L)
    return sum(c[l]*zeta(l, N+1) for l in range(4, jhi+1))

# ----------------------------------------------- spectral confirmation
def tridiag_solve(beta, mu, rhs):
    """Solve (T - mu I) x = rhs for the zero-diagonal tridiagonal T with off-diag beta."""
    n = len(rhs)
    d = [-mu]*n
    cp = [mpf(0)]*n; dp = [mpf(0)]*n
    cp[0] = beta[0]/d[0]; dp[0] = rhs[0]/d[0]
    for i in range(1, n):
        a = beta[i-1]
        denom = d[i] - a*cp[i-1]
        if i < n-1:
            cp[i] = beta[i]/denom
        dp[i] = (rhs[i] - a*dp[i-1])/denom
    x = [mpf(0)]*n
    x[-1] = dp[-1]
    for i in range(n-2, -1, -1):
        x[i] = dp[i] - cp[i]*x[i+1]
    return x

def matvecT(beta, v):
    n = len(v); r = [mpf(0)]*n
    for i in range(n):
        if i > 0:   r[i] += beta[i-1]*v[i-1]
        if i < n-1: r[i] += beta[i]*v[i+1]
    return r

def spectral_confirm(Nspec, dps_spec):
    old = mp.dps; mp.dps = dps_spec
    beta_d = np.array([float((1.0/(((j)**2+1.0)*((j+1)**2+1.0)))**0.5) for j in range(1, Nspec)])
    M = np.zeros((Nspec, Nspec))
    for j in range(Nspec-1):
        M[j, j+1] = beta_d[j]; M[j+1, j] = beta_d[j]
    w, V = np.linalg.eigh(M)
    beta = [sqrt(u_real(j+1)) for j in range(1, Nspec)]   # exact off-diagonals
    ssum = mpf(0); s_sorted = []
    for idx in range(Nspec):
        mu = mpf(float(w[idx]))
        v = [mpf(float(V[i, idx])) for i in range(Nspec)]
        for _ in range(4):                                 # Rayleigh quotient iteration
            try:
                wv = tridiag_solve(beta, mu, v)
            except ZeroDivisionError:
                break
            nrm = sqrt(sum(x*x for x in wv))
            v = [x/nrm for x in wv]
            Tv = matvecT(beta, v)
            mu = sum(v[i]*Tv[i] for i in range(Nspec))
        s_sorted.append(mu)
        if mu > 0:
            ssum += log(1 + mu*mu)
    lr = logR(Nspec)
    s_sorted.sort(reverse=True)
    res = {
        "Nspec": Nspec, "dps_spec": dps_spec,
        "sum_pos_log1ps2": mp.nstr(ssum, 45),
        "logR_Nspec": mp.nstr(lr, 45),
        "agreement_digits": int(-mp.log10(fabs(ssum - lr))) if ssum != lr else dps_spec,
        "s1": mp.nstr(s_sorted[0], 45),
        "s2": mp.nstr(s_sorted[1], 45),
    }
    mp.dps = old
    return res, s_sorted[0], s_sorted[1]

# --------------------------------------------------------------- main
def main():
    rep = {"task_id": "DELTA-FREDHOLM-P0", "phase": "T2A", "dps": DPS}
    delta_ref = mpf("0.12385719436062639272850498970259084096757955")

    # headline at N=4000, D=10, jhi=48
    L = 54
    N0 = 4000
    lr0 = logR(N0)
    dA = lr0 + tail(N0, 10, 48, L)
    rep["delta_A"] = mp.nstr(dA, 62)

    # ---- enclosure sweep
    variants = {}
    for (N, D, jhi) in [(2000,8,40),(2000,9,44),(4000,9,44),(4000,10,48),(4000,10,52),(8000,10,48)]:
        val = logR(N) + tail(N, D, jhi, L)
        variants[f"N{N}_D{D}_j{jhi}"] = mp.nstr(val, 60)
    vals = [mpf(v) for v in variants.values()]
    spread = max(fabs(a-dA) for a in vals)
    rep["enclosure_variants"] = variants
    rep["enclosure_spread"] = mp.nstr(spread, 6)
    rep["diff_vs_ref"] = mp.nstr(fabs(dA - delta_ref), 6)
    rep["agreement_vs_ref_digits"] = int(-mp.log10(fabs(dA - delta_ref)))

    # leading tail coefficients (report for the record: c4=1,c5=2,c6=1,...)
    cc = logrho_series(8, 12)
    rep["logrho_coeffs_c4_c10"] = [mp.nstr(cc[l], 8) for l in range(4, 11)]

    # ---- spectral confirmation (exhibits eigenvalues)
    sc, s1, s2 = spectral_confirm(160, max(60, min(DPS, 80)))
    rep["spectral_confirmation"] = sc

    rep["runtime_s"] = round(time.time()-T0, 1)
    with open(__file__, "rb") as fh:
        rep["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    with open("out/delta_A.txt", "w") as fh:
        fh.write(mp.nstr(dA, DPS-5))
    with open("out/s1s2.txt", "w") as fh:
        fh.write(mp.nstr(s1, 65) + "\n" + mp.nstr(s2, 65) + "\n")
    out = json.dumps(rep, indent=2)
    print(out)
    with open("out/t2_spectral_result.json", "w") as fh:
        fh.write(out)

if __name__ == "__main__":
    main()
