"""Re-validate Step 3/4 hits with proper Alg/Rat-first pipeline,
then deep-validate genuine Log/Trans candidates at dps=200, K=2000.

Pipeline:
  Stage B: PSLQ on [1,L,L^2,L^3,L^4] at dps=100. If hit -> Alg/Rat.
  Stage C: PSLQ on trans basis at dps=100. Phantom guard.
  Deep:    PSLQ at dps=200, K_2000, 7-basis battery, residual<1e-100.
"""
from __future__ import annotations
import json
import math
import time
from pathlib import Path

import mpmath as mp_

HERE = Path(__file__).parent
INPUT = HERE / "anomaly_minus_one_36.json"
OUT = HERE / "reclassified_hits.json"


def kn_mp_deg2(coeffs, N, dps):
    a2, a1, a0, b1, b0 = coeffs
    mp_.mp.dps = dps
    a2m, a1m, a0m, b1m, b0m = (mp_.mpf(c) for c in (a2, a1, a0, b1, b0))
    Pp = mp_.mpf(1); Pc = b0m
    Qp = mp_.mpf(0); Qc = mp_.mpf(1)
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


def reclassify_one(coeffs, dps_main=100, n_main=600):
    """Returns dict with label and details."""
    mp_.mp.dps = dps_main
    res = kn_mp_deg2(coeffs, n_main, dps_main)
    if res is None:
        return {"label": "fail", "msg": "Q=0"}
    L, Lprev = res
    diff = abs(L - Lprev)
    if not mp_.isfinite(L):
        return {"label": "fail", "msg": "non-finite"}

    # Stage B: rat/alg
    rat_basis = [L ** k for k in range(5)]
    try:
        rel = mp_.pslq(rat_basis, maxcoeff=10**6)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(int(c) * x for c, x in zip(rel, rat_basis)))
        if residual < mp_.mpf(10) ** (-40):
            label = "Rat" if all(int(c) == 0 for c in rel[2:]) else "Alg"
            return {"label": label,
                    "L_100": mp_.nstr(L, 50),
                    "relation": [int(c) for c in rel],
                    "residual": mp_.nstr(residual, 5)}

    # Stage C: trans
    pi_v = mp_.pi; ln2 = mp_.log(2); ln3 = mp_.log(3); ln5 = mp_.log(5)
    basis = [mp_.mpf(1), L, pi_v, L * pi_v, pi_v ** 2, L * pi_v ** 2,
             ln2, L * ln2, ln3, L * ln3, ln5, L * ln5]
    names = ["1", "L", "pi", "L*pi", "pi^2", "L*pi^2",
             "log2", "L*log2", "log3", "L*log3", "log5", "L*log5"]
    try:
        rel = mp_.pslq(basis, maxcoeff=10**9)
    except Exception:
        rel = None
    if rel is None:
        return {"label": "Desert", "L_100": mp_.nstr(L, 50)}
    residual = abs(sum(int(c) * x for c, x in zip(rel, basis)))
    if residual > mp_.mpf(10) ** (-40):
        return {"label": "Desert", "L_100": mp_.nstr(L, 50),
                "msg": f"weak relation residual {mp_.nstr(residual,3)}"}
    L_idx = [1, 3, 5, 7, 9, 11]
    if all(rel[i] == 0 for i in L_idx):
        return {"label": "Phantom", "L_100": mp_.nstr(L, 50),
                "relation": [int(c) for c in rel],
                "names": names}
    uses_log = any(int(rel[i]) != 0 for i in (6, 7, 8, 9, 10, 11))
    uses_pi = any(int(rel[i]) != 0 for i in (2, 3, 4, 5))
    label = "Log" if (uses_log and not uses_pi) else "Trans"
    return {"label": label,
            "L_100": mp_.nstr(L, 50),
            "relation": [int(c) for c in rel],
            "names": names,
            "residual": mp_.nstr(residual, 5)}


def deep_validate(coeffs):
    """dps=200, N=2000, residual<1e-100. Run trans basis with logs."""
    mp_.mp.dps = 220
    res = kn_mp_deg2(coeffs, 2000, 220)
    if res is None:
        return {"label": "fail", "msg": "Q=0"}
    L, Lprev = res
    diff = abs(L - Lprev)
    pi_v = mp_.pi; ln2 = mp_.log(2); ln3 = mp_.log(3); ln5 = mp_.log(5)
    # First Alg/Rat at high precision
    rat_basis = [L ** k for k in range(5)]
    try:
        rel = mp_.pslq(rat_basis, maxcoeff=10**8)
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(int(c) * x for c, x in zip(rel, rat_basis)))
        if residual < mp_.mpf(10) ** (-100):
            label = "Rat" if all(int(c) == 0 for c in rel[2:]) else "Alg"
            return {"label": label,
                    "L_200": mp_.nstr(L, 200),
                    "tail_diff": mp_.nstr(diff, 5),
                    "relation": [int(c) for c in rel],
                    "residual": mp_.nstr(residual, 5)}
    # Log basis (Le_logext)
    basis_Le = [L * ln2, L * ln3, L * ln5, mp_.mpf(1), L]
    names_Le = ["L*log2", "L*log3", "L*log5", "1", "L"]
    try:
        rel = mp_.pslq(basis_Le, maxcoeff=10**12, tol=mp_.mpf(10) ** (-120))
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(int(c) * x for c, x in zip(rel, basis_Le)))
        if residual < mp_.mpf(10) ** (-100):
            if not all(rel[i] == 0 for i in (0, 1, 2, 4)):
                return {"label": "Log",
                        "L_200": mp_.nstr(L, 200),
                        "tail_diff": mp_.nstr(diff, 5),
                        "relation": [int(c) for c in rel],
                        "names": names_Le,
                        "residual": mp_.nstr(residual, 5)}
    # Trans basis (Standard A)
    PI = pi_v
    Z2 = mp_.zeta(2); Z3 = mp_.zeta(3)
    basis_A = [mp_.mpf(1), L, PI, PI ** 2, PI ** 3, PI ** 4,
               ln2, ln3, ln5, Z2, Z3]
    names_A = ["1", "L", "pi", "pi^2", "pi^3", "pi^4",
               "log2", "log3", "log5", "zeta2", "zeta3"]
    try:
        rel = mp_.pslq(basis_A, maxcoeff=10**12, tol=mp_.mpf(10) ** (-120))
    except Exception:
        rel = None
    if rel is not None:
        residual = abs(sum(int(c) * x for c, x in zip(rel, basis_A)))
        if residual < mp_.mpf(10) ** (-100):
            if rel[1] != 0:
                return {"label": "Trans",
                        "L_200": mp_.nstr(L, 200),
                        "tail_diff": mp_.nstr(diff, 5),
                        "relation": [int(c) for c in rel],
                        "names": names_A,
                        "residual": mp_.nstr(residual, 5)}
    return {"label": "Desert_or_unidentified",
            "L_200": mp_.nstr(L, 200),
            "tail_diff": mp_.nstr(diff, 5)}


def main():
    t0 = time.time()
    data = json.loads(INPUT.read_text())
    s3_hits = data["step3_extended_b1_8_to_12"]["full_sweep_extra_hits"]
    s4 = data["step4_alternative_ratios"]

    out = {"step3_reclassified": [], "step4_reclassified": []}

    # Step 3 hits — reclassify all 362
    print(f"[Reclassify] Step 3 hits: {len(s3_hits)}")
    s3_summary = {"Log": 0, "Trans": 0, "Alg": 0, "Rat": 0,
                  "Phantom": 0, "Desert": 0, "fail": 0}
    s3_genuine = []
    for i, rec in enumerate(s3_hits):
        coeffs = tuple(rec["coeffs"])
        rc = reclassify_one(coeffs)
        rc["coeffs"] = list(coeffs)
        s3_summary[rc["label"]] = s3_summary.get(rc["label"], 0) + 1
        out["step3_reclassified"].append(rc)
        if rc["label"] in ("Log", "Trans"):
            s3_genuine.append(rc)
        if (i + 1) % 50 == 0:
            print(f"  ... {i+1}/{len(s3_hits)} processed", flush=True)
    print(f"  Step 3 reclassified summary: {s3_summary}")

    # Deep-validate step 3 genuine candidates
    print(f"[Deep] Step 3 genuine candidates to deep-validate: {len(s3_genuine)}")
    deep3 = []
    for rc in s3_genuine:
        coeffs = tuple(rc["coeffs"])
        dv = deep_validate(coeffs)
        dv["coeffs"] = list(coeffs)
        dv["stage_c_label"] = rc["label"]
        deep3.append(dv)
        print(f"  {coeffs}: {dv['label']}  L={dv.get('L_200','')[:40]}...")
    out["step3_deep_validated"] = deep3

    # Step 4 hits — reclassify each ratio's full_sweep_records
    print(f"\n[Reclassify] Step 4 by ratio:")
    step4_out = []
    for ratio_block in s4:
        ratio = ratio_block["ratio"]
        full_hits = ratio_block.get("full_sweep_records", [])
        bs_hits = ratio_block.get("bauer_stern_records", [])
        print(f"  ratio={ratio}: {len(full_hits)} full-sweep hits, "
              f"{len(bs_hits)} BS probes")
        rc_summary = {"Log": 0, "Trans": 0, "Alg": 0, "Rat": 0,
                      "Phantom": 0, "Desert": 0, "fail": 0}
        rc_records = []
        genuine = []
        for rec in full_hits:
            coeffs = tuple(rec["coeffs"])
            rc = reclassify_one(coeffs)
            rc["coeffs"] = list(coeffs)
            rc_summary[rc["label"]] = rc_summary.get(rc["label"], 0) + 1
            rc_records.append(rc)
            if rc["label"] in ("Log", "Trans"):
                genuine.append(rc)
        # BS probes deep-validate (all targets)
        bs_deep = []
        for rec in bs_hits:
            coeffs = tuple(rec["coeffs"])
            dv = deep_validate(coeffs)
            dv["coeffs"] = list(coeffs)
            bs_deep.append(dv)
            print(f"    BS-deep {coeffs}: {dv['label']}")
        deep_genuine = []
        for rc in genuine:
            coeffs = tuple(rc["coeffs"])
            dv = deep_validate(coeffs)
            dv["coeffs"] = list(coeffs)
            dv["stage_c_label"] = rc["label"]
            deep_genuine.append(dv)
            print(f"    Deep {coeffs}: {dv['label']}")
        step4_out.append({
            "ratio": ratio,
            "reclassified_summary": rc_summary,
            "reclassified": rc_records,
            "bs_deep_validated": bs_deep,
            "deep_validated_genuine": deep_genuine,
        })
    out["step4_reclassified"] = step4_out
    out["wall_seconds"] = round(time.time() - t0, 1)

    OUT.write_text(json.dumps(out, indent=2, default=str))
    print(f"\nWrote {OUT}")
    print(f"Wall: {out['wall_seconds']}s")


if __name__ == "__main__":
    main()
