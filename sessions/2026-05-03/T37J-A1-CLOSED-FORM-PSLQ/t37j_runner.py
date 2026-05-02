"""T37J-A1-CLOSED-FORM-PSLQ runner.

Phases:
  A  Input validation + precision check + CF rational reconstruction
  B  Per-rep PSLQ at tol=1e-30 and tol=1e-12 (HARD HYGIENE)
  C  Joint PSLQ + functional-form scan + polynomial-in-(Delta_b,A) fit
  D  QL09 boundary consistency vs candidate f
  E  Emit JSON / certificate / claims.jsonl

Refit-only: consumes 017c phase_c_partition.json (a_1 medians + envelopes
at >= 40 digits) and T35 representatives.json. No new mpmath series.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import mpmath as mp

# ---------- paths ----------
HERE = Path(__file__).resolve().parent
BRIDGE = HERE.parent.parent.parent  # siarc-relay-bridge/
SRC_017C = BRIDGE / "sessions" / "2026-05-02" / "T37-S2-EXTRACTION-POLYNOMIAL-AWARE"
SRC_T35 = BRIDGE / "sessions" / "2026-05-02" / "T35-STOKES-MULTIPLIER-DISCRIMINATION"

# ---------- precision ----------
mp.mp.dps = 300

# ---------- IO helpers ----------
CLAIMS_PATH = HERE / "claims.jsonl"
HALT_PATH = HERE / "halt_log.json"
DISC_PATH = HERE / "discrepancy_log.json"
UNEX_PATH = HERE / "unexpected_finds.json"

CLAIMS: list[dict] = []
DISC: list[dict] = []
UNEX: list[dict] = []


def sha(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def add_claim(claim: str, *, dps: int, script: str, output_hash: str,
              evidence_type: str = "computation") -> None:
    CLAIMS.append({
        "claim": claim,
        "evidence_type": evidence_type,
        "dps": dps,
        "reproducible": True,
        "script": script,
        "output_hash": output_hash,
    })


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def halt(label: str, detail: dict) -> None:
    write_json(HALT_PATH, {"halt": label, "detail": detail})
    write_jsonl(CLAIMS_PATH, CLAIMS + [{
        "claim": f"verdict_label={label}",
        "evidence_type": "label",
        "dps": int(mp.mp.dps),
        "reproducible": True,
        "script": "t37j_runner.py",
        "output_hash": sha(label),
    }])
    write_json(DISC_PATH, DISC)
    write_json(UNEX_PATH, UNEX)
    print(f"HALT: {label}")
    sys.exit(0)


# ---------- Phase A ----------
def load_inputs() -> tuple[dict, dict]:
    pj = SRC_017C / "phase_c_partition.json"
    rj = SRC_T35 / "representatives.json"
    if not pj.exists() or not rj.exists():
        halt("T37J_INPUT_INVALID", {"missing": [str(p) for p in (pj, rj) if not p.exists()]})

    a1_block = json.loads(pj.read_text(encoding="utf-8"))["a_1"]
    reps_block = json.loads(rj.read_text(encoding="utf-8"))["representatives"]

    # Build per-rep a_1 measurements (median + envelope) at high precision.
    rep_data: dict[str, dict] = {}
    for side, key in [("neg", "neg_data"), ("pos", "pos_data")]:
        for rid, med, env in a1_block[key]:
            rep_data[rid] = {
                "side": side,
                "a_1_median_str": med,
                "a_1_envelope_str": env,
            }
    # Merge representative metadata
    for r in reps_block:
        rid = r["id"]
        if rid not in rep_data:
            continue
        rep_data[rid].update({
            "Delta_b": int(r["Delta_b"]),
            "A": int(r["A_pred"]),
            "alpha": int(r["alpha"]),
            "beta": int(r["beta"]),
        })
    return rep_data, {"src_017c": str(pj), "src_t35": str(rj)}


def precision_check(rep_data: dict) -> None:
    bad = []
    for rid, d in rep_data.items():
        if rid == "QL09":
            continue
        med = mp.mpf(d["a_1_median_str"])
        env = mp.mpf(d["a_1_envelope_str"])
        ratio = env / abs(med)
        d["precision_ratio_str"] = mp.nstr(ratio, 6)
        if ratio > mp.mpf("1e-30"):
            bad.append((rid, mp.nstr(ratio, 6)))
    if bad:
        halt("T37J_PRECISION_INSUFFICIENT", {"bad_reps": bad})


def cf_rational(x: mp.mpf, q_max: int = 1000) -> tuple[int, int, mp.mpf]:
    """Continued-fraction reconstruction; returns (p, q, |x - p/q|)."""
    # Compute CF expansion (a_0, a_1, ...) until denominator exceeds q_max.
    a_terms: list[int] = []
    y = x
    for _ in range(80):
        a_n = mp.floor(y)
        a_terms.append(int(a_n))
        frac = y - a_n
        if frac == 0 or abs(frac) < mp.mpf("1e-280"):
            break
        y = 1 / frac
    # Convergents: h_n / k_n with h_{-1}=1, h_{-2}=0, k_{-1}=0, k_{-2}=1.
    h_prev2, h_prev1 = 0, 1
    k_prev2, k_prev1 = 1, 0
    best = (int(mp.nint(x)), 1, abs(x - mp.nint(x)))
    for ai in a_terms:
        h_n = ai * h_prev1 + h_prev2
        k_n = ai * k_prev1 + k_prev2
        if k_n > q_max:
            break
        h_prev2, h_prev1 = h_prev1, h_n
        k_prev2, k_prev1 = k_prev1, k_n
        err = abs(x - mp.mpf(h_n) / k_n)
        best = (int(h_n), int(k_n), err)
    return best


# ---------- PSLQ helpers ----------
def run_pslq(values: list[mp.mpf], tol: mp.mpf, maxcoeff: int):
    try:
        return mp.pslq(values, tol=tol, maxcoeff=maxcoeff)
    except Exception:
        return None


def explain_relation(atoms_names: list[str], rel) -> str:
    if rel is None:
        return "no_relation"
    parts = []
    for name, c in zip(atoms_names, rel):
        if c == 0:
            continue
        parts.append(f"{c:+d}*{name}")
    return " ".join(parts) if parts else "trivial"


# ---------- Phase B ----------
def per_rep_pslq(rep_data: dict) -> dict:
    """Run PSLQ per non-QL09 rep on a 12-atom basis at tol=1e-30 and tol=1e-12."""
    out: dict[str, dict] = {}
    rationals = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 6),
                 Fraction(1, 9), Fraction(1, 12), Fraction(1, 18), Fraction(1, 36),
                 Fraction(1, 72)]
    for rid, d in rep_data.items():
        if rid == "QL09":
            continue
        a1 = mp.mpf(d["a_1_median_str"])
        Db = d["Delta_b"]
        A = d["A"]
        # Atoms: [a_1, 1, 1/2, 1/3, 1/4, 1/6, 1/9, 1/12, 1/18, 1/36, 1/72,
        #         Delta_b, Delta_b/(2A)^2, (Delta_b - 1)/(2A)^2,
        #         (Delta_b + 1)/(2A)^2]
        atom_specs: list[tuple[str, mp.mpf]] = []
        atom_specs.append(("a_1", a1))
        atom_specs.append(("1", mp.mpf(1)))
        for r in rationals:
            atom_specs.append((f"1/{r.denominator}", mp.mpf(r.numerator) / r.denominator))
        atom_specs.append(("Delta_b", mp.mpf(Db)))
        atom_specs.append(("Delta_b/(2A)^2", mp.mpf(Db) / (2 * A) ** 2))
        atom_specs.append((f"(Delta_b-1)/(2A)^2", mp.mpf(Db - 1) / (2 * A) ** 2))
        atom_specs.append((f"(Delta_b+1)/(2A)^2", mp.mpf(Db + 1) / (2 * A) ** 2))
        # cap to keep PSLQ tractable
        atom_specs = atom_specs[:16]
        names = [s[0] for s in atom_specs]
        vals = [s[1] for s in atom_specs]

        rel_tight = run_pslq(vals, mp.mpf("1e-30"), 10 ** 15)
        rel_loose = run_pslq(vals, mp.mpf("1e-12"), 10 ** 8)

        # CF reconstruction of a_1
        p, q, cf_err = cf_rational(a1, q_max=1000)

        # Verify rational p/q matches at tol=1e-30
        rational_match = (cf_err < mp.mpf("1e-30"))

        # Hygiene flag: relation found at tol=1e-12 but not at tol=1e-30
        hygiene_flag = (rel_loose is not None and rel_tight is None)

        out[rid] = {
            "a_1_median_str": d["a_1_median_str"][:80] + "...",
            "Delta_b": Db,
            "A": A,
            "atom_names": names,
            "rel_tol_1e-30": list(rel_tight) if rel_tight is not None else None,
            "rel_tol_1e-30_explained": explain_relation(names, rel_tight),
            "rel_tol_1e-12": list(rel_loose) if rel_loose is not None else None,
            "rel_tol_1e-12_explained": explain_relation(names, rel_loose),
            "cf_p": p,
            "cf_q": q,
            "cf_err_str": mp.nstr(cf_err, 6),
            "rational_match_at_1e-30": bool(rational_match),
            "hygiene_flag_loose_only": bool(hygiene_flag),
        }
    return out


# ---------- Phase C ----------
def joint_pslq(rep_data: dict) -> dict:
    """PSLQ across the 3 non-anomalous reps.

    Search whether any integer combination
       c1*a1_V + c2*a1_QL15 + c3*a1_QL05 + c4*1 + c5*Delta_b_V + ...
    vanishes at tol=1e-30 maxcoeff=1e10.
    """
    rids = ["V_quad", "QL15", "QL05"]
    a1s = [mp.mpf(rep_data[r]["a_1_median_str"]) for r in rids]
    Dbs = [rep_data[r]["Delta_b"] for r in rids]
    As = [rep_data[r]["A"] for r in rids]

    # Multiple basis configurations
    configs = [
        # config1: a_1's + 1
        (["a1_V", "a1_QL15", "a1_QL05", "1"],
         a1s + [mp.mpf(1)]),
        # config2: a_1's + Delta_b's
        (["a1_V", "a1_QL15", "a1_QL05", "Db_V", "Db_QL15", "Db_QL05", "1"],
         a1s + [mp.mpf(d) for d in Dbs] + [mp.mpf(1)]),
        # config3: a_1's + Delta_b/(2A)^2's + 1
        (["a1_V", "a1_QL15", "a1_QL05",
          "Db_V/(2A)^2", "Db_QL15/(2A)^2", "Db_QL05/(2A)^2", "1"],
         a1s + [mp.mpf(d) / (2 * a) ** 2 for d, a in zip(Dbs, As)] + [mp.mpf(1)]),
        # config4: a_1's + Delta_b/A^2's + 1
        (["a1_V", "a1_QL15", "a1_QL05",
          "Db_V/A^2", "Db_QL15/A^2", "Db_QL05/A^2", "1"],
         a1s + [mp.mpf(d) / a ** 2 for d, a in zip(Dbs, As)] + [mp.mpf(1)]),
    ]
    out = []
    for names, vals in configs:
        rel_tight = run_pslq(vals, mp.mpf("1e-30"), 10 ** 10)
        rel_loose = run_pslq(vals, mp.mpf("1e-12"), 10 ** 6)
        out.append({
            "atom_names": names,
            "rel_tol_1e-30": list(rel_tight) if rel_tight is not None else None,
            "rel_tol_1e-30_explained": explain_relation(names, rel_tight),
            "rel_tol_1e-12": list(rel_loose) if rel_loose is not None else None,
            "rel_tol_1e-12_explained": explain_relation(names, rel_loose),
            "hygiene_flag_loose_only": bool(rel_loose is not None and rel_tight is None),
        })
    return {"configs": out}


def functional_form_scan(rep_data: dict) -> list[dict]:
    """Test candidate f(Delta_b, A) forms against 3 non-anomalous reps."""
    rids = ["V_quad", "QL15", "QL05"]
    measurements = []
    for r in rids:
        d = rep_data[r]
        measurements.append({
            "rep": r,
            "a_1": mp.mpf(d["a_1_median_str"]),
            "Delta_b": d["Delta_b"],
            "A": d["A"],
        })

    def make(form_name, fn):
        return form_name, fn

    candidates = [
        make("Delta_b/(2A)^2",
             lambda Db, A: mp.mpf(Db) / (2 * A) ** 2),
        make("(Delta_b - 1)/(2A)^2",
             lambda Db, A: mp.mpf(Db - 1) / (2 * A) ** 2),
        make("Delta_b/A^2",
             lambda Db, A: mp.mpf(Db) / A ** 2),
        make("Delta_b/(A*(A-1))",
             lambda Db, A: mp.mpf(Db) / (A * (A - 1))),
        make("Delta_b/(4*A)",
             lambda Db, A: mp.mpf(Db) / (4 * A)),
        make("Delta_b*A/(2A)^2 = Db/(4A)",
             lambda Db, A: mp.mpf(Db * A) / (2 * A) ** 2),
        make("Delta_b/(A^2 - 1)",
             lambda Db, A: mp.mpf(Db) / (A ** 2 - 1)),
        make("(Delta_b - 9/4)/A^2  [V_quad+QL15 fit]",
             lambda Db, A: (mp.mpf(Db) - mp.mpf(9) / 4) / A ** 2),
        # Scan affine: a_1 = (c0 + c1*Delta_b)/(2A)^2 with c0,c1 small ints
    ]
    results = []
    for name, fn in candidates:
        residuals = []
        max_res = mp.mpf(0)
        for m in measurements:
            pred = fn(m["Delta_b"], m["A"])
            res = abs(m["a_1"] - pred)
            residuals.append({
                "rep": m["rep"],
                "predicted": mp.nstr(pred, 30),
                "residual": mp.nstr(res, 6),
            })
            if res > max_res:
                max_res = res
        results.append({
            "form": name,
            "residuals": residuals,
            "max_residual": mp.nstr(max_res, 6),
            "max_residual_below_1e-30": bool(max_res < mp.mpf("1e-30")),
        })

    # Affine-in-(Delta_b, A) brute-force scan over small integer coefficients
    # Fit a_1 * (2A)^2 = c0 + c1*Delta_b + c2*A + c3*Delta_b*A + c4*A^2 ...
    # Solve LSQ on integer-rational candidates with denom <= 12.
    # Direct: a_1*(2A)^2 measurements:
    # V_quad: 36 * (-53/36) = -53
    # QL15:   36 * (-89/36) = -89
    # QL05:   64 * (31/4)   = 496
    # Hypothesis form: a_1*(2A)^2 = c1*Delta_b + c2*A + c3
    # 3 equations, 3 unknowns -> unique solution (if non-singular).
    # Solve linear system:
    # -53 = -11 c1 + 3 c2 + c3
    # -89 = -20 c1 + 3 c2 + c3
    # +496 =   8 c1 + 4 c2 + c3
    M = mp.matrix([[-11, 3, 1],
                   [-20, 3, 1],
                   [8, 4, 1]])
    b = mp.matrix([-53, -89, 496])
    try:
        c = mp.lu_solve(M, b)
        c1, c2, c3 = c[0], c[1], c[2]
        affine_form = {
            "form": "a_1 * (2A)^2 = c1*Delta_b + c2*A + c3",
            "c1": mp.nstr(c1, 30),
            "c2": mp.nstr(c2, 30),
            "c3": mp.nstr(c3, 30),
            "c1_rational_guess": str(Fraction(float(c1)).limit_denominator(1000)),
            "c2_rational_guess": str(Fraction(float(c2)).limit_denominator(1000)),
            "c3_rational_guess": str(Fraction(float(c3)).limit_denominator(1000)),
        }
    except Exception as e:
        affine_form = {"error": str(e)}
    results.append({"form_affine_3eq3unk": affine_form})

    return results


def polynomial_fit(rep_data: dict) -> dict:
    """Fit a_1 as low-order polynomial in (Delta_b, A) with rational coefficients.

    With only 3 data points, we have at most 3 free coefficients we can pin.
    Try a few 3-coefficient polynomial families and report residuals.
    """
    rids = ["V_quad", "QL15", "QL05"]
    rows = [(rep_data[r]["Delta_b"], rep_data[r]["A"], mp.mpf(rep_data[r]["a_1_median_str"]))
            for r in rids]

    families = [
        ("a_1 = c0 + c1*Delta_b + c2/A^2",
         lambda Db, A: [mp.mpf(1), mp.mpf(Db), mp.mpf(1) / A ** 2]),
        ("a_1 = c0 + c1*Delta_b + c2*A",
         lambda Db, A: [mp.mpf(1), mp.mpf(Db), mp.mpf(A)]),
        ("a_1 = c0/A + c1*Delta_b/A + c2*Delta_b/A^2",
         lambda Db, A: [mp.mpf(1) / A, mp.mpf(Db) / A, mp.mpf(Db) / A ** 2]),
        ("a_1 = c0 + c1*Delta_b/(2A)^2 + c2/A",
         lambda Db, A: [mp.mpf(1), mp.mpf(Db) / (2 * A) ** 2, mp.mpf(1) / A]),
    ]
    results = []
    for name, basis_fn in families:
        rows_basis = [basis_fn(Db, A) for Db, A, _ in rows]
        target = [a1 for _, _, a1 in rows]
        M = mp.matrix(rows_basis)
        b = mp.matrix(target)
        try:
            c = mp.lu_solve(M, b)
            preds = [sum(M[i, j] * c[j] for j in range(M.cols)) for i in range(M.rows)]
            res = [abs(preds[i] - target[i]) for i in range(M.rows)]
            max_res = max(res)
            results.append({
                "family": name,
                "coefficients": [mp.nstr(c[i], 30) for i in range(M.rows)],
                "coeff_rational_guess": [str(Fraction(float(c[i])).limit_denominator(10000))
                                         for i in range(M.rows)],
                "max_residual": mp.nstr(max_res, 6),
                "fits_to_machine_zero": bool(max_res < mp.mpf("1e-50")),
            })
        except Exception as e:
            results.append({"family": name, "error": str(e)})
    return {"families": results}


# ---------- Phase D ----------
def ql09_boundary(rep_data: dict, scan_results: list[dict],
                  poly_results: dict) -> dict:
    """Evaluate every candidate f at QL09 = (Delta_b=1, A=4); compare to a_1≈0."""
    a1_QL09 = mp.mpf(rep_data["QL09"]["a_1_median_str"])
    out = []
    # Functional forms (skip the affine entry which is a dict not residual)
    for entry in scan_results:
        if "form" not in entry:
            continue
        # We re-evaluate by name — too brittle; instead recompute via lambdas
        # we already evaluated in functional_form_scan. For QL09 boundary we
        # rely on a parallel small set defined here:
        pass

    qd = mp.mpf(1)
    qa = 4
    candidates = [
        ("Delta_b/(2A)^2", mp.mpf(qd) / (2 * qa) ** 2),
        ("(Delta_b - 1)/(2A)^2", mp.mpf(qd - 1) / (2 * qa) ** 2),
        ("Delta_b/A^2", mp.mpf(qd) / qa ** 2),
        ("Delta_b/(A*(A-1))", mp.mpf(qd) / (qa * (qa - 1))),
        ("Delta_b/(4*A)", mp.mpf(qd) / (4 * qa)),
        ("Delta_b/(A^2 - 1)", mp.mpf(qd) / (qa ** 2 - 1)),
    ]
    for name, val in candidates:
        out.append({
            "form": name,
            "f_at_QL09": mp.nstr(val, 30),
            "delta_vs_measured_a1": mp.nstr(abs(val - a1_QL09), 6),
            "consistent_with_a1_eq_0": bool(abs(val - a1_QL09) < mp.mpf("1e-30")),
        })

    # Affine 3-eq-3-unk solution evaluated at QL09
    affine_entry = next((e["form_affine_3eq3unk"] for e in scan_results
                         if "form_affine_3eq3unk" in e), None)
    affine_eval = None
    if affine_entry and "c1" in affine_entry:
        c1 = mp.mpf(affine_entry["c1"])
        c2 = mp.mpf(affine_entry["c2"])
        c3 = mp.mpf(affine_entry["c3"])
        # a_1 * (2A)^2 = c1*Db + c2*A + c3 -> a_1 = (...)/(2A)^2
        rhs = c1 * qd + c2 * qa + c3
        a1_pred = rhs / (2 * qa) ** 2
        affine_eval = {
            "form": "affine_3eq3unk on (V_quad, QL15, QL05)",
            "f_at_QL09_a1": mp.nstr(a1_pred, 30),
            "delta_vs_measured_a1": mp.nstr(abs(a1_pred - a1_QL09), 6),
            "consistent_with_a1_eq_0": bool(abs(a1_pred - a1_QL09) < mp.mpf("1e-30")),
        }

    # Polynomial families evaluated at QL09
    poly_eval = []
    for fam in poly_results.get("families", []):
        if "coefficients" not in fam:
            continue
        name = fam["family"]
        coeffs = [mp.mpf(s) for s in fam["coefficients"]]
        if "c0 + c1*Delta_b + c2/A^2" in name:
            pred = coeffs[0] + coeffs[1] * qd + coeffs[2] / qa ** 2
        elif "c0 + c1*Delta_b + c2*A" in name:
            pred = coeffs[0] + coeffs[1] * qd + coeffs[2] * qa
        elif "c0/A + c1*Delta_b/A + c2*Delta_b/A^2" in name:
            pred = coeffs[0] / qa + coeffs[1] * qd / qa + coeffs[2] * qd / qa ** 2
        elif "c0 + c1*Delta_b/(2A)^2 + c2/A" in name:
            pred = coeffs[0] + coeffs[1] * qd / (2 * qa) ** 2 + coeffs[2] / qa
        else:
            continue
        poly_eval.append({
            "family": name,
            "f_at_QL09": mp.nstr(pred, 30),
            "delta_vs_measured_a1": mp.nstr(abs(pred - a1_QL09), 6),
            "consistent_with_a1_eq_0": bool(abs(pred - a1_QL09) < mp.mpf("1e-30")),
        })

    return {
        "a1_QL09_measured": rep_data["QL09"]["a_1_median_str"][:60] + "...",
        "candidate_evaluations": out,
        "affine_evaluation": affine_eval,
        "polynomial_family_evaluations": poly_eval,
    }


# ---------- main ----------
def main() -> None:
    rep_data, src = load_inputs()
    add_claim("inputs_loaded_017c+T35", dps=300, script="t37j_runner.py",
              output_hash=sha(json.dumps(src, sort_keys=True)))

    precision_check(rep_data)
    add_claim("precision_check_passed_envelope_lt_1e-30_for_3_non_QL09_reps",
              dps=300, script="t37j_runner.py",
              output_hash=sha("precision_check"))

    # Phase A.3 CF reconstruction
    cf_table = {}
    for rid in ["V_quad", "QL15", "QL05"]:
        x = mp.mpf(rep_data[rid]["a_1_median_str"])
        p, q, err = cf_rational(x, q_max=1000)
        cf_table[rid] = {"p": p, "q": q, "err_str": mp.nstr(err, 6),
                         "rational_str": f"{p}/{q}",
                         "match_at_1e-30": bool(err < mp.mpf("1e-30"))}
        add_claim(f"cf_rational_{rid}={p}/{q}_err={mp.nstr(err, 3)}",
                  dps=300, script="t37j_runner.py",
                  output_hash=sha(f"{rid}:{p}/{q}"))

    # Phase B
    b_results = per_rep_pslq(rep_data)
    for rid, br in b_results.items():
        add_claim(f"pslq_per_rep_{rid}_tol_1e-30: {br['rel_tol_1e-30_explained']}",
                  dps=300, script="t37j_runner.py",
                  output_hash=sha(f"{rid}:tight:{br['rel_tol_1e-30']}"))
        add_claim(f"pslq_per_rep_{rid}_tol_1e-12: {br['rel_tol_1e-12_explained']}",
                  dps=300, script="t37j_runner.py",
                  output_hash=sha(f"{rid}:loose:{br['rel_tol_1e-12']}"))
        if br["hygiene_flag_loose_only"]:
            DISC.append({
                "rep": rid,
                "issue": "PSLQ relation appears at tol=1e-12 but not at tol=1e-30",
                "loose_relation": br["rel_tol_1e-12_explained"],
                "interpretation": "precision artefact, NOT a closed form",
            })

    # Phase C
    joint = joint_pslq(rep_data)
    for cfg in joint["configs"]:
        add_claim(f"joint_pslq[{cfg['atom_names'][0]}..]: tight={cfg['rel_tol_1e-30_explained']}",
                  dps=300, script="t37j_runner.py",
                  output_hash=sha(json.dumps(cfg["atom_names"]) + str(cfg["rel_tol_1e-30"])))

    scan = functional_form_scan(rep_data)
    best_form = None
    for entry in scan:
        if "form" in entry and entry.get("max_residual_below_1e-30"):
            best_form = entry
            break
    add_claim(f"functional_form_scan_best={best_form['form'] if best_form else 'none_passed_1e-30'}",
              dps=300, script="t37j_runner.py",
              output_hash=sha(json.dumps(scan, default=str)))

    poly = polynomial_fit(rep_data)
    add_claim("polynomial_in_(Delta_b,A)_fit: see a_1_unifying_relation_search.json",
              dps=300, script="t37j_runner.py",
              output_hash=sha(json.dumps(poly, default=str)))

    # Phase D
    bd = ql09_boundary(rep_data, scan, poly)
    bd_consistent = any(e["consistent_with_a1_eq_0"]
                        for e in bd["candidate_evaluations"])
    if bd.get("affine_evaluation"):
        bd_consistent = bd_consistent or bd["affine_evaluation"]["consistent_with_a1_eq_0"]
    add_claim(f"QL09_boundary_check: any_candidate_consistent_with_a1_eq_0={bd_consistent}",
              dps=300, script="t37j_runner.py",
              output_hash=sha(json.dumps(bd, default=str)))

    # Verdict logic
    # 1. unifying form across 3 reps: any scan entry with max_res < 1e-30
    # 2. + QL09 consistency
    rationals_clean = all(b_results[r]["rational_match_at_1e-30"]
                          for r in ["V_quad", "QL15", "QL05"])
    rationals_partial = any(b_results[r]["rational_match_at_1e-30"]
                            for r in ["V_quad", "QL15", "QL05"]) and not rationals_clean
    no_rationals = not any(b_results[r]["rational_match_at_1e-30"]
                           for r in ["V_quad", "QL15", "QL05"])

    if best_form is not None:
        if bd_consistent:
            verdict = "T37J_UNIFYING_RELATION_FOUND_INCLUDING_QL09"
        else:
            verdict = "T37J_UNIFYING_CLOSED_FORM_FOUND"
    elif rationals_clean:
        verdict = "T37J_RATIONAL_PER_REP_ONLY"
    elif rationals_partial:
        verdict = "T37J_RATIONAL_PARTIAL"
    else:
        verdict = "T37J_NO_RATIONAL_DETECTED"

    add_claim(f"verdict_label={verdict}",
              evidence_type="label",
              dps=300, script="t37j_runner.py",
              output_hash=sha(verdict))

    # Emit deliverables
    write_json(HERE / "a_1_pslq_per_rep.json", {
        "cf_rational_reconstruction": cf_table,
        "per_rep_pslq": b_results,
    })
    write_json(HERE / "a_1_unifying_relation_search.json", {
        "joint_pslq": joint,
        "functional_form_scan": scan,
        "polynomial_fit": poly,
        "ql09_boundary": bd,
    })

    write_jsonl(CLAIMS_PATH, CLAIMS)
    write_json(DISC_PATH, DISC)
    write_json(UNEX_PATH, UNEX)
    if not HALT_PATH.exists():
        write_json(HALT_PATH, {"halt": None, "verdict": verdict})

    print(f"VERDICT: {verdict}")
    print(f"AEAL claims: {len(CLAIMS)}")
    print(f"Deliverables in: {HERE}")


if __name__ == "__main__":
    main()
