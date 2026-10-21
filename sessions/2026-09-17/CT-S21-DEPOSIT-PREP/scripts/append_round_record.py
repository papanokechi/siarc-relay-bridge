# -*- coding: utf-8 -*-
"""Append the CT-S21 round to AUDIT.md and DEPOSIT-DEPENDENCIES.md."""
import os

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESS = os.path.dirname(HERE)
AUD = os.path.join(SESS, 'CT-R1-AUDIT', 'AUDIT.md')
DEP = os.path.join(SESS, 'CT-R1-AUDIT', 'DEPOSIT-DEPENDENCIES.md')

A_MARK = '## R23 — CT-S21 deposit preparation'
A = '''
''' + A_MARK + '''

Packet `CT-S21-DEPOSIT-PREP`, then the operator ruling on M1. Output
`CT-S21-DEPOSIT-PREP/DEPOSIT-READY.md`; claims `S21-01` .. `S21-23`.

**Round 1 — the gate.** Re-fetched all five cited sources (four byte-identical
to the local copies), read ten page images one per message, recorded licence
strings as printed, and ran the consistency scan. Verdict: **not ready**, six
items. The largest was not an error in the notice: **C5's tabulation was
incomplete**, and incomplete in the companion's favour.

**The Theorem 3.1 finding.** v1.2's own §3 already proves C1's local analysis —
`p₀ = 1`, `q₀ = 0`, `I(ρ) = ρ² = 0`, the logarithm in `y₂` only — and Step 4
**displays the monodromy as `[[1, 2πi], [0, 1]]`**, unipotent and not the
identity. Theorem 3.1(ii)'s claim is about the *effective* monodromy on `M₁₁`,
which is weaker than and independent of apparency. The notice as drafted would
have read as though §3 fell with Remark 2.2.

**Round 2 — the ruling applied.** C1 gained a scope limitation; C5 gained the
`Remark 3.2` row and a statement of three deliberate exclusions:

| passage | rests on | in C5? |
|---|---|---|
| Remark 3.2 | apparency, stated flatly without the `M₁₁` qualifier | **yes**, dependency only |
| Remark 4.2 | `θ₁ = θ₂ = 0`, which **survives C1** | no |
| Remark 6.7 | Theorem 3.1(ii), unadjudicated | no |
| Theorem 3.1 | — it is the *source* of the correct computation | no; under C1 |

`θ₁ = θ₂ = 0` survives because it is the difference of the local exponents,
both `0` by the double root C1 establishes; `θ = 0` is exactly the resonant case
in which logarithms occur. **C2 is therefore safe**, resting on those values.

**Three defects in the gate itself**, all found by reading output rather than
exit codes, and all now controlled by `scripts/control_item4.py`:

1. a **false negative from hard wrapping** — a hedge reported missing that was
   present, wrapped across a blockquote line;
2. a **check that could no longer fail** — the C4 test hardcoded `"Four
   points"`, so correcting the notice to `"Seven"` left it matching nothing and
   passing silently. The seventh amendment's failure mode, inside the gate built
   to catch it;
3. a **substring search with no polarity** — `author-confirmed` matched the
   notice's own `"nothing here is author-confirmed"`.

**Corrections to my own record.** `R1-107` ("zero third-party bytes would be
staged") was **false** and is amended in place: nine third-party files were
still stageable. `.gitignore` now default-denies media, verified by effect,
17 → 0. An earlier draft of `DEPOSIT-READY.md` also mislisted the CT-S18/S19
packet images as exposed; re-deriving the count corrected it.

**Result: the notice is ready**, subject to two deposit-day confirmations.
'''

D_MARK = '## R23 — deposit gate cleared'
D = '''
''' + D_MARK + '''

`CT-S21-DEPOSIT-PREP` cleared the remaining deposit-side items.

| item | was | now |
|---|---|---|
| C5 tabulation complete | incomplete (4 passages unexamined) | Remark 3.2 added; Remarks 4.2, 6.7, Theorem 3.1 excluded with reasons |
| C1 scope vs §3 | unstated | scope limitation in C1, point 3 |
| C3 letter status | placeholder, "had not been sent" | authors notified; no reply at finalisation |
| `S4-06`, `S5B-C6` review | `None` in corpus, `cold` in notice | `cold` written back, with `review_note` |
| C4 count | "Four", enumerating seven | "Seven"; checked programmatically |
| family (4.1) page | "p. 2655" | unchanged **by ruling**; letter already sent |
| commit-side media | 17 stageable, 9 third-party | **0**, verified by effect |

**Remaining before deposit:** confirm no author reply has arrived (C3), and run
the standing deposit-day citation checklist. `R1-57` is still the sole `self`
row and is disclosed in the notice.
'''

for path, mark, text in ((AUD, A_MARK, A), (DEP, D_MARK, D)):
    before = open(path, encoding='utf-8').read()
    assert mark not in before, 'already appended: ' + path
    with open(path, 'a', encoding='utf-8') as f:
        f.write(text)
    back = open(path, encoding='utf-8').read()
    assert mark in back, 'readback: section missing from ' + path
    print('%-28s %d -> %d lines' % (os.path.basename(path),
                                    before.count('\n'), back.count('\n')))
print('READBACK OK')
