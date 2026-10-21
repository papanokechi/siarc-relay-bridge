"""Mutants on the checker, to prove the controls in verify_rulings.py can fail.

20/20 controls passing on the first run is not evidence the controls work.
Each arm loosens the checker in exactly the way one ruling forbids, runs the
control harness against the loosened copy, and requires three things together:

  1. the harness REFUSED (non-zero exit), and
  2. it refused FOR THE INJECTED REASON (the named control failed), not
     because the mutated source would not parse, and
  3. the real checker is byte-identical afterwards.

Condition 2 needs the broke_script guard: a SyntaxError traceback echoes the
mutated source line, so a bare substring test for the reason can match a
script that never executed a single assertion.
"""
import hashlib
import io
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
CHECKER = HERE.parent / "CT-R1-AUDIT" / "check_invariants.py"
HARNESS = HERE / "scripts" / "verify_rulings.py"
SRC = CHECKER.read_text(encoding="utf-8")
BEFORE = hashlib.sha256(CHECKER.read_bytes()).hexdigest()

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


# each arm: (name, old, new, the control text it must break)
ARMS = [
    ("M1  cutoff moved one day later, hiding a claim that should be judged",
     'CONVENTION_DATE = "2026-09-17"', 'CONVENTION_DATE = "2026-09-18"',
     "a claim dated ON the cutoff is in scope"),
    ("M2  counter pattern widened to any id, disabling 1(b)(i) wholesale",
     r'SESSION_LOCAL_ID = re.compile(r"^(?:\d+-)?C\d+$")',
     r'SESSION_LOCAL_ID = re.compile(r"^.*$")',
     "a genuine global collision still FAILS 1(b)(i)"),
    ("M3  within-session duplicate threshold raised, disabling 1(b)(ii)",
     "        if n > 1:\n            local_dups.append((cid, f, n))",
     "        if n > 99:\n            local_dups.append((cid, f, n))",
     "a session-local counter reused WITHIN one session FAILS 1(b)(ii)"),
    ("M4  mirror pattern unanchored, so any path containing 'mirror' matches",
     r'MIRROR_PATH = re.compile(r"[\\/]deposit[\\/]")',
     r'MIRROR_PATH = re.compile(r"deposit|mirror")',
     "a mirror NOT at the deposit path is still reported"),
    ("M5  identical claim text accepted as an exemption -- the loosening the "
     "ruling forbids",
     "    matched = [str(p) for p in paths if MIRROR_PATH.search(str(p))]",
     "    matched = [str(p) for p in paths if MIRROR_PATH.search(str(p))] or "
     "([str(paths[0])] if len({b for _, _, b in occ}) == 1 else [])",
     "a mirror NOT at the deposit path is still reported"),
    ("M6  known-hole list turned into a blanket amnesty for any damage",
     'mark = "KNOWN HOLE" if key else "NEW DAMAGE"',
     'mark = "KNOWN HOLE"',
     "reported as NEW DAMAGE, not absorbed"),
    ("M7  idless claims fall silent instead of getting their own line",
     "        idless.append((p, lineno))",
     "        idless.extend([])",
     "an idless claim gets its own printed line"),
]

say("=" * 78)
say("CT-S34  mutants on the checker  (θ, ∞ sentinels)")
say("=" * 78)
say("checker sha256 before: %s" % BEFORE)
say("harness              : %s" % HARNESS.name)
say()

missing = [a[0] for a in ARMS if a[1] not in SRC]
assert not missing, "mutation target absent, arm cannot fire: %r" % missing

caught = 0
for name, old, new, must_break in ARMS:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        # mutate a COPY of the checker, and point a copy of the harness at it
        mc = tmp / "check_invariants.py"
        mc.write_text(SRC.replace(old, new), encoding="utf-8")
        mh = tmp / "verify_rulings.py"
        h = HARNESS.read_text(encoding="utf-8")
        h = h.replace(
            "HERE = pathlib.Path(__file__).resolve().parents[1]",
            "HERE = pathlib.Path(r%r)" % str(HERE))
        h = h.replace(
            'CHECKER = HERE.parent / "CT-R1-AUDIT" / "check_invariants.py"',
            "CHECKER = pathlib.Path(r%r)" % str(mc))
        # the harness writes its own output; send that to the temp dir too
        h = h.replace('OUT = HERE / "outputs" / "verify_rulings.out.txt"',
                      "OUT = pathlib.Path(r%r)" % str(tmp / "o.txt"))
        mh.write_text(h, encoding="utf-8")
        r = subprocess.run([sys.executable, str(mh)], capture_output=True,
                           text=True, encoding="utf-8", errors="replace",
                           cwd=str(tmp))
        out = (r.stdout or "") + (r.stderr or "")

    refused = r.returncode != 0
    # A traceback that is NOT an AssertionError means the harness died before
    # judging anything; its output can still echo the injected reason.
    broke = ("Traceback" in out and "AssertionError" in out
             and out.count("Traceback") > 1) or (
        "Traceback" in out and "AssertionError" not in out)
    right = ("CONTROL FAILED" in out and must_break in out and not broke)
    verdict = "CAUGHT" if (refused and right) else "MISSED"
    caught += verdict == "CAUGHT"
    say("%-6s %s" % (verdict, name))
    say("       refused=%s  right_reason=%s  broke_script=%s"
        % (refused, right, broke))
    if verdict == "MISSED":
        say("       ---- last output ----")
        for ln in out.strip().splitlines()[-6:]:
            say("       " + ln)

after = hashlib.sha256(CHECKER.read_bytes()).hexdigest()
say()
say("checker sha256 after : %s" % after)
say("byte-identical       : %s" % (after == BEFORE))
say("ARMS: %d/%d CAUGHT" % (caught, len(ARMS)))

assert after == BEFORE, "a mutant arm wrote to the real checker"
assert caught == len(ARMS), "an arm was MISSED: the controls cannot fail"

OUT = HERE / "outputs" / "mutants.out.txt"
blob = BUF.getvalue().encode("utf-8")
assert b"\r" not in blob
OUT.write_bytes(blob)
raw = OUT.read_bytes()
assert raw == blob
assert "θ" in raw.decode("utf-8") and "∞" in raw.decode("utf-8")
assert "θ" not in raw.decode("latin-1")
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
