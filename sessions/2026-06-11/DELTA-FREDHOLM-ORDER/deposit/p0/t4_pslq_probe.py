#!/usr/bin/env python3
"""
DELTA-FREDHOLM-P0 -- PHASE T4 (optional, runs only on a PASS verdict).

PSLQ probe of the two largest positive eigenvalues s1, s2 of the infinite
edge-weighted path operator T against a basis of reciprocal Bessel zeros
    { 1/j_{nu,k} : nu in {0,1/2,1,3/2,2},  k in {1,2,3} }
plus { 1, pi, sqrt(2), sqrt(5), sqrt(10) }.
Expected outcome: NULL (no low-height integer relation).  A hit is only
CONJECTURED, pending a precision-stability re-test at 120 digits.

s1, s2 are computed by Rayleigh-quotient iteration (numpy double seeds refined
on the exact tridiagonal at high dps) and verified stable across N and dps.

Usage:  python t4_pslq_probe.py [dps]
"""
import sys, json, hashlib, time, os
from mpmath import mp, mpf, sqrt, pi, pslq, besseljzero, fabs, log10
import numpy as np

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 90
mp.dps = DPS
T0 = time.time()
os.makedirs("out", exist_ok=True)

def u_real(n):
    return mpf(1) / (((n-1)**2 + 1) * (n**2 + 1))

def tridiag_solve(beta, mu, rhs):
    n = len(rhs); d = [-mu]*n
    cp = [mpf(0)]*n; dp = [mpf(0)]*n
    cp[0] = beta[0]/d[0]; dp[0] = rhs[0]/d[0]
    for i in range(1, n):
        a = beta[i-1]; denom = d[i] - a*cp[i-1]
        if i < n-1: cp[i] = beta[i]/denom
        dp[i] = (rhs[i] - a*dp[i-1])/denom
    x = [mpf(0)]*n; x[-1] = dp[-1]
    for i in range(n-2, -1, -1):
        x[i] = dp[i] - cp[i]*x[i+1]
    return x

def matvecT(beta, v):
    n = len(v); r = [mpf(0)]*n
    for i in range(n):
        if i > 0:   r[i] += beta[i-1]*v[i-1]
        if i < n-1: r[i] += beta[i]*v[i+1]
    return r

def top_eigs(N, niter=6):
    beta_d = np.array([float((1.0/(((j)**2+1.0)*((j+1)**2+1.0)))**0.5) for j in range(1, N)])
    M = np.zeros((N, N))
    for j in range(N-1):
        M[j, j+1] = beta_d[j]; M[j+1, j] = beta_d[j]
    w, V = np.linalg.eigh(M)
    order = np.argsort(w)[::-1]
    beta = [sqrt(u_real(j+1)) for j in range(1, N)]
    res = []
    for idx in order[:2]:
        mu = mpf(float(w[idx]))
        v = [mpf(float(V[i, idx])) for i in range(N)]
        for _ in range(niter):
            wv = tridiag_solve(beta, mu, v)
            nrm = sqrt(sum(x*x for x in wv))
            v = [x/nrm for x in wv]
            Tv = matvecT(beta, v)
            mu = sum(v[i]*Tv[i] for i in range(N))
        res.append(mu)
    return res

def build_basis():
    names = []; vals = []
    for nu in [mpf(0), mpf(1)/2, mpf(1), mpf(3)/2, mpf(2)]:
        for k in [1, 2, 3]:
            j = besseljzero(nu, k)
            names.append(f"1/j_{{{mp.nstr(nu,3)},{k}}}"); vals.append(1/j)
    for nm, v in [("1", mpf(1)), ("pi", pi), ("sqrt2", sqrt(2)),
                  ("sqrt5", sqrt(5)), ("sqrt10", sqrt(10))]:
        names.append(nm); vals.append(v)
    return names, vals

def probe(x, label, names, vals):
    cur_names = list(names); cur_vals = list(vals)
    basis_degeneracies = []
    for _ in range(len(vals)):
        reln = pslq([x] + cur_vals, maxcoeff=10**10, maxsteps=10**6)
        if reln is None:
            return {"target": label, "value": mp.nstr(x, 60),
                    "outcome": "NULL", "relation": None,
                    "basis_degeneracies_removed": basis_degeneracies}
        if reln[0] == 0:
            # relation does NOT involve the target -> pure basis degeneracy; deflate
            idxs = [i for i in range(1, len(reln)) if reln[i] != 0]
            basis_degeneracies.append(
                [(cur_names[i-1], reln[i]) for i in idxs])
            drop = idxs[-1]
            del cur_names[drop-1]; del cur_vals[drop-1]
            continue
        # candidate relation involving the target (subject to stability screen)
        return {"target": label, "value": mp.nstr(x, 60),
                "outcome": "CANDIDATE", "relation": reln,
                "terms": [(cur_names[i-1], reln[i]) for i in range(1, len(reln)) if reln[i] != 0],
                "basis_degeneracies_removed": basis_degeneracies}
    return {"target": label, "value": mp.nstr(x, 60), "outcome": "NULL",
            "relation": None, "basis_degeneracies_removed": basis_degeneracies}

def run_at(dps_local):
    mp.dps = dps_local
    s = top_eigs(400)
    names, vals = build_basis()
    return s, probe(s[0], "s1", names, vals), probe(s[1], "s2", names, vals)

def screen(rlo, rhi):
    """Working-precision artifact screen: a genuine integer relation is identical
    at both precisions; a spurious one changes coefficients or vanishes."""
    if rlo["outcome"] == "NULL" or rhi["outcome"] == "NULL":
        return "NULL"
    if rlo.get("relation") == rhi.get("relation"):
        return "HIT-STABLE(CONJECTURED; verify higher precision)"
    return "NULL(artifact: PSLQ relation precision-unstable across dps)"

def main():
    rep = {"task_id": "DELTA-FREDHOLM-P0", "phase": "T4", "dps_lo": DPS, "dps_hi": DPS+40}
    rep["basis_note"] = ("j_{1/2,k} = k*pi exactly, so 1/j_{1/2,k} = 1/(k*pi) are "
                         "Q-linearly dependent (rank 1); PSLQ deflation removes these "
                         "basis-internal degeneracies before judging the target.")

    # eigenvalue stability across truncation N (at DPS)
    mp.dps = DPS
    s_200 = top_eigs(200); s_400 = top_eigs(400)
    rep["s1"] = mp.nstr(s_400[0], 64)
    rep["s2"] = mp.nstr(s_400[1], 64)
    rep["s1_N200_vs_N400_digits"] = int(-log10(fabs(s_200[0]-s_400[0]))) if s_200[0] != s_400[0] else DPS
    rep["s2_N200_vs_N400_digits"] = int(-log10(fabs(s_200[1]-s_400[1]))) if s_200[1] != s_400[1] else DPS

    _, r1_lo, r2_lo = run_at(DPS)
    _, r1_hi, r2_hi = run_at(DPS+40)
    names, _ = build_basis()
    rep["basis"] = names
    rep["probe_s1"] = {"dps_lo": r1_lo, "dps_hi": r1_hi, "screened_outcome": screen(r1_lo, r1_hi)}
    rep["probe_s2"] = {"dps_lo": r2_lo, "dps_hi": r2_hi, "screened_outcome": screen(r2_lo, r2_hi)}
    rep["T4_verdict"] = ("NULL" if rep["probe_s1"]["screened_outcome"].startswith("NULL")
                         and rep["probe_s2"]["screened_outcome"].startswith("NULL")
                         else "HIT(see screened_outcome)")
    rep["runtime_s"] = round(time.time()-T0, 1)
    with open(__file__, "rb") as fh:
        rep["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    out = json.dumps(rep, indent=2)
    print(out)
    with open("out/t4_pslq_result.json", "w") as fh:
        fh.write(out)

if __name__ == "__main__":
    main()
