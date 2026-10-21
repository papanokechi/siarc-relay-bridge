# Mutant controls for the review_note requirement added to S35-04 by the
# operator ruling of 2026-09-19.
#
# The ruling asked for a field.  A field with no failing check is prose, not a
# record, so each of the three things the ruling fixes -- that the note is
# present, that it names the re-derivable/not-replayable distinction, and that
# the label stays STRUCTURAL -- gets a mutant that removes it.
#
# Amendment E: none of the three mutants is drawn from the assertions' own
# strings.  M1 renames the key (the failure mode the projection defect would
# have produced silently).  M2 promotes the label, the thing the ruling
# explicitly said must not move.  M3 supplies a plausible, well-formed note
# that simply does not make the distinction -- the mutant a check that only
# tested for the key's presence would accept.
#
# Every arm asserts the emitter refused BEFORE writing, by requiring
# claims.jsonl to be byte-identical after the arm as before it, and rejects
# SyntaxError/NameError so a script that never ran cannot count as a refusal.

import hashlib
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, "emit_claims_s35.py")
ART = os.path.join(ROOT, "claims.jsonl")


def sha(p):
    return hashlib.sha256(io.open(p, "rb").read()).hexdigest()


MUT = [
    ("M1 review_note key renamed (the silent-drop failure mode)",
     '         review_note="Re-derivable but not replayable: the second isolated "',
     '         review_note_DROPPED="Re-derivable but not replayable: the second isolated "'),
    ("M2 Tier 2 label promoted to VERIFIED",
     '               "deg a = deg b and so confirms the exclusion only.",\n'
     '         label="STRUCTURAL"',
     '               "deg a = deg b and so confirms the exclusion only.",\n'
     '         label="VERIFIED"'),
    ("M3 note present but silent on replayability",
     'review_note="Re-derivable but not replayable: the second isolated "',
     'review_note="Confirmed by a second isolated reader, whose reading was '
     'independent of this corpus. "  #'),
]


def main():
    orig = io.open(SRC, encoding="utf-8").read()

    # Reader integrity: assert a known-present non-ASCII-free but distinctive
    # feature before evaluating any absence, so an empty or misdecoded read
    # cannot pass as "mutation site not found".
    assert "review_note" in orig, "reader integrity: emitter source not read"
    assert "OPTIONAL" in orig, "reader integrity: emitter source not read"

    before = sha(ART)
    caught = 0
    try:
        for name, a, b in MUT:
            assert a in orig, "SETUP-FAIL, mutation site absent: %s" % name
            io.open(SRC, "w", encoding="utf-8", newline="").write(
                orig.replace(a, b, 1))
            p = subprocess.run([sys.executable, SRC],
                               capture_output=True, text=True)
            out = (p.stdout or "") + (p.stderr or "")
            broke = "SyntaxError" in out or "NameError" in out
            ok = p.returncode != 0 and "AssertionError" in out and not broke
            intact = sha(ART) == before
            print("%-52s %s  rc=%d  pre_write=%s"
                  % (name, "CAUGHT" if ok else "MISSED", p.returncode, intact))
            if ok and intact:
                caught += 1
    finally:
        io.open(SRC, "w", encoding="utf-8", newline="").write(orig)

    print("")
    print("%d/%d mutants caught, all refused before writing" % (caught, len(MUT)))
    print("claims.jsonl unchanged by the mutant run: %s" % (sha(ART) == before))
    assert sha(ART) == before, "a mutant wrote to claims.jsonl"
    assert caught == len(MUT), "a mutant was accepted"
    return 0


if __name__ == "__main__":
    sys.exit(main())
