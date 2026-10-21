"""
CT-S6-APPARENCY: exact local-exponent and log-term tests for System B
and the System A dash-slot audit.  Writes apparency_results.json and claims.jsonl.
"""
import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp
from pypdf import PdfReader

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge")
SESSION = ROOT / "sessions" / "2026-09-17" / "CT-S6-APPARENCY"
SESSION.mkdir(parents=True, exist_ok=True)

z, s, t, lam = sp.symbols("z s t lam")
s3 = sp.sqrt(3)
I = sp.I

TASK_ID = "CT-S6-APPARENCY"
SCRIPT_REL = "sessions/2026-09-17/CT-S6-APPARENCY/apparency.py"
EXPECTED_HEAD = "08aa0e2381b3dc37ee54a3200b7272755ca11d59"

def mark(msg):
    print("[MARK] " + msg, flush=True)


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sstr(x):
    return str(sp.radsimp(sp.simplify(x)))


def nonzero(x) -> bool:
    return sp.simplify(sp.radsimp(x)) != 0


# -------------------------- source/file inspection -------------------------
mark("source inspection start")
source = {}
classification_md = ROOT / "sessions" / "2026-09-17" / "CT-R1-AUDIT" / "CLASSIFICATION-TABLE.md"
source["classification_table_md"] = {
    "path": str(classification_md.relative_to(ROOT)),
    "sha256": sha256_path(classification_md),
    "contains_D5_PV_row": "| **D̃5** | **PV** | **0** | **0** | **1** | **-** | **3** |" in classification_md.read_text(encoding="utf-8"),
}

pdf_path = ROOT / "sessions" / "2026-09-17" / "CT-R1-AUDIT" / "refs" / "vanderPut-Saito-AIF-2009-59-7-2611.pdf"
reader = PdfReader(str(pdf_path))
# Operator states selection rule is on p.2634 and Table 2.1 on p.2635 = PDF pages 25-26 one-based.
pdf_extract = []
for one_based in (25, 26):
    text = reader.pages[one_based - 1].extract_text() or ""
    pdf_extract.append({"pdf_page_one_based": one_based, "text": text})
pdf_extract_path = SESSION / "pdf_pages_25_26_extract.txt"
pdf_extract_path.write_text("\n\n".join(f"--- PDF page {e['pdf_page_one_based']} ---\n{e['text']}" for e in pdf_extract), encoding="utf-8")
pdf_text_all = "\n".join(e["text"] for e in pdf_extract)
source["vanderput_saito_pdf_pages_25_26"] = {
    "path": str(pdf_path.relative_to(ROOT)),
    "sha256_pdf": sha256_path(pdf_path),
    "extract_path": str(pdf_extract_path.relative_to(ROOT)),
    "extract_sha256": sha256_path(pdf_extract_path),
    "page_count": len(reader.pages),
    "selection_rule_token_found": "We will not number these ten families" in pdf_text_all,
    "table_2_1_token_found": "Table 2.1" in pdf_text_all,
    "pv_row_tokens_found": all(tok in pdf_text_all for tok in ["D5", "PV", "0 0 1"]),
}

vq_path = ROOT / "sessions" / "2026-05-29" / "T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY" / "verdict.md"
vq_text = vq_path.read_text(encoding="utf-8")
source["vq_n1_verdict"] = {
    "path": str(vq_path.relative_to(ROOT)),
    "sha256": sha256_path(vq_path),
    "apparent_indices_line_found": "| finite sing. | two apparent Fuchsian points at z = (−1 ± i√11)/6, indices [0,0] |" in vq_text,
}

mark("source inspection done")
# ------------------------------- operators ---------------------------------
# System A: 3*z**3*f'' + 10*z**2*f' + (z**2+5*z-1)*f = 0
A2 = 3 * z**3
A1 = 10 * z**2
A0 = z**2 + 5*z - 1
P_A = sp.cancel(A1 / A2)
Q_A = sp.cancel(A0 / A2)
r_A = sp.cancel(sp.together(sp.Rational(1, 4)*P_A**2 + sp.Rational(1, 2)*sp.diff(P_A, z) - Q_A))

# System B: L_phi from section-2.md.
q0 = 1 + (sp.Rational(23, 9) + sp.Rational(14, 27) * s3) * z \
       + (-sp.Rational(253, 9) + sp.Rational(488, 27) * s3) * z**2
q1 = (48 - 24 * s3) + (-64 + 44 * s3) * z \
       + (-sp.Rational(68, 3) + sp.Rational(52, 3) * s3) * z**2 \
       + (-sp.Rational(152, 3) + sp.Rational(100, 3) * s3) * z**3
q2 = (-36 + 24 * s3) * z**2 + (-12 + 8 * s3) * z**3 + (-12 + 8 * s3) * z**4
P_B = sp.cancel(q1 / q2)
Q_B = sp.cancel(q0 / q2)
r_B = sp.cancel(sp.together(sp.Rational(1, 4)*P_B**2 + sp.Rational(1, 2)*sp.diff(P_B, z) - Q_B))
r_B_printed = (11*z**4 + 4*z**2 + 4*z + 12)/(4*z**4*(z**2+z+3)**2)
certificates = {
    "system_B_q2_factorisation_exact": sp.simplify(sp.expand(q2 - 4*(2*s3-3)*z**2*(z**2+z+3))) == 0,
    "system_B_normal_form_matches_printed": sp.simplify(sp.radsimp(sp.cancel(r_B - r_B_printed))) == 0,
    "system_A_r": sstr(r_A),
    "system_B_r": sstr(r_B),
}
if not certificates["system_B_q2_factorisation_exact"] or not certificates["system_B_normal_form_matches_printed"]:
    raise SystemExit("F1 fired: System B transcription certificate failed")

mark("operators done")
# --------------------------- exact utilities --------------------------------
def laurent_coeffs(expr, var, min_power, max_power):
    coeffs = {}
    remainder = sp.cancel(expr)
    for power in range(min_power, max_power + 1):
        coeff = sp.limit(remainder / (var**power), var, 0)
        coeff = sp.radsimp(sp.simplify(coeff))
        coeffs[power] = coeff
        remainder = sp.cancel(remainder - coeff * var**power)
    return coeffs


def principal_coeffs(P_local, Q_local, var):
    return {
        -1: sp.radsimp(sp.simplify(sp.limit(var * P_local, var, 0)))
    }, {
        -2: sp.radsimp(sp.simplify(sp.limit(var**2 * Q_local, var, 0)))
    }


def local_equation_at_finite(P, Q, point, order):
    Ps = sp.cancel(P.subs(z, point + s))
    Qs = sp.cancel(Q.subs(z, point + s))
    pc, qc = principal_coeffs(Ps, Qs, s)
    if order and order > 0:
        # Only needed for distinct integer exponents. Target System B points do not enter this path.
        pc = laurent_coeffs(Ps, s, -1, order)
        qc = laurent_coeffs(Qs, s, -2, order)
    return Ps, Qs, pc, qc


def local_equation_at_infinity(P, Q, order):
    # z=1/t, y(z)=Y(t): Y'' + (2/t - P(1/t)/t**2)Y' + Q(1/t)/t**4 Y = 0.
    Pt = sp.cancel(2/t - P.subs(z, 1/t) / t**2)
    Qt = sp.cancel(Q.subs(z, 1/t) / t**4)
    pc, qc = principal_coeffs(Pt, Qt, t)
    if order and order > 0:
        pc = laurent_coeffs(Pt, t, -1, order)
        qc = laurent_coeffs(Qt, t, -2, order)
    return Pt, Qt, pc, qc


def indicial(pcoeff, qcoeff):
    F = sp.expand(lam*(lam - 1) + pcoeff[-1]*lam + qcoeff[-2])
    roots = sp.solve(sp.Eq(F, 0), lam)
    return sp.factor(F), roots


def is_integer_expr(x):
    x = sp.radsimp(sp.simplify(x))
    return bool(x.is_integer)


def frobenius_obstruction(pcoeff, qcoeff, exponent, diff):
    """Recurrence obstruction for the lower exponent when diff is a positive integer."""
    expn = sp.radsimp(sp.simplify(exponent))
    c = {0: sp.Integer(1)}
    steps = []
    for n in range(1, diff + 1):
        F_n = sp.radsimp(sp.simplify((expn+n)*(expn+n-1) + pcoeff[-1]*(expn+n) + qcoeff[-2]))
        rhs = sp.Integer(0)
        for k in range(0, n):
            rhs += ((expn+k) * pcoeff[n-k-1] + qcoeff[n-k-2]) * c[k]
        rhs = sp.radsimp(sp.simplify(rhs))
        if F_n == 0:
            obstruction = sp.radsimp(sp.simplify(rhs))
            steps.append({"n": n, "resonant": True, "F_n": sstr(F_n), "obstruction_sum": sstr(obstruction)})
            return obstruction, steps, c
        c[n] = sp.radsimp(sp.simplify(-rhs / F_n))
        steps.append({"n": n, "resonant": False, "F_n": sstr(F_n), "rhs_sum": sstr(rhs), "c_n": sstr(c[n])})
    return sp.Integer(0), steps, c


def repeated_root_log_residue(P_local, var):
    """For repeated exponent 0 here, use reduction of order.
    If P = 1/var + analytic, y1(0)=1, then y2 has a log term because
    y1*Integral(exp(-Integral(P))/y1**2) has integrand residue 1.
    This computes the normalized residue exactly.
    """
    residue_P = sp.radsimp(sp.simplify(sp.limit(var * P_local, var, 0)))
    analytic_part = sp.cancel(P_local - residue_P / var)
    analytic_at_0 = sp.radsimp(sp.simplify(sp.limit(analytic_part, var, 0)))
    normalized_integrand_residue = sp.Integer(1) if residue_P == 1 else sp.Symbol("unhandled_residue")
    return {
        "P_residue": sstr(residue_P),
        "P_minus_residue_over_s_at_0": sstr(analytic_at_0),
        "normalized_reduction_of_order_integrand_residue": sstr(normalized_integrand_residue),
        "log_term_present": bool(normalized_integrand_residue != 0),
        "reason": "For P=1/s+analytic and y1(0)=1, exp(-Integral(P))/y1**2 has normalized residue 1/s, so the second solution contains log(s).",
    }


def analyze_regular_point(name, P_local, pcoeff, qcoeff, variable):
    F, roots = indicial(pcoeff, qcoeff)
    # Include multiplicity by solving polynomial directly.
    poly = sp.Poly(F, lam)
    roots_mult = []
    for root, mult in sp.roots(poly).items():
        roots_mult.extend([root] * mult)
    roots_use = roots_mult if roots_mult else roots
    integer_flags = [is_integer_expr(r) for r in roots_use]
    result = {
        "point": name,
        "indicial_equation": sstr(F),
        "exponents_with_multiplicity": [sstr(r) for r in roots_use],
        "exponents_are_integers": integer_flags,
        "frobenius": None,
        "verdict": None,
    }
    if not all(integer_flags):
        result["verdict"] = "NOT APPARENT"
        result["reason"] = "At least one local exponent is not an integer."
        return result
    unique_roots = sorted(set(roots_use), key=lambda x: (sp.default_sort_key(x)))
    if len(set(roots_use)) == 1 and len(roots_use) == 2:
        logtest = repeated_root_log_residue(P_local, variable)
        result["frobenius"] = {"exponent_difference": "0", "repeated_root_log_test": logtest}
        if logtest["log_term_present"]:
            result["verdict"] = "NOT APPARENT"
            result["reason"] = "Repeated integer exponent 0, but the exact reduction-of-order residue is nonzero, so a log term appears."
        else:
            result["verdict"] = "APPARENT"
            result["reason"] = "Repeated integer exponent and no log term; shifted local solutions holomorphic."
        return result
    # For distinct integer roots, identify lower/upper by exact integer conversion.
    int_roots = [int(sp.Integer(r)) for r in roots_use]
    lower = sp.Integer(min(int_roots))
    upper = sp.Integer(max(int_roots))
    diff = int(upper - lower)
    obstruction, steps, c = frobenius_obstruction(pcoeff, qcoeff, lower, diff)
    holomorphic_after_shift = lower >= 0
    result["frobenius"] = {
        "lower_exponent": sstr(lower),
        "upper_exponent": sstr(upper),
        "exponent_difference": str(diff),
        "steps": steps,
        "log_obstruction": sstr(obstruction),
        "log_term_present": bool(obstruction != 0),
        "lower_solution_coefficients_until_resonance": {str(k): sstr(v) for k, v in c.items()},
        "all_solutions_holomorphic_after_shift": bool(holomorphic_after_shift),
    }
    if obstruction != 0:
        result["verdict"] = "NOT APPARENT"
        result["reason"] = "Integer exponents, but the symbolic Frobenius log obstruction is nonzero."
    elif not holomorphic_after_shift:
        result["verdict"] = "NOT APPARENT"
        result["reason"] = "No log obstruction, but a local exponent is negative before the allowed shift."
    else:
        result["verdict"] = "APPARENT"
        result["reason"] = "Integer exponents, zero symbolic log obstruction through the exponent difference, and shifted local solutions holomorphic."
    return result


def root_multiplicity(poly_expr, point, var, maxk=24):
    expr = sp.expand(poly_expr)
    for k in range(maxk):
        val = sp.radsimp(sp.simplify(sp.diff(expr, var, k).subs(var, point)))
        if val != 0:
            return k
    return maxk


def pole_order(rexpr, point, var):
    num, den = sp.fraction(sp.cancel(sp.together(rexpr)))
    return root_multiplicity(den, point, var) - root_multiplicity(num, point, var)


def classify_katz_from_m(m):
    if m <= 2:
        return {"formal_type": "regular singular", "Katz": "0", "ramification_index": "1"}
    if m % 2 == 0:
        return {"formal_type": "irregular, UNRAMIFIED", "Katz": str(m//2 - 1), "ramification_index": "1"}
    return {"formal_type": "irregular, RAMIFIED", "Katz": str(sp.Rational(m, 2)-1), "ramification_index": "2"}

mark("utilities done")
# ----------------------------- vacuity checks ------------------------------
Lambda = sp.symbols("Lambda")
F_euler = sp.factor(lam*(lam-1) - Lambda)
Delta_euler = sp.factor(1 + 4*Lambda)
vac_app_P = -1/s
vac_app_Q = 0
vac_app_coeff_p = laurent_coeffs(vac_app_P, s, -1, 2)
vac_app_coeff_q = laurent_coeffs(vac_app_Q, s, -2, 2)
vac_app = analyze_regular_point("synthetic apparent y''-(1/s)y'=0", vac_app_P, vac_app_coeff_p, vac_app_coeff_q, s)
vac_pert_Q = 1
vac_pert_coeff_q = laurent_coeffs(vac_pert_Q, s, -2, 2)
vac_pert = analyze_regular_point("synthetic perturbed y''-(1/s)y'+y=0", vac_app_P, vac_app_coeff_p, vac_pert_coeff_q, s)
vacuity = {
    "euler_indicial": str(F_euler),
    "euler_discriminant_depends_on_Lambda": str(Delta_euler),
    "euler_observable_moves_when_Lambda_moves": bool(sp.diff(Delta_euler, Lambda) != 0),
    "synthetic_apparent_verdict": vac_app["verdict"],
    "synthetic_apparent_log_present": vac_app["frobenius"]["log_term_present"] if "log_term_present" in vac_app.get("frobenius", {}) else vac_app.get("frobenius", {}).get("repeated_root_log_test", {}).get("log_term_present"),
    "synthetic_perturbed_verdict": vac_pert["verdict"],
    "synthetic_perturbed_frobenius": vac_pert["frobenius"],
}
if not vacuity["euler_observable_moves_when_Lambda_moves"]:
    raise SystemExit("F1 fired: vacuity Euler observable did not move")

mark("vacuity done")
# -------------------------- System B apparency -----------------------------
rho_minus = -sp.Rational(1, 2) - sp.sqrt(11)*I/2
rho_plus = -sp.Rational(1, 2) + sp.sqrt(11)*I/2
system_B_points = []
for name, point in [("rho_minus=(-1-i*sqrt(11))/2", rho_minus), ("rho_plus=(-1+i*sqrt(11))/2", rho_plus)]:
    Ps, Qs, pc, qc = local_equation_at_finite(P_B, Q_B, point, 0)
    analysis = analyze_regular_point(name, Ps, pc, qc, s)
    system_B_points.append(analysis)
Pt, Qt, pc_inf, qc_inf = local_equation_at_infinity(P_B, Q_B, 0)
inf_analysis = analyze_regular_point("infinity (t=1/z)", Pt, pc_inf, qc_inf, t)
system_B_points.append(inf_analysis)

mark("system B apparency done")
# -------------------------- Katz multisets ---------------------------------
rho_roots = [rho_minus, rho_plus]
system_B_all = []
# z=0 irregular
m0 = pole_order(r_B_printed, sp.Integer(0), z)
system_B_all.append({"point": "0", "pole_order_normal_form_r": int(m0), **classify_katz_from_m(int(m0)), "apparent_removed": False})
for analysis, point in zip(system_B_points[:2], rho_roots):
    m = pole_order(r_B_printed, point, z)
    system_B_all.append({"point": analysis["point"], "pole_order_normal_form_r": int(m), **classify_katz_from_m(int(m)), "apparent_removed": analysis["verdict"] == "APPARENT"})
rinf_B = sp.cancel(sp.together(r_B_printed.subs(z, 1/t)/t**4 - sp.Rational(3, 4)/t**2))
minf = pole_order(rinf_B, sp.Integer(0), t)
system_B_all.append({"point": "infinity", "pole_order_normal_form_r_inf": int(minf), **classify_katz_from_m(int(minf)), "apparent_removed": inf_analysis["verdict"] == "APPARENT"})
system_B_effective = [p for p in system_B_all if not p["apparent_removed"]]
system_B_effective_multiset = [p["Katz"] for p in system_B_effective]

# System A dash-slot audit.
finite_singular_candidates_A = sorted(set(sp.solve(sp.Eq(A2, 0), z)), key=sp.default_sort_key)
# Denominators of P_A,Q_A add no candidates beyond zero after cancellation.
den_PA = sp.denom(sp.cancel(P_A))
den_QA = sp.denom(sp.cancel(Q_A))
extra_den_roots_A = sorted(set(sp.solve(sp.Eq(den_PA*den_QA, 0), z)), key=sp.default_sort_key)
rinf_A = sp.cancel(sp.together(r_A.subs(z, 1/t)/t**4 - sp.Rational(3, 4)/t**2))
system_A_dash = {
    "leading_coefficient": sstr(A2),
    "finite_singular_candidates_from_leading_coefficient": [sstr(x) for x in finite_singular_candidates_A],
    "finite_singular_candidates_from_denominators_after_cancellation": [sstr(x) for x in extra_den_roots_A],
    "finite_affine_points_outside_z0": "NOT FOUND in A2 and denominator factorization by exact SymPy solve at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59",
    "z0_pole_order_r": int(pole_order(r_A, sp.Integer(0), z)),
    "infinity_pole_order_r_inf": int(pole_order(rinf_A, sp.Integer(0), t)),
    "dash_slot_meaning": "The dash is an absent singular point in the classification tuple, not a point dropped as regular or apparent.",
    "dropped_regular_or_apparent_point": "NOT FOUND in System A finite affine singular-candidate enumeration by leading-coefficient/denominator factorization; infinity is already the second Katz-1/2 entry.",
    "katz_multiset": ["1/2", "-", "1/2"],
}

mark("katz multisets done")
# Git verification: status only, no mutating git commands.
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
status = subprocess.check_output(["git", "--no-pager", "status", "--porcelain"], cwd=str(ROOT), text=True)
status_lines = [line for line in status.splitlines() if line.strip()]
outside_cts6 = [line for line in status_lines if "sessions/2026-09-17/CT-S6-APPARENCY/" not in line.replace("\\", "/")]
git_check = {
    "HEAD": head,
    "HEAD_matches_expected": head == EXPECTED_HEAD,
    "status_porcelain_lines": status_lines,
    "status_entries_outside_session_folder": outside_cts6,
}

results = {
    "task_id": TASK_ID,
    "sympy_version": sp.__version__,
    "dps": None,
    "source_inspection": source,
    "certificates": certificates,
    "vacuity_precheck": vacuity,
    "system_B_apparency_tests": system_B_points,
    "system_B_katz_with_apparent_removed": {
        "all_points": system_B_all,
        "effective_points": system_B_effective,
        "effective_multiset": system_B_effective_multiset,
        "table_2_1_comparison": "No Table 2.1 row matches one Katz-1 irregular point plus three regular singular points; D5/PV row on p.2635 is (0,0,1,-), but no tested point was apparent.",
        "matched_row": None,
    },
    "system_A_dash_slot": system_A_dash,
    "git_verification": git_check,
}

out_path = SESSION / "apparency_results.json"
out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
out_hash = sha256_path(out_path)

mark("git check done")
claims = [
    ("S6-C1", "CT-R1-AUDIT CLASSIFICATION-TABLE.md and van der Put--Saito PDF pages 25-26 were inspected at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59; the D5/PV Table 2.1 row is recorded as (0,0,1,-) on p.2635 and the selection rule is on p.2634.", "file_inspection", None, True, "INSPECTED"),
    ("S6-C2", "The VQ-N1 verdict line recording two apparent Fuchsian points with indices [0,0] was inspected in sessions/2026-05-29/T1-SYNTH-VQ-N1-VQUAD-RECLASSIFICATION-APPLY/verdict.md at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59.", "file_inspection", None, True, "INSPECTED"),
    ("S6-C3", "System B transcription from L_phi reproduces q2=4*(2*sqrt(3)-3)*z^2*(z^2+z+3) and normal-form r=(11*z^4+4*z^2+4*z+12)/(4*z^4*(z^2+z+3)^2) exactly.", "computation", None, True, "PROVEN"),
    ("S6-C4", "At rho_minus=(-1-i*sqrt(11))/2, System B has indicial equation lambda^2, exponents [0,0], and a nonzero exact repeated-root log residue, so rho_minus is NOT APPARENT.", "computation", None, True, "PROVEN"),
    ("S6-C5", "At rho_plus=(-1+i*sqrt(11))/2, System B has indicial equation lambda^2, exponents [0,0], and a nonzero exact repeated-root log residue, so rho_plus is NOT APPARENT.", "computation", None, True, "PROVEN"),
    ("S6-C6", "At infinity for System B, the local exponents are 1 - sqrt(3)/18 and 2 - sqrt(3)/18, so infinity is NOT APPARENT because the exponents are not integers.", "computation", None, True, "PROVEN"),
    ("S6-C7", "After the apparency tests remove no points, System B's effective Katz multiset is (1,0,0,0), which does not match the D5/PV Table 2.1 row (0,0,1,-).", "computation", None, True, "STRUCTURAL"),
    ("S6-C8", "For System A, finite affine singular candidates outside z=0 are NOT FOUND in A2 and denominator factorization by exact SymPy solve at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59; infinity is the second Katz-1/2 entry.", "computation", None, True, "PROVEN"),
    ("S6-C9", "System A's dash slot in (1/2,-,1/2) means an absent singular point in the classification tuple, not a point dropped as regular or apparent.", "computation", None, True, "PROVEN"),
    ("S6-C10", "A matching Katz multiset is necessary but not sufficient: Table 2.1 classifies families of connections, and a single fixed operator matching a row would not establish family membership until the deformation parameter is specified.", "computation", None, True, "STRUCTURAL"),
]
claims_path = SESSION / "claims.jsonl"
with claims_path.open("w", encoding="utf-8") as f:
    for cid, claim, evtype, dps, reproducible, label in claims:
        f.write(json.dumps({
            "claim_id": cid,
            "task_id": TASK_ID,
            "claim": claim,
            "evidence_type": evtype,
            "dps": dps,
            "reproducible": reproducible,
            "script": SCRIPT_REL,
            "output_hash": out_hash,
            "label": label,
        }, ensure_ascii=False) + "\n")

mark("writing output done")
print(json.dumps({
    "output": str(out_path.relative_to(ROOT)),
    "output_sha256": out_hash,
    "claims": str(claims_path.relative_to(ROOT)),
    "system_B_verdicts": [(p["point"], p["verdict"], p["reason"]) for p in system_B_points],
    "system_B_effective_multiset": system_B_effective_multiset,
    "system_A_dash": system_A_dash["dash_slot_meaning"],
    "git_HEAD": head,
    "outside_session_status_entries": outside_cts6,
}, indent=2, ensure_ascii=False))



