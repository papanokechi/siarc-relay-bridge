#!/usr/bin/env python3
"""
P06-DESERT-VALIDATION Step 2: Precision-stability check.

Re-runs a sample of the (4,3) and (5,3) desert sweep at 260 dps
(2x the original 130 dps used in cycles 1-3) and checks whether any
Trans-stratum relation is recovered that was missed at the lower
precision.  Expected outcome: zero new relations.

Sample selection note: per-family PSLQ residuals were not retained in
the cycle-1/2/3 result JSONs, so the "smallest residual" criterion
requested by the task is not literally available.  Instead we draw a
deterministic 100-triple sample (50 from each profile) using a
fixed-seed Sobol-like even-spacing through the 4,410-triple integer
cube A in [1,10], B in [-10,10], C in [-10,10] (skipping divergent
b(0)=b(1)=0 cases at C=0, A+B=0).  This gives uniform geometric
coverage and is reproducible.

Outputs: step2_precision_stability_result.json
"""
import json
import time
from pathlib import Path
from mpmath import mp, mpf, pi as mp_pi, zeta, log, catalan, pslq

HERE = Path(__file__).resolve().parent
DPS_LOW = 130
DPS_HIGH = 260
N_TERMS_43 = 1500
N_TERMS_53 = 2000
MAXCOEFF = 10000
SAMPLE_PER_PROFILE = 50
RNG_SEED = 20260501

# 13-element basis matching the desert paper exactly: NO pi
def make_basis(V, dps):
    mp.dps = dps + 50
    PI = mp_pi
    z3 = zeta(3); pi2 = PI ** 2; ln2 = log(2); ln2sq = ln2 ** 2
    cat = catalan; piln2 = PI * ln2; z5 = zeta(5)
    pi4_90 = PI ** 4 / 90; pi2ln2 = pi2 * ln2
    z3pi2 = z3 * pi2; z3ln2 = z3 * ln2
    z2ln2sq = (pi2 / 6) * ln2sq
    bv = [V, mpf(1), z3, pi2, ln2sq, cat, piln2, z5, pi4_90,
          pi2ln2, z3pi2, z3ln2, z2ln2sq]
    mp.dps = dps
    return [+x for x in bv]


def eval_pcf_43(A, B, C, nterms, dps, start_n=0):
    mp.dps = dps + 50
    mA, mB, mC = mpf(A), mpf(B), mpf(C)
    if start_n == 0:
        b0 = mC
        Pp, Pc = mpf(1), b0
        Qp, Qc = mpf(0), mpf(1)
        rng_start = 1
    else:
        b1 = mpf(3) * (mA + mB + mC)
        Pp, Pc = mpf(1), b1
        Qp, Qc = mpf(0), mpf(1)
        rng_start = 2
    for n in range(rng_start, nterms + 1):
        nn = mpf(n)
        an = -(nn * nn) * ((nn + 1) * (nn + 1))
        bn = (2 * nn + 1) * (mA * nn * nn + mB * nn + mC)
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 80 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10) ** 30:
                Pp /= s; Pc /= s; Qp /= s; Qc /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


def eval_pcf_53(A, B, C, nterms, dps):
    mp.dps = dps + 50
    mA, mB, mC = mpf(A), mpf(B), mpf(C)
    b0 = mC
    Pp, Pc = mpf(1), b0
    Qp, Qc = mpf(0), mpf(1)
    for n in range(1, nterms + 1):
        nn = mpf(n)
        an = -(nn * nn) * ((nn + 1) * (nn + 1)) * (2 * nn + 1)
        bn = (2 * nn + 1) * (mA * nn * nn + mB * nn + mC)
        Pn = bn * Pc + an * Pp
        Qn = bn * Qc + an * Qp
        Pp, Pc = Pc, Pn
        Qp, Qc = Qc, Qn
        if n % 60 == 0 and Qc != 0:
            s = abs(Qc)
            if s > mpf(10) ** 20:
                Pp /= s; Pc /= s; Qp /= s; Qc /= s
    if Qc == 0:
        return None
    mp.dps = dps
    return +(Pc / Qc)


def deterministic_sample(n_per_profile, seed):
    """Even-spaced deterministic sample over A in [1,10], |B|<=10, |C|<=10."""
    import random
    rng = random.Random(seed)
    triples = []
    for A in range(1, 11):
        for B in range(-10, 11):
            for C in range(-10, 11):
                if C == 0 and A + B == 0:
                    continue  # divergent
                triples.append((A, B, C))
    rng.shuffle(triples)
    return triples[:n_per_profile]


def pslq_check(V, dps, maxcoeff):
    bv = make_basis(V, dps)
    mp.dps = dps
    try:
        rel = pslq(bv, maxcoeff=maxcoeff, maxsteps=8000)
    except Exception:
        return None, None, bv
    if rel is None:
        return None, None, bv
    if rel[0] == 0:
        return None, None, bv
    resid = abs(sum(c * x for c, x in zip(rel, bv)))
    return rel, resid, bv


def run_profile(profile, eval_fn, nterms, sample_seed):
    sample = deterministic_sample(SAMPLE_PER_PROFILE, sample_seed)
    rows = []
    for (A, B, C) in sample:
        # eval at low precision
        if eval_fn is eval_pcf_43:
            start_n = 1 if C == 0 else 0
            V_low = eval_fn(A, B, C, nterms, DPS_LOW, start_n=start_n)
            V_high = eval_fn(A, B, C, nterms, DPS_HIGH, start_n=start_n)
        else:
            V_low = eval_fn(A, B, C, nterms, DPS_LOW)
            V_high = eval_fn(A, B, C, nterms, DPS_HIGH)
        if V_low is None or V_high is None:
            rows.append({"profile": profile, "A": A, "B": B, "C": C,
                         "status": "diverged"})
            continue
        rel_low, resid_low, _ = pslq_check(V_low, DPS_LOW, MAXCOEFF)
        rel_high, resid_high, _ = pslq_check(V_high, DPS_HIGH, MAXCOEFF)
        rows.append({
            "profile": profile, "A": A, "B": B, "C": C,
            "rel_130": [int(c) for c in rel_low] if rel_low else None,
            "rel_260": [int(c) for c in rel_high] if rel_high else None,
            "resid_log10_130": (float(mp.log10(resid_low))
                                if resid_low and resid_low > 0 else None),
            "resid_log10_260": (float(mp.log10(resid_high))
                                if resid_high and resid_high > 0 else None),
        })
    return rows


def main():
    t0 = time.time()
    print("=== STEP 2 precision-stability check ===")
    print(f"Sample size: {SAMPLE_PER_PROFILE} per profile, deterministic seed={RNG_SEED}")
    print(f"DPS_LOW={DPS_LOW}, DPS_HIGH={DPS_HIGH}, MAXCOEFF={MAXCOEFF}")

    print("\nProfile (4,3)...")
    rows_43 = run_profile("(4,3)", eval_pcf_43, N_TERMS_43, RNG_SEED)
    print(f"  done, {time.time()-t0:.1f}s")

    print("\nProfile (5,3)...")
    rows_53 = run_profile("(5,3)", eval_pcf_53, N_TERMS_53, RNG_SEED + 1)
    print(f"  done, {time.time()-t0:.1f}s")

    all_rows = rows_43 + rows_53
    new_at_high = [r for r in all_rows
                   if r.get("rel_260") is not None and r.get("rel_130") is None]
    diverged = [r for r in all_rows if r.get("status") == "diverged"]

    out = {
        "task": "P06-DESERT-VALIDATION-STEP2",
        "description": ("Precision-stability check: re-run a 100-triple "
                        "deterministic sample (50 per profile) of the "
                        "(4,3)/(5,3) desert at 130 vs 260 dps with the "
                        "exact desert basis (no pi)."),
        "dps_low": DPS_LOW, "dps_high": DPS_HIGH,
        "maxcoeff": MAXCOEFF,
        "sample_per_profile": SAMPLE_PER_PROFILE,
        "rng_seed": RNG_SEED,
        "n_total": len(all_rows),
        "n_diverged": len(diverged),
        "n_relations_at_130": sum(1 for r in all_rows if r.get("rel_130")),
        "n_relations_at_260": sum(1 for r in all_rows if r.get("rel_260")),
        "n_new_relations_only_at_260": len(new_at_high),
        "wall_clock_s": time.time() - t0,
        "rows": all_rows,
    }
    out_path = HERE / "step2_precision_stability_result.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nDONE.")
    print(f"  Total triples tested:      {out['n_total']}")
    print(f"  Diverged:                  {out['n_diverged']}")
    print(f"  Relations at 130 dps:      {out['n_relations_at_130']}")
    print(f"  Relations at 260 dps:      {out['n_relations_at_260']}")
    print(f"  NEW relations at 260 only: {out['n_new_relations_only_at_260']}")
    print(f"  Wall clock: {out['wall_clock_s']:.1f}s")
    print(f"  Output: {out_path}")
    if out["n_new_relations_only_at_260"] > 0:
        print("\n*** HALT TRIGGER: new relation(s) found at 260 dps! ***")
        for r in new_at_high:
            print(f"  {r['profile']} (A,B,C)=({r['A']},{r['B']},{r['C']}) rel_260={r['rel_260']}")


if __name__ == "__main__":
    main()
