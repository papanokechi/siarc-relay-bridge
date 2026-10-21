#!/usr/bin/env python3
"""mutants_s38 -- the eight pre-registered control arms (PREREG Part D).

An arm is CAUGHT only when all three hold:
  * the run exits non-zero;
  * its output names the condition the arm was built to exercise;
  * the output contains no Traceback, SyntaxError or NameError.

The third condition matters: a broken script echoes its own source line, so a
traceback can contain the arm's reason string while no assertion ever ran.
Every mutation below is therefore a VALID edit, never a syntax break.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SESS = os.path.dirname(HERE)
PY = sys.executable
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

BROKE = ("Traceback", "SyntaxError", "NameError", "IndentationError")


def run(cmd, cwd=None):
    p = subprocess.run(cmd, cwd=cwd, env=ENV, capture_output=True, text=True)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def judge(name, rc, out, wants):
    broke = [b for b in BROKE if b in out]
    hit = [w for w in wants if w in out]
    ok = rc != 0 and not broke and len(hit) == len(wants)
    print("  %-52s %s" % (name, "CAUGHT" if ok else "MISSED"))
    print("      rc=%s  reason=%s  broke=%s"
          % (rc, len(hit) == len(wants), bool(broke)))
    if not ok:
        for w in wants:
            if w not in out:
                print("      missing expectation: %r" % w)
        if broke:
            print("      script broke: %s" % broke)
        print("      ---- tail ----")
        for l in out.strip().splitlines()[-12:]:
            print("      %s" % l)
    return ok


def clause_failed(out, clause):
    return any(clause in l and "FAIL" in l for l in out.splitlines())


def stage_tree():
    t = tempfile.mkdtemp(prefix="s38m-")
    shutil.copytree(os.path.join(SESS, "scripts"), os.path.join(t, "scripts"))
    shutil.copytree(os.path.join(SESS, "refs"), os.path.join(t, "refs"))
    for f in ("theorem.tex", "section1.tex", "section1_standalone.tex"):
        shutil.copyfile(os.path.join(SESS, f), os.path.join(t, f))
    return t


def driver(t, body):
    p = os.path.join(t, "drv.py")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(body)
    return p


def main():
    print("mutants_s38 -- eight pre-registered arms")
    cp = os.path.join(HERE, "check_proposal.py")
    rd = os.path.join(HERE, "rendered_diff.py")
    caught = 0
    total = 0

    # arm 4's letter is discovered from the index at run time, so that the
    # arm is not merely echoing a constant the checker already knows about.
    sys.path.insert(0, HERE)
    import symbol_index as SI
    by_base, _o, _p, _s = SI.build_index(verbose=False)
    forbidden = set()
    import check_proposal as CP
    for s in (CP.PAINLEVE, CP.EXPONENTS, CP.R_FAMILY, CP.GLYPH_AMBIGUOUS):
        forbidden |= s
    discovered = next(b for b in sorted(by_base)
                      if b.startswith("\\") and b not in forbidden
                      and b not in CP.HOMOGLYPH)
    print("  arm 4 letter discovered from the index at run time: %s"
          % discovered)

    print("\n[arms 1-4: the proposal screen]")
    for name, cand, clause in [
            ("1 proposal uses q            -> clause 2", "q",
             "C2 not a chart coordinate"),
            ("2 proposal uses \\lambda      -> clause 3", "\\lambda",
             "C3 not an exponent letter"),
            ("3 proposal uses r            -> clause 4", "r",
             "C4 not r / \\rinf / r(c)"),
            ("4 proposal uses %-14s -> clause 1" % discovered, discovered,
             "C1 unused in index")]:
        rc, out = run([PY, cp, cand])
        total += 1
        ok = judge(name, rc, out, ["PROPOSAL REJECTED"])
        if ok and not clause_failed(out, clause):
            print("      rejected, but not on %s -- wrong reason" % clause)
            ok = False
            print("  %-52s %s" % ("  -> re-judged", "MISSED"))
        caught += 1 if ok else 0

    print("\n[arms 5-6: the rendered-text equivalence]")
    t5 = stage_tree()
    p = os.path.join(t5, "theorem.tex")
    txt = open(p, encoding="utf-8").read()
    assert "converges" in txt
    open(p, "w", encoding="utf-8", newline="\n").write(
        txt.replace("converges", "diverges", 1))
    rc, out = run([PY, os.path.join(t5, "scripts", "rendered_diff.py")])
    total += 1
    caught += 1 if judge("5 a word of prose also changed", rc, out,
                         ["DIFFERS",
                          "RENDERED TEXT DIFFERS BY MORE THAN THE SYMBOLS"]) \
        else 0

    t6 = stage_tree()
    shutil.copyfile(os.path.join(t6, "refs", "theorem-pre-S38.tex"),
                    os.path.join(t6, "theorem.tex"))
    rc, out = run([PY, os.path.join(t6, "scripts", "rendered_diff.py")])
    total += 1
    caught += 1 if judge("6 rename changed nothing (non-vacuity)", rc, out,
                         ["the rename did not reach the page"]) else 0

    print("\n[arms 7-8: reader integrity and the vacuity pre-check]")
    t7 = stage_tree()
    empty = os.path.join(t7, "empty.tex")
    open(empty, "w").write("")
    rc, out = run([PY, driver(t7, (
        "import sys, pathlib\n"
        "sys.path.insert(0, %r)\n"
        "import symbol_index as SI\n"
        "SI.SOURCES = [(l, pathlib.Path(%r) if l == 'section1.tex' else p,\n"
        "               k, o) for (l, p, k, o) in SI.SOURCES]\n"
        "SI.build_index(verbose=True)\n"
        "print('NO COLLISIONS FOUND')\n") % (HERE, empty))])
    total += 1
    caught += 1 if judge("7 a source emptied -> refuse, not 'no collisions'",
                         rc, out, ["READER INTEGRITY FAILED"]) else 0

    t8 = stage_tree()
    rc, out = run([PY, driver(t8, (
        "import sys\n"
        "sys.path.insert(0, %r)\n"
        "import symbol_index as SI\n"
        "_tex, _pro = SI.scan_tex, SI.scan_prose\n"
        "SI.scan_tex = lambda t: [x for x in _tex(t) if x[1] != 'B']\n"
        "SI.scan_prose = lambda t: [x for x in _pro(t) if x[1] != 'B']\n"
        "SI.build_index(verbose=True)\n") % HERE)])
    total += 1
    caught += 1 if judge("8 B sensitivity control removed", rc, out,
                         ["VACUITY PRE-CHECK FAILED"]) else 0

    for t in (t5, t6, t7, t8):
        shutil.rmtree(t, ignore_errors=True)

    print("\n[verdict]")
    print("  arms CAUGHT : %d/%d" % (caught, total))
    if caught != total:
        print("  VERDICT: CONTROL SUITE FAILED")
        sys.exit(1)
    print("  VERDICT: ALL ARMS CAUGHT FOR THE STATED REASON")
    sys.exit(0)


if __name__ == "__main__":
    main()
