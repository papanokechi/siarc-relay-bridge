"""T37K-EXTEND-A3-SUBFAMILY runner.

Goal: identify a third A=3 PCF rep (Delta_b not in {-11, -20}), run
017c-style two-stage windowed fit at dps=300 / N=2000, K_lead in
{22,25,28} x W1 in {(800,1200),(800,1500),(800,1800)}, and test
whether the candidate A=3 sub-family relation

    36 * a_1 = 4 * Delta_b - 9     (i.e., (2A)^2 * a_1 = 4*Delta_b - 9 at A=3)

generalizes from V_quad (Delta_b=-11) and QL15 (Delta_b=-20).

Convention: Birkhoff coefficients [a2,a1,a0]; PCF parameters
(alpha, beta, gamma, delta, epsilon) with b(n) = alpha n^2 + beta n + gamma,
a(n) = delta n + epsilon. T_n := a_n * zeta_*^n / Gamma(n);
T_n_lead = C * (1 + a_1/n + a_2/n^2 + ...).

Recurrence kernel: lifted from
T35-STOKES-MULTIPLIER-DISCRIMINATION/derive_recurrence.py +
T37E-EXTENDED-RECURRENCE/derive_recurrence_dps400.py (verbatim).
Two-stage fit: column-scaled normal equations (017c style).
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import mpmath as mp


HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parent.parent.parent
T37J_DIR = BRIDGE / "sessions" / "2026-05-02" / "T37J-A1-CLOSED-FORM-PSLQ"
T37E_DIR = BRIDGE / "sessions" / "2026-05-02" / "T37E-EXTENDED-RECURRENCE"
T35_DIR  = BRIDGE / "sessions" / "2026-05-02" / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

DPS = 300
WORK_DPS = 350         # guard
N_MAX = 2000

K_LEADS = [22, 25, 28]
W1S = [(800, 1200), (800, 1500), (800, 1800)]
K_NEXT = 4
W2 = (40, 100)

ENVELOPE_GATE = mp.mpf("1e-25")    # halt T37K_FIT_DIVERGED if half_range > this
RELATION_TIGHT = mp.mpf("1e-30")
RELATION_LOOSE = mp.mpf("1e-3")

PSLQ_TOL_TIGHT = mp.mpf(10) ** (-30)
PSLQ_TOL_HARD  = mp.mpf(10) ** (-12)
PSLQ_MAXCOEFF  = 10**15

# --------------------------------------------------------------------------
# Bookkeeping
# --------------------------------------------------------------------------

CLAIMS: List[Dict] = []


def sha(payload) -> str:
    if isinstance(payload, (dict, list)):
        s = json.dumps(payload, sort_keys=True, default=str)
    else:
        s = str(payload)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def claim(text: str, etype: str, dps: int, script: str, payload, repro: bool = True) -> None:
    CLAIMS.append({
        "claim": text,
        "evidence_type": etype,
        "dps": dps,
        "reproducible": repro,
        "script": script,
        "output_hash": sha(payload),
    })


def write_claims():
    (HERE / "claims.jsonl").write_text(
        "\n".join(json.dumps(c) for c in CLAIMS) + "\n"
    )


def write_json(name: str, payload):
    (HERE / name).write_text(json.dumps(payload, indent=2, default=str))


def halt(label: str, **details):
    halt_payload = {"label": label, "details": details, "claims_so_far": len(CLAIMS)}
    write_json("halt_log.json", halt_payload)
    write_claims()
    print(f"HALT: {label}")
    sys.exit(0)


# --------------------------------------------------------------------------
# Phase A : third A=3 rep selection
# --------------------------------------------------------------------------

EXISTING_DELTA_B = {
    "V_quad": -11,
    "QL15":   -20,
    "QL05":    8,
    "QL09":    1,
}


def select_third_a3_rep() -> Dict:
    """Parametric enumeration of A=3 PCFs (Delta_b < 0, Delta_b not in {-11,-20}).

    Selection rule (per prompt 017k §A.2):
        (a) smallest |Delta_b - (-15.5)|
        (b) tie-break on lowest |alpha|+|beta|+|gamma|+|delta|+|epsilon|
        (c) require non-degenerate recurrence on test n (delta and/or epsilon != 0)

    We enumerate small-|coeff| candidates with alpha in {1..3}, |beta|<=3,
    |gamma|<=3, delta in {0,1}, epsilon in {0,1}.
    """
    forbidden = {-11, -20}
    candidates = []
    for alpha in (1, 2, 3):
        for beta in range(-3, 4):
            for gamma in range(-3, 4):
                Delta_b = beta * beta - 4 * alpha * gamma
                if Delta_b >= 0:
                    continue              # need A=3
                if Delta_b in forbidden:
                    continue
                for delta in (0, 1):
                    for epsilon in (0, 1):
                        # require non-degenerate: at least one of {delta, epsilon} != 0
                        if delta == 0 and epsilon == 0:
                            continue
                        # require alpha > 0 (already), and integer recurrence well-defined
                        s_abs = abs(alpha) + abs(beta) + abs(gamma) + abs(delta) + abs(epsilon)
                        candidates.append({
                            "alpha": alpha, "beta": beta, "gamma": gamma,
                            "delta": delta, "epsilon": epsilon,
                            "Delta_b": Delta_b,
                            "dist_to_midpoint": abs(Delta_b - (-15.5)),
                            "sum_abs": s_abs,
                        })
    candidates.sort(key=lambda c: (c["dist_to_midpoint"], c["sum_abs"],
                                    abs(c["beta"]), abs(c["gamma"]), -c["epsilon"]))
    if not candidates:
        halt("T37K_NO_THIRD_A3_REP_FOUND",
             reason="parametric enumeration produced no A=3 candidate with Delta_b not in {-11,-20}")
    chosen = candidates[0]
    chosen["id"] = "T37K_A3_third"
    chosen["A_pred"] = 3
    chosen["side"] = "neg"
    chosen["c0_str"] = "+2/sqrt(alpha)"
    chosen["rho_str"] = "-3/2 - beta/alpha"
    chosen["source"] = "parametric enumeration (T37K Phase A.3)"
    return {"chosen": chosen, "shortlist": candidates[:8]}


def crossvalidate_rep(rep: Dict) -> Dict:
    alpha = mp.mpf(rep["alpha"])
    beta  = mp.mpf(rep["beta"])
    gamma = mp.mpf(rep["gamma"])
    Delta_b_computed = beta * beta - 4 * alpha * gamma
    A_computed = 3 if Delta_b_computed < 0 else 4
    # well-defined recurrence: c = 2/sqrt(alpha), diag(1) = alpha c/2 = sqrt(alpha) != 0
    c = mp.mpf(2) / mp.sqrt(alpha)
    diag1 = alpha * c / 2
    return {
        "Delta_b_target": rep["Delta_b"],
        "Delta_b_computed": str(Delta_b_computed),
        "A_target": rep["A_pred"],
        "A_computed": A_computed,
        "diag_at_k1": str(diag1),
        "ok_A": A_computed == rep["A_pred"],
        "ok_Delta_b": abs(Delta_b_computed - mp.mpf(rep["Delta_b"])) < mp.mpf("1e-50"),
        "ok_recurrence_diag_nonzero": diag1 != 0,
    }


# --------------------------------------------------------------------------
# Phase B.1 : Birkhoff a_n recurrence (verbatim t37e kernel)
# --------------------------------------------------------------------------

def derive_a_series(rep: Dict) -> Tuple[List[mp.mpf], mp.mpf, mp.mpf]:
    mp.mp.dps = WORK_DPS
    alpha = mp.mpf(rep["alpha"])
    beta  = mp.mpf(rep["beta"])
    gamma = mp.mpf(rep["gamma"])
    delta = mp.mpf(rep["delta"])
    epsi  = mp.mpf(rep["epsilon"])
    sign  = mp.mpf(+1)                  # T35-canonical
    c = sign * mp.mpf(2) / mp.sqrt(alpha)
    rho = mp.mpf(-3) / 2 - beta / alpha
    zeta_star = 2 * abs(c)

    coeff_km1_quad = alpha / mp.mpf(16)
    base_km1 = gamma - beta * beta / (4 * alpha)
    Ukm2 = -c * delta / 2
    base_km3 = epsi - beta * delta / (2 * alpha)
    diag_premul = alpha * c / 2

    a = [mp.mpf(0)] * (N_MAX + 1)
    a[0] = mp.mpf(1)
    for k in range(1, N_MAX + 1):
        two_km1 = mp.mpf(2 * k - 1)
        Ukm1 = coeff_km1_quad * (two_km1 ** 2) + base_km1
        Ukm3 = (two_km1 / 4) * delta + base_km3
        rhs = Ukm1 * a[k - 1]
        if k - 2 >= 0:
            rhs += Ukm2 * a[k - 2]
        if k - 3 >= 0:
            rhs += Ukm3 * a[k - 3]
        diag = diag_premul * mp.mpf(k)
        a[k] = rhs / diag
    return a, c, zeta_star


def write_recurrence_csv(a: Sequence[mp.mpf], path: Path) -> str:
    h = hashlib.sha256()
    with path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["n", "a_n_real"])
        for n, val in enumerate(a):
            s = mp.nstr(val, WORK_DPS, strip_zeros=False)
            w.writerow([n, s])
            h.update(f"{n},{s}\n".encode("utf-8"))
    return h.hexdigest()[:16]


# --------------------------------------------------------------------------
# Phase B.2 : two-stage windowed fit (017c style)
# --------------------------------------------------------------------------

def column_scaled_solve(cols: List[List[mp.mpf]], b: List[mp.mpf]) -> Tuple[List[mp.mpf], mp.mpf, int]:
    """017c column-scaled normal-equations solver via sym eigendecomp.

    Returns (x, cond, rank).
    """
    M = len(b)
    K = len(cols)
    scales = []
    for col in cols:
        s = mp.mpf(0)
        for v in col:
            s += v * v
        scales.append(mp.sqrt(s))
    AtA = [[mp.mpf(0)] * K for _ in range(K)]
    Atb = [mp.mpf(0)] * K
    for i in range(K):
        si = scales[i]
        for j in range(i, K):
            dot = mp.mpf(0)
            for m in range(M):
                dot += cols[i][m] * cols[j][m]
            AtA[i][j] = dot / (si * scales[j])
            AtA[j][i] = AtA[i][j]
        bd = mp.mpf(0)
        for m in range(M):
            bd += cols[i][m] * b[m]
        Atb[i] = bd / si

    A_mat = mp.matrix(AtA)
    try:
        evals, Q = mp.eighe(A_mat)
    except Exception:
        try:
            evals, Q = mp.eigsy(A_mat)
        except Exception:
            evals, Q = mp.eig(A_mat)
    eigvals = [evals[i] for i in range(K)]
    eigabs = [abs(e) for e in eigvals]
    eig_max = max(eigabs)
    eig_min = min(eigabs)
    cond = mp.sqrt(eig_max / eig_min) if eig_min > 0 else mp.mpf("1e300")
    Linv = [1 / eigvals[i] if eigabs[i] > 0 else mp.mpf(0) for i in range(K)]
    Qt_b = [mp.mpf(0)] * K
    for i in range(K):
        s = mp.mpf(0)
        for j in range(K):
            s += Q[j, i] * Atb[j]
        Qt_b[i] = s
    z = [Linv[i] * Qt_b[i] for i in range(K)]
    y = [mp.mpf(0)] * K
    for i in range(K):
        s = mp.mpf(0)
        for j in range(K):
            s += Q[i, j] * z[j]
        y[i] = s
    x = [y[i] / scales[i] for i in range(K)]
    rank = sum(1 for v in eigabs if v > 0)
    return x, cond, rank


def build_T(a: Sequence[mp.mpf], zeta_star: mp.mpf) -> List[mp.mpf]:
    T = [None] * (N_MAX + 1)
    z_pow = mp.mpf(1)
    for n in range(1, N_MAX + 1):
        z_pow = z_pow * zeta_star
        T[n] = a[n] * z_pow / mp.gamma(n)
    return T


def stage1_fit(T: Sequence[mp.mpf], n_lo: int, n_hi: int, K_lead: int) -> Dict:
    ns = list(range(n_lo, n_hi + 1))
    cols = []
    for k in range(K_lead + 1):
        col = []
        for n in ns:
            col.append(mp.mpf(1) if k == 0 else mp.mpf(1) / (mp.mpf(n) ** k))
        cols.append(col)
    b = [T[n] for n in ns]
    alpha, cond, rank = column_scaled_solve(cols, b)
    C_fit = alpha[0]
    a_coeff = [alpha[k] / C_fit for k in range(K_lead + 1)] if C_fit != 0 else None
    return {"alpha": alpha, "C": C_fit, "a_k": a_coeff, "cond": cond, "rank": rank,
            "n_lo": n_lo, "n_hi": n_hi, "K_lead": K_lead}


def stage1_predict(stage1: Dict, n: int) -> mp.mpf:
    alpha = stage1["alpha"]
    K = stage1["K_lead"]
    nm = mp.mpf(n)
    s = alpha[0]
    for k in range(1, K + 1):
        s += alpha[k] / (nm ** k)
    return s


def stage2_fit(T: Sequence[mp.mpf], stage1: Dict, n_lo: int, n_hi: int, K_next: int) -> Dict:
    ns = list(range(n_lo, n_hi + 1))
    r_data = [T[n] - stage1_predict(stage1, n) for n in ns]
    cols = []
    two = mp.mpf(2)
    for k in range(K_next + 1):
        col = []
        for n in ns:
            base = mp.mpf(1) / (two ** n)
            if k == 0:
                col.append(base)
            else:
                col.append(base / (mp.mpf(n) ** k))
        cols.append(col)
    beta, cond, rank = column_scaled_solve(cols, r_data)
    D = beta[0]
    b_coeff = [beta[k] / D for k in range(K_next + 1)] if D != 0 else None
    return {"beta": beta, "D": D, "b_k": b_coeff, "cond": cond, "rank": rank,
            "n_lo": n_lo, "n_hi": n_hi, "K_next": K_next}


def run_stability_grid(T: Sequence[mp.mpf]) -> List[Dict]:
    rows = []
    for K_lead in K_LEADS:
        for W1 in W1S:
            s1 = stage1_fit(T, W1[0], W1[1], K_lead)
            s2 = stage2_fit(T, s1, W2[0], W2[1], K_NEXT)
            rec = {
                "K_lead": K_lead, "W1": list(W1), "K_next": K_NEXT, "W2": list(W2),
                "C": s1["C"],
                "a_1": s1["a_k"][1] if s1["a_k"] else None,
                "a_2": s1["a_k"][2] if s1["a_k"] else None,
                "D": s2["D"],
                "cond1": s1["cond"], "cond2": s2["cond"],
                "rank1": s1["rank"], "rank2": s2["rank"],
            }
            rows.append(rec)
    return rows


def median_and_halfrange(values: Sequence[mp.mpf]) -> Tuple[mp.mpf, mp.mpf]:
    sv = sorted(values, key=lambda v: float(v))
    n = len(sv)
    med = sv[n // 2] if n % 2 == 1 else (sv[n // 2 - 1] + sv[n // 2]) / 2
    hr = (sv[-1] - sv[0]) / 2
    return med, hr


# --------------------------------------------------------------------------
# Phase C : relation test + PSLQ
# --------------------------------------------------------------------------

def pslq_basis_atoms(a_1: mp.mpf, Delta_b: int) -> Tuple[List[mp.mpf], List[str]]:
    """12-atom basis matching 017j Phase B (per-rep)."""
    Db = mp.mpf(Delta_b)
    atoms = [
        mp.mpf(1),
        a_1,
        mp.mpf(1) / 2,
        mp.mpf(1) / 3,
        mp.mpf(1) / 4,
        mp.mpf(1) / 6,
        mp.mpf(1) / 9,
        mp.mpf(1) / 12,
        mp.mpf(1) / 18,
        mp.mpf(1) / 36,
        mp.mpf(1) / 72,
        Db / 36,
    ]
    labels = [
        "1", "a_1", "1/2", "1/3", "1/4", "1/6",
        "1/9", "1/12", "1/18", "1/36", "1/72",
        "Delta_b/36",
    ]
    return atoms, labels


def pslq_probe(a_1: mp.mpf, Delta_b: int, tol: mp.mpf) -> Dict:
    atoms, labels = pslq_basis_atoms(a_1, Delta_b)
    try:
        rel = mp.pslq(atoms, tol=tol, maxcoeff=PSLQ_MAXCOEFF)
    except (ValueError, ZeroDivisionError) as exc:
        return {"relation": None, "error": str(exc), "tol": str(tol),
                "atoms": labels}
    if rel is None:
        return {"relation": None, "atoms": labels, "tol": str(tol)}
    # residual: sum coef[i] * atom[i]
    resid = mp.mpf(0)
    for ci, ai in zip(rel, atoms):
        resid += mp.mpf(ci) * ai
    return {
        "relation": [int(x) for x in rel],
        "atoms": labels,
        "tol": str(tol),
        "residual": mp.nstr(resid, 30),
    }


# --------------------------------------------------------------------------
# Phase D : certificate
# --------------------------------------------------------------------------

def write_certificate(payload: Dict):
    rep = payload["selected_rep"]
    lines = [
        "# Subfamily Certificate — T37K-EXTEND-A3-SUBFAMILY",
        "",
        "## Selected third A=3 representative",
        "",
        f"- id: `{rep['id']}`",
        f"- (alpha, beta, gamma, delta, epsilon) = "
        f"({rep['alpha']}, {rep['beta']}, {rep['gamma']}, {rep['delta']}, {rep['epsilon']})",
        f"- Delta_b (target) = {rep['Delta_b']}",
        f"- A_pred = {rep['A_pred']} (side = {rep['side']})",
        f"- |sum of integer params| = "
        f"{abs(rep['alpha'])+abs(rep['beta'])+abs(rep['gamma'])+abs(rep['delta'])+abs(rep['epsilon'])}",
        f"- |Delta_b - (-15.5)| = {abs(rep['Delta_b'] - (-15.5))}",
        f"- provenance: {rep['source']}",
        "",
        "## a_1 measurement (third A=3 rep)",
        "",
        f"- median (60-digit cap): `{payload['a_1_median_60']}`",
        f"- envelope half-range:    `{payload['a_1_envelope']}`",
        f"- grid: 9 configs, K_lead in {{22,25,28}} x W1 in "
        "{{(800,1200),(800,1500),(800,1800)}}",
        "",
        "## Relation test",
        "",
        f"- predicted_a_1 = (4*Delta_b - 9) / 36 = `{payload['predicted_a_1']}`",
        f"- residual      = a_1_median - predicted_a_1 = `{payload['residual']}`",
        f"- tight gate    = 1e-30; loose gate = 1e-3",
        f"- outcome       = **{payload['relation_outcome']}**",
        "",
        "## PSLQ cross-validation",
        "",
        f"- tol=1e-30 relation: `{payload['pslq_tight']['relation']}`",
        f"- tol=1e-12 relation: `{payload['pslq_hard']['relation']}`",
        f"- artefact-only at tol=1e-12? "
        f"`{payload['pslq_tight']['relation'] != payload['pslq_hard']['relation']}`",
        "",
        "## Picture v1.11 amendment recommendation",
        "",
        payload["picture_recommendation"],
    ]
    (HERE / "subfamily_certificate.md").write_text("\n".join(lines) + "\n")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main():
    HERE.mkdir(parents=True, exist_ok=True)
    print(f"== T37K-EXTEND-A3-SUBFAMILY ==")
    print(f"DPS={DPS} (work {WORK_DPS}), N_MAX={N_MAX}")

    # Validate inputs
    for p in (T37J_DIR / "handoff.md", T37E_DIR / "handoff.md",
              T35_DIR / "representatives.json"):
        if not p.exists():
            halt("T37K_INPUT_INVALID", missing=str(p))

    # ------------- Phase A -------------
    print("\n[Phase A] selecting third A=3 rep...")
    sel = select_third_a3_rep()
    chosen = sel["chosen"]
    print(f"  -> selected: alpha={chosen['alpha']} beta={chosen['beta']} "
          f"gamma={chosen['gamma']} delta={chosen['delta']} eps={chosen['epsilon']}")
    print(f"     Delta_b={chosen['Delta_b']}, A=3, |sum|={chosen['sum_abs']}")
    write_json("third_A3_rep_selection.json", sel)
    claim(
        f"Phase A: selected third A=3 PCF rep "
        f"(alpha={chosen['alpha']}, beta={chosen['beta']}, gamma={chosen['gamma']}, "
        f"delta={chosen['delta']}, epsilon={chosen['epsilon']}); Delta_b={chosen['Delta_b']}",
        "computation", DPS, "t37k_runner.py", sel,
    )

    cv = crossvalidate_rep(chosen)
    write_json("rep_crossvalidation.json", cv)
    if not cv["ok_A"]:
        halt("T37K_INVALID_REP", reason="A_computed != A_target", crosscheck=cv)
    if not cv["ok_Delta_b"]:
        halt("T37K_INVALID_REP", reason="Delta_b mismatch", crosscheck=cv)
    if not cv["ok_recurrence_diag_nonzero"]:
        halt("T37K_INVALID_REP", reason="diag(1) == 0", crosscheck=cv)
    claim(
        f"Phase A.5: A_computed = {cv['A_computed']} (matches target A=3)",
        "verification", DPS, "t37k_runner.py", cv,
    )
    claim(
        f"Phase A.5: Delta_b_computed = {cv['Delta_b_computed']} matches "
        f"Delta_b_target = {cv['Delta_b_target']}",
        "verification", DPS, "t37k_runner.py", cv,
    )

    # ------------- Phase B.1 -------------
    print("\n[Phase B.1] deriving a_n recurrence (dps={}, N={})...".format(DPS, N_MAX))
    t0 = time.time()
    a, c, zeta_star = derive_a_series(chosen)
    print(f"  -> a[1] = {mp.nstr(a[1], 20)}")
    print(f"  -> a[{N_MAX}] ~ 10^{int(mp.log10(abs(a[N_MAX]))) if a[N_MAX] != 0 else 0}")
    print(f"  -> elapsed {time.time()-t0:.1f}s; c={mp.nstr(c, 20)}, "
          f"zeta_star={mp.nstr(zeta_star, 20)}")
    csv_path = HERE / "recurrence_third_A3_rep.csv"
    csv_hash = write_recurrence_csv(a, csv_path)
    claim(
        f"Phase B.1: Birkhoff recurrence at dps={WORK_DPS}, N={N_MAX} for third A=3 rep; "
        f"a_1_raw = {mp.nstr(a[1], 30)}",
        "computation", DPS, "t37k_runner.py",
        {"a_1": str(a[1]), "a_N": str(a[N_MAX]), "csv_hash": csv_hash},
    )

    # ------------- Phase B.2 / B.3 -------------
    print("\n[Phase B.2/B.3] T_n cache + 9-config two-stage fit...")
    T = build_T(a, zeta_star)
    grid = run_stability_grid(T)
    a1_vals = [r["a_1"] for r in grid if r["a_1"] is not None]
    if len(a1_vals) < 9:
        halt("T37K_FIT_DIVERGED", reason="some configs returned None for a_1",
             valid=len(a1_vals))
    a1_med, a1_hr = median_and_halfrange(a1_vals)
    a2_med, a2_hr = median_and_halfrange([r["a_2"] for r in grid if r["a_2"] is not None])
    C_med, C_hr   = median_and_halfrange([r["C"]   for r in grid])
    fit_payload = {
        "rep": chosen["id"],
        "Delta_b": chosen["Delta_b"],
        "K_LEADS": K_LEADS,
        "W1S": [list(w) for w in W1S],
        "K_NEXT": K_NEXT,
        "W2": list(W2),
        "valid_count": len(a1_vals),
        "a_1_median_full":   mp.nstr(a1_med, 200),
        "a_1_median_60":     mp.nstr(a1_med, 60),
        "a_1_envelope_half_range": mp.nstr(a1_hr, 30),
        "a_2_median_60":     mp.nstr(a2_med, 60),
        "a_2_envelope_half_range": mp.nstr(a2_hr, 30),
        "C_median_60":       mp.nstr(C_med, 60),
        "C_envelope_half_range": mp.nstr(C_hr, 30),
        "configs": [
            {
                "K_lead": r["K_lead"], "W1": r["W1"],
                "C": mp.nstr(r["C"], 60),
                "a_1": mp.nstr(r["a_1"], 60),
                "cond1": mp.nstr(r["cond1"], 6),
                "cond2": mp.nstr(r["cond2"], 6),
            } for r in grid
        ],
    }
    write_json("a_1_third_A3_rep_fit.json", fit_payload)
    print(f"  -> a_1 median = {mp.nstr(a1_med, 30)}")
    print(f"     half_range = {mp.nstr(a1_hr, 6)}")
    claim(
        f"Phase B.2/B.3: a_1_median (third A=3 rep) = {mp.nstr(a1_med, 60)}",
        "computation", DPS, "t37k_runner.py",
        {"a_1_median": mp.nstr(a1_med, 200), "envelope": mp.nstr(a1_hr, 30)},
    )
    claim(
        f"Phase B.3: a_1 envelope half-range = {mp.nstr(a1_hr, 6)} across 9-config grid",
        "computation", DPS, "t37k_runner.py", {"hr": mp.nstr(a1_hr, 30)},
    )

    if a1_hr > ENVELOPE_GATE:
        halt("T37K_FIT_DIVERGED",
             reason="envelope half_range > 1e-25",
             half_range=mp.nstr(a1_hr, 30),
             a_1_median=mp.nstr(a1_med, 60))

    # ------------- Phase C -------------
    print("\n[Phase C] relation test...")
    Db = chosen["Delta_b"]
    predicted = (mp.mpf(4) * mp.mpf(Db) - mp.mpf(9)) / mp.mpf(36)
    residual = a1_med - predicted
    abs_res = abs(residual)
    print(f"  predicted_a_1 = (4*{Db}-9)/36 = {mp.nstr(predicted, 30)}")
    print(f"  measured a_1  = {mp.nstr(a1_med, 30)}")
    print(f"  residual      = {mp.nstr(residual, 30)}")

    if abs_res < RELATION_TIGHT and a1_hr < ENVELOPE_GATE:
        outcome = "T37K_RELATION_GENERALIZES"
    elif abs_res > RELATION_LOOSE and a1_hr < ENVELOPE_GATE:
        outcome = "T37K_RELATION_FALSIFIED_PROVISIONAL"  # may upgrade to ALTERNATE in C.5
    else:
        outcome = "T37K_INDETERMINATE"

    relation_payload = {
        "Delta_b_third": Db,
        "predicted_a_1": mp.nstr(predicted, 200),
        "measured_a_1":  mp.nstr(a1_med, 200),
        "residual":      mp.nstr(residual, 200),
        "abs_residual":  mp.nstr(abs_res, 200),
        "envelope":      mp.nstr(a1_hr, 30),
        "tight_gate":    "1e-30",
        "loose_gate":    "1e-3",
        "outcome":       outcome,
    }

    claim(
        f"Phase C.1: predicted_a_1 = (4*Delta_b - 9)/36 = {mp.nstr(predicted, 60)} "
        f"at Delta_b = {Db}",
        "computation", DPS, "t37k_runner.py", relation_payload,
    )
    claim(
        f"Phase C.2: residual = a_1_median - predicted_a_1 = {mp.nstr(residual, 60)}",
        "computation", DPS, "t37k_runner.py", relation_payload,
    )
    claim(
        f"Phase C.3: relation outcome classification = {outcome}",
        "verification", DPS, "t37k_runner.py", relation_payload,
    )

    # Phase C.4 / C.5: PSLQ probe on 12-atom basis (full) + 2-atom (per-rep)
    print("\n[Phase C.4/C.5] PSLQ on 12-atom basis...")
    pslq_tight = pslq_probe(a1_med, Db, PSLQ_TOL_TIGHT)
    pslq_hard  = pslq_probe(a1_med, Db, PSLQ_TOL_HARD)
    # Mark artefact relations: coef on a_1 (atom index 1) == 0
    for p in (pslq_tight, pslq_hard):
        rel = p.get("relation")
        p["a_1_coef_zero"] = (rel is not None and rel[1] == 0)
        p["is_basis_trivial"] = p["a_1_coef_zero"]   # alias
    # Per-rep [1, a_1] PSLQ (017j-style) — confirm whether a_1 itself is rational
    perrep_atoms = [mp.mpf(1), a1_med]
    try:
        rel_perrep_t = mp.pslq(perrep_atoms, tol=PSLQ_TOL_TIGHT, maxcoeff=PSLQ_MAXCOEFF)
    except Exception as exc:
        rel_perrep_t = None
    try:
        rel_perrep_h = mp.pslq(perrep_atoms, tol=PSLQ_TOL_HARD, maxcoeff=PSLQ_MAXCOEFF)
    except Exception as exc:
        rel_perrep_h = None
    perrep = {
        "atoms": ["1", "a_1"],
        "tol30_relation": [int(x) for x in rel_perrep_t] if rel_perrep_t else None,
        "tol12_relation": [int(x) for x in rel_perrep_h] if rel_perrep_h else None,
    }
    if rel_perrep_t is not None and rel_perrep_t[1] != 0:
        p_, q_ = -int(rel_perrep_t[0]), int(rel_perrep_t[1])
        perrep["a_1_rational"] = f"{p_}/{q_}"
        perrep["a_1_rational_value"] = mp.nstr(mp.mpf(p_) / mp.mpf(q_), 30)
        perrep["matches_apparent_-17/4"] = (Fraction(p_, q_) == Fraction(-17, 4))
    relation_payload["pslq_tight"] = pslq_tight
    relation_payload["pslq_hard"]  = pslq_hard
    relation_payload["pslq_perrep"] = perrep
    write_json("subfamily_relation_test.json", relation_payload)

    print(f"  PSLQ tol=1e-30 (12-atom): {pslq_tight.get('relation')}  "
          f"a_1_coef_zero={pslq_tight['a_1_coef_zero']}")
    print(f"  PSLQ tol=1e-12 (12-atom): {pslq_hard.get('relation')}  "
          f"a_1_coef_zero={pslq_hard['a_1_coef_zero']}")
    print(f"  PSLQ tol=1e-30 (2-atom [1,a_1]): {perrep['tol30_relation']}  "
          f"a_1 = {perrep.get('a_1_rational', 'N/A')}")

    claim(
        f"Phase C.4: PSLQ at tol=1e-30 maxcoeff=1e15 -> "
        f"relation={pslq_tight.get('relation')}",
        "computation", DPS, "t37k_runner.py", pslq_tight,
    )
    claim(
        f"Phase C.4: PSLQ HARD HYGIENE at tol=1e-12 -> "
        f"relation={pslq_hard.get('relation')} (artefact filter); "
        f"a_1_coef_zero={pslq_hard['a_1_coef_zero']}",
        "verification", DPS, "t37k_runner.py", pslq_hard,
    )
    claim(
        f"Phase C.4 per-rep [1,a_1] PSLQ tol=1e-30 -> {perrep.get('tol30_relation')}; "
        f"a_1 rational = {perrep.get('a_1_rational', 'N/A')}",
        "computation", DPS, "t37k_runner.py", perrep,
    )

    # Cross-rep consistency check: is [4, -36, 9] the relation across V_quad/QL15 + third?
    # V_quad: a_1=-53/36, Delta_b=-11. Test: 4*(-11) - 36*(-53/36) - 9 = -44+53-9 = 0. OK.
    # QL15:   a_1=-89/36, Delta_b=-20. Test: 4*(-20) - 36*(-89/36) - 9 = -80+89-9 = 0. OK.
    # Third:  4*Db - 36*a_1_med - 9 = ?
    cross_check_third = 4 * mp.mpf(Db) - 36 * a1_med - 9
    cross_payload = {
        "V_quad_residual_relation": "0 (algebraic): 4*(-11) - 36*(-53/36) - 9 = 0",
        "QL15_residual_relation":   "0 (algebraic): 4*(-20) - 36*(-89/36) - 9 = 0",
        "third_residual_relation":  mp.nstr(cross_check_third, 60),
        "all_three_match_to_30":    abs(cross_check_third) < RELATION_TIGHT,
    }
    write_json("cross_rep_consistency.json", cross_payload)
    claim(
        f"Phase C.4 cross-rep: 4*Delta_b - 36*a_1 - 9 evaluated at third A=3 rep = "
        f"{mp.nstr(cross_check_third, 30)} (V_quad+QL15 are 0 algebraically)",
        "verification", DPS, "t37k_runner.py", cross_payload,
    )

    # Refine outcome if RELATION_FALSIFIED_PROVISIONAL: a true ALTERNATE
    # relation must (i) involve a_1 with nonzero coefficient, (ii) appear
    # at tol=1e-30 AND tol=1e-12 (HARD HYGIENE), (iii) not be the original
    # ansatz. A basis-trivial identity (coefficient on a_1 is 0) does not
    # qualify as a relation involving a_1.
    if outcome == "T37K_RELATION_FALSIFIED_PROVISIONAL":
        rel_t = pslq_tight.get("relation")
        rel_h = pslq_hard.get("relation")
        is_trivial = pslq_tight["is_basis_trivial"] or pslq_hard["is_basis_trivial"]
        hygiene_match = (rel_t == rel_h) and (rel_t is not None)
        if rel_t is None or is_trivial or not hygiene_match:
            outcome = "T37K_RELATION_FALSIFIED"
        else:
            outcome = "T37K_ALTERNATE_RELATION"
        relation_payload["outcome"] = outcome
        write_json("subfamily_relation_test.json", relation_payload)

    claim(
        f"Phase C: final relation outcome label = {outcome}",
        "verification", DPS, "t37k_runner.py", {"outcome": outcome},
    )

    # ------------- Phase D : certificate + verdict -------------
    print(f"\n[Phase D] outcome = {outcome}")

    # Picture v1.11 recommendation
    if outcome == "T37K_RELATION_GENERALIZES":
        rec = ("Picture v1.11: amend G20 to record (2A)^2 * a_1 = 4*Delta_b - 9 "
               "as a candidate A=3 sub-family closed form, holding across 3 reps "
               "(V_quad, QL15, third). AEAL elevation requires a fourth A=3 rep "
               "+ Claude review.")
    elif outcome == "T37K_RELATION_FALSIFIED":
        rec = ("Picture v1.11: G20 catalogue stands as discrete; the "
               "V_quad/QL15 match was a 2-point coincidence. No A=3 sub-family "
               "closed form via the (2A)^2*a_1 = 4*Delta_b - 9 ansatz.")
    elif outcome == "T37K_ALTERNATE_RELATION":
        rec = ("Picture v1.11: original (2A)^2*a_1 = 4*Delta_b - 9 ansatz "
               "falsifies, but PSLQ surfaces an alternate closed form on the "
               "12-atom basis (see subfamily_relation_test.json). Further A=3 "
               "reps required to falsify or confirm.")
    elif outcome == "T37K_INDETERMINATE":
        rec = ("Picture v1.11: precision insufficient at dps=300; recommend "
               "extending the third rep to dps=400 (017e style) before "
               "amending picture.")
    else:
        rec = "Outcome label unrecognized; see verdict.md."

    cert_payload = {
        "selected_rep": chosen,
        "a_1_median_60":   fit_payload["a_1_median_60"],
        "a_1_envelope":    fit_payload["a_1_envelope_half_range"],
        "predicted_a_1":   mp.nstr(predicted, 60),
        "residual":        mp.nstr(residual, 60),
        "relation_outcome": outcome,
        "pslq_tight":      pslq_tight,
        "pslq_hard":       pslq_hard,
        "picture_recommendation": rec,
    }
    write_certificate(cert_payload)

    verdict_payload = {
        "task": "T37K-EXTEND-A3-SUBFAMILY",
        "outcome": outcome,
        "third_A3_rep": chosen,
        "a_1_median_60":   fit_payload["a_1_median_60"],
        "a_1_envelope":    fit_payload["a_1_envelope_half_range"],
        "predicted_a_1":   mp.nstr(predicted, 60),
        "residual":        mp.nstr(residual, 60),
        "abs_residual":    mp.nstr(abs_res, 60),
        "pslq_tight_relation": pslq_tight.get("relation"),
        "pslq_hard_relation":  pslq_hard.get("relation"),
        "picture_recommendation": rec,
    }
    write_json("verdict.json", verdict_payload)

    # verdict.md
    vlines = [
        f"# Verdict — T37K-EXTEND-A3-SUBFAMILY",
        "",
        f"**Outcome:** `{outcome}`",
        "",
        f"- Third A=3 rep: (alpha={chosen['alpha']}, beta={chosen['beta']}, "
        f"gamma={chosen['gamma']}, delta={chosen['delta']}, epsilon={chosen['epsilon']}); "
        f"Delta_b = {chosen['Delta_b']}",
        f"- Measured a_1 (median, 60 dig): `{fit_payload['a_1_median_60']}`",
        f"- Envelope half-range:           `{fit_payload['a_1_envelope_half_range']}`",
        f"- Predicted a_1 (relation):      `{mp.nstr(predicted, 60)}`",
        f"- Residual:                      `{mp.nstr(residual, 60)}`",
        f"- |residual|:                    `{mp.nstr(abs_res, 30)}`",
        "",
        f"## Picture recommendation",
        "",
        rec,
    ]
    (HERE / "verdict.md").write_text("\n".join(vlines) + "\n")

    claim(
        f"Verdict label = {outcome}",
        "verification", DPS, "t37k_runner.py", verdict_payload,
    )

    # Empty placeholder logs (per standing procedure)
    if not (HERE / "halt_log.json").exists():
        write_json("halt_log.json", {})
    write_json("discrepancy_log.json", {})
    if outcome == "T37K_RELATION_FALSIFIED":
        write_json("unexpected_finds.json", {
            "summary": "(2A)^2*a_1 = 4*Delta_b - 9 was a 2-point coincidence",
            "third_rep": chosen,
            "residual": mp.nstr(residual, 60),
        })
    elif outcome == "T37K_RELATION_GENERALIZES":
        write_json("unexpected_finds.json", {
            "summary": "A=3 sub-family relation holds across 3 reps to >=30 digits",
            "third_rep": chosen,
            "residual": mp.nstr(residual, 60),
        })
    else:
        write_json("unexpected_finds.json", {})

    write_claims()
    print(f"\nDONE. Outcome = {outcome}. {len(CLAIMS)} AEAL claims written.")


if __name__ == "__main__":
    main()
