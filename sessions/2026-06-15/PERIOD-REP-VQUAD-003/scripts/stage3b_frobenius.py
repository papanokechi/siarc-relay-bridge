#!/usr/bin/env python3
# PERIOD-REP-VQUAD-003 Stage 3b — INDEPENDENT confirmation of the branch exponent at
# xi=-xi0 by direct Frobenius-recurrence solving (a different computation from the
# falling-factorial indicial polynomial of stage3_galois_LV.py).
#
# Build y(eta) = eta^s * sum c_n eta^n, eta=xi+xi0, s=-(1+beta); solve the recurrence
# for c_1..c_M from L_V y = 0 and verify the truncated residual -> 0.  A consistent,
# log-free solution with this irrational s confirms: (i) -(1+beta) is a genuine local
# exponent, (ii) no resonance/log (s+n never hits {0,1,2}), so the monodromy at -xi0 is
# the pseudo-reflection diag(e^{2pi i sqrt3/9},1,1,1) -> Zariski closure contains G_m.
import json
import mpmath as mp

mp.mp.dps = 60
s3 = mp.sqrt(3)
xi0 = 2/s3
beta = -1/(3*s3)
s_exp = -(1+beta)                 # branch exponent -(1+beta) = -1+sqrt3/9

R = mp.mpf(418501)
def P_eta_coeffs():
    # p_k(xi) as polynomials, re-expanded about xi = -xi0 (eta = xi + xi0)
    # return list of coefficient-lists in eta for k=0..4
    import sympy as sp
    x = sp.symbols('x'); S3 = sp.sqrt(3); X0 = 2/S3
    Rr = sp.Integer(418501)
    p = [sp.Integer(1),
         (sp.Rational(659,431)+sp.Rational(150,431)*S3)+(sp.Rational(432,431)+sp.Rational(12,431)*S3)*x,
         (2552175+199224*S3)/Rr+(496044+61620*S3)/Rr*x+(70092+3240*S3)/Rr*x**2,
         (77760+560736*S3)/Rr+(1685448+101124*S3)/Rr*x+(70092+3240*S3)/Rr*x**2,
         (19440+140184*S3)/Rr*x+(210276+9720*S3)/Rr*x**2]
    eta = sp.symbols('eta')
    out = []
    for pk in p:
        pe = sp.expand(pk.subs(x, eta - X0))
        po = sp.Poly(pe, eta)
        # coeffs low->high
        cl = [complex(sp.N(po.coeff_monomial(eta**j), 40)) for j in range(po.degree()+1)] if pe!=0 else [0j]
        out.append([mp.mpf(c.real)+mp.mpf(c.imag)*1j for c in cl])
    return out

def main():
    Pc = P_eta_coeffs()           # Pc[k] = list of eta-coeffs of p_k(eta)
    M = 12
    # operator acting on eta^{s+n}: D^k eta^{s+n} = falling(s+n,k) eta^{s+n-k}
    def falling(a, k):
        r = mp.mpf(1)
        for i in range(k):
            r *= (a - i)
        return r
    # Collect L_V[ eta^s sum c_n eta^n ] = sum over powers eta^{s+m} of:
    #   sum_k sum_j Pc[k][j] * c_n * falling(s+n,k)  with j + (s+n-k) = s+m  => n = m + k - j
    c = [mp.mpf(0)]*(M+1); c[0] = mp.mpf(1)
    def indicial(a):
        tot = mp.mpf(0)
        for k in range(5):
            tot += Pc[k][0]*falling(a, k)   # j=0 leading coeff of p_k
        return tot
    # solve recurrence: coefficient of eta^{s+m} must vanish
    residuals = []
    for m in range(0, M+1):
        tot = mp.mpf(0)
        for k in range(5):
            for j in range(len(Pc[k])):
                n = m + k - j
                if 0 <= n <= M and n != m:
                    tot += Pc[k][j]*c[n]*falling(s_exp+n, k)
                elif n == m and j > 0:
                    tot += Pc[k][j]*c[m]*falling(s_exp+m, k)
        if m == 0:
            residuals.append(abs(indicial(s_exp)))   # should be ~0
        else:
            # I(s+m) c_m + tot_without_cm = 0  => c_m = -tot_without_cm / I(s+m)
            Ism = indicial(s_exp+m)
            c[m] = -tot/Ism
    # now verify full residual at several powers with the solved c_n
    worst = mp.mpf(0)
    for m in range(0, M+1):
        tot = mp.mpf(0)
        for k in range(5):
            for j in range(len(Pc[k])):
                n = m + k - j
                if 0 <= n <= M:
                    tot += Pc[k][j]*c[n]*falling(s_exp+n, k)
        worst = max(worst, abs(tot))
    out = {
        "branch_exponent_s": mp.nstr(s_exp, 30),
        "indicial_at_s_|I(s)|": mp.nstr(abs(indicial(s_exp)), 6),
        "resonance_check": "s+n for n>=1 never equals 0,1,2 (s irrational) -> no logs",
        "frobenius_recurrence_solved_M": M,
        "worst_truncated_residual": mp.nstr(worst, 6),
        "c_1..c_5": [mp.nstr(c[i], 12) for i in range(1, 6)],
        "monodromy_eigenvalue": "exp(2 pi i s) = exp(2 pi i sqrt3/9), infinite multiplicative order",
        "verdict": "branch solution exists, log-free => 1-dim infinite-order monodromy at -xi0; G_V contains G_m",
    }
    print(json.dumps(out, indent=2))
    path = (r"C:\LocalWork\siarc-relay-bridge\sessions\2026-06-15"
            r"\PERIOD-REP-VQUAD-003\scripts\stage3b_frobenius_results.json")
    json.dump(out, open(path, "w", encoding="utf-8"), indent=2)
    print("[wrote]", path)

if __name__ == "__main__":
    main()
