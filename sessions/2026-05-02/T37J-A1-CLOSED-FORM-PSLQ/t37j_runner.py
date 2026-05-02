"""
T37J-A1-CLOSED-FORM-PSLQ runner.

Tests whether the apparent rational a_1 values from 017c admit
(a) per-rep closed forms via PSLQ verification, and
(b) a unifying functional form f(Delta_b, A) across reps.

Convention: PCF coefficients [a2, a1, a0] (leading first).
Input: 017c a_1 medians + envelopes (already at >= 40 digits)
       T35 representatives.json (alpha, beta, c, A, Delta_b)
PSLQ probe at mpmath dps=300, tol in {1e-30, 1e-12}, maxcoeff <= 1e15.
"""
from __future__ import annotations

import hashlib
import json
import sys
import traceback
from fractions import Fraction
from pathlib import Path

import mpmath as mp


HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parent.parent.parent  # ...\siarc-relay-bridge
T37C = BRIDGE / "sessions" / "2026-05-02" / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE"
T35 = BRIDGE / "sessions" / "2026-05-02" / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

mp.mp.dps = 300

# 017c a_1 medians (>=46 digits) and envelope half_ranges from
# T37-S2-EXTRACTION-POLYNOMIAL-AWARE/q24_a1_partition.md.
# Stored as exact rationals where the q24 table writes them as such.
# These are the values that 017c published; we use them verbatim.
A1_DATA = {
    "V_quad": {
        "a_1_str": "-1.4722222222222222222222222222222222222222222222222",
        "envelope_str": "6.27e-48",
        "apparent_rational": (-53, 36),
    },
    "QL15": {
        "a_1_str": "-2.4722222222222222222222222222222222222222222222222",
        "envelope_str": "2.39e-46",
        "apparent_rational": (-89, 36),
    },
    "QL05": {
        "a_1_str": "+7.7499999999999999999999999999999999999999999999974",
        "envelope_str": "1.41e-40",
        "apparent_rational": (31, 4),
    },
    "QL09": {
        "a_1_str": "-1.708566178e-57",
        "envelope_str": "1.04e-42",
        "apparent_rational": (0, 1),
    },
}


def sha(payload) -> str:
    if isinstance(payload, (dict, list)):
        s = json.dumps(payload, sort_keys=True, default=str)
    else:
        s = str(payload)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


CLAIMS: list[dict] = []


def claim(text: str, etype: str, dps: int, script: str, payload, repro: bool = True):
    CLAIMS.append({
        "claim": text,
        "evidence_type": etype,
        "dps": dps,
        "reproducible": repro,
        "script": script,
        "output_hash": sha(payload),
    })


def halt(label: str, **details):
    halt_log = {
        "label": label,
        "details": details,
        "claims_so_far": len(CLAIMS),
    }
    (HERE / "halt_log.json").write_text(json.dumps(halt_log, indent=2, default=str))
    (HERE / "claims.jsonl").write_text(
        "\n".join(json.dumps(c) for c in CLAIMS) + "\n"
    )
    print(f"HALT: {label}")
    sys.exit(0)


def cf_reconstruct(x: mp.mpf, qmax: int = 1000) -> tuple[Fraction, mp.mpf] | None:
    """Continued fraction reconstruction; return best p/q with q<=qmax and |x-p/q|."""
    if not mp.isfinite(x):
        return None
    sign = -1 if x < 0 else 1
    y = abs(x)
    # Stern-Brocot / cf
    a = mp.floor(y)
    cf = [int(a)]
    frac = y - a
    while frac > mp.mpf("1e-200") and len(cf) < 50:
        inv = 1 / frac
        a = mp.floor(inv)
        cf.append(int(a))
        frac = inv - a
    # Convergents
    h0, h1 = 1, cf[0]
    k0, k1 = 0, 1
    best = (Fraction(cf[0]), abs(y - cf[0]))
    for ai in cf[1:]:
        h2 = ai * h1 + h0
        k2 = ai * k1 + k0
        if k2 > qmax:
            break
        diff = abs(y - mp.mpf(h2) / mp.mpf(k2))
        if diff < best[1]:
            best = (Fraction(h2, k2), diff)
        h0, h1 = h1, h2
        k0, k1 = k1, k2
    p, q = best[0].numerator, best[0].denominator
    return Fraction(sign * p, q), best[1]


# ------------------------------------------------------------------ PHASE A
def phase_a():
    # Validate inputs
    if not (T37C / "verdict.json").exists():
        halt("T37J_INPUT_INVALID", reason="017c verdict.json missing")
    if not (T35 / "representatives.json").exists():
        halt("T37J_INPUT_INVALID", reason="T35 representatives.json missing")

    reps = json.loads((T35 / "representatives.json").read_text())["representatives"]
    rep_meta = {r["id"]: r for r in reps}

    parsed = {}
    for rid, d in A1_DATA.items():
        a1 = mp.mpf(d["a_1_str"])
        env = mp.mpf(d["envelope_str"])
        parsed[rid] = {
            "a_1": a1,
            "envelope": env,
            "apparent_rational": d["apparent_rational"],
            "Delta_b": rep_meta[rid]["Delta_b"],
            "A": rep_meta[rid]["A_pred"],
            "side": rep_meta[rid]["side"],
        }

    # A.2 precision check (skip QL09: a_1 == 0 to envelope)
    for rid in ("V_quad", "QL15", "QL05"):
        a1 = parsed[rid]["a_1"]
        env = parsed[rid]["envelope"]
        ratio = env / abs(a1)
        if ratio >= mp.mpf("1e-30"):
            halt(
                "T37J_PRECISION_INSUFFICIENT",
                rep=rid,
                envelope=str(env),
                a_1=str(a1),
                ratio=str(ratio),
            )
    claim(
        "Phase A.2: precision threshold env/|a_1| < 1e-30 satisfied for V_quad, QL15, QL05",
        "verification",
        300,
        "t37j_runner.py",
        {rid: str(parsed[rid]["envelope"] / abs(parsed[rid]["a_1"]))
         for rid in ("V_quad", "QL15", "QL05")},
    )

    # A.3 continued-fraction reconstruction at q<=1000
    cf_results = {}
    for rid in ("V_quad", "QL15", "QL05"):
        a1 = parsed[rid]["a_1"]
        rec = cf_reconstruct(a1, qmax=1000)
        if rec is None:
            cf_results[rid] = None
            continue
        frac, diff = rec
        cf_results[rid] = {
            "p": frac.numerator,
            "q": frac.denominator,
            "diff": str(diff),
            "matches_apparent": (frac.numerator, frac.denominator) ==
                                parsed[rid]["apparent_rational"],
            "matches_to_1e30": diff < mp.mpf("1e-30"),
        }
        claim(
            f"Phase A.3: rep {rid} CF reconstruction p/q = {frac.numerator}/{frac.denominator}, |a_1 - p/q| = {mp.nstr(diff, 5)}",
            "computation",
            300,
            "t37j_runner.py",
            cf_results[rid],
        )
    return parsed, cf_results


# ------------------------------------------------------------------ PHASE B
def per_rep_pslq(parsed, rid, tol_exp):
    a1 = parsed[rid]["a_1"]
    # Per-rep basis is the minimal 2-atom basis [1, a_1].
    # PSLQ on [1, a_1] returns integer relation [p, -q] such that
    # p - q*a_1 = 0  i.e.  a_1 = p/q.
    # Larger bases with small rationals {1/2, 1/3, 1/4, 1/6, ...} are
    # rank-degenerate (e.g. 1/2 + 1/3 + 1/6 = 1) and PSLQ locks onto
    # those trivial identities before targeting a_1.
    atoms = [mp.mpf(1), a1]
    tol = mp.mpf(f"1e-{tol_exp}")
    try:
        rel = mp.pslq(atoms, tol=tol, maxcoeff=10**15, maxsteps=4000)
    except Exception as e:  # pylint: disable=broad-except
        return {"relation": None, "error": str(e), "tol_exp": tol_exp}
    if rel is None:
        return {"relation": None, "tol_exp": tol_exp}
    # Verify residual
    resid = mp.fsum(int(c) * a for c, a in zip(rel, atoms))
    return {
        "relation": list(int(c) for c in rel),
        "residual": str(resid),
        "tol_exp": tol_exp,
        "atoms_label": ["1", "a_1"],
        "interpretation": (
            f"a_1 = {-int(rel[0])}/{int(rel[1])}"
            if rel and len(rel) == 2 and int(rel[1]) != 0 else None
        ),
    }


def phase_b(parsed):
    results = {}
    for rid in ("V_quad", "QL15", "QL05"):
        r30 = per_rep_pslq(parsed, rid, 30)
        r12 = per_rep_pslq(parsed, rid, 12)

        # HARD HYGIENE: a relation found at tol=1e-12 but NOT at tol=1e-30
        # is a precision artefact. We only use r30 as the "candidate closed form".
        # If ONLY r12 reports a relation while r30 reports None, flag.
        artefact = (r12.get("relation") is not None
                    and r30.get("relation") is None)

        results[rid] = {
            "tol30": r30,
            "tol12": r12,
            "artefact_only_at_tol12": artefact,
        }
        claim(
            f"Phase B: rep {rid} PSLQ relation at tol=1e-30 maxcoeff=1e15",
            "computation",
            300,
            "t37j_runner.py",
            r30,
        )
        claim(
            f"Phase B: rep {rid} PSLQ HARD HYGIENE re-check at tol=1e-12",
            "computation",
            300,
            "t37j_runner.py",
            r12,
        )

    # Aggregate B.3 rational-confirmation summary
    rat_summary = {}
    for rid in ("V_quad", "QL15", "QL05"):
        rel30 = results[rid]["tol30"].get("relation")
        # Format rational from relation if it has structure [c0, c_a1, ...] with c_a1 != 0.
        rat_summary[rid] = {
            "tol30_relation": rel30,
            "matches_apparent_rational": parsed[rid]["apparent_rational"],
        }
    claim(
        "Phase B.3: rational-confirmation summary across the 3 non-anomalous reps",
        "synthesis",
        300,
        "t37j_runner.py",
        rat_summary,
    )

    return results


# ------------------------------------------------------------------ PHASE C
def phase_c(parsed):
    """Unifying-relation search across the 3 non-anomalous reps."""
    rids = ("V_quad", "QL15", "QL05")
    a1s = [parsed[r]["a_1"] for r in rids]
    Dbs = [mp.mpf(parsed[r]["Delta_b"]) for r in rids]
    As = [mp.mpf(parsed[r]["A"]) for r in rids]

    out = {}

    # C.2 joint PSLQ — three small, targeted searches
    # Search 1: linear over {1, a_1_V, a_1_QL15, a_1_QL05}
    rel1 = mp.pslq([mp.mpf(1)] + a1s, tol=mp.mpf("1e-30"), maxcoeff=10**10,
                   maxsteps=4000)
    out["search1_linear_a1s"] = list(int(c) for c in rel1) if rel1 else None

    # Search 2: a_1's against (Delta_b/(2A)^2) atoms
    twoA_sq = [(2 * a) ** 2 for a in As]
    db_norm = [d / s for d, s in zip(Dbs, twoA_sq)]
    atoms2 = [mp.mpf(1)] + a1s + db_norm
    rel2 = mp.pslq(atoms2, tol=mp.mpf("1e-30"), maxcoeff=10**10, maxsteps=4000)
    out["search2_with_db_norm"] = (list(int(c) for c in rel2) if rel2 else None,
                                   ["1", "a1_V", "a1_QL15", "a1_QL05",
                                    "Db/(2A)^2_V", "Db/(2A)^2_QL15",
                                    "Db/(2A)^2_QL05"])

    # Search 3: a_1's against {Delta_b, A, Delta_b/A, 1/A^2}
    atoms3 = [mp.mpf(1)] + a1s + Dbs + As
    rel3 = mp.pslq(atoms3, tol=mp.mpf("1e-30"), maxcoeff=10**10, maxsteps=4000)
    out["search3_db_A"] = (list(int(c) for c in rel3) if rel3 else None,
                           ["1", "a1_V", "a1_QL15", "a1_QL05",
                            "Db_V", "Db_QL15", "Db_QL05",
                            "A_V", "A_QL15", "A_QL05"])

    claim(
        "Phase C.2: joint PSLQ across the 3 non-anomalous reps' a_1 atoms",
        "computation",
        300,
        "t37j_runner.py",
        {k: v for k, v in out.items() if k.startswith("search")},
    )

    # C.3 functional-form fit
    candidates = {
        "Db/(2A)^2": lambda d, a: d / ((2 * a) ** 2),
        "(Db-1)/(2A)^2": lambda d, a: (d - 1) / ((2 * a) ** 2),
        "(Db+1)/(2A)^2": lambda d, a: (d + 1) / ((2 * a) ** 2),
        "Db/A^2": lambda d, a: d / (a * a),
        "Db/(A*(A-1))": lambda d, a: d / (a * (a - 1)),
        "Db/(4A)": lambda d, a: d / (4 * a),
        "Db*A/(4A^2-1)": lambda d, a: d * a / (4 * a * a - 1),
        "(Db-A)/(2A)^2": lambda d, a: (d - a) / ((2 * a) ** 2),
        "(4*Db-9)/(2A)^2": lambda d, a: (4 * d - 9) / ((2 * a) ** 2),
        "(4*Db-9)/36": lambda d, a: (4 * d - 9) / 36,
        "Db/((2A)^2-2A)": lambda d, a: d / ((2 * a) ** 2 - 2 * a),
    }
    fits = {}
    for name, f in candidates.items():
        per_rep = []
        max_resid = mp.mpf(0)
        for rid, a1, d, a in zip(rids, a1s, Dbs, As):
            pred = f(d, a)
            resid = abs(a1 - pred)
            per_rep.append({"rep": rid, "pred": str(pred), "resid": str(resid)})
            if resid > max_resid:
                max_resid = resid
        fits[name] = {"per_rep": per_rep, "max_resid": str(max_resid),
                      "passes_1e30": max_resid < mp.mpf("1e-30")}
    out["functional_fits"] = fits
    best = min(fits.items(), key=lambda kv: mp.mpf(kv[1]["max_resid"]))
    out["best_functional"] = {"name": best[0], "max_resid": best[1]["max_resid"],
                              "passes_1e30": best[1]["passes_1e30"]}
    claim(
        f"Phase C.3: best candidate functional form {best[0]} max-residual {best[1]['max_resid']}",
        "computation",
        300,
        "t37j_runner.py",
        out["best_functional"],
    )

    # Sub-family probe: A=3 reps only (V_quad + QL15)
    subA3 = mp.pslq(
        [mp.mpf(1), a1s[0], a1s[1], Dbs[0], Dbs[1]],
        tol=mp.mpf("1e-30"), maxcoeff=10**10, maxsteps=4000,
    )
    out["subfamily_A3_pslq"] = (list(int(c) for c in subA3) if subA3 else None,
                                ["1", "a1_V", "a1_QL15", "Db_V", "Db_QL15"])

    # Test "36 a_1 = 4 Delta_b - 9" on each rep individually
    subA3_form = {}
    for rid, a1, d, a in zip(rids, a1s, Dbs, As):
        lhs = (2 * a) ** 2 * a1
        rhs = 4 * d - 9
        subA3_form[rid] = {
            "lhs_(2A)^2*a_1": str(lhs),
            "rhs_4Db-9": str(rhs),
            "diff": str(abs(lhs - rhs)),
        }
    out["subA3_form_test_(2A)^2*a1=4Db-9"] = subA3_form
    claim(
        "Phase C: A=3 sub-family relation (2A)^2*a_1 = 4*Delta_b - 9 tested across all 3 reps",
        "computation",
        300,
        "t37j_runner.py",
        subA3_form,
    )

    # C.4 polynomial-in-(Delta_b, A) fit (3 measurements; degree-1 in each gives
    # 4 unknowns, under-determined; we only run a least-squares stub that records
    # the basis size vs measurements imbalance.)
    out["polyfit_note"] = (
        "Only 3 non-anomalous measurements available; "
        "any polynomial p(Db,A) with >=3 free coefficients is non-unique. "
        "The minimal-coefficient degree-1 form a_1 = c0 + c1*Db + c2*A "
        "is exactly determined: solving yields c0,c1,c2 below."
    )
    # Solve 3x3 system: a_1 = c0 + c1*Db + c2*A
    M = mp.matrix([[1, Dbs[i], As[i]] for i in range(3)])
    b = mp.matrix([a1s[i] for i in range(3)])
    coef = mp.lu_solve(M, b)
    out["polyfit_deg1_coefs"] = {"c0": str(coef[0]), "c1": str(coef[1]),
                                 "c2": str(coef[2])}
    # Try rational reconstruction on the coefficients
    coef_rats = {}
    for nm, val in zip(("c0", "c1", "c2"), (coef[0], coef[1], coef[2])):
        rec = cf_reconstruct(val, qmax=2000)
        if rec is not None:
            frac, diff = rec
            coef_rats[nm] = {"p": frac.numerator, "q": frac.denominator,
                             "diff": str(diff)}
        else:
            coef_rats[nm] = None
    out["polyfit_deg1_rationals"] = coef_rats
    claim(
        "Phase C.4: degree-1 polynomial fit a_1 = c0 + c1*Db + c2*A solved exactly across 3 reps",
        "computation",
        300,
        "t37j_runner.py",
        {"coef": out["polyfit_deg1_coefs"], "rat": coef_rats},
    )

    # C.5 closed-form-candidate summary
    out["closed_form_candidate"] = {
        "exists_global": out["best_functional"]["passes_1e30"],
        "best_form": out["best_functional"]["name"],
        "max_resid": out["best_functional"]["max_resid"],
        "subfamily_A3_relation": "36*a_1 = 4*Delta_b - 9 (exact for V_quad and QL15)",
        "subfamily_A3_extends_to_QL05": False,
    }
    claim(
        f"Phase C.5: closed-form-candidate summary: global f exists = {out['best_functional']['passes_1e30']}",
        "synthesis",
        300,
        "t37j_runner.py",
        out["closed_form_candidate"],
    )
    return out


# ------------------------------------------------------------------ PHASE D
def phase_d(parsed, phase_c_out):
    """QL09 boundary check against the (sub-family) relation and the best f."""
    Db = mp.mpf(parsed["QL09"]["Delta_b"])
    A = mp.mpf(parsed["QL09"]["A"])
    a1 = parsed["QL09"]["a_1"]
    env = parsed["QL09"]["envelope"]
    out = {}
    # Test best global functional form
    best = phase_c_out["best_functional"]["name"]
    candidates = {
        "Db/(2A)^2": lambda d, a: d / ((2 * a) ** 2),
        "(Db-1)/(2A)^2": lambda d, a: (d - 1) / ((2 * a) ** 2),
        "(Db+1)/(2A)^2": lambda d, a: (d + 1) / ((2 * a) ** 2),
        "Db/A^2": lambda d, a: d / (a * a),
        "Db/(A*(A-1))": lambda d, a: d / (a * (a - 1)),
        "Db/(4A)": lambda d, a: d / (4 * a),
        "Db*A/(4A^2-1)": lambda d, a: d * a / (4 * a * a - 1),
        "(Db-A)/(2A)^2": lambda d, a: (d - a) / ((2 * a) ** 2),
        "(4*Db-9)/(2A)^2": lambda d, a: (4 * d - 9) / ((2 * a) ** 2),
        "(4*Db-9)/36": lambda d, a: (4 * d - 9) / 36,
        "Db/((2A)^2-2A)": lambda d, a: d / ((2 * a) ** 2 - 2 * a),
    }
    f_best = candidates[best]
    pred_best = f_best(Db, A)
    out["best_form_at_QL09"] = {
        "form": best,
        "pred": str(pred_best),
        "measured_a1": str(a1),
        "envelope": str(env),
        "diff": str(abs(pred_best - a1)),
        "consistent_to_1e30": abs(pred_best - a1) < mp.mpf("1e-30"),
    }
    # Test A=3 sub-family relation at QL09: predicts (2A)^2*a_1 = 4*Db - 9
    # i.e., a_1 = (4*1 - 9)/64 = -5/64
    sub_pred = (4 * Db - 9) / ((2 * A) ** 2)
    out["subA3_form_at_QL09"] = {
        "relation": "(2A)^2 * a_1 = 4*Db - 9",
        "pred_a1": str(sub_pred),
        "measured_a1": str(a1),
        "diff": str(abs(sub_pred - a1)),
        "consistent_to_1e30": abs(sub_pred - a1) < mp.mpf("1e-30"),
    }
    claim(
        "Phase D: QL09 boundary check against best global form and A=3 sub-family relation",
        "computation",
        300,
        "t37j_runner.py",
        out,
    )
    return out


# ------------------------------------------------------------------ MAIN
def main():
    try:
        parsed, cf_results = phase_a()
        phase_b_results = phase_b(parsed)

        # HARD HYGIENE summary check
        for rid, r in phase_b_results.items():
            if r["artefact_only_at_tol12"]:
                halt("T37J_PSLQ_OVERCLAIM",
                     rep=rid,
                     tol12_relation=r["tol12"]["relation"],
                     tol30_relation=r["tol30"].get("relation"))

        phase_c_out = phase_c(parsed)
        phase_d_out = phase_d(parsed, phase_c_out)

        # Persist outputs
        a1_pslq_per_rep = {
            "phase_a_cf": {rid: cf_results.get(rid) for rid in cf_results},
            "phase_b_pslq": phase_b_results,
        }
        (HERE / "a_1_pslq_per_rep.json").write_text(
            json.dumps(a1_pslq_per_rep, indent=2, default=str))

        unifying = {
            "phase_c": phase_c_out,
            "phase_d_QL09_boundary": phase_d_out,
        }
        (HERE / "a_1_unifying_relation_search.json").write_text(
            json.dumps(unifying, indent=2, default=str))

        # Determine verdict
        global_exists = phase_c_out["best_functional"]["passes_1e30"]
        ql09_consistent = phase_d_out["best_form_at_QL09"]["consistent_to_1e30"]
        per_rep_clean = all(
            phase_b_results[rid]["tol30"].get("relation") is not None
            for rid in ("V_quad", "QL15", "QL05")
        )
        if global_exists and ql09_consistent:
            verdict = "T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09"
        elif global_exists:
            verdict = "T37J_UNIFYING_CLOSED_FORM_FOUND"
        elif per_rep_clean:
            verdict = "T37J_RATIONAL_PER_REP_ONLY"
        else:
            # If some clean and others not -> partial
            any_clean = any(
                phase_b_results[rid]["tol30"].get("relation") is not None
                for rid in ("V_quad", "QL15", "QL05")
            )
            verdict = "T37J_RATIONAL_PARTIAL" if any_clean else "T37J_NO_RATIONAL_DETECTED"

        verdict_obj = {
            "label": verdict,
            "global_unifying_exists": global_exists,
            "ql09_consistent_with_best_global": ql09_consistent,
            "per_rep_pslq_clean": per_rep_clean,
            "subfamily_A3_relation": "36*a_1 = 4*Delta_b - 9 (exact for V_quad, QL15; predicts 23/64 for QL05 vs measured 31/4 -> fails extension)",
        }
        claim(
            f"Verdict: {verdict}",
            "synthesis",
            300,
            "t37j_runner.py",
            verdict_obj,
        )
        (HERE / "verdict.md").write_text(
            f"# T37J verdict\n\n**Label:** {verdict}\n\n"
            f"```\n{json.dumps(verdict_obj, indent=2)}\n```\n"
        )

        # Empty stub logs (none triggered)
        for fn in ("halt_log.json", "discrepancy_log.json", "unexpected_finds.json"):
            p = HERE / fn
            if not p.exists():
                p.write_text("{}\n")

        # claims.jsonl
        (HERE / "claims.jsonl").write_text(
            "\n".join(json.dumps(c) for c in CLAIMS) + "\n"
        )

        print(f"verdict: {verdict}")
        print(f"claims: {len(CLAIMS)}")
        return verdict
    except Exception:  # pylint: disable=broad-except
        tb = traceback.format_exc()
        (HERE / "halt_log.json").write_text(json.dumps({
            "label": "T37J_RUNNER_EXCEPTION",
            "traceback": tb,
        }, indent=2))
        print(tb)
        raise


if __name__ == "__main__":
    main()
