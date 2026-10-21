"""
CT-S23-OUTSIDER-READ - adjudication of the two cold returns against PREREG.

Scores, mechanically:
  F1  (PREREG section 3) - instrument validity. Fires if the CONTROL reader
      returns SELF-CONTAINED, or lists fewer than 5 items under task 2.
  F2  (PREREG section 3) - sensitivity of the MAIN read. Recorded as
      LOW-SENSITIVITY if |T2 n G| / |G| < 0.5, with G read from the hashed
      outputs/jargon_index.out.txt written BEFORE the reads were dispatched.
  VAC (PREREG section 4 arm (i)) - the observable must move when the packet
      moves. Fires if the two reads return the SAME verdict.

Every threshold here is transcribed from PREREG.md and none was changed after
the returns were seen. Where a pre-registered criterion turns out to be
ill-posed that is reported as a finding, not adjusted.
"""

import hashlib
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
MAIN = HERE / "outputs" / "coldread_main.txt"
CTRL = HERE / "outputs" / "coldread_control.txt"
IDX = HERE / "outputs" / "jargon_index.out.txt"
OUT = HERE / "outputs" / "adjudicate.out.txt"

VERDICTS = ["NOT SELF-CONTAINED",
            "SELF-CONTAINED AFTER LISTED REPAIRS",
            "SELF-CONTAINED"]

# G-term -> regex recognising it inside a reader's task-2 list.
G_PATTERNS = {
    "System C": r"System C",
    "K": r"\*\*`?K`?\*\*|`K`",
    "Katz multiset": r"Katz",
    "PV": r"\bPV\b|Painlev",
    "D5tilde": r"D̃₅|D5|D_5|D̃5",
}


def verdict_of(text):
    """Longest-match first, so the substring 'SELF-CONTAINED' cannot shadow
    'NOT SELF-CONTAINED'."""
    tail = text[int(len(text) * 0.6):]
    for v in VERDICTS:  # NOT... first, then ...REPAIRS, then bare
        if re.search(r"\*\*" + re.escape(v) + r"\*\*", tail):
            return v
    for v in VERDICTS:
        if v in tail:
            return v
    return None


def task2_section(text):
    m2 = re.search(r"^##\s*2[\.\s]", text, re.M)
    m3 = re.search(r"^##\s*3[\.\s]", text, re.M)
    if not m2:
        return ""
    return text[m2.start():m3.start() if m3 else len(text)]


def count_items(sec):
    return len(re.findall(r"^\s*(?:[-*]|\d+\.)\s+\S", sec, re.M))


def read_G(idx_text):
    m = re.search(r"G \(used before defined\), \|G\| = (\d+):\n(.*?)\n\n",
                  idx_text, re.S)
    assert m, "could not read G from the hashed index"
    n = int(m.group(1))
    g = re.findall(r"^\s*-\s*(.+)$", m.group(2), re.M)
    assert len(g) == n, "G count mismatch: header %d, listed %d" % (n, len(g))
    return g


def main():
    main_t = MAIN.read_text(encoding="utf-8", errors="replace")
    ctrl_t = CTRL.read_text(encoding="utf-8", errors="replace")
    idx_t = IDX.read_text(encoding="utf-8")
    G = read_G(idx_t)

    L = []
    L.append("CT-S23-OUTSIDER-READ - adjudication of the cold returns")
    L.append("")
    for name, p in (("main", MAIN), ("control", CTRL), ("index", IDX)):
        L.append("  %-8s %-26s sha256 %s"
                 % (name, p.name, hashlib.sha256(p.read_bytes()).hexdigest()))
    L.append("")
    L.append("G, from the index hashed before dispatch: %s" % G)
    L.append("")

    v_main, v_ctrl = verdict_of(main_t), verdict_of(ctrl_t)
    s_main, s_ctrl = task2_section(main_t), task2_section(ctrl_t)
    n_main, n_ctrl = count_items(s_main), count_items(s_ctrl)

    L.append("%-10s %-38s %s" % ("read", "verdict", "task-2 items"))
    L.append("-" * 64)
    L.append("%-10s %-38s %d" % ("MAIN", v_main, n_main))
    L.append("%-10s %-38s %d" % ("CONTROL", v_ctrl, n_ctrl))
    L.append("")

    # ---- F1: instrument validity -----------------------------------------
    f1 = (v_ctrl == "SELF-CONTAINED") or (n_ctrl < 5)
    L.append("F1  instrument validity (control must not say SELF-CONTAINED,")
    L.append("    and must list >= 5 task-2 items)")
    L.append("    control verdict   : %s" % v_ctrl)
    L.append("    control T2 items  : %d" % n_ctrl)
    L.append("    -> F1 %s" % ("FIRED - main read is VOID" if f1 else "did not fire"))
    L.append("")

    # ---- F2: sensitivity of the main read --------------------------------
    hit, miss = [], []
    for g in G:
        pat = G_PATTERNS[g]
        (hit if re.search(pat, s_main) else miss).append(g)
    frac = len(hit) / len(G)
    f2 = frac < 0.5
    L.append("F2  sensitivity of the MAIN read, scored on its task-2 section")
    for g in G:
        L.append("    %-16s %s" % (g, "FOUND" if g in hit else "missed"))
    L.append("    |T2 n G| / |G|    : %d/%d = %.2f  (threshold 0.50)"
             % (len(hit), len(G), frac))
    L.append("    -> F2 %s" % ("FIRED - read recorded LOW-SENSITIVITY"
                               if f2 else "did not fire"))
    L.append("")

    # ---- VAC: pre-registered vacuity arm (i) ------------------------------
    vac = (v_main == v_ctrl)
    L.append("VAC PREREG section 4 arm (i): fires if both reads return the")
    L.append("    SAME verdict")
    L.append("    main = %s" % v_main)
    L.append("    ctrl = %s" % v_ctrl)
    L.append("    -> VAC %s" % ("FIRED" if vac else "did not fire"))
    L.append("")
    if vac:
        L.append("    NOTE, recorded and NOT adjusted. Arm (i) was written on")
        L.append("    the assumption that the packet would come back")
        L.append("    SELF-CONTAINED, so it encoded 'different verdicts' as the")
        L.append("    signal that the instrument reads its input. It cannot")
        L.append("    distinguish an insensitive instrument from two documents")
        L.append("    that are both genuinely not self-contained. As written it")
        L.append("    is ILL-POSED. Per P0 this is reported as a finding; the")
        L.append("    criterion is not rewritten to fit the outcome. The")
        L.append("    surviving discrimination evidence is F1 and F2, both")
        L.append("    pre-registered and both independent of the verdict, plus")
        L.append("    the task-2 item counts above.")
        L.append("")

    L.append("DISPOSITION")
    if f1:
        L.append("  Instrument VOID. No verdict may be read off the main return.")
    elif f2:
        L.append("  Main read recorded LOW-SENSITIVITY; its verdict carries no")
        L.append("  weight, though its individual findings may still be checked.")
    else:
        L.append("  Instrument discriminates (F1 clear) and the main read is")
        L.append("  sensitive (F2 clear, %d/%d). Its CONTENT is admissible as"
                 % (len(hit), len(G)))
        L.append("  evidence. Its VERDICT is weakened by VAC firing and is")
        L.append("  reported with that qualification attached.")

    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))
    back = OUT.read_text(encoding="utf-8")
    assert "DISPOSITION" in back, "readback failed"
    print("\nreadback OK; sha256 %s"
          % hashlib.sha256(OUT.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    sys.exit(main())
