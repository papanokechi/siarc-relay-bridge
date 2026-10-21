"""CT-S56 -- compare the Amendment H sweep before and after editing.

The before/after deltas are DERIVED from the two sweep outputs, not transcribed
from prose. A transcribed delta drifts the moment either sweep is re-run, and a
sweep whose headline number is wrong is worse than no sweep.

The sweep is a census, not a gate: 'independent' and 'apparent' RISE, because
the revision now discusses both rather than asserting them. A gate demanding
they fall would have been a threshold tuned to an expectation.
"""
import hashlib
import io
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUTD = SESS / "outputs"
BEFORE = OUTD / "sweep_v12_before.out.txt"
AFTER = OUTD / "sweep_v12_after.out.txt"
OUT = OUTD / "sweep_compare.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


TERM = re.compile(r"^TERM\s+(.+?)\s{2,}(\d+) hit\(s\)$", re.M)
TOTAL = re.compile(r"^TOTAL HITS ACROSS ALL TERMS:\s*(\d+)$", re.M)


def parse(p: Path):
    t = p.read_text(encoding="utf-8", errors="replace")
    counts = {m.group(1).strip(): int(m.group(2)) for m in TERM.finditer(t)}
    tot = TOTAL.search(t)
    return counts, (int(tot.group(1)) if tot else None)


def main() -> int:
    b, btot = parse(BEFORE)
    a, atot = parse(AFTER)

    say("=" * 74)
    say("CT-S56 -- Amendment H sweep, v1.2 before vs revision after")
    say("=" * 74)
    say("")

    if not b or not a or btot is None or atot is None:
        say("REFUSED: could not parse one of the sweep outputs; a parser that")
        say("silently returns nothing would report 'no change' for every term.")
        OUT.write_text(BUF.getvalue(), encoding="utf-8")
        return 2

    say(f"    terms parsed : before {len(b)}, after {len(a)}")
    say(f"    totals       : before {btot}, after {atot}   "
        f"(net {atot - btot:+d})")
    say("")
    if sum(b.values()) != btot or sum(a.values()) != atot:
        say(f"REFUSED: per-term counts ({sum(b.values())}, {sum(a.values())}) do")
        say("not sum to the reported totals; the parse is incomplete.")
        OUT.write_text(BUF.getvalue(), encoding="utf-8")
        return 2
    say("    [PASS] per-term counts sum to the reported totals in both files")
    say("")

    say("[1] PER-TERM")
    say("")
    say(f"    {'term':<26}{'before':>8}{'after':>8}{'delta':>8}")
    for k in sorted(set(b) | set(a)):
        bb, aa = b.get(k, 0), a.get(k, 0)
        mark = "" if bb == aa else "   <-"
        say(f"    {k:<26}{bb:>8}{aa:>8}{aa - bb:>+8}{mark}")
    say("")

    say("[2] THE TWO TERMS THAT WERE MEANT TO FALL")
    for k in ("completes", "twice"):
        if k in b and k in a:
            ok = a[k] < b[k]
            say(f"    [{'as intended' if ok else 'NOT AS INTENDED'}] "
                f"{k}: {b[k]} -> {a[k]}")
    say("")
    say("[3] THE TWO TERMS THAT ROSE, AND WHY THAT IS NOT A DEFECT")
    for k in ("independent", "apparent"):
        if k in b and k in a:
            say(f"    {k}: {b[k]} -> {a[k]}  ({a[k] - b[k]:+d})")
    say("    Items 3, 4 and 5 replace assertions of independence and apparency")
    say("    with discussion of why neither holds. Prose that explains a")
    say("    correction necessarily uses the word it is correcting, so the")
    say("    count rising is expected. Every remaining hit was read by hand;")
    say("    the count alone decides nothing.")
    say("")
    say("=" * 74)
    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
