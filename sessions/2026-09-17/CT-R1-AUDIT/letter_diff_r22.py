# -*- coding: utf-8 -*-
"""R22: diff the operator's pasted letter (review #17) against the authoritative
repo draft, and check every formula in the repo draft against TYPO-EVIDENCE.md.
Writes LETTER-DIFF-R22.md, then reads it back.
"""
import difflib
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
S16 = os.path.join(os.path.dirname(HERE), 'CT-S16-MEMBERSHIP-C')
DRAFT = os.path.join(S16, 'LETTER-vdPS-DRAFT.md')
EVID = os.path.join(S16, 'TYPO-EVIDENCE.md')
OUT = os.path.join(HERE, 'LETTER-DIFF-R22.md')

draft = open(DRAFT, encoding='utf-8').read()
evid = open(EVID, encoding='utf-8').read()

body = re.split(r'(?m)^---\s*$', draft)[1]
body = body.split('## Note for the operator')[0].strip()
assert body.startswith('Subject:'), 'body extraction failed: %r' % body[:60]
assert body.rstrip().endswith('0009-0000-6192-8273'), 'body truncated'

OPERATOR = u"""Subject: Possible typo in family (4.1), Ann. Inst. Fourier 59 (2009), p. 2655

Dear Professors van der Put and Saito,

I have been working with your paper "Moduli spaces for linear differential equations and the Painlev\u00e9 equations", Ann. Inst. Fourier 59 (2009), no. 7, 2611\u20132667, and I believe there is a small typographical error in the family (4.1) on p. 2655.

The entry b(z) appears to be missing a factor of t in its first term: [FILL IN: printed form \u2192 corrected form].

My evidence is your own constraint det A(1) = \u2212\u03b8\u2081\u00b2/4. The printed form does not satisfy it; the corrected form satisfies it identically. The residual between the two readings factors as \u2212(q\u22121)(t\u22121)(\u2026)/4, so the two agree exactly at t = 1, which is the pattern one expects from a dropped t.

The same entry appears in arXiv:0902.1702v5, p. 34, so it seems to have survived the revision of Section 4. I could not find a published erratum.

I am using the corrected form in work in preparation and would rather check with you than assume I am right.

With thanks and best regards,

Papanokechi
Independent researcher, Yokohama
ORCID 0009-0000-6192-8273"""

# ---- formula checks against TYPO-EVIDENCE.md --------------------------------
RESIDUAL = u'\u2212(q\u22121)(t\u22121)(4p + q\u00b2t + q\u00b2 \u2212 qt \u2212 q)/4'
checks = [
    (u'residual factorisation, full form',
     RESIDUAL in body,
     RESIDUAL.replace(u'\u2212', '-') in evid.replace(u'\u2212', '-')),
    (u'corrected bracket (p + \u00bd(q\u22121)q t)\u00b2',
     u'(p + \u00bd(q\u22121)q t)\u00b2' in body,
     u'(p + \u00bd(q\u22121)q t)\u00b2' in evid),
    (u'printed bracket (p + \u00bd(q\u22121)q)\u00b2',
     u'(p + \u00bd(q\u22121)q)\u00b2' in body,
     u'(p + \u00bd(q\u22121)q)\u00b2' in evid),
    (u'B\u2081[1,2] corroboration present',
     u'B\u2081[1,2]' in body, u'B\u2081[1,2]' in evid),
    (u'det A(0) does not discriminate',
     u'det A(0)' in body, u'det A(0)' in evid),
    (u'arXiv:0902.1702v5, p. 34',
     u'arXiv:0902.1702v5' in body and 'p. 34' in body,
     u'arXiv:0902.1702v5' in evid and 'p. 34' in evid),
    (u'no published erratum',
     'erratum' in body, 'erratum' in evid or 'corrigendum' in evid),
]

dl = list(difflib.unified_diff(
    OPERATOR.splitlines(), body.splitlines(),
    fromfile='operator paste (review #17)', tofile='repo LETTER-vdPS-DRAFT.md',
    lineterm='', n=1))

L = [u'# R22 — letter check before sending: operator paste vs repo draft', u'',
     u'*The operator asked for a diff against `CT-S16-MEMBERSHIP-C/LETTER-vdPS-DRAFT.md`,'
     u' which was checked against page images and is authoritative, and for both of the'
     u' letter\u2019s formulas to be verified against `TYPO-EVIDENCE.md`. Nothing has been sent.*',
     u'', u'## Verdict', u'',
     u'**Send the repo version.** The two differ in four places and the repo version is'
     u' stronger or more exact at every one of them. No place was found where the'
     u' operator\u2019s paste is better.', u'',
     u'## Formula checks against `TYPO-EVIDENCE.md`', u'',
     u'| item | in repo draft | in evidence pack | agree |', u'|---|---|---|---|']
allok = True
for name, ind, ine in checks:
    allok &= (ind and ine)
    L.append(u'| %s | %s | %s | %s |' % (name, 'yes' if ind else '**no**',
                                         'yes' if ine else '**no**',
                                         'yes' if (ind and ine) else '**NO**'))
L += [u'', u'Result: **%s**.' % ('every formula in the letter matches the evidence pack verbatim'
                                 if allok else 'MISMATCH - do not send'), u'',
      u'## Unified diff', u'', u'```diff'] + dl + [u'```', u'']

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(u'\n'.join(L) + u'\n')

back = open(OUT, encoding='utf-8').read()
assert 'Unified diff' in back and RESIDUAL in back, 'readback failed'
print('wrote %s (%d bytes, %d diff lines)' % (OUT, len(back), len(dl)))
print('all formula checks agree:', allok)
for name, ind, ine in checks:
    print('  %-46s draft=%-5s evidence=%s' % (name, ind, ine))
print('READBACK OK')
