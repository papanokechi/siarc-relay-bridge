"""CT-R1-AUDIT round 2: apply the operator's INSPECTED ruling, and record the
Zenodo companion-paper evidence that supersedes three earlier findings.

Two things happen here.

(1) TAXONOMY (operator ruling 1). A new provenance label INSPECTED is adopted:
    "established by direct inspection of named files at a stated commit; valid
    only for that commit." Binding rules:
      (a) any claim with evidence_type 'file_inspection' gets INSPECTED and can
          never be PROVEN;
      (b) absence claims are written "NOT FOUND in <scope> by <method>", never
          "does not exist".

    Applying (a) literally would demote genuine theorems, because several
    mathematical claims were mis-tagged 'file_inspection' merely because their
    proof lives in a .tex file. That is an evidence_type error, not a label
    error. Those claims are retagged evidence_type='proof' and keep their label.
    This is flagged to the operator as a schema consequence of ruling 1.

(2) SUPERSESSION. The companion paper was downloaded from Zenodo this round.
    Conjecture 4.1 DOES exist (v1.2); in v1.0/v1.1 the object numbered 4.1 is a
    Theorem. This supersedes S4-01, S4-08 and R1-05.

Run from sessions/2026-09-17/CT-R1-AUDIT/.
"""
import json, hashlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
BASE = HERE.parent

VALID = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}

# Mathematical claims mis-tagged file_inspection: retag evidence, keep label.
RETAG_PROOF = {
    "S1-01", "S1-02", "S1-03", "S1-04", "S1-05",
    "S3A-02", "S3B-04", "S3B-07",
    "R1-02", "R1-03", "R1-08", "R1-09",
}

# Genuine repository-content claims: become INSPECTED.
TO_INSPECTED = {
    "R1-01", "R1-05", "R1-06", "R1-07",
    "S1-07", "S2-05",
    "S3A-01", "S3A-03", "S3A-04", "S3A-05", "S3A-06",
    "S4-01", "S4-02", "S4-08", "S4-10",
    "S5B-C7",
}

# Absence claims rewritten per rule (b), and findings superseded by the Zenodo pull.
REWRITE = {
    "S2-05":
        "NOT FOUND in sessions/2026-05-01/PCF2-SESSION-Q1/ (whole session folder, at commit "
        "08aa0e2381b3dc37ee54a3200b7272755ca11d59) by case-insensitive recursive text search for "
        "'rho': zero matches, so no stored quantity of that name at d=4 was located. What the "
        "session DOES store is xi_0 = d/beta_d^{1/d} (newton_d4_results.json) and WKB fit "
        "parameters A, alpha, beta, gamma (results.json). P2 task 5's 'check it against stored "
        "values' therefore had no d=4 target. Phrasing corrected per operator ruling 1(b): this "
        "is a NOT FOUND result, not a proof of non-existence.",
    "S3A-06":
        "NOT FOUND in sessions/2026-05-08/T1-OPERATOR-CT-V131-.../channel_theory_outline_v131_"
        "with_r1a_caveat.tex (the newest in-repo Channel Theory source, v1.3.1, at commit "
        "08aa0e2381b3dc37ee54a3200b7272755ca11d59) by text search for 'Proposition 3.3.A': zero "
        "matches. The object that carries the intended statement xi_0 = 2/sqrt(beta_2) is "
        "Conjecture 3.3.A-star, 'Cross-degree universality of xi_0', label prop:xi0 at L502, "
        "proven at d=2. P1's citation 'Proposition 3.3.A' does not match this source; it may "
        "match a version not present in this repo. Phrasing corrected per operator ruling 1(b).",
    "S4-01":
        "SUPERSEDED BY DIRECT EVIDENCE (round R2). Conjecture 4.1 EXISTS. The V_quad companion "
        "was retrieved from Zenodo (concept DOI 10.5281/zenodo.20455089) and placed in "
        "sessions/2026-09-17/CT-R1-AUDIT/refs/. Three versions exist. In v1.0 (version DOI "
        "10.5281/zenodo.20455090, 10 pp) and v1.1 (10.5281/zenodo.20480603, 12 pp) the object "
        "numbered 4.1 is a THEOREM; in v1.2 (10.5281/zenodo.20481592, 12 pp) it is CONJECTURE 4.1, "
        "'Painleve V (D5^(1)) classification'. The operator's hypothesis is therefore CONFIRMED "
        "exactly. The earlier finding arose because the repo's own bibitem{Vquad} cites version "
        "DOI 20455090 = v1.0, and because no copy of the companion was in the repo at all; the "
        "search that produced the finding covered the PERIOD-REP paper, a different document. "
        "Both the original claim and the R1 amendment are withdrawn. Finding S4-F1 is CLOSED.",
    "S4-08":
        "SUPERSEDED (round R2). At the time of CT-S4, P5 step 3 was correctly HALTED because NOT "
        "FOUND in the repository, by filename and full-text search, was any rank-2 Painleve "
        "classification table. That halt was correct under the rules then in force. The operator "
        "has since supplied van der Put & Saito, Ann. Inst. Fourier 59 (2009) no. 7, 2611-2667, "
        "DOI 10.5802/aif.2502; the citation was verified and a copy placed at "
        "sessions/2026-09-17/CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf (sha256 "
        "1666bd6be824a99fc0b48adbe48233a9b2a520fd7e8adf187e98d22525473605). Table 2.1, p. 2635, is "
        "extracted in CLASSIFICATION-TABLE.md. The halt condition is LIFTED.",
    "R1-05":
        "SUPERSEDED BY DIRECT EVIDENCE (round R2), and the conclusion is reversed. R1 concluded "
        "that the companion was absent from the repo so Conjecture 4.1 could be neither confirmed "
        "nor refuted. The paper has now been downloaded from Zenodo and all three versions are in "
        "sessions/2026-09-17/CT-R1-AUDIT/refs/: v1.0 (20455090, sha256 c07c97d6..., 10 pp), v1.1 "
        "(20480603, sha256 e07c1dda..., 12 pp), v1.2 (20481592, sha256 a5d9e264..., 12 pp). "
        "Conjecture 4.1 EXISTS in v1.2; the object numbered 4.1 is a Theorem in v1.0 and v1.1. The "
        "operator's version hypothesis is CONFIRMED. The repo's bibitem{Vquad} cites v1.0, which "
        "is why the label was not found by anyone reading only the cited version. Note also that "
        "the companion's published title differs from the title in the repo's bibliography entry.",
}

NEW = [
    ("R1-12", "R2-companion",
     "The V_quad companion was retrieved from Zenodo concept DOI 10.5281/zenodo.20455089, which "
     "resolves to latest record 20481592. Three versions exist, all with title 'A non-classical "
     "Painleve V transcendent from a quadratic polynomial continued fraction: surface "
     "classification and resurgent Stokes data': v1.0 = 10.5281/zenodo.20455090, 2026-05-30, "
     "538588 bytes, 10 pp, sha256 c07c97d6fcd4d65bb888f951e853c85d21897a55190290fa3e32f38410ff1601; "
     "v1.1 = 10.5281/zenodo.20480603, 2026-06-01, 606008 bytes, 12 pp, sha256 "
     "e07c1ddab16ffe22e2a118a1f8c97f45c9b959148af01933c9a4a50bc2a790a1; v1.2 = "
     "10.5281/zenodo.20481592, 2026-06-01, 612719 bytes, 12 pp, sha256 "
     "a5d9e264699e6397030f0512e17f0cd503fcf2eafd57db9b00b57523fcc88d85. Note the published title "
     "differs from the title used in the repo's bibitem{Vquad}, which also cites the v1.0 version "
     "DOI rather than the concept DOI.",
     "file_inspection", None, "Zenodo REST API + sha256", "", "INSPECTED"),

    ("R1-13", "R2-conj41",
     "Object 4.1 across the three companion versions, by regex search of extracted PDF text with "
     "fi/fl ligatures normalised: v1.0 has 'Theorem 4.1' (3 occurrences) and no Conjecture 4.1; "
     "v1.1 has 'Theorem 4.1' (4 occurrences) and no Conjecture 4.1; v1.2 has 'Conjecture 4.1' "
     "(7 occurrences) and no Theorem 4.1. The only other numbered 4.x object anywhere is Remark 4.5 "
     "in v1.2. This CONFIRMS the operator's hypothesis exactly: the Conjecture 4.1 label appears "
     "only from v1.2, and at v1.0 the object numbered 4.1 is a theorem.",
     "file_inspection", None, "pypdf text extraction + regex", "", "INSPECTED"),

    ("R1-14", "R2-conj41-content",
     "Conjecture 4.1 is about a THIRD ODE, neither System A nor System B. The companion v1.2 "
     "Sec 2.2 derives, by a formal continuum limit of the Wallis recurrence, its equation (6)-(7): "
     "a(x)y'' + b(x)y' + c(x)y = 0 with a(x)=3x^2+x+1, b(x)=6x+1, c(x)=-x^2, satisfying the "
     "exactness identity b(x)=a'(x) so that the operator is d/dx[a(x)y'] + c(x)y = 0. Call this "
     "System C. The companion states its finite singularities are the roots of a(x), namely "
     "s_{1,2} = (-1 +- i sqrt 11)/6, both regular singular and ASSERTED APPARENT, and that x=infinity "
     "is irregular of Poincare rank 1. Conjecture 4.1 asserts the isomonodromic deformation family "
     "containing (6) is governed by Painleve V with alpha=1/6, beta=0, gamma=0, delta=-1/2, with "
     "space of initial conditions the Sakai surface D5^(1) and symmetry W(A3^(1)) = affine S4. "
     "Note s_{1,2} = (-1 +- i sqrt 11)/6 are exactly the points CT-S5B-COVER computed for the "
     "INVERTED System B under z -> 1/x, so System C and the inverted System B are closely related.",
     "file_inspection", None, "companion v1.2 Sec 2.2, Remark 2.1, Sec 4", "", "INSPECTED"),

    ("R1-15", "R2-conj41-caveat",
     "Conjecture 4.1 documents its own principal weakness, quoted verbatim from companion v1.2 "
     "Sec 4: 'the surface-type determination D5^(1) rests on a match against the Jimbo-Miwa-Ueno "
     "classification table [5] and is not yet corroborated by an independent Lax-pair derivation "
     "(see Remark 4.5).' This matters because van der Put & Saito state in their Introduction "
     "(p. 2612) that their work extends Jimbo-Miwa-Ueno precisely by allowing 'all possible "
     "irregular singularities including ramification', which the JMU tables exclude. So the "
     "conjecture's stated evidential basis is a table that cannot see ramification, which is the "
     "very phenomenon at issue in CT-S4. Conjecture 4.1 also argues beta=gamma=0 'reflects the "
     "fact that both finite singularities are apparent', making the apparency computation "
     "delegated to CT-S6-APPARENCY load-bearing for the conjecture itself.",
     "file_inspection", None, "companion v1.2 Sec 4; vdP-Saito p. 2612", "", "INSPECTED"),

    ("R1-16", "R2-taxonomy",
     "Operator ruling 1 adopted: new provenance label INSPECTED, with rule (a) any file_inspection "
     "claim is INSPECTED and never PROVEN, and rule (b) absence claims phrased 'NOT FOUND in "
     "<scope> by <method>'. Applying rule (a) literally would have demoted genuine theorems, "
     "because 12 mathematical claims (S1-01..S1-05, S3A-02, S3B-04, S3B-07, R1-02, R1-03, R1-08, "
     "R1-09) were tagged evidence_type 'file_inspection' merely because the proof text lives in a "
     ".tex or .md file. That is an evidence_type error, not a label error; those are retagged "
     "evidence_type='proof' and keep their labels. 16 genuine repository-content claims were "
     "relabelled INSPECTED. Three absence claims were rephrased per rule (b). SCHEMA QUESTION FOR "
     "THE OPERATOR: 'proof' is a new evidence_type value not in the original "
     "file_inspection|computation|build set, introduced as a direct consequence of ruling 1. "
     "Please confirm or replace it.",
     "computation", None, "apply_audit_r2.py", "", "STRUCTURAL"),
]


def main():
    files = sorted(BASE.glob("CT-*/claims.jsonl"))
    seen, touched = set(), []
    for f in files:
        rows, changed = [], False
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            c = json.loads(line)
            cid = c["claim_id"]
            if cid in RETAG_PROOF:
                c["evidence_type"] = "proof"
                c["audit_r2"] = ("Retagged evidence_type file_inspection -> proof under operator "
                                 "ruling 1: this is a mathematical claim whose proof happens to "
                                 "live in a file, not a claim about repository contents. Label "
                                 "unchanged.")
                seen.add(cid); changed = True
            if cid in TO_INSPECTED:
                if c["label"] != "INSPECTED":
                    c.setdefault("label_before_r2", c["label"])
                c["label"] = "INSPECTED"
                c["audit_r2"] = (c.get("audit_r2", "") + " Relabelled INSPECTED under operator "
                                 "ruling 1(a): established by direct inspection of named files at "
                                 "commit 08aa0e2381b3dc37ee54a3200b7272755ca11d59; valid only for "
                                 "that commit.").strip()
                seen.add(cid); changed = True
            if cid in REWRITE:
                c["claim_before_r2"] = c["claim"]
                c["claim"] = REWRITE[cid]
                seen.add(cid); changed = True
            if changed:
                c["amended_in"] = "CT-R1-AUDIT/R2"
            rows.append(c)
        if changed:
            f.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
            touched.append(str(f.relative_to(BASE)))

    expected = RETAG_PROOF | TO_INSPECTED | set(REWRITE)
    missing = expected - seen
    if missing:
        print("ERROR: not found:", sorted(missing)); sys.exit(1)

    # append the new R2 claims
    own = HERE / "claims.jsonl"
    existing = [json.loads(l) for l in own.read_text(encoding="utf-8").splitlines() if l.strip()]
    have = {c["claim_id"] for c in existing}
    audit = hashlib.sha256((HERE / "AUDIT.md").read_bytes()).hexdigest()
    for cid, tid, claim, ev, dps, script, _oh, label in NEW:
        if cid in have:
            continue
        existing.append({"claim_id": cid, "task_id": tid, "claim": claim,
                         "evidence_type": ev, "dps": dps, "reproducible": True,
                         "script": script, "output_hash": audit, "label": label})
    own.write_text("\n".join(json.dumps(c) for c in existing) + "\n", encoding="utf-8")

    counts, total = {}, 0
    for f in sorted(BASE.glob("CT-*/claims.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                c = json.loads(line)
                assert c["label"] in VALID, (f, c["claim_id"], c["label"])
                assert not (c["evidence_type"] == "file_inspection"
                            and c["label"] == "PROVEN"), f"rule 1(a) violated: {c['claim_id']}"
                counts[c["label"]] = counts.get(c["label"], 0) + 1
                total += 1

    print("amended files:")
    for t in touched:
        print("  ", t)
    print(f"\nretagged to evidence_type=proof : {len(RETAG_PROOF)}")
    print(f"relabelled INSPECTED            : {len(TO_INSPECTED)}")
    print(f"absence/superseded rewrites     : {len(REWRITE)}")
    print(f"new R2 claims appended          : {len(NEW)}")
    print(f"\ncorpus total: {total}")
    for k in sorted(counts):
        print(f"  {k:12} {counts[k]}")
    print("\nrule 1(a) invariant holds: no file_inspection claim is PROVEN.")


if __name__ == "__main__":
    main()
