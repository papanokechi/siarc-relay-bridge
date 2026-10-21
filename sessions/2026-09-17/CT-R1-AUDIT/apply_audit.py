"""CT-R1-AUDIT: apply operator-review label amendments to earlier sessions' claims.jsonl.

Every amendment records `label_before` and `amended_in` so the change is auditable.
Run from sessions/2026-09-17/.
"""
import json, hashlib, pathlib, sys

BASE = pathlib.Path(__file__).resolve().parent.parent

# claim_id -> (new_label or None to keep, reason, optional new claim text suffix)
AMEND = {
    # ---- CT-S1-THEOREM ----
    "S1-03": (None,
        "AUDIT R1: label PROVEN UPHELD, but only after repair. The first draft of "
        "thm:radius Step 3 asserted without proof that the balanced multinomial "
        "coefficient is the largest; that assertion is load-bearing (it is what turns "
        "'at least the average' into the lower bound d^{dn}/(dn+1)^{d-1}). A proof by "
        "the exchange argument k_i/(k_j+1) > 1 was added to theorem.tex in R1. "
        "Not machine-checked: the Lean file still has 7 sorry."),
    "S1-04": ("PROVEN",
        "AUDIT R1: UPGRADED STRUCTURAL -> PROVEN. Gap G1 was closed in theorem.tex. "
        "Step 3 now proves from Gamma(x+1)=x Gamma(x) alone that "
        "h(n)=Gamma(n+1-r)n^r/Gamma(n+1) satisfies h(n)/h(n-1)=1+O(1/n^2), hence "
        "h(n)=h_inf(1+O(1/n)) with h_inf finite and nonzero. The sole imported "
        "ingredient is the constant h_inf=1, cited precisely to DLMF (5.11.12), "
        "Sec 5.11(iii), where G_0(a,b)=1. Citation of a classical result, not a gap."),

    # ---- CT-S2-RHO-D4 ----
    "S2-05": ("STRUCTURAL",
        "AUDIT R1: DOWNGRADED PROVEN -> STRUCTURAL. This is a NEGATIVE search result "
        "(a case-insensitive grep returning zero matches). A null grep is only as good "
        "as its search terms and cannot be a proof of absence. Reclassified for "
        "consistency with the other file_inspection claims in this corpus."),

    # ---- CT-S3A-ZETA-AUDIT ----
    "S3A-03": ("STRUCTURAL",
        "AUDIT R1: DOWNGRADED PROVEN -> STRUCTURAL. Evidence type is file_inspection: "
        "reading and interpreting a source comment. Accurate, but interpretation of a "
        "self-contradictory comment is not a proof. Now consistent with S4-01/S4-02, "
        "which carry STRUCTURAL on identical evidence type."),
    "S3A-06": ("STRUCTURAL",
        "AUDIT R1: DOWNGRADED PROVEN -> STRUCTURAL. Evidence type is file_inspection. "
        "Same reasoning as S3A-03."),

    # ---- CT-S3B-RINF ----
    "S3B-01": (None,
        "AUDIT R1: label PROVEN UPHELD. The content is a rigorous elementary estimate, "
        "not a numerical observation: for b(n)=3n^2+n+1 the tail terms are ~1/(9k^4), "
        "so the tail sum is ~1/(27N^3); setting 1/(27N^3)=1e-3000 gives N~10^999.5. "
        "Exact arithmetic throughout."),
    "S3B-03": (None,
        "AUDIT R1: label PROVEN UPHELD. disc(3n^2+n+1) = 1-12 = -11 < 0, so both roots "
        "are non-real and in particular no root is a positive integer. Complete proof."),

    # ---- CT-S4-FORMAL-TYPE ----
    "S4-01": ("STRUCTURAL",
        "AUDIT R1: CLAIM SCOPE CORRECTED; the original wording overstated the finding. "
        "The search actually covered sessions/2026-06-15/VQUAD-PERIODREP-PAPER-001, "
        "which is the PERIOD-REP paper, NOT the V_quad companion. The companion is a "
        "DISTINCT document, cited as bibitem{Vquad} ('The V_quad polynomial continued "
        "fraction: a Painleve-V standalone closure on the Sakai surface D5^(1)', Zenodo, "
        "version DOI 10.5281/zenodo.20455090), and a repo-wide search finds it ONLY as "
        "bibliography title strings -- no copy of the companion exists in this repo at "
        "ANY version. Therefore 'Conjecture 4.1 does not exist' is RETRACTED as a "
        "citation defect and restated as: the companion paper is absent from the repo, "
        "so Conjecture 4.1 can be neither confirmed nor refuted here. The operator's "
        "v1.0/v1.1 hypothesis is NOT confirmed either -- there is no copy to inspect."),
    "S4-03": (None,
        "AUDIT R1: label PROVEN UPHELD, with the basis restated. The proof is the "
        "SYMBOLIC derivation [1 - z*b(theta+1) - z^2] f = 1 with theta = z d/dz, which "
        "is exact and holds at all orders. The vanishing residual at z^0..z^38 against "
        "the exact integer sequence is CORROBORATION, not the proof; a finite check "
        "alone would not warrant PROVEN."),
    "S4-04": (None,
        "AUDIT R1: label PROVEN UPHELD. Two exact CAS identity verifications of a "
        "transcription; exact arithmetic, no tolerance."),
    "S4-05": (None,
        "AUDIT R1: label PROVEN UPHELD, with a dependency named. The pole orders are "
        "computed in exact arithmetic (integers, no tolerance). The step from pole order "
        "to {ramified, Katz invariant} uses the STANDARD classification of second-order "
        "formal singularities, which is cited, not proved in session."),
    "S4-06": (None, "AUDIT R1: label PROVEN UPHELD. Same basis and same cited "
        "classification dependency as S4-05."),
    "S4-07": (None, "AUDIT R1: label PROVEN UPHELD. Action values read off the exact "
        "normal forms; exact arithmetic."),
}


def main():
    files = sorted(BASE.glob("CT-*/claims.jsonl"))
    touched, seen = [], set()
    for f in files:
        rows, changed = [], False
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            c = json.loads(line)
            cid = c["claim_id"]
            if cid in AMEND:
                seen.add(cid)
                new_label, note = AMEND[cid]
                c["audit_r1"] = note
                c["amended_in"] = "CT-R1-AUDIT"
                if new_label and new_label != c["label"]:
                    c["label_before"] = c["label"]
                    c["label"] = new_label
                changed = True
            rows.append(c)
        if changed:
            f.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
            touched.append(str(f.relative_to(BASE)))

    missing = set(AMEND) - seen
    if missing:
        print("ERROR: claim ids not found:", sorted(missing))
        sys.exit(1)

    # recount labels across the whole corpus
    counts, total = {}, 0
    for f in sorted(BASE.glob("CT-*/claims.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                c = json.loads(line)
                assert "label" in c, f"missing label in {f}: {c['claim_id']}"
                counts[c["label"]] = counts.get(c["label"], 0) + 1
                total += 1

    print("amended files:")
    for t in touched:
        print("  ", t)
    print(f"\namended claims: {len(seen)}")
    print(f"corpus total  : {total}")
    for k in sorted(counts):
        print(f"  {k:12} {counts[k]}")
    h = hashlib.sha256()
    for f in sorted(BASE.glob("CT-*/claims.jsonl")):
        h.update(f.read_bytes())
    print("\ncorpus sha256:", h.hexdigest())


if __name__ == "__main__":
    main()
