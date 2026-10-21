# -*- coding: utf-8 -*-
"""Remove the draft scaffolding from the notice and set its H1.

NOT RUN. The title depends on an operator choice (Option A or B in
DEPOSIT-FORM.md), and every wording change in this object has been ruled on
first. Run exactly one of:

    python scripts/apply_title.py A
    python scripts/apply_title.py B

Then re-run item4_consistency.py and control_item4.py, take the NEW sha256 it
prints, and use that one in the upload dialog. The hash WILL change.
"""
import hashlib
import io
import json
import re
import sys

NOTICE = (r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17'
          r'\CT-R1-AUDIT\DRAFT-COMPANION-v1.3-NOTICE.md')

_REC = r'C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S21-DEPOSIT-PREP\outputs\depday_zenodo_20481592.json'
_T = json.load(io.open(_REC, encoding='utf-8'))['metadata']['title']

TITLES = {
    'A': _T + ' \u2014 v1.3 correction notice',
    'B': 'Correction notice to "' + _T + '"',
}

BAD = re.compile(rb'[\x00-\x09\x0b-\x1f\x7f]')

opt = (sys.argv[1] if len(sys.argv) > 1 else '').upper()
if opt not in TITLES:
    sys.exit('choose A or B (see DEPOSIT-FORM.md)')

raw = open(NOTICE, 'rb').read()
text = raw.decode('utf-8')
nl = '\r\n' if '\r\n' in text else '\n'
lines = text.split(nl)

assert lines[0].startswith('# DRAFT'), 'H1 is not the draft heading: %r' % lines[0]
lines[0] = '# ' + TITLES[opt]

# drop the STATUS block: the bold paragraph addressed to the operator
joined = nl.join(lines)
m = re.search(r'\*\*STATUS: DRAFT FOR THE OPERATOR\..*?\*\*\s*', joined, re.S)
assert m, 'STATUS block not found'
joined = joined[:m.start()] + joined[m.end():]

out = joined.encode('utf-8')
assert b'DRAFT' not in out, 'a DRAFT mention survived'
assert BAD.search(out.replace(b'\r\n', b'\n')) is None, 'control chars'
assert TITLES[opt].encode('utf-8') in out

open(NOTICE, 'wb').write(out)
back = open(NOTICE, 'rb').read()          # separate read
assert back == out, 'readback differs from intended bytes'

print('option %s applied' % opt)
print('H1: %s' % back.decode('utf-8').split(nl)[0])
print('DRAFT mentions remaining: %d' % back.count(b'DRAFT'))
print('bytes %d -> %d' % (len(raw), len(back)))
print('NEW sha256 (use THIS in the dialog): %s' % hashlib.sha256(back).hexdigest())
