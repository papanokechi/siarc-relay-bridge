"""mutants_walkthrough.py -- can verify_walkthrough.py actually fire?

CT-S35-CTV17-ITEM6.

MUTANT PROVENANCE (P0 Amendment E).  None of these arms is drawn from the
check's own pattern list.  Each one re-introduces a defect that was ACTUALLY
PRESENT in WALKTHROUGH.md on 2026-09-19 and is recorded in claim S35-19, plus
two further arms taken from the deposit's own history rather than from the
gate's source:

  M1  a check count left behind when checks were added      (real: '13/13')
  M2  a character count belonging to a superseded revision  (real: 54 068)
  M3  an instruction to compare a hash against a constant   (real: 'Expected:')
  M4  a cd into the session the packet was copied FROM      (real: CT-S27)
  M5  a display command that truncates the counts           (real: -Last 12)
  M6  a runnable block naming a script that is not there    (from S35-16's
      FileNotFoundError, not from any list in the gate)

Each arm must be CAUGHT, and caught for the RIGHT REASON -- the named check
must be the one that fails.  An arm that merely makes the gate exit non-zero
does not count: a SyntaxError or a crashed reader also exits non-zero, and a
traceback echoes the source line, which can contain the very string the arm is
looking for.  So every arm is also guarded against the gate having broken.

Writes only into a temp directory.  WALKTHROUGH.md is never modified; the run
asserts its sha256 is unchanged at the end.
"""

import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
WALK = os.path.join(SESSION, "WALKTHROUGH.md")
GATE = os.path.join(HERE, "verify_walkthrough.py")

FAKE_HASH = "0" * 64


def sha256(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# --- the mutations -------------------------------------------------------
# Each returns the mutated text, or None if its anchor is absent (which is
# itself a failure: an arm that cannot apply proves nothing).

def m1_stale_check_count(t):
    # Anchor is the UNBOLDED '21/21' as section 0 actually writes it.  The
    # gate's first version required '**21/21**' and so could not see the one
    # count in the file -- found by this arm, which is the point of drawing
    # mutants from outside the check's own patterns.
    return t.replace("21/21", "19/19", 1) if "21/21" in t else None


def m2_superseded_char_count(t):
    return t.replace("68 303", "54 068") if "68 303" in t else None


def m3_eye_compared_hash(t):
    anchor = "Open `DESCRIPTION-v1.7-rev3.html`."
    if anchor not in t:
        return None
    return t.replace(anchor, "Expected: `%s`.\n\n%s" % (FAKE_HASH, anchor), 1)


def m4_cd_into_origin_session(t):
    old = "cd " + SESSION
    new = "cd " + os.path.join(os.path.dirname(SESSION),
                               "CT-S27-CTV17-DEPOSIT-PREP")
    return t.replace(old, new, 1) if old in t else None


def m5_truncating_display(t):
    old = "preflight_deposit_rev2.py | Select-Object -Last 16"
    return t.replace(old, old.replace("-Last 16", "-Last 4"), 1) \
        if old in t else None


def m6_absent_script(t):
    old = "python scripts\\verify_description.py"
    return t.replace(old, "python scripts\\verify_description_v2.py", 1) \
        if old in t else None


ARMS = [
    ("M1 check count left behind when checks were added", m1_stale_check_count, "W1"),
    ("M2 char count of a superseded revision", m2_superseded_char_count, "W2"),
    ("M3 hash reinstated for comparison by eye", m3_eye_compared_hash, "W3"),
    ("M4 cd into the session the packet was copied from", m4_cd_into_origin_session, "W4"),
    ("M5 display command truncates the counts", m5_truncating_display, "W8"),
    ("M6 runnable block names a script that is absent", m6_absent_script, "W5"),
]


def run_gate_on(path):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", VW_WALK_OVERRIDE=path)
    p = subprocess.run([sys.executable, GATE], capture_output=True, text=True,
                       encoding="utf-8", env=env, cwd=SESSION)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def failing_checks(out):
    return set(re.findall(r"\[FAIL\]\s+(W\d)", out))


def main():
    before = sha256(WALK)
    with open(WALK, "rb") as fh:
        original = fh.read().decode("utf-8")

    tmp = tempfile.mkdtemp(prefix="s35_walk_")
    print("=" * 76)
    print("mutants_walkthrough.py -- 6 arms, none drawn from the gate's own")
    print("  pattern lists; every arm is a defect this packet really had.")
    print("=" * 76)

    # Control: unmutated copy must PASS, or nothing below means anything.
    clean = os.path.join(tmp, "clean.md")
    with open(clean, "wb") as fh:
        fh.write(original.encode("utf-8"))
    rc, out = run_gate_on(clean)
    base_ok = (rc == 0 and not failing_checks(out))
    print("\n  [%s] baseline: unmutated copy passes the gate (rc=%d)"
          % ("PASS" if base_ok else "BROKEN", rc))
    if not base_ok:
        print("  every arm below is meaningless while the baseline fails")

    caught = 0
    print()
    for label, mutate, expect in ARMS:
        mutated = mutate(original)
        if mutated is None:
            print("  %-52s NOT APPLIED -- anchor absent" % label)
            continue
        if mutated == original:
            print("  %-52s NOT APPLIED -- text unchanged" % label)
            continue
        path = os.path.join(tmp, re.sub(r"\W+", "_", label)[:40] + ".md")
        with open(path, "wb") as fh:
            fh.write(mutated.encode("utf-8"))
        rc, out = run_gate_on(path)

        fired = failing_checks(out)
        broke = ("Traceback" in out or "SyntaxError" in out
                 or "NameError" in out)
        right = (rc != 0) and (expect in fired) and not broke
        caught += 1 if right else 0
        print("  %-52s %-7s rc=%d expected %s fired %s%s"
              % (label, "CAUGHT" if right else "MISSED", rc, expect,
                 ",".join(sorted(fired)) or "none",
                 "  [GATE BROKE]" if broke else ""))

    shutil.rmtree(tmp, ignore_errors=True)

    after = sha256(WALK)
    intact = (before == after)
    print("\n" + "=" * 76)
    print("%d/%d arms caught, each by the check that is supposed to catch it"
          % (caught, len(ARMS)))
    print("WALKTHROUGH.md unchanged by the mutant run: %s" % intact)
    print("=" * 76)
    return 0 if (caught == len(ARMS) and intact and base_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
