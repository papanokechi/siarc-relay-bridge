"""mutants_draft_check.py -- controls for draft_check.py (CT-S37-DRAFT-B).

Each arm mutates a COPY of the drafted prose and requires draft_check.py to
refuse.  An arm is CAUGHT only if all three hold:

  * the checker exits with the expected non-zero code (or 0 for the alias arm);
  * the output names the mutated claim id and the expected verdict word
    ("for the stated reason");
  * the output contains no Traceback / SyntaxError / NameError, so that a
    checker which simply crashed is never scored as having caught anything.

The copied tree has claim_index.ROOT PINNED to the real sessions directory.
Without that pin, __file__-derived paths resolve into the temp directory and
every arm dies before judging anything.
"""
import pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent.parent
SESSIONS = HERE.parents[1]
assert SESSIONS.name == "sessions", SESSIONS

ROOT_BLOCK = re.compile(
    r"ROOT = pathlib\.Path\(__file__\).*?parents\[2\]", re.S)


def stage(tmp):
    (tmp / "scripts").mkdir(parents=True)
    for n in ("draft_check.py", "claim_index.py"):
        shutil.copy2(HERE / "scripts" / n, tmp / "scripts" / n)
    for n in ("section3.tex", "section4.tex"):
        shutil.copy2(HERE / n, tmp / n)
    ci = tmp / "scripts" / "claim_index.py"
    src = ci.read_text(encoding="utf-8")
    pinned = 'ROOT = pathlib.Path(r"%s")' % SESSIONS
    assert ROOT_BLOCK.search(src), "PIN FAILED: ROOT block not found"
    src2 = ROOT_BLOCK.sub(lambda m: pinned, src, count=1)
    assert pinned in src2, "PIN FAILED: claim_index.ROOT was not repointed"
    ci.write_text(src2, encoding="utf-8")
    return tmp


def run(tmp):
    r = subprocess.run([sys.executable, str(tmp / "scripts" / "draft_check.py")],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def insert_label(text, cid, label, nth=0):
    needle = "\\texttt{%s}" % cid
    idx, seen = -1, -1
    while seen < nth:
        idx = text.find(needle, idx + 1)
        assert idx >= 0, "citation %s occurrence %d not found" % (cid, nth)
        seen += 1
    return text[:idx] + "\\textbf{%s}" % label + text[idx:]


def replace_cite(text, old, new, nth=0):
    a, b = "\\texttt{%s}" % old, "\\texttt{%s}" % new
    idx, seen = -1, -1
    while seen < nth:
        idx = text.find(a, idx + 1)
        assert idx >= 0, "citation %s not found" % old
        seen += 1
    return text[:idx] + b + text[idx + len(a):]


# ---- arms: (name, file, mutate(text)->text, expected_rc, required_words) ----
ARMS = [
    ("M1 S4-03 PROVEN -> CONJECTURED", "section3.tex",
     lambda t: insert_label(t, "S4-03", "CONJECTURED"), 1,
     ["S4-03", "MISMATCH", "CONJECTURED"]),
    ("M2 S16-01 INSPECTED -> PROVEN (forbidden upgrade)", "section4.tex",
     lambda t: insert_label(t, "S16-01", "PROVEN"), 1,
     ["S16-01", "MISMATCH", "PROVEN"]),
    ("M3 S6-C16 STRUCTURAL -> VERIFIED", "section3.tex",
     lambda t: insert_label(t, "S6-C16", "VERIFIED"), 1,
     ["S6-C16", "MISMATCH", "VERIFIED"]),
    ("M4 S16-04 STRUCTURAL -> INSPECTED", "section4.tex",
     lambda t: insert_label(t, "S16-04", "INSPECTED"), 1,
     ["S16-04", "MISMATCH", "INSPECTED"]),
    ("M5 cite a claim id that does not exist", "section3.tex",
     lambda t: replace_cite(t, "S4-03", "S4-99"), 1,
     ["S4-99", "UNRESOLVED"]),
    ("M6 cite a structurally superseded claim", "section3.tex",
     lambda t: replace_cite(t, "S4-03", "S21-26"), 1,
     ["S21-26", "SUPERSEDED"]),
    ("M7 alias form S9-PVPARAMS-C005 must resolve AND be reported", "section3.tex",
     lambda t: replace_cite(t, "CT-S9-PVPARAMS-C005", "S9-PVPARAMS-C005"), 0,
     ["S9-PVPARAMS-C005", "alias"]),
    ("M8 reader integrity: section3.tex emptied", "section3.tex",
     lambda t: "", 2,
     ["READER INTEGRITY FAILED", "section3.tex"]),
    ("M9 boundary: section4.tex reduced to 4 citations", "section4.tex",
     None, 2,
     ["READER INTEGRITY FAILED", "section4.tex", "pairs"]),
]

CID = re.compile(r"\\texttt\{((?:CT-)?S\d+[A-Z]*(?:-[A-Z0-9]+)+)\}")


def m9(text):
    """Keep the first four citations, neutralise the rest.  Bytes and
    subsection count are left untouched, so ONLY the pair bound can fire."""
    n = [0]

    def sub(m):
        n[0] += 1
        return m.group(0) if n[0] <= 4 else "\\texttt{see the text above}"
    return CID.sub(sub, text)


ARMS[8] = (ARMS[8][0], ARMS[8][1], m9, ARMS[8][3], ARMS[8][4])


def main():
    caught = 0
    print("mutants_draft_check -- %d arms\n" % len(ARMS))
    for name, fname, mutate, exp_rc, words in ARMS:
        with tempfile.TemporaryDirectory() as td:
            tmp = stage(pathlib.Path(td) / "work")
            p = tmp / fname
            p.write_text(mutate(p.read_text(encoding="utf-8")), encoding="utf-8")
            rc, out = run(tmp)
        broke = any(w in out for w in ("Traceback", "SyntaxError", "NameError"))
        missing = [w for w in words if w not in out]
        ok = (rc == exp_rc) and not missing and not broke
        caught += ok
        print("  %-52s rc=%s exp=%s %s" % (name, rc, exp_rc,
                                           "CAUGHT" if ok else "MISSED"))
        if not ok:
            if broke:
                print("      checker CRASHED; not scored as caught")
                print("      " + out.strip().splitlines()[-1][:160])
            if missing:
                print("      output did not name: %s" % ", ".join(missing))
            if rc != exp_rc:
                print("      unexpected exit code")
    print("\n%d/%d arms CAUGHT" % (caught, len(ARMS)))
    sys.exit(0 if caught == len(ARMS) else 1)


if __name__ == "__main__":
    main()
