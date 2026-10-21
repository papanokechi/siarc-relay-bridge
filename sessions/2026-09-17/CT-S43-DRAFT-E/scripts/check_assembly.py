"""check_assembly.py -- cross-section label assembly check (CT-S42, repointed from CT-S41).

Group A's gate and Group B's gate were each green while sections 0 and 2
referenced `sec:local` and section 3 defined `sec:systems`.  Neither could see
it:

  * Group A built sections 0-2 with a stub that DECLARED sec:local, so the
    reference resolved against a label no section defines.  The stub
    manufactured its own target.
  * Group B built sections 3-4, which never reference section 3 from outside,
    so the mismatch had no symptom there either.

The defect is therefore invisible to page counts, to rendered diffs and to
both builds.  It appears only when the sections are assembled, and only if the
stub is forbidden from standing in for a section that EXISTS.

Two rules, both able to fail:

  R1  every \\ref/\\eqref target used by sections 0-8 resolves to a \\label
      defined by sections 0-8, or to a stub entry.
  R2  the stub may declare ONLY labels for sections that do not yet exist.  A
      stub entry whose label is also defined by a drafted section is the
      failure above, and is reported even though the build is green.

R3 reads the real build log and requires zero undefined references, so that a
green source-level analysis cannot disagree with the compiler in silence.
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
SECTION_FILES = [
    ("section0", HERE / "refs" / "section0.tex"),
    ("section1", HERE / "refs" / "section1.tex"),
    ("section2", HERE / "refs" / "section2.tex"),
    ("section3", HERE / "refs" / "section3.tex"),
    ("section4", HERE / "refs" / "section4.tex"),
    ("section5", HERE / "refs" / "section5.tex"),
    ("section6", HERE / "refs" / "section6.tex"),
    ("section7", HERE / "refs" / "section7.tex"),
    ("section8", HERE / "refs" / "section8.tex"),
    ("section9", HERE / "section9.tex"),
    ("section10", HERE / "section10.tex"),
    ("appendixA", HERE / "appendixA.tex"),
    ("appendixB", HERE / "appendixB.tex"),
]
STUB = HERE / "forwardrefs_E.tex"
BUILD_LOG = HERE / "paper.log"

LABEL = re.compile(r"\\label\{([^{}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|Cref|cref)\{([^{}]+)\}")
# Only the \csname r@NAME\endcsname declarations count as stub entries; the
# file's comments mention sec:local deliberately and must not be read as one.
STUB_ENTRY = re.compile(r"r@([^\\]+?)\\endcsname")

MIN_LABELS = 60
MIN_REFS = 40


def read_or_fail(p):
    try:
        return p.read_bytes().decode("utf-8-sig").replace("\r\n", "\n")
    except OSError as e:
        print("READER INTEGRITY FAILED: cannot read %s: %s" % (p, e))
        sys.exit(2)
    except UnicodeDecodeError as e:
        print("READER INTEGRITY FAILED: cannot decode %s: %s" % (p, e))
        sys.exit(2)


def main():
    print("check_assembly (CT-S42, repointed from CT-S41) -- cross-section labels, sections 0-8\n")

    defined, used = {}, {}
    for name, p in SECTION_FILES:
        if not p.exists():
            print("READER INTEGRITY FAILED: %s missing at %s" % (name, p))
            sys.exit(2)
        t = read_or_fail(p)
        for lab in LABEL.findall(t):
            defined.setdefault(lab, []).append(name)
        for r in REF.findall(t):
            used.setdefault(r, set()).add(name)

    # reader integrity as BOUNDS, never fingerprints (S36-09)
    print("[reader integrity]")
    if len(defined) < MIN_LABELS or len(used) < MIN_REFS:
        print("  READER INTEGRITY FAILED: %d labels, %d referenced targets "
              "(bounds: >= %d, >= %d)"
              % (len(defined), len(used), MIN_LABELS, MIN_REFS))
        sys.exit(2)
    print("  %d distinct labels defined, %d distinct targets referenced  OK"
          % (len(defined), len(used)))

    stub_text = read_or_fail(STUB) if STUB.exists() else ""
    stub = set(STUB_ENTRY.findall(stub_text))
    # CT-S43: Group E supplies sec:limits, sec:open and app:methods, which
    # were the stub's three entries, so the stub is retired.  The original
    # guard here refused an EMPTY stub, because with the stub allowed into
    # R1's resolution set an empty parse made R2 pass vacuously.  With the
    # stub gone, R1 no longer consults it at all: every reference must resolve
    # to a real \label.  That is strictly stronger than R1+R2 together, so
    # retiring the stub removes the vacuity rather than creating it.
    if stub:
        print("  %d stub entries parsed: %s"
              % (len(stub), ", ".join(sorted(stub))))
    else:
        print("  stub absent or empty: R1 resolves against real labels only, "
              "which is strictly stronger than the stub-allowed form  OK")

    fails = []

    print("\n[R1 every referenced target resolves]")
    dangling = sorted(t for t in used if t not in defined and t not in stub)
    for t in dangling:
        print("  R1 FIRED: %-22s referenced by %s, defined by NO section and "
              "not in the stub" % (t, ", ".join(sorted(used[t]))))
    if dangling:
        fails.append("R1: %d dangling target(s): %s"
                     % (len(dangling), ", ".join(dangling)))
    else:
        print("  all %d referenced targets resolve  OK" % len(used))

    print("\n[R2 the stub may not stand in for a section that exists]")
    if not stub:
        print("  the stub is retired: every label it carried is now defined "
              "by a section, and R1 above consulted no stub  OK")
    overreach = sorted(s for s in stub if s in defined)
    for s in overreach:
        print("  R2 FIRED: the stub declares %-20s which %s also defines; the "
              "stub is manufacturing a target for an EXISTING section"
              % (s, ", ".join(defined[s])))
    if overreach:
        fails.append("R2: stub overreaches on %s" % ", ".join(overreach))
    else:
        print("  no stub entry collides with a drafted section  OK")

    print("\n[R2b no label is defined twice]")
    dup = sorted(k for k, v in defined.items() if len(v) > 1)
    for k in dup:
        print("  R2b FIRED: %s defined in %s" % (k, ", ".join(defined[k])))
    if dup:
        fails.append("R2b: %d duplicated label(s)" % len(dup))
    else:
        print("  no label defined twice  OK")

    print("\n[R3 the compiler agrees]")
    if not BUILD_LOG.exists():
        print("  R3 FIRED: no build log at %s; a source-level analysis alone "
              "cannot certify the assembly" % BUILD_LOG)
        fails.append("R3: build log absent")
    else:
        log = read_or_fail(BUILD_LOG)
        if "Output written" not in log:
            print("  R3 FIRED: the build produced no output; the log cannot "
                  "certify anything")
            fails.append("R3: build produced no output")
        else:
            warn = [l.strip() for l in log.splitlines()
                    if "Warning" in l and ("undefined" in l
                                           or "multiply" in l)]
            errs = [l.strip() for l in log.splitlines() if l.startswith("!")]
            for l in warn + errs:
                print("  R3 FIRED: " + l[:150])
            if warn or errs:
                fails.append("R3: %d undefined/multiply-defined, %d error(s)"
                             % (len(warn), len(errs)))
            else:
                print("  build log: 0 errors, 0 undefined, 0 multiply-defined "
                      "references  OK")

    print("\n[summary]")
    print("  sections analysed : %d" % len(SECTION_FILES))
    print("  labels defined    : %d" % len(defined))
    print("  targets referenced: %d" % len(used))
    print("  stub entries      : %d" % len(stub))
    print("  failures          : %s" % ("; ".join(fails) if fails else "none"))
    print("VERDICT: %s" % ("PASS" if not fails else "FAIL"))
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
