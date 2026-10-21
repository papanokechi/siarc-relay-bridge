"""CT-S56 -- the Amendment H sweep, as a script.

The before/after sweeps were originally run inline and their outputs saved by
hand. An output with no script behind it cannot be reproduced and goes stale
silently the moment the text changes -- which is exactly what happened when the
L455 correction was added. This makes the sweep reproducible.

Amendment H: the sweep's result is part of the output whether or not it finds
anything, so terms with zero hits are printed too.

Usage:  python sweep.py before|after
"""
import hashlib
import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent

TARGETS = {
    "before": SESS / "refs" / "src-v1.2" / "vquad-periodrep-paper.tex",
    "after": SESS / "revision" / "vquad-periodrep-paper.tex",
}
TITLES = {
    "before": "v1.2 BASE (before editing)",
    "after": "CT-S56 REVISION (after editing)",
}

# The operator's list, plus the two compound probes. These reproduce the
# ORIGINAL inline sweep exactly (57 hits on v1.2). Two are not the obvious
# patterns, and were recovered by matching the original output line by line:
#   * 'completes' was run as the STEM 'complet', which also catches
#     "a complete rational solution" -- 2 hits, not 1.
#   * the Painleve probe is a PROXIMITY search over the FLATTENED text, so it
#     spans line breaks -- 6 hits, not 4.
#   * 'independent' is run as the STEM 'independen'. The original inline runs
#     used 'independent' for the before-sweep and the stem for the after-sweep
#     -- an instrument that CHANGED BETWEEN ITS OWN TWO RUNS. It was invisible,
#     because on v1.2 the two patterns return the identical 15 lines; it shows
#     only on the revision, where item 5's new prose says "Its independence
#     from B and C", which 'independent' cannot match. The stem is adopted for
#     both runs: it leaves the before-output byte-identical and it is the
#     better instrument, since an independence claim phrased as a noun is
#     exactly what item 5 exists to correct.
# Reconstructing these faithfully matters: a sweep whose instrument quietly
# changes between its before and after runs yields a delta that means nothing.
TERMS = [
    ("D_5", "line", re.compile(r"D_5")),
    ("Sakai", "line", re.compile(r"Sakai")),
    ("Painlev near transcendent", "prox",
     re.compile(r"Painlev.{0,100}transcend|transcend.{0,100}Painlev",
                re.S | re.I)),
    ("completes", "line", re.compile(r"complet")),
    ("twice", "line", re.compile(r"twice")),
    ("independent", "line", re.compile(r"independen", re.I)),
    ("structural argument", "line", re.compile(r"structural argument", re.I)),
    ("apparent", "line", re.compile(r"apparen", re.I)),
]

# The token a proximity hit is attributed to. See the prox branch in main().
ANCHOR = re.compile(r"Painlev", re.I)


def main() -> int:
    which = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    if which not in TARGETS:
        print("usage: sweep.py before|after")
        return 2

    src = TARGETS[which]
    raw = src.read_bytes()
    text = raw.decode("utf-8").replace("\r\n", "\n")
    lines = text.split("\n")

    buf = io.StringIO()

    def say(s=""):
        print(s)
        buf.write(s + "\n")

    say("=" * 74)
    say(f"AMENDMENT H SWEEP -- {TITLES[which]}")
    say("=" * 74)
    say(f"file   : {src.relative_to(SESS)}")
    say(f"sha256 : {hashlib.sha256(raw).hexdigest()}   (of the file's bytes)")
    say(f"lines  : {len(lines)}")
    say("")

    total = 0
    for name, mode, pat in TERMS:
        if mode == "line":
            hits = [(i + 1, l) for i, l in enumerate(lines) if pat.search(l)]
        else:
            # Proximity mode: the pattern may span a line break, so it is run
            # against the whole text. Each match is attributed to the line
            # carrying its ANCHOR token ('Painlev'), not to the line the match
            # happens to start or end on. That rule is what reproduces the
            # original output: hit 1 spans L90-L91 and is reported at L90,
            # hit 2 spans L122-L123 and is reported at L123 -- neither a
            # start-line nor an end-line rule gives both.
            hits = []
            for m in pat.finditer(text):
                a = ANCHOR.search(text, m.start(), m.end())
                pos = a.start() if a else m.start()
                ln = text.count("\n", 0, pos) + 1
                hits.append((ln, lines[ln - 1]))
        total += len(hits)
        say(f"TERM {name:<29}{len(hits)} hit(s)")
        for ln, l in hits:
            say(f"   L{ln:<5} {l.strip()}")
        if not hits:
            say("   (none -- reported because an empty sweep and an absent sweep")
            say("    must not look the same)")
        say("")

    say(f"TOTAL HITS ACROSS ALL TERMS: {total}")
    say("=" * 74)

    out = SESS / "outputs" / f"sweep_v12_{which}.out.txt"
    out.write_text(buf.getvalue(), encoding="utf-8")
    print(f"\n[written] {out}")
    print(f"[sha256]  {hashlib.sha256(out.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
