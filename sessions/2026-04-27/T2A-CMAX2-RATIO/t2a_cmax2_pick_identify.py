"""
T2A-CMAX2-PICK-IDENTIFY — basis-identify the 3 Trans-hard picks
with ratio != 1 (Step 6). Recompute at dps=300 K_2000, run PSLQ
against bases A-E (per T2A-BASIS-IDENTIFY pattern), with mandatory
L-coefficient != 0 phantom defense.
"""
import json
import time
from pathlib import Path

import mpmath as mp


PICKS = json.load(open("t2a_cmax2_ratio_picks.json"))
DPS = 300
ITER = 2000
TOL = mp.mpf(10) ** (-80)
HMAX = 10**14


def kn_mp(a4, a3, a2, a1, a0, b2, b1, b0, N, dps):
    mp.mp.dps = dps
    b_at_0 = mp.mpf(b0)
    b_at_1 = mp.mpf(b2 + b1 + b0)
    a_at_1 = mp.mpf(a4 + a3 + a2 + a1 + a0)
    P_prev2 = b_at_0
    P_prev1 = b_at_1 * b_at_0 + a_at_1
    Q_prev2 = mp.mpf(1)
    Q_prev1 = b_at_1
    K_prev = K_curr = None
    for n in range(2, N + 1):
        an = a4*n*n*n*n + a3*n*n*n + a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        P_curr = bn * P_prev1 + an * P_prev2
        Q_curr = bn * Q_prev1 + an * Q_prev2
        if Q_curr == 0:
            return None
        K_prev = K_curr
        K_curr = P_curr / Q_curr
        if n % 16 == 0:
            mag = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
            P_curr /= mag; Q_curr /= mag
            P_prev1 /= mag; Q_prev1 /= mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def try_pslq(name, basis, l_index, log):
    rel = mp.pslq(basis, maxcoeff=HMAX, tol=TOL)
    if rel is None:
        log.append((name, "MISS"))
        return None
    if int(rel[l_index]) == 0:
        log.append((name, "PHANTOM", [int(x) for x in rel]))
        return None
    log.append((name, "HIT", [int(x) for x in rel]))
    return rel


def identify(L):
    pi = mp.pi
    log2 = mp.log(2)
    log3 = mp.log(3)
    z3 = mp.zeta(3)
    z5 = mp.zeta(5)
    cat = mp.catalan
    sqrt2 = mp.sqrt(2)
    sqrt3 = mp.sqrt(3)
    sqrt5 = mp.sqrt(5)

    log = []
    findings = []

    # A: standard transcendentals (L at index 0)
    A = [L, mp.mpf(1), pi, pi**2, log2, log3, z3, z5, cat]
    rel = try_pslq("A_standard", A, 0, log)
    if rel: findings.append(("A_standard", [int(x) for x in rel]))

    # B: elliptic / AGM
    K_lemn = mp.ellipk(mp.mpf("0.5"))   # K(1/2)
    E_lemn = mp.ellipe(mp.mpf("0.5"))
    B = [L, mp.mpf(1), pi, K_lemn, E_lemn, mp.exp(1)]
    rel = try_pslq("B_elliptic", B, 0, log)
    if rel: findings.append(("B_elliptic", [int(x) for x in rel]))

    # C: ₂F₁ / Clausen-like (numerical samples)
    cl2 = mp.clsin(2, mp.pi/3)            # Clausen at pi/3
    f21_half = mp.hyp2f1(mp.mpf("0.5"), mp.mpf("0.5"),
                         mp.mpf(1), mp.mpf("0.5"))
    C = [L, mp.mpf(1), pi, cl2, f21_half, log2]
    rel = try_pslq("C_2F1_Clausen", C, 0, log)
    if rel: findings.append(("C_2F1_Clausen", [int(x) for x in rel]))

    # D: algebraic * pi^2
    D = [L, mp.mpf(1)*pi*pi, sqrt2*pi*pi, sqrt3*pi*pi,
         sqrt5*pi*pi, pi*pi/2, pi*pi/3, pi*pi/4, pi*pi/5]
    rel = try_pslq("D_alg_times_pi2", D, 0, log)
    if rel: findings.append(("D_alg_times_pi2", [int(x) for x in rel]))

    # Dp: algebraic * pi
    Dp = [L, pi, sqrt2*pi, sqrt3*pi, sqrt5*pi,
          pi/2, pi/3, pi/4]
    rel = try_pslq("Dp_alg_times_pi", Dp, 0, log)
    if rel: findings.append(("Dp_alg_times_pi", [int(x) for x in rel]))

    # Da: algebraic deg <= 8 (no transcendentals; tests if L itself algebraic)
    Da = [L, L*L, L*L*L, L*L*L*L, mp.mpf(1)]
    rel = try_pslq("Da_algebraic", Da, 0, log)
    if rel: findings.append(("Da_algebraic", [int(x) for x in rel]))

    return findings, log


def main():
    print(f"[STEP 6] Identifying {len(PICKS)} ratio!=1 Trans-hard picks")
    t0 = time.time()
    out = []
    for i, p in enumerate(PICKS):
        a = p["coeffs_a"]; b = p["coeffs_b"]
        ratio = p["a4_b2sq_ratio"]
        print(f"\n[Pick {i+1}] a={a} b={b} ratio={ratio}")
        Kn, Kn_1 = kn_mp(*a, *b, ITER, DPS)
        diff = abs(Kn - Kn_1)
        L_str = mp.nstr(Kn, 60)
        print(f"  L = {L_str}")
        print(f"  |diff| = {mp.nstr(diff, 4)}")

        mp.mp.dps = 100
        findings, log = identify(Kn)
        for entry in log:
            print(f"  {entry}")
        out.append({
            "pick_index": i+1,
            "coeffs_a": a, "coeffs_b": b,
            "ratio": ratio,
            "L_dps300": L_str,
            "diff": mp.nstr(diff, 4),
            "findings": [(name, rel) for name, rel in findings],
            "pslq_log": [list(e) for e in log],
        })

    summary = {"picks": out, "elapsed_sec": time.time()-t0}
    Path("t2a_cmax2_pick_identify_results.json").write_text(
        json.dumps(summary, indent=2))
    print(f"\n[DONE] elapsed={time.time()-t0:.1f}s")
    print(f"any_hits = {sum(1 for p in out if p['findings'])}/"
          f"{len(out)}")


if __name__ == "__main__":
    main()
