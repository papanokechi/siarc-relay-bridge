"""emit_p0_adopted.py -- CT-S27-CTV17-DEPOSIT-PREP

Generates P0-ADOPTED-ABCD.txt from the four ```text clause blocks in
P0-AMENDMENTS-ABCD.md, so the paste-ready file cannot drift from the ruled
text.  Reader integrity first, per the clause this very script emits.
"""

import hashlib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.dirname(HERE)
SRC = os.path.join(SESSION, "P0-AMENDMENTS-ABCD.md")
DST = os.path.join(SESSION, "P0-ADOPTED-ABCD.txt")

SENTINELS = ["# P0 amendments A\u2013D \u2014 RULED",   # non-ASCII: en dash, em dash
             "ADOPTED as amended",
             "## Amendment A", "## Amendment B",
             "## Amendment C", "## Amendment D"]

EXPECT_FIRST_LINE = {
    "A": "- BASIS DEGENERACY PRE-CHECK.",
    "B": "- ARTEFACT HASHING IS TERMINAL.",
    "C": "- READER INTEGRITY.",
    "D": "- DEPOSITED TEXT IS AUTHORITATIVE.",
}

with open(SRC, "rb") as fh:
    raw = fh.read()
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
assert "\r" not in text, "CR survived normalisation"
for s in SENTINELS:
    assert s in text, "known-present sentinel absent, the read is suspect: %r" % s
assert any(ord(c) > 127 for c in SENTINELS[0]), "sentinel 0 must be non-ASCII"

blocks = re.findall(r"```text\n(.*?)```", text, re.DOTALL)
assert len(blocks) == 4, "expected 4 clause blocks, found %d" % len(blocks)

letters = "ABCD"
for letter, b in zip(letters, blocks):
    first = b.strip().split("\n")[0].strip()
    assert first.startswith(EXPECT_FIRST_LINE[letter]), \
        "block %s does not open with %r: %r" % (letter, EXPECT_FIRST_LINE[letter], first)
    assert all(ord(c) < 128 for c in b), \
        "block %s carries non-ASCII; the paste target is a plain-text preamble" % letter

header = (
    "P0 AMENDMENTS A-D -- ADOPTED 2026-09-19\n"
    "Paste these four clauses into the session preamble, under the sections named.\n"
    "Generated from P0-AMENDMENTS-ABCD.md by scripts/emit_p0_adopted.py. Do not edit by hand.\n"
    "\n"
    "A -- append under PRE-REGISTRATION\n"
    "B -- append under AEAL RECORD\n"
    "C -- append under PRE-REGISTRATION, after the vacuity pre-check clause\n"
    "D -- append under GOVERNANCE\n"
    "\n" + "=" * 76 + "\n\n")

body = ""
for letter, b in zip(letters, blocks):
    body += "%s\n%s\n" % (b.rstrip(), "\n")

with open(DST, "w", encoding="ascii", newline="\n") as fh:
    fh.write(header + body)

with open(DST, encoding="ascii") as fh:
    back = fh.read()
for letter, b in zip(letters, blocks):
    assert b.rstrip() in back, "block %s did not survive the round trip" % letter
    assert EXPECT_FIRST_LINE[letter] in back

with open(DST, "rb") as fh:
    h = hashlib.sha256(fh.read()).hexdigest()

print("P0-ADOPTED-ABCD.txt written and read back")
print("  clauses : %d (A, B, C, D)" % len(blocks))
print("  bytes   : %d" % os.path.getsize(DST))
print("  sha256  : %s   (from disk)" % h)
print()
for letter, b in zip(letters, blocks):
    print("  %s: %-34s %3d lines" % (letter, EXPECT_FIRST_LINE[letter],
                                     len(b.rstrip().split("\n"))))
print()
print("C carries the two folded-in additions:")
print("  non-ASCII sentinel  :", "non-ASCII character" in blocks[2])
print("  confirming absence  :", "CONFIRMS the hypothesis" in blocks[2])
assert "non-ASCII character" in blocks[2] and "CONFIRMS the hypothesis" in blocks[2], \
    "C was not amended as ruled"
