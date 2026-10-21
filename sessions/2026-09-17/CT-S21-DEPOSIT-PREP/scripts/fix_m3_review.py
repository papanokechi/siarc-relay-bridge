# -*- coding: utf-8 -*-
"""M3 - write review='cold' back to S4-06 and S5B-C6.

The notice's support table shows both as cold; VERIFY-S14.md and _deps_table.md
record that the cold read happened, by route "D - corroborated". The corpus rows
were stale, not the notice. Amended in place under the R20 precedent, with a
.bak alongside.
"""
import json
import os
import shutil

SESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(SESS) if os.path.basename(SESS) != '2026-09-17' else SESS
assert os.path.basename(SESS) == '2026-09-17', SESS

NOTE = ('review field written back at CT-S21 (M3): the notice support table '
        'showed this claim as cold while the corpus carried review=None. '
        'VERIFY-S14.md and _deps_table.md record the cold read as having '
        'happened by route "D - corroborated"; the corpus row was stale, not '
        'the notice. Amended in place under the R20 precedent.')
TARGETS = {'S4-06', 'S5B-C6'}

found = {}
for d in sorted(os.listdir(SESS)):
    p = os.path.join(SESS, d, 'claims.jsonl')
    if not os.path.isfile(p):
        continue
    rows = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    hit = [r for r in rows if r['claim_id'] in TARGETS]
    if not hit:
        continue
    shutil.copyfile(p, p + '.bak-s21m3')
    for r in rows:
        if r['claim_id'] in TARGETS:
            before = r.get('review')
            assert before is None, '%s already has review=%r' % (r['claim_id'], before)
            r['review'] = 'cold'
            r['review_note'] = NOTE
            found[r['claim_id']] = d
    with open(p, 'w', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')

assert set(found) == TARGETS, 'not all targets found: %r' % (found,)

# readback from a fresh parse of the files on disk
for cid, d in found.items():
    rows = [json.loads(l) for l in
            open(os.path.join(SESS, d, 'claims.jsonl'), encoding='utf-8') if l.strip()]
    r = next(x for x in rows if x['claim_id'] == cid)
    assert r['review'] == 'cold', r
    assert r.get('review_note'), r
    print('%-8s in %-28s review=%s' % (cid, d, r['review']))
print('READBACK OK')
