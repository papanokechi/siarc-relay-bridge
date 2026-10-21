"""Emit the revision-5 claims for CT-S24-PAPER-OUTLINE.

Same three-phase ordering as emit_claims_rev3/rev4 (P0 Amendment B: a claim's
hash is taken after the artefact is final, and re-running a checker invalidates
every hash pointing at its output).

Phase 2 writes to a NEW filename, verify_outline_rev5.out.txt. The revision-1,
-3 and -4 artefacts are asserted to resolve before the write and to be
byte-unchanged after it.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
CLAIMS = SESSION / "claims.jsonl"
PRIOR = [
    SESSION / "outputs" / "verify_outline.out.txt",
    SESSION / "outputs" / "verify_outline_rev3.out.txt",
    SESSION / "outputs" / "verify_outline_rev4.out.txt",
]
OUT_REV5 = SESSION / "outputs" / "verify_outline_rev5.out.txt"

NEW_IDS = ["S24-20", "S24-21"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


CLAIMS_REV5 = [
    {
        "claim_id": "S24-20",
        "task_id": "CT-S24-PAPER-OUTLINE/structure",
        "claim": (
            "THE METHOD PARAGRAPH MISDESCRIBED ITS OWN PROOF, and is corrected at revision 5. "
            "OUTLINE.md section 1 paragraph 2 read 'Growth is obtained from a "
            "Pincherle/minimal-solution argument'. CT-S1-THEOREM/theorem.tex does not work that "
            "way, verified by reading it: prop:exists obtains convergence of "
            "r_n = Q_n / prod_{k<=n} b(k) UNCONDITIONALLY under (A1), by absolute summability of "
            "the increments and telescoping (theorem.tex lines 109-111, 'the telescoping series "
            "... converges absolutely', COMPLETE, claim S1-01 PROVEN); prop:positive obtains "
            "r_infinity >= 1 > 0 from strict monotonicity of r_n together with that convergence "
            "(lines 123-136, COMPLETE, claim S1-02 PROVEN); and rem:pincherle is labelled "
            "STRUCTURAL and ends, verbatim, 'nothing below depends on this remark' (lines "
            "153-155; the gap table at line 416 repeats 'interpretive only'). The paragraph "
            "therefore credited the result to an argument the paper deliberately does NOT rest "
            "on. This matters beyond accuracy: the Odlyzko p. 77 page objects to "
            "Birkhoff-Trjitzinsky as possibly non-rigorous (S24-13), and section 2.0 is written "
            "to pre-empt that by stating nothing rests on it, so a method paragraph led by "
            "Pincherle invites precisely the question section 2.0 exists to close. THREE EDITS: "
            "the sentence is replaced by the elementary-argument statement with 'Pincherle's "
            "theorem supplies the minimal-solution interpretation but is not used'; a guard is "
            "added to section 2.0 item 1 warning that the Perron-Kreuser-plus-Pincherle "
            "attribution paragraph must not migrate into the method statement, since the paper's "
            "own (H) comes from prop:positive; and section 2's claim line, which listed S1-05 "
            "flat beside four PROVEN propositions, now labels it STRUCTURAL and interpretive."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/verify_outline.py",
        "output_hash": None,
    },
    {
        "claim_id": "S24-21",
        "task_id": "CT-S24-PAPER-OUTLINE/structure",
        "claim": (
            "TWO SMALLER REPAIRS AT REVISION 5. (a) THE TWO-SIDED BOUND IS NOT AN EXISTING "
            "RESULT. The corrected method paragraph says positivity of b supplies r_infinity != 0 "
            "'together with a two-sided bound', but prop:positive proves the LOWER bound "
            "r_infinity >= 1 only; a search of the tex sources for an upper bound of the form "
            "r_infinity <= exp(sum ...) returns nothing. It is therefore recorded in section 2 as "
            "an UNFOLDED DRAFTING ADDITION CARRYING NO CLAIM ID, with its one-line proof sketched "
            "(r_n = r_{n-1} + r_{n-2}/(b(n-1)b(n)) and r_{n-2} <= r_{n-1} give "
            "r_n <= r_{n-1} exp(1/(b(n-1)b(n))), the sum converging since deg b >= 1), and with "
            "the instruction to prove it at drafting and emit a claim, or else weaken the "
            "paragraph to the one-sided statement. The outline states explicitly that it must NOT "
            "be written citing S1-02. (b) A STALE CROSS-REFERENCE: section 5 item N2 directed the "
            "uniqueness question to 'section 11', which ceased to exist at revision 2 when the "
            "Borel section was cut and the sections renumbered, old 10 -> 9 and old 11 -> 10. "
            "Corrected to section 10, with the renumbering noted inline so the correction is "
            "self-explaining. A sweep of all remaining section 9, 10 and 11 references in "
            "OUTLINE.md found no other stale instance; the one surviving 'section 9' that is not "
            "about the cut is Birkhoff-Trjitzinsky's own Fundamental Theorem section 9 p. 69."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/verify_outline.py",
        "output_hash": None,
    },
]


def load():
    return [json.loads(l) for l in CLAIMS.read_text(encoding="utf-8").splitlines() if l.strip()]


def write(rows):
    with open(CLAIMS, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=True) + "\n")


def main() -> int:
    rows = load()
    existing = {r["claim_id"] for r in rows}
    print(f"claims.jsonl before: {len(rows)} rows")

    cited = {r["output_hash"] for r in rows if r.get("output_hash")}
    before = {}
    for p in PRIOR:
        before[p] = sha256(p)
        assert before[p] in cited, f"{p.name} already fails to resolve"
        print(f"pre-check: {p.name} {before[p][:8]} resolves")

    for c in CLAIMS_REV5:
        if c["claim_id"] in existing:
            print(f"  {c['claim_id']}: already present, refusing to duplicate")
            return 2
        rows.append(c)
    write(rows)
    print(f"phase 1: appended {len(CLAIMS_REV5)} claims with output_hash = null")

    print(f"phase 2: running verify_outline.py -> {OUT_REV5.name}")
    with open(OUT_REV5, "w", encoding="utf-8") as fh:
        rc = subprocess.run(
            [sys.executable, str(HERE / "verify_outline.py")],
            stdout=fh, stderr=subprocess.STDOUT, cwd=str(SESSION),
        ).returncode
    tail = OUT_REV5.read_text(encoding="utf-8").strip().splitlines()[-1]
    print(f"         checker exit {rc}; last line: {tail}")
    if rc != 0:
        print("FAIL: checker reports defects; hashes NOT written")
        return 1

    h5 = sha256(OUT_REV5)
    print(f"         {OUT_REV5.name} sha256 {h5}")

    rows = load()
    for r in rows:
        if r["claim_id"] in NEW_IDS:
            r["output_hash"] = h5
    write(rows)

    back = {r["claim_id"]: r for r in load()}
    for i in NEW_IDS:
        assert back[i]["output_hash"] == h5, f"{i} carries the wrong hash"

    cited_after = {r["output_hash"] for r in load() if r.get("output_hash")}
    for p in PRIOR:
        assert sha256(p) == before[p], f"{p.name} was modified"
        assert before[p] in cited_after, f"{p.name} no longer resolves"
    print("phase 3: all three prior artefacts unchanged and still resolve: OK")

    print(f"claims.jsonl after: {len(back)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
