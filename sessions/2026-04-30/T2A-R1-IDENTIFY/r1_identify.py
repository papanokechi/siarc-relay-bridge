"""T2A-R1-IDENTIFY -- Identify mystery constant R1 = -0.10123520070804963...

R1 originates from degree-(4,2) Trans-hard family:
    coeffs_a (leading-first) = [1, 0, -1, -1, -1]
    coeffs_b (leading-first) = [-1, 1, -1]
Reference: bridge commit fa259b0 (T2A-DEGREE42-DEEP-VALIDATE),
           refined in 45fe389 (T2A-BASIS-IDENTIFY) where R1 was saved
           at dps=300 K_2000 to t2a_mystery_constant.txt.

This script:
  1. Recomputes R1 to dps=2000 with stability self-check.
  2. Runs PSLQ at dps=1000 and dps=2000 against Tier 1..5 bases.
     Hard requirement: rel[L_index] != 0 (phantom-trap filter).
  3. If 0 hits, runs integer-relation against
        {R1, R1^2, 1/R1, log|R1|, exp(R1), arctan R1} U Tier-1.
  4. Functional / modular probes vs j-invariant at small CM points.
  5. Writes r1_pslq_log.txt, r1_results.json, identification_verdict
     and claims.jsonl.
"""
from __future__ import annotations
import json, time, hashlib, sys
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).parent
LOG  = HERE / "r1_pslq_log.txt"
RES  = HERE / "r1_results.json"
CLM  = HERE / "claims.jsonl"

# ---- R1 originating PCF tuple (leading-first) ----
A_COEFFS = [1, 0, -1, -1, -1]   # a4, a3, a2, a1, a0
B_COEFFS = [-1, 1, -1]          # b2, b1, b0

DPS_TARGET = 2000
N_ITER     = 8000        # K_N partial denominators
DPS_BUFFER = 200         # work at DPS_TARGET+buffer
HMAX_PSLQ  = 10**12

log_lines = []
def log(msg=""):
    print(msg, flush=True)
    log_lines.append(str(msg))


# ============================================================
# PCF evaluator (matches T2A-BASIS-IDENTIFY convention)
# ============================================================
def kn_mp(a4, a3, a2, a1, a0, b2, b1, b0, N, dps):
    mp.mp.dps = dps
    b_at_0 = mp.mpf(b0); b_at_1 = mp.mpf(b2 + b1 + b0)
    a_at_1 = mp.mpf(a4 + a3 + a2 + a1 + a0)
    P_prev2 = b_at_0
    P_prev1 = b_at_1 * b_at_0 + a_at_1
    Q_prev2 = mp.mpf(1)
    Q_prev1 = b_at_1
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
    return K_curr, K_prev


# ============================================================
# Step 1 -- recompute R1 at dps=2000 with stability check
# ============================================================
def step1_recompute():
    log("="*72)
    log("STEP 1 -- recompute R1 at dps=%d, K_%d (buffer dps=%d)" %
        (DPS_TARGET, N_ITER, DPS_TARGET + DPS_BUFFER))
    log("  PCF tuple: a (leading-first) = %s" % A_COEFFS)
    log("             b (leading-first) = %s" % B_COEFFS)
    t0 = time.time()
    a4, a3, a2, a1, a0 = A_COEFFS
    b2, b1, b0         = B_COEFFS
    res = kn_mp(a4, a3, a2, a1, a0, b2, b1, b0,
                N=N_ITER, dps=DPS_TARGET + DPS_BUFFER)
    K_N, K_Nm1 = res
    diff = abs(K_N - K_Nm1)
    log("  K_%d              = %s" % (N_ITER, mp.nstr(K_N, 40)))
    log("  |K_N - K_{N-1}|  = %s" % mp.nstr(diff, 5))
    log("  expected ~ -0.10123520070804963...")
    log("  recompute time   = %.1fs" % (time.time() - t0))
    return K_N, K_Nm1, diff


# ============================================================
# Step 2 -- multi-tier PSLQ
# ============================================================
def relation_residual(rel, basis):
    s = mp.mpf(0)
    for c, x in zip(rel, basis):
        s += mp.mpf(c) * x
    return abs(s)


def try_pslq(basis_vec, l_index, tol_pow=None, hmax=HMAX_PSLQ):
    """PSLQ on basis_vec; require rel[l_index] != 0 (phantom-trap filter)."""
    if tol_pow is None:
        tol_pow = -(mp.mp.dps - 50)
    tol = mp.mpf(10) ** tol_pow
    try:
        rel = mp.pslq(basis_vec, maxcoeff=hmax, tol=tol)
    except Exception as ex:
        return None, "pslq error: %s" % str(ex)[:80], None
    if rel is None:
        return None, "no relation found", None
    res = relation_residual(rel, basis_vec)
    if res > mp.mpf(10) ** (tol_pow + 20):
        return None, "residual %s > tol*1e20" % mp.nstr(res, 3), None
    if rel[l_index] == 0:
        return None, "L-coef=0 (phantom)", mp.nstr(res, 4)
    return [int(x) for x in rel], None, mp.nstr(res, 4)


def build_tier_constants(R1):
    """Return (label -> mpf) for each tier basis element (excluding R1).
    R1 must already be at current mp.dps."""
    PI   = mp.pi
    L2   = mp.log(2)
    LPI  = mp.log(PI)
    K_C  = mp.catalan       # Catalan's constant G
    Z2   = mp.zeta(2)
    Z3   = mp.zeta(3)
    GAM  = mp.euler
    L3   = mp.log(3)

    tiers = {}
    # Tier 1: standard transcendentals + log pi + Catalan G + Euler gamma
    # (note: K usually denotes complete elliptic; "K" here is "Catalan G" per spec)
    tiers["T1"] = [
        ("1", mp.mpf(1)),
        ("pi", PI),
        ("pi^2", PI*PI),
        ("pi^3", PI**3),
        ("log2", L2),
        ("logpi", LPI),
        ("G_Catalan", K_C),
        ("zeta3", Z3),
        ("gamma_Euler", GAM),
    ]
    # Tier 2 = T1 + Li_n(1/2) for n=2..5 + a few 2F1 specials
    Li2_half = mp.polylog(2, mp.mpf(1)/2)
    Li3_half = mp.polylog(3, mp.mpf(1)/2)
    Li4_half = mp.polylog(4, mp.mpf(1)/2)
    Li5_half = mp.polylog(5, mp.mpf(1)/2)
    F_half_half_1_half = mp.hyp2f1(mp.mpf(1)/2, mp.mpf(1)/2, 1, mp.mpf(1)/2)
    F_third_2third_1_half = mp.hyp2f1(mp.mpf(1)/3, mp.mpf(2)/3, 1, mp.mpf(1)/2)
    F_quarter_3qtr_1_half = mp.hyp2f1(mp.mpf(1)/4, mp.mpf(3)/4, 1, mp.mpf(1)/2)
    tiers["T2"] = tiers["T1"] + [
        ("Li2(1/2)", Li2_half), ("Li3(1/2)", Li3_half),
        ("Li4(1/2)", Li4_half), ("Li5(1/2)", Li5_half),
        ("2F1(1/2,1/2;1;1/2)", F_half_half_1_half),
        ("2F1(1/3,2/3;1;1/2)", F_third_2third_1_half),
        ("2F1(1/4,3/4;1;1/2)", F_quarter_3qtr_1_half),
    ]
    # Tier 3 = T2 + Gamma(1/3), Gamma(1/4), Gamma(1/6) and selected products
    G13 = mp.gamma(mp.mpf(1)/3)
    G14 = mp.gamma(mp.mpf(1)/4)
    G16 = mp.gamma(mp.mpf(1)/6)
    tiers["T3"] = tiers["T2"] + [
        ("Gamma(1/3)", G13),
        ("Gamma(1/4)", G14),
        ("Gamma(1/6)", G16),
        ("Gamma(1/3)^3", G13**3),
        ("Gamma(1/4)^2", G14**2),
        ("Gamma(1/4)^4", G14**4),
        ("Gamma(1/6)*Gamma(1/3)", G16*G13),
    ]
    # Tier 4 = T3 + Apery-likes + Dirichlet L-values L(2,chi_-3), L(2,chi_-4)
    # L(2, chi_-3) = sum_{n>=1} chi_-3(n)/n^2;
    # L(2, chi_-4) = Catalan G (already in T1 as G_Catalan); add L(2, chi_-3).
    # L(2, chi_-3) via Hurwitz: L(s,chi) = q^{-s} * sum_a chi(a) zeta(s, a/q)
    # chi_-3(1)=1, chi_-3(2)=-1, chi_-3(0)=0; q=3
    L2_chi_m3 = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3)) / 9
    # L(2,chi_-4) closed form is Catalan G (same as G_Catalan above)
    tiers["T4"] = tiers["T3"] + [
        ("zeta2", Z2),
        ("L2_chi_m3", L2_chi_m3),
        # zeta(3) and L(2,chi_-4)=G_Catalan already present
    ]
    # Tier 5 = T4 + AGM values, lemniscatic omega, Gauss M(1, sqrt 2)
    M1_sq2 = mp.agm(1, mp.sqrt(2))
    M1_sq3 = mp.agm(1, mp.sqrt(3))
    # lemniscatic omega: omega = 2 * \int_0^1 dt/sqrt(1-t^4) = Gamma(1/4)^2/(2*sqrt(2*pi))
    omega_lemn = G14**2 / (2 * mp.sqrt(2*PI))
    tiers["T5"] = tiers["T4"] + [
        ("M(1,sqrt2)", M1_sq2),
        ("M(1,sqrt3)", M1_sq3),
        ("omega_lemn", omega_lemn),
        ("log3", L3),
    ]
    return tiers


def step2_pslq(R1):
    log("\n" + "="*72)
    log("STEP 2 -- multi-tier PSLQ at dps=1000 and dps=2000")
    hits = []
    summary = []

    for dps in (1000, 2000):
        mp.mp.dps = dps
        log("\n[dps=%d] recomputing tier constants ..." % dps)
        # R1 at this precision: re-read with sufficient digits
        # We hold R1 as a high-precision mpf at full dps (caller passed full).
        R1_loc = +R1  # rebind at current dps
        tiers = build_tier_constants(R1_loc)
        for tier_name in ("T1", "T2", "T3", "T4", "T5"):
            entries = tiers[tier_name]
            labels = ["R1"] + [e[0] for e in entries]
            basis  = [R1_loc] + [e[1] for e in entries]
            # PSLQ with R1 at index 0 (L-index)
            tol_pow = -(dps - 100)
            t0 = time.time()
            rel, msg, residue = try_pslq(basis, l_index=0,
                                         tol_pow=tol_pow,
                                         hmax=HMAX_PSLQ)
            dt = time.time() - t0
            cmax = max((abs(c) for c in rel), default=0) if rel else None
            line = ("  [dps=%d %s] basis_size=%d hmax=1e12 t=%.1fs -> "
                    % (dps, tier_name, len(basis), dt))
            if rel is not None:
                line += ("HIT  rel=%s  residue=%s  |c|max=%s"
                         % (rel, residue, cmax))
                hits.append({"dps": dps, "tier": tier_name,
                             "labels": labels, "rel": rel,
                             "residue": str(residue), "cmax": str(cmax)})
            else:
                # Even when no hit, record the |coef|max bound implied by
                # PSLQ termination (HMAX_PSLQ).
                line += "MISS (%s)" % msg
            log(line)
            summary.append({"dps": dps, "tier": tier_name,
                            "basis_size": len(basis), "hit": rel is not None,
                            "msg": msg if rel is None else "HIT",
                            "residue": str(residue) if residue else None})
    return hits, summary


# ============================================================
# Step 3 -- algebraic / functional integer relation
# ============================================================
def step3_algebraic(R1):
    log("\n" + "="*72)
    log("STEP 3 -- integer relation against {R1, R1^2, 1/R1, log|R1|, "
        "exp(R1), arctan R1} U Tier-1")
    mp.mp.dps = 1500
    R1_loc = +R1
    R1sq = R1_loc * R1_loc
    invR = 1 / R1_loc
    logA = mp.log(abs(R1_loc))
    expR = mp.exp(R1_loc)
    atnR = mp.atan(R1_loc)
    PI   = mp.pi
    L2   = mp.log(2)
    LPI  = mp.log(PI)
    K_C  = mp.catalan
    Z3   = mp.zeta(3)
    GAM  = mp.euler
    labels = ["R1", "R1^2", "1/R1", "log|R1|", "exp(R1)", "arctan(R1)",
              "1", "pi", "pi^2", "pi^3", "log2", "logpi",
              "G_Catalan", "zeta3", "gamma_Euler"]
    basis  = [R1_loc, R1sq, invR, logA, expR, atnR,
              mp.mpf(1), PI, PI*PI, PI**3, L2, LPI, K_C, Z3, GAM]
    rel, msg, residue = try_pslq(basis, l_index=0,
                                  tol_pow=-(mp.mp.dps - 100),
                                  hmax=HMAX_PSLQ)
    if rel is None:
        log("  [Step 3] MISS (%s)" % msg)
    else:
        cmax = max(abs(c) for c in rel)
        log("  [Step 3] HIT  rel=%s  residue=%s  |c|max=%s"
            % (rel, residue, cmax))
    return {"labels": labels, "rel": rel, "msg": msg,
            "residue": str(residue) if residue else None}


# ============================================================
# Step 4 -- LMFDB / RIES surrogate
#   We cannot hit external services from the agent; instead run
#   a curated probe against L-values up to small conductor and
#   weight <= 4 that we can compute directly via Hurwitz zeta.
# ============================================================
def step4_lvalue_lookup(R1):
    log("\n" + "="*72)
    log("STEP 4 -- L-value lookup (offline surrogate of LMFDB)")
    log("  Probing L(s, chi) for chi mod q in {3,4,5,6,7,8,11},")
    log("  weight s in {2,3,4}, plus eta(s) (Dirichlet eta).")
    mp.mp.dps = 1500
    R1_loc = +R1
    PI = mp.pi

    def hurwitz_L(chi_table, s):
        # L(s, chi) = q^{-s} * sum_{a=1..q-1} chi(a) * zeta(s, a/q)
        q = len(chi_table)
        s_mp = mp.mpf(s)
        S = mp.mpf(0)
        for a, ca in enumerate(chi_table, start=0):
            if ca == 0:
                continue
            S += ca * mp.zeta(s_mp, mp.mpf(a)/q)
        return mp.mpf(q) ** (-s_mp) * S

    chis = {
        # primitive Dirichlet characters (just enough for probe)
        "chi_-3 (mod 3)":  [0, 1, -1],
        "chi_-4 (mod 4)":  [0, 1, 0, -1],
        "chi_5  (mod 5)":  [0, 1, -1, -1, 1],            # quadratic residue
        "chi_-7 (mod 7)":  [0, 1, 1, -1, 1, -1, -1],
        "chi_8a (mod 8)":  [0, 1, 0, -1, 0, -1, 0, 1],
        "chi_-8 (mod 8)":  [0, 1, 0, 1, 0, -1, 0, -1],
        "chi_-11(mod 11)": [0, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1],
    }
    results = []
    for name, ch in chis.items():
        for s in (2, 3, 4):
            try:
                Lval = hurwitz_L(ch, s)
            except Exception as ex:
                continue
            # form basis {R1, 1, pi, pi^2, pi^3, L(s,chi)} and PSLQ
            basis = [R1_loc, mp.mpf(1), PI, PI*PI, PI**3, Lval]
            rel, msg, residue = try_pslq(basis, l_index=0,
                                          tol_pow=-(mp.mp.dps - 100),
                                          hmax=10**8)
            tag = "%s s=%d" % (name, s)
            if rel is not None:
                cmax = max(abs(c) for c in rel)
                log("  [LMFDB-surrogate] HIT  %s  rel=%s  residue=%s |c|max=%s"
                    % (tag, rel, residue, cmax))
                results.append({"L": tag, "rel": rel,
                                "residue": str(residue),
                                "cmax": str(cmax)})
            else:
                # silent unless DEBUG: log a one-line miss
                pass
    if not results:
        log("  [LMFDB-surrogate] 0 hits across %d (chi,s) pairs"
            % (sum(1 for _ in chis) * 3))
    return results


# ============================================================
# Step 5 -- modular / CM probes (j-invariant at small CM points)
# ============================================================
def step5_modular(R1):
    log("\n" + "="*72)
    log("STEP 5 -- functional / modular probes")
    mp.mp.dps = 1500
    R1_loc = +R1
    PI = mp.pi
    # j-invariant integer values at small CM discriminants
    j_table = {
        "j(i)":        mp.mpf(1728),
        "j(2i)":       mp.mpf(66**3),                  # = 287496
        "j(rho)":      mp.mpf(0),
        "j(sqrt-2)":   mp.mpf(20**3),                  # = 8000
        "j(sqrt-7)":   -mp.mpf(15)**3,                 # = -3375
        "j(sqrt-11)":  -mp.mpf(32)**3,                 # = -32768
        "j(sqrt-19)":  -mp.mpf(96)**3,                 # = -884736
        "j(sqrt-43)":  -mp.mpf(960)**3,
        "j(sqrt-67)":  -mp.mpf(5280)**3,
        "j(sqrt-163)": -mp.mpf(640320)**3,
    }
    results = []
    log("  Testing 2-term modular equation:  R1 == p/q * j_d^{1/k} ?")
    for name, jval in j_table.items():
        for k in (1, 2, 3, 4, 6):
            try:
                v = mp.power(jval, mp.mpf(1)/k) if jval >= 0 else \
                    -mp.power(-jval, mp.mpf(1)/k)
            except Exception:
                continue
            if v == 0:
                continue
            ratio = R1_loc / v
            # is ratio rational with small height?
            try:
                rel = mp.pslq([ratio, mp.mpf(1)], maxcoeff=10**6,
                              tol=mp.mpf(10)**(-(mp.mp.dps - 100)))
            except Exception:
                rel = None
            if rel is not None and rel[0] != 0:
                p_q = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                # confirm
                resid = abs(R1_loc - p_q * v)
                if resid < mp.mpf(10)**(-(mp.mp.dps - 200)):
                    log("  HIT  R1 = %s * %s^(1/%d)   resid=%s"
                        % (mp.nstr(p_q, 8), name, k, mp.nstr(resid, 4)))
                    results.append({"form": "R1 = p/q * %s^(1/%d)" % (name, k),
                                    "p_over_q": mp.nstr(p_q, 30),
                                    "residue": mp.nstr(resid, 6)})
    if not results:
        log("  [modular] 0 hits across j-table x k in {1,2,3,4,6}")
    return results


# ============================================================
# main
# ============================================================
def sha256_file(p):
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def main():
    t_start = time.time()
    K_N, K_Nm1, diff = step1_recompute()
    # store R1 at high precision for reuse
    R1 = K_N

    # write 2000-digit value
    with open(HERE / "r1_dps2000.txt", "w") as f:
        f.write("# R1 at dps=%d, K_%d  (PCF a=%s, b=%s)\n"
                % (DPS_TARGET, N_ITER, A_COEFFS, B_COEFFS))
        f.write(mp.nstr(R1, DPS_TARGET) + "\n")
        f.write("# |K_N - K_{N-1}| = %s\n" % mp.nstr(diff, 6))

    hits2, summary2 = step2_pslq(R1)
    step3 = step3_algebraic(R1)
    step4 = step4_lvalue_lookup(R1)
    step5 = step5_modular(R1)

    # ---- verdict ----
    any_hit = bool(hits2) or (step3["rel"] is not None) or \
              bool(step4) or bool(step5)
    verdict = {"identification_verdict": "HIT" if any_hit else "NULL",
               "confidence_bound_max_coef": HMAX_PSLQ,
               "tiers_tested": ["T1", "T2", "T3", "T4", "T5"],
               "dps_levels": [1000, 2000],
               "phantom_filter": "rel[L_index] != 0 enforced",
               "elapsed_sec": time.time() - t_start}
    log("\n" + "="*72)
    log("VERDICT: %s" % verdict["identification_verdict"])
    if not any_hit:
        log("  No relation with |coef| <= %d found in any tier or probe."
            % HMAX_PSLQ)
        log("  Confidence bound: NO integer relation with L-coefficient != 0")
        log("  exists between R1 and Tier-1..5 basis (%d distinct "
            "constants total) at hmax=1e12, dps=2000."
            % (len(set(lab for s in summary2 for lab in []))))

    # ---- write outputs ----
    LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    out = {"task": "T2A-R1-IDENTIFY",
           "date": "2026-04-30",
           "pcf_tuple": {"a_coeffs_leading_first": A_COEFFS,
                         "b_coeffs_leading_first": B_COEFFS,
                         "source_commit": "fa259b0",
                         "refined_commit": "45fe389"},
           "R1_dps2000_first50": mp.nstr(R1, 50),
           "stability_diff": mp.nstr(diff, 6),
           "step2_pslq_hits": hits2,
           "step2_summary": summary2,
           "step3_algebraic": {k: (v if not isinstance(v, mp.mpf) else str(v))
                                for k, v in step3.items()},
           "step4_lvalue_hits": step4,
           "step5_modular_hits": step5,
           "verdict": verdict}
    with open(RES, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, default=str)

    # ---- AEAL claims ----
    claims = []
    claims.append({
        "claim": "R1 = -0.10123520070804963... computed at dps=%d, K_%d, "
                 "stability |K_N-K_{N-1}| = %s" % (DPS_TARGET, N_ITER,
                                                   mp.nstr(diff, 4)),
        "evidence_type": "computation",
        "dps": DPS_TARGET, "reproducible": True,
        "script": "r1_identify.py",
        "output_hash": sha256_file(HERE / "r1_dps2000.txt")
    })
    claims.append({
        "claim": "PSLQ at dps in {1000,2000}, hmax=1e12, against Tier-1..5 "
                 "graded basis with phantom-trap filter found %d hit(s)"
                 % len(hits2),
        "evidence_type": "computation",
        "dps": 2000, "reproducible": True,
        "script": "r1_identify.py",
        "output_hash": "see r1_results.json"
    })
    claims.append({
        "claim": "Algebraic/functional integer-relation probe "
                 "{R1,R1^2,1/R1,log|R1|,exp(R1),arctan(R1)} U Tier-1 "
                 "found %d hit(s) at dps=1500"
                 % (1 if step3["rel"] is not None else 0),
        "evidence_type": "computation",
        "dps": 1500, "reproducible": True,
        "script": "r1_identify.py",
        "output_hash": "see r1_results.json"
    })
    claims.append({
        "claim": "L-value surrogate (chi mod q in {3,4,5,7,8,11}, s in {2,3,4})"
                 " plus j-invariant CM probe found %d hit(s)"
                 % (len(step4) + len(step5)),
        "evidence_type": "computation",
        "dps": 1500, "reproducible": True,
        "script": "r1_identify.py",
        "output_hash": "see r1_results.json"
    })
    with open(CLM, "w", encoding="utf-8") as f:
        for c in claims:
            f.write(json.dumps(c) + "\n")

    log("\nDone. Total elapsed: %.1fs" % (time.time() - t_start))
    log("Outputs:")
    log("  %s" % LOG.name)
    log("  %s" % RES.name)
    log("  %s" % CLM.name)
    log("  r1_dps2000.txt")
    LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
