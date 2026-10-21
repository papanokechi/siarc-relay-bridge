# -*- coding: utf-8 -*-
"""Write the R33.2 block and the P0 line from a file, never through -c."""
import io
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, 'outputs')

R332 = u"""### R33.2 - The damage is older than today, and it is in the record (S21-65)

Having identified the backtick as the cause, the session tree was scanned for
the residue rather than for the cause: any control character in a markdown,
json or text file, with raw PDF extractions excluded by path.

213 files scanned, 10 carrying control characters. Nine are raw pdftotext or
OCR output under `CT-S8-LITCHECK/refs/`, `CT-S15-COLDREAD-DEFERRED/`,
`CT-S16-MEMBERSHIP-C/outputs/` and `CT-S21-DEPOSIT-PREP/outputs/`, where
control bytes are the normal residue of extracting mathematics from a PDF and
carry no meaning. Those are expected and were already the known exception.

The tenth is not. `CT-S1-THEOREM/REPORT.md` carries two TAB bytes, and reading
them in context shows the same defect, from the R1 round:

    > **AMENDED IN AUDIT ROUND R1** (see \\../CT-R1-AUDIT/AUDIT.md\\).
    > (1) Theorem \\<TAB>hm:radius\\ Step 3 contained ...

Two markdown code spans have been destroyed. Every backtick became a backslash,
and where the backtick preceded a `t` the pair collapsed to a TAB, so
`` `thm:radius` `` reads as a backslash, a tab, and `hm:radius`. The label is
unrecoverable from the text alone; it is legible only because the surrounding
sentence still names Theorem and Step 3.

So this class is not a defect of today's round. It has been latent in the
record since R1, it survived every gate built since, and it was found only
after an unrelated write was routed through an appender that refuses control
characters. The five invariants do not look at bytes. That is the same finding
as "gates that check claims do not check bytes", one level further down: the
byte check that exists was pointed at the deposit object, and the record around
it was never in scope.

**Not repaired.** `CT-S1-THEOREM/` is an earlier session folder and P0 forbids
modifying it. The damage is recorded here and the file left as it is. Anyone
reading that report should know the two mangled spans are `` `../CT-R1-AUDIT/AUDIT.md` ``
and `` `thm:radius` ``, on the evidence of the surrounding sentence rather than
of the bytes.

**The deposit object is clean.** `DRAFT-COMPANION-v1.3-NOTICE.md` and the
staged `upload/` copy both remain 35918 bytes at
`c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c`, carry no
control characters, and were not touched by any of this. Nothing here changes
the deposit (S21-66).
"""

P0 = u"""
- **Never pass markdown through a double-quoted PowerShell string.** The
  backtick is PowerShell's escape character, so a code span opener followed by
  a, b, e, f, n, r, t, v or 0 is silently consumed. The damage is selective:
  most backticks in a document survive, and their survival reads as evidence
  that nothing is wrong. Write the text to a file and run the file. The rule is
  not "escape the backticks" - enumerating the affected letters is the
  coverage-list mistake this file already warns about. (R33.1, R33.2)
- **Route every write to a recorded file through an appender that refuses
  control characters**, and give that appender a two-sided control: one input
  it must reject, one it must accept. A control that fails for the same reason
  as the run it is controlling certifies nothing. (R33.1)
"""

for name, text in (('r33_2_section.md', R332), ('p0_backtick.md', P0)):
    p = os.path.join(OUT, name)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    back = io.open(p, encoding='utf-8').read()
    assert back == text, name
    bad = [c for c in back if ord(c) < 0x20 and c != '\n']
    assert not bad, '%s control chars %r' % (name, bad)
    print('%-22s %5d bytes  readback OK  no control chars'
          % (name, len(back.encode('utf-8'))))
