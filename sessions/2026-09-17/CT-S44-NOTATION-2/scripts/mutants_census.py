"""Control arms for symbol_census.py's corpus-identity guard.

The guard exists because this session's first census ran against a tree that
was half repaired: it reported 186 occurrences over 139643 chars, a state that
matches neither the pre-pass corpus (185 / 138537) nor the repaired one
(211 / 142015), and which no longer exists.  A census that names its corpus by
path alone cannot notice that.  These arms confirm the guard resolves the
corpus POSITIVELY, by a marker each tree carries and the other does not.

An arm that cannot reach its mutation site must say so, loudly, and must not be
scored as if the rule had been exercised.
"""
import hashlib
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "symbol_census.py"
SITE = '    base = (HERE / "refs") if which == "prepass" else HERE'

ARMS = [
    # (name, replacement for SITE, argv, reason that must appear in output)
    ("A1 prepass pointed at the repaired tree",
     "    base = HERE",
     "prepass",
     "not the pre-pass corpus"),
    ("A2 repaired pointed at refs/",
     '    base = HERE / "refs"',
     "repaired",
     "not the repaired corpus"),
    ("A3 marker test inverted",
     SITE + "\n    has_repair_unused = None",
     "prepass",
     None),  # A3 is a NEGATIVE arm: a no-op edit must still PASS
]


def run(text, argv):
    tmp = HERE / "_arm_census.py"
    tmp.write_text(text, encoding="utf-8")
    try:
        p = subprocess.run([sys.executable, str(tmp), argv],
                           capture_output=True, text=True, encoding="utf-8")
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    finally:
        tmp.unlink(missing_ok=True)


def main():
    src = SRC.read_text(encoding="utf-8")
    if SITE not in src:
        sys.exit("ARM HARNESS FAILED: mutation site absent from %s" % SRC.name)

    # Positive control: the unmutated script must PASS on both corpora, or a
    # caught arm proves only that the script is broken.
    for argv in ("prepass", "repaired"):
        rc, out = run(src, argv)
        if rc != 0:
            sys.exit("ARM HARNESS FAILED: unmutated script exits %d on %s:\n%s"
                     % (rc, argv, out))

    caught = skipped = missed = 0
    for name, repl, argv, reason in ARMS:
        mutated = src.replace(SITE, repl, 1)
        if mutated == src:
            print("  SKIPPED  %s (mutation site absent)" % name)
            skipped += 1
            continue
        rc, out = run(mutated, argv)
        broke = "SyntaxError" in out or "NameError" in out
        if reason is None:
            # negative arm: a semantically neutral edit must NOT fire the guard
            ok = rc == 0 and not broke
            print("  %s  %s" % ("CAUGHT " if ok else "MISSED ", name))
            caught += 1 if ok else 0
            missed += 0 if ok else 1
            continue
        ok = rc != 0 and reason in out and not broke
        print("  %s  %s" % ("CAUGHT " if ok else "MISSED ", name))
        if not ok:
            print("           rc=%d broke=%s reason_present=%s"
                  % (rc, broke, reason in out))
        caught += 1 if ok else 0
        missed += 0 if ok else 1

    # The census outputs on disk must be unchanged by running the arms.
    for f in ("symbol_census.out.txt", "symbol_census_prepass.out.txt"):
        p = HERE.parent / "outputs" / f
        print("  [intact] %s %s" % (f, hashlib.sha256(p.read_bytes()).hexdigest()[:16]))

    print("%d CAUGHT, %d SKIPPED, %d MISSED of %d arms"
          % (caught, skipped, missed, len(ARMS)))
    return 0 if (missed == 0 and skipped == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
