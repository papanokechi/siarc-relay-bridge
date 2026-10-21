#!/usr/bin/env python3
"""CT-S58: control harness for emit_claims_s58.py.

A harness in which every arm refuses looks identical to one in which every arm
works. A0 is a positive baseline that must WRITE; only then does a refusal in
M1..M6 mean anything.

Every arm runs in a scratch tree. Running mutants in the real session
directory would overwrite the very claims.jsonl the record depends on.

Exit codes: 0 all arms behave / 1 an arm misbehaves / 3 crash.
"""
import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
EMIT = HERE / "emit_claims_s58.py"


def stage(tmp: Path):
    """Mirror the session layout into a scratch tree."""
    (tmp / "scripts").mkdir(parents=True)
    (tmp / "outputs").mkdir(parents=True)
    shutil.copy2(EMIT, tmp / "scripts" / "emit_claims_s58.py")
    for p in (SESS / "outputs").glob("*"):
        if p.is_file():
            shutil.copy2(p, tmp / "outputs" / p.name)
    return tmp / "scripts" / "emit_claims_s58.py"


def run(script: Path):
    r = subprocess.run([sys.executable, str(script)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def broke(out: str):
    """A traceback echoes the source line, so an injected reason can appear in
    the output of a script that never ran. Reject those outright."""
    return ("SyntaxError" in out or "NameError" in out
            or "IndentationError" in out)


ARMS = [
    ("A0", None, None, "positive baseline: unmutated emitter must WRITE"),
    ("M1", ('"output_hash": h}', '"output_hash": "0"*64}'),
     "output_hash", "hash that does not match the cited output"),
    ("M2", ('"INSPECTED", "locate_revision.py", "locate_revision.out.txt"),\n'
            '        C("S58-02"',
            '"PROVEN", "locate_revision.py", "locate_revision.out.txt"),\n'
            '        C("S58-02"'),
     "PROVEN", "a PROVEN label, which this session may not use"),
    ("M3", ('"locate_painleve.out.txt")', '"no_such_output.txt")'),
     "missing", "a claim citing an output file that does not exist"),
    # The mutant must be drawn from OUTSIDE what the output legitimately
    # contains. The first version of this arm used "99", which occurs in the
    # output as the line number section5.tex:99 -- so the arm was wrong, not
    # the check. 8642 was confirmed absent before being used here.
    ("M4", ("is 15 .tex", "is 8642 .tex"),
     "8642 does not occur", "a figure that does not occur in the cited output"),
    ("M5", ('C("S58-02",', 'C("S58-01",'),
     "duplicate", "two claims sharing one claim_id"),
    ("M6", ('"All 33 replacements CT-S56 applied to v1.2 are located on '
            'exactly "\n          "one page of the revised PDF; the revised '
            'PDF has 27 pages."',
            '"   "'),
     "empty claim", "a claim whose text is blank"),
]


def main():
    src = EMIT.read_text(encoding="utf-8")
    bad = 0
    print(f"{'arm':<5}{'exit':<6}{'verdict':<12}description")
    print("-" * 78)
    for name, mut, reason, desc in ARMS:
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            script = stage(tmp)
            if mut is not None:
                old, new = mut
                text = src
                if old not in text:
                    print(f"{name:<5}{'-':<6}{'BAD-ARM':<12}"
                          f"mutation target not found in the emitter source")
                    bad += 1
                    continue
                text = text.replace(old, new, 1)
                script.write_text(text, encoding="utf-8")
            rc, out = run(script)
            rec = tmp / "claims.jsonl"
            if name == "A0":
                ok = rc == 0 and rec.exists() and len(
                    rec.read_text(encoding="utf-8").strip().splitlines()) == 10
                verdict = "WROTE" if ok else "FAILED"
                if not ok:
                    bad += 1
                    print(f"      {out[:300]}")
            else:
                if broke(out):
                    ok, verdict = False, "BROKE-SCRIPT"
                else:
                    ok = (rc == 2 and not rec.exists()
                          and reason.lower() in out.lower())
                    verdict = "CAUGHT" if ok else "MISSED"
                if not ok:
                    bad += 1
                    print(f"      rc={rc} wrote={rec.exists()} :: "
                          f"{out[:300]}")
            print(f"{name:<5}{rc:<6}{verdict:<12}{desc}")
    print("-" * 78)
    print(f"{len(ARMS)-bad}/{len(ARMS)} arms behaved as required")

    # The record must be untouched by this harness.
    real = SESS / "claims.jsonl"
    if real.exists():
        h = hashlib.sha256(real.read_bytes()).hexdigest()
        print(f"real claims.jsonl sha256 {h} (this harness never wrote to it)")
    return 1 if bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        print(f"CRASH: {type(e).__name__}: {e}")
        sys.exit(3)
