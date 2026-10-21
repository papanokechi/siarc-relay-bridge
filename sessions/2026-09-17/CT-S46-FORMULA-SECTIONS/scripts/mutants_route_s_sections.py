"""Control arms for route_s_sections.py.

Three expectation kinds:
  caught  -- the mutated paper value must be reported DIFFERS (exit 1)
  halt    -- the mutated reader must refuse (exit 2 / READER FAILED), never
             render a verdict
  clean   -- a semantically neutral edit must NOT fire anything (exit 0)

A crash never scores as caught: a traceback echoes the offending source line,
so the arm's own marker string can appear in the output of a script that never
executed a single check. `broke` guards against exactly that.
"""
import pathlib
import subprocess
import tempfile
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "route_s_sections.py"
TMP = HERE / "_mutant_route_s_sections.py"
ORIG = SRC.read_text(encoding="utf-8")

ARMS = [
    # --- paper-value mutations: the defect class under test -----------------
    ("M1 eq:rA numerator 3 -> 2",
     "rA_displayed = (-3 * z ** 2 - 5 * z + 3) / (9 * z ** 3)",
     "rA_displayed = (-3 * z ** 2 - 5 * z + 2) / (9 * z ** 3)",
     "caught", "A1 eq:rA"),

    ("M2 eq:QC constant 5 -> 6",
     "QC_displayed = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "                + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "QC_displayed = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "                + 6 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "caught", "S5 eq:QC"),

    # the Appendix A defect class: a sign copied across without its flip
    ("M3 eq:QC sign +i sqrt11 -> -i sqrt11",
     "                + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "                + 5 - sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "caught", "S5 eq:QC"),

    ("M4 eq:QC denominator 54 -> 45 (transposed)",
     "QC_displayed = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "                + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "QC_displayed = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "                + 5 + sp.I * sp.sqrt(11)) / (45 * z * (z - 1))",
     "caught", "S5 eq:QC"),

    ("M5 eq:rC constant 11 -> 111",
     "rC_displayed = (12 * x ** 4 + 4 * x ** 3 + 4 * x ** 2 + 11) "
     "/ (4 * aC ** 2)",
     "rC_displayed = (12 * x ** 4 + 4 * x ** 3 + 4 * x ** 2 + 111) "
     "/ (4 * aC ** 2)",
     "caught", "C1 eq:rC"),

    ("M6 eq:spm sqrt11 -> sqrt13",
     "spm_plus = (-1 + sp.I * sp.sqrt(11)) / 6",
     "spm_plus = (-1 + sp.I * sp.sqrt(13)) / 6",
     "caught", "eq:spm"),

    ("M7 eliminant 108 -> 180 (transposed)",
     "eliminant = 27 * thi ** 2 + 108 * thi + 107",
     "eliminant = 27 * thi ** 2 + 180 * thi + 107",
     "caught", "eq:eliminant"),

    ("M8 eq:PC 2z-1 -> 2z+1",
     "PC_displayed = (2 * z - 1) / (z * (z - 1))",
     "PC_displayed = (2 * z + 1) / (z * (z - 1))",
     "caught", "eq:PC"),

    # --- reader attacks: the instrument must refuse, not conclude ----------
    ("M9 baseline corrupted -> V3 must refuse",
     "_rA_disp = (-3 * z ** 2 - 5 * z + 3) / (9 * z ** 3)",
     "_rA_disp = (-3 * z ** 2 - 5 * z + 4) / (9 * z ** 3)",
     "halt", "VACUITY V3 FAILED"),

    ("M10 residual always zero -> V1 must refuse",
     "def _resid(a, b):\n    return sp.simplify(sp.together(sp.expand(a - b)))",
     "def _resid(a, b):\n    return sp.Integer(0)",
     "halt", "VACUITY"),

    ("M11 X2 reader blinded -> must refuse",
     "bogus = sp.simplify(-3 / (sp.sqrt(3) * sp.sqrt(zp)))",
     "bogus = sp.simplify(-2 / (sp.sqrt(3) * sp.sqrt(zp)))",
     "halt", "READER FAILED"),

    # --- negative arm: a neutral edit must NOT fire ------------------------
    ("M12 comment reworded (neutral)",
     "# ---------------------------------------------------------------------------\n"
     'say("[5] Section 5: eq:eliminant")',
     "# ---- section five ----\n"
     'say("[5] Section 5: eq:eliminant")',
     "clean", ""),
    # --- restatement arm: section 9 reprints eq:QC; if the two printings
    # --- disagree that is CT-S45's Appendix A defect, across two sections
    ("M13 sec9 reprint of eq:QC altered",
     "QC_sec9 = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "           + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z - 1))",
     "QC_sec9 = (22 * z ** 2 - 22 * z - 2 * sp.I * sp.sqrt(11) * z\n"
     "           + 5 + sp.I * sp.sqrt(11)) / (54 * z * (z + 1))",
     "caught", "R2 eq:QC == sec9 L39"),

    ("M14 sec9 reprint of P_C altered",
     "PC_sec9 = (2 * z - 1) / (z * (z - 1))",
     "PC_sec9 = (2 * z - 1) / (z * (z - 2))",
     "caught", "R1 eq:PC == sec9 L39"),
]


def run(text):
    """Run a (possibly mutated) copy of the script in a SCRATCH directory.

    This matters, and it was a real defect: the harness first ran each mutant
    with cwd set to the session root, so every mutant overwrote
    outputs/route_s_sections.out.txt -- the exact file the claims cite by
    digest. After a full gate run the surviving artefact was the LAST ARM's
    output, reporting a display DIFFERS that does not. It was caught only
    because the emitter re-reads its evidence and refused to write.

    A control harness must not be able to touch the evidence it is a control
    for.
    """
    TMP.write_text(text, encoding="utf-8")
    with tempfile.TemporaryDirectory() as scratch:
        (pathlib.Path(scratch) / "outputs").mkdir()
        r = subprocess.run([sys.executable, str(TMP)], capture_output=True,
                           text=True, cwd=scratch)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


print("=" * 74)
print("CONTROL ARMS -- route_s_sections.py")
print("=" * 74)

base_rc, base_out = run(ORIG)
print("baseline: exit %d, %s" % (
    base_rc, "all checked displays match" if base_rc == 0 else "NOT CLEAN"))
if base_rc != 0 or "checked displays match" not in base_out:
    TMP.unlink(missing_ok=True)
    sys.exit("BASELINE FAILED: arms cannot be interpreted against it")
print()

results = []
for name, old, new, expect, marker in ARMS:
    if old not in ORIG:
        results.append((name, "SKIPPED (mutation site absent)", expect))
        print("  %-44s SKIPPED (mutation site absent)" % name)
        continue
    if ORIG.count(old) != 1:
        results.append((name, "SKIPPED (mutation site not unique)", expect))
        print("  %-44s SKIPPED (not unique)" % name)
        continue
    rc, out = run(ORIG.replace(old, new))
    broke = "Traceback" in out or "SyntaxError" in out or "NameError" in out
    if expect == "caught":
        ok = (rc == 1) and ("DIFFERS" in out) and (marker in out) and not broke
    elif expect == "halt":
        ok = (rc not in (0, 1)) and (marker in out) and not broke
    else:  # clean
        ok = (rc == 0) and ("DIFFERS" not in out) and not broke
    verdict = ("CAUGHT" if expect != "clean" else "CLEAN") if ok else "MISSED"
    if broke:
        verdict += " (script crashed -- not a detection)"
    results.append((name, verdict, expect))
    print("  %-44s %-8s %s" % (name, verdict, "expect=" + expect))

TMP.unlink(missing_ok=True)

good = sum(1 for _, v, _ in results if v in ("CAUGHT", "CLEAN"))
print()
print("=" * 74)
print("ARMS: %d/%d as expected" % (good, len(results)))
print("=" * 74)

with open(HERE.parent / "outputs" / "mutants_route_s_sections.out.txt", "w",
          encoding="utf-8") as fh:
    fh.write("ARMS: %d/%d as expected\n" % (good, len(results)))
    for name, v, e in results:
        fh.write("  %-44s %-8s expect=%s\n" % (name, v, e))

sys.exit(0 if good == len(results) else 1)
