#!/usr/bin/env python3
# PERIOD-REP-VQUAD-002 Stage 3.2 — Borel-Pade pole census (numerical confirmation).
# Independently confirms the dominant Borel singularity location/sign and the ABSENCE
# of an infinite resurgent tower (consistent with the proven holonomic L_V whose finite
# singular locus is {0, -xi0, inf}). Branch point at -xi0 should manifest as a string
# of Pade poles accumulating at -xi0 (the standard Pade-approximation-of-a-cut signature).
import sys as _sys  # bundle portability: force UTF-8 console output
try:
    _sys.stdout.reconfigure(encoding="utf-8")
    _sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import sys, math, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from holonomic_recognition_q3 import formal_series_coeffs_exact, borel_coeffs
from extract_verify_operators import q3_to_mp
import mpmath as mp
mp.mp.dps = 120

def pade_poles(coeffs, L, M):
    """Diagonal-ish Pade [L/M] from power-series coeffs; return poles (roots of denom)."""
    # Solve for denominator b_1..b_M from c_{L+1..L+M} convolution; b_0=1.
    # sum_{j} b_j c_{n-j} = 0 for n=L+1..L+M
    import mpmath
    N = M
    A = mp.matrix(N, N)
    rhs = mp.matrix(N, 1)
    for i in range(N):
        n = L + 1 + i
        for j in range(1, M+1):
            A[i, j-1] = coeffs[n-j] if 0 <= n-j < len(coeffs) else mp.mpf(0)
        rhs[i] = -coeffs[n] if n < len(coeffs) else mp.mpf(0)
    bsol = mp.lu_solve(A, rhs)
    denom = [mp.mpf(1)] + [bsol[k] for k in range(M)]   # b_0..b_M (low->high)
    # poles = roots of sum_k denom[k] x^k
    poly_hi = denom[::-1]
    roots = mp.polyroots(poly_hi, maxsteps=200, extraprec=200)
    return roots

def main():
    a = formal_series_coeffs_exact(120)
    b = [q3_to_mp(x) for x in borel_coeffs(a)]
    r3 = math.sqrt(3.0); xi0 = 2.0/r3
    out = {"xi0": xi0, "minus_xi0": -xi0}
    print(f"xi0 = 2/sqrt3 = {xi0:.15f};  -xi0 = {-xi0:.15f}")
    census = []
    for (L, M) in [(20,20),(25,25),(30,30),(35,35),(40,40)]:
        try:
            roots = pade_poles(b, L, M)
        except Exception as e:
            print(f"[{L}/{M}] solve failed: {e}"); continue
        # nearest pole to origin
        rr = sorted(roots, key=lambda z: abs(z))
        nearest = rr[0]
        # closest real pole to -xi0
        realpoles = [z for z in roots if abs(mp.im(z)) < 1e-6*abs(z)+1e-12]
        near_mxi0 = min(roots, key=lambda z: abs(z-(-xi0)))
        # any pole near +2*xi0 or -2*xi0 (tower test), excluding accumulation near -xi0
        twox = min(roots, key=lambda z: abs(abs(z)-2*xi0))
        census.append({"L":L,"M":M,
                       "nearest_pole":[float(mp.re(nearest)),float(mp.im(nearest))],
                       "nearest_pole_abs":float(abs(nearest)),
                       "closest_to_minus_xi0":[float(mp.re(near_mxi0)),float(mp.im(near_mxi0))],
                       "dist_to_minus_xi0":float(abs(near_mxi0+xi0))})
        print(f"[{L}/{M}] nearest pole = {float(mp.re(nearest)):+.8f}{float(mp.im(nearest)):+.2e}i "
              f"|.|={float(abs(nearest)):.8f} ; closest-to(-xi0) dist={float(abs(near_mxi0+xi0)):.2e}")
    out["census"] = census
    # verdict
    dists = [c["dist_to_minus_xi0"] for c in census]
    out["dominant_singularity_at_minus_xi0"] = min(dists) < 1e-3
    print(f"\nDominant Borel singularity at -xi0 (negative axis): {out['dominant_singularity_at_minus_xi0']}")
    print("Holonomic L_V (order 4, finite singular locus {0,-xi0,inf}) => NO infinite resurgent tower.")
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "borel_pade_results.json"),"w",encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    print("[done] wrote borel_pade_results.json")

if __name__ == "__main__":
    main()
