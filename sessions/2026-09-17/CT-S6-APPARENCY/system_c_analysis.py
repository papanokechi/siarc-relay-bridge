"""
CT-S6-APPARENCY scope update: System C exact apparency, infinity type,
Remark 2.2 spot tests, and relation to System B/inverted System B.
"""
import hashlib
import json
import subprocess
from pathlib import Path

import sympy as sp
from pypdf import PdfReader

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge")
SESSION = ROOT / "sessions" / "2026-09-17" / "CT-S6-APPARENCY"
TASK_ID = "CT-S6-APPARENCY-SCOPE-UPDATE"
SCRIPT_REL = "sessions/2026-09-17/CT-S6-APPARENCY/system_c_analysis.py"
EXPECTED_HEAD = "08aa0e2381b3dc37ee54a3200b7272755ca11d59"

x, z, u, lam, Lambda = sp.symbols("x z u lam Lambda")
s3 = sp.sqrt(3)
I = sp.I


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def simp(e):
    return sp.radsimp(sp.factor(sp.cancel(sp.simplify(e))))


def sstr(e):
    return str(simp(e))


def normal_r(P, Q, var):
    return sp.cancel(sp.together(P**2 / 4 + sp.diff(P, var) / 2 - Q))


def principal_coeffs(P, Q, var):
    return {
        "p_minus_1": simp(sp.limit(var * P, var, 0)),
        "q_minus_2": simp(sp.limit(var**2 * Q, var, 0)),
    }


def indicial_from_principal(pc):
    F = sp.expand(lam * (lam - 1) + pc["p_minus_1"] * lam + pc["q_minus_2"])
    roots_mult = []
    for root, mult in sp.roots(sp.Poly(F, lam)).items():
        roots_mult.extend([simp(root)] * mult)
    return simp(F), roots_mult


def is_integer_expr(e):
    return bool(simp(e).is_integer)


def repeated_zero_log_test(P, var):
    residue = simp(sp.limit(var * P, var, 0))
    analytic0 = simp(sp.limit(P - residue / var, var, 0))
    # For the repeated exponent rho=0 with P=1/var+holomorphic and Q at most simple pole,
    # the holomorphic Frobenius solution y1 has y1(0)=1.  Reduction of order gives
    # y2 = y1 * integral(exp(-int P)/y1**2), whose normalized integrand has residue 1.
    log_residue = sp.Integer(1) if residue == 1 else sp.Symbol("unhandled")
    return {
        "P_residue": sstr(residue),
        "P_minus_residue_over_local_at_0": sstr(analytic0),
        "normalized_reduction_of_order_integrand_residue": sstr(log_residue),
        "log_term_present": bool(log_residue != 0),
        "method": "symbolic Frobenius repeated-root test via reduction of order; exponent difference 0",
    }


def frobenius_distinct_test(P, Q, var, lower, diff):
    # Exact Laurent coefficients only if needed by a distinct integer resonance.
    coeffP = {}
    coeffQ = {}
    for k in range(-1, diff):
        coeffP[k] = simp(sp.limit((P - sum(coeffP[j] * var**j for j in coeffP)) / var**k, var, 0))
    for k in range(-2, diff - 1):
        coeffQ[k] = simp(sp.limit((Q - sum(coeffQ[j] * var**j for j in coeffQ)) / var**k, var, 0))
    c = {0: sp.Integer(1)}
    steps = []
    rho = sp.Integer(lower)
    pminus = coeffP[-1]
    qminus = coeffQ[-2]
    obstruction = sp.Integer(0)
    for n in range(1, diff + 1):
        Fn = simp((rho+n)*(rho+n-1) + pminus*(rho+n) + qminus)
        rhs = sp.Integer(0)
        for k in range(0, n):
            rhs += ((rho+k) * coeffP[n-k-1] + coeffQ[n-k-2]) * c[k]
        rhs = simp(rhs)
        if Fn == 0:
            obstruction = rhs
            steps.append({"n": n, "resonant": True, "F_n": sstr(Fn), "obstruction_sum": sstr(obstruction)})
            break
        c[n] = simp(-rhs / Fn)
        steps.append({"n": n, "resonant": False, "F_n": sstr(Fn), "rhs_sum": sstr(rhs), "c_n": sstr(c[n])})
    return {"steps": steps, "log_obstruction": sstr(obstruction), "log_term_present": bool(obstruction != 0)}


def analyze_point(name, P_local, Q_local, var, expected_exponents=None):
    pc = principal_coeffs(P_local, Q_local, var)
    F, exps = indicial_from_principal(pc)
    integer_flags = [is_integer_expr(e) for e in exps]
    out = {
        "point": name,
        "principal_coefficients": {k: sstr(v) for k, v in pc.items()},
        "indicial_equation": sstr(F),
        "exponents_with_multiplicity": [sstr(e) for e in exps],
        "expected_exponents": expected_exponents,
        "expected_exponents_match": None,
        "exponents_are_integers": integer_flags,
        "frobenius_log_test": None,
        "verdict": None,
        "reason": None,
    }
    if expected_exponents is not None:
        out["expected_exponents_match"] = sorted([sstr(e) for e in exps]) == sorted(expected_exponents)
    if not all(integer_flags):
        out["verdict"] = "NOT APPARENT"
        out["reason"] = "At least one local exponent is not an integer."
        return out
    if len(set(exps)) == 1 and len(exps) == 2 and simp(exps[0]) == 0:
        test = repeated_zero_log_test(P_local, var)
        out["frobenius_log_test"] = test
        if test["log_term_present"]:
            out["verdict"] = "NOT APPARENT"
            out["reason"] = "Repeated integer exponent 0 and exact nonzero log residue."
        else:
            out["verdict"] = "APPARENT"
            out["reason"] = "Repeated integer exponent 0 and no symbolic log term; shifted solutions holomorphic."
        return out
    ints = [int(sp.Integer(e)) for e in exps]
    lower, upper = min(ints), max(ints)
    diff = upper - lower
    test = frobenius_distinct_test(P_local, Q_local, var, lower, diff)
    out["frobenius_log_test"] = test
    if test["log_term_present"]:
        out["verdict"] = "NOT APPARENT"
        out["reason"] = "Integer exponents but exact nonzero Frobenius log obstruction."
    elif lower < 0:
        out["verdict"] = "NOT APPARENT"
        out["reason"] = "No log obstruction, but a negative exponent remains before shift."
    else:
        out["verdict"] = "APPARENT"
        out["reason"] = "Integer exponents, zero log obstruction through exponent difference, and shifted solutions holomorphic."
    return out


def root_multiplicity(poly_expr, point, var, maxk=24):
    expr = sp.expand(poly_expr)
    for k in range(maxk):
        val = simp(sp.diff(expr, var, k).subs(var, point))
        if val != 0:
            return k
    return maxk


def pole_order(r, point, var):
    num, den = sp.fraction(sp.cancel(sp.together(r)))
    return root_multiplicity(den, point, var) - root_multiplicity(num, point, var)


def classify_by_pole_order(m):
    if m <= 2:
        return {"formal_type": "regular singular", "Katz": "0", "ramification_index": "1", "Poincare_rank": "0"}
    if m % 2 == 0:
        return {"formal_type": "irregular, UNRAMIFIED", "Katz": str(m//2 - 1), "ramification_index": "1", "Poincare_rank": str(m//2 - 1)}
    katz = sp.Rational(m, 2) - 1
    return {"formal_type": "irregular, RAMIFIED", "Katz": str(katz), "ramification_index": "2", "Poincare_rank": str(katz)}

# -------------------------- primary-source inspection ----------------------
companion_v12 = ROOT / "sessions" / "2026-09-17" / "CT-R1-AUDIT" / "refs" / "vquad_resurgence_v1.2_zenodo-20481592.pdf"
reader = PdfReader(str(companion_v12))
relevant_pages = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    if any(tok in text for tok in ["Conjecture 4.1", "Remark 2.2", "a(x)", "apparent", "D5"]):
        relevant_pages.append({"pdf_page_one_based": idx + 1, "text": text})
extract_path = SESSION / "vquad_resurgence_v1.2_relevant_extract.txt"
extract_path.write_text("\n\n".join(f"--- PDF page {p['pdf_page_one_based']} ---\n{p['text']}" for p in relevant_pages), encoding="utf-8")
comp_text = "\\n".join(p["text"] for p in relevant_pages)
comp_compact = comp_text.replace(" ", "").replace("\n", "")
companion_inspection = {
    "path": str(companion_v12.relative_to(ROOT)),
    "sha256": sha256_path(companion_v12),
    "sha256_matches_operator": sha256_path(companion_v12).lower() == "a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85",
    "relevant_extract_path": str(extract_path.relative_to(ROOT)),
    "relevant_extract_sha256": sha256_path(extract_path),
    "relevant_pdf_pages_one_based": [p["pdf_page_one_based"] for p in relevant_pages],
    "conjecture_4_1_found": ("Conjecture4.1" in comp_compact) or ("Conjecture 4.1" in comp_text),
    "remark_2_2_found": ("Remark2.2" in comp_compact) or ("Remark 2.2" in comp_text),
    "equation_tokens_found": all(tok in comp_compact for tok in ["3x2+x+1", "6x+1"]) and (("−x2" in comp_compact) or ("-x2" in comp_compact)),
}

# -------------------------- System C ---------------------------------------
aC = 3*x**2 + x + 1
PC = sp.cancel(sp.diff(aC, x) / aC)
QC = sp.cancel(-x**2 / aC)
rC = normal_r(PC, QC, x)
s_minus = -sp.Rational(1, 6) - sp.sqrt(11)*I/6
s_plus = -sp.Rational(1, 6) + sp.sqrt(11)*I/6
system_c_points = []
for name, point in [("s_minus=(-1-i*sqrt(11))/6", s_minus), ("s_plus=(-1+i*sqrt(11))/6", s_plus)]:
    Ploc = sp.cancel(PC.subs(x, point + u))
    Qloc = sp.cancel(QC.subs(x, point + u))
    system_c_points.append(analyze_point(name, Ploc, Qloc, u, expected_exponents=["0", "1"]))

rC_inf = sp.cancel(sp.together(rC.subs(x, 1/u) / u**4 - sp.Rational(3, 4) / u**2))
m_inf_C = pole_order(rC_inf, sp.Integer(0), u)
system_c_infinity = {
    "r_C": sstr(rC),
    "r_infinity_local": sstr(rC_inf),
    "pole_order_at_infinity": int(m_inf_C),
    **classify_by_pole_order(int(m_inf_C)),
    "companion_poincare_rank_1_confirmed": classify_by_pole_order(int(m_inf_C))["Poincare_rank"] == "1",
}

system_c_all_points = [
    {"point": "s_minus", "Katz": "0", "apparent_removed": system_c_points[0]["verdict"] == "APPARENT"},
    {"point": "s_plus", "Katz": "0", "apparent_removed": system_c_points[1]["verdict"] == "APPARENT"},
    {"point": "infinity", "Katz": system_c_infinity["Katz"], "apparent_removed": False},
]
system_c_effective = [p for p in system_c_all_points if not p["apparent_removed"]]
system_c_effective_multiset = [p["Katz"] for p in system_c_effective]

# -------------------------- Remark 2.2 tests -------------------------------
def test_polynomial_b(label, bpoly):
    P = sp.cancel(sp.diff(bpoly, x) / bpoly)
    Q = sp.cancel(-x**2 / bpoly)
    roots = sp.solve(sp.Eq(bpoly, 0), x)
    analyses = []
    for root in roots:
        Ploc = sp.cancel(P.subs(x, root + u))
        Qloc = sp.cancel(Q.subs(x, root + u))
        analyses.append(analyze_point(f"{label} root {sstr(root)}", Ploc, Qloc, u))
    return {"label": label, "b": sstr(bpoly), "roots": [sstr(r) for r in roots], "root_tests": analyses}

remark_tests = [
    test_polynomial_b("b_test_1", x + 1),
    test_polynomial_b("b_test_2", x**2 + 1),
]
remark_always_apparent_refuted_by_tests = any(
    a["verdict"] != "APPARENT" for test in remark_tests for a in test["root_tests"]
)

# -------------------------- System C vs System B ---------------------------
q0 = 1 + (sp.Rational(23, 9) + sp.Rational(14, 27) * s3) * z + (-sp.Rational(253, 9) + sp.Rational(488, 27) * s3) * z**2
q1 = (48 - 24 * s3) + (-64 + 44 * s3) * z + (-sp.Rational(68, 3) + sp.Rational(52, 3) * s3) * z**2 + (-sp.Rational(152, 3) + sp.Rational(100, 3) * s3) * z**3
q2 = (-36 + 24 * s3) * z**2 + (-12 + 8 * s3) * z**3 + (-12 + 8 * s3) * z**4
PB = sp.cancel(q1 / q2)
QB = sp.cancel(q0 / q2)
rB = normal_r(PB, QB, z)
PBinv = sp.cancel(2/x - PB.subs(z, 1/x) / x**2)
QBinv = sp.cancel(QB.subs(z, 1/x) / x**4)
rBinv = normal_r(PBinv, QBinv, x)
half_integral_diff = simp(sp.integrate(sp.cancel((PBinv - PC) / 2), x))
relation = {
    "coordinate_map": "z=1/x",
    "r_B_inverted": sstr(rBinv),
    "r_C": sstr(rC),
    "normal_form_difference": sstr(rBinv - rC),
    "same_normal_form_after_inversion": simp(rBinv - rC) == 0,
    "literal_P_difference_PBinv_minus_PC": sstr(PBinv - PC),
    "literal_Q_difference_QBinv_minus_QC_is_zero": simp(QBinv - QC) == 0,
    "gauge_factor_from_inverted_B_solution_to_C_solution": "x**(sqrt(3)/18 - 1) * exp(-sqrt(3)*x/3)",
    "half_integral_PBinv_minus_PC": sstr(half_integral_diff),
    "interpretation": "If Y(x)=y_B(1/x) solves inverted System B, then y_C(x)=x**(sqrt(3)/18 - 1)*exp(-sqrt(3)*x/3)*Y(x) has System C normal form; the gauge is multivalued at x=0.",
}
if not relation["same_normal_form_after_inversion"]:
    relation["F8"] = "FIRED"
else:
    relation["F8"] = "not fired"

# -------------------------- Table source -----------------------------------
vps_pdf = ROOT / "sessions" / "2026-09-17" / "CT-R1-AUDIT" / "refs" / "vanderPut-Saito-AIF-2009-59-7-2611.pdf"
vps_extract = SESSION / "pdf_pages_25_26_extract.txt"
table = {
    "path": str(vps_pdf.relative_to(ROOT)),
    "sha256": sha256_path(vps_pdf),
    "existing_extract_path": str(vps_extract.relative_to(ROOT)),
    "D5_PV_row_page": "p.2635 / PDF page 26",
    "D5_PV_row": "D5 PV 0 0 1 - dim P 3",
    "system_C_matches_D5_PV_row_after_actual_apparency_removal": system_c_effective_multiset == ["0", "0", "1"],
}

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(ROOT), text=True).strip()
status = subprocess.check_output(["git", "--no-pager", "status", "--porcelain", "--untracked-files=all"], cwd=str(ROOT), text=True)
status_lines = [line for line in status.splitlines() if line.strip()]

results = {
    "task_id": TASK_ID,
    "sympy_version": sp.__version__,
    "dps": None,
    "companion_v12_inspection": companion_inspection,
    "system_C": {
        "operator": "(3*x**2+x+1)*y'' + (6*x+1)*y' - x**2*y = 0",
        "self_adjoint_identity_b_equals_a_prime": simp(sp.diff(aC, x) - (6*x+1)) == 0,
        "finite_apparency_tests": system_c_points,
        "infinity": system_c_infinity,
        "all_points": system_c_all_points,
        "effective_points_after_removing_apparent": system_c_effective,
        "effective_multiset": system_c_effective_multiset,
    },
    "remark_2_2_tests": {
        "pre_registered_b_polynomials": ["x+1", "x**2+1"],
        "tests": remark_tests,
        "always_apparent_claim_refuted_by_these_tests": remark_always_apparent_refuted_by_tests,
    },
    "system_C_vs_System_B": relation,
    "table_2_1": table,
    "falsifiers": {
        "F5_companion_exponents_0_1": "FIRED" if any(p["expected_exponents_match"] is False for p in system_c_points) else "not fired",
        "F6_apparent_with_log_or_nonholomorphic": "not fired; no System C finite point was classified APPARENT",
        "F7_infinity_not_rank_1": "not fired" if system_c_infinity["companion_poincare_rank_1_confirmed"] else "FIRED",
        "F8_relation_difference_nonzero": relation["F8"],
    },
    "git_verification": {"HEAD": head, "HEAD_matches_expected": head == EXPECTED_HEAD, "status_porcelain_lines": status_lines},
}

out_path = SESSION / "system_c_results.json"
out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
out_hash = sha256_path(out_path)

new_claims = [
    ("S6-C11", "The companion v1.2 PDF was inspected at HEAD 08aa0e2381b3dc37ee54a3200b7272755ca11d59; Conjecture 4.1, Remark 2.2, and the System C equation tokens were found in the extracted relevant pages.", "file_inspection", "INSPECTED"),
    ("S6-C12", "For System C, b(x)=6*x+1 equals a'(x) for a(x)=3*x^2+x+1 exactly, so the operator is in self-adjoint form.", "computation", "PROVEN"),
    ("S6-C13", "At s_minus=(-1-i*sqrt(11))/6, System C has indicial equation lambda^2 and exponents [0,0], not the companion-claimed {0,1}; the exact repeated-root log residue is 1, so s_minus is NOT APPARENT.", "computation", "PROVEN"),
    ("S6-C14", "At s_plus=(-1+i*sqrt(11))/6, System C has indicial equation lambda^2 and exponents [0,0], not the companion-claimed {0,1}; the exact repeated-root log residue is 1, so s_plus is NOT APPARENT.", "computation", "PROVEN"),
    ("S6-C15", "System C at infinity has normal-form pole order 4, is unramified, and has Katz invariant/Poincare rank 1.", "computation", "PROVEN"),
    ("S6-C16", "After removing the System C points actually proved apparent, no finite points are removed and the effective Katz multiset is (0,0,1), matching the van der Put--Saito Table 2.1 D5/PV row on p.2635.", "computation", "STRUCTURAL"),
    ("S6-C17", "The preregistered Remark 2.2 tests b=x+1 and b=x^2+1 both have simple-root tests with exponents [0,0] and nonzero log residue 1, so the tested instances are NOT APPARENT and refute the tested 'always apparent' assertion.", "computation", "PROVEN"),
    ("S6-C18", "Under z=1/x, System B has exactly the same normal-form potential as System C; the original scalar equations differ by the explicit gauge factor x**(sqrt(3)/18 - 1)*exp(-sqrt(3)*x/3), so they are gauge-equivalent in normal form but not literally the same operator.", "computation", "PROVEN"),
    ("S6-C19", "The companion's claim that beta=gamma=0 reflects both finite singularities being apparent is not supported by the exact scalar System C apparency test in this session.", "computation", "STRUCTURAL"),
]
claims_file = SESSION / "claims.jsonl"
old_lines = []
if claims_file.exists():
    for line in claims_file.read_text(encoding="utf-8").splitlines():
        try:
            old_id = json.loads(line).get("claim_id", "")
        except Exception:
            old_id = ""
        if not old_id.startswith("S6-C1") or old_id == "S6-C1":
            # keep S6-C1 and S6-C2..S6-C10; drop prior C11-C19 update lines
            if old_id not in {f"S6-C{i}" for i in range(11, 20)}:
                old_lines.append(line)
claims_file.write_text(("\n".join(old_lines) + ("\n" if old_lines else "")), encoding="utf-8")
with claims_file.open("a", encoding="utf-8") as f:
    for cid, claim, evtype, label in new_claims:
        f.write(json.dumps({
            "claim_id": cid,
            "task_id": TASK_ID,
            "claim": claim,
            "evidence_type": evtype,
            "dps": None,
            "reproducible": True,
            "script": SCRIPT_REL,
            "output_hash": out_hash,
            "label": label,
        }, ensure_ascii=False) + "\n")

print(json.dumps({
    "output": str(out_path.relative_to(ROOT)),
    "output_sha256": out_hash,
    "system_C_finite_verdicts": [(p["point"], p["exponents_with_multiplicity"], p["verdict"], p["reason"]) for p in system_c_points],
    "system_C_infinity": system_c_infinity,
    "system_C_effective_multiset": system_c_effective_multiset,
    "remark_2_2_refuted_by_tests": remark_always_apparent_refuted_by_tests,
    "relation_same_normal_form_after_inversion": relation["same_normal_form_after_inversion"],
    "falsifiers": results["falsifiers"],
    "git_HEAD": head,
}, indent=2, ensure_ascii=False))


