"""T2A-BASIS-IDENTIFY — identify the basis for 5 representative
degree-(4,2) Trans-hard limits."""
from __future__ import annotations
import json, time, hashlib
from pathlib import Path
import mpmath as mp

INPUT = Path("t2a_degree42_results.json")
OUT   = Path("t2a_basis_identify_results.json")
MYST  = Path("t2a_mystery_constant.txt")

DPS_BIG  = 300
N_ITER   = 2000
DPS_PSLQ = 300
HMAX     = 10**12
TOL_PSLQ = mp.mpf(10) ** (-100)
RESID_THRESH = mp.mpf(10) ** (-80)


def kn_mp(a4, a3, a2, a1, a0, b2, b1, b0, N, dps):
    mp.mp.dps = dps
    b_at_0 = mp.mpf(b0); b_at_1 = mp.mpf(b2 + b1 + b0)
    a_at_1 = mp.mpf(a4 + a3 + a2 + a1 + a0)
    P_prev2 = b_at_0; P_prev1 = b_at_1 * b_at_0 + a_at_1
    Q_prev2 = mp.mpf(1); Q_prev1 = b_at_1
    K_curr = K_prev = None
    for n in range(2, N + 1):
        an = a4*n*n*n*n + a3*n*n*n + a2*n*n + a1*n + a0
        bn = b2*n*n + b1*n + b0
        P_curr = bn * P_prev1 + an * P_prev2
        Q_curr = bn * Q_prev1 + an * Q_prev2
        if Q_curr == 0:
            return None
        K_prev = K_curr; K_curr = P_curr / Q_curr
        if n % 16 == 0:
            mag = max(abs(P_curr), abs(Q_curr), mp.mpf(1))
            P_curr /= mag; Q_curr /= mag
            P_prev1 /= mag; Q_prev1 /= mag
        P_prev2, P_prev1 = P_prev1, P_curr
        Q_prev2, Q_prev1 = Q_prev1, Q_curr
    return (K_curr, K_prev)


def relation_residual(rel, basis):
    s = mp.mpf(0)
    for c, x in zip(rel, basis):
        s += mp.mpf(c) * x
    return abs(s)


def try_pslq(basis_vec, name="", l_index=None):
    """PSLQ on basis_vec; require residual<1e-80; if l_index is given,
    require rel[l_index] != 0 (rejects basis-internal identities)."""
    try:
        rel = mp.pslq(basis_vec, maxcoeff=HMAX, tol=TOL_PSLQ)
    except Exception as ex:
        return None, str(ex)[:80], None
    if rel is None:
        return None, "no relation", None
    res = relation_residual(rel, basis_vec)
    if res > RESID_THRESH:
        return None, f"residual {mp.nstr(res,3)} > 1e-80", None
    if l_index is not None and rel[l_index] == 0:
        return None, "basis-internal identity (L-coef=0)", mp.nstr(res, 5)
    return [int(x) for x in rel], None, mp.nstr(res, 5)


def main():
    t0 = time.time()
    # --- STEP 1: load and select 5 reps spread by |L| ---
    data = json.load(open(INPUT))
    cand = data["trans_families"]
    triples = []
    for r in cand:
        try:
            L = float(r["limit"])
        except Exception:
            continue
        if abs(L) > 0.1:
            triples.append((L, r))
    triples.sort(key=lambda x: abs(x[0]))
    n = len(triples)
    idxs = [0, n // 4, n // 2, 3 * n // 4, n - 1]
    reps = [triples[i][1] for i in idxs]

    print("[STEP 1] 5 representatives (|L|>0.1, spread by magnitude):")
    for k, r in enumerate(reps):
        print(f"  R{k+1}: a={r['coeffs_a']} b={r['coeffs_b']}  L_50={r['limit'][:32]}")

    # --- STEP 2: recompute at dps=300 K_2000 ---
    print(f"\n[STEP 2] Recompute at dps={DPS_BIG}, K_{N_ITER}")
    mp.mp.dps = DPS_BIG
    PI = mp.pi
    LN2 = mp.log(2); LN3 = mp.log(3); LN5 = mp.log(5)
    Z2 = mp.zeta(2); Z3 = mp.zeta(3); Z5 = mp.zeta(5)
    SQ2 = mp.sqrt(2); SQ3 = mp.sqrt(3); SQ5 = mp.sqrt(5); SQ6 = mp.sqrt(6)
    PHI = (1 + SQ5) / 2
    CBR2 = mp.cbrt(2); CBR3 = mp.cbrt(3)
    EUL = mp.euler
    AGM12 = mp.agm(1, SQ2)
    AGM13 = mp.agm(1, SQ3)
    KEL = mp.ellipk(mp.mpf("0.5"))
    H1 = mp.hyp2f1(mp.mpf(1)/2, mp.mpf(1)/2, 1, mp.mpf(1)/2)
    H2 = mp.hyp2f1(mp.mpf(1)/3, mp.mpf(2)/3, 1, mp.mpf(1)/2)
    CL2_S = mp.clsin(2, PI / 3)
    CL2_C = mp.clcos(2, PI / 3)
    CAT = mp.catalan

    big_limits = []
    for k, r in enumerate(reps):
        a = r["coeffs_a"]; b = r["coeffs_b"]
        t1 = time.time()
        res = kn_mp(a[0], a[1], a[2], a[3], a[4],
                    b[0], b[1], b[2], N_ITER, DPS_BIG)
        if res is None:
            print(f"  R{k+1}: FAILED (Q=0)"); big_limits.append(None); continue
        K_curr, K_prev = res
        diff = abs(K_curr - K_prev)
        big_limits.append(K_curr)
        print(f"  R{k+1}: L = {mp.nstr(K_curr, 50)}  |diff|={mp.nstr(diff,3)}  ({time.time()-t1:.1f}s)")

    # --- STEP 3: PSLQ battery ---
    print(f"\n[STEP 3] PSLQ battery (residual threshold 1e-80)")
    findings = []
    for k, L in enumerate(big_limits):
        rec = {"rep": k + 1,
               "coeffs_a": reps[k]["coeffs_a"],
               "coeffs_b": reps[k]["coeffs_b"],
               "L_300": mp.nstr(L, 80) if L is not None else None,
               "results": {}}
        if L is None:
            findings.append(rec); continue

        # BASIS A.  L is at index 1.
        basis_A = [mp.mpf(1), L, PI, PI**2, PI**3, PI**4,
                   LN2, LN3, LN5, Z3, Z5, SQ2, SQ3, SQ5, EUL]
        names_A = ["1","L","pi","pi^2","pi^3","pi^4",
                   "log2","log3","log5","zeta3","zeta5",
                   "sqrt2","sqrt3","sqrt5","euler"]
        rel, msg, resid = try_pslq(basis_A, "A", l_index=1)
        rec["results"]["A_standard"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_A}
        # BASIS B (elliptic / AGM)
        basis_B = [mp.mpf(1), L, AGM12, AGM13, KEL, KEL**2, PI*KEL]
        names_B = ["1","L","agm(1,sqrt2)","agm(1,sqrt3)","K(0.5)","K(0.5)^2","pi*K(0.5)"]
        rel, msg, resid = try_pslq(basis_B, "B", l_index=1)
        rec["results"]["B_elliptic"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_B}
        # BASIS C (hypergeometric / Clausen)
        basis_C = [mp.mpf(1), L, H1, H2, CL2_S, CL2_C, CAT]
        names_C = ["1","L","2F1(1/2,1/2;1;1/2)","2F1(1/3,2/3;1;1/2)",
                   "Cl2(pi/3)_sin","Cl2(pi/3)_cos","Catalan"]
        rel, msg, resid = try_pslq(basis_C, "C", l_index=1)
        rec["results"]["C_hypergeo"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_C}
        # BASIS D — L = (algebraic) * pi^2.  phi removed (= (1+sqrt5)/2).  L at index 0.
        P2 = PI**2
        basis_D = [L, P2, SQ2*P2, SQ3*P2, SQ5*P2, SQ6*P2, CBR2*P2, CBR3*P2]
        names_D = ["L","pi^2","sqrt2*pi^2","sqrt3*pi^2","sqrt5*pi^2",
                   "sqrt6*pi^2","cbrt2*pi^2","cbrt3*pi^2"]
        rel, msg, resid = try_pslq(basis_D, "D", l_index=0)
        rec["results"]["D_alg_times_pi2"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_D}
        # L = alg * pi.  phi removed.  L at index 0.
        basis_Dp = [L, PI, SQ2*PI, SQ3*PI, SQ5*PI]
        names_Dp = ["L","pi","sqrt2*pi","sqrt3*pi","sqrt5*pi"]
        rel, msg, resid = try_pslq(basis_Dp, "Dp", l_index=0)
        rec["results"]["Dp_alg_times_pi"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_Dp}
        # And L = alg (rational/algebraic only)
        basis_Da = [mp.mpf(1), L, L*L, L*L*L, L**4, L**5, L**6, L**7, L**8]
        names_Da = ["1","L","L^2","L^3","L^4","L^5","L^6","L^7","L^8"]
        rel, msg, resid = try_pslq(basis_Da, "Da", l_index=1)
        rec["results"]["Da_algebraic_deg8"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_Da}

        findings.append(rec)

    # BASIS E — pairwise ratios
    print(f"\n[STEP 3-E] pairwise PSLQ on L_i / L_j against simple algebraic basis")
    pairwise = []
    for i in range(len(big_limits)):
        for j in range(i + 1, len(big_limits)):
            Li, Lj = big_limits[i], big_limits[j]
            if Li is None or Lj is None: continue
            ratio = Li / Lj
            # PSLQ: ratio against [1, sqrt2, sqrt3, sqrt5, cbrt2, cbrt3]
            # phi removed (= (1+sqrt5)/2 is dependent on {1, sqrt5}).
            # ratio is at index 0; require ratio-coefficient nonzero.
            v = [ratio, mp.mpf(1), SQ2, SQ3, SQ5, CBR2, CBR3]
            rel, msg, resid = try_pslq(v, f"E[{i+1},{j+1}]", l_index=0)
            pairwise.append({
                "i": i+1, "j": j+1,
                "ratio": mp.nstr(ratio, 30),
                "hit": rel, "msg": msg, "resid": resid,
                "names": ["L_i/L_j","1","sqrt2","sqrt3","sqrt5","cbrt2","cbrt3"],
            })

    # --- STEP 4: interpret ---
    summary_lines = []
    for rec in findings:
        hits = {k: v for k, v in rec["results"].items() if v["hit"] is not None}
        if hits:
            for bname, h in hits.items():
                summary_lines.append(f"R{rec['rep']}: HIT in {bname} -> {h['hit']} resid={h['resid']}")
        else:
            summary_lines.append(f"R{rec['rep']}: MISS in all bases")

    print("\n[STEP 4] Per-rep findings:")
    for ln in summary_lines:
        print("  " + ln)

    print("\n[STEP 4-E] Pairwise ratio findings:")
    for p in pairwise:
        if p["hit"] is not None:
            print(f"  L_{p['i']}/L_{p['j']} = {p['ratio'][:30]}  HIT {p['hit']} resid={p['resid']}")
        else:
            print(f"  L_{p['i']}/L_{p['j']} = {p['ratio'][:30]}  MISS")

    all_miss = all(rec["results"] and not any(v["hit"] for v in rec["results"].values())
                   for rec in findings if rec["L_300"])
    if all_miss and big_limits[0] is not None:
        # save 300-digit mystery constant
        with open(MYST, "w", encoding="utf-8") as f:
            f.write(f"# T2A degree-(4,2) Trans-hard mystery constant (R1)\n")
            f.write(f"# coeffs_a = {findings[0]['coeffs_a']}\n")
            f.write(f"# coeffs_b = {findings[0]['coeffs_b']}\n")
            f.write(f"# dps=300, K_2000\n")
            f.write(mp.nstr(big_limits[0], 300) + "\n")
        print(f"\n[STEP 4] All bases miss for all 5 -> wrote {MYST}")

    out = {
        "task": "T2A-BASIS-IDENTIFY",
        "dps_recompute": DPS_BIG, "iter_recompute": N_ITER,
        "dps_pslq": DPS_PSLQ, "hmax": HMAX,
        "residual_threshold": "1e-80",
        "representatives": findings,
        "pairwise_ratios": pairwise,
        "all_bases_missed": all_miss,
        "elapsed_total_sec": time.time() - t0,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    h = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    print(f"\n[DONE] wrote {OUT}  sha256={h}  elapsed={time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
