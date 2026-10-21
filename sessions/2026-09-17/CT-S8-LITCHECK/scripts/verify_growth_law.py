"""CT-S8-LITCHECK: numerical check of results 1-3 for Q_n = b(n)Q_{n-1} + Q_{n-2}.

Claimed:
  (1) lim |Q_n/(dn)!|^{1/n} = |beta_d|/d^d
  (2) Q_n/Gamma(dn+1) = K (beta_d/d^d)^n n^s (1+O(1/n)),  s = beta_{d-1}/beta_d + (d-1)/2
  (3) K = r_inf (2pi)^{(d-1)/2} / ( sqrt(d) * prod_i Gamma(1-r_i) ),  b(n)=beta_d prod_i (n-r_i)

Run: python verify_growth_law.py
"""
import mpmath as mp

mp.mp.dps = 60


def run(betas, N=4000):
    d = len(betas) - 1
    b = lambda n: sum(mp.mpf(betas[k]) * mp.mpf(n) ** k for k in range(d + 1))
    Qm1, Q0 = mp.mpf(0), mp.mpf(1)
    P = mp.mpf(1)
    for n in range(1, N + 1):
        Qn = b(n) * Q0 + Qm1
        Qm1, Q0 = Q0, Qn
        P *= b(n)
    rinf = Q0 / P
    bd = mp.mpf(betas[d])
    bd1 = mp.mpf(betas[d - 1])
    s = bd1 / bd + mp.mpf(d - 1) / 2
    rho = bd / mp.mpf(d) ** d
    K_num = Q0 / mp.gamma(d * N + 1) / (rho ** N) / mp.mpf(N) ** s
    roots = mp.polyroots([mp.mpf(c) for c in reversed(betas)])
    K_th = rinf * (2 * mp.pi) ** (mp.mpf(d - 1) / 2) / (
        mp.sqrt(d) * mp.fprod([mp.gamma(1 - r) for r in roots])
    )
    root1 = mp.power(abs(Q0 / mp.gamma(d * N + 1)), mp.mpf(1) / N)
    return d, rinf, K_num, K_th, root1, abs(rho)


if __name__ == "__main__":
    for betas in [[3, 2], [1, 0, 1], [0, 1, 2], [2, 1, 1, 1]]:
        d, rinf, Kn, Kt, r1, rr = run(betas)
        print("beta", betas, "d", d)
        print("  r_inf            ", mp.nstr(rinf, 20))
        print("  K_numeric        ", mp.nstr(Kn, 20))
        print("  K_closed_form    ", mp.nstr(Kt, 20))
        print("  ratio            ", mp.nstr(Kn / Kt, 20))
        print("  |Q/(dn)!|^(1/n)  ", mp.nstr(r1, 12), " vs |beta_d|/d^d", mp.nstr(rr, 12))
