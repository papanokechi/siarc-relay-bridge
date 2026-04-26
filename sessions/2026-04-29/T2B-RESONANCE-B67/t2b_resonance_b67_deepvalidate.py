"""T2B-RESONANCE-B67 — Step 4 deep validation.

For each Log/Trans candidate from Stage B/C, recompute at
dps=150, K_1500, and run PSLQ against the 7-basis battery from
T2A-BASIS-IDENTIFY (A standard, B elliptic, C hypergeo,
D alg*pi^2, Dp alg*pi, Da algebraic deg-8, plus a Log-extension
basis). All checks require L-coefficient != 0 (phantom guard).
"""
from __future__ import annotations
import json
import time
from pathlib import Path

import mpmath as mp_

INPUT = Path(__file__).parent / "t2b_resonance_b67_results.json"
OUT = Path(__file__).parent / "t2b_resonance_b67_deepvalidate.json"

DPS_BIG = 150
N_ITER = 1500
DPS_PSLQ = 150
HMAX = 10**12
TOL_PSLQ = mp_.mpf(10) ** (-80)
RESID_THRESH = mp_.mpf(10) ** (-60)


def kn_mp_deg2(coeffs, N, dps):
    """deg-(2,1) PCF: a_n = a2 n^2 + a1 n + a0; b_n = b1 n + b0."""
    a2, a1, a0, b1, b0 = coeffs
    mp_.mp.dps = dps
    a2m, a1m, a0m, b1m, b0m = (mp_.mpf(c) for c in (a2, a1, a0, b1, b0))
    Pp = mp_.mpf(1)
    Pc = b0m
    Qp = mp_.mpf(0)
    Qc = mp_.mpf(1)
    K_curr = K_prev = None
    for n in range(1, N + 1):
        an = a2m * n * n + a1m * n + a0m
        bn = b1m * n + b0m
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if Qc == 0:
            return None
        K_prev = K_curr
        K_curr = Pc / Qc
        if n % 16 == 0:
            mag = max(abs(Pc), abs(Qc), mp_.mpf(1))
            Pc /= mag; Qc /= mag; Pp /= mag; Qp /= mag
    return (K_curr, K_prev)


def relation_residual(rel, basis):
    s = mp_.mpf(0)
    for c, x in zip(rel, basis):
        s += mp_.mpf(c) * x
    return abs(s)


def try_pslq(basis_vec, l_index=None):
    """l_index can be an int or a list of indices that all involve L
    (standalone or multiplied). Phantom guard requires AT LEAST ONE
    of those indices to have a nonzero relation coefficient."""
    try:
        rel = mp_.pslq(basis_vec, maxcoeff=HMAX, tol=TOL_PSLQ)
    except Exception as ex:
        return None, str(ex)[:80], None
    if rel is None:
        return None, "no relation", None
    res = relation_residual(rel, basis_vec)
    if res > RESID_THRESH:
        return None, f"residual {mp_.nstr(res, 3)} > 1e-60", None
    if l_index is not None:
        idxs = [l_index] if isinstance(l_index, int) else list(l_index)
        if all(rel[i] == 0 for i in idxs):
            return None, "phantom (no L-bearing coef)", mp_.nstr(res, 5)
    return [int(x) for x in rel], None, mp_.nstr(res, 5)


def main():
    t0 = time.time()
    data = json.loads(INPUT.read_text())
    candidates = list(data.get("trans_records", [])) + list(data.get("log_records", []))
    print(f"[STEP 4] Deep validation of {len(candidates)} candidates")
    print(f"  dps={DPS_BIG}  N={N_ITER}  PSLQ residual threshold 1e-60")

    mp_.mp.dps = DPS_BIG
    PI = mp_.pi
    LN2 = mp_.log(2)
    LN3 = mp_.log(3)
    LN5 = mp_.log(5)
    Z2 = mp_.zeta(2)
    Z3 = mp_.zeta(3)
    SQ2 = mp_.sqrt(2)
    SQ3 = mp_.sqrt(3)
    SQ5 = mp_.sqrt(5)
    SQ6 = mp_.sqrt(6)
    CBR2 = mp_.cbrt(2)
    CBR3 = mp_.cbrt(3)
    CAT = mp_.catalan
    EUL = mp_.euler
    AGM12 = mp_.agm(1, SQ2)
    AGM13 = mp_.agm(1, SQ3)
    KEL = mp_.ellipk(mp_.mpf("0.5"))

    findings = []
    for k, rec in enumerate(candidates):
        coeffs = rec["coeffs"]
        ratio = rec["ratio"]
        Lstage = rec["L"]
        print(f"\n  C{k+1}: ratio={ratio}  coeffs={coeffs}  L_50={Lstage}")
        t1 = time.time()
        res = kn_mp_deg2(coeffs, N_ITER, DPS_BIG)
        if res is None:
            print(f"    FAILED (Q=0)")
            findings.append({"rec": rec, "fail": "Q=0"})
            continue
        L, Lprev = res
        diff = abs(L - Lprev)
        print(f"    L_150 = {mp_.nstr(L, 60)}  |diff|={mp_.nstr(diff, 3)}  ({time.time()-t1:.1f}s)")

        out_rec = {
            "rec": rec,
            "L_150": mp_.nstr(L, 80),
            "tail_diff": mp_.nstr(diff, 5),
            "results": {},
        }
        # BASIS A — standard
        basis_A = [mp_.mpf(1), L, PI, PI**2, PI**3, PI**4,
                   LN2, LN3, LN5, Z2, Z3, SQ2, SQ3, SQ5, EUL]
        names_A = ["1","L","pi","pi^2","pi^3","pi^4",
                   "log2","log3","log5","zeta2","zeta3",
                   "sqrt2","sqrt3","sqrt5","euler"]
        rel, msg, resid = try_pslq(basis_A, l_index=1)
        out_rec["results"]["A_standard"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_A}
        # BASIS B — elliptic / AGM
        basis_B = [mp_.mpf(1), L, AGM12, AGM13, KEL, KEL**2, PI*KEL]
        names_B = ["1","L","agm(1,sqrt2)","agm(1,sqrt3)","K(0.5)","K(0.5)^2","pi*K(0.5)"]
        rel, msg, resid = try_pslq(basis_B, l_index=1)
        out_rec["results"]["B_elliptic"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_B}
        # BASIS C — hypergeometric / Clausen / Catalan
        H1 = mp_.hyp2f1(mp_.mpf(1)/2, mp_.mpf(1)/2, 1, mp_.mpf(1)/2)
        H2 = mp_.hyp2f1(mp_.mpf(1)/3, mp_.mpf(2)/3, 1, mp_.mpf(1)/2)
        CL2_S = mp_.clsin(2, PI/3)
        CL2_C = mp_.clcos(2, PI/3)
        basis_C = [mp_.mpf(1), L, H1, H2, CL2_S, CL2_C, CAT]
        names_C = ["1","L","2F1(1/2,1/2;1;1/2)","2F1(1/3,2/3;1;1/2)",
                   "Cl2_sin","Cl2_cos","Catalan"]
        rel, msg, resid = try_pslq(basis_C, l_index=1)
        out_rec["results"]["C_hypergeo"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_C}
        # BASIS D — L = (algebraic)*pi^2; L at index 0
        P2 = PI**2
        basis_D = [L, P2, SQ2*P2, SQ3*P2, SQ5*P2, SQ6*P2, CBR2*P2, CBR3*P2]
        names_D = ["L","pi^2","sqrt2*pi^2","sqrt3*pi^2","sqrt5*pi^2",
                   "sqrt6*pi^2","cbrt2*pi^2","cbrt3*pi^2"]
        rel, msg, resid = try_pslq(basis_D, l_index=0)
        out_rec["results"]["D_alg_times_pi2"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_D}
        # BASIS Dp — L = (algebraic)*pi
        basis_Dp = [L, PI, SQ2*PI, SQ3*PI, SQ5*PI]
        names_Dp = ["L","pi","sqrt2*pi","sqrt3*pi","sqrt5*pi"]
        rel, msg, resid = try_pslq(basis_Dp, l_index=0)
        out_rec["results"]["Dp_alg_times_pi"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_Dp}
        # BASIS Da — L algebraic deg-8
        basis_Da = [mp_.mpf(1), L, L*L, L**3, L**4, L**5, L**6, L**7, L**8]
        names_Da = ["1","L","L^2","L^3","L^4","L^5","L^6","L^7","L^8"]
        rel, msg, resid = try_pslq(basis_Da, l_index=1)
        out_rec["results"]["Da_algebraic_deg8"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_Da}
        # BASIS LogExt — L = (rational)/log(p) candidates
        # L appears at index 4 (alone) and indices 0,1,2 (L*log p).
        basis_Le = [L*LN2, L*LN3, L*LN5, mp_.mpf(1), L]
        names_Le = ["L*log2","L*log3","L*log5","1","L"]
        rel, msg, resid = try_pslq(basis_Le, l_index=[0, 1, 2, 4])
        out_rec["results"]["Le_logext"] = {"hit": rel, "msg": msg, "resid": resid, "names": names_Le}

        # Print summary
        for bname, rd in out_rec["results"].items():
            if rd["hit"] is not None:
                print(f"    HIT {bname}: {rd['hit']}  resid={rd['resid']}")

        findings.append(out_rec)

    summary = {
        "task": "T2B-RESONANCE-B67 step 4 deep validation",
        "dps": DPS_BIG,
        "n_iter": N_ITER,
        "n_candidates": len(candidates),
        "findings": findings,
        "wall_seconds": round(time.time() - t0, 2),
    }
    OUT.write_text(json.dumps(summary, indent=2, default=str))
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
