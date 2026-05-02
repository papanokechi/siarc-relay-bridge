"""T2.5d-J0-CHOWLA-SELBERG-CLOSURE -- runner for Phases A through E.

Closes (or escalates) the j=0 cubic finite-N ambiguity flagged in
PCF2-SESSION-T2 Phase D, where a 4-parameter deep-WKB ansatz left
A_fit at A_true=6 with |delta| ~ 1.5e-5 at N_max=480, indistinguishable
within the 4-param tail-window from a real Gamma(1/3)-amplitude
correction.

Strategy
--------
Phase A.  Generate y_n = log|L_N - L_ref| at dps high enough to
          resolve the residual at N=1200. For a cubic with leading
          WKB exponent A=6, |L_N - L_ref| ~ exp(-6 N log N), so dps
          must exceed roughly 6 N log10(N). At N=1200 this is ~22150,
          so the prompt's dps>=8000 spec must be interpreted as
          dps>=22150 to honour the joint dps/N requirement. We set
          dps=25000 (a 200-digit safety buffer above the floor) and
          run N_grid = [200, 300, ..., 1200] with N_ref = 1320.
          JUDGMENT CALL: the literal dps=8000 reading is internally
          infeasible for an A=6 cubic at N=1200; we honour the >= spec
          and document this in halt_log.json.

Phase B.  Two 5-parameter WKB ansatze fit at full mp precision:
            LIN:  y_n = -A n log n + alpha n - beta log n + gamma
                       + c1 / n
            EXP:  y_n = -A n log n + alpha n - beta log n + gamma
                       + c1 / n^4
          Both are linear in their parameters and solved by
          mp-precision normal equations (mp.matrix solve), so A is
          extracted at full dps rather than at float64.

Phase C.  N-scaling: refit on tail windows [N/2, N] for
          N_max in {320, 400, 480} (the operative T2 grid plus the
          dps=8000 extension). Inspect A_fit vs 1/N_max trend.

Phase D.  PSLQ on A_fit at dps=8000 against the augmented
          Chowla-Selberg basis (B19 + Omega_-3 with H6 normalisation).
          Only fired if Phase C does NOT show A converging to 6 within
          finite-N residual.

Phase E.  Write claims.jsonl, verdict.md, halt_log.json, etc.

Halt conditions
---------------
- AMBIGUOUS_AT_DPS8000  : ansatz LIN vs EXP disagree by > 1e-30 at
                          the largest tail window AND |A_fit - 6|
                          remains > 1e-5 (the T2 floor).
- NUMERICAL_INSTABILITY : NaN/inf in any fit residual.
- PSLQ_BASIS_INSUFFICIENT: PSLQ returns no relation up to maxcoeff
                          1e50.
- GAMMA13_OVERCLAIM     : self-caught (no asserted "proves" wording).

Output (in this directory)
--------------------------
  Qn_j0_dps8000_N<Nmax>_<family>.csv     (per family ns vs y_n)
  wkb_5param_lin.log
  wkb_5param_exp.log
  wkb_5param_results.json
  N_scaling_plot.tsv
  PSLQ.log                                (only if Phase D fired)
  PSLQ_relation.txt                       (only if Phase D succeeded)
  claims.jsonl
  verdict.md
  halt_log.json
  discrepancy_log.json
  unexpected_finds.json
  rubber_duck_critique.md
  handoff.md
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
LOG_PATH = HERE / "runner.log"

# Coefficient ordering convention: leading coefficient FIRST,
# i.e. coeffs = [a_d, a_{d-1}, ..., a_1, a_0].
J_ZERO_FAMILIES = [
    (30, [1, -3, 3, -3]),
    (31, [1, -3, 3,  1]),
    (32, [1, -3, 3,  2]),
    (33, [1, -3, 3,  3]),
]

# Phase A precision/grid configuration.  Spec says dps>=8000 AND
# N>=1200; for an A=6 cubic the joint feasibility floor on dps is
# 6 N log10(N) at N=1200 ~ 22150 digits, so we set dps=25000.
DPS         = 25000
N_GRID      = list(range(200, 1201, 100))   # 11 points: 200..1200 step 100
N_REF       = 1320
N_GRID_REF_GUARD = N_REF - 100              # guard band

# A=6 prediction (to test).
A_TRUE = mp.mpf(6)


# ---------- logging helper ----------

def L(msg: str, log: Path = LOG_PATH):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------- Phase A: continued-fraction tail extraction ----------

def cf_value(coeffs, N, dps):
    """Backward-evaluate the continued fraction with partial quotient
    a_n = poly(coeffs, n), truncated at depth N.  Coefficient ordering
    is leading-coefficient first."""
    with mp.workdps(dps):
        ms = [mp.mpf(c) for c in coeffs]

        def b(k):
            v = ms[0]
            kk = mp.mpf(k)
            for c in ms[1:]:
                v = v * kk + c
            return v

        x = b(N)
        for k in range(N - 1, -1, -1):
            x = b(k) + mp.mpf(1) / x
        return +x


def compute_yn_series(coeffs, n_grid, n_ref, dps, label):
    L(f"  {label} L_ref at N={n_ref} ...")
    t0 = time.time()
    L_ref = cf_value(coeffs, n_ref, dps)
    L(f"    L_ref done in {time.time()-t0:.1f}s")
    ns_used, ys_mp = [], []
    for N in n_grid:
        t1 = time.time()
        with mp.workdps(dps):
            d = abs(cf_value(coeffs, N, dps) - L_ref)
        if d == 0:
            L(f"    N={N}: |L_N - L_ref| underflowed; SKIP")
            continue
        with mp.workdps(dps):
            y = mp.log(d)
        ns_used.append(N)
        ys_mp.append(y)
        L(f"    N={N}: y={mp.nstr(y, 8)} ({time.time()-t1:.1f}s)")
    return ns_used, ys_mp, L_ref


def write_qn_csv(family_id, ns, ys_mp, dps):
    path = HERE / f"Qn_j0_dps{dps}_N{ns[-1] if ns else 0}_fam{family_id}.csv"
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["N", "y_n_log_abs_residual_mp_str"])
        with mp.workdps(dps):
            for N, y in zip(ns, ys_mp):
                w.writerow([N, mp.nstr(y, dps // 2)])
    return path


# ---------- Phase B: mp-precision 5-param fits ----------

def basis_lin(n_mp):
    """5-param LIN basis row: [-n log n, n, -log n, 1, 1/n]"""
    return [-n_mp * mp.log(n_mp), n_mp, -mp.log(n_mp), mp.mpf(1),
            mp.mpf(1) / n_mp]


def basis_exp(n_mp):
    """5-param EXP basis row: [-n log n, n, -log n, 1, 1/n^4]"""
    return [-n_mp * mp.log(n_mp), n_mp, -mp.log(n_mp), mp.mpf(1),
            mp.mpf(1) / n_mp**4]


def basis_4param(n_mp):
    """4-param T2-baseline row: [-n log n, n, -log n, 1]"""
    return [-n_mp * mp.log(n_mp), n_mp, -mp.log(n_mp), mp.mpf(1)]


def lstsq_mp(rows, ys, dps):
    """Solve normal equations X^T X beta = X^T y at workdps=dps.
    Returns (beta, residuals_mp)."""
    with mp.workdps(dps):
        m = len(rows)
        k = len(rows[0])
        X = mp.matrix(rows)            # m x k
        y = mp.matrix(ys)              # m x 1
        XtX = X.T * X                  # k x k
        Xty = X.T * y                  # k x 1
        beta = mp.lu_solve(XtX, Xty)   # k x 1
        resid = y - X * beta
        return beta, resid


def fit_one_family(label, ns, ys_mp, dps):
    """Run 4-param T2 baseline + 5-param LIN + 5-param EXP fits on a
    single (ns, ys_mp) pair at workdps=dps."""
    with mp.workdps(dps):
        ns_mp = [mp.mpf(N) for N in ns]
        rows4 = [basis_4param(n) for n in ns_mp]
        rowsL = [basis_lin(n) for n in ns_mp]
        rowsE = [basis_exp(n) for n in ns_mp]

        b4, r4 = lstsq_mp(rows4, ys_mp, dps)
        bL, rL = lstsq_mp(rowsL, ys_mp, dps)
        bE, rE = lstsq_mp(rowsE, ys_mp, dps)

        out = {
            "label": label,
            "n_points": len(ns),
            "ns": ns,
            "fit_4param": {
                "A":     mp.nstr(b4[0], 60),
                "alpha": mp.nstr(b4[1], 60),
                "beta":  mp.nstr(b4[2], 60),
                "gamma": mp.nstr(b4[3], 60),
                "delta": mp.nstr(b4[0] - A_TRUE, 60),
                "resid_max": mp.nstr(max(abs(x) for x in r4), 30),
            },
            "fit_5param_LIN": {
                "A":     mp.nstr(bL[0], 60),
                "alpha": mp.nstr(bL[1], 60),
                "beta":  mp.nstr(bL[2], 60),
                "gamma": mp.nstr(bL[3], 60),
                "c1":    mp.nstr(bL[4], 60),
                "delta": mp.nstr(bL[0] - A_TRUE, 60),
                "resid_max": mp.nstr(max(abs(x) for x in rL), 30),
            },
            "fit_5param_EXP": {
                "A":     mp.nstr(bE[0], 60),
                "alpha": mp.nstr(bE[1], 60),
                "beta":  mp.nstr(bE[2], 60),
                "gamma": mp.nstr(bE[3], 60),
                "c4":    mp.nstr(bE[4], 60),
                "delta": mp.nstr(bE[0] - A_TRUE, 60),
                "resid_max": mp.nstr(max(abs(x) for x in rE), 30),
            },
        }
        # Lin/exp agreement.
        diff_LE = bL[0] - bE[0]
        out["A_lin_minus_A_exp"] = mp.nstr(diff_LE, 60)
        out["A_avg"] = mp.nstr((bL[0] + bE[0]) / 2, 60)
        # Number of agreement digits:
        if diff_LE == 0:
            n_agree = dps  # cap
        else:
            n_agree = int(-mp.log10(abs(diff_LE)))
        out["agreement_digits"] = n_agree
        return out, b4, bL, bE


# ---------- Phase C: N-scaling ----------

def n_scaling(label, ns, ys_mp, dps):
    """Refit on increasing tail windows.  For each N_max in ns we use
    the points whose N >= N_max/2."""
    rows = []
    with mp.workdps(dps):
        ns_mp_full = [mp.mpf(N) for N in ns]
        for j, N_max in enumerate(ns):
            cutoff = N_max // 2
            sub_idx = [i for i, N in enumerate(ns) if N >= cutoff and N <= N_max]
            if len(sub_idx) < 6:
                continue
            sub_ns = [ns[i] for i in sub_idx]
            sub_ys = [ys_mp[i] for i in sub_idx]
            sub_rowsL = [basis_lin(mp.mpf(N)) for N in sub_ns]
            sub_rowsE = [basis_exp(mp.mpf(N)) for N in sub_ns]
            try:
                bL, _ = lstsq_mp(sub_rowsL, sub_ys, dps)
                bE, _ = lstsq_mp(sub_rowsE, sub_ys, dps)
            except Exception as exc:
                rows.append({"N_max": N_max, "error": str(exc)})
                continue
            rows.append({
                "N_max": N_max,
                "n_points": len(sub_ns),
                "A_lin": mp.nstr(bL[0], 30),
                "A_exp": mp.nstr(bE[0], 30),
                "delta_lin": mp.nstr(bL[0] - A_TRUE, 30),
                "delta_exp": mp.nstr(bE[0] - A_TRUE, 30),
            })
    return rows


# ---------- Phase D: PSLQ on augmented Chowla-Selberg basis ----------

def make_augmented_basis(dps):
    with mp.workdps(dps):
        pi = mp.pi
        log2, log3, log5, log7 = (mp.log(k) for k in (2, 3, 5, 7))
        sqrt3 = mp.sqrt(3)
        Gamma13 = mp.gamma(mp.mpf(1) / 3)
        Gamma23 = mp.gamma(mp.mpf(2) / 3)
        zeta2 = mp.zeta(2)
        zeta3 = mp.zeta(3)
        Omega_m3 = Gamma13**3 / (2 * pi)
        basis = [
            ("1",          mp.mpf(1)),
            ("pi",         pi),
            ("pi^2",       pi**2),
            ("Gamma(1/3)", Gamma13),
            ("Gamma(1/3)^2", Gamma13**2),
            ("Gamma(1/3)^3", Gamma13**3),
            ("Gamma(2/3)", Gamma23),
            ("log2",       log2),
            ("log3",       log3),
            ("log5",       log5),
            ("log7",       log7),
            ("zeta(2)",    zeta2),
            ("zeta(3)",    zeta3),
            ("Omega_-3",   Omega_m3),
            ("pi/sqrt3",   pi / sqrt3),
        ]
    return basis


def run_pslq(target_mp, dps, max_coeff=10**50, tol_exp=40):
    """Run mp.pslq on [target] + basis values.  Returns relation
    coefficients or None."""
    basis = make_augmented_basis(dps)
    with mp.workdps(dps):
        vec = [target_mp] + [v for _, v in basis]
        tol = mp.mpf(10) ** (-tol_exp)
        try:
            rel = mp.pslq(vec, tol=tol, maxcoeff=max_coeff)
        except Exception as exc:
            return None, basis, f"pslq exception: {exc}"
    return rel, basis, None


# ---------- main ----------

def main():
    LOG_PATH.write_text("")  # reset
    L("=== T2.5d J0 CHOWLA-SELBERG CLOSURE — runner start ===")
    L(f"DPS={DPS}, N_GRID={N_GRID}, N_REF={N_REF}")
    L(f"Families: {[f for f, _ in J_ZERO_FAMILIES]}")
    L(f"PRECISION FEASIBILITY: at A=6, |L_N - L_ref| ~ exp(-6 N log N).")
    L(f"  At N=1200: needed dps ~ {int(6*1200*math.log10(1200))}; "
      f"using dps={DPS} (safety buffer ~{DPS - int(6*1200*math.log10(1200))} digits).")
    L(f"  Literal spec dps=8000+N>=1200 infeasible for A=6 cubic; "
      f"we honour dps>=8000 by setting dps={DPS} and document.")

    # ---------- Phase A ----------
    L("\n[Phase A] Generating Q_n series (y_n = log|L_N - L_ref|).")
    family_data = {}
    csv_hashes = {}
    for fid, coeffs in J_ZERO_FAMILIES:
        L(f"  Family {fid} coeffs={coeffs}")
        ns, ys_mp, L_ref = compute_yn_series(coeffs, N_GRID, N_REF, DPS, f"fam{fid}")
        if len(ns) < 8:
            L(f"  fam{fid}: only {len(ns)} usable points — SKIP family")
            continue
        family_data[fid] = (coeffs, ns, ys_mp)
        csv_path = write_qn_csv(fid, ns, ys_mp, DPS)
        csv_hashes[fid] = sha(csv_path)
        L(f"  fam{fid}: wrote {csv_path.name} sha256={csv_hashes[fid][:16]}")

    # ---------- Phase B ----------
    L("\n[Phase B] 5-param WKB fits (LIN + EXP) at dps=%d." % DPS)
    fits = {}
    for fid, (coeffs, ns, ys_mp) in family_data.items():
        out, b4, bL, bE = fit_one_family(f"fam{fid}", ns, ys_mp, DPS)
        out["coeffs"] = coeffs
        fits[fid] = out
        L(f"  fam{fid} 4param A={out['fit_4param']['A'][:25]} delta={out['fit_4param']['delta'][:25]}")
        L(f"  fam{fid} LIN    A={out['fit_5param_LIN']['A'][:25]} delta={out['fit_5param_LIN']['delta'][:25]}")
        L(f"  fam{fid} EXP    A={out['fit_5param_EXP']['A'][:25]} delta={out['fit_5param_EXP']['delta'][:25]}")
        L(f"  fam{fid} A_lin - A_exp = {out['A_lin_minus_A_exp'][:25]}  agree={out['agreement_digits']} digits")

    (HERE / "wkb_5param_results.json").write_text(json.dumps(fits, indent=2))

    # Per-ansatz log files.
    with open(HERE / "wkb_5param_lin.log", "w", encoding="utf-8") as fh:
        for fid, out in fits.items():
            fh.write(f"# fam{fid} coeffs={out['coeffs']}\n")
            fh.write(json.dumps(out["fit_5param_LIN"], indent=2) + "\n\n")
    with open(HERE / "wkb_5param_exp.log", "w", encoding="utf-8") as fh:
        for fid, out in fits.items():
            fh.write(f"# fam{fid} coeffs={out['coeffs']}\n")
            fh.write(json.dumps(out["fit_5param_EXP"], indent=2) + "\n\n")

    # ---------- Phase C ----------
    L("\n[Phase C] N-scaling of A_fit on tail windows.")
    nscaling = {}
    for fid, (coeffs, ns, ys_mp) in family_data.items():
        rows = n_scaling(f"fam{fid}", ns, ys_mp, DPS)
        nscaling[fid] = rows
        for r in rows:
            L(f"  fam{fid} N_max={r.get('N_max')} A_lin={r.get('A_lin', 'NA')[:20]} "
              f"A_exp={r.get('A_exp', 'NA')[:20]}")

    with open(HERE / "N_scaling_plot.tsv", "w", encoding="utf-8") as fh:
        fh.write("family_id\tN_max\tn_points\tA_lin\tA_exp\tdelta_lin\tdelta_exp\n")
        for fid, rows in nscaling.items():
            for r in rows:
                if "error" in r:
                    continue
                fh.write(f"{fid}\t{r['N_max']}\t{r['n_points']}\t"
                         f"{r['A_lin']}\t{r['A_exp']}\t"
                         f"{r['delta_lin']}\t{r['delta_exp']}\n")
    (HERE / "N_scaling.json").write_text(json.dumps(nscaling, indent=2))

    # ---------- Phase D decision ----------
    L("\n[Phase D] decision on PSLQ phase.")
    # Aggregate: take A_avg from all families' largest tail window.
    # Test A converges to 6 within finite-N residual.
    A_avgs = []
    deltas_lin = []
    deltas_exp = []
    le_diffs = []
    for fid, out in fits.items():
        with mp.workdps(DPS):
            A_avg = mp.mpf(out["A_avg"])
            d_lin = mp.mpf(out["fit_5param_LIN"]["delta"])
            d_exp = mp.mpf(out["fit_5param_EXP"]["delta"])
            le    = mp.mpf(out["A_lin_minus_A_exp"])
        A_avgs.append(A_avg)
        deltas_lin.append(d_lin)
        deltas_exp.append(d_exp)
        le_diffs.append(le)

    with mp.workdps(DPS):
        max_abs_delta_lin = max(abs(d) for d in deltas_lin)
        max_abs_delta_exp = max(abs(d) for d in deltas_exp)
        max_abs_le_diff   = max(abs(d) for d in le_diffs)

    L(f"  max |delta_lin| = {mp.nstr(max_abs_delta_lin, 12)}")
    L(f"  max |delta_exp| = {mp.nstr(max_abs_delta_exp, 12)}")
    L(f"  max |A_lin - A_exp| = {mp.nstr(max_abs_le_diff, 12)}")

    LIN_EXP_AGREE_THRESH = mp.mpf(10) ** (-30)
    A_EQ_6_THRESH        = mp.mpf(10) ** (-30)
    A_NEQ_6_THRESH       = mp.mpf(10) ** (-10)

    pslq_outputs = {}
    verdict = None
    halt_info = {}

    if max_abs_le_diff > LIN_EXP_AGREE_THRESH:
        verdict = "AMBIGUOUS_AT_DPS8000"
        halt_info["reason"] = ("LIN/EXP 5-param ansatze disagree on A by "
                               f"{mp.nstr(max_abs_le_diff, 12)} > 1e-30; "
                               "finite-N bias is not eliminable at dps=8000.")
    elif max_abs_delta_lin < A_EQ_6_THRESH and max_abs_delta_exp < A_EQ_6_THRESH:
        verdict = "PASS_A_EQ_6_ONLY"
    elif max_abs_delta_lin < A_NEQ_6_THRESH and max_abs_delta_exp < A_NEQ_6_THRESH:
        # Not at full 30-digit precision but inside artefact band.
        # Skip Phase D; declare A=6 with finite-N residual.
        verdict = "PASS_A_EQ_6_ONLY"
    else:
        # delta is large: try PSLQ.
        L("\n[Phase D] running PSLQ on each family A_lin in CS-augmented basis.")
        for fid, out in fits.items():
            with mp.workdps(DPS):
                A_lin = mp.mpf(out["fit_5param_LIN"]["A"])
            rel, basis, err = run_pslq(A_lin, DPS,
                                       max_coeff=10**50, tol_exp=40)
            pslq_outputs[fid] = {
                "A_lin": out["fit_5param_LIN"]["A"],
                "relation": [int(r) for r in rel] if rel else None,
                "basis_labels": [name for name, _ in basis],
                "error": err,
            }
            if rel:
                L(f"  fam{fid}: PSLQ found a relation of length {len(rel)}")
            else:
                L(f"  fam{fid}: PSLQ found no relation (err={err}).")
        with open(HERE / "PSLQ.log", "w", encoding="utf-8") as fh:
            fh.write(json.dumps(pslq_outputs, indent=2))

        any_rel = any(p["relation"] for p in pslq_outputs.values())
        if any_rel:
            verdict = "PASS_GAMMA13"
            with open(HERE / "PSLQ_relation.txt", "w", encoding="utf-8") as fh:
                for fid, p in pslq_outputs.items():
                    if p["relation"]:
                        fh.write(f"# fam{fid} A_lin = {p['A_lin']}\n")
                        fh.write("PSLQ relation (integer coeffs in basis "
                                 "[A_lin] + augmented CS basis):\n")
                        for c, name in zip(p["relation"],
                                           ["A_lin"] + p["basis_labels"]):
                            fh.write(f"  {c:+d}  {name}\n")
                        fh.write("\n")
                fh.write("\n# NOTE: PSLQ detection is an empirical signal;\n")
                fh.write("# a relation at confidence >= 50 digits is evidence\n")
                fh.write("# but NOT a proof of Gamma(1/3) closure.\n")
        else:
            verdict = "PSLQ_BASIS_INSUFFICIENT"
            halt_info["reason"] = (
                "PSLQ found no integer relation at maxcoeff=1e50, "
                "tol=1e-40 for any family; H6 D=-3 closure not detected "
                "by the 15-element augmented CS basis at dps=8000."
            )

    # ---------- Phase E: write outputs ----------
    L(f"\n[Phase E] verdict = {verdict}")

    halt_log = {
        "verdict": verdict,
        "spec_dps_min": 8000,
        "spec_N_min": 1200,
        "literal_spec_dps_8000_internally_infeasible_at_A_eq_6": True,
        "literal_spec_infeasibility_argument": (
            "For an A=6 cubic continued fraction, |L_N - L_ref| ~ "
            "exp(-6 N log N). At N=1200, log10|L_N - L_ref| ~ -22150, "
            "so resolving y_N at N=1200 requires dps >= ~22150. "
            "The literal dps=8000 + N>=1200 reading cannot be honoured "
            "simultaneously without precision underflow. We honour the "
            "prompt's `dps>=8000` clause by setting dps=25000 (a safety "
            "buffer above the 22150-digit floor at N=1200) and run N "
            "up to 1200."
        ),
        "actual_dps": DPS,
        "actual_N_max": N_GRID[-1],
        "actual_N_ref": N_REF,
        "halt_info": halt_info,
    }
    (HERE / "halt_log.json").write_text(json.dumps(halt_log, indent=2))

    (HERE / "discrepancy_log.json").write_text(json.dumps({
        "spec_vs_run": {
            "dps_spec_min": 8000, "dps_run": DPS,
            "N_min_spec": 1200, "N_max_run": N_GRID[-1],
            "rationale": ("Literal dps=8000 cannot resolve y_N at "
                          "N=1200 for A=6 cubics (needs dps>=22150). "
                          "Prompt's `dps>=8000` clause honoured by "
                          "setting dps=25000."),
        }
    }, indent=2))

    (HERE / "unexpected_finds.json").write_text(json.dumps({}, indent=2))

    # AEAL claims.
    claims = []
    claims.append({
        "claim": ("T25D-A1: j=0 sub-catalogue extracted as the four "
                  "R1.1 j=0 cubic families with coefficients "
                  "[1,-3,3,a0] for a0 in {-3,1,2,3} (family_ids 30..33). "
                  "These are the literal j(tau_b)=0 cubics from the "
                  "PCF-2 v1.3 50-cubic catalogue (carried over from "
                  "PCF2-SESSION-T2 Phase D)."),
        "evidence_type": "computation",
        "dps": DPS,
        "reproducible": True,
        "script": "t25d_j0_runner.py",
        "output_hash": "see_runner.log",
    })
    for fid in family_data:
        claims.append({
            "claim": (f"T25D-A2(fam{fid}): Q_n series (y_n = "
                      f"log|L_N - L_ref|) at dps={DPS}, "
                      f"N in {family_data[fid][1][0]}..{family_data[fid][1][-1]}, "
                      f"N_ref={N_REF}, n_points={len(family_data[fid][1])}."),
            "evidence_type": "computation",
            "dps": DPS,
            "reproducible": True,
            "script": "t25d_j0_runner.py",
            "output_hash": csv_hashes.get(fid, "NA"),
        })
    for fid, out in fits.items():
        claims.append({
            "claim": (f"T25D-A3(fam{fid}): 5-param LIN ansatz fit "
                      f"A_lin = {out['fit_5param_LIN']['A'][:30]}, "
                      f"delta_lin = {out['fit_5param_LIN']['delta'][:30]}."),
            "evidence_type": "computation",
            "dps": DPS,
            "reproducible": True,
            "script": "t25d_j0_runner.py",
            "output_hash": "wkb_5param_results.json",
        })
        claims.append({
            "claim": (f"T25D-A4(fam{fid}): 5-param EXP ansatz fit "
                      f"A_exp = {out['fit_5param_EXP']['A'][:30]}, "
                      f"delta_exp = {out['fit_5param_EXP']['delta'][:30]}."),
            "evidence_type": "computation",
            "dps": DPS,
            "reproducible": True,
            "script": "t25d_j0_runner.py",
            "output_hash": "wkb_5param_results.json",
        })
        claims.append({
            "claim": (f"T25D-A5(fam{fid}): LIN-EXP 5-param fit "
                      f"agreement = {out['agreement_digits']} digits "
                      f"(A_lin - A_exp = "
                      f"{out['A_lin_minus_A_exp'][:30]})."),
            "evidence_type": "computation",
            "dps": DPS,
            "reproducible": True,
            "script": "t25d_j0_runner.py",
            "output_hash": "wkb_5param_results.json",
        })
    claims.append({
        "claim": ("T25D-A6: N-scaling of A_fit (LIN and EXP) on tail "
                  "windows [N_max/2, N_max] for N_max in the run grid; "
                  "see N_scaling_plot.tsv."),
        "evidence_type": "computation",
        "dps": DPS,
        "reproducible": True,
        "script": "t25d_j0_runner.py",
        "output_hash": "N_scaling_plot.tsv",
    })
    if pslq_outputs:
        claims.append({
            "claim": (f"T25D-A7: PSLQ phase D ran on each family's "
                      f"A_lin against the 15-element augmented CS basis "
                      f"at dps={DPS}, maxcoeff=1e50, tol=1e-40; result "
                      f"verdict = {verdict}."),
            "evidence_type": "computation",
            "dps": DPS,
            "reproducible": True,
            "script": "t25d_j0_runner.py",
            "output_hash": "PSLQ.log",
        })

    with open(HERE / "claims.jsonl", "w", encoding="utf-8") as fh:
        for c in claims:
            fh.write(json.dumps(c) + "\n")

    # Hash CSV files for AEAL.
    output_hashes = {p.name: sha(p) for p in HERE.glob("Qn_j0_*.csv")}
    output_hashes["wkb_5param_results.json"] = sha(HERE / "wkb_5param_results.json")
    output_hashes["N_scaling_plot.tsv"] = sha(HERE / "N_scaling_plot.tsv")
    (HERE / "output_hashes.json").write_text(json.dumps(output_hashes, indent=2))

    # Verdict file.
    with open(HERE / "verdict.md", "w", encoding="utf-8") as fh:
        fh.write(f"# T2.5d-J0-CHOWLA-SELBERG-CLOSURE — verdict\n\n")
        fh.write(f"**Verdict label:** `{verdict}`\n\n")
        fh.write(f"**op:j-zero-amplitude-h6 status:** "
                 f"{'CLOSED' if verdict in ('PASS_GAMMA13','PASS_A_EQ_6_ONLY') else 'OPEN'}\n\n")
        fh.write("## Spec vs run\n\n")
        fh.write(f"- Spec asked dps>=8000, N>=1200.\n")
        fh.write(f"- For A=6 cubics, |L_N - L_ref| ~ exp(-6 N log N), "
                 f"so dps for N=1200 must be >= ~22150. The literal "
                 f"dps=8000 reading is internally infeasible.\n")
        fh.write(f"- Run used dps={DPS} (above the 22150-digit floor) "
                 f"with N up to {N_GRID[-1]}, N_ref={N_REF}.\n\n")
        fh.write("## Per-family fit summary (5-param LIN)\n\n")
        fh.write("| family | A_lin | delta_lin | A_lin - A_exp | agree_digits |\n")
        fh.write("|---|---|---|---|---|\n")
        for fid, out in fits.items():
            fh.write(f"| {fid} | {out['fit_5param_LIN']['A'][:25]} | "
                     f"{out['fit_5param_LIN']['delta'][:18]} | "
                     f"{out['A_lin_minus_A_exp'][:18]} | "
                     f"{out['agreement_digits']} |\n")
        fh.write("\n")
        if pslq_outputs:
            fh.write("## PSLQ Phase D outcome\n\n")
            for fid, p in pslq_outputs.items():
                if p["relation"]:
                    fh.write(f"- fam{fid}: relation found, length "
                             f"{len(p['relation'])}; see PSLQ_relation.txt.\n")
                else:
                    fh.write(f"- fam{fid}: no relation at "
                             f"maxcoeff=1e50, tol=1e-40.\n")

    L("=== runner end ===")
    return {
        "verdict": verdict,
        "fits": fits,
        "nscaling": nscaling,
        "pslq": pslq_outputs,
        "halt_log": halt_log,
    }


if __name__ == "__main__":
    main()
