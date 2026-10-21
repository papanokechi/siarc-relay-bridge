# -*- coding: utf-8 -*-
"""Propagate the final hash, and make apply_title.py derive titles from the record."""
import io
import json
import os
import re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OLD = 'a9a938f7c0c6a372948148465b09bcd7df366d60dd1aab302e282ca0cdca85fd'
NEW = 'c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c'

for name in ['DEPOSIT-FORM.md', 'DEPOSIT-DAY-PASS.md']:
    p = os.path.join(HERE, name)
    t = io.open(p, encoding='utf-8').read()
    t2 = (t.replace(OLD, NEW)
           .replace('a9a938f7\u2026', 'c936662f\u2026')
           .replace('35 964', '35 918')
           .replace('35,964', '35,918'))
    if t2 != t:
        io.open(p, 'w', encoding='utf-8', newline='').write(t2)
    chk = io.open(p, encoding='utf-8').read()
    print('%-22s new hash present=%s  old hash gone=%s'
          % (name, NEW in chk or 'c936662f' in chk, OLD not in chk and 'a9a938f7' not in chk))

# apply_title.py: derive both titles from the record, never retype them
sp = os.path.join(HERE, 'scripts', 'apply_title.py')
s = io.open(sp, encoding='utf-8').read()
rec = os.path.join(HERE, 'outputs', 'depday_zenodo_20481592.json')
title = json.load(io.open(rec, encoding='utf-8'))['metadata']['title']

block = (
    "_REC = r'%s'\n"
    "_T = json.load(io.open(_REC, encoding='utf-8'))['metadata']['title']\n"
    "\n"
    "TITLES = {\n"
    "    'A': _T + ' \\u2014 v1.3 correction notice',\n"
    "    'B': 'Correction notice to \"' + _T + '\"',\n"
    "}\n" % rec
)
s = re.sub(r"TITLES = \{.*?\n\}\n", lambda _m: block, s, flags=re.S)
if 'import json' not in s:
    s = s.replace('import io', 'import io\nimport json', 1)
io.open(sp, 'w', encoding='utf-8', newline='').write(s)

back = io.open(sp, encoding='utf-8').read()
print('apply_title: derives from record =', '_T = json.load' in back)
print('apply_title: ASCII "Painleve" gone =', 'Painleve' not in back)
