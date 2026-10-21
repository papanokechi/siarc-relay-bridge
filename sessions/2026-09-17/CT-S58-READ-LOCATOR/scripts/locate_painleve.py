#!/usr/bin/env python3
"""CT-S58: locate, in the Painlevé paper's source, every statement that falls
within the scope of the five LMP correction items.

This does NOT judge those statements. It produces the reading list for the
operator's Tier-2 cross-check: the two papers share objects (V_quad, L_phi,
apparency at xi=0, the D_5^(1) identification, verification independence), and
the Painlevé paper was drafted before items 4 and 5 existed.

Commissioning clause: every pattern is reported with its count, INCLUDING
zero. An empty sweep and an absent sweep must not look alike.

Exit codes: 0 clean / 1 finding / 2 refusal / 3 crash.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
S17 = SESS.parent
PAPER = S17 / "CT-S50-READ-REPAIRS"
OUT = SESS / "outputs"

# (item, pattern-name, regex, case-sensitive?, why it is in that item's scope)
#
# Case matters. The first run made every pattern case-insensitive, so the
# macro pattern for the shared operators matched \lvert and \lVert and
# reported three hits for an operator the paper never names. Three phantom
# findings. LaTeX macro patterns are case-sensitive here; prose patterns are
# not, and each row says which it is.
PATTERNS = [
    (1, "D_5 surface", r"D_?5|D\^?\{?\(1\)|Sakai", False,
     "item 1: the surface identification is conjectural"),
    (1, "Painleve V", r"Painlev", False,
     "item 1: the transcendent claim rests on the same conjecture"),
    (1, "conjectural hedging", r"conjectur", False,
     "item 1: where the paper already hedges, no edit is needed"),
    (2, "stratum / part (ii)(a)", r"stratum|\(ii\)\s*\(a\)|complet", False,
     "item 2: 'completes part (ii)(a)' was an overclaim in the LMP paper"),
    (3, "Galois / Kovacic", r"Kovacic|Galois|SL_?2", False,
     "item 3: the 'proved twice' claim concerned L_phi's Galois group"),
    (3, "proved twice", r"twice|second proof|two independent proofs", False,
     "item 3: the exact phrase pattern that was withdrawn"),
    (4, "apparency", r"apparen", False,
     "item 4: xi=0 is NOT apparent; any inheritance of that claim is a defect"),
    (4, "logarithm", r"logarith", False,
     "item 4: the corrected statement is that a logarithm is present at 0"),
    (4, "xi = 0 / the origin", r"\\xi\s*=\s*0|\\xizero|origin", False,
     "item 4: the point itself"),
    (5, "independence", r"independen", False,
     "item 5: B and C are not mutually independent"),
    (5, "verification methods", r"Method~?[ABC]\b", True,
     "item 5: the three-methods framing"),
    (5, "Stokes datum S", r"Stokes|amplitude", False,
     "item 5: S entering Method B through the amplitude is the defect"),
    (0, "shared object, by NAME: V_quad", r"\\Vquad|V_\{?\\mathrm\{quad", True,
     "neither item: does the paper use the LMP paper's NAME for the object?"),
    (0, "shared operator, by NAME: L_phi / L_V", r"\\Lphi|\\LV\b|L_\\phi|L_V",
     True,
     "neither item: does the paper use the LMP paper's NAMES for the operators?"),
    (0, "shared object, by SUBSTANCE: b(n)=3n^2+n+1", r"3n\^?\{?2\}?\+n\+1",
     True,
     "neither item: the same object identified by content rather than by name"),
    (0, "the companion, by reference", r"companion", False,
     "neither item: where the paper points at the LMP paper's material"),
]

# Controls. The negative one must return zero; if it does not, the patterns are
# matching noise. The positive one must return non-zero; if it does not, the
# reader cannot see the source at all and every zero above is uninterpretable.
NEG_CONTROL = ("Riemann hypothesis", r"Riemann\s+hypothesis")
POS_CONTROL = ("section heading", r"\\section\{")


def die(msg, code=2):
    print(f"REFUSED: {msg}")
    sys.exit(code)


def main():
    if not PAPER.exists():
        die(f"Painleve paper source not found at {PAPER}")
    srcs = sorted(p for p in PAPER.glob("*.tex"))
    if not srcs:
        die(f"no .tex files in {PAPER}")

    files = {}
    for p in srcs:
        files[p.name] = p.read_text(encoding="utf-8",
                                    errors="replace").split("\n")

    def sweep(rx, cs=False):
        c = re.compile(rx) if cs else re.compile(rx, re.I)
        hits = []
        for name in sorted(files):
            for i, ln in enumerate(files[name], 1):
                if c.search(ln):
                    hits.append((name, i, ln.strip()))
        return hits

    # Case-sensitivity control: probe with the pattern that ACTUALLY failed
    # (r"\\LV", no word boundary), not with the repaired one. A control built
    # from the fixed pattern proves nothing: it must be able to reproduce the
    # defect it exists to exclude.
    cs_probe = sweep(r"\\LV", cs=True)
    ci_probe = sweep(r"\\LV", cs=False)
    if len(ci_probe) <= len(cs_probe):
        die("case control is vacuous: the case-insensitive probe did not "
            "over-match, so it cannot demonstrate the defect it guards")
    cs_note = (f"case control: '\\\\LV' case-sensitive {len(cs_probe)} hit(s), "
               f"case-insensitive {len(ci_probe)} hit(s) -- case-insensitivity "
               f"manufactures {len(ci_probe) - len(cs_probe)} phantom hit(s) "
               f"(it matches \\lvert, \\lVert); macro patterns below are "
               f"case-sensitive")

    neg = sweep(NEG_CONTROL[1])
    pos = sweep(POS_CONTROL[1])
    if pos == []:
        die(f"POSITIVE control failed: {POS_CONTROL[0]!r} matched nothing; "
            "the reader cannot see the source and every zero below is void")
    if neg:
        die(f"NEGATIVE control failed: {NEG_CONTROL[0]!r} matched "
            f"{len(neg)} line(s); the patterns are matching noise")

    lines, W = [], "=" * 78
    lines.append(W)
    lines.append("CT-S58 -- Painleve paper: statements in scope of the five "
                 "LMP correction items")
    lines.append(W)
    lines.append(f"source: {PAPER}")
    lines.append(f"files : {len(srcs)} .tex, "
                 f"{sum(len(v) for v in files.values())} lines")
    lines.append(f"controls: POSITIVE {POS_CONTROL[0]!r} {len(pos)} hits PASS; "
                 f"NEGATIVE {NEG_CONTROL[0]!r} 0 hits PASS")
    lines.append(cs_note)
    lines.append("")
    lines.append("Every pattern below is listed with its count, including "
                 "zero. A zero reads")
    lines.append("'pattern ran, 0 hits' and is a result, not an omission.")
    lines.append("")

    total, zero_patterns, by_item = 0, [], {}
    results = []
    for item, name, rx, cs, why in PATTERNS:
        hits = sweep(rx, cs)
        total += len(hits)
        by_item.setdefault(item, 0)
        by_item[item] += len(hits)
        if not hits:
            zero_patterns.append(name)
        results.append({"item": item, "pattern": name, "regex": rx,
                        "case_sensitive": cs,
                        "why": why, "count": len(hits),
                        "hits": [{"file": f, "line": l, "text": t}
                                 for f, l, t in hits]})
        lines.append("-" * 78)
        lines.append(f"ITEM {item if item else '-'}  {name}   "
                     f"{'pattern ran, 0 hits' if not hits else f'{len(hits)} hit(s)'}")
        lines.append(f"   scope: {why}")
        lines.append(f"   regex: {rx}   ({'case-sensitive' if cs else 'case-insensitive'})")
        for f, l, t in hits:
            lines.append(f"     {f}:{l}  {t[:150]}")
    lines.append("-" * 78)
    lines.append("")
    lines.append(W)
    lines.append("SUMMARY BY ITEM")
    lines.append(W)
    for item in sorted(by_item):
        label = f"item {item}" if item else "shared objects"
        lines.append(f"  {label:<16} {by_item[item]} line-hit(s)")
    lines.append(f"  {'TOTAL':<16} {total} line-hit(s)")
    lines.append(f"  patterns returning zero: "
                 f"{', '.join(zero_patterns) if zero_patterns else 'none'}")
    lines.append(W)

    txt = "\n".join(lines) + "\n"
    OUT.mkdir(exist_ok=True)
    (OUT / "locate_painleve.out.txt").write_text(txt, encoding="utf-8")
    (OUT / "locate_painleve.json").write_text(
        json.dumps(results, indent=1), encoding="utf-8")
    print(txt[:4000])
    h = hashlib.sha256((OUT / "locate_painleve.out.txt").read_bytes()).hexdigest()
    print(f"\noutput sha256 {h}")
    print(f"full output: {OUT / 'locate_painleve.out.txt'}")

    # F4: all five items empty would mean the sweep cannot see.
    item_hits = sum(by_item.get(i, 0) for i in (1, 2, 3, 4, 5))
    if item_hits == 0:
        print("\n[FINDING] F4: no pattern for any of the five items matched; "
              "either the papers share nothing or the sweep is blind")
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
