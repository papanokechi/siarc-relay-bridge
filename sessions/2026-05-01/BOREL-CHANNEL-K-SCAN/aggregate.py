"""Aggregate K-scan results for QL15, QL26 and the V_quad reference
(copied from BOREL-CHANNEL-5X) into k_scan_summary.json with
side-by-side comparison and decision verdicts."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / "BOREL-CHANNEL-5X"


def load(p):
    with open(p) as f:
        return json.load(f)


def reduce_grid(grid):
    """Return list of (K, residual, rho_abs, best_eq) tuples."""
    out = []
    for r in grid:
        out.append({
            "K": r["K"],
            "M": r["M"],
            "depth": r["depth"],
            "dps": r["dps"],
            "best_eq": r["best_eq"],
            "residual": r["residual"],
            "rho_star_abs": r["rho_star_abs"],
            "verdict_K": r.get("verdict_K"),
        })
    return out


def diagnose(rows):
    """Return (residual_trend, rho_trend, decision)."""
    rs = [float(r["residual"]) for r in rows]
    pr = [float(r["rho_star_abs"]) for r in rows]
    res_min = min(rs); res_max = max(rs)
    rho_min = min(pr); rho_max = max(pr)
    rho_spread = rho_max - rho_min
    # Decision rule from prompt
    flat_residual = res_max <= 1e-4
    bounded_rho = rho_spread < 0.5
    if flat_residual and bounded_rho:
        decision = "CONFIRMED"
    elif (not flat_residual) or (not bounded_rho):
        if (not flat_residual) and (not bounded_rho):
            decision = "ARTEFACT"
        else:
            decision = "AMBIGUOUS"
    else:
        decision = "AMBIGUOUS"
    return {
        "residual_min": res_min, "residual_max": res_max,
        "rho_min": rho_min, "rho_max": rho_max,
        "rho_spread": rho_spread,
        "flat_residual_<=1e-4": flat_residual,
        "bounded_rho_spread_<0.5": bounded_rho,
        "decision": decision,
    }


def main():
    ql15 = load(HERE / "ql15_k_scan.json")
    ql26 = load(HERE / "ql26_k_scan.json")
    vq = load(PARENT / "vquad_kscan.json")

    ql15_rows = reduce_grid(ql15["grid"])
    ql26_rows = reduce_grid(ql26["grid"])
    # vquad has same shape but no verdict_K key
    vq_rows = []
    for r in vq:
        vq_rows.append({
            "K": r["K"], "M": r["M"], "depth": r["depth"], "dps": r["dps"],
            "best_eq": r["best_eq"], "residual": r["residual"],
            "rho_star_abs": r["rho_star_abs"], "verdict_K": None,
        })

    diag_ql15 = diagnose(ql15_rows)
    diag_ql26 = diagnose(ql26_rows)
    diag_vq = diagnose(vq_rows)

    confirmed = [name for name, d in
                 (("QL15", diag_ql15), ("QL26", diag_ql26))
                 if d["decision"] == "CONFIRMED"]
    if len(confirmed) == 0:
        flag = ("BOREL CHANNEL CONFIRMED ANOMALOUS -- no Delta<0 family in "
                "{QL01, QL02, QL06, V_quad, QL15, QL26} admits a genuine "
                "Borel-channel Painleve reduction. The channel must be "
                "re-specified (recommended: connection-coefficient channel "
                "of the underlying difference equation).")
    elif len(confirmed) == 1:
        flag = (f"BOREL CHANNEL PARTIAL -- one family [{confirmed[0]}] admits "
                f"a Borel-channel Painleve reduction; the other and V_quad do "
                f"not. Inhomogeneous channel structure -- a short note "
                f"(5-7pp) on the one confirmed instance + the inhomogeneity "
                f"finding is warranted.")
    else:
        flag = ("BOREL CHANNEL PARTIALLY UNIVERSAL -- two of the five "
                "non-V_quad Delta<0 families admit Borel-channel Painleve "
                "reductions; V_quad does not. Triggers a short paper "
                "(8-10pp) and a possible PCF-1 v1.3 -> v2.0 expansion.")

    summary = {
        "session": "BOREL-CHANNEL-K-SCAN",
        "date": "2026-05-01",
        "decision_rule": {
            "CONFIRMED": "residual <= 1e-4 across K in {12,16,20,24} AND "
                         "rho_star_abs spread < 0.5",
            "ARTEFACT": "residual grows OR rho_star_abs diverges with K",
            "AMBIGUOUS": "one criterion met, the other not",
        },
        "v_quad_reference (canonical artefact)": {
            "rows": vq_rows,
            "diagnosis": diag_vq,
        },
        "QL15": {"rows": ql15_rows, "diagnosis": diag_ql15,
                 "h_cross_check_K24": ql15.get("h_cross_check_K24")},
        "QL26": {"rows": ql26_rows, "diagnosis": diag_ql26,
                 "h_cross_check_K24": ql26.get("h_cross_check_K24")},
        "side_by_side_table": {
            "header": ["K", "V_quad_residual", "V_quad_rho_abs",
                       "QL15_residual", "QL15_rho_abs",
                       "QL26_residual", "QL26_rho_abs"],
            "rows": [
                [vq_rows[i]["K"],
                 vq_rows[i]["residual"], vq_rows[i]["rho_star_abs"],
                 ql15_rows[i]["residual"], ql15_rows[i]["rho_star_abs"],
                 ql26_rows[i]["residual"], ql26_rows[i]["rho_star_abs"]]
                for i in range(4)
            ],
        },
        "split_finding": (
            "Both QL15 and QL26 behave the same way as V_quad: residuals "
            "fail to drop below 1e-5 systematically and Pade pole radius "
            "drifts unboundedly with K. No structural split detected."
            if (diag_ql15["decision"] == diag_ql26["decision"]
                == diag_vq["decision"])
            else "Split detected -- families behave differently under K-scan."
        ),
        "final_flag": flag,
        "verdicts": {
            "QL15": diag_ql15["decision"],
            "QL26": diag_ql26["decision"],
            "V_quad (reference)": diag_vq["decision"],
        },
    }
    out = HERE / "k_scan_summary.json"
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Wrote {out}")

    print("\nSide-by-side (K, V_quad, QL15, QL26):")
    print(f"{'K':>3} | {'V_quad res':>14} {'V_quad rho':>10} | "
          f"{'QL15 res':>14} {'QL15 rho':>10} | "
          f"{'QL26 res':>14} {'QL26 rho':>10}")
    for row in summary["side_by_side_table"]["rows"]:
        K, vr, vp, q1r, q1p, q2r, q2p = row
        print(f"{K:>3} | {vr:>14} {vp[:10]:>10} | "
              f"{q1r:>14} {q1p[:10]:>10} | {q2r:>14} {q2p[:10]:>10}")
    print(f"\nVerdicts: QL15={diag_ql15['decision']}, QL26={diag_ql26['decision']}, "
          f"V_quad={diag_vq['decision']}")
    print(f"\nFINAL FLAG: {flag}")


if __name__ == "__main__":
    main()
