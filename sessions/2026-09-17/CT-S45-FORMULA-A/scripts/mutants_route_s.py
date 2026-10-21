"""Control arms for route_s.py.

route_s.py reported a sign error in one appendix display.  A check that finds a
defect still has to be shown capable of failing: these arms plant known-wrong
expressions and confirm each is caught, and plant a neutral edit that must NOT
be caught.

Two of the arms attack the READER rather than the appendix: if the transcribed
a(z)/b(z)/c(z) is corrupted, the vacuity pre-checks must HALT (exit 2) rather
than proceed to compare appendix literals against a meaningless baseline.  An
arm that merely crashes the script is not caught -- a traceback echoes the
source line, so 'the reason appeared in the output' is not sufficient.
"""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "route_s.py"

# (name, old, new, expected: "caught" | "clean" | "halt")
ARMS = [
    # --- arms against the appendix literals: must be CAUGHT as DIFFERS ---
    ("A1 E7 residual sign flipped",
     "E7 = -sp.Rational(1, 4) * (q - 1)",
     "E7 = sp.Rational(1, 4) * (q - 1)", "caught"),
    ("A2 E7 coefficient 4p -> 5p",
     "* (4 * p + q ** 2 * t + q ** 2\n                                               - q * t - q)",
     "* (5 * p + q ** 2 * t + q ** 2\n                                               - q * t - q)", "caught"),
    ("A3 E11 digit transposed (4pqt -> 4pqt with q^3 -> q^2)",
     "+ q ** 3 * t ** 2 - q ** 3",
     "+ q ** 2 * t ** 2 - q ** 3", "caught"),
    ("A4 E16 c(0) wrong",
     'check("E16", sp.simplify(c.subs(z, 0)), q / (q - 1))',
     'check("E16", sp.simplify(c.subs(z, 0)), q / (q + 1))', "caught"),
    ("A5 E8 rational point value altered",
     "sp.Rational(-223, 144)", "sp.Rational(-224, 144)", "caught"),

    # --- arms against the READER: must HALT, not merely report DIFFERS ---
    ("A6 transcription of a(z) corrupted (sign of theta_inf)",
     "(-2 * q * t + t - thi)", "(-2 * q * t + t + thi)", "halt"),
    ("A7 transcription of c(z) corrupted",
     "c = -(z - q) / (q - 1)", "c = -(z - q) / (q + 1)", "halt"),

    # --- negative arm: a neutral edit must NOT fire anything ---
    ("A8 neutral edit (comment added)",
     "FAIL = []", "FAIL = []  # neutral", "clean"),
]


def run(text):
    tmp = HERE / "_arm_route_s.py"
    tmp.write_text(text, encoding="utf-8")
    try:
        pr = subprocess.run([sys.executable, str(tmp)],
                            capture_output=True, text=True,
                            encoding="utf-8", cwd=str(HERE.parent))
        return pr.returncode, (pr.stdout or "") + (pr.stderr or "")
    finally:
        tmp.unlink(missing_ok=True)


def main():
    src = SRC.read_text(encoding="utf-8")

    # Positive control: the unmutated script must run to completion and report
    # exactly the one known defect.  If it reports none, or crashes, every
    # "caught" below would be meaningless.
    rc, out = run(src)
    if "Traceback" in out:
        sys.exit("ARM HARNESS FAILED: unmutated script crashed:\n" + out[-2000:])
    if "ROUTE S: 1 of the checked displays DIFFER: E12" not in out:
        sys.exit("ARM HARNESS FAILED: unmutated script did not report the "
                 "known E12 defect; baseline has moved:\n" + out[-2000:])
    print("  [baseline] unmutated script reports exactly E12, rc=%d" % rc)

    caught = skipped = missed = 0
    for name, old, new, expect in ARMS:
        if old not in src:
            print("  SKIPPED  %s (mutation site absent)" % name)
            skipped += 1
            continue
        rc, out = run(src.replace(old, new, 1))
        broke = "Traceback" in out
        if expect == "caught":
            # must report a DIFFERS beyond the known E12, and must not crash
            extra = [ln for ln in out.splitlines()
                     if ln.strip().startswith("DIFFERS")
                     and not ln.strip().endswith("E12")]
            ok = (not broke) and rc == 1 and bool(extra)
        elif expect == "halt":
            ok = (not broke) and rc == 2 and "HALT" in out
        else:  # clean
            ok = (not broke) and rc == 1 and \
                 "ROUTE S: 1 of the checked displays DIFFER: E12" in out
        print("  %s  %-52s (expect %s, rc=%d%s)"
              % ("CAUGHT " if ok else "MISSED ", name, expect, rc,
                 ", CRASHED" if broke else ""))
        caught += 1 if ok else 0
        missed += 0 if ok else 1

    print("%d CAUGHT, %d SKIPPED, %d MISSED of %d arms"
          % (caught, skipped, missed, len(ARMS)))
    return 0 if (missed == 0 and skipped == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
