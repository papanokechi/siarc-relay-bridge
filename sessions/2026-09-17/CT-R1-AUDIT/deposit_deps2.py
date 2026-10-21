"""Pass 2 of the deposit dependency audit.

Pass 1 flagged 26 supporting claims as neither `cold` nor INSPECTED. That is too
blunt. A cold session's OWN claims are marked `self` -- correctly, since a
session cannot cold-read itself -- yet those very claims ARE the independent
reproduction that makes the parent claim `cold`. A supporting claim therefore
clears the gate in any of four ways:

  A  it is itself `cold`;
  B  it is INSPECTED (a fact about a file or page, read at a stated hash);
  C  it IS part of a cold session's output, i.e. it is the independent work;
  D  it was independently recomputed by a cold session (named explicitly).

Anything left over is a genuine gap and is reported as one.
"""
import json, glob, os
from pathlib import Path

ROOT = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17")
COLD_SESSIONS = {"CT-S7-COLDREAD", "CT-S10-COLDREAD2", "CT-S11-COLDREAD3",
                 "CT-S12-COLDREAD4", "CT-S13-COLDREAD5"}

# D: supporting claim -> (cold session, the specific claim_id it was recomputed against).
# The claim_id is recorded so the link can be re-checked later, not just asserted.
CORROBORATED = {
    "S4-05":  ("CT-S13-COLDREAD5", ["A1", "A2-A3"], "recomputed System A's normal form and both Katz invariants"),
    "S5B-C4": ("CT-S13-COLDREAD5", ["A5-formal"], "recomputed the z=w^2 pullback"),
    "S5B-C5": ("CT-S13-COLDREAD5", ["A5-formal"], "recomputed the z=w^2 pullback"),
    "S6-C9":  ("CT-S13-COLDREAD5", ["A4-table"], "read the four ordered columns of Table 2.1 and confirmed the dash slot"),
    "S6-C10": ("CT-S13-COLDREAD5", ["A6"], "reached the same necessary-not-sufficient conclusion independently"),
    "S6-C13": ("CT-S11-COLDREAD3", ["step-4-log", "c-independence"], "proved the general lemma forcing exponents [0,0] at every simple root of chi"),
    "S6-C14": ("CT-S11-COLDREAD3", ["step-4-log", "c-independence"], "as S6-C13"),
    "S6-C17": ("CT-S11-COLDREAD3", ["sympy-examples"], "independent symbolic examples of the same lemma"),
    "R1-30":  ("CT-S12-COLDREAD4", ["CT-S12-COLDREAD4-Q3-C4C5"], "re-derived the System C parameter values in its own script"),
    "R1-65":  ("CT-S12-COLDREAD4", ["CT-S12-COLDREAD4-Q1-DICT"], "inputs page-image verified; the arithmetic step is 1-0-0"),
    "R1-34":  ("CT-S12-COLDREAD4", ["CT-S12-COLDREAD4-Q3-C4C5"], "superseded and re-derived in C2 from the same page-image-verified dictionary"),
    "S4-06":  ("CT-S14-COLDREAD-B", ["c01", "c02", "c03"], "recomputed object B's singular points, Katz invariants and the (0,0,1) tuple in its own code, from the printed normal form alone"),
    "S5B-C6": ("CT-S14-COLDREAD-B", ["c05", "c06", "c09", "c11"], "independently established the inversion identity, the twist and the Table 2.1 row for object B"),
    # R1-56 and CT-S9-PVPARAMS-C014 are cleared by route A (their own `review: cold`
    # field, set after CT-S15-COLDREAD-DEFERRED). No CORROBORATED entry is added for
    # them: route A takes precedence, so the claim_ids named here would never be
    # link-checked, and naming unverified ids in the record is exactly what the P0
    # rule forbids.
}

DEPS = {
    "C1 - Remark 2.2 is false (the lemma)": ["R1-18", "R1-43", "step-4-log", "c-independence",
                                             "sympy-examples", "S6-C13", "S6-C14", "S6-C17"],
    "C2 - the PV parameter contradiction": ["R1-65", "R1-64", "R1-31", "R1-32", "R1-29", "R1-30",
                                            "R1-34", "CT-S12-COLDREAD4-Q1-DICT",
                                            "CT-S12-COLDREAD4-Q1-EIGEN", "CT-S12-COLDREAD4-Q3-C4C5",
                                            "CT-S12-COLDREAD4-Q4-C6", "CT-S9-PVPARAMS-C003"],
    "C3 - not well-posed as isomonodromy": ["R1-33", "CT-S12-COLDREAD4-Q5-C7", "CT-S9-PVPARAMS-C014"],
    "C4 - per-object surface labels": ["R1-52", "R1-53", "R1-54", "R1-55", "R1-56", "R1-57",
                                       "R1-06", "R1-07", "S4-05", "S4-06", "S5B-C4", "S5B-C5",
                                       "S5B-C6", "S6-C9", "S6-C10", "A4-table", "A5-table"],
    "C5 - downstream passages in v1.2": ["R1-66", "R1-63"],
}

rec = {}
for f in glob.glob(str(ROOT / "*" / "claims.jsonl")):
    sess = os.path.basename(os.path.dirname(f))
    for l in open(f, encoding="utf-8"):
        if l.strip():
            r = json.loads(l)
            rec[r["claim_id"]] = (sess, r)

out, gaps = [], []
for item, ids in DEPS.items():
    out.append("\n### " + item + "\n")
    out.append("| Claim | Session | Label | Route | Basis |")
    out.append("|---|---|---|---|---|")
    for cid in ids:
        sess, r = rec[cid]
        lab = r.get("label")
        if r.get("review") == "cold":
            route, basis = "**A — cold**", r.get("review_note", "")[:110]
        elif sess in COLD_SESSIONS:
            route, basis = "**C — is the cold work**", f"produced by {sess}, the independent session"
        elif lab == "INSPECTED":
            route, basis = "**B — INSPECTED**", "fact about a named file/page at a stated hash"
        elif cid in CORROBORATED:
            sess_c, against, why = CORROBORATED[cid]
            # Verify the named corroborating claim_ids actually exist, so route D
            # cannot be asserted against a claim that is not in the record.
            bad = [a for a in against if a not in rec]
            link = ", ".join(f"`{a}`" for a in against)
            if bad:
                route, basis = "**BROKEN LINK**", f"named claims not in corpus: {bad}"
                gaps.append((item, cid, lab, sess))
            else:
                route = "**D — corroborated**"
                basis = f"{sess_c} {link} — {why}"
        else:
            route, basis = "**GAP**", "no independent check"
            gaps.append((item, cid, lab, sess))
        out.append(f"| `{cid}` | {sess} | {lab} | {route} | {basis} |")

Path(ROOT / "CT-R1-AUDIT" / "_deps_table.md").write_text("\n".join(out), encoding="utf-8")
print("\n".join(out[-1:]))
print("\n=== GAPS:", len(gaps))
for item, cid, lab, sess in gaps:
    print(f"   {cid:12} {lab:12} {sess:22} [{item}]")
