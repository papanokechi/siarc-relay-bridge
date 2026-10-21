"""Count the title's three headline terms in the PUBLISHED description.

Reads the archived copy of record 22850681, not the network, so the result is
reproducible after the fact.  Reader integrity (P0 Amendment C) is asserted
before any count is reported, and the absence report in particular: "Bridge
Conjecture: 0" and "my reader could not see the file" are otherwise identical
output.
"""

import hashlib
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REC = os.path.join(HERE, "refs", "zenodo-22850681-record.json")
REC_SHA = "0126450834aca76572aaad13ec475ab68df8b8a79a02b207594799c55fb1faed"


def main():
    raw = io.open(REC, "rb").read()
    got = hashlib.sha256(raw).hexdigest()
    if got != REC_SHA:
        sys.exit("ABORT: archived record is not the one this script was written\n"
                 "  on disk : %s\n  expected: %s" % (got, REC_SHA))

    md = json.loads(raw.decode("utf-8"))["metadata"]
    title, desc = md["title"], md["description"]

    # ---- reader integrity, BEFORE any count is reported --------------------
    # Known-present features, one of which is non-ASCII: an ASCII-only sentinel
    # set survives a wrong-codec read intact and cannot detect it.
    checks = [
        ("title is the published one", "Channel Theory for Polynomial" in title),
        ("non-ASCII present in the title", any(ord(c) > 127 for c in title)),
        ("non-ASCII present in the description", any(ord(c) > 127 for c in desc)),
        ("description is substantial", len(desc) > 60000),
        ("a known-present word is found", desc.count("Pincherle") > 0),
    ]
    print("READER INTEGRITY (asserted before any absence is reported)")
    print("-" * 74)
    for name, ok in checks:
        print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not all(ok for _, ok in checks):
        sys.exit("ABORT: the reader cannot see the file; no count below would "
                 "mean anything.")
    print()

    print("TITLE (verbatim)")
    print("-" * 74)
    print("  %s" % title)
    print()

    print("TERM COUNTS IN THE PUBLISHED DESCRIPTION")
    print("-" * 74)
    terms = ["Perron", "Kreuser", "Pincherle", "Bridge Conjecture"]
    for t in terms:
        print("  %-20s %d" % (t, len(re.findall(re.escape(t), desc))))
    loose = [re.sub(r"<[^>]+>", "", desc[max(0, m.start() - 60):m.start() + 60])
             for m in re.finditer(r"(?i)bridge", desc)]
    print("  %-20s %d" % ("bridge (any case)", len(loose)))
    for ctx in loose:
        print("      ...%s..." % " ".join(ctx.split()))
    print()
    print("Counts are of the PUBLISHED text, archived at sha256 %s." % REC_SHA)
    return 0


if __name__ == "__main__":
    sys.exit(main())
