#!/usr/bin/env python3
"""CT-S54 claim emitter.

Every figure is resolved to the single summary line that reports it in
outputs/method_b_independence.out.txt -- never by searching the file for a
digit string, which can match a line number (CT-S44 finding S44-17).

Validates the in-memory buffer BEFORE writing; a post-write assertion would
leave a corrupt artefact on disk.

Exit: 0 wrote, 2 refused.
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SESS = HERE.parent
OUT = SESS / "outputs" / "method_b_independence.out.txt"
CLAIMS = SESS / "claims.jsonl"

TASK = "CT-S54-METHOD-B-INDEPENDENCE"


def refuse(msg):
    print("REFUSED:", msg)
    print("Nothing was written to claims.jsonl.")
    sys.exit(2)


def anchor(text, pattern, what):
    """Return the single line matching pattern, or refuse."""
    hits = [ln for ln in text.splitlines() if re.search(pattern, ln)]
    if len(hits) != 1:
        refuse(f"anchor for {what} matched {len(hits)} lines, expected exactly 1 "
               f"(pattern {pattern!r})")
    return hits[0]


def figure(line, what):
    m = re.search(r"([0-9]+\.[0-9]+e[+-][0-9]+)", line)
    if not m:
        refuse(f"no figure found on the {what} line: {line!r}")
    return m.group(1)


def main():
    if not OUT.exists():
        refuse(f"{OUT} does not exist; run method_b_independence.py first")
    text = OUT.read_text(encoding="utf-8")
    ohash = hashlib.sha256(OUT.read_bytes()).hexdigest()

    o1 = figure(anchor(text, r"^\s*O1 relB\s", "O1"), "O1")
    o2 = figure(anchor(text, r"^\s*O2 relC1\s", "O2"), "O2")
    o3 = figure(anchor(text, r"^\s*O3 relC2\s", "O3"), "O3")
    gap = figure(anchor(text, r"^\s*\|O1 - O2\|", "|O1-O2|"), "|O1-O2|")
    o4 = figure(anchor(text, r"^\s*O4 relB_indep", "O4"), "O4")

    l_p1 = anchor(text, r"^\s*P1: ", "P1")
    l_a0 = anchor(text, r"^\s*O3 relative move", "A0 control")
    l_same = anchor(text, r"^\s*O1 and O2 moved by the same amount", "same-move")
    l_stream = anchor(text, r"Method B block references a Borel coefficient stream",
                      "stream")
    l_p4 = anchor(text, r"^\s*P4: ", "P4")

    if not l_p1.strip().endswith("True"):
        refuse("P1 is not True; the central claim does not hold and must not be written")
    if not l_same.strip().endswith("True"):
        refuse("O1 and O2 did not move by the same amount; F1 territory")
    if not l_stream.strip().endswith("False"):
        refuse("the Method B block does appear to reference a Borel coefficient "
               "stream; claim S54-04 would be false")
    if not l_p4.strip().endswith("True"):
        refuse("P4 is not True; O4 does not differ from O1")
    if "0.0" not in l_a0:
        refuse(f"A0 control line does not show an exactly zero move: {l_a0!r}")
    if o1 != o2:
        refuse(f"O1 ({o1}) and O2 ({o2}) differ as printed; the identity claim fails")

    claims = [
        {
            "claim_id": "S54-01",
            "claim": (
                "Method B's reported relative error and Method C's first reported "
                f"relative error are the same quantity: both are {o1}, and they agree "
                f"to {gap} at dps 120. The factor e^-xi0 cancels, leaving |2piK - S|/S "
                "in both cases."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 120,
        },
        {
            "claim_id": "S54-02",
            "claim": (
                "Method B as printed in eq. (26) and as implemented in the cited script "
                "stage4_methods.py takes its branch amplitude from the Stokes datum "
                "(A = K*Gamma(1+beta), K = S/2pi). Perturbing S alone by a relative "
                "1e-30 moves Method B's figure and Method C's figure by an identical "
                "relative amount, while the independent observable C = |A|/|beta| does "
                "not move at all."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 120,
        },
        {
            "claim_id": "S54-03",
            "claim": (
                "The manuscript's statement that 'Method B is independent of the Stokes "
                "datum: it derives S e^-xi0 ... rather than assuming S' (sub:methodB), "
                "and Table 2's row giving Method B as independent of the Stokes datum, "
                "are overclaims with respect to the derivation as printed and the "
                "computation as cited."
            ),
            "label": "STRUCTURAL",
            "evidence_type": "file_inspection",
            "dps": None,
        },
        {
            "claim_id": "S54-04",
            "claim": (
                "The manuscript states that Method B's closed form 'matches the directly "
                "summed Borel data'. The Method B block of stage4_methods.py contains no "
                "reference to a Borel coefficient stream; it compares K*Gamma(1+beta) "
                "against the deposited S. No directly summed Borel data enters."
            ),
            "label": "INSPECTED",
            "evidence_type": "file_inspection",
            "dps": None,
        },
        {
            "claim_id": "S54-05",
            "claim": (
                "A genuinely Stokes-independent route exists and was executed in Stage "
                "1.4 (numerical-integral.md section 2): the branch amplitude extracted "
                "from the coefficient stream b_m by Neville acceleration reconstructs "
                f"the deposited S to relative error {o4}, a figure distinct from the "
                f"{o1} reported for Method B. The repair is a rewording plus a corrected "
                "figure, not a retraction of Method B."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 120,
        },
        {
            "claim_id": "S54-06",
            "claim": (
                f"Method C's second check, C = |A|/|beta| against the deposited C, is "
                f"{o3} and is insensitive to a perturbation of S. It is a numerical fact "
                "genuinely distinct from the S = 2piK identity shared by B and C. The "
                "three-method agreement therefore rests on two distinct numerical facts "
                "plus Method A's exact symbolic identity, not three."
            ),
            "label": "VERIFIED",
            "evidence_type": "computation",
            "dps": 120,
        },
    ]

    buf = []
    for c in claims:
        c["task_id"] = TASK
        c["reproducible"] = True
        c["script"] = "scripts/method_b_independence.py"
        c["output_hash"] = ohash
        # Pre-write validation of the in-memory record.
        if not c["claim"].strip():
            refuse(f"{c['claim_id']} has empty claim text")
        if c["label"] not in ("PROVEN", "VERIFIED", "STRUCTURAL",
                              "CONJECTURED", "INSPECTED"):
            refuse(f"{c['claim_id']} carries an unknown label {c['label']!r}")
        if len(c["output_hash"]) != 64:
            refuse(f"{c['claim_id']} output_hash is not a sha256")
        buf.append(json.dumps(c, ensure_ascii=False))

    ids = [c["claim_id"] for c in claims]
    if len(set(ids)) != len(ids):
        refuse("duplicate claim_id in buffer")

    CLAIMS.write_text("\n".join(buf) + "\n", encoding="utf-8")
    print(f"wrote {len(buf)} claims -> {CLAIMS.name}")
    print("claims.jsonl sha256:",
          hashlib.sha256(CLAIMS.read_bytes()).hexdigest())
    for c in claims:
        print(f"  {c['claim_id']}  {c['label']:11s} {c['claim'][:66]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
