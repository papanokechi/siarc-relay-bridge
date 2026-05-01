"""Auxiliary: N-scaling of j=0 cubic delta across R1.1, R1.3, T2-D.

Demonstrates that |delta_j=0| shrinks monotonically with the maximum
fitting depth N_max, consistent with a finite-N tail-window artefact
(A_true = 6 asymptotically), rather than A_true != 6.
"""
from __future__ import annotations
import csv, json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# R1.1 free A (N_max ~ 67, dps=200..1000 escalation)
R11 = HERE.parent.parent / "2026-05-01" / "PCF2-SESSION-R1.1" / "assembled_data_v2.csv"
# R1.3 free A (N=[50..250] step 2, N_ref=400, dps=2000)
R13 = HERE.parent.parent / "2026-05-01" / "PCF2-SESSION-R1.3" / "residualization_d3.csv"
# T2-D free A (N=[180..480] step 10, N_ref=700, dps=4000)
T2D = HERE / "phase_D_pslq.json"


def main():
    r11 = {int(r["family_id"]): r for r in csv.DictReader(open(R11))}
    r13 = {int(r["family_id"]): r for r in csv.DictReader(open(R13))}
    t2d = json.loads(T2D.read_text())["fits"]

    rows = []
    for fid in (30, 31, 32, 33):
        d11 = float(r11[str(fid) if str(fid) in r11 else fid].get("delta", "nan")) if False else float(r11[fid]["delta"])
        s11 = float(r11[fid]["A_stderr"])
        d13 = float(r13[fid]["delta_R13_free"])
        s13 = float(r13[fid]["A_stderr_R13_free"])
        d2  = t2d[str(fid)]["free"]["delta_deep"]
        s2  = t2d[str(fid)]["free"]["A_stderr"]
        rows.append({
            "family_id": fid,
            "R11": {"Nmax": 67,  "delta": d11, "stderr": s11,
                    "abs_delta": abs(d11)},
            "R13": {"Nmax": 250, "delta": d13, "stderr": s13,
                    "abs_delta": abs(d13)},
            "T2D": {"Nmax": 480, "delta": d2,  "stderr": s2,
                    "abs_delta": abs(d2)},
            "ratio_R11_to_R13": abs(d11 / d13),
            "ratio_R13_to_T2D": abs(d13 / d2),
            "monotone_decreasing": abs(d11) > abs(d13) > abs(d2),
        })
        print(f"fam{fid}: |delta| = R11({abs(d11):.3e} @N=67) > "
              f"R13({abs(d13):.3e} @N=250) > T2D({abs(d2):.3e} @N=480)? "
              f"{rows[-1]['monotone_decreasing']}")
        print(f"        ratio R11/R13 = {abs(d11/d13):.2f}, "
              f"R13/T2D = {abs(d13/d2):.2f}")

    out = {
        "claim": ("|delta_j=0| at the j=0 cubic cell shrinks monotonically "
                  "with N_max across R1.1 (N=67), R1.3 (N=250), T2-D "
                  "(N=480), consistent with finite-N tail-window artefact "
                  "(A_true = 6 asymptotically) rather than A_true != 6."),
        "rows": rows,
        "all_monotone": all(r["monotone_decreasing"] for r in rows),
    }
    out_path = HERE / "phase_D_n_scaling.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nall families monotone decreasing: {out['all_monotone']}")
    print(f"wrote {out_path.name}")


if __name__ == "__main__":
    main()
