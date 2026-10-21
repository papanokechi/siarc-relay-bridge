import hashlib, json
from pathlib import Path

S = Path(__file__).resolve().parent
h = hashlib.sha256((S / "verify_s6.out").read_bytes()).hexdigest()

new = [
    ("R1-17", "System C's normal form equals the inverted System B normal form identically, both being (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2); independently re-derived in CT-R1-AUDIT without using CT-S6 outputs.", "PROVEN"),
    ("R1-18", "At every simple root s of chi with c(s)!=0, the equation chi*y''+chi'*y'+c*y=0 has indicial polynomial exactly lambda^2, so the exponents are 0,0 and the point is never apparent; this refutes companion Remark 2.2 in full generality rather than by counterexample.", "PROVEN"),
    ("R1-19", "System C at s_pm=(-1 +/- i*sqrt(11))/6 has normal-form residue -1/4, hence a repeated exponent 1/2, hence a log term: NOT APPARENT. The companion's claimed exponents {0,1} with theta_1=theta_2=0 are refuted.", "PROVEN"),
    ("R1-20", "System B's point z=infinity has exponents differing by exactly 1 and becomes an ordinary point of the normal form (R=11/4 finite at x=0 under z=1/x), so it carries no moduli; System B's effective Katz multiset after rank-1 normalisation is (0,0,1), not (1,0,0,0). CT-S6 claim S6-C7 is SUPERSEDED as an artefact of an apparency test that disallows twisting.", "STRUCTURAL"),
    ("R1-21", "Conjecture 4.1's conclusion (Sakai surface D5^(1), PV) is consistent with the van der Put-Saito Table 2.1 row (0,0,1) p.2635 for System C, but its stated reason is false because the finite singularities are not apparent; and a matching Katz multiset is necessary but not sufficient for family membership.", "STRUCTURAL"),
]

with (S / "claims.jsonl").open("a", encoding="utf-8") as f:
    for cid, claim, label in new:
        f.write(json.dumps({
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R2-VERIFY",
            "claim": claim, "label": label,
            "evidence_type": "computation", "dps": None, "reproducible": True,
            "script": "sessions/2026-09-17/CT-R1-AUDIT/verify_s6.py",
            "output_hash": h,
        }, ensure_ascii=False) + "\n")

lines = (S / "claims.jsonl").read_text(encoding="utf-8").strip().split("\n")
print(f"output_hash = {h}")
print(f"CT-R1-AUDIT claims now: {len(lines)}")
bad = [json.loads(l) for l in lines
       if json.loads(l).get("evidence_type") == "file_inspection"
       and json.loads(l).get("label") == "PROVEN"]
print(f"rule 1(a) violations: {len(bad)}")
