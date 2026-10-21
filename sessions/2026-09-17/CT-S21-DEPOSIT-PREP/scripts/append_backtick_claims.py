# -*- coding: utf-8 -*-
"""Append claims S21-64..66. Written to a file, not passed through -c."""
import hashlib
import io
import json
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CJ = os.path.join(HERE, 'claims.jsonl')


def h(rel):
    return hashlib.sha256(open(os.path.join(HERE, rel), 'rb').read()).hexdigest()


NEW = [
    ('S21-64', 'VERIFIED', 'build', 'scripts/write_r33.py',
     'The backtick is PowerShell\u2019s escape character, so markdown code spans passed through a double-quoted '
     'python -c string are silently mangled. Writing the R33 audit block this way turned the code span for '
     'verify_upload_file.py into byte 0x0b followed by erify_upload_file.py, while the span around references '
     'survived because the following letter is not one PowerShell consumes. The damage is therefore selective: '
     'surviving backticks in the same document read as evidence that nothing is wrong. Caught by append_block.py '
     'refusing control characters before writing; fixed by writing the block from a script file.'),
    ('S21-65', 'VERIFIED', 'file_inspection', 'scripts/scan_backtick_damage.py',
     'Scan of the session tree for the residue of this class: 213 markdown, json and text files scanned, 10 '
     'carrying control characters. Nine are raw pdftotext or OCR output where control bytes are expected. The '
     'tenth, CT-S1-THEOREM/REPORT.md, carries two TAB bytes in prose and shows two markdown code spans destroyed '
     'in the R1 round, every backtick having become a backslash and the backtick-t pair having collapsed to a TAB. '
     'The class therefore predates this round, survived every gate built since, and was found only because an '
     'unrelated write was routed through a control-character-refusing appender. NOT REPAIRED: CT-S1-THEOREM is an '
     'earlier session folder and P0 forbids modifying it.'),
    ('S21-66', 'VERIFIED', 'file_inspection', 'scripts/scan_backtick_damage.py',
     'The deposit object is unaffected by any of the above. DRAFT-COMPANION-v1.3-NOTICE.md and the staged copy '
     'upload/vquad_resurgence_v1.3_correction_notice.md are both 35918 bytes at sha256 '
     'c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c, unchanged across this round, and neither '
     'carries a control character. The upload instruction is unchanged.'),
]


def main():
    rows = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
    n0 = len(rows)
    have = {r['claim_id'] for r in rows}
    for cid, label, ev, script, txt in NEW:
        if cid in have:
            print('SKIP %s already present' % cid)
            continue
        rows.append(dict(claim_id=cid, task_id='CT-S21-DEPOSIT-PREP', claim=txt,
                         label=label, evidence_type=ev, dps=None, reproducible=True,
                         script=script, output_hash=h(script)))
    with io.open(CJ, 'w', encoding='utf-8', newline='\n') as f:
        for x in rows:
            f.write(json.dumps(x, ensure_ascii=False) + '\n')
    back = [json.loads(x) for x in io.open(CJ, encoding='utf-8').read().splitlines() if x.strip()]
    assert len(back) == n0 + len([c for c in NEW if c[0] not in have])
    assert back[-1]['claim_id'] == 'S21-66'
    print('claims %d -> %d  READBACK OK' % (n0, len(back)))


if __name__ == '__main__':
    main()
