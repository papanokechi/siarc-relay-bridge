# -*- coding: utf-8 -*-
"""Replace the deposit-day checklist section with the run version, byte-wise."""
import hashlib
import os
import re
import sys

ROOT = r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17'
NOTICE = os.path.join(ROOT, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md')
NEWF = os.path.join(ROOT, 'CT-S21-DEPOSIT-PREP', 'outputs', 'checklist_replacement.md')

BAD = re.compile(rb'[\x00-\x09\x0b-\x1f\x7f]')


def bad_chars(d):
    return sorted(set(BAD.findall(d.replace(b'\r\n', b'\n'))))


START = '## Deposit-day checklist'.encode('utf-8')

before = open(NOTICE, 'rb').read()
nl = b'\r\n' if before.count(b'\r\n') > before.count(b'\n') // 2 else b'\n'

i = before.find(START)
assert i != -1, 'section not found'
assert before.count(START) == 1

new = open(NEWF, 'rb').read().replace(b'\r\n', b'\n').rstrip(b'\n')
new = new.replace(b'\n', nl) + nl

after = before[:i] + new

# the false status line must be gone, the run status present
assert 'NOT YET DONE'.encode('utf-8') not in after, 'stale status survived'
assert 'Only the deposit-day citation'.encode('utf-8') not in after
assert 'RUN, 18 September 2026'.encode('utf-8') in after
for tok in [b'1666bd6b', b'255d4f07', b'20455089', b'Version 1.2.8']:
    assert tok in after, 'missing %r' % tok

with open(NOTICE, 'wb') as f:
    f.write(after)

back = open(NOTICE, 'rb').read()
assert back == after, 'readback differs from intended bytes'
hits = bad_chars(back)
if hits:
    print('FAIL control chars %r' % hits)
    sys.exit(1)

print('notice %d -> %d bytes, %d -> %d lines'
      % (len(before), len(back), before.count(b'\n') + 1, back.count(b'\n') + 1))
print('stale "NOT YET DONE" removed; all four result rows present; no control chars')
print('sha256 %s' % hashlib.sha256(back).hexdigest())
