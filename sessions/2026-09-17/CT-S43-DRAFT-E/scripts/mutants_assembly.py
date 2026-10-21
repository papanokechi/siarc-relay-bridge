"""mutants_assembly.py -- controls for check_assembly.py (CT-S41, repointed from CT-S40).

Each arm mutates a COPY of the assembly and requires check_assembly.py to
refuse.  An arm is CAUGHT only if all three hold:

  * the expected exit code;
  * the output names the expected rule AND the mutated object, so an arm can
    never be scored on a refusal for some other reason;
  * no Traceback / SyntaxError / NameError, so a script that merely crashed is
    never counted as having caught anything.

A1 is the arm that matters: it reinstates the exact defect this session found,
and it is the only arm whose absence would have let the defect through again.
A2 is its cause -- a stub standing in for a section that exists.
"""
import pathlib, re, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent.parent


ROOT_TEX = ("section9.tex", "section10.tex", "appendixA.tex", "appendixB.tex")
REFS_TEX = tuple("section%d.tex" % i for i in range(9))
BUILD_LOG = "paper.log"


def stage(tmp):
    (tmp / "scripts").mkdir(parents=True)
    (tmp / "refs").mkdir(parents=True)
    (tmp / "outputs" / "build").mkdir(parents=True)
    shutil.copy2(HERE / "scripts" / "check_assembly.py", tmp / "scripts")
    for n in ROOT_TEX:
        shutil.copy2(HERE / n, tmp / n)
    for n in REFS_TEX:
        shutil.copy2(HERE / "refs" / n, tmp / "refs" / n)
    if (HERE / "forwardrefs_E.tex").exists():
        shutil.copy2(HERE / "forwardrefs_E.tex", tmp / "forwardrefs_E.tex")
    shutil.copy2(HERE / BUILD_LOG, tmp / BUILD_LOG)
    return tmp


def run(tmp):
    r = subprocess.run(
        [sys.executable, str(tmp / "scripts" / "check_assembly.py")],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def reinstate_sec_local(tmp):
    p = tmp / "refs" / "section0.tex"
    t = p.read_text(encoding="utf-8")
    assert "{sec:systems}" in t, "STAGING FAILED: no sec:systems to revert"
    p.write_text(t.replace("{sec:systems}", "{sec:local}", 1),
                 encoding="utf-8")


def stub_overreach(tmp):
    """Exactly what CT-S39's forwardrefs.tex did: declare a label for a
    section that now exists.  The stub is retired in CT-S43, so this arm
    RE-CREATES it; a rule that is only non-vacuous while its input exists
    would otherwise pass by the input's disappearance."""
    p = tmp / "forwardrefs_E.tex"
    add = ("\\makeatletter\n"
           "\\expandafter\\gdef\\csname r@sec:point\\endcsname"
           "{{5}{1}{}{section.5}{}}\n\\makeatother\n")
    p.write_text(add, encoding="utf-8")


def dangling_ref(tmp):
    """The replacement for the retired A6.  With the stub gone, R1 has no
    escape hatch: a reference to a label no section defines must fire, and
    nothing can stand in for it."""
    p = tmp / "refs" / "section7.tex"
    t = p.read_text(encoding="utf-8")
    assert "\\ref{app:methods}" in t, "STAGING FAILED: no app:methods ref"
    p.write_text(t.replace("\\ref{app:methods}", "\\ref{app:ghost}", 1),
                 encoding="utf-8")


def duplicate_label(tmp):
    p = tmp / "refs" / "section2.tex"
    t = p.read_text(encoding="utf-8")
    assert "\\label{sec:growth}" in t, "STAGING FAILED: sec:growth absent"
    p.write_text(t + "\n\\label{sec:point}\n", encoding="utf-8")


def drop_log(tmp):
    (tmp / BUILD_LOG).unlink()


def inject_warning(tmp):
    p = tmp / BUILD_LOG
    t = p.read_text(encoding="utf-8", errors="replace")
    p.write_text(t + "\nLaTeX Warning: Reference `eq:ghost' on page 3 "
                 "undefined on input line 9.\n", encoding="utf-8")


def truncate_sections(tmp):
    for n in REFS_TEX:
        (tmp / "refs" / n).write_text("% emptied\n", encoding="utf-8")
    for n in ROOT_TEX:
        (tmp / n).write_text("% emptied\n", encoding="utf-8")


ARMS = [
    ("A1 reinstate the sec:local / sec:systems mismatch",
     reinstate_sec_local, 1, ["R1 FIRED", "sec:local", "section0"]),
    ("A2 re-created stub declares a label a section defines",
     stub_overreach, 1, ["R2 FIRED", "sec:point", "EXISTING"]),
    ("A3 the same label defined by two sections",
     duplicate_label, 1, ["R2b FIRED", "sec:point", "section2"]),
    ("A4 build log removed",
     drop_log, 1, ["R3 FIRED", "no build log"]),
    ("A5 build log carries an undefined reference",
     inject_warning, 1, ["R3 FIRED", "eq:ghost", "undefined"]),
    ("A6 forward ref with no section and no stub to cover it",
     dangling_ref, 1, ["R1 FIRED", "app:ghost", "section7"]),
    ("A7 all sections emptied (bounds, not fingerprints)",
     truncate_sections, 2, ["READER INTEGRITY FAILED", "bounds"]),
]


def main():
    caught = 0
    print("mutants_assembly -- %d arms\n" % len(ARMS))
    for name, mutate, exp_rc, words in ARMS:
        with tempfile.TemporaryDirectory() as td:
            tmp = stage(pathlib.Path(td) / "work")
            mutate(tmp)
            rc, out = run(tmp)
        broke = any(w in out for w in ("Traceback", "SyntaxError", "NameError"))
        missing = [w for w in words if w not in out]
        ok = (rc == exp_rc) and not missing and not broke
        caught += ok
        print("  %-52s rc=%s exp=%s %s"
              % (name, rc, exp_rc, "CAUGHT" if ok else "MISSED"))
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
