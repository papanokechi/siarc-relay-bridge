"""Emit claims.jsonl for CT-R1-AUDIT with sha256 hashes of the referenced outputs."""
import json, hashlib, pathlib

HERE = pathlib.Path(__file__).resolve().parent


def sha(name):
    p = HERE / name
    if not p.exists():
        raise FileNotFoundError(p)
    return hashlib.sha256(p.read_bytes()).hexdigest()


AUDIT = sha("AUDIT.md")
TABLE = sha("CLASSIFICATION-TABLE.md")
LOG = sha("apply_audit.log")
PDF = sha("refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf")

CLAIMS = [
    ("R1-01", "R1-hygiene",
     "The .gitignore covering the 6.5 GB lean/.lake/ tree sits INSIDE the session folder, at "
     "sessions/2026-09-17/CT-S1-THEOREM/lean/.gitignore, not at the repo root. git status "
     "--porcelain --untracked-files=all reports exactly one .gitignore path, that one, as "
     "untracked; git diff on the repo-root .gitignore is empty. No unintended repo change.",
     "file_inspection", None, "git status / git diff", AUDIT, "STRUCTURAL"),

    ("R1-02", "R1-proof-audit",
     "AUDIT FINDING, now repaired. theorem.tex Theorem thm:radius Step 3 asserted without proof "
     "that the balanced multinomial coefficient (dn)!/(n!)^d is the largest over compositions of "
     "dn into d parts. The assertion is LOAD-BEARING: the lower bound d^{dn}/(dn+1)^{d-1} is "
     "obtained as max >= average and fails without maximality. A complete proof was added by the "
     "exchange argument: if k_i >= k_j+2, moving one unit from part i to part j multiplies the "
     "coefficient by k_i/(k_j+1) >= (k_j+2)/(k_j+1) > 1, so any maximiser over the finite set of "
     "compositions has |k_i-k_j| <= 1, which with sum k_i = dn forces all k_i = n. Steps 1,2,4,5 "
     "were checked and are correct as written; no Stirling or Gamma asymptotics appears anywhere "
     "in part (i), as the prompt required.",
     "file_inspection", None, "theorem.tex (thm:radius, Step 3 sub-lemma)", AUDIT, "PROVEN"),

    ("R1-03", "R1-gap-G1",
     "Gap G1 closed. With h(n) := Gamma(n+1-r) n^r / Gamma(n+1), the identity Gamma(x+1)=x Gamma(x) "
     "alone gives h(n)/h(n-1) = (1 - r/n)(1 - 1/n)^(-r) = 1 + O(1/n^2); since sum O(1/n^2) converges, "
     "the telescoping product converges to a finite nonzero h_inf, and the tail of a convergent "
     "sum O(1/m^2) is O(1/n), so h(n) = h_inf (1 + O(1/n)). The entire O(1/n) error bookkeeping is "
     "therefore self-contained. The sole imported ingredient is the constant h_inf = 1, cited to "
     "DLMF (5.11.12), Sec 5.11(iii) 'Ratios', where G_0(a,b) = 1, with a = 1-r, b = 1, z = n. The "
     "equation number and statement were verified against dlmf.nist.gov/5.11 directly, not from "
     "memory. Claim S1-04 is upgraded STRUCTURAL -> PROVEN modulo that named citation.",
     "file_inspection", None, "theorem.tex (thm:growth, Step 3)", AUDIT, "PROVEN"),

    ("R1-04", "R1-labels",
     "Label amendments applied by apply_audit.py across five claims.jsonl files, 13 claims amended. "
     "Downgraded PROVEN -> STRUCTURAL: S2-05 (a negative grep result cannot prove absence), S3A-03 "
     "and S3A-06 (file_inspection, and partly negative results). Upgraded STRUCTURAL -> PROVEN: "
     "S1-04 (Gap G1 closed). Upheld with basis restated: S1-01, S1-02, S1-03, S3B-01, S3B-03, "
     "S4-03, S4-04, S4-05, S4-06, S4-07. Each amended row carries audit_r1, amended_in, and where "
     "the label moved, label_before. Corpus after R1: 47 claims, 16 PROVEN, 21 STRUCTURAL, "
     "10 VERIFIED; every row parses and carries exactly one label.",
     "computation", None, "apply_audit.py", LOG, "STRUCTURAL"),

    ("R1-05", "R1-companion-version",
     "The 'Conjecture 4.1 does not exist' finding is RETRACTED as a citation defect and restated as "
     "missing data. What CT-S4 searched was sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001, the "
     "PERIOD-REP paper, not the V_quad companion. The companion is a distinct document, cited as "
     "bibitem{Vquad} in sections/section-9-references.md L6-11 ('The V_quad polynomial continued "
     "fraction: a Painleve-V standalone closure on the Sakai surface D5^(1)', Zenodo, version DOI "
     "10.5281/zenodo.20455090, concept 10.5281/zenodo.20455089). A repo-wide search for its title "
     "string returns ONLY citing occurrences: bibliography entries, LaTeX preambles, and outline "
     "mentions. No copy of the companion exists in this repo at ANY version, so Conjecture 4.1 can "
     "be neither confirmed nor refuted here. The operator's v1.0/v1.1 hypothesis is likewise NOT "
     "confirmed: there is no copy to inspect. The only companion version number visible anywhere is "
     "the v1.2 inside the bibitem{StokesNote} citation string, which is a citation, not a copy. "
     "Finding S4-F1 stands as a pure missing-data finding.",
     "file_inspection", None, "repo-wide title-string search", AUDIT, "STRUCTURAL"),

    ("R1-06", "R1-citation",
     "The operator-supplied classification citation is VERIFIED against the publisher and a copy is "
     "in the session folder. Marius van der Put and Masa-Hiko Saito, 'Moduli spaces for linear "
     "differential equations and the Painleve equations', Annales de l'Institut Fourier, Tome 59, "
     "no. 7 (2009), pp. 2611-2667, DOI 10.5802/aif.2502, open access via Centre Mersenne. File "
     "refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf, 1058380 bytes, 58 pages, title page matching the "
     "stated volume/issue/pages. It is the correct source: the Introduction states the paper "
     "constructs the ten rank-two isomonodromic families and explicitly allows 'all possible "
     "irregular singularities including ramification', which Jimbo-Miwa-Ueno's tables exclude. "
     "Caveat for re-searchers: the PDF uses the fi ligature, so grep for 'ramified' returns zero "
     "hits; search 'rami'.",
     "file_inspection", None, "publisher metadata + PDF title page", PDF, "STRUCTURAL"),

    ("R1-07", "R1-table",
     "Table 2.1 'Classification of Families' (p. 2635) extracted verbatim into "
     "CLASSIFICATION-TABLE.md, together with the selection rule on p. 2634. The paper identifies "
     "the ten families by their Katz-invariant multiset, not by number. The D5-tilde / PV row is "
     "(r(0), r(1), r(infinity), r(t)) = (0, 0, 1, -) with dim P = 3: two regular singular points and "
     "one irregular point of Katz invariant 1, hence UNRAMIFIED. This confirms from a verified "
     "primary source the premise that P5 was given and that CT-S4 had to take on trust. P5 step 3's "
     "halt condition is lifted.",
     "file_inspection", None, "CLASSIFICATION-TABLE.md", TABLE, "STRUCTURAL"),

    ("R1-08", "R1-table-match",
     "Matching CT-S4 and CT-S5B-COVER outputs against Table 2.1. System A (the f = Sum Q_n z^n ODE "
     "for b(n)=3n^2+n+1) has ramified Katz 1/2 at z=0, ramified Katz 1/2 at z=infinity, and no other "
     "singular point, so its Katz multiset is (1/2, -, 1/2), which is the D8-tilde row, PIII(D8). "
     "Its pullback along z=w^2 has unramified Katz 1 at w=0 and at infinity, multiset (1, -, 1), "
     "which is the D6-tilde row, PIII(D6). Both matches are exact and mutually consistent, since a "
     "quadratic cover is the classical relation between PIII(D8) and PIII(D6). NEITHER is D5-tilde / "
     "PV. Because the Katz multiset is an invariant of the family, no change of variable moves "
     "between rows.",
     "file_inspection", None, "CLASSIFICATION-TABLE.md", TABLE, "STRUCTURAL"),

    ("R1-09", "R1-table-match",
     "System B (L_phi) taken at face value has one irregular Katz-1 point at z=0 plus THREE regular "
     "singular points (rho_pm = (-1 +- i sqrt 11)/2 and z=infinity), which is not a row of Table "
     "2.1, since the table admits #S=4 only when all r(p)=0. If exactly one of those three is an "
     "APPARENT singularity, and so carries no moduli and is not counted, the effective multiset "
     "becomes (0, 0, 1), which is the D5-tilde / PV row. VQ-N1 records apparent indices [0,0]. "
     "Neither CT-S5B-COVER nor this session recomputed the apparency of rho_pm or of infinity, so "
     "the D5-tilde match for System B is not established.",
     "file_inspection", None, "CLASSIFICATION-TABLE.md", TABLE, "CONJECTURED"),

    ("R1-10", "R1-p5b-review",
     "CT-S5B-COVER's two central computations were re-derived independently by hand and confirmed. "
     "The normal-form pullback rule R = (phi')^2 r(phi) - (1/2) Schwarzian(phi) follows from "
     "v'' - (phi''/phi') v' - (phi')^2 r(phi) v = 0 together with the standard reduction "
     "R = a^2/4 + a'/2 - b. For phi = w^2, Schwarzian = -3/(2w^2), giving correction +3/(4w^2), and "
     "R(w) = 4w^2 r_A(w^2) + 3/(4w^2) = (-48w^4 - 53w^2 + 48)/(36w^4); the numerator at w=0 is 48, "
     "nonzero, so the pole order is 4, even, hence unramified with Katz 1. At infinity the potential "
     "is (48t^4 - 80t^2 - 48)/(36t^4), numerator -48 at t=0, pole order 4, Katz 1. For phi = 1/x the "
     "Schwarzian vanishes and R(x) = r_B(1/x)/x^4 = (12x^4+4x^3+4x^2+11)/(4(3x^2+x+1)^2), with roots "
     "(-1 +- i sqrt 11)/6 and R(0) = 11/4 finite so x=0 is ordinary. Every value matches the agent's "
     "output exactly. Separately, S5B-C2 is labelled STRUCTURAL but is arguably PROVEN; the "
     "conservative label was left in place.",
     "computation", None, "hand re-derivation, recorded in AUDIT.md section 5", AUDIT, "PROVEN"),

    ("R1-11", "R1-build",
     "theorem.tex recompiles after the R1 repairs with pdflatex: a final pass reports NO undefined "
     "references and NO undefined citations, and writes theorem.pdf at 7 pages, 343115 bytes "
     "(previously 6 pages). A thebibliography block with the DLMF entry was added to resolve the "
     "new citation.",
     "build", None, "pdflatex theorem.tex", AUDIT, "VERIFIED"),
]


def main():
    out = HERE / "claims.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        for cid, tid, claim, ev, dps, script, oh, label in CLAIMS:
            fh.write(json.dumps({
                "claim_id": cid, "task_id": tid, "claim": claim,
                "evidence_type": ev, "dps": dps, "reproducible": True,
                "script": script, "output_hash": oh, "label": label,
            }) + "\n")
    print(f"wrote {len(CLAIMS)} claims -> {out}")
    counts = {}
    for _, _, _, _, _, _, _, lab in CLAIMS:
        counts[lab] = counts.get(lab, 0) + 1
    for k in sorted(counts):
        print(f"  {k:12} {counts[k]}")


if __name__ == "__main__":
    main()
