"""Emit the revision-3 claims for CT-S24-PAPER-OUTLINE.

Ordering is deliberate and follows the rule this round proposes as P0
Amendment B: *a claim's hash must be taken after the artefact is final.*

There is a genuine ordering constraint here. verify_outline.py resolves cited
claim ids against the corpus, so it cannot pass until the new claims exist; but
the new claims must carry the hash of that checker's output. The resolution is
three phases, not a guess:

  phase 1  append the new claims with output_hash = null
  phase 2  run the checker to its FINAL output path and hash the file on disk
  phase 3  write that hash into the new claims, then read back and assert

Phase 2 writes to a NEW filename (verify_outline_rev3.out.txt). The revision-2
output is left untouched, so the eleven existing claims that cite its hash keep
resolving. That is the defect from revision 2 being structurally avoided rather
than remembered.
"""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
CLAIMS = SESSION / "claims.jsonl"
OUT_REV3 = SESSION / "outputs" / "verify_outline_rev3.out.txt"
OUT_ODLYZKO = SESSION / "outputs" / "verify_odlyzko_p77.out.txt"

NEW_IDS = ["S24-12", "S24-13", "S24-14", "S24-15"]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


CLAIMS_REV3 = [
    {
        "claim_id": "S24-12",
        "task_id": "CT-S24-PAPER-OUTLINE/attribution",
        "claim": (
            "The Odlyzko p. 77 citation, blocked at revision 2, is CLEARED. It was "
            "re-obtained from the author's own site as Asymptotic Enumeration Methods "
            "(192 pages, sha256 d0b58928e580ab355a6a6805846f023d5a89ebffe9fb966048beb28c1da67bff) "
            "and verified from a rendered page image, not from the session record that "
            "first reported it. The printed folio 77 sits at PDF index 76, an offset of "
            "-1, resolved by locating the folio in the header/footer band rather than by "
            "trusting the index. The page carries verbatim: 'so determines the asymptotics "
            "of a_n up to a multiplicative constant. However, the Birkhoff-Trjitzinsky "
            "method does not in general provide any techniques for determining that "
            "constant.' Checker scripts/verify_odlyzko_p77.py passes 5 of 5 controls, of "
            "which three are negative: a fabricated near-miss fragment occurs nowhere in "
            "the document, the quoted fragments do not occur on a decoy page, and an "
            "impossible folio does not resolve. Nemes arXiv:2508.15246v2 is RETAINED "
            "alongside Odlyzko rather than replaced by it, giving two independent sources "
            "for one statement. NOTE ON THE REVISION-2 FINDING: the repo-wide zero-occurrence "
            "result was correct and the conclusion drawn from it was not. The citation "
            "originated in CT-S22-DEPENDENCE-LIT, whose record was stored outside the "
            "worktree and whose downloaded PDFs were deleted at session close, so absence "
            "from the worktree was the expected observation and not evidence of an "
            "unsourced citation."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/verify_odlyzko_p77.py",
        "output_hash": None,
    },
    {
        "claim_id": "S24-13",
        "task_id": "CT-S24-PAPER-OUTLINE/attribution",
        "claim": (
            "TWO REFINEMENTS forced by reading the page image, which the intermediate "
            "session record had compressed, both of which must survive into the paper. "
            "(i) THE ATTRIBUTION SPLITS. The 'up to a multiplicative constant' half is "
            "Odlyzko reporting Wimp and Zeilberger, reference [384] on that page: 'Wimp "
            "and Zeilberger point out that it is usually easy to show that the largest of "
            "the terms of the form (9.35) does show up with a nonzero coefficient, and so "
            "determines the asymptotics of a_n up to a multiplicative constant.' Only the "
            "following sentence, that the method provides no technique for the constant, "
            "is Odlyzko's own assertion. Citing the whole passage to Odlyzko would "
            "misattribute the first half to him. (ii) THE SAME PAGE OBJECTS TO "
            "BIRKHOFF-TRJITZINSKY: 'The major objection to the use of the "
            "Birkhoff-Trjitzinsky results is that they may not be rigorous, since gaps are "
            "alleged to exist in the complicated proofs.' A referee who checks p. 77 reads "
            "this too. It does not bite, because nothing in the paper rests on "
            "Birkhoff-Trjitzinsky: the growth rate is Perron-Kreuser via Gautschi, the "
            "exponent s is derived directly, and B-T is cited only for the provenance of "
            "the normal-solution shape. The paper must say so in the same breath as the "
            "B-T citation rather than in a later section."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/verify_odlyzko_p77.py",
        "output_hash": None,
    },
    {
        "claim_id": "S24-14",
        "task_id": "CT-S24-PAPER-OUTLINE/structure",
        "claim": (
            "The cut Borel material's destination is now NAMED as Channel Theory v1.7, "
            "replacing revision 2's 'v1.7 or a short note of its own'. The stated reason is "
            "the same test the cut section failed for the paper: in v1.7 the material "
            "connects by argument rather than by object, because zeta* and "
            "op:cc-median-resurgence-execute already live in that document. Two things v1.7 "
            "can then do that no other destination can: restate "
            "op:cc-median-resurgence-execute with the zeta* = 2 xi_0 finding, which changes "
            "what that open problem asks; and record the Stage-5B NOT FOUND against its "
            "stated search space, a negative being meaningful only against a stated space. "
            "v1.7 therefore carries five items: the Perron-Kreuser attribution, the "
            "exponent, K through r_infinity, the vacuity explanation, and the Borel and "
            "S_zeta* material with its restated open problem. A TRANSIT MANIFEST was added "
            "to OUTLINE.md section 3.4 for the two items flagged as liable to be lost in "
            "transit, both of which are method rather than result and neither of which is "
            "carried by any claim id that travels automatically: the PSLQ basis-ellipsis "
            "repair, which must print the basis in full, together with the S22-21 "
            "degeneracy that an elided basis concealed; and the xi_0 / zeta* naming "
            "prohibition, K being the amplitude at xi_0 and S_zeta* at the action difference "
            "2 xi_0. The paper's open questions are confirmed at TWO, the z-dependent gauge "
            "and the scope limits on membership."
        ),
        "label": "STRUCTURAL",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/verify_outline.py",
        "output_hash": None,
    },
    {
        "claim_id": "S24-15",
        "task_id": "CT-S24-PAPER-OUTLINE/governance",
        "claim": (
            "A second proposed P0 amendment was APPENDED to "
            "CT-S22-STOKES/P0-AMENDMENT.md as Amendment B, artefact hashing and checker "
            "re-runs, leaving Amendment A unaltered. Status PROPOSED and operator-gated; P0 "
            "is pasted per-session and has no canonical file, so this document remains the "
            "place a future session pastes from. The gap it closes: P0's AEAL RECORD line "
            "fixes WHAT must be hashed and is silent on WHEN, permitting a hash to be taken "
            "while its target is still moving, and it treats the checker as standing outside "
            "the system it checks when in fact re-running a checker invalidates every hash "
            "pointing at its output. Evidence: claims S24-01 through S24-07 carried "
            "output_hash a3bab67a for outputs/verify_outline.out.txt until a Tee-Object "
            "redirect overwrote that file, whose new content hashed fe5657ba, leaving seven "
            "hashes resolving to nothing and the revision-1 output unrecoverable. Caught on "
            "read-back; check_invariants.py has no visibility into whether a hash still "
            "resolves. The revision-3 run avoids the defect structurally rather than by "
            "memory, writing the checker to the new path verify_outline_rev3.out.txt so that "
            "the eleven existing claims citing fe5657ba continue to resolve."
        ),
        "label": "INSPECTED",
        "evidence_type": "file_inspection",
        "dps": None,
        "reproducible": True,
        "script": "scripts/emit_claims_rev3.py",
        "output_hash": None,
    },
]


def load():
    rows = []
    for line in CLAIMS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write(rows):
    with open(CLAIMS, "w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=True) + "\n")


def main() -> int:
    rows = load()
    existing = {r["claim_id"] for r in rows}
    print(f"claims.jsonl before: {len(rows)} rows")

    # ---- phase 1: append with a null hash ------------------------------
    for c in CLAIMS_REV3:
        if c["claim_id"] in existing:
            print(f"  {c['claim_id']}: already present, refusing to duplicate")
            return 2
        rows.append(c)
    write(rows)
    print(f"phase 1: appended {len(CLAIMS_REV3)} claims with output_hash = null")

    # ---- phase 2: run the checker to its FINAL path, then hash ---------
    print(f"phase 2: running verify_outline.py -> {OUT_REV3.name}")
    with open(OUT_REV3, "w", encoding="utf-8") as fh:
        rc = subprocess.run(
            [sys.executable, str(HERE / "verify_outline.py")],
            stdout=fh, stderr=subprocess.STDOUT, cwd=str(SESSION),
        ).returncode
    tail = OUT_REV3.read_text(encoding="utf-8").strip().splitlines()[-1]
    print(f"         checker exit {rc}; last line: {tail}")
    if rc != 0:
        print("FAIL: checker still reports defects; hashes NOT written")
        return 1

    h_outline = sha256(OUT_REV3)
    h_odlyzko = sha256(OUT_ODLYZKO)
    print(f"         {OUT_REV3.name} sha256 {h_outline}")
    print(f"         {OUT_ODLYZKO.name} sha256 {h_odlyzko}")

    # ---- phase 3: write hashes, then read back and assert --------------
    rows = load()
    for r in rows:
        if r["claim_id"] in ("S24-12", "S24-13"):
            r["output_hash"] = h_odlyzko
        elif r["claim_id"] in ("S24-14", "S24-15"):
            r["output_hash"] = h_outline
    write(rows)

    back = {r["claim_id"]: r for r in load()}
    bad = [i for i in NEW_IDS if not back.get(i, {}).get("output_hash")]
    assert not bad, f"read-back: claims still carrying a null hash: {bad}"
    assert back["S24-12"]["output_hash"] == h_odlyzko
    assert back["S24-14"]["output_hash"] == h_outline

    # the revision-2 artefact must still exist and still hash as cited
    old = SESSION / "outputs" / "verify_outline.out.txt"
    old_h = sha256(old)
    cited = {r["output_hash"] for r in load() if r["claim_id"] <= "S24-11"}
    print(f"phase 3: revision-2 artefact {old.name} sha256 {old_h}")
    assert old_h in cited, "the revision-2 output no longer matches what its claims cite"
    print("         revision-2 hash still resolves for the earlier claims: OK")

    print(f"claims.jsonl after: {len(back)} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
