# -*- coding: utf-8 -*-
"""Deposit shape change: keep the paper in the record; stage the upload copy.

Also fixes a filename that would have published as "DRAFT-...".
"""
import hashlib
import io
import os
import shutil

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT = os.path.join(os.path.dirname(HERE), 'CT-R1-AUDIT')
NOTICE = os.path.join(AUDIT, 'DRAFT-COMPANION-v1.3-NOTICE.md')
UPDIR = os.path.join(HERE, 'upload')
UPNAME = 'vquad_resurgence_v1.3_correction_notice.md'


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


os.makedirs(UPDIR, exist_ok=True)
dst = os.path.join(UPDIR, UPNAME)
shutil.copyfile(NOTICE, dst)
assert sha(dst) == sha(NOTICE), 'copy differs from source'
print('staged %s' % UPNAME)
print('  sha256 %s' % sha(dst))
print('  identical to the notice: True')
print('  source filename began "DRAFT-" and would have published as such')

# --- A2 in the walkthrough ---
wp = os.path.join(HERE, 'DEPOSIT-WALKTHROUGH.md')
w = io.open(wp, encoding='utf-8').read()
old = ('**Deposit: the notice only.** Decide its form (PDF render, or the Markdown as\n'
       'deposited) — that choice is yours and is not recorded anywhere as settled.')
new = ("**Deposit: the notice ALONGSIDE the v1.2 PDF.** *(Superseded the earlier\n"
       "\"notice only\" reading — operator ruling, see AUDIT §R31.)* A new version whose\n"
       "sole file is an erratum makes the concept DOI resolve to a record where the paper\n"
       "itself is absent, so anyone following a citation lands on a correction with\n"
       "nothing to correct.\n"
       "\n"
       "Note the mechanics: on Zenodo **New version**, the previous files are carried\n"
       "over by default. Keeping the paper is therefore the *default*, and the notice-only\n"
       "shape would have required actively **deleting** `vquad_resurgence.pdf` from the\n"
       "draft. So: **do not delete it**, and **add** the notice beside it.\n"
       "\n"
       "The held copy `refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` is byte-identical\n"
       "to the deposited file (612 719 bytes, md5 `4d1e4d59…`), so if the carry-over ever\n"
       "has to be redone by hand it can be re-uploaded without altering the paper.\n"
       "\n"
       "The notice's own form (Markdown as-is, or a PDF render) remains your choice; a\n"
       "render has its own hash.")
assert old in w, 'A2 text not found'
w = w.replace(old, new)
io.open(wp, 'w', encoding='utf-8', newline='').write(w)
chk = io.open(wp, encoding='utf-8').read()
assert new in chk and 'Deposit: the notice only.' not in chk
print('A2 updated; stale "notice only" gone')
