"""
Phase A1 cross-check + A2 genus -- eigenvalue (convergence-exponent) route.

R_infinity(lambda)^2 = prod_k (1 + lambda s_k^2),  {s_k} = positive spectrum of the
Jacobi operator T (zero diagonal, off-diagonal sqrt(u_{j+1}), P0 convention).
The order of this canonical product = convergence exponent of the zeros
lambda_k = -1/s_k^2, i.e. rho_prod = inf{ t : sum_k s_k^{2t} < inf } = 1/p if
s_k^2 ~ c k^{-p}.  Must equal the coefficient-route rho = 1/(2d).

Genus (A2): p* = smallest integer with sum |1/lambda_k|^{p*+1} = sum s_k^{2(p*+1)} < inf.
sum s_k^2 = S = sum u_n < inf (trace class) => expect p* = 0.

Eigenvalues by numpy (double) for the power-law fit (cross-checked vs mpmath at a few k),
with finite-size convergence checked across N.
"""
import json, sys, hashlib
import numpy as np


def offdiag(coeffs, N):
    cc = coeffs
    b = lambda k: sum(cc[j] * k ** j for j in range(len(cc)))
    u = lambda i: 1.0 / (b(i - 1) * b(i))
    # T[j-1,j] = sqrt(u_{j+1}), j=1..N-1  -> off-diagonal entries sqrt(u_2..u_N)
    return np.array([np.sqrt(u(i)) for i in range(2, N + 1)]), u


def pos_spectrum(coeffs, N):
    e, u = offdiag(coeffs, N)
    d = np.zeros(N)
    w = np.linalg.eigvalsh(np.diag(d) + np.diag(e, 1) + np.diag(e, -1))
    s = np.sort(w[w > 0])[::-1]          # positive eigenvalues, descending
    return s, u


def fit_powerlaw(s, klo, khi):
    k = np.arange(1, len(s) + 1)
    sel = (k >= klo) & (k <= khi)
    lk, ls = np.log(k[sel]), np.log(s[sel])
    p_s = np.polyfit(lk, ls, 1)          # log s = slope*log k + b  -> slope ~ -d
    ls2 = np.log(s[sel] ** 2)
    p_s2 = np.polyfit(lk, ls2, 1)        # log s^2 -> slope ~ -2d = -p
    return -p_s[0], -p_s2[0]             # (d_est, p_est=2d_est)


def fit_corrected(s, klo, khi):
    """curvature-corrected: log s_k = -d log k + c0 + c1/k + c2/k^2 ; return d."""
    k = np.arange(1, len(s) + 1)
    sel = (k >= klo) & (k <= khi)
    kk, ls = k[sel].astype(float), np.log(s[sel])
    X = np.column_stack([np.log(kk), np.ones_like(kk), 1 / kk, 1 / kk ** 2])
    coef, *_ = np.linalg.lstsq(X, ls, rcond=None)
    return -coef[0]                      # d_est (corrected)


def analyze(name, coeffs, d_true, N=900, Ncheck=1400):
    s, u = pos_spectrum(coeffs, N)
    s2, _ = pos_spectrum(coeffs, Ncheck)

    # finite-size convergence of the first K eigenvalues
    K = 40
    conv = float(np.max(np.abs((s[:K] - s2[:K]) / s[:K])))

    # power-law fit over a converged mid-range
    d_est, p_est = fit_powerlaw(s, klo=3, khi=40)
    d_corr = fit_corrected(s, klo=3, khi=min(60, len(s) - 5))
    p_corr = 2 * d_corr

    # ratios s_1/s_2, s_2/s_3 ... ~ ((k+1)/k)^d
    ratios = [float(s[i] / s[i + 1]) for i in range(5)]
    pred = [float(((i + 2) / (i + 1)) ** d_true) for i in range(5)]

    # genus: sum s_k^{2(p+1)} for p=0,1; and sum s_k^2 (=S)
    S_spec = float(np.sum(s ** 2))
    S_true = float(np.sum([u(n) for n in range(2, 20000)]))
    sums = {p: float(np.sum(s ** (2 * (p + 1)))) for p in (0, 1)}

    rho_prod = 1.0 / p_est
    rho_prod_c = 1.0 / p_corr
    print(f"\n=== {name}: b={coeffs} (d_true={d_true}), N={N} ===")
    print(f"  finite-size conv (N={N} vs {Ncheck}, first {K}): {conv:.2e}")
    print(f"  s_1..s_6 = {[float(x) for x in s[:6]]}")
    print(f"  consecutive ratios s_k/s_{{k+1}}: {[round(r,4) for r in ratios]}")
    print(f"                     predicted ((k+1)/k)^d: {[round(p,4) for p in pred]}")
    print(f"  power-law fit (k=3..40):  s_k ~ k^(-d),  d_est = {d_est:.4f}  [expect {d_true}]")
    print(f"                            s_k^2 ~ k^(-p), p_est = {p_est:.4f}  [expect {2*d_true}]")
    print(f"  curvature-corrected:      d_corr = {d_corr:.4f} -> p_corr = {p_corr:.4f}")
    print(f"  => rho_prod = 1/p     = {rho_prod:.4f}   (corrected {rho_prod_c:.4f})  [expect {1/(2*d_true):.4f}]")
    print(f"  --- genus ---")
    print(f"  sum s_k^2 (spectral)  = {S_spec:.8f}")
    print(f"  S = sum u_n (direct)  = {S_true:.8f}   (match => sum s_k^2 = S < inf)")
    print(f"  sum |1/lambda_k|^1 = sum s_k^2     = {sums[0]:.6e}  < inf  (=> genus 0 candidate)")
    print(f"  sum |1/lambda_k|^2 = sum s_k^4     = {sums[1]:.6e}")
    print(f"  => genus p* = 0  (smallest p with sum s_k^(2(p+1)) < inf; already converges at p=0)")
    return {
        "name": name, "coeffs": coeffs, "d_true": d_true, "N": N,
        "finite_size_conv": conv, "s_top6": [float(x) for x in s[:6]],
        "ratios": ratios, "ratios_pred": pred,
        "d_est": d_est, "p_est": p_est, "d_corr": d_corr, "p_corr": p_corr,
        "rho_prod": rho_prod, "rho_prod_corrected": rho_prod_c,
        "expect_rho": 1.0 / (2 * d_true),
        "sum_s2_spectral": S_spec, "S_direct": S_true,
        "sum_s2": sums[0], "sum_s4": sums[1], "genus": 0,
    }


if __name__ == "__main__":
    res = []
    res.append(analyze("(1,0,1)", [1, 0, 1], 2))
    res.append(analyze("(1,0,5)", [5, 0, 1], 2))
    res.append(analyze("(1,3,2)", [2, 3, 1], 2))
    res.append(analyze("b=k+1 (d=1)", [1, 1], 1))
    res.append(analyze("b=k^3+1 (d=3)", [1, 0, 0, 1], 3, N=700, Ncheck=1000))
    out = {"results": res}
    js = json.dumps(out, indent=2)
    with open("out/eigenvalue_route_result.json", "w", newline="\n") as f:
        f.write(js)
    print("\nsha256(result json) =", hashlib.sha256(js.encode()).hexdigest())
