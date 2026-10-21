# -*- coding: utf-8 -*-
"""Scan the session tree for backtick-escape damage and control characters.

The PowerShell backtick consumes the following character when it is one of
a b e f n r t v 0. In markdown that turns a code span opener into a control
byte. This looks for the residue, not for the cause.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 0x09 TAB and 0x08 BS are the signatures that were missed once before.
CTRL = set(range(0x00, 0x0a)) | set(range(0x0b, 0x20)) | {0x7f}
CTRL.discard(0x09) if False else None  # TAB stays in: it is a signature.

SKIP_DIRS = {'.git', '.lake', 'node_modules', '__pycache__', 'coldpackets'}
# Raw PDF text extractions legitimately carry control bytes.
SKIP_SUBSTR = ('CT-S9-PVPARAMS' + os.sep + 'outputs',)


def main():
    hits = 0
    scanned = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if any(s in dirpath for s in SKIP_SUBSTR):
            continue
        for fn in filenames:
            if not fn.lower().endswith(('.md', '.jsonl', '.json', '.txt')):
                continue
            p = os.path.join(dirpath, fn)
            try:
                data = open(p, 'rb').read()
            except OSError:
                continue
            scanned += 1
            data = data.replace(b'\r\n', b'\n')
            bad = sorted({b for b in data if b in CTRL})
            if bad:
                hits += 1
                rel = os.path.relpath(p, ROOT)
                for b in bad:
                    i = data.index(bytes([b]))
                    print('CTRL %-58s %r at %d: %r'
                          % (rel[:58], bytes([b]), i, data[max(0, i - 30):i + 20]))
    print()
    print('files scanned: %d' % scanned)
    print('files with control characters: %d' % hits)
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main())
