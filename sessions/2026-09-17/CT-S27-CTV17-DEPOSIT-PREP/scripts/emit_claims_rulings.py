"""Record the operator rulings of 2026-09-19: Amendment E adopted, C extended.

A ruling is a fact about the governance record, so it is INSPECTED, not
VERIFIED: the evidence is the amendment files as they now stand, read back from
disk after they were final.

S27-15 is NOT edited.  It said Amendment E was PROPOSED and not adopted, which
was true when written.  The corpus supersedes rather than rewrites, so the
change of status is a new claim that names the old one.
"""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
CLAIMS = os.path.join(SESSION, "claims.jsonl")
LABELS = {"PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"}

# The ruling is a statement about these two files, so they are the evidence.
EVIDENCE = ["P0-AMENDMENT-E.md", "P0-AMENDMENTS-ABCD.md"]

REQUIRED = {
    "P0-AMENDMENT-E.md": [
        "**Status: ADOPTED, 2026-09-19, by operator ruling.**",
        "MUTANT PROVENANCE",
        "P0 amendment backlog: zero",
    ],
    "P0-AMENDMENTS-ABCD.md": [
        "The requirement is SYMMETRIC",
        "mutant provenance",
        "ADOPTED",
    ],
}

CLAIM = dict(
    claim_id="S27-21",
    label="INSPECTED",
    claim=(
        "P0 AMENDMENT E (MUTANT PROVENANCE) IS ADOPTED, AND AMENDMENT C IS "
        "EXTENDED WITH A SYMMETRY CLAUSE, BY OPERATOR RULING OF 2026-09-19. "
        "E was proposed and ruled on in the same round, on two live instances: "
        "X2's string list, and P1 without P2. The ruling identifies the second "
        "as the sharper case, since P1 alone is satisfied by deleting the "
        "citations it protects, placing it in the same class as a search space "
        "with no target in it (Amendment A). C's new bullet states that a "
        "reader which INVENTS a defect fails identically to one which misses "
        "it, and is worse if acted on; its occasion was S27-19. This claim "
        "SUPERSEDES the status recorded in S27-15, which said E was PROPOSED "
        "and not adopted; S27-15 was true when written and is not edited. "
        "P0 amendment backlog: zero."),
    evidence_type="file_inspection",
    script="scripts/emit_claims_rulings.py",
)


def main():
    assert CLAIM["label"] in LABELS
    head = CLAIM["claim"].split(".")[0]
    assert not any(head.startswith(lab) for lab in LABELS), (
        "the label belongs in the 'label' field, not as a text prefix")

    # Amendment C's clause: assert a KNOWN-PRESENT feature of each file,
    # including a non-ASCII one, before concluding anything from the contents.
    digests = []
    for name in EVIDENCE:
        path = os.path.join(SESSION, name)
        raw = open(path, "rb").read()
        text = raw.decode("utf-8").replace("\r\n", "\n")
        assert "\u2014" in text, "%s: no em dash -- decoded with the wrong codec?" % name
        for frag in REQUIRED[name]:
            assert frag in text, "%s: required text absent: %r" % (name, frag)
        digests.append((name, hashlib.sha256(raw).hexdigest(), len(raw)))
        print("  read %-24s %8d B  %s" % (name, len(raw), digests[-1][1][:16]))

    # Amendment E: the ruled files must not merely contain the word 'ADOPTED';
    # E's own status line must say so, and the stale 'PROPOSED, not adopted'
    # heading must be gone.  A check for the presence of 'ADOPTED' alone would
    # have passed on the file before it was edited.
    e_text = io.open(os.path.join(SESSION, "P0-AMENDMENT-E.md"),
                     encoding="utf-8").read()
    assert "PROPOSED, not adopted" not in e_text, (
        "P0-AMENDMENT-E.md still carries its PROPOSED heading")
    print("  negative control: the stale 'PROPOSED, not adopted' heading is gone")

    existing = set()
    with io.open(CLAIMS, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                existing.add(json.loads(line)["claim_id"])
    assert "S27-15" in existing, "the superseded claim must exist to be named"
    if CLAIM["claim_id"] in existing:
        print("  skip %s (already present)" % CLAIM["claim_id"])
        return

    # The output hash is over the two ruled files, concatenated in a fixed
    # order, taken from disk AFTER they are final (Amendment B).
    h = hashlib.sha256()
    for name, digest, _ in digests:
        h.update(("%s %s\n" % (name, digest)).encode("utf-8"))

    rec = {
        "claim_id": CLAIM["claim_id"],
        "task_id": "CT-S27-CTV17-DEPOSIT-PREP/rulings",
        "claim": CLAIM["claim"],
        "label": CLAIM["label"],
        "evidence_type": CLAIM["evidence_type"],
        "dps": None,
        "reproducible": True,
        "script": CLAIM["script"],
        "output_hash": h.hexdigest(),
        "supersedes": "S27-15 (status only)",
    }
    with io.open(CLAIMS, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print("appended %s  output_hash %s" % (rec["claim_id"], rec["output_hash"][:16]))

    with io.open(CLAIMS, encoding="utf-8") as fh:
        total = sum(1 for line in fh if line.strip())
    print("claims.jsonl now holds %d claim(s)" % total)


if __name__ == "__main__":
    main()
