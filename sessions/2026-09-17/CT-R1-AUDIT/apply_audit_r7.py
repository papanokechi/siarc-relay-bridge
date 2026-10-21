"""CT-R1-AUDIT R7: record the two cold reads (CT-S11, CT-S12), the Wong-Li
citation verification, and the deposit route change."""
import hashlib
import json
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
S = ROOT / "CT-R1-AUDIT"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


h_a = sha(ROOT / "CT-S11-COLDREAD3" / "verify_examples.out")
h_b = sha(ROOT / "CT-S12-COLDREAD4" / "compute_pv_checks.out")
h_bib = sha(S / "refs" / "dlmf_bib_W.html")

# ---- promote the cold-read claims -----------------------------------------
UPD = {
    "R1-18": ("cold",
              "Cold-read SOUND by CT-S11-COLDREAD3 from a self-contained packet with no access to the "
              "derivation history. The cold reader also IMPROVED the proof: instead of appealing generically "
              "to Frobenius theory for the log term, it gave the explicit reduction-of-order argument. Since "
              "p = chi'/chi, exp(-int p) = 1/chi, so the second solution is y2 = y1 * int dx/(chi*y1^2), whose "
              "integrand has a simple pole at s with residue 1/(h(s)*y1(s)^2) != 0. This exhibits the log "
              "coefficient EXPLICITLY and nonzero, closing the only soft step. Confirmed by hand. It also "
              "confirmed that dropping c(s) != 0 is legitimate and that the phrase 'assume s is a genuine "
              "singular point' does no hidden work, since p is singular at any simple root of chi regardless "
              "of c."),
    "R1-31": ("cold",
              "Cold-read SOUND by CT-S12-COLDREAD4, which re-derived the PV rescaling law from the Painleve V "
              "equation by direct symbolic substitution rather than taking it on trust -- the single "
              "load-bearing step. It confirmed (alpha,beta,gamma,delta) -> (alpha,beta,c*gamma,c^2*delta) for "
              "W(z)=w(cz), AND checked the opposite convention, where it reads (alpha,beta,gamma/c,delta/c^2). "
              "The conclusion holds under either: fixing delta = -1/2 forces c^2 = 1, so gamma = 1 cannot be "
              "rescaled to gamma = 0."),
    "R1-32": ("cold",
              "Independently rediscovered by CT-S12-COLDREAD4 directly from the Jimbo page image, without "
              "being told to look for it: the page states the standing assumption (A1)_PV 'theta_0, theta_t "
              "not in Z', which the case theta_0 = theta_t = 0 violates. Two independent parties have now "
              "found this on the page. CT-S9-PVPARAMS, which produced the original result, missed it."),
    "R1-33": ("cold",
              "Cold-read SOUND WITH CAVEAT by CT-S12-COLDREAD4. It confirmed that k = 2/sqrt(3) is forced by "
              "Jimbo's normalisation at infinity and that t = -/+ 2i*sqrt(33)/9 follows, so the operator is a "
              "single normalised fibre. CAVEAT, independently raised and matching the flag already on this "
              "claim: the identification of the two finite singular points with Jimbo's 0 and t is an "
              "ASSUMPTION, legitimate for placing a two-finite-singularity one-irregular-singularity problem "
              "into Jimbo's normalisation but not proved by the scalar equation alone. The conclusion is "
              "conditional on it."),
}
for fn in ROOT.glob("*/claims.jsonl"):
    rows = [json.loads(l) for l in fn.read_text(encoding="utf-8").splitlines() if l.strip()]
    ch = False
    for r in rows:
        if r["claim_id"] in UPD:
            rev, note = UPD[r["claim_id"]]
            r["review"] = rev
            r["audit_r7"] = note
            ch = True
            print("promoted", r["claim_id"], "->", rev)
    if ch:
        fn.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")

NEW = [
    ("R1-43",
     "Cold read A (CT-S11-COLDREAD3) returns SOUND on the Remark 2.2 lemma, and strengthens it. Its explicit "
     "reduction-of-order argument gives the logarithm's coefficient as 1/(h(s) y1(s)^2), manifestly nonzero, "
     "replacing the packet's generic appeal to Frobenius theory. Verified by hand: with p = chi'/chi, "
     "exp(-int p dx) = 1/chi, so the reduction-of-order integrand is 1/(chi y1^2), which has a simple pole at "
     "any simple root s of chi. This is now the recommended form of the proof.",
     "PROVEN", "proof", h_a, "cold"),
    ("R1-44",
     "Cold read B (CT-S12-COLDREAD4) returns SOUND WITH CAVEAT on the PV parameter contradiction. The two "
     "caveats are (a) the published tuple (1/6,0,0,-1/2) was unsourced IN THE PACKET -- an artefact of cold-read "
     "design, since the packet deliberately withheld the companion paper to preserve isolation; the tuple is "
     "sourced in the repo -- and (b) the (A1)_PV violation, which was already recorded as R1-32. Neither "
     "caveat is a new defect.",
     "INSPECTED", "file_inspection", h_b, None),
    ("R1-45",
     "DLMF bibliography verified 2026-09-17 at https://dlmf.nist.gov/bib/W: 'Wong and Li (1992a)' is "
     "'Asymptotic expansions for second-order linear difference equations. II', Stud. Appl. Math. 87(4) "
     "289-324, and it is the entry cited for eq. (2.9.14) -- our case. 'Wong and Li (1992b)' is J. Comput. "
     "Appl. Math. 41(1-2) 65-94, cited for the bounded-coefficient case, which is NOT ours. CT-S8-LITCHECK's "
     "identification is CONFIRMED. The suffix ordering is counterintuitive -- '1992a' is the paper titled "
     "'II' -- so any access request must quote the full citation, not the DLMF key.",
     "INSPECTED", "file_inspection", h_bib, None),
    ("R1-46",
     "Wong & Li (1992a) was NOT OBTAINED. The Wiley copy is paywalled; no mirror or shadow library was used. "
     "The DOI for the companion paper Wong & Li (1992b) resolves to a ScienceDirect stub reporting "
     "accessType anon_guest, which is not evidence of open access and is in any case the wrong paper. "
     "Access requires operator action: Wiley single-article purchase, National Diet Library or university "
     "visitor access to Stud. Appl. Math. 1992 holdings, or an author request.",
     "INSPECTED", "file_inspection", None, None),
    ("R1-47",
     "Deposit route CHANGED by operator review #4: the standalone note is DROPPED. The residual contribution "
     "after gate 3 is too thin to carry a note -- K is a routine product-of-Gammas computation given the "
     "growth law, its substance sits in r_inf which has no closed form (PSLQ null), and in the "
     "Birkhoff-Trjitzinsky / Wong-Li framework the constant multiplying the dominant solution is exactly the "
     "undetermined connection constant; the Borel framing and the vacuity explanation are expository. The "
     "material goes into Channel Theory v1.7 as a correction-and-attribution notice instead, which also "
     "removes the Wong-Li blocker, since a version notice can state plainly that the question was not "
     "determined whereas a note claiming a contribution could not.",
     "INSPECTED", "file_inspection", None, None),
    ("R1-48",
     "Two notice drafts prepared for the operator, neither applied to any source file: "
     "DRAFT-CT-v1.7-NOTICE.md (items N1-N4: attribution of Conjecture 3.3.A* to Perron-Kreuser plus "
     "Pincherle and retirement of the conjecture label; supersession of the EBR positivity grounding; K and "
     "the r_inf series; the one-line vacuity explanation) and DRAFT-COMPANION-v1.3-NOTICE.md (items C1-C4: "
     "the Remark 2.2 lemma; the refuted derivation and the genuine parameter contradiction; the "
     "well-posedness restatement of Conjecture 4.1; the per-object label table). Passages whose wording "
     "depends on Wong & Li are marked [WONG-LI] with two alternative phrasings each.",
     "INSPECTED", "file_inspection", None, None),
    ("R1-49",
     "Citation hygiene adopted as a standing P0 rule (P0-CITATION-RULE.md): re-fetch and hash every external "
     "citation at deposit time; read rendered page images rather than OCR for any load-bearing statement; the "
     "rule covers HYPOTHESES as well as theorem statements; never use a mirror or shadow library for a "
     "paywalled source. Evidence base: four citation-level defects in this run, none in any mathematical "
     "argument, one of which (the Gautschi (2.8) OCR artefact, in a hypothesis) would have flipped the "
     "prior-art conclusion.",
     "INSPECTED", "file_inspection", None, None),
]
with (S / "claims.jsonl").open("a", encoding="utf-8") as f:
    for cid, claim, label, ev, oh, rev in NEW:
        rec = {"claim_id": cid, "task_id": "CT-R1-AUDIT-R7", "claim": claim, "label": label,
               "evidence_type": ev, "dps": None, "reproducible": True,
               "script": "sessions/2026-09-17/CT-R1-AUDIT/coldpackets/", "output_hash": oh}
        if rev:
            rec["review"] = rev
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

import collections
lab, rev, bad = collections.Counter(), collections.Counter(), []
for p in ROOT.glob("*/claims.jsonl"):
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        lab[r.get("label")] += 1
        if r.get("evidence_type") == "proof":
            rev[r.get("review")] += 1
        if r.get("evidence_type") == "file_inspection" and r.get("label") == "PROVEN":
            bad.append(r["claim_id"])
print("hashes:", h_a[:16], h_b[:16], h_bib[:16])
print("corpus:", sum(lab.values()), dict(lab))
print("proof review:", dict(rev))
print("rule 1(a) violations:", bad or "none")
