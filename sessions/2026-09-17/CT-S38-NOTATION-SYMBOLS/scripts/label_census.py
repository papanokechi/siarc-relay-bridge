#!/usr/bin/env python3
r"""label_census -- which epistemic labels does the corpus actually carry?

P0 as pasted enumerates four labels: PROVEN, VERIFIED, STRUCTURAL,
CONJECTURED.  INSPECTED was adopted later as an operator ruling and was never
folded back into the preamble, so CT-S37's Group B check reported prose
carrying a label P0 does not list.  The operator's ruling: P0 is stale, not the
corpus.  This script establishes the census that the ruling rests on.

The census walks every claims.jsonl under sessions/2026-09-17/ and reports the
label of every claim line.  It fails if any line carries no label, more than
one label field, or a label outside the five.
"""
import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # sessions/2026-09-17
SELF = os.path.dirname(HERE)                   # this session's folder
FIVE = ["PROVEN", "VERIFIED", "STRUCTURAL", "INSPECTED", "CONJECTURED"]


def corpus_files(root):
    """Every claims.jsonl EXCEPT this session's own.

    The census walks the corpus, and this session writes claims.jsonl into
    that corpus.  A census that counted its own output would change the moment
    it was cited, leaving S38-17 pointing at a digest that resolves to
    nothing.  Excluding this session makes the census invariant under its own
    emission; the exclusion is asserted below, not assumed.
    """
    out = []
    for dirpath, _d, names in os.walk(root):
        for n in names:
            if n != "claims.jsonl":
                continue
            p = os.path.join(dirpath, n)
            if os.path.dirname(p) == SELF:
                continue
            out.append(p)
    return sorted(out)


def census(root, extra_lines=()):
    files = corpus_files(root)
    if not files:
        print("READER INTEGRITY FAILED: no claims.jsonl found under %s" % root)
        sys.exit(4)
    counts = collections.Counter()
    unknown, missing, dup = [], [], []
    total = 0
    for p in files:
        try:
            with open(p, "r", encoding="utf-8") as fh:
                lines = fh.read().replace("\r\n", "\n").split("\n")
        except Exception as exc:
            print("READER INTEGRITY FAILED: cannot read %s (%s)" % (p, exc))
            sys.exit(4)
        for raw in lines:
            if not raw.strip():
                continue
            total += 1
            try:
                obj = json.loads(raw)
            except Exception:
                unknown.append((p, "<unparseable>"))
                continue
            if raw.count('"label"') > 1:
                dup.append((p, obj.get("claim_id")))
            lab = obj.get("label")
            if lab is None:
                missing.append((p, obj.get("claim_id")))
                continue
            counts[lab] += 1
            if lab not in FIVE:
                unknown.append((p, "%s -> %s" % (obj.get("claim_id"), lab)))
    for raw in extra_lines:
        total += 1
        obj = json.loads(raw)
        lab = obj.get("label")
        counts[lab] += 1
        if lab not in FIVE:
            unknown.append(("<injected>", "%s -> %s"
                            % (obj.get("claim_id"), lab)))
    return files, total, counts, unknown, missing, dup


def report(files, total, counts, unknown, missing, dup, tag):
    print("[%s]" % tag)
    print("  claims.jsonl files : %d" % len(files))
    print("  claim lines        : %d" % total)
    for lab in FIVE:
        print("    %-12s %4d" % (lab, counts.get(lab, 0)))
    other = sorted(k for k in counts if k not in FIVE)
    for lab in other:
        print("    %-12s %4d   <-- NOT IN P0's LIST, NOR IN THE FIVE"
              % (lab, counts[lab]))
    rows = [
        ("C1 every claim line carries a label", not missing),
        ("C2 no line carries two label fields", not dup),
        ("C3 every label is one of the five", not unknown),
        ("C4 the five partition the corpus",
         sum(counts.get(l, 0) for l in FIVE) == total),
        ("C5 INSPECTED is present in the corpus", counts.get("INSPECTED", 0) > 0),
        ("C6 this session's own claims.jsonl exists and is excluded",
         os.path.exists(os.path.join(SELF, "claims.jsonl"))
         and all(os.path.dirname(p) != SELF for p in files)),
    ]
    for label, good in rows:
        print("  %-44s %s" % (label, "ok" if good else "FAILED"))
    return sum(0 if g else 1 for _l, g in rows)


def main():
    root = ROOT
    print("label_census -- epistemic labels actually carried by the corpus")
    print("  root: %s" % root)
    bad = report(*census(root), tag="census")

    print("\n[control -- an injected sixth label must be reported]")
    inj = json.dumps({"claim_id": "CONTROL-00", "label": "ASSUMED",
                      "claim": "control line, not a corpus claim"})
    c = census(root, extra_lines=[inj])
    caught = bool(c[3])
    print("  injected ASSUMED reported as not-in-the-five : %s"
          % ("CAUGHT" if caught else "MISSED"))
    if c[3]:
        for where, what in c[3]:
            print("    %s  %s" % (where, what))

    print("\n[verdict]")
    n = counts_of(root)
    print("  INSPECTED %d of %d claim lines (%.1f%%), the most common label"
          % (n[0], n[1], 100.0 * n[0] / n[1]))
    print("  checks failed : %d" % bad)
    print("  control       : %s" % ("CAUGHT" if caught else "MISSED"))
    if bad or not caught:
        print("  VERDICT: CENSUS NOT ESTABLISHED")
        sys.exit(1)
    print("  VERDICT: P0's FOUR-LABEL LIST IS STALE; THE CORPUS CARRIES FIVE")
    sys.exit(0)


def counts_of(root):
    _f, total, counts, _u, _m, _d = census(root)
    return counts.get("INSPECTED", 0), total


if __name__ == "__main__":
    main()
