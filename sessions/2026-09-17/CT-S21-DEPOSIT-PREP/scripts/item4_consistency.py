# -*- coding: utf-8 -*-
"""CT-S21 item 4 - internal consistency of the v1.3 notice.

F4 claim_ids resolve and are not superseded
F5 support-table rows match the live label/review
F6 internal cross-references resolve (files, sessions, section/item numbers)
F7 no sentence asserts author confirmation that has not happened

Vacuity pre-check runs FIRST and must fail on injected bad data, or we halt.
Counts are re-derived in a separate invocation by recount.py.
"""
import json
import os
import re

SESS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
assert os.path.basename(HERE) == 'CT-S21-DEPOSIT-PREP', HERE
assert os.path.basename(SESS) == '2026-09-17', SESS
NOTICE = os.path.join(SESS, 'CT-R1-AUDIT', 'DRAFT-COMPANION-v1.3-NOTICE.md')
OUT = os.path.join(HERE, 'outputs', 'item4_consistency.md')

notice = open(NOTICE, encoding='utf-8').read()

corpus = {}
for root, dirs, names in os.walk(SESS):
    dirs[:] = [d for d in dirs if d not in ('.lake', '__pycache__', '.git')]
    for n in names:
        if n == 'claims.jsonl':
            for line in open(os.path.join(root, n), encoding='utf-8'):
                if line.strip():
                    r = json.loads(line)
                    corpus[r['claim_id']] = r

ID_RX = re.compile(r'`((?:R1|S\d+[A-Z]?|CT-S\d+[A-Z]?-[A-Z0-9]+)-[A-Za-z0-9-]*\d+)`')
SESSION_DIRS = set(os.listdir(SESS))


def check(text, cor):
    """Return (missing, superseded, found) for claim ids cited in text.

    A token that names a session directory is not a claim id; classifying it as
    a missing claim was a false positive in the first run.
    """
    ids = sorted(set(ID_RX.findall(text)))
    ids = [i for i in ids if i not in SESSION_DIRS]
    missing = [i for i in ids if i not in cor]
    superseded = [i for i in ids
                  if i in cor and 'supersede' in json.dumps(cor[i]).lower()]
    return missing, superseded, ids


# ---- VACUITY PRE-CHECK (must fail) ----------------------------------------
vac = []
m, s, _ = check(u'a citation of `R1-99999` here', corpus)
vac.append(('absent id is reported missing', m == ['R1-99999']))
fake = dict(corpus)
fake['R1-56'] = dict(corpus.get('R1-56', {'claim_id': 'R1-56'}))
fake['R1-56']['claim'] = 'this claim is superseded by nothing'
m2, s2, _ = check(u'`R1-56`', fake)
vac.append(('superseded marker is detected', s2 == ['R1-56']))
m3, s3, _ = check(u'`R1-56`', corpus)
vac.append(('clean input yields no false positive', m3 == [] and s3 == []))
VAC_OK = all(v for _, v in vac)
if not VAC_OK:
    raise SystemExit('HALT: vacuity pre-check failed -> the checker measures nothing: %r' % vac)

missing, superseded, ids = check(notice, corpus)

# ---- F5 support-table rows -------------------------------------------------
SUPPORT = [
    ('R1-56', 'STRUCTURAL', 'cold'),
    ('CT-S9-PVPARAMS-C014', 'STRUCTURAL', 'cold'),
    ('R1-57', 'CONJECTURED', 'self'),
    ('S4-06', 'PROVEN', 'cold'),
    ('S5B-C6', 'PROVEN', 'cold'),
]
rows = []
for cid, label, review in SUPPORT:
    r = corpus.get(cid)
    if r is None:
        rows.append((cid, label, review, 'ABSENT', 'ABSENT', False))
        continue
    lab = r.get('label')
    rev = r.get('review') or '(none)'
    rows.append((cid, label, review, lab, rev, lab == label and rev == review))

# ---- F6 referenced files ---------------------------------------------------
files = sorted(set(re.findall(r'`([A-Za-z0-9._-]+\.md)`', notice)))
filestat = []
for f in files:
    hits = []
    for root, dirs, names in os.walk(SESS):
        dirs[:] = [d for d in dirs if d not in ('.lake', '__pycache__', '.git')]
        if f in names:
            hits.append(os.path.relpath(os.path.join(root, f), SESS).replace('\\', '/'))
    filestat.append((f, hits))

sessions = sorted(set(re.findall(r'`(CT-S\d+[A-Z]?(?:-[A-Z0-9]+)+)`', notice)))
sessdirs = set(os.listdir(SESS))
sessions = [s for s in sessions if s not in corpus]
sessstat = [(s, s in sessdirs) for s in sessions]

# ---- F6 internal numbering -------------------------------------------------
defined = set(re.findall(r'^### (C\d)\.', notice, re.M))
cited = set(re.findall(r'\*\*(C\d)\*\*', notice))
num_missing = sorted(cited - defined)

# Prose in this notice is hard-wrapped and often inside a blockquote, so any
# phrase test must run on normalised text. Searching the raw string produced a
# FALSE NEGATIVE at CT-S21: "No published erratum is known to us" was reported
# missing because it wraps as "No published\n> erratum is known to us".
flat = re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*>\s?', '', notice))

# The C4 caveat list. The count word is NOT hardcoded: hardcoding "Four" meant
# that correcting the notice to "Seven" left the detector matching nothing and
# reporting 0 items with no verdict - a check that could no longer fail.
WORDS = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
         'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
c4_m = re.search(r'(\w+) points must accompany this table', flat, re.I)
assert c4_m, 'F6: the C4 caveat-list sentence was not found at all'
c4_word = c4_m.group(1).lower()
assert c4_word in WORDS, 'F6: unrecognised count word %r' % c4_word
c4_said = WORDS[c4_word]
c4 = notice.split(c4_m.group(0))[1] if c4_m.group(0) in notice else \
    notice[notice.lower().index(c4_word + ' points must accompany'):]
c4_items = re.findall(r'^(\d+)\. \*\*', c4, re.M)
c4_agrees = (c4_said == len(c4_items))

# ---- F7 author-confirmation wording ---------------------------------------
PATTERNS = [
    r'the authors (?:have )?confirm',
    r'author-confirmed',
    r'confirmed by (?:the )?(?:authors?|van der Put|Saito|Jimbo)',
    r'acknowledged by the authors',
    r'erratum (?:has been|was) (?:issued|published)',
    r'in press', r'accepted for publication',
]
# A substring search has no polarity: "nothing here is author-confirmed" matches
# the pattern while asserting the opposite. Negated contexts are separated out
# and listed, never silently dropped.
NEGATED = re.compile(r'(nothing (?:here )?is|not|no|never)\s+\S{0,24}$', re.I)
f7, f7_negated = [], []
for p in PATTERNS:
    for mm in re.finditer(p, notice, re.I):
        a = max(0, mm.start() - 90)
        ctx = notice[a:mm.end() + 90].replace('\n', ' ')
        lead = re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*>\s?', '', notice[a:mm.start()]))
        (f7_negated if NEGATED.search(lead) else f7).append((p, ctx))

# the notice's own hedges, tested on the normalised text
hedge = ('no reply had been received when this notice was finalised' in flat.lower())
erratum_hedge = 'No published erratum is known to us' in flat

L = [u'# Item 4 - internal consistency', u'',
     u'Checker: `scripts/item4_consistency.py`. Corpus: every `claims.jsonl` under',
     u'`sessions/2026-09-17/`.', u'',
     u'## Vacuity pre-check (ran first; a pass here is required before any result below)', u'',
     u'| probe | able to fail? |', u'|---|---|']
for name, ok in vac:
    L.append(u'| %s | %s |' % (name, 'yes' if ok else '**NO**'))
L += [u'', u'All three fired as designed, so the checker discriminates.', u'',
      u'## F4 - claim ids cited by the notice', u'',
      u'Cited: %d distinct ids - %s' % (len(ids), ', '.join('`%s`' % i for i in ids)), u'',
      u'- missing from the corpus: **%s**' % (', '.join(missing) if missing else 'none'),
      u'- marked superseded: **%s**' % (', '.join(superseded) if superseded else 'none'),
      u'', u'## F5 - support-table rows against the live claims', u'',
      u'| claim | notice label | notice review | live label | live review | agrees |',
      u'|---|---|---|---|---|---|']
for cid, el, er, al, ar, ok in rows:
    L.append(u'| `%s` | %s | %s | %s | %s | %s |'
             % (cid, el, er, al, ar, 'yes' if ok else '**NO**'))
L += [u'', u'## F6 - cross-references', u'', u'### Files named in the notice', u'',
      u'| file | resolves |', u'|---|---|']
for f, hits in filestat:
    L.append(u'| `%s` | %s |' % (f, hits[0] if len(hits) == 1
                                 else ('**%d copies**: %s' % (len(hits), '; '.join(hits))
                                       if hits else '**NOT FOUND**')))
L += [u'', u'### Sessions named in the notice', u'', u'| session | directory exists |', u'|---|---|']
for s, ok in sessstat:
    L.append(u'| `%s` | %s |' % (s, 'yes' if ok else '**NO**'))
L += [u'', u'### Internal numbering', u'',
      u'- items defined: %s' % ', '.join(sorted(defined)),
      u'- items cited: %s' % ', '.join(sorted(cited)),
      u'- cited but not defined: **%s**' % (', '.join(num_missing) if num_missing else 'none'),
      u'- C4 says **"%s"** and then enumerates **%d**: %s — **%s**'
      % (c4_m.group(0), len(c4_items), ', '.join(c4_items),
         'agrees' if c4_agrees else 'MISMATCH'),
      u'', u'## F7 - author-confirmation wording', u'',
      u'Patterns searched: %s' % ', '.join('`%s`' % p for p in PATTERNS), u'',
      u'- asserting hits: **%s**' % (('%d - see below' % len(f7)) if f7 else 'none'),
      u'- negated hits (listed, not dropped): **%d**' % len(f7_negated),
      u'- the notice keeps a hedge on the letter status: **%s**' % ('yes' if hedge else '**NO**'),
      u'- the notice keeps "No published erratum is known to us": **%s**'
      % ('yes' if erratum_hedge else '**NO**'), u'']
for p, ctx in f7:
    L.append(u'- ASSERTING `%s` -> ...%s...' % (p, ctx))
for p, ctx in f7_negated:
    L.append(u'- negated `%s` -> ...%s...' % (p, ctx))
L.append(u'')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(u'\n'.join(L) + u'\n')

back = open(OUT, encoding='utf-8').read()
assert 'Vacuity pre-check' in back and 'F7' in back, 'readback failed'
print('wrote', OUT, len(back), 'bytes')
print('vacuity ok:', VAC_OK)
print('ids cited:', len(ids), '| missing:', missing, '| superseded:', superseded)
print('support rows disagreeing:', [r[0] for r in rows if not r[5]])
print('files not found:', [f for f, h in filestat if not h])
print('files with multiple copies:', [(f, len(h)) for f, h in filestat if len(h) > 1])
print('sessions missing:', [s for s, ok in sessstat if not ok])
print('cited-but-undefined items:', num_missing)
print('C4 count word vs enumerated:', c4_said, 'vs', len(c4_items),
      '->', 'agrees' if c4_agrees else 'MISMATCH')
print('F7 asserting hits:', len(f7), '| negated hits:', len(f7_negated))
print('hedges present: letter=%s erratum=%s' % (hedge, erratum_hedge))
print('READBACK OK')
