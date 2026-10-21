# -*- coding: utf-8 -*-
"""Sweep the deposit-prep documents for consequences of superseded decisions.

R32's lesson: when a decision is overruled, what was derived from it does not
update itself. This looks for the derived statements, not the decisions.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUD = os.path.join(os.path.dirname(HERE), 'CT-R1-AUDIT')

# Only forward-looking instruction documents. The audit and claims are an
# append-only record: stale text there is history and must NOT be rewritten.
TARGETS = [
    os.path.join(HERE, 'DEPOSIT-FORM.md'),
    os.path.join(HERE, 'DEPOSIT-WALKTHROUGH.md'),
    os.path.join(HERE, 'DEPOSIT-DAY-PASS.md'),
    os.path.join(AUD, 'DRAFT-COMPANION-v1.3-NOTICE.md'),
]

STALE = [
    ('superseded hash a9a938f7', r'a9a938f7'),
    ('superseded hash d070fab1', r'd070fab1'),
    ('superseded hash aba11232', r'aba11232'),
    ('notice-only shape', r'notice only\.|the notice only\b'),
    ('add a supplement row', r'is supplement to\*\*|as \*\*is supplement'),
    ('two DOIs in A3', r'the two DOIs in A3'),
    ('title must match H1', r"H1 \u2014 must match|must match exactly"),
    ('word DRAFT', r'\bDRAFT\b'),
    ('pass not yet run', r'NOT YET DONE'),
    ('editorial marker', r'\[(?:Deposit-day|TODO|FIXME|XXX)'),
]
# Lines that legitimately *name* a superseded thing while correcting it.
EXEMPT = re.compile(
    r'supersed|previously|earlier|no longer|stale|was written for|'
    r'do not add|add nothing|Superseded|corrected|history', re.I)

total = 0
for p in TARGETS:
    text = io.open(p, encoding='utf-8').read()
    lines = text.split('\n')
    for label, pat in STALE:
        rx = re.compile(pat)
        for i, ln in enumerate(lines, 1):
            if rx.search(ln) and not EXEMPT.search(ln):
                print('HIT  %-28s %s:%d' % (label, os.path.basename(p), i))
                print('       %s' % ln.strip()[:110])
                total += 1

print()
print('live instruction documents scanned: %d' % len(TARGETS))
print('unexplained stale statements: %d' % total)
print('(audit and claims deliberately excluded: append-only record)')
