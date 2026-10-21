# -*- coding: utf-8 -*-
"""Append R33.3 and claims S21-67, S21-68."""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, 'outputs')
CJ = os.path.join(HERE, 'claims.jsonl')

BLOCK = u"""### R33.3 - A count that changed meaning, and a damaged file with a future (S21-67, S21-68)

Two closing items, both raised by the operator at the boundary.

**The claim count.** This round reported "66 claims" where every previous round
reported the corpus figure, which stood at 406. The operator flagged the drop
and was right to: a checker reporting a smaller number as OK is exactly this
round's defect class. It was not that. 66 is the size of
`CT-S21-DEPOSIT-PREP/claims.jsonl` alone; the corpus is **413 claims in 22
files**, which is 406 plus the seven appended since, with no duplicate id.
`check_invariants.py` prints its own scope on the first line and was never
narrowed. The defect was in the prose: a number was reused with a different
referent and without saying so. That is the same drift class as the stale hash,
one level up from the bytes, and it is worth recording precisely because the
gate was sound and the sentence was not (S21-67).

**`CT-S1-THEOREM/REPORT.md` has a future, not only a past.** R33.2 recorded the
R1-era backtick damage and left the file alone, correctly, since P0 forbids
modifying an earlier session folder. But that file reports on the theorem that
part (i) is headed for. Two destroyed code spans surviving every gate built
since means the gates were never scanning it, and the remedy at publication is
not to repair the file in place but to **regenerate the report** from its
sources and cite the regenerated one. Citing a known-damaged file because it is
the historical artefact would carry the damage forward into a deposit. Recorded
here so that whoever scopes part (i) meets this before choosing a source
(S21-68).
"""


def h(rel):
    return hashlib.sha256(open(os.path.join(HERE, rel), 'rb').read()).hexdigest()


NEW = [
    ('S21-67', 'VERIFIED', 'build', 'scripts/write_r33_3.py',
     'Reconciliation of the claim count the operator flagged. The corpus is 413 claims in 22 claims.jsonl files '
     'with zero duplicate claim_ids, being the previous 406 plus the seven appended this round. The figure 66 '
     'reported earlier was the size of CT-S21-DEPOSIT-PREP/claims.jsonl alone. check_invariants.py prints '
     '"corpus: 413 claims in 22 files" as its first line, so its scope is corpus-wide and was not narrowed. The '
     'defect was in the reporting prose, which reused a number with a changed referent without saying so.'),
    ('S21-68', 'STRUCTURAL', 'file_inspection', 'scripts/write_r33_3.py',
     'Consequence recorded for part (i): CT-S1-THEOREM/REPORT.md carries R1-era backtick damage and is the report '
     'on the theorem part (i) is headed for. It is not repaired, because P0 forbids modifying an earlier session '
     'folder, so at publication the report must be REGENERATED from its sources and the regenerated file cited. '
     'Citing the historical artefact would carry two destroyed code spans into a deposit. Labelled STRUCTURAL: it '
     'is a decision about future practice, not a verified property of an artefact.'),
]


def main():
    p = os.path.join(OUT, 'r33_3_section.md')
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(BLOCK)
    back = io.open(p, encoding='utf-8').read()
    assert back == BLOCK
    assert not [c for c in back if ord(c) < 0x20 and c != '\n']
    print('r33_3_section.md %d bytes readback OK' % len(back.encode('utf-8')))

    rows = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
    n0 = len(rows)
    have = {r['claim_id'] for r in rows}
    for cid, label, ev, script, txt in NEW:
        if cid in have:
            print('SKIP %s' % cid)
            continue
        rows.append(dict(claim_id=cid, task_id='CT-S21-DEPOSIT-PREP', claim=txt, label=label,
                         evidence_type=ev, dps=None, reproducible=True, script=script,
                         output_hash=h(script)))
    with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
        for x in rows:
            f.write(json.dumps(x, ensure_ascii=False) + '\n')
    back2 = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
    assert back2[-1]['claim_id'] == 'S21-68'
    print('session claims %d -> %d  READBACK OK' % (n0, len(back2)))


if __name__ == '__main__':
    main()
