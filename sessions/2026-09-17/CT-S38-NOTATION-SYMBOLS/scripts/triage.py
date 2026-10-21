#!/usr/bin/env python3
"""triage -- how many genuine symbol collisions does section 1 actually have?

The operator's ruling says "fix the 6 genuine collisions in section 1", leaves
about 65 to their own sections and lets about 9 retire with the cut section 9.
No artefact in the corpus holds that triage, so the number is re-derived here
by the instrument rather than assumed, and the measured value is reported
against 6 whichever way it falls.

A base is a SECTION-1 COLLISION candidate when it occurs in section1.tex and
also occurs in at least one other source under a key section1.tex does not
use.  That is a necessary condition, not a sufficient one -- Q_n in section 1
and Q_n in theorem.tex are the same object -- so each candidate is printed
with its evidence and adjudicated in REPORT.md.  The script reports the
candidate set; it does not decide.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import symbol_index as SI                                    # noqa: E402

S1 = "section1.tex"


def main():
    by_base, _occ, _per, _srcs = SI.build_index(verbose=False)

    print("triage -- section 1 collision candidates")
    print("rule: base occurs in %s AND elsewhere under a key %s does not use"
          % (S1, S1))

    cands, shared, s1only = [], [], []
    for base in sorted(by_base):
        keys = by_base[base]
        in_s1 = {k for (k, l) in keys if any(s == S1 for (s, _c) in l)}
        if not in_s1:
            continue
        elsewhere = {}
        for (k, l) in keys:
            for (s, c) in l:
                if s != S1:
                    elsewhere.setdefault(k, set()).add(s)
        foreign = {k: v for k, v in elsewhere.items() if k not in in_s1}
        if not elsewhere:
            s1only.append(base)
        elif foreign:
            cands.append((base, sorted(in_s1), foreign))
        else:
            shared.append(base)

    print("\n[section-1 bases: %d]" % (len(cands) + len(shared) + len(s1only)))
    print("  %3d carry a key used only outside section 1  -> CANDIDATES"
          % len(cands))
    print("  %3d carry exactly the same keys elsewhere    -> same object"
          % len(shared))
    print("  %3d occur in section 1 only                  -> no collision"
          % len(s1only))

    print("\n[candidates, with evidence]")
    for base, in_s1, foreign in cands:
        print("\n  BASE %-10s section 1 uses: %s" % (base, ", ".join(in_s1)))
        for k in sorted(foreign):
            print("      elsewhere %-18s %s" % (k, ", ".join(sorted(
                foreign[k]))))

    print("\n[bases with identical keys inside and outside section 1]")
    print("  " + " ".join(shared))
    print("\n[bases confined to section 1]")
    print("  " + " ".join(s1only))

    print("\n[measured]")
    print("  candidate count : %d" % len(cands))
    print("  operator's figure for section 1 : 6")
    print("  These are CANDIDATES under a necessary condition; the genuine")
    print("  count is adjudicated in REPORT.md against this evidence.")
    sys.exit(0)


if __name__ == "__main__":
    main()
