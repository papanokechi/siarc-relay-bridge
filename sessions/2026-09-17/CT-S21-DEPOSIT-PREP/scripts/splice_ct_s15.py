# -*- coding: utf-8 -*-
"""Splice the CT-S15 paragraph in the notice, byte-wise.

The old and new blocks both live in files. Nothing is built from a Python
string literal, so no escape can be interpreted on the way in.
"""
import hashlib
import os
import re
import sys

ROOT = r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17'
NOTICE = os.path.join(ROOT, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md')
NEWF = os.path.join(ROOT, 'CT-S21-DEPOSIT-PREP', 'outputs', 'ct_s15_replacement.md')

BAD = re.compile(rb'[\x00-\x09\x0b-\x1f\x7f]')


def bad_chars(d):
    return sorted(set(BAD.findall(d.replace(b'\r\n', b'\n'))))


START = b'**CT-S15-COLDREAD-DEFERRED**'
END = b'None of this is machine-checked'

before = open(NOTICE, 'rb').read()
nl = b'\r\n' if before.count(b'\r\n') > before.count(b'\n') // 2 else b'\n'

i = before.find(START)
j = before.find(END)
assert i != -1 and j != -1 and i < j, 'anchors not found'
old = before[i:j]

new = open(NEWF, 'rb').read().replace(b'\r\n', b'\n').rstrip(b'\n')
new = new.replace(b'\n', nl) + nl + nl

# sanity: the three things the ruling requires, checked on the new text
need = {
    'wrong page named': b'in fact printed',
    'faithful to page given': b'faithful readings of the page the reader was given',
    'packet not reader': b'not in the reader',
    're-verified this round': b're-verified on deposit',
    'true page named': b'true printed p. 1152',
}
missing = [k for k, v in need.items() if v not in new]
assert not missing, 'replacement missing: %s' % missing

after = before[:i] + new + before[j:]
assert b'ran **OCR** on' not in after, 'OCR attribution survived'
assert after.count(START) == 1

with open(NOTICE, 'wb') as f:
    f.write(after)

back = open(NOTICE, 'rb').read()          # separate read
assert back == after, 'readback differs from intended bytes'
hits = bad_chars(back)
if hits:
    print('FAIL control chars %r' % hits)
    sys.exit(1)
assert old not in back, 'old paragraph still present'

print('notice %d -> %d bytes, %d -> %d lines'
      % (len(before), len(back), before.count(b'\n') + 1, back.count(b'\n') + 1))
print('old block removed, new block present, no control chars')
print('all 5 required statements present: %s' % ', '.join(need))
print('sha256 %s' % hashlib.sha256(back).hexdigest())
