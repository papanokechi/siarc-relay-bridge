# -*- coding: utf-8 -*-
"""Thorough scan for Python escape-mangled LaTeX/Greek macros.

The R25 scan looked for \\r, \\a, \\v, \\f only. It missed \\t (TAB) and \\b
(BACKSPACE), which are exactly the escapes that eat the most common macros in
this corpus: \\theta -> TAB+'heta', \\tau -> TAB+'au', \\times -> TAB+'imes',
\\beta -> BS+'eta'. Those are load-bearing tokens in a Painleve document.

Reports per file and per token so the notice can be repaired precisely.
"""
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP = {'.lake', '__pycache__', '.git', 'refs', 'pages', 'coldpackets'}

# control char -> the macro(s) it would have come from
MANGLED = [
    ('\t', r'\t', ['heta', 'au', 'imes', 'ext', 'ilde', 'frac']),
    ('\x08', r'\b', ['eta', 'egin', 'ig', 'ar', 'f']),
    ('\x07', r'\a', ['lpha', 'rg', 'pprox']),
    ('\x0b', r'\v', ['arepsilon', 'arphi', 'ec']),
    ('\x0c', r'\f', ['rac', 'orall']),
    ('\r', r'\r', ['ho', 'ightarrow', 'm', 'e']),
]

# Decisive tails: a control char followed by these is mangling wherever it sits.
# The earlier version skipped anything at line start to avoid flagging TAB
# indentation -- and thereby suppressed real hits at the start of wrapped prose
# lines. That is the "could not fire" shape again, so position is now used only
# to break ties on generic tails, never to suppress a decisive one.
DECISIVE = {'heta', 'au', 'imes', 'ilde', 'eta', 'egin', 'lpha', 'arepsilon',
            'arphi', 'rac', 'ho', 'ightarrow', 'orall'}

rows = []
for dp, dns, fns in os.walk(ROOT):
    dns[:] = [d for d in dns if d not in SKIP]
    for fn in fns:
        if not fn.endswith(('.md', '.jsonl', '.json', '.tex', '.txt')):
            continue
        p = os.path.join(dp, fn)
        try:
            raw = io.open(p, encoding='utf-8', newline='').read()
        except (UnicodeDecodeError, OSError):
            continue
        rel = os.path.relpath(p, ROOT)
        found = []
        for ch, macro, tails in MANGLED:
            for m in re.finditer(re.escape(ch) + r'([A-Za-z]+)', raw):
                tail = m.group(1)
                # a TAB used for indentation is followed by nothing alphabetic
                # at line start; require the char to be mid-line to flag it.
                ls = raw.rfind('\n', 0, m.start()) + 1
                at_line_start = raw[ls:m.start()].strip() == ''
                hit = any(tail.startswith(t) for t in tails)
                decisive = any(tail.startswith(t) for t in DECISIVE
                               if any(tail.startswith(x) for x in tails))
                if hit and (decisive or not at_line_start):
                    ln = raw.count('\n', 0, m.start()) + 1
                    found.append((macro, macro + tail[:12], ln))
        if found:
            rows.append((rel, found))

total = sum(len(f) for _, f in rows)
print('files with escape-mangled macros: %d   occurrences: %d' % (len(rows), total))
for rel, found in rows:
    print('\n  %s  (%d)' % (rel, len(found)))
    for macro, recon, ln in found[:20]:
        print('     line %-6d %s  <- likely %r' % (ln, recon, recon))
if not rows:
    print('  (none)')
