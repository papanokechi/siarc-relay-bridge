"""Build REFS-MANIFEST.md (the artefact the 'manifest route' has so far only
named) and the .gitignore that makes the refs/ hold mechanical rather than
declarative.  Writes, then reads back, and fails loudly.
"""
import hashlib
import os
import re

SESS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT = os.path.join(SESS, 'CT-R1-AUDIT')
REVIEW = os.path.join(AUDIT, 'REFS-LICENCE-REVIEW.md')
MAN = os.path.join(AUDIT, 'REFS-MANIFEST.md')
GI = os.path.join(SESS, '.gitignore')

OWN = ('vquad_resurgence_', 'companion_v12_')
DERIVED_EXT = ('.py',)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


files = []
for root, dirs, names in os.walk(SESS):
    dirs[:] = [d for d in dirs if d not in ('.lake', '__pycache__', '.git')]
    parts = os.path.relpath(root, SESS).split(os.sep)
    if not ({'refs', 'pages'} & set(parts)):
        continue
    for n in names:
        p = os.path.join(root, n)
        files.append((os.path.relpath(p, SESS).replace('\\', '/'), os.path.getsize(p), sha(p)))
files.sort()

with open(REVIEW, encoding='utf-8') as f:
    review = f.read()


def listed(rel):
    base = os.path.basename(rel)
    if base in review:
        return True
    stem = re.split(r'[_.]', base)[0]
    # the review lists some rows by glob, e.g. vdPS_p*.png, vquad_resurgence_v1.0/v1.1/v1.2*
    for pat in re.findall(r'`([^`]+)`', review):
        pat = pat.strip()
        if '*' in pat:
            rx = re.escape(pat).replace(r'\*', '.*')
            if re.search(rx.split('/')[-1], base):
                return True
        elif pat.endswith(base) or base in pat:
            return True
    return bool(stem) and stem in review and len(stem) > 6


rows, unlisted, own_n, code_n = [], [], 0, 0
for rel, size, h in files:
    base = os.path.basename(rel)
    if base.endswith(DERIVED_EXT):
        cls, note = 'session-produced', 'written in this run; not third-party material'
        code_n += 1
    elif base.startswith(OWN):
        cls, note = "operator's own", \
            "operator's own deposit; deposit licence field **NOT CHECKED**"
        own_n += 1
    else:
        cls, note = 'third-party', 'redistribution permission **NOT CHECKED**'
    inv = 'yes' if listed(rel) else '**no row**'
    if inv != 'yes' and cls == 'third-party':
        unlisted.append(rel)
    rows.append((rel, size, h, cls, inv, note))

L = ["# `refs/` manifest — hashes, not bytes", "",
     "*Built at R21. This is the artefact the \"manifest route\" has until now only",
     "named: `REFS-LICENCE-REVIEW.md` **recommended** committing a manifest instead",
     "of the files, and the recommendation was adopted in prose, but no manifest",
     "file existed and nothing excluded `refs/` from a commit.*", "",
     "A hash proves a later reader fetched the same bytes. The bytes themselves",
     "stay out of the repository under the standing hold (review #15).", "",
     "## What a commit would have staged before this round", "",
     "`sessions/2026-09-17/` was, and remains, untracked. There was **no**",
     "`.gitignore` anywhere above `CT-S1-THEOREM/lean/`, so `git add sessions/`",
     "would have staged **all %d** files below — including the whole-page AIF" % len(files),
     "renders and the Gautschi page image, the two items the review names",
     "explicitly as DO NOT COMMIT. That is now prevented mechanically by",
     "`sessions/2026-09-17/.gitignore`.", "",
     "## Inventory", "",
     "`in review?` records whether the file has a row in `REFS-LICENCE-REVIEW.md`.",
     "**No licence determination is made here.** Every third-party row is",
     "**NOT CHECKED**, which is what the review says and what the deposit-day pass",
     "is for.", "",
     "| file | bytes | sha256 | class | in review? | licence |",
     "|---|---|---|---|---|---|"]
for rel, size, h, cls, inv, note in rows:
    L.append("| `%s` | %d | `%s` | %s | %s | %s |" % (rel, size, h, cls, inv, note))

L += ["", "## Finding: the inventory was incomplete", "",
      "The standing hold reads *\"everything under any `refs/` directory\"*, so the",
      "files below **are** covered by it. But the review's inventory table has no",
      "row for any of them, so nothing had ever been enumerated or hashed:", ""]
for u in unlisted:
    L.append("- `%s`" % u)
L += ["",
      "That is %d third-party files, among them complete third-party articles"
      % len(unlisted),
      "rather than page regions. The hold's wording covered them; the inventory did",
      "not. Wording is not a mechanism — this is the same lesson as the `.gitignore`",
      "above, one level up.", "",
      "## Counts", "",
      "- %d files total under `refs/` or `pages/`" % len(files),
      "- %d operator's own deposits or renders of them" % own_n,
      "- %d session-produced scripts (kept in the commit by an explicit negation)" % code_n,
      "- %d third-party files with **no** licence determination" % (len(files) - own_n - code_n),
      "",
      "## Rule", "",
      "No row here moves from **NOT CHECKED** except by reading the licence on the",
      "item itself — the article's own title page, or the arXiv abstract page for",
      "that submission, or the Zenodo record's `metadata.rights`. The status of a",
      "publisher, a venue, or a neighbouring row clears nothing.", ""]

with open(MAN, 'w', encoding='utf-8') as f:
    f.write("\n".join(L) + "\n")

GITIGNORE = """# Added R21. The refs/ hold (REFS-LICENCE-REVIEW.md, review #15) is a
# redistribution question and only arises on commit. Until each row of
# REFS-MANIFEST.md is individually checked, no reference file or page image is
# committed. Hashes travel in REFS-MANIFEST.md instead; the bytes stay in the
# off-repo backup.
#
# Patterns exclude directory CONTENTS, not the directories, so the negation
# below can re-include session-produced scripts.
**/refs/*
**/pages/*
!**/refs/*.py
!**/pages/*.py

# Build tree: ~124k files. Also excluded from the backup by make_backup.py.
**/.lake/
**/__pycache__/
"""
with open(GI, 'w', encoding='utf-8') as f:
    f.write(GITIGNORE)

# ---- read back -------------------------------------------------------------
with open(MAN, encoding='utf-8') as f:
    mb = f.read()
with open(GI, encoding='utf-8') as f:
    gb = f.read()
assert mb.count('| `') >= len(files), 'manifest rows missing'
assert 'NOT CHECKED' in mb and '## Finding' in mb, 'manifest content missing'
assert '**/refs/*' in gb and '!**/refs/*.py' in gb, 'gitignore content missing'
print('manifest: %s (%d bytes, %d files)' % (MAN, len(mb), len(files)))
print('gitignore: %s (%d bytes)' % (GI, len(gb)))
print('third-party unlisted in the review: %d' % len(unlisted))
for u in unlisted:
    print('   ', u)
print('READBACK OK')
