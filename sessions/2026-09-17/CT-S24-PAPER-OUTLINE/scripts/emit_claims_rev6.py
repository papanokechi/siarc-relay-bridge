"""Emit the revision-5 claims for CT-S24-PAPER-OUTLINE.

Same three-phase ordering as emit_claims_rev3/rev4/rev5 (P0 Amendment B: a claim's
hash is taken after the artefact is final, and re-running a checker invalidates
every hash pointing at its output).

Phase 2 writes to a NEW filename, verify_outline_rev6.out.txt. The revision-1,
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
    SESSION / "outputs" / "verify_outline_rev5.out.txt",
]
OUT_rev6 = SESSION / "outputs" / "verify_outline_rev6.out.txt"

NEW_IDS = ["S24-22"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


CLAIMS_rev6 = [
    {
        "claim_id": "S24-22",
        "task_id": "CT-S24-PAPER-OUTLINE/structure",
        "claim": (
            "REVISION 6: THE OUTLINE'S LAST OPEN ITEM IS CLOSED, AND THE PRE-DECLARED FALLBACK "
            "WAS NOT TAKEN. At revision 5 the upper bound r_infinity <= exp(sum_{k>=1} "
            "1/(b(k)b(k+1))) was recorded in section 2 as an UNFOLDED DRAFTING ADDITION CARRYING "
            "NO CLAIM ID (S24-21(a)), with the standing instruction to prove it at drafting or "
            "else weaken section 1 paragraph 2 to the one-sided statement. It is now PROVED as "
            "Proposition U in CT-S26-UPPER-BOUND/PROOF.md (claim S26-01, PROVEN), under (A1) "
            "together with b(n) > 0 for every n >= 1, so the phrase 'two-sided bound' in section "
            "1 paragraph 2 stands unweakened. FOUR THINGS TRAVEL WITH IT INTO SECTION 2, and the "
            "section-2 box is rewritten to carry all four. (i) The positivity hypothesis is "
            "LOAD-BEARING and must be stated rather than inherited from context: three of six "
            "sign-changing b violate the inequality outright, one of them because r_n becomes "
            "non-positive (S26-04). (ii) The upper half must NOT be written citing S1-02, which "
            "supplies the monotonicity step and the lower bound only; it carries S26-01. (iii) "
            "The proof uses no minimal-solution, Pincherle or Perron-Kreuser input at any step, "
            "so section 2.0's undertaking that nothing rests on Birkhoff-Trjitzinsky extends to "
            "it unchanged -- which is the same concern that produced the revision-5 correction "
            "to the method paragraph. (iv) The insertion of the proposition into "
            "CT-S1-THEOREM/theorem.tex after prop:positive, about fifteen lines, is a DRAFTING "
            "ACTION AND IS NOT DONE: theorem.tex belongs to an earlier session and this corpus "
            "does not edit earlier sessions, so the LaTeX source of record still carries the "
            "one-sided statement only. ALSO RECORDED, and relevant to section 2.0's "
            "drafting-discipline note: CT-S26's own known-answer control FIRED, because the "
            "Bessel closed form registered in its PREREG was wrong by an index shift (S26-05). "
            "The PREREG was left unedited and the correction written as a separate addendum. A "
            "known-answer test is only as good as the known answer, and a wrong control that had "
            "happened to agree would have certified a broken engine."
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

    for c in CLAIMS_rev6:
        if c["claim_id"] in existing:
            print(f"  {c['claim_id']}: already present, refusing to duplicate")
            return 2
        rows.append(c)
    write(rows)
    print(f"phase 1: appended {len(CLAIMS_rev6)} claims with output_hash = null")

    print(f"phase 2: running verify_outline.py -> {OUT_rev6.name}")
    with open(OUT_rev6, "w", encoding="utf-8") as fh:
        rc = subprocess.run(
            [sys.executable, str(HERE / "verify_outline.py")],
            stdout=fh, stderr=subprocess.STDOUT, cwd=str(SESSION),
        ).returncode
    tail = OUT_rev6.read_text(encoding="utf-8").strip().splitlines()[-1]
    print(f"         checker exit {rc}; last line: {tail}")
    if rc != 0:
        print("FAIL: checker reports defects; hashes NOT written")
        return 1

    h5 = sha256(OUT_rev6)
    print(f"         {OUT_rev6.name} sha256 {h5}")

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
