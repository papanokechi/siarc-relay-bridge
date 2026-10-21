"""Append claims S27-22..S27-27: the sixth item and the renumber.

Pre-write validation only; nothing reaches disk until the whole buffer passes.
`output_hash` is read from disk, never carried in a variable.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESSION = HERE.parent
LEDGER = SESSION / "claims.jsonl"
TASK = "CT-S27-CTV17-DEPOSIT-PREP/sixth-item"

NOTICE = SESSION / "NOTICE-v1.7-rev2.md"
DESC = SESSION / "DESCRIPTION-v1.7-rev2.html"
OUT = SESSION / "outputs"

VALID = {"PROVEN", "VERIFIED", "STRUCTURAL", "CONJECTURED", "INSPECTED"}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


CLAIMS = [
    ("S27-22",
     "THE NOTICE SOURCE WAS COPIED FORWARD RATHER THAN EDITED IN PLACE. NOTICE-v1.7.md "
     "belongs to the earlier session CT-S26-CTV17-DRAFT, which P0 forbids modifying. It "
     "was copied byte-identically to NOTICE-v1.7-rev2.md in this session (source sha256 "
     "a0bb2b84...), all subsequent edits were made to the copy, and make_description.py's "
     "NOTICE constant was repointed. The CT-S26 original is unchanged.",
     "INSPECTED", OUT / "renumber_notice.out.txt", "scripts/renumber_notice.py"),

    ("S27-23",
     "THE SECTION RENUMBER WAS DRIVEN BY AN ENUMERATED LIST WITH A CONTROL, NOT BY A "
     "REGEX. Inserting a new section 7 required 7,8,9 -> 8,9,10, but the token 'section 9' "
     "in this notice denotes three different documents: this notice's own sources table "
     "(1 occurrence), section 9 of the v1.6 deposited record (7 occurrences), and section "
     "9 of Birkhoff-Trjitzinsky 1933 p. 69 (2 occurrences); 'section 8' also denotes the "
     "v1.4 EBR deposit's scope statement. A blind renumber would have rewritten "
     "references to other people's documents and still looked well-formed. The script "
     "rewrites three headings in descending order and exactly four self-references, each "
     "required to fire exactly once, and asserts that all seven references to other "
     "documents are untouched. All eleven assertions passed.",
     "INSPECTED", OUT / "renumber_notice.out.txt", "scripts/renumber_notice.py"),

    ("S27-24",
     "THE SIXTH ITEM IS PUBLISHED IN THREE TIERS WITH THE EXCLUSION SEPARATED FROM THE "
     "REACHABLE SET. Section 7 states: the exclusion of the D5-tilde/PV row for deg b = 2 "
     "and deg a in {0,1,2}, VERIFIED and obtained twice independently; the reachable set "
     "PIII(D8), PIII(D7), PIII(D6), STRUCTURAL, also obtained independently; and the "
     "coefficient dependence with its codimension-3 exceptional locus, STRUCTURAL and "
     "explicitly NOT independently confirmed, with the disclosure that it came from a "
     "derivation which corrected an earlier error of its own. The three tiers are not "
     "merged and the weakest is named as weakest.",
     "INSPECTED", NOTICE, "scripts/make_description.py"),

    ("S27-25",
     "THE SIXTH ITEM DOES NOT MERGE THE GENERATING-FUNCTION OPERATOR WITH THE V_quad "
     "PAINLEVE IDENTIFICATION. Section 7.0 names the object as the operator annihilating "
     "the generating function of the denominators, states that op:cc-stokes-closed-form "
     "concerns the CC-channel connection-coefficient ratio against a Riemann-Hilbert "
     "datum, and records that the two have NOT been shown to coincide. Section 7.4 and "
     "the closing caveats state that the exclusion is therefore not evidence about the "
     "conjectural identification in either direction. This is the one-name-two-objects "
     "prohibition applied at the level of objects rather than constants; the notice "
     "neither strengthens nor disputes the record's own Painleve label.",
     "INSPECTED", NOTICE, "scripts/verify_description.py"),

    ("S27-26",
     "A SEVENTEENTH GATE CHECK, N5, WAS ADDED AND IS TWO-SIDED. A presence-only check "
     "would pass a section 7 that said all the right things and then added one sentence "
     "refuting the V_quad identification or calling a row match VERIFIED. N5 therefore "
     "requires five features AND rejects sentences that refute an identification or that "
     "attach VERIFIED/PROVEN to a family-membership verb. Its two load-bearing mutants "
     "are drawn from those two failure modes rather than from its own required-string "
     "list, per Amendment E; the third is an ordinary deletion mutant for the presence "
     "half. All three were rejected. verify_description.py now runs 17 checks, 0 failed, "
     "0 broken, with the three reader-integrity controls still firing.",
     "INSPECTED", OUT / "verify_description_r7.out.txt", "scripts/verify_description.py"),

    ("S27-27",
     "THE DEPOSIT PACKET IS GREEN AGAIN AT THE NEW HASH, AND THE STALE HASH WAS CAUGHT BY "
     "THE GATE RATHER THAN BY INSPECTION. Regenerating the description changed it from "
     "54068 to 63123 characters; preflight check S2 failed immediately, naming the "
     "declared hash as pointing at nothing. Nine sites across DEPOSIT-FORM.md and "
     "WALKTHROUGH.md were updated in one validated pass which also corrected the "
     "paste-completeness stop point from section 9 to section 10 and the size ratio from "
     "2.3x to 2.7x. Both files are CRLF and the line endings were preserved by "
     "normalising once after decoding. preflight_deposit_rev2.py then returned GATE: "
     "PASSED, 11 checks, 0 failed, 0 broken. Publishing remains operator-gated.",
     "INSPECTED", OUT / "preflight_deposit_r3.out.txt", "scripts/preflight_deposit_rev2.py"),
]


def main():
    existing = [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
    seen = {c["claim_id"] for c in existing}
    print("ledger holds %d claims, last %s" % (len(existing), existing[-1]["claim_id"]))

    buf = []
    for cid, text, label, artefact, script in CLAIMS:
        assert cid not in seen, "duplicate claim id %s" % cid
        assert label in VALID
        assert artefact.exists(), "artefact missing: %s" % artefact
        buf.append({
            "claim_id": cid,
            "task_id": TASK,
            "claim": text,
            "label": label,
            "evidence_type": "file_inspection",
            "dps": None,
            "reproducible": True,
            "script": script,
            "output_hash": sha(artefact),
        })
        seen.add(cid)

    lines = [json.dumps(r, ensure_ascii=True) for r in buf]
    for ln, r in zip(lines, buf):
        assert json.loads(ln) == r
        assert "\n" not in ln
        assert len(r["output_hash"]) == 64
        assert r["label"] not in r["claim"], "%s duplicates its label in prose" % r["claim_id"]
    print("pre-write validation passed: %s" % ", ".join(r["claim_id"] for r in buf))

    with LEDGER.open("a", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    after = [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(after) == len(existing) + len(buf)
    print("ledger now holds %d claims, last %s" % (len(after), after[-1]["claim_id"]))
    for r in buf:
        print("  %-8s %-10s %s..." % (r["claim_id"], r["label"], r["claim"][:60]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
