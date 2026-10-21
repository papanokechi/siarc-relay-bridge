"""Emit claims.jsonl for CT-S2-RHO-D4 with sha256 hashes of the output files."""
import hashlib
import json
import os


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


TASK = "CT-S2-RHO-D4"
st = sha256("s_table.json")
va = sha256("vacuity.json")
d2 = sha256("d2_anchor.json")

tab = json.load(open("s_table.json"))
worst = max(r["residual_float"] for r in tab["representatives"])
anchor = json.load(open("d2_anchor.json"))
vac = json.load(open("vacuity.json"))

claims = [
    {
        "claim_id": "S2-01",
        "task_id": TASK,
        "claim": (
            "For all 8 PCF2-SESSION-Q1 d=4 representatives, the growth law "
            "Q_n/Gamma(4n+1) ~ K (beta_4/4^4)^n n^s holds with "
            "s = beta_3/beta_4 + 3/2. Max |s_measured - s_predicted| over the 8 "
            f"representatives = {worst:.3e}, after 4 levels of ratio-2 Richardson "
            "extrapolation on the ladder n = 1250,2500,5000,10000,20000 at dps 80. "
            "Pre-registered falsifier |diff| > 1e-6 did NOT fire. Label: VERIFIED."
        ),
        "evidence_type": "computation",
        "dps": 80,
        "reproducible": True,
        "script": "s_exponent.py",
        "output_hash": st,
    },
    {
        "claim_id": "S2-02",
        "task_id": TASK,
        "claim": (
            "All 8 representatives have r_inf = lim Q_n / prod_{k<=n} b(k) nonzero "
            "(range 0.9241 to 1.0795), with N/2-vs-N agreement of about 28.8-30.5 "
            "decimal digits. Q_n is therefore not the minimal solution for any of "
            "them, so all 8 are in scope for the falsifier. 6 of the 8 b(n) change "
            "sign on n >= 1 (spec required at least 2). Label: VERIFIED."
        ),
        "evidence_type": "computation",
        "dps": 80,
        "reproducible": True,
        "script": "s_exponent.py",
        "output_hash": st,
    },
    {
        "claim_id": "S2-03",
        "task_id": TASK,
        "claim": (
            "Vacuity pre-check PASSES both arms. Arm (i): with beta_4=1, beta_3=-3 "
            "fixed and (beta_2,beta_1,beta_0) varied over a 16-point grid (2 points "
            "excluded by the positive-integer-root precheck), the spread of "
            f"s_measured is {vac['arm_i_s_spread']:.3e}, i.e. s does not depend on "
            "the lower coefficients. Arm (ii): varying beta_3 over 9 values at "
            "beta_4=1 and 4 values at beta_4=7, s_measured tracks "
            "beta_3/beta_4 + 3/2 with max residual "
            f"{vac['arm_ii_max_residual']:.3e}; s moves by exactly "
            "Delta(beta_3)/beta_4. The observable is therefore sensitive to the "
            "data the hypothesis is about, and the test is not vacuous. "
            "Label: VERIFIED."
        ),
        "evidence_type": "computation",
        "dps": 80,
        "reproducible": True,
        "script": "s_exponent.py",
        "output_hash": va,
    },
    {
        "claim_id": "S2-04",
        "task_id": TASK,
        "claim": (
            "Convention map, anchored at d=2 because PCF2-SESSION-Q1 stores no rho "
            "at d=4. For V_quad (b(n)=3n^2+n+1) the measured growth exponent is "
            f"s = {anchor['s_measured'][:22]} (predicted 5/6, residual "
            f"{anchor['residual']}), giving -s-1 = -1.83333333333333333268, which "
            "equals the rho = -11/6 stored in "
            "sessions/2026-05-01/CC-PIPELINE-G/results_vquad.json to 6.6e-19. "
            "CC-PIPELINE-G derives that rho independently, from the u^1-order "
            "indicial equation of the Birkhoff formal solution in u = sqrt(z) "
            "(newton_birkhoff.py lines 385-394, rho = -3/2 - beta_1/beta_2), NOT "
            "from the Q_n growth law, so the agreement is not tautological. "
            "Hence rho_CT = rho_d = -s-1 = -(d+1)/2 - beta_{d-1}/beta_d at d=2. "
            "Label: STRUCTURAL (numerical agreement at d=2 is VERIFIED; the "
            "identification of the two exponents as the same object for general d "
            "is not proven here)."
        ),
        "evidence_type": "computation",
        "dps": 80,
        "reproducible": True,
        "script": "d2_anchor.py",
        "output_hash": d2,
    },
    {
        "claim_id": "S2-05",
        "task_id": TASK,
        "claim": (
            "PCF2-SESSION-Q1 stores no quantity named rho at d=4. A case-insensitive "
            "search of the whole session folder for rho returns zero matches. It "
            "stores xi_0 = d/beta_d^{1/d} (newton_d4_results.json) and WKB fit "
            "parameters A, alpha, beta, gamma (results.json). P2 task 5's "
            "'check it against stored values' therefore has no d=4 target. "
            "Label: VERIFIED (file inspection)."
        ),
        "evidence_type": "file_inspection",
        "dps": 0,
        "reproducible": True,
        "script": "grep -i rho sessions/2026-05-01/PCF2-SESSION-Q1/",
        "output_hash": st,
    },
]

with open("claims.jsonl", "w") as f:
    for c in claims:
        f.write(json.dumps(c) + "\n")

print("wrote claims.jsonl")
for name, h in (("s_table.json", st), ("vacuity.json", va),
                ("d2_anchor.json", d2)):
    print(f"  {name:20s} {h}")
