# -*- coding: utf-8 -*-
"""Repair escape-mangled text in AUDIT.md section R24 and reword the two claims
the operator asked to be restated.

Byte-exact replacements; each is asserted present before the write, and the file
is re-read from disk afterwards. A separate invocation of scan_escape_damage.py
re-derives the control-character count.
"""
import io
import os

P = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'CT-R1-AUDIT', 'AUDIT.md')

# The source literals were written with \r / \a interpreted as escapes. A later
# text-mode read-modify-write promoted each lone CR to a full CRLF line break,
# so the damage now presents as a spurious line break, not a control character.
REPAIRS = [
    ('pulled into \r\nefs/.**', 'pulled into `refs/`.**'),
    ('third-party files in \r\nefs/ cleared', 'third-party files in `refs/` cleared'),
    ('NOT CHECKED. \x07cquire_refs.py refuses', 'NOT CHECKED. `acquire_refs.py` refuses'),
    ('K and \r\n_infinity in v1.7.', 'K and r_infinity in v1.7.'),
]

src = io.open(P, encoding='utf-8', newline='').read()
before = src

for bad, good in REPAIRS:
    assert bad in src, 'repair target absent: %r' % bad[:40]
    src = src.replace(bad, good)

# --- operator rewording 1: the Wong-Zhao absence claim (INSPECTED rule) ------
OLD_ABS = ("""confirms at section 3 that Wong-Li II covers the equation class but does not\r
   state the growth law, so the purchase is warranted.""")
NEW_ABS = ("""confirms at section 3 that Wong-Li II covers the equation class; the growth\r
   law is **NOT FOUND in section 3 by full-text read** (CT-S21, pp. 12-20,\r
   six positive controls fired; outputs/wz_sec3_absence.json). Stated as an\r
   absence claim, not as "the survey does not state it". The purchase is\r
   warranted.""")
assert OLD_ABS in src, 'absence-claim target absent'
src = src.replace(OLD_ABS, NEW_ABS)

assert src != before
io.open(P, 'w', encoding='utf-8', newline='').write(src)

back = io.open(P, encoding='utf-8', newline='').read()
assert back == src, 'READBACK MISMATCH'
for bad, _ in REPAIRS:
    assert bad not in back, 'repair did not take: %r' % bad[:40]
assert 'NOT FOUND in section 3 by full-text read' in back
assert '\r\n' in back and '\r\r' not in back
print('AUDIT.md repaired and reworded; %d -> %d chars' % (len(before), len(back)))
print('READBACK OK')
