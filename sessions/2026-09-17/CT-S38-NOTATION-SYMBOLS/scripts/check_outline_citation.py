#!/usr/bin/env python3
r"""check_outline_citation -- OUTLINE.md cites the corpus form.

Operator ruling: "Fix the outline. An alias implemented in the checker is a
workaround for a citation defect; the outline should cite the corpus form."

CT-S37's draft check resolved the family only through a CT- prefix alias and
REPORTED that, correctly, rather than normalising it silently.  This check
establishes that the defect is now fixed at the source: no bare S9-PVPARAMS-*
citation survives in OUTLINE.md, and every id the outline does cite resolves to
exactly one claim in the corpus.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
ROOT = os.path.dirname(SESS)
OUTLINE = os.path.join(ROOT, "CT-S24-PAPER-OUTLINE", "OUTLINE.md")

BARE = r"(?<!CT-)(?<![A-Za-z0-9-])S9-PVPARAMS-C\d+"
FULL = r"CT-S9-PVPARAMS-C\d+"


def read_or_fail(p):
    try:
        with open(p, "r", encoding="utf-8") as fh:
            return fh.read().replace("\r\n", "\n")
    except Exception as exc:
        print("READER INTEGRITY FAILED: cannot read %s (%s)" % (p, exc))
        sys.exit(4)


def corpus_ids():
    """Claim ids from every claims.jsonl EXCEPT this session's own.

    Same reason as label_census: this check walks the corpus and this session
    writes into it, so counting its own output would make the cited digest
    stale the moment it was cited.
    """
    ids = {}
    for dirpath, _d, names in os.walk(ROOT):
        for n in names:
            if n != "claims.jsonl":
                continue
            p = os.path.join(dirpath, n)
            if os.path.dirname(p) == SESS:
                continue
            for m in re.finditer(r'"claim_id"\s*:\s*"([^"]+)"', read_or_fail(p)):
                ids[m.group(1)] = ids.get(m.group(1), 0) + 1
    if not ids:
        print("READER INTEGRITY FAILED: no claim ids found under %s" % ROOT)
        sys.exit(4)
    if not os.path.exists(os.path.join(SESS, "claims.jsonl")):
        print("READER INTEGRITY FAILED: this session has no claims.jsonl, so "
              "the exclusion above is vacuous")
        sys.exit(4)
    return ids


def audit(text, ids):
    bare = re.findall(BARE, text)
    full = sorted(set(re.findall(FULL, text)))
    unresolved = [i for i in full if ids.get(i, 0) != 1]
    return bare, full, unresolved


def run(text, ids, tag):
    bare, full, unresolved = audit(text, ids)
    print("[%s]" % tag)
    print("  bare S9-PVPARAMS-* citations : %d" % len(bare))
    for b in sorted(set(bare)):
        print("    %s   <-- NOT A CORPUS ID" % b)
    print("  CT-S9-PVPARAMS-* cited       : %d  (%s)"
          % (len(full), ", ".join(full) if full else "none"))
    for u in unresolved:
        print("    %s resolves to %d claims" % (u, ids.get(u, 0)))
    rows = [
        ("O1 no bare short-form citation survives", not bare),
        ("O2 the corpus form is actually cited", len(full) >= 2),
        ("O3 every cited id resolves to exactly one claim", not unresolved),
    ]
    for label, good in rows:
        print("  %-48s %s" % (label, "ok" if good else "FAILED"))
    return sum(0 if g else 1 for _l, g in rows)


def main():
    text = read_or_fail(OUTLINE)
    ids = corpus_ids()
    print("check_outline_citation -- the outline cites the corpus form")
    print("  outline : %s (%d B)" % (OUTLINE, len(text)))
    print("  corpus  : %d distinct claim ids\n" % len(ids))
    bad = run(text, ids, "outline as it now stands")

    print("\n[controls -- each mutation must be REJECTED]")
    arms = [
        ("C1 the short form reinstated", "O1",
         lambda t: t.replace("CT-S9-PVPARAMS-C002", "S9-PVPARAMS-C002", 1)),
        ("C2 a citation pointed at a non-existent claim", "O3",
         lambda t: t.replace("CT-S9-PVPARAMS-C002",
                             "CT-S9-PVPARAMS-C999", 1)),
        ("C3 the family removed entirely (non-vacuity)", "O2",
         lambda t: re.sub(FULL, "", t)),
    ]
    nmiss = 0
    for name, want, mut in arms:
        b, f, u = audit(mut(text), ids)
        fired = []
        if b:
            fired.append("O1")
        if len(f) < 2:
            fired.append("O2")
        if u:
            fired.append("O3")
        ok = want in fired
        print("  %-46s %s  (fired: %s)"
              % (name, "CAUGHT" if ok else "MISSED",
                 ", ".join(fired) or "nothing"))
        nmiss += 0 if ok else 1

    print("\n[verdict]")
    print("  checks failed : %d" % bad)
    print("  arms CAUGHT   : %d/%d" % (len(arms) - nmiss, len(arms)))
    if bad or nmiss:
        print("  VERDICT: OUTLINE CITATION FORM NOT ESTABLISHED")
        sys.exit(1)
    print("  VERDICT: OUTLINE CITES THE CORPUS FORM")
    sys.exit(0)


if __name__ == "__main__":
    main()
