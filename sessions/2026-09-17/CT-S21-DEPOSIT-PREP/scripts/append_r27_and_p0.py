# -*- coding: utf-8 -*-
"""Byte-wise append of composed sections (eighth-amendment pattern).

Never build the section text in Python source: compose it in its own file and
copy the bytes. Then verify the tail equals the source bytes exactly, and scan
the whole result for control characters.
"""
import hashlib
import io
import os
import re
import sys

ROOT = r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17'
JOBS = [
    (os.path.join(ROOT, 'CT-S21-DEPOSIT-PREP', 'outputs', 'r27_section.md'),
     os.path.join(ROOT, 'CT-R1-AUDIT', 'AUDIT.md')),
    (os.path.join(ROOT, 'CT-S21-DEPOSIT-PREP', 'outputs', 'p0_detector_hygiene.md'),
     os.path.join(ROOT, 'CT-R1-AUDIT', 'P0-CITATION-RULE.md')),
]

# Control chars that escape-mangling produces. CRLF is legitimate on Windows and
# both targets already carry it, so strip CRLF pairs first and flag what is left
# - including a BARE \r, which is exactly what a mangled \refs/ leaves behind.
#
# \x09 (TAB) IS IN THE CLASS. It is the signature of a mangled \theta, and the
# first version of this scanner omitted it - reproducing, in the detector written
# to enforce the detector-hygiene rule, the very coverage gap that rule names.
# Only \n is excluded.
BAD = re.compile(rb'[\x00-\x09\x0b-\x1f\x7f]')


def bad_chars(data):
    return sorted(set(BAD.findall(data.replace(b'\r\n', b'\n'))))

rc = 0
for src, dst in JOBS:
    add = open(src, 'rb').read().replace(b'\r\n', b'\n')
    before = open(dst, 'rb').read()
    if add in before:
        print('SKIP already present: %s' % os.path.basename(dst))
        continue
    with open(dst, 'ab') as f:
        f.write(add)

    after = open(dst, 'rb').read()          # separate read, not the buffer
    assert after[:len(before)] == before, 'prefix changed in %s' % dst
    tail = after[len(before):]
    if tail != add:
        print('FAIL byte mismatch in %s' % dst)
        rc = 1
        continue
    hits = bad_chars(after)
    if hits:
        print('FAIL control chars %r in %s' % (sorted(set(hits)), dst))
        rc = 1
        continue
    n0 = before.count(b'\n')
    n1 = after.count(b'\n')
    print('%s: %d -> %d lines, +%d bytes, tail bytes identical, no control chars'
          % (os.path.basename(dst), n0, n1, len(tail)))
    print('   sha256 %s' % hashlib.sha256(after).hexdigest()[:16])

sys.exit(rc)
