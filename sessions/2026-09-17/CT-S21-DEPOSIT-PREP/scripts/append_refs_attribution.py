# -*- coding: utf-8 -*-
"""Amend S21-26 in place and append the round's new claims.

P0: the amendment rewrites the claim rather than deleting it, keeps a .bak, and
the file is re-read and re-counted in a SEPARATE invocation by
check_invariants.py. Every appended claim names its script and output hash.
"""
import hashlib
import io
import json
import os
import shutil

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJ = os.path.join(HERE, 'claims.jsonl')
OUT = os.path.join(HERE, 'outputs')


def h(name):
    p = os.path.join(OUT, name)
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ---------- 1. amend S21-26 --------------------------------------------------
shutil.copy2(CJ, CJ + '.bak-s21refs')
lines = io.open(CJ, encoding='utf-8').read().splitlines()
rows = [json.loads(x) for x in lines if x.strip()]
n_before = len(rows)

hit = [r for r in rows if r['claim_id'] == 'S21-26']
assert len(hit) == 1, 'expected exactly one S21-26, got %d' % len(hit)
r = hit[0]
assert 'CONJECTURED' in json.dumps(r), 'S21-26 was not CONJECTURED: %s' % r
r['claim'] = (
    "SUPERSEDED BY S21-28. The content attributed to arXiv:2306.05930 is "
    "LOCATED and quoted: printed p. 5, section 2.3 'Asymptotics'. The "
    "attribution was substantively correct but the paraphrase overstated it - "
    "the paper says 'we do not know how to compute the leading coefficient "
    "exactly in general' (state of the art), NOT that it is not computable "
    "(a claim about the world). Background in the preliminaries, not a theorem "
    "of theirs: their contribution starts at section 3, p. 6.")
r['label'] = 'INSPECTED'
r['superseded_by'] = 'S21-28'
r['amended'] = '2026-09-18'
r['amend_note'] = ('was CONJECTURED pending location of the passage; located '
                   'from a rendered page image in this round')

# ---------- 2. append ---------------------------------------------------------
NEW = [
    dict(claim_id='S21-28',
         claim=("arXiv:2306.05930 (Ibrahim & Salvy), printed p. 5, section 2.3, "
                "prints verbatim: 'we do not know how to compute the leading "
                "coefficient exactly in general. Currently, the closest we have "
                "is a certified numerical approximation in the form of an "
                "interval that can be made arbitrarily small, but 0 cannot be "
                "excluded. This is known as the connexion problem for linear "
                "differential equations.' Read from a rendered page image."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/locate_passages.py', dps=None, reproducible=True,
         output_file='pages/salvy_printed5_idx4.png'),
    dict(claim_id='S21-29',
         claim=("The remark at S21-28 is BACKGROUND, not a result of that paper: "
                "it sits in section 2.3 within the preliminaries, while the "
                "authors' own contribution begins at section 3 'Positivity "
                "certificates', Definition 3, printed p. 6. If cited in v1.7 it "
                "must be cited as a statement of the standard situation."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/locate_passages.py', dps=None, reproducible=True,
         output_file='outputs/refs_attribution.md'),
    dict(claim_id='S21-30',
         claim=("Wong & Zhao (arXiv:2204.09305) section 3 DOES cover this "
                "project's equation class: equation (3.2), y(n+2) + n^p a(n) "
                "y(n+1) + n^q b(n) y(n) = 0, attributed to Wong & Li [100]. "
                "The operator's reading is confirmed on this point."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/wz_sec3_absence.py', dps=None, reproducible=True,
         output_file='outputs/wz_sec3_absence.json'),
    dict(claim_id='S21-31',
         claim=("ABSENCE CLAIM, stated with scope: the growth law "
                "Q_n/Gamma(dn+1) ~ K (beta_d/d^d)^n n^s, the exponent "
                "s = beta_{d-1}/beta_d + (d-1)/2, and any explicit leading "
                "constant are NOT FOUND in Wong & Zhao section 3 (PDF pp. 12-20) "
                "by full-text read. Six positive controls fired first over the "
                "same extracted string, so the test was not vacuous (S17-22); "
                "had any control failed the script emits VOID and no absence "
                "verdict. NOT phrased as 'the survey does not state it'."),
         label='INSPECTED', evidence_type='computation',
         script='scripts/wz_sec3_absence.py', dps=None, reproducible=True,
         output_file='outputs/wz_sec3_absence.json'),
    dict(claim_id='S21-32',
         claim=("STRUCTURAL reason the growth law is absent from Wong & Zhao "
                "section 3: at (3.23) the section defines K_n by "
                "K_{n+1}/K_{n-1} = c_n and sets x_n = y_n/K_n, so K_n absorbs "
                "exactly the product growth and Theorems 3.1-3.3 describe x_n by "
                "uniform Airy/Bessel expansions near transition points. It is a "
                "turning-point theory in a parameter; the growth constant is "
                "normalised out of view, and K_0, K_1 are left depending on the "
                "particular sequence. This corroborates S21-28: the constant is "
                "the part tied to initial conditions."),
         label='STRUCTURAL', evidence_type='file_inspection',
         script='scripts/wz_sec3_absence.py', dps=None, reproducible=True,
         output_file='outputs/wz_sec3_text.txt'),
    dict(claim_id='S21-33',
         claim=("The CC-BY-4.0 determination for both refs/ arXiv PDFs is now "
                "VERSION-PINNED to the bytes held: page-1 stamps read "
                "'arXiv:2204.09305v1 [math.CA] 20 Apr 2022' and "
                "'arXiv:2306.05930v2 [cs.SC] 3 Nov 2023', and the versioned "
                "abstract pages /abs/2204.09305v1 and /abs/2306.05930v2 both "
                "print http://creativecommons.org/licenses/by/4.0/. arXiv "
                "licences are per-submission AND per-version; the licence was "
                "read from the abstract page, never from the PDF."),
         label='INSPECTED', evidence_type='file_inspection',
         script='scripts/arxiv_versions.py', dps=None, reproducible=True,
         output_file='outputs/abs_2204.09305v1.html'),
    dict(claim_id='S21-34',
         claim=("DEFECT FOUND AND REPAIRED in AUDIT.md section R24: four sites "
                "where a Python source literal interpreted \\r (in '\\refs/', "
                "'\\r_infinity') and \\a (in '\\acquire_refs.py') as escapes. A "
                "later text-mode read-modify-write promoted each lone CR to a "
                "full CRLF, so the damage presented as spurious line breaks. "
                "NEW FAILURE MODE FOR P0: the readback rule did not catch this, "
                "because the script read back the same already-mangled string it "
                "wrote. Readback proves a write happened, NOT that the intended "
                "text was written. Remaining stray control characters in the "
                "tree are confined to raw PDF text extractions under "
                "CT-S9-PVPARAMS/outputs/, where they are source artefacts."),
         label='VERIFIED', evidence_type='build',
         script='scripts/scan_escape_damage.py', dps=None, reproducible=True,
         output_file='outputs/refs_attribution.md'),
]

for c in NEW:
    c['task_id'] = 'CT-S21-DEPOSIT-PREP'
    c['output_hash'] = h(os.path.basename(c['output_file'])) \
        if c['output_file'].startswith('outputs/') else None
    rows.append(c)

ids = [x['claim_id'] for x in rows]
assert len(ids) == len(set(ids)), 'duplicate claim_id'

with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
    for x in rows:
        f.write(json.dumps(x, ensure_ascii=False) + '\n')

# ---------- 3. readback -------------------------------------------------------
back = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
assert len(back) == n_before + len(NEW), \
    'count wrong: %d -> %d, expected +%d' % (n_before, len(back), len(NEW))
got = {x['claim_id']: x for x in back}
assert got['S21-26']['label'] == 'INSPECTED' and got['S21-26']['superseded_by'] == 'S21-28'
for c in NEW:
    assert c['claim_id'] in got, 'missing %s' % c['claim_id']
    assert got[c['claim_id']]['claim'] == c['claim'], 'text mismatch %s' % c['claim_id']
print('claims %d -> %d (+%d), S21-26 amended' % (n_before, len(back), len(NEW)))
print('READBACK OK')
