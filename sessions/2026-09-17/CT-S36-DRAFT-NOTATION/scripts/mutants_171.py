"""mutants_171.py -- negative controls for check_171.py (CT-S36, task 3).

Each arm copies the session's inputs to a fresh temporary root, damages ONE
thing, runs check_171.py against that root with --root, and requires it to
exit 1 FOR THE STATED REASON.  An arm that merely crashes the script is not a
catch: a traceback echoes the source line, so `reason in out` alone can be true
for a script that never ran a single assertion.  Each arm therefore also
requires that no SyntaxError/NameError/Traceback appears.

Per P0 Amendment E the damage is chosen from outside check_171.py's own anchor
list: arms 1-3 delete whole subsections of section1.tex, named by their prose
heading, not by any anchor string.

check_171.py takes --root, so nothing derived from __file__ has to be
repointed inside the copy.
"""
import pathlib, shutil, subprocess, sys, tempfile, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
CHECK = HERE / "check_171.py"


def build_root(tmp):
    (tmp / "refs").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "section1.tex", tmp / "section1.tex")
    shutil.copy2(ROOT / "refs" / "ct-s23-task2-items.txt",
                 tmp / "refs" / "ct-s23-task2-items.txt")


def drop_subsection(text, heading):
    """Delete the \\subsection whose title is `heading`, up to the next one."""
    start = text.index(r"\subsection{" + heading)
    nxt = text.find(r"\subsection{", start + 10)
    if nxt == -1:
        nxt = len(text)
    return text[:start] + text[nxt:]


ARMS = []


def arm(name, reason):
    def deco(fn):
        ARMS.append((name, reason, fn))
        return fn
    return deco


@arm("M1 monodromy subsection deleted", "anchor 'traces' is ABSENT")
def m1(tmp):
    p = tmp / "section1.tex"
    p.write_text(drop_subsection(p.read_text(encoding="utf-8"),
                                 "Monodromy and trace coordinates"),
                 encoding="utf-8")


@arm("M2 footnote paragraph deleted", "anchor 'footnote' is ABSENT")
def m2(tmp):
    p = tmp / "section1.tex"
    t = p.read_text(encoding="utf-8")
    i = t.index(r"\footnote{%")
    j = t.index("is never one of these three.}", i) + len("is never one of these three.}")
    p.write_text(t[:i] + t[j:], encoding="utf-8")


@arm("M3 Katz subsection deleted", "anchor 'multiset' is ABSENT")
def m3(tmp):
    p = tmp / "section1.tex"
    p.write_text(drop_subsection(p.read_text(encoding="utf-8"),
                                 "Katz invariants and the classification table"),
                 encoding="utf-8")


@arm("M4 hypothesis (A2) removed", "task-required definitions absent")
def m4(tmp):
    p = tmp / "section1.tex"
    t = p.read_text(encoding="utf-8")
    i = t.index(r"\item[\textbf{(A2)}]")
    j = t.index(r"\item[\textbf{(A3)}]")
    p.write_text(t[:i] + t[j:], encoding="utf-8")


@arm("M5 section 1 emptied", "READER INTEGRITY FAILED")
def m5(tmp):
    (tmp / "section1.tex").write_text("", encoding="utf-8")


@arm("M6 one item dropped from the 171", "READER INTEGRITY FAILED")
def m6(tmp):
    p = tmp / "refs" / "ct-s23-task2-items.txt"
    lines = p.read_text(encoding="utf-8").splitlines()
    p.write_text("\n".join(lines[:-1]), encoding="utf-8")


@arm("M7 items file decoded as latin-1 (mojibake)", "READER INTEGRITY FAILED")
def m7(tmp):
    p = tmp / "refs" / "ct-s23-task2-items.txt"
    raw = p.read_bytes()
    p.write_bytes(raw.decode("utf-8").encode("latin-1", "replace"))


@arm("M8 control item 054 ruled defined elsewhere",
     "control item 54 not reported STILL UNDEFINED")
def m8(tmp):
    """Damages the RULINGS TABLE, not section 1: exercises the control arm."""
    src = CHECK.read_text(encoding="utf-8")
    src = src.replace(
        '54:(UNDEF,"CONTROL:',
        '54:(ELSE,"CONTROL:')
    (tmp / "check_171_mut.py").write_text(src, encoding="utf-8")


def run(tmp, script):
    r = subprocess.run([sys.executable, str(script), "--root", str(tmp)],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    print("mutants_171.py -- negative controls for check_171.py\n")

    rc, out = run(ROOT, CHECK)
    print("BASELINE (undamaged inputs): exit=%d  %s"
          % (rc, "PASS" if rc == 0 else "FAIL -- baseline must be green"))
    if rc != 0:
        sys.exit(1)

    caught = 0
    for name, reason, fn in ARMS:
        with tempfile.TemporaryDirectory() as td:
            tmp = pathlib.Path(td)
            build_root(tmp)
            fn(tmp)
            script = tmp / "check_171_mut.py"
            if not script.exists():
                script = CHECK
            rc, out = run(tmp, script)
            broke = bool(re.search(r"SyntaxError|NameError|Traceback", out))
            right = reason in out
            ok = (rc == 1) and right and not broke
            caught += ok
            print("  %-46s exit=%d reason=%-5s broke=%-5s -> %s"
                  % (name, rc, right, broke, "CAUGHT" if ok else "MISSED"))
            if not ok:
                print("       expected reason: %r" % reason)

    print("\n%d/%d arms CAUGHT" % (caught, len(ARMS)))
    sys.exit(0 if caught == len(ARMS) else 1)


if __name__ == "__main__":
    main()
