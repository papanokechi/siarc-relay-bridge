# -*- coding: utf-8 -*-
"""Control for the patched F6/F7 detectors: mutate the notice, run the REAL
checker, confirm it fires, restore, and verify the restore by sha256.

States what would have made it fire: if either mutation passed unnoticed, the
corresponding detector would be certifying nothing.
"""
import hashlib
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
NOTICE = os.path.join(SESS, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md')
CHECK = os.path.join(HERE, 'scripts', 'item4_consistency.py')
OUTMD = os.path.join(HERE, 'outputs', 'item4_consistency.md')
BAK = NOTICE + '.control-bak'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run():
    r = subprocess.run([sys.executable, CHECK], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '') + (r.stderr or '')


orig = sha(NOTICE)
orig_out = open(OUTMD, encoding='utf-8').read() if os.path.exists(OUTMD) else ''
shutil.copyfile(NOTICE, BAK)
results = {}
try:
    text = open(NOTICE, encoding='utf-8').read()

    # Mutation 1: count word disagrees with the enumerated items.
    m1 = text.replace('Seven points must accompany this table',
                      'Six points must accompany this table')
    assert m1 != text, 'mutation 1 did not apply'
    open(NOTICE, 'w', encoding='utf-8', newline='\n').write(m1)
    out = run()
    results['F6 count-word mismatch'] = ('MISMATCH' in out, out.strip().splitlines()[-6:])

    # Mutation 2: a genuine, NON-negated author-confirmation assertion.
    m2 = text.replace('No published\n> erratum is known to us.',
                      'The authors have confirmed this.')
    assert m2 != text, 'mutation 2 did not apply'
    open(NOTICE, 'w', encoding='utf-8', newline='\n').write(m2)
    out = run()
    results['F7 asserting hit'] = ('F7 asserting hits: 0' not in out, out.strip().splitlines()[-4:])

    # Mutation 3: blockquote re-wrap of a hedge - the false-negative class that
    # the raw-string search actually suffered at CT-S21.
    m3 = text.replace('No published\n> erratum is known to us.',
                      'No published erratum\n> is known to us.')
    assert m3 != text, 'mutation 3 did not apply'
    open(NOTICE, 'w', encoding='utf-8', newline='\n').write(m3)
    out = run()
    results['F7 hedge survives re-wrap'] = ('erratum=True' in out, out.strip().splitlines()[-3:])
finally:
    shutil.copyfile(BAK, NOTICE)
    os.remove(BAK)

assert sha(NOTICE) == orig, 'RESTORE FAILED - notice differs from its original sha256'
run()  # regenerate the real output over the restored notice
final = open(OUTMD, encoding='utf-8').read()

print('notice restored, sha256 matches original:', orig[:16], '...')
ok = True
for k, (fired, tail) in results.items():
    print('%-28s -> %s' % (k, 'FIRED (good)' if fired else '*** DID NOT FIRE ***'))
    if not fired:
        ok = False
        for t in tail:
            print('     ', t)
assert ok, 'a control did not fire; the detector certifies nothing'
assert 'MISMATCH' not in final, 'real output should be clean after restore'
print('ALL CONTROLS FIRED; real output regenerated and clean')
