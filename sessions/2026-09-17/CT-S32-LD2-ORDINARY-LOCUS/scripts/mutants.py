"""Mutant arms against scripts/emit_claims.py's own validation.

Each arm injects one fault, runs the emitter in a subprocess, and requires
BOTH that the emitter refuses AND that claims.jsonl on disk is byte-identical
afterwards -- the second half is the point: an emitter that writes before it
asserts leaves a corrupted artefact behind on every arm it "catches".
"""
import hashlib
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "emit_claims.py"
DEST = HERE.parent / "claims.jsonl"
ART = HERE.parent / "outputs" / "locus.out.txt"

ORIG = SRC.read_text(encoding="utf-8")
BEFORE = DEST.read_bytes()
H0 = hashlib.sha256(BEFORE).hexdigest()
assert len(BEFORE) > 0

MUTANTS = [
    ("M1 duplicate claim_id",
     'add("S32-02", T + "/locus"', 'add("S32-01", T + "/locus"',
     "duplicate claim_id within this session"),
    ("M2 unrecognised label",
     '"PROVEN", "symbolic_computation",\n    "A SINGULAR POINT',
     '"PROVED", "symbolic_computation",\n    "A SINGULAR POINT',
     "S32-01"),
    ("M3 empty review_note",
     'NOTE = ("contaminated re-derivation; prior treatment of the same '
     'operator "\n        "was in context")',
     'NOTE = ""',
     "S32-01"),
    ("M4 PROVEN resting on file_inspection",
     'add("S32-09", T + "/coverage", "INSPECTED", "file_inspection"',
     'add("S32-09", T + "/coverage", "PROVEN", "file_inspection"',
     "S32-09"),
    ("M5 supersedes target not named in the claim text",
     'supersedes="S28-10")',
     'supersedes="S28-99")',
     "supersedes target not named"),
    ("M6 output_hash not the hash of the artefact on disk",
     'H = hashlib.sha256(ART.read_bytes()).hexdigest()',
     'H = "0" * 64',
     "artefact changed under the emitter"),
    ("M7 review value outside self|cold|lean",
     '"review": "self", "review_note": NOTE}',
     '"review": "warm", "review_note": NOTE}',
     "S32-01"),
]

fired = 0
for name, old, new, expect in MUTANTS:
    assert old in ORIG, "mutant %s: anchor not found -- the arm is vacuous" % name
    SRC.write_text(ORIG.replace(old, new, 1), encoding="utf-8")
    try:
        p = subprocess.run([sys.executable, str(SRC)], capture_output=True,
                           text=True, encoding="utf-8", cwd=str(HERE.parent))
        after = DEST.read_bytes()
        refused = p.returncode != 0
        intact = after == BEFORE
        seen = expect in (p.stderr or "") + (p.stdout or "")
        status = "CAUGHT" if (refused and intact and seen) else "MISSED"
        print("  [%s] %-52s rc=%s  artefact intact=%s  matched=%s"
              % (status, name, p.returncode, intact, seen))
        assert refused, "%s: the emitter ACCEPTED the fault" % name
        assert seen, "%s: refused, but not for the injected reason" % name
        assert intact, ("%s: refused but claims.jsonl was modified -- the "
                        "emitter writes before it asserts" % name)
        fired += 1
    finally:
        SRC.write_text(ORIG, encoding="utf-8")

assert SRC.read_text(encoding="utf-8") == ORIG, "source not restored"
assert DEST.read_bytes() == BEFORE, "claims.jsonl not restored"
assert hashlib.sha256(DEST.read_bytes()).hexdigest() == H0

# a clean re-run must reproduce the file byte-for-byte
p = subprocess.run([sys.executable, str(SRC)], capture_output=True, text=True,
                   encoding="utf-8", cwd=str(HERE.parent))
assert p.returncode == 0, p.stderr
assert DEST.read_bytes() == BEFORE, "clean re-run changed claims.jsonl"

print("\n  %d/%d mutant arms fired; claims.jsonl byte-identical throughout"
      % (fired, len(MUTANTS)))
print("  claims.jsonl sha256 %s" % H0)
print("  artefact     sha256 %s"
      % hashlib.sha256(ART.read_bytes()).hexdigest())
