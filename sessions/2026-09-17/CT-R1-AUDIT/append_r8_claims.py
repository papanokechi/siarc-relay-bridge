import hashlib, json
from pathlib import Path

D = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT")


def h(rel):
    p = D / rel
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING:" + rel


GL = h("gate1_locate.log")
AR = h("AUTHOR-REQUEST-WONGLI.md")
GV = h("GATE1-VERIFY.md")
R8 = h("apply_audit_r8.log")
NO = h("DRAFT-COMPANION-v1.3-NOTICE.md")

rows = [
    ("R1-44", "The Wong-Li title in the operator's draft author request was defective: it read "
              "'Asymptotic expansions for second-order difference equations, II', omitting the word "
              "'linear'. Both the publisher record (Crossref, DOI 10.1002/sapm1992874289) and the "
              "stored DLMF bibliography (refs/dlmf_bib_W.html) give 'second-order LINEAR difference "
              "equations'. Corrected in both the subject line and the body. Aggravating factor: DLMF "
              "1992b carries the same title minus the trailing 'II', so a degraded title can resolve "
              "to the wrong paper.", "INSPECTED", "file_inspection", AR, "self"),
    ("R1-45", "The signature block of the author request (mononym 'Papanokechi', ORCID "
              "0009-0000-6192-8273, Yokohama) was verified character by character, ORCID digit by "
              "digit, against sessions/2026-06-16/VQUAD-ZENODO-DEPOSIT-001/upload-copy-paste.md. It "
              "matches. No part of the identity block was invented.", "INSPECTED", "file_inspection",
     AR, "self"),
    ("R1-46", "GATE 1 PASS. Every tuple, equation number and remark number quoted in "
              "DRAFT-COMPANION-v1.3-NOTICE.md was checked against companion v1.2 (sha256 a5d9e264...) "
              "by locating the pages and then reading 3x-rendered page images per the P0 rule. All 11 "
              "checked items match, including Remark 2.2's number and verbatim apparency wording, "
              "Conjecture 4.1's number, and the tuple (alpha,beta,gamma,delta) = (1/6, 0, 0, -1/2). "
              "No defect found.", "INSPECTED", "file_inspection", GL, "self"),
    ("R1-47", "Companion v1.2 p.6 states and applies the PV scaling law "
              "(alpha,beta,gamma,delta) -> (alpha,beta,c*gamma,c^2*delta) with c=sqrt(3), to send "
              "delta_raw=-1/6 to delta=-1/2. This is the SAME law used in our refutation, so the "
              "'convention artefact' defence of gamma=0 is closed by the companion's own text. Its "
              "assertion that the rescaling leaves gamma=0 invariant holds only because gamma was "
              "assumed 0; the correct value gamma=1 maps to sqrt(3).", "INSPECTED", "file_inspection",
     GL, "self"),
    ("R1-48", "The gamma contradiction does not depend on the C1 apparency lemma. The companion's own "
              "assignment theta_1 = theta_2 = 0 is CORRECT as a statement about local exponents; "
              "Jimbo's dictionary gamma = 1 - theta_0 - theta_t then yields gamma = 1, so the "
              "published gamma = 0 is unattainable on the companion's own local data. C1 is "
              "load-bearing only for the monodromy statement (unipotent, nontrivial) and for Remark "
              "2.2 itself. C2 therefore has two independent grounds.", "PROVEN", "proof", GV, "self"),
    ("R1-49", "A full-text pass over companion v1.2 located five passages depending on the apparency "
              "claim, now tabulated as section C5 of the draft notice. The substantive one is Sec 7.1 "
              "item 1, which offers apparency as the first of four components of a 'complete "
              "explanation' for the identification obstruction; it must be withdrawn or re-argued. "
              "The other three components are unaffected, the theta_1=theta_2=0 degeneration of the "
              "Jimbo connection formula in particular, since those exponent values are correct.",
     "INSPECTED", "file_inspection", GL, "self"),
    ("R1-50", "GATE 3 (wording): one defect found and fixed. 'Necessary condition' language is present "
              "on every row match (C4 point 1, reinforced by points 2-4): PASS. C3 was NOT verbatim as "
              "drafted -- it read 'The operator has the local formal type...' where the operator's "
              "drafted text names the object, 'System C has the local formal type...'. This is exactly "
              "the per-object ambiguity C4 forbids, and 'operator' is overloaded in this repository. "
              "Corrected to 'System C'.", "INSPECTED", "file_inspection", NO, "self"),
    ("R1-51", "RULING 2 APPLIED: the `review` field now defines `cold` per claim type. Proofs: read by "
              "an independent party without the derivation history. Computations: reproduced by an "
              "independent party using DIFFERENT CODE, ideally a different method, without access to "
              "the original script or output; re-executing the original script stays `self`. Every "
              "review value now carries a `review_note` recording the method. Retro-applied across 36 "
              "reviewed claims: 8 cold, 28 self, 0 lacking a review_note. R1-40 (CT-S8's independent "
              "60-dps derivation and verification of K from the Gauss multiplication formula, own "
              "script) was promoted to cold under the new definition.", "INSPECTED", "build", R8,
     "self"),
]

out = D / "claims.jsonl"
with out.open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh, rev in rows:
        rec = {
            "claim_id": cid, "task_id": "CT-R1-AUDIT-R8", "claim": claim, "label": label,
            "evidence_type": ev, "dps": None, "reproducible": True,
            "script": "gate1_locate.py / apply_audit_r8.py", "output_hash": oh,
            "review": rev,
            "review_note": ("self: produced and checked by this session. Gate 1 was specified by the "
                            "operator as a NON-isolated check, so `self` is the correct and intended "
                            "value here, not a shortfall."),
        }
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

print("appended", len(rows), "R8 claims ->", out)
for cid, *_ in rows:
    print(" ", cid)
