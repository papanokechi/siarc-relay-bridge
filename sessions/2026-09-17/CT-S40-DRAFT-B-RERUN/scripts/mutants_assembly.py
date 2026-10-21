"""mutants_assembly.py -- controls for check_assembly.py (CT-S40).

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


def stage(tmp):
    (tmp / "scripts").mkdir(parents=True)
    (tmp / "refs").mkdir(parents=True)
    (tmp / "outputs" / "build_after").mkdir(parents=True)
    shutil.copy2(HERE / "scripts" / "check_assembly.py", tmp / "scripts")
    for n in ("section3.tex", "section4.tex", "forwardrefs_CDE.tex"):
        shutil.copy2(HERE / n, tmp / n)
    for n in ("section0.tex", "section1.tex", "section2.tex"):
        shutil.copy2(HERE / "refs" / n, tmp / "refs" / n)
    shutil.copy2(HERE / "outputs" / "build_after" / "combined_0to4.log",
                 tmp / "outputs" / "build_after" / "combined_0to4.log")
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
    section that now exists."""
    p = tmp / "forwardrefs_CDE.tex"
    t = p.read_text(encoding="utf-8")
    add = ("\\expandafter\\gdef\\csname r@sec:moduli\\endcsname"
           "{{4}{1}{}{section.4}{}}\n")
    p.write_text(t.replace("\\makeatother", add + "\\makeatother"),
                 encoding="utf-8")


def duplicate_label(tmp):
    p = tmp / "refs" / "section2.tex"
    t = p.read_text(encoding="utf-8")
    assert "\\label{sec:growth}" in t, "STAGING FAILED: sec:growth absent"
    p.write_text(t + "\n\\label{sec:moduli}\n", encoding="utf-8")


def drop_log(tmp):
    (tmp / "outputs" / "build_after" / "combined_0to4.log").unlink()


def inject_warning(tmp):
    p = tmp / "outputs" / "build_after" / "combined_0to4.log"
    t = p.read_text(encoding="utf-8", errors="replace")
    p.write_text(t + "\nLaTeX Warning: Reference `eq:ghost' on page 3 "
                 "undefined on input line 9.\n", encoding="utf-8")


def empty_stub(tmp):
    p = tmp / "forwardrefs_CDE.tex"
    t = p.read_text(encoding="utf-8")
    p.write_text(re.sub(r"\\expandafter.*\n", "", t), encoding="utf-8")


def truncate_sections(tmp):
    for n in ("section0.tex", "section1.tex", "section2.tex"):
        (tmp / "refs" / n).write_text("% emptied\n", encoding="utf-8")
    for n in ("section3.tex", "section4.tex"):
        (tmp / n).write_text("% emptied\n", encoding="utf-8")


ARMS = [
    ("A1 reinstate the sec:local / sec:systems mismatch",
     reinstate_sec_local, 1, ["R1 FIRED", "sec:local", "section0"]),
    ("A2 stub declares a label a drafted section defines",
     stub_overreach, 1, ["R2 FIRED", "sec:moduli", "EXISTING"]),
    ("A3 the same label defined by two sections",
     duplicate_label, 1, ["R2b FIRED", "sec:moduli", "section2"]),
    ("A4 build log removed",
     drop_log, 1, ["R3 FIRED", "no build log"]),
    ("A5 build log carries an undefined reference",
     inject_warning, 1, ["R3 FIRED", "eq:ghost", "undefined"]),
    ("A6 stub emptied of entries (R2 must not pass vacuously)",
     empty_stub, 2, ["READER INTEGRITY FAILED", "vacuously"]),
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
