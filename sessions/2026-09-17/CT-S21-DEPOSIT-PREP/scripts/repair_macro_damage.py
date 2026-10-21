# -*- coding: utf-8 -*-
"""Repair escape-mangled macros: TAB+'heta' -> 'theta', BS+'eta' -> 'beta'.

The surrounding prose in both files is plain ASCII ('sigma_3', 'diag(1,0)',
'theta_t not in Z'), so the repair restores the plain word, not a LaTeX macro.
Counts are asserted before and after, and scan_macro_damage.py re-derives the
total in a separate invocation.
"""
import io
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)

TARGETS = [
    (os.path.join(SESS, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md'),
     [('\theta', 'theta')], 4),
    (os.path.join(HERE, 'outputs', 'item2_quotes.md'),
     [('\x08eta', 'beta')], 1),
]

for path, subs, expected in TARGETS:
    src = io.open(path, encoding='utf-8', newline='').read()
    n = sum(src.count(bad) for bad, _ in subs)
    assert n == expected, '%s: expected %d mangled, found %d' % (path, expected, n)
    out = src
    for bad, good in subs:
        out = out.replace(bad, good)
    assert out != src
    io.open(path, 'w', encoding='utf-8', newline='').write(out)

    back = io.open(path, encoding='utf-8', newline='').read()
    assert back == out, 'READBACK MISMATCH %s' % path
    assert sum(back.count(bad) for bad, _ in subs) == 0, 'repair did not take'
    # intent check: the repaired words must actually be present
    for _, good in subs:
        assert good in back
    print('%-46s %d repaired, %d -> %d chars'
          % (os.path.basename(path), n, len(src), len(back)))

print('READBACK OK')
