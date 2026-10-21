# -*- coding: utf-8 -*-
"""Scan the session record for stray control characters from \\r / \\n / \\a
escape mangling in Python source literals.

This defect class survives the P0 readback rule: the script wrote an already
mangled string and read back the same mangled string, so the comparison passed.
The readback rule verifies that a write happened, not that the intended text was
the text written.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = {'.lake', '__pycache__', '.git', 'refs', 'pages', 'coldpackets'}

# A bare CR not part of CRLF, or a BEL/FF/VT -- none belong in these documents.
BAD = re.compile(r'\r(?!\n)|[\x07\x0b\x0c]')
# 'word' immediately after a line break where the break splits a known token.
SUSPECT_WORDS = ('efs/', '_infinity', 'cquire_', 'laims.jsonl', 'eport')

rows = []
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in SKIP]
    for fn in fns:
        if not fn.endswith(('.md', '.jsonl', '.json', '.txt')):
            continue
        p = os.path.join(dp, fn)
        try:
            raw = open(p, 'rb').read().decode('utf-8')
        except (UnicodeDecodeError, OSError):
            continue
        ctrl = len(BAD.findall(raw))
        sus = []
        for w in SUSPECT_WORDS:
            for m in re.finditer(r'[\r\n]' + re.escape(w), raw):
                ln = raw[:m.start()].count('\n') + 1
                sus.append((w, ln))
        if ctrl or sus:
            rows.append((os.path.relpath(p, ROOT), ctrl, sus))

print('files with stray control chars or split tokens: %d' % len(rows))
for rel, ctrl, sus in rows:
    print('  %-58s ctrl=%-3d split=%s' % (rel, ctrl, sus[:8]))
if not rows:
    print('  (none)')
