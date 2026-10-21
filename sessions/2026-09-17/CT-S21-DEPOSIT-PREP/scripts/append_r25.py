# -*- coding: utf-8 -*-
"""Append outputs/r25_section.md to AUDIT.md byte-wise.

Eighth-amendment pattern: the section text is composed in its own file, never in
a Python string literal, so no escape can be interpreted on the way in. The
appended bytes are compared to the source file's bytes after the write, and the
result is scanned for control characters.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, 'outputs', 'r25_section.md')
DST = os.path.join(os.path.dirname(HERE), 'CT-R1-AUDIT', 'AUDIT.md')

section = io.open(SRC, encoding='utf-8', newline='').read()
assert '## R25' in section

before = io.open(DST, encoding='utf-8', newline='').read()
assert '## R25' not in before, 'R25 already present - refusing to double-append'
nl = '\r\n' if before.count('\r\n') > before.count('\n') / 2 else '\n'
body = section.replace('\r\n', '\n').replace('\n', nl)

with io.open(DST, 'a', encoding='utf-8', newline='') as f:
    f.write(body)

after = io.open(DST, encoding='utf-8', newline='').read()
assert after.startswith(before), 'existing content disturbed'
assert after[len(before):] == body, 'appended bytes differ from source'
assert '## R25' in after
# intent check the readback rule cannot give us:
stray = re.findall(r'\r(?!\n)|[\x07\x0b\x0c]', after)
assert not stray, 'control characters introduced: %r' % stray
print('AUDIT.md %d -> %d chars; R25 appended, 0 stray control chars'
      % (len(before), len(after)))
print('lines:', after.count(nl) + 1)
print('READBACK OK')
