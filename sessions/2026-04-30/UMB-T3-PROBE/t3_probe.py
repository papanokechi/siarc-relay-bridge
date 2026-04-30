"""UMB-T3-PROBE  (P-09)

Higher-stratum desert sweep.  For each candidate family, we
  1. compute the limit L at dps in [500, 1000, 1500] via backward
     recurrence on the canonical PCF a(n)/(b(n) + ...) form
  2. run a 5-tier basis-exhaustion PSLQ at dps=1500
  3. for NULLs at every tier, also run PSLQ at dps=500 and dps=1000
     and record log10|best_residual| vs dps -> mu_slope
  4. simple Mobius check: PSLQ on 1/L against Tier1
  5. write t3_candidates.json (<=5 entries) + mu_slope_plot.png

Coefficient ordering: leading-first  [a_d, ..., a_0], same as
f1_base_computation.py and t2a_degree42_deep_validate.py.
"""
from __future__ import annotations
import csv, hashlib, json, math, os, random, sys, time
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
IRR_CSV = ROOT / "pcf-casoratian-identities" / "data" / "new_irrational_constants.csv"
T2A_DEEP = ROOT / "siarc-relay-bridge" / "sessions" / "2026-04-26" / "T2A-DEGREE42-DEEP-VALIDATE" / "t2a_degree42_deep_results.json"

DPS_LEVELS = [500, 1000, 1500]
DPS_PROBE = 1500
PSLQ_HMAX = mp.mpf("1e10")
KMAX_FACTOR = 2  # K_iters = KMAX_FACTOR * dps


# -------------------------------------------------------------------------
#  PCF limit via backward recurrence
# -------------------------------------------------------------------------

def poly_eval(coeffs, n):
    """Horner; coeffs leading-first."""
    s = mp.mpf(0)
    for c in coeffs:
        s = s * n + c
    return s


def pcf_limit(a, b, dps, K=None):
    """Compute K(a, b) as
        b(0) + a(1) / (b(1) + a(2)/(b(2) + ...))
    via backward recurrence.  a, b are leading-first coefficient
    lists.  Returns mpf at the given dps (caller should set mp.dps
    around the computation).
    """
    mp.mp.dps = dps + 30
    if K is None:
        K = KMAX_FACTOR * dps
    x = mp.mpf(0)
    for n in range(K, 0, -1):
        an = poly_eval(a, n)
        bn = poly_eval(b, n)
        denom = bn + x
        if denom == 0:
            return None  # division by zero — degenerate
        x = an / denom
    L = poly_eval(b, 0) + x
    return L


# -------------------------------------------------------------------------
#  Basis tiers
# -------------------------------------------------------------------------

def build_tiers(dps):
    """Return list of tier names + per-tier list of mpf basis constants
    (Tier_k is cumulative)."""
    mp.mp.dps = dps + 30
    pi = mp.pi
    log2 = mp.log(2)
    log3 = mp.log(3)
    log5 = mp.log(5)
    G = mp.catalan
    zeta3 = mp.zeta(3)
    zeta2 = pi**2 / 6
    zeta4 = pi**4 / 90
    zeta5 = mp.zeta(5)
    Li2_half = mp.polylog(2, mp.mpf(1)/2)
    Li3_half = mp.polylog(3, mp.mpf(1)/2)
    Lchi3 = mp.dirichlet(2, [0, 1, -1])  # L(2, chi_{-3})
    sqrt2 = mp.sqrt(2)
    sqrt3 = mp.sqrt(3)
    sqrt5 = mp.sqrt(5)
    g13 = mp.gamma(mp.mpf(1)/3)
    g14 = mp.gamma(mp.mpf(1)/4)
    g16 = mp.gamma(mp.mpf(1)/6)
    AGM12 = 1 / mp.agm(1, sqrt2)             # related to lemniscate
    omega_lem = g14**2 / (2 * mp.sqrt(2 * pi))   # lemniscate constant

    tier1 = {
        "1": mp.mpf(1), "pi": pi, "log2": log2, "log3": log3,
        "pi2": pi**2, "zeta3": zeta3, "log5": log5,
    }
    tier2 = dict(tier1, **{
        "G": G, "zeta5": zeta5, "Li2_1/2": Li2_half, "Li3_1/2": Li3_half,
        "Lchi3_2": Lchi3, "sqrt2": sqrt2, "sqrt3": sqrt3, "sqrt5": sqrt5,
    })
    tier3 = dict(tier2, **{
        "Gamma1/3": g13, "Gamma1/4": g14, "Gamma1/6": g16,
        "Gamma1/3^2": g13**2, "Gamma1/4^2": g14**2,
    })
    tier4 = dict(tier3, **{
        "AGM(1,sqrt2)": AGM12, "omega_lem": omega_lem,
        "exp1": mp.e, "expm1pi": mp.expm1(pi),
    })
    tier5 = dict(tier4, **{
        "pi*log2": pi*log2, "pi*log3": pi*log3,
        "pi*G": pi*G, "log2*log3": log2*log3, "pi*zeta3": pi*zeta3,
    })
    return [
        ("T1", tier1),
        ("T2", tier2),
        ("T3", tier3),
        ("T4", tier4),
        ("T5", tier5),
    ]


# -------------------------------------------------------------------------
#  PSLQ probe (with phantom-trap)
# -------------------------------------------------------------------------

def pslq_probe(L, basis_dict, dps, hmax=PSLQ_HMAX):
    """Strong-mode PSLQ.  Return (rel_or_None, residual, names,
    max_coef).  A hit requires rel[0] != 0 (phantom-trap).
    """
    mp.mp.dps = dps + 30
    names = list(basis_dict.keys())
    vec = [L] + [basis_dict[k] for k in names]
    try:
        rel = mp.pslq(vec, tol=mp.mpf(10)**(-(dps - 60)), maxcoeff=hmax)
    except Exception:
        rel = None
    if rel is None:
        return None, float(mp.fabs(L)), names, None
    s = mp.mpf(0)
    for c, v in zip(rel, vec):
        s += c * v
    res = float(mp.fabs(s))
    max_coef = max(abs(int(c)) for c in rel) if rel else None
    if rel[0] == 0:
        return None, res, names, max_coef  # phantom
    return rel, res, names, max_coef


def pslq_probe_weak(L, basis_dict, dps):
    """Weak-mode PSLQ with hmax allowed to grow with dps so we
    *always* find something.  Used to track coefficient growth
    (mu-coef-slope) and residual decay (mu-res-slope) for NULLs.
    """
    mp.mp.dps = dps + 30
    names = list(basis_dict.keys())
    vec = [L] + [basis_dict[k] for k in names]
    weak_hmax = mp.mpf(10) ** (dps // 3)
    try:
        rel = mp.pslq(vec, tol=mp.mpf(10)**(-(dps - 60)), maxcoeff=weak_hmax)
    except Exception:
        rel = None
    if rel is None:
        return None, float(mp.fabs(L)), 0
    s = mp.mpf(0)
    for c, v in zip(rel, vec):
        s += c * v
    res = float(mp.fabs(s))
    max_coef = max(abs(int(c)) for c in rel) if rel else 0
    return rel, res, max_coef


# -------------------------------------------------------------------------
#  Family loaders
# -------------------------------------------------------------------------

def load_trans_hard():
    """Load the 30 trans_hard examples from T2A-DEGREE42-DEEP-VALIDATE."""
    data = json.loads(T2A_DEEP.read_text(encoding="utf-8"))
    fams = []
    for ex in data["trans_hard_examples"]:
        fams.append({
            "id": f"TH_a{'_'.join(str(x) for x in ex['coeffs_a'])}_b{'_'.join(str(x) for x in ex['coeffs_b'])}",
            "source": "T2A_trans_hard_42",
            "a": ex["coeffs_a"],
            "b": ex["coeffs_b"],
            "L_published": ex["L"],
        })
    return fams


def load_t2a_r1():
    return [{
        "id": "T2A_R1",
        "source": "T2A-R1-IDENTIFY",
        "a": [1, 0, -1, -1, -1],
        "b": [-1, 1, -1],
        "L_published": "-0.10123520070804963",
    }]


def load_irr_482_sample(n_sample=10, seed=2026):
    rng = random.Random(seed)
    rows = []
    with IRR_CSV.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for r in reader:
            rows.append({
                "id": f"IRR482_{r['id']}",
                "source": "irr_482",
                "a": [1],
                "b": [int(r["A"]), int(r["B"]), int(r["C"])],
                "L_published": r["value"],
            })
    rng.shuffle(rows)
    return rows[:n_sample]


# -------------------------------------------------------------------------
#  Mobius reduction check
# -------------------------------------------------------------------------

def mobius_check(L, basis_dict, dps):
    """If 1/L hits a tier with nonzero L-coefficient, that's a Mobius
    reduction.  Return rel for 1/L or None.
    """
    mp.mp.dps = dps + 30
    inv = 1 / L
    rel, res, _, _ = pslq_probe(inv, basis_dict, dps)
    return rel, res


def algebraic_check(L, dps, max_deg=4, hmax=mp.mpf("1e8")):
    """Run PSLQ on {1, L, L^2, ..., L^max_deg} to detect if L is a
    root of a small-coefficient integer polynomial.  Returns
    (deg, coeffs, residual) or (0, None, residual_floor).
    """
    mp.mp.dps = dps + 30
    powers = [mp.mpf(1)]
    for _ in range(max_deg):
        powers.append(powers[-1] * L)
    try:
        rel = mp.pslq(powers, tol=mp.mpf(10)**(-(dps - 60)), maxcoeff=hmax)
    except Exception:
        rel = None
    if rel is None:
        return 0, None, float(mp.fabs(L))
    s = mp.mpf(0)
    for c, v in zip(rel, powers):
        s += c * v
    res = float(mp.fabs(s))
    # find degree (highest non-zero coef index)
    deg = 0
    for i, c in enumerate(rel):
        if c != 0:
            deg = i
    return deg, [int(c) for c in rel], res


# -------------------------------------------------------------------------
#  Per-family driver
# -------------------------------------------------------------------------

def process_family(fam):
    print(f"\n[fam {fam['id']}]  a={fam['a']}  b={fam['b']}", flush=True)
    out = {"id": fam["id"], "source": fam["source"], "a": fam["a"], "b": fam["b"],
           "L_published": fam.get("L_published")}

    # 1) compute limits at all dps levels
    Ls = {}
    for dps in DPS_LEVELS:
        t0 = time.time()
        L = pcf_limit(fam["a"], fam["b"], dps)
        if L is None:
            out["error"] = f"degenerate at dps={dps}"
            return out
        Ls[dps] = mp.mpf(str(L))  # snapshot at this dps
        print(f"  dps={dps:5d}  L={mp.nstr(L, 25)}  ({time.time()-t0:.1f}s)", flush=True)
    out["L_dps"] = {dps: mp.nstr(Ls[dps], 40) for dps in DPS_LEVELS}

    # convergence sanity
    diff = mp.fabs(Ls[DPS_LEVELS[-1]] - Ls[DPS_LEVELS[0]])
    out["convergence_diff_lowest_vs_highest"] = mp.nstr(diff, 5)
    # divergent only if values disagree by more than a generous margin
    # (otherwise low-dps just has fewer correct digits than high-dps)
    if diff > mp.mpf("1e-30"):
        out["divergent_warn"] = True
        return out

    # 2) 5-tier PSLQ at dps=DPS_PROBE
    L = Ls[DPS_PROBE]
    mp.mp.dps = DPS_PROBE + 60
    tiers = build_tiers(DPS_PROBE)
    tier_results = []
    all_null = True
    for tname, basis in tiers:
        t0 = time.time()
        rel, res, names, mxc = pslq_probe(L, basis, DPS_PROBE)
        tier_results.append({
            "tier": tname,
            "basis_size": len(basis),
            "hit": rel is not None,
            "relation": [int(x) for x in rel] if rel else None,
            "names": names,
            "residual_log10": math.log10(res) if res > 0 else -10000,
            "max_coef": mxc,
            "time_sec": round(time.time() - t0, 2),
        })
        print(f"  {tname} (|B|={len(basis)})  hit={rel is not None}  res=10^{tier_results[-1]['residual_log10']:.1f}  ({time.time()-t0:.1f}s)", flush=True)
        if rel is not None:
            all_null = False
    out["tiers"] = tier_results
    out["all_null"] = all_null

    if not all_null:
        # demoted: some tier identified it
        for t in tier_results:
            if t["hit"]:
                out["demoted_at_tier"] = t["tier"]
                break
        return out

    # 3) mu_slope: weak-PSLQ at each dps, track residual *and*
    #    max-coefficient growth.  T3 candidates have coef growing
    #    ~ linearly in dps (no real relation, only forced fake fits).
    print("  -> NULL across all 5 tiers; computing mu_slope ...", flush=True)
    mu_pts = []
    # Reuse the high-precision basis already built at DPS_PROBE; mpmath
    # will internally use whatever working precision we set around the
    # PSLQ call.
    weak_basis = tiers[-1][1]
    for dps in DPS_LEVELS:
        Lp = Ls[dps]
        _, res, mxc = pslq_probe_weak(Lp, weak_basis, dps)
        mu_pts.append({
            "dps": dps,
            "log10_res": math.log10(res) if res > 0 else -10000,
            "log10_max_coef": math.log10(mxc) if mxc and mxc > 0 else 0,
        })
        print(f"    weak dps={dps}  log10|res|={mu_pts[-1]['log10_res']:.2f}  log10(max_coef)={mu_pts[-1]['log10_max_coef']:.2f}", flush=True)

    def linreg(xs, ys):
        n = len(xs); xm = sum(xs)/n; ym = sum(ys)/n
        num = sum((x-xm)*(y-ym) for x,y in zip(xs,ys))
        den = sum((x-xm)**2 for x in xs) or 1.0
        return num/den

    xs = [p["dps"] for p in mu_pts]
    res_slope = linreg(xs, [p["log10_res"] for p in mu_pts])
    coef_slope = linreg(xs, [p["log10_max_coef"] for p in mu_pts])
    out["mu_probe"] = mu_pts
    out["mu_res_slope"] = res_slope
    out["mu_coef_slope"] = coef_slope
    # mu = inf candidate: PSLQ never settles on bounded-coef relation.
    # Two signatures:
    #   (a) hard NULL — weak PSLQ returns None at every dps (max_coef=0)
    #   (b) coef-growth — rels found but coefs grow ~ linearly in dps
    weak_all_none = all(p["log10_max_coef"] == 0 for p in mu_pts)
    out["weak_all_none"] = weak_all_none
    out["mu_inf_flag"] = bool(weak_all_none or coef_slope > 0.05)

    # 4) Mobius / inverse check (against Tier1 *and* Tier3)
    inv_rel, inv_res = mobius_check(L, tiers[0][1], DPS_PROBE)
    out["mobius_inv_T1"] = {
        "hit": inv_rel is not None,
        "relation": [int(x) for x in inv_rel] if inv_rel else None,
        "residual_log10": math.log10(inv_res) if inv_res > 0 else -10000,
    }
    inv_rel3, inv_res3 = mobius_check(L, tiers[2][1], DPS_PROBE)
    out["mobius_inv_T3"] = {
        "hit": inv_rel3 is not None,
        "relation": [int(x) for x in inv_rel3] if inv_rel3 else None,
        "residual_log10": math.log10(inv_res3) if inv_res3 > 0 else -10000,
    }
    if inv_rel is not None or inv_rel3 is not None:
        out["mobius_demoted"] = True

    # 5) Algebraic check: is L a root of an integer poly of deg <= 4
    #    with coefs <= 1e8?  Captures the 482-irrational family
    #    (most are algebraic of degree 2) and any deg-(4,2) family
    #    whose limit happens to be a low-degree algebraic number.
    alg_deg, alg_coefs, alg_res = algebraic_check(L, DPS_PROBE, max_deg=4)
    out["algebraic_check"] = {
        "deg": alg_deg,
        "coefs": alg_coefs,
        "residual_log10": math.log10(alg_res) if alg_res > 0 else -10000,
    }
    if alg_deg >= 1:
        out["algebraic_demoted"] = True
        out["algebraic_degree"] = alg_deg

    return out


# -------------------------------------------------------------------------
#  Main
# -------------------------------------------------------------------------

def main():
    t_start = time.time()
    families = []
    families += load_t2a_r1()
    families += load_trans_hard()
    families += load_irr_482_sample(10)
    print(f"Total families: {len(families)}  (R1=1, trans_hard={sum(1 for f in families if f['source']=='T2A_trans_hard_42')}, irr_482={sum(1 for f in families if f['source']=='irr_482')})", flush=True)

    results = []
    for fam in families:
        try:
            r = process_family(fam)
        except Exception as e:
            r = {"id": fam["id"], "error": f"{type(e).__name__}: {e}"}
        results.append(r)
        # incremental save
        (HERE / "t3_probe_partial.json").write_text(
            json.dumps({"results_so_far": results}, indent=2), encoding="utf-8")

    # Determine T3 candidates: all_null AND not Mobius/algebraic-demoted
    candidates = [r for r in results
                  if r.get("all_null")
                  and not r.get("mobius_demoted")
                  and not r.get("algebraic_demoted")
                  and not r.get("error")]
    # rank: prefer mu_inf_flag, then smallest |slope|, then most negative log10_res at dps=1500
    def rank_key(r):
        return (
            -1 if r.get("mu_inf_flag") else 0,
            -r.get("mu_coef_slope", 0),
            -(r["mu_probe"][-1]["log10_res"] if r.get("mu_probe") else 0),
        )
    candidates.sort(key=rank_key)
    top_candidates = candidates[:5]

    # full results
    full_path = HERE / "t3_probe_full.json"
    full_path.write_text(json.dumps({
        "task": "UMB-T3-PROBE",
        "elapsed_sec": round(time.time() - t_start, 1),
        "n_families": len(results),
        "n_all_null": sum(1 for r in results if r.get("all_null")),
        "n_mobius_demoted": sum(1 for r in results if r.get("mobius_demoted")),
        "n_algebraic_demoted": sum(1 for r in results if r.get("algebraic_demoted")),
        "n_t3_candidates": len(candidates),
        "results": results,
    }, indent=2), encoding="utf-8")

    out_path = HERE / "t3_candidates.json"
    out_path.write_text(json.dumps({
        "task": "UMB-T3-PROBE",
        "n_candidates": len(top_candidates),
        "ranking_key": "mu_inf_flag desc, |mu_slope| asc, log10_res desc",
        "candidates": top_candidates,
    }, indent=2), encoding="utf-8")

    print(f"\n=== SUMMARY ===")
    print(f"Total families processed   : {len(results)}")
    print(f"All-NULL across 5 tiers    : {sum(1 for r in results if r.get('all_null'))}")
    print(f"Mobius-demoted (1/L hits)  : {sum(1 for r in results if r.get('mobius_demoted'))}")
    print(f"Algebraic-demoted (deg<=4) : {sum(1 for r in results if r.get('algebraic_demoted'))}")
    print(f"Surviving T3 candidates    : {len(candidates)}")
    print(f"Top-5 written to           : {out_path.name}")
    print(f"Full results               : {full_path.name}")
    print(f"Elapsed                    : {time.time() - t_start:.1f}s")

    # sha256 of full output
    h = hashlib.sha256(full_path.read_bytes()).hexdigest()
    print(f"sha256(t3_probe_full.json) = {h}")


if __name__ == "__main__":
    main()
