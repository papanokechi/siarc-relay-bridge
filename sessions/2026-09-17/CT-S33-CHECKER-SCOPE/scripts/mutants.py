"""Mutant arms on emit_claims.py.

Each arm injects a defect the emitter must refuse. An arm passes only on three
conditions together, because the first two alone are what CT-S28 defect 6.3
and CT-S32 arm M6 both satisfied while still corrupting the artefact:

  1. the emitter refused (non-zero exit);
  2. it refused FOR THE INJECTED REASON, not incidentally;
  3. claims.jsonl on disk is byte-identical to before the arm ran.
"""
import hashlib
import io
import pathlib
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parents[1]
EMIT = HERE / "scripts" / "emit_claims.py"
TARGET = HERE / "claims.jsonl"
SRC = EMIT.read_text(encoding="utf-8")
BASE = hashlib.sha256(TARGET.read_bytes()).hexdigest()

BUF = io.StringIO()
N = [0]


def say(s=""):
    print(s)
    BUF.write(s + "\n")


ARMS = [
    ("M1 duplicate claim_id",
     lambda s: s.replace('claim("S33-02"', 'claim("S33-01"', 1),
     "duplicate claim_id in memory"),
    ("M2 unrecognised label",
     lambda s: s.replace('"S33-03", "VERIFIED"', '"S33-03", "PROCEED"', 1),
     "S33-03"),
    ("M3 review label dropped",
     lambda s: s.replace('review="self"', 'review="lean"', 1),
     "S33-"),
    ("M4 contamination note altered",
     lambda s: s.replace(
         'NOTE = "contaminated re-derivation',
         'NOTE = "clean re-derivation', 1),
     "pinned hash"),
    ("M5 PROVEN resting on file inspection",
     lambda s: s.replace('"S33-01", "PROVEN", "source_and_measurement"',
                         '"S33-01", "PROVEN", "file_inspection"', 1),
     "S33-01"),
    ("M6 empty evidence",
     lambda s: s.replace(
         "# ----------------------------------------------- validate BEFORE writing ---",
         'C[2]["evidence"] = "   "\n'
         "# ----------------------------------------------- validate BEFORE writing ---",
         1),
     "S33-03"),
    ("M7 CRLF injected into the bytes destined for disk",
     lambda s: s.replace('blob = text.encode("utf-8")',
                         'blob = text.replace("\\n", "\\r\\n").encode("utf-8")', 1),
     "carriage return in the bytes destined for disk"),
    ("M8 hash asserted against the wrong bytes",
     lambda s: s.replace('digest = hashlib.sha256(blob).hexdigest()',
                         'digest = hashlib.sha256(b"x").hexdigest()', 1),
     "hexdigest() == digest"),
]

say("=" * 78)
say("CT-S33  mutant arms on emit_claims.py  (θ, ∞ sentinels)")
say("=" * 78)
say("claims.jsonl before any arm: sha256 %s" % BASE)
say()

for name, mutate, reason in ARMS:
    src = mutate(SRC)
    assert src != SRC, "%s: mutation did not apply" % name
    with tempfile.TemporaryDirectory() as td:
        f = pathlib.Path(td) / "emit_mutant.py"
        # parents[1] of the mutant must still be this session folder, so the
        # mutant writes to the REAL claims.jsonl if it gets that far. That is
        # deliberate: condition 3 is only meaningful if the artefact is at risk.
        f = EMIT.parent / "_mutant.py"
        f.write_text(src, encoding="utf-8")
        try:
            r = subprocess.run([sys.executable, str(f)], capture_output=True,
                               text=True, encoding="utf-8", errors="replace")
        finally:
            f.unlink()

    out = (r.stdout or "") + (r.stderr or "")
    after = hashlib.sha256(TARGET.read_bytes()).hexdigest()
    refused = r.returncode != 0
    # A mutation that breaks the SCRIPT rather than the claim set refuses for
    # the wrong reason, and a traceback echoes the source line, which can make
    # a naive substring test on the reason succeed. M6 passed that way once.
    broke_script = "SyntaxError" in out or "NameError" in out
    right_reason = (reason in out) and not broke_script
    intact = after == BASE
    verdict = "CAUGHT" if (refused and right_reason and intact) else "MISSED"
    say("  [%s] %s" % (verdict, name))
    say("         refused=%s  for-the-injected-reason=%s  artefact-intact=%s"
        % (refused, right_reason, intact))
    if broke_script:
        say("         MUTATION BROKE THE SCRIPT, not the claim set")
    if not intact:
        say("         ARTEFACT CORRUPTED: %s" % after)
    tail = [l for l in out.strip().splitlines() if l.strip()]
    if tail:
        say("         %s" % tail[-1][:110])
    assert refused, "%s: emitter did NOT refuse" % name
    assert right_reason, "%s: refused, but not for the injected reason" % name
    assert intact, "%s: artefact was modified before the refusal" % name
    N[0] += 1

say()
say("ARMS: %d/%d CAUGHT" % (N[0], len(ARMS)))
say("claims.jsonl after every arm:  sha256 %s" % BASE)
say()
say("What would have made an arm fire: the emitter accepting the injected")
say("defect; refusing for an unrelated reason (a mutation that breaks the")
say("script rather than the claim set); or refusing only after the write, the")
say("failure mode of CT-S28 defect 6.3 and CT-S32 arm M6, which condition 3")
say("is the only one of the three able to detect.")

OUT = HERE / "outputs" / "mutants.out.txt"
data = BUF.getvalue()
OUT.write_text(data, encoding="utf-8", newline="")
raw = OUT.read_bytes()
assert b"\r\n" not in raw
t = raw.decode("utf-8")
assert "θ" in t and "∞" in t, "non-ASCII sentinel absent: reader unverified"
assert "θ" not in raw.decode("latin-1")
assert t == data
assert hashlib.sha256(TARGET.read_bytes()).hexdigest() == BASE
print("sha256 = %s  bytes = %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
