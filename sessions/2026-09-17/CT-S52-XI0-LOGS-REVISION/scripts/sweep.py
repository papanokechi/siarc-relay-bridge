#!/usr/bin/env python3
"""CT-S52 Part B -- the Amendment H sweep.

Run BEFORE editing and again AFTER. Every hit is listed with its line number,
including hits that are not edited; the report says why each was left. An empty
sweep and an absent sweep must not look the same, so the script always prints a
per-term count, zero included.

usage: sweep.py <tex> <label> [outfile]
"""
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re
import hashlib

TERMS = [
    ("D_5", r"D_5|D_\{5\}|D\^\{\(1\)\}_5|D_5\^\{\(1\)\}|\\Dfive"),
    ("Sakai", r"Sakai"),
    ("Painlev near transcendent", None),      # handled specially
    ("completes", r"complete[sd]?\b"),
    ("twice", r"twice"),
    ("independent", r"independen"),
    ("structural argument", r"structural argument"),
    ("apparent", r"apparen"),
]


def main():
    tex = sys.argv[1]
    label = sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else None
    with open(tex, "rb") as fh:
        data = fh.read()
    raw = data.decode("utf-8")
    lines = raw.replace("\r\n", "\n").split("\n")
    L = []

    def say(s=""):
        print(s)
        L.append(s)

    say("=" * 74)
    say("AMENDMENT H SWEEP -- %s" % label)
    say("=" * 74)
    say("file   : %s" % tex)
    say("sha256 : %s   (of the file's bytes)"
        % hashlib.sha256(data).hexdigest())
    say("lines  : %d" % len(lines))
    total = 0
    for name, pat in TERMS:
        say()
        if pat is None:
            # "Painlev" within 2 lines of "transcendent"
            hits = []
            for i, ln in enumerate(lines):
                if re.search(r"Painlev", ln, re.I):
                    lo, hi = max(0, i - 2), min(len(lines), i + 3)
                    if any(re.search(r"transcenden", lines[j], re.I)
                           for j in range(lo, hi)):
                        hits.append((i + 1, ln))
        else:
            hits = [(i + 1, ln) for i, ln in enumerate(lines)
                    if re.search(pat, ln, re.I)]
        total += len(hits)
        say("TERM %-28s %d hit(s)" % (name, len(hits)))
        for n, ln in hits:
            s = ln.strip()
            if len(s) > 150:
                s = s[:147] + "..."
            say("   L%-5d %s" % (n, s))
    say()
    say("TOTAL HITS ACROSS ALL TERMS: %d" % total)
    say("=" * 74)
    if out:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(L) + "\n")
        print("[wrote]", os.path.abspath(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
