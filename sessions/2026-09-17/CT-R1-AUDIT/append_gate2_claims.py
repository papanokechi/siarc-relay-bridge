import hashlib, json
from pathlib import Path

D = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT")
S13 = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S13-COLDREAD5")


def h(p):
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING:" + str(p)


VS = h(D / "VERIFY-S13.md")
CO = h(S13 / "compute_system_a.out")
NO = h(D / "DRAFT-COMPANION-v1.3-NOTICE.md")

NOTE = ("cold: CT-S13-COLDREAD5 worked from a self-contained packet with no access to "
        "CT-S4-FORMAL-TYPE, CT-S5B-COVER, CLASSIFICATION-TABLE.md, any DRAFT-*, VERIFY-*, "
        "AUDIT.md or REPORT.md. It recomputed the Katz data in its own SymPy script "
        "(compute_system_a.py) and read Table 2.1 from the rendered page images, not an OCR "
        "layer. Different code and independent reading of the primary source.")

rows = [
    ("R1-52", "GATE 2 RESULT. Cold read of C4 returns: (A0)-(A3) and (A5) SOUND (Katz 1/2 at 0 and "
              "infinity, ramified, both doubled to 1 and unramified on the quadratic cover; the ODE "
              "annihilates the series, verified to z^43 in independent code); the Table 2.1 row "
              "lookups to PIII(D8) and PIII(D6) are correct as ordered Katz-data matches; but (A6) "
              "is ERROR as a family-membership inference.", "STRUCTURAL", "computation", CO, "cold",
     NOTE),
    ("R1-53", "NEW DEFECT FOUND BY GATE 2, independently re-verified by this session from the PDF: "
              "van der Put-Saito p.2634 states that the strong Riemann-Hilbert problem has a positive "
              "answer for every type EXCEPT possibly (1/2,-,1/2) and (-,-,5/2), and that for those two "
              "types they consider only the modules M(u) for which it does hold. (1/2,-,1/2) is "
              "exactly object A's type. The PIII(D8) row is therefore restricted by a condition that "
              "has NOT been checked for object A. Written into the notice as C4 point 5.",
     "INSPECTED", "file_inspection", VS, "cold", NOTE),
    ("R1-54", "The three-entry notation (1/2,-,1/2) is van der Put-Saito's OWN designation for the "
              "family, not a contraction introduced in this work: p.2634 reads 'We will not number "
              "these ten families, but indicate them by their Katz invariants, e.g., (0,0,0,0), "
              "(0,0,1), ..., (0,-,3/2), (-,-,3), (-,-,5/2).' The cold reader's Q5 caveat that the "
              "notation suppresses table columns is therefore not accepted on its premise, though its "
              "ordered-column point is correct and has been adopted.", "INSPECTED", "file_inspection",
     VS, "self", "self: resolved by this session from the running text on the same page; the isolated "
                 "reader was right to flag the apparent mismatch."),
    ("R1-55", "C4 weakened and re-grounded in response to gate 2. Added: point 1 now quotes the "
              "caption 'Classification of Families' and the trace-zero rank-2 setup from p.2634; "
              "point 5 the strong Riemann-Hilbert restriction; point 6 the unbridged "
              "scalar-operator-to-rank-2-connection gap (determinant condition, irreducibility, "
              "singular set unverified); point 7 that dim P = 0 for the PIII(D8) row, which bears on "
              "C3's single-fibre objection. Family membership of object A is NOT ESTABLISHED.",
     "STRUCTURAL", "file_inspection", NO, "cold", NOTE),
]

out = D / "claims.jsonl"
with out.open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh, rev, note in rows:
        f.write(json.dumps({
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R8", "claim": claim, "label": label,
            "evidence_type": ev, "dps": None, "reproducible": True,
            "script": "CT-S13-COLDREAD5/compute_system_a.py", "output_hash": oh,
            "review": rev, "review_note": note,
        }, ensure_ascii=False) + "\n")

print("appended", len(rows), "gate-2 claims")
for cid, *_ in rows:
    print(" ", cid)
