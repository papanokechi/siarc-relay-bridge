import hashlib, json
from pathlib import Path

D = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT")
NO = hashlib.sha256((D / "DRAFT-COMPANION-v1.3-NOTICE.md").read_bytes()).hexdigest()

SELF = ("self: authoring change to the draft notice made by this session under operator ruling; "
        "no independent party has read the revised wording.")

rows = [
    ("R1-56", "CORRECTION to R1-55 under operator review #6. The dim P = 0 note in C4 point 7 "
              "conflated two distinct things. P is the PARAMETER space of the family (vdP-Saito "
              "p.2634: 'a space of parameters P ... consisting of traces or eigenvalues of the "
              "matrices'), so dim P = 0 means PIII(D8) has no free parameters. That is expected and "
              "is NOT a defect, and it says nothing about the isomonodromic TIME variable, which "
              "still gives a one-dimensional deformation. The link CT-S13 drew to C3's single-fibre "
              "concern is a conflation and has been removed: C3 concerns the absence of a WRITTEN "
              "deformation, not the absence of parameters. Whether object A lies in a deformation is "
              "recorded as a separate open question.", "STRUCTURAL", "file_inspection", NO, "self",
     SELF),
    ("R1-57", "Recorded as a POSSIBLE APPROACH ONLY, carrying no weight: the quadratic cover of "
              "object A lands in the (1,-,1) row, which is NOT one of the two types vdP-Saito exempt "
              "from the strong Riemann-Hilbert guarantee. Whether the pullback can be used to decide "
              "the strong Riemann-Hilbert condition for object A itself is UNVERIFIED; the relation "
              "between the two problems has not been examined.", "CONJECTURED", "file_inspection",
     NO, "self", SELF),
    ("R1-58", "C2 restructured under operator ruling to lead with the ground that depends on nothing "
              "proved in this work: the companion's own theta_1 = theta_2 = 0, the companion's own "
              "stated scaling law, and Jimbo's published dictionary, all verified from page images. "
              "gamma = 1 - theta_0 - theta_t = 1 contradicts the published gamma = 0 using published "
              "sources alone. The apparency ground via C1 now follows as explicitly labelled "
              "independent corroboration, with the note that C1 leaves the exponent values intact "
              "and changes only the monodromy.", "STRUCTURAL", "file_inspection", NO, "self", SELF),
    ("R1-59", "C5 rewritten under operator ruling so that the notice RECORDS what fails rather than "
              "rebuilding the argument: item 1 refuted citing C1; the 'complete explanation' "
              "characterisation withdrawn; items 2-4 stated to not depend on apparency, with the "
              "explicit scope statement that their correctness is NOT re-examined in this notice. "
              "The words 'survive', 'stand' and 'unaffected' are avoided as endorsements, since "
              "nothing in this work has independently checked items 2-4. The same scope statement is "
              "applied to the untouched conclusions of Sec 2.2.", "STRUCTURAL", "file_inspection",
     NO, "self", SELF),
    ("R1-60", "Deposit-day P0 citation checklist added to the notice, covering four external "
              "citations (van der Put-Saito pp.2634-2635, Jimbo p.1152 including assumption (A1)_PV, "
              "companion v1.2 via its Zenodo version DOI, and DLMF Sec 32.2 with its release version "
              "and date). Per operator ruling it is deliberately NOT executed now, so that recorded "
              "hashes match what is cited on the deposit day. The checklist states that HYPOTHESES "
              "as well as theorem statements are in scope, per the Gautschi (2.8) near-miss.",
     "INSPECTED", "file_inspection", NO, "self", SELF),
]

out = D / "claims.jsonl"
with out.open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh, rev, note in rows:
        f.write(json.dumps({
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R9", "claim": claim, "label": label,
            "evidence_type": ev, "dps": None, "reproducible": True,
            "script": "append_r9_claims.py", "output_hash": oh,
            "review": rev, "review_note": note,
        }, ensure_ascii=False) + "\n")

print("appended", len(rows), "R9 claims")
for cid, *_ in rows:
    print(" ", cid)
