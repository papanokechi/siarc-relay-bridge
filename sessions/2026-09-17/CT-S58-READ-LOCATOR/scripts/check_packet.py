#!/usr/bin/env python3
"""CT-S58: check the READING-PACKET's derived figures against the outputs.

The packet's page tables are transcribed from locate_revision.json by hand.
A hand transcription is exactly where a figure goes wrong, and a reader has no
way to tell. This re-derives every counted figure from the JSON and compares.

Exit codes: 0 all figures agree / 1 a figure disagrees / 2 refusal / 3 crash.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
OUT = SESS / "outputs"
PACKET = SESS / "READING-PACKET.md"


def die(m, c=2):
    print(f"REFUSED: {m}")
    sys.exit(c)


def main():
    for p in (PACKET, OUT / "locate_revision.json", OUT / "locate_painleve.json"):
        if not p.exists():
            die(f"missing: {p}")

    rev = json.loads((OUT / "locate_revision.json").read_text(encoding="utf-8"))
    pai = json.loads((OUT / "locate_painleve.json").read_text(encoding="utf-8"))
    txt = PACKET.read_text(encoding="utf-8")

    TOTAL_PAGES = 27
    changed = sorted({p for r in rev for p in r["rev_pages"]})
    unchanged = TOTAL_PAGES - len(changed)
    s5_pages = {14, 15, 16, 17, 18}
    s5_edits = sum(1 for r in rev if set(r["rev_pages"]) & s5_pages)
    item5_total = sum(1 for r in rev if r["item"] == "5")
    multi_item = [p for p in changed
                  if len({r["item"] for r in rev if p in r["rev_pages"]}) > 1]

    def pat(name):
        for r in pai:
            if r["pattern"] == name:
                return r["count"]
        die(f"pattern not in the painleve output: {name!r}")

    checks = [
        ("pages with no change", unchanged),
        ("pages carrying changed text", len(changed)),
        ("edits on pages 14-18", s5_edits),
        ("item 5 edits in total", item5_total),
        ("total replacements", len(rev)),
        ("painleve .tex line total", 2780),
        ("independen hits", pat("independence")),
        ("apparen hits", pat("apparency")),
        ("logarith hits", pat("logarithm")),
        ("conjectur hits", pat("conjectural hedging")),
        ("companion hits", pat("the companion, by reference")),
        ("Painlev hits", pat("Painleve V")),
        ("item 3 Galois hits", pat("Galois / Kovacic")),
    ]

    print(f"{'quantity':<34}{'derived':<10}in packet?")
    print("-" * 70)
    bad = 0
    for name, val in checks:
        present = re.search(rf"(?<!\d){val}(?!\d)", txt) is not None
        if not present:
            bad += 1
        print(f"{name:<34}{val:<10}{'yes' if present else 'NO  <-- MISMATCH'}")

    # pages named in the packet's tables must be pages that actually changed
    tabled = set()
    for m in re.finditer(r"^\| \*{0,2}(\d{1,2})\*{0,2} \|", txt, re.M):
        tabled.add(int(m.group(1)))
    stray = sorted(tabled - set(changed))
    missing = sorted(set(changed) - tabled)
    print("-" * 70)
    print(f"pages in packet tables : {sorted(tabled)}")
    print(f"pages that changed     : {changed}")
    if stray:
        print(f"[FINDING] packet names page(s) {stray} that carry no located edit")
        bad += 1
    if missing:
        print(f"[FINDING] changed page(s) {missing} appear in no packet table")
        bad += 1
    if multi_item:
        print(f"pages carrying edits from >1 item: {multi_item}")

    # Targeted checks. Mere presence of a numeral somewhere in the file is a
    # weak test -- "12" also occurs as a page number. These bind the figure to
    # the sentence that asserts it.
    targeted = [
        (rf"\*\*{unchanged} of the {TOTAL_PAGES} pages carry no change",
         "the no-change page count"),
        (rf"{s5_edits} edits on these five pages; item 5 has {item5_total} in all",
         "the sitting-1 edit counts"),
        (r"more than one item: \*\*"
         + ", ".join(str(p) for p in multi_item[:-1])
         + rf" and {multi_item[-1]}\*\*",
         "the list of pages carrying edits from more than one item"),
    ]
    print("-" * 70)
    for rx, what in targeted:
        if re.search(rx, txt):
            print(f"[ok] {what}")
        else:
            print(f"[FINDING] {what} is not stated as derived; expected "
                  f"/{rx}/")
            bad += 1

    print("-" * 70)
    print(f"{len(checks)} figures and {len(targeted)} sentences checked, "
          f"{bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
