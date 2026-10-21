"""CT-S56 -- control harness for the claims emitter.

Design rules, each of which exists because it was learned the hard way:

  * A0 is a POSITIVE baseline that must WRITE. A harness in which every arm
    refuses looks exactly like a harness in which every arm works.
  * Arms run in a scratch cwd. An arm run in the real session directory would
    overwrite the very claims.jsonl the claims cite.
  * 'Refused for the injected reason' must reject SyntaxError and NameError:
    Python's traceback echoes the offending source line, so a broken script
    prints the arm's own reason string and scores CAUGHT while never running.
  * The real claims.jsonl is hashed before and after and must be byte-identical.
"""
import hashlib
import io
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
EMIT = HERE / "emit_claims_s56.py"
CLAIMS = SESS / "claims.jsonl"
OUT = SESS / "outputs" / "mutants_s56.out.txt"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


# (name, find, replace, expect_write, reason_fragment)
#
# Every negative arm injects a DEFECT INTO THE DATA rather than disabling the
# guard that looks for it. Disabling a guard on correct data proves only that
# the refusal path can be reached; it never shows the guard detects anything.
# The first version of M1 did exactly that and scored MISSED, correctly.
ANCHOR = "    validate(claims)"


def inject(stmt):
    return (ANCHOR, f"    {stmt}\n{ANCHOR}")


ARMS = [
    ("A0 baseline (no mutation)", None, None, True, None),

    ("M1 output_hash is not the hash of its output",
     *inject('claims[0]["output_hash"] = "0" * 64'),
     False, "output_hash"),

    ("M2 a claim cites a script that does not exist",
     *inject('claims[0]["script"] = "scripts/no_such_script.py"'),
     False, "script that does not exist"),

    ("M3 a claim is labelled PROVEN",
     *inject('claims[0]["label"] = "PROVEN"'),
     False, "PROVEN"),

    ("M4 a figure that occurs in no cited output",
     *inject('claims[0]["claim"] += " The measured value was 123456 units."'),
     False, "does not occur anywhere"),

    ("M5 a duplicated claim_id",
     *inject('claims[1]["claim_id"] = claims[0]["claim_id"]'),
     False, "twice"),

    ("M6 an empty claim body",
     *inject('claims[3]["claim"] = "   "'),
     False, "empty claim"),

    ("M7 an invalid epistemic label",
     *inject('claims[2]["label"] = "NOPE"'),
     False, "label"),

    ("M8 a cited output file that does not exist",
     *inject('claims[4]["output_file"] = "outputs_that_are_not_there.txt"'),
     False, "missing output"),
]


def run_arm(name, find, repl, expect_write, reason):
    src = EMIT.read_text(encoding="utf-8")
    mutated = src
    if find is not None:
        if src.count(find) != 1:
            return None, f"pattern occurs {src.count(find)} times, not once"
        mutated = src.replace(find, repl)

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # mirror the layout the emitter expects: scripts/ beside outputs/
        (td / "scripts").mkdir()
        (td / "outputs").mkdir()
        for f in (SESS / "outputs").glob("*.txt"):
            shutil.copy2(f, td / "outputs" / f.name)
        for f in HERE.glob("*.py"):
            shutil.copy2(f, td / "scripts" / f.name)
        # the emitter checks that each cited script exists, relative to SESS
        (td / "revision").mkdir(exist_ok=True)
        (td / "scripts" / "emit_claims_s56.py").write_text(mutated, encoding="utf-8")

        p = subprocess.run(
            [sys.executable, str(td / "scripts" / "emit_claims_s56.py")],
            capture_output=True, text=True, cwd=td, timeout=300)
        out = (p.stdout or "") + (p.stderr or "")
        wrote = (td / "claims.jsonl").exists()
        return (p.returncode, out, wrote), None


def main() -> int:
    before = hashlib.sha256(CLAIMS.read_bytes()).hexdigest()

    say("=" * 74)
    say("CT-S56 -- control harness for emit_claims_s56.py")
    say("=" * 74)
    say("")
    say(f"    claims.jsonl sha256 before : {before}")
    say(f"    arms : {len(ARMS)}  (A0 is a positive baseline that must WRITE)")
    say("")

    caught = 0
    problems = []
    for name, find, repl, expect_write, reason in ARMS:
        res, err = run_arm(name, find, repl, expect_write, reason)
        if err:
            say(f"    [SETUP FAIL] {name}: {err}")
            problems.append(name)
            continue
        rc, out, wrote = res

        broke = ("SyntaxError" in out or "NameError" in out
                 or "IndentationError" in out)
        if expect_write:
            ok = wrote and rc == 0 and not broke
            say(f"    [{'PASS' if ok else 'FAIL'}] {name}")
            say(f"           rc={rc} wrote={wrote} broke={broke}")
            if not ok:
                problems.append(name)
                say(f"           {out.strip()[:200]}")
        else:
            right_reason = (reason is not None and reason in out) and not broke
            ok = (not wrote) and rc == 2 and right_reason
            if ok:
                caught += 1
            say(f"    [{'CAUGHT' if ok else 'MISSED'}] {name}")
            say(f"           rc={rc} wrote={wrote} broke={broke} "
                f"reason_seen={reason in out if reason else None}")
            if not ok:
                problems.append(name)
                say(f"           {out.strip()[:200]}")
    say("")

    after = hashlib.sha256(CLAIMS.read_bytes()).hexdigest()
    say(f"    claims.jsonl sha256 after  : {after}")
    intact = before == after
    say(f"    [{'PASS' if intact else 'FAIL'}] the real claims.jsonl is "
        f"byte-identical after the run")
    say("")
    say(f"    negative arms caught : {caught} / {len(ARMS) - 1}")
    say("")
    say("=" * 74)
    ok = not problems and intact
    say("HARNESS PASS: the baseline writes, every negative arm refuses for its"
        if ok else f"HARNESS FAIL: {len(problems)} problem arm(s)")
    if ok:
        say("own injected reason, and no arm touched the real record.")
    else:
        for p in problems:
            say(f"    - {p}")
    say("=" * 74)

    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
