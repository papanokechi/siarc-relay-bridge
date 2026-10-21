# Item 4 - internal consistency

Checker: `scripts/item4_consistency.py`. Corpus: every `claims.jsonl` under
`sessions/2026-09-17/`.

## Vacuity pre-check (ran first; a pass here is required before any result below)

| probe | able to fail? |
|---|---|
| absent id is reported missing | yes |
| superseded marker is detected | yes |
| clean input yields no false positive | yes |

All three fired as designed, so the checker discriminates.

## F4 - claim ids cited by the notice

Cited: 5 distinct ids - `CT-S9-PVPARAMS-C014`, `R1-56`, `R1-57`, `S4-06`, `S5B-C6`

- missing from the corpus: **none**
- marked superseded: **none**

## F5 - support-table rows against the live claims

| claim | notice label | notice review | live label | live review | agrees |
|---|---|---|---|---|---|
| `R1-56` | STRUCTURAL | cold | STRUCTURAL | cold | yes |
| `CT-S9-PVPARAMS-C014` | STRUCTURAL | cold | STRUCTURAL | cold | yes |
| `R1-57` | CONJECTURED | self | CONJECTURED | self | yes |
| `S4-06` | PROVEN | cold | PROVEN | cold | yes |
| `S5B-C6` | PROVEN | cold | PROVEN | cold | yes |

## F6 - cross-references

### Files named in the notice

| file | resolves |
|---|---|
| `DEPOSIT-DEPENDENCIES.md` | CT-R1-AUDIT/DEPOSIT-DEPENDENCIES.md |
| `LOADBEARING-TEST.md` | CT-R1-AUDIT/LOADBEARING-TEST.md |
| `VERIFY-S14.md` | CT-R1-AUDIT/VERIFY-S14.md |
| `VERIFY-S15.md` | CT-R1-AUDIT/VERIFY-S15.md |
| `VERIFY-S18.md` | CT-S18-COLDREAD-C3/VERIFY-S18.md |

### Sessions named in the notice

| session | directory exists |
|---|---|
| `CT-S14-COLDREAD-B` | yes |
| `CT-S15-COLDREAD-DEFERRED` | yes |
| `CT-S18-COLDREAD-C3` | yes |
| `CT-S19-COLDREAD-MEMBERSHIP` | yes |

### Internal numbering

- items defined: C1, C2, C3, C4, C5
- items cited: C1, C2, C3, C4, C5
- cited but not defined: **none**
- C4 says **"Seven points must accompany this table"** and then enumerates **7**: 1, 2, 3, 4, 5, 6, 7 — **agrees**

## F7 - author-confirmation wording

Patterns searched: `the authors (?:have )?confirm`, `author-confirmed`, `confirmed by (?:the )?(?:authors?|van der Put|Saito|Jimbo)`, `acknowledged by the authors`, `erratum (?:has been|was) (?:issued|published)`, `in press`, `accepted for publication`

- asserting hits: **none**
- negated hits (listed, not dropped): **1**
- the notice keeps a hedge on the letter status: **yes**
- the notice keeps "No published erratum is known to us": **yes**

- negated `author-confirmed` -> ...l; **no reply had > been received when this notice was finalised**, and nothing here is > author-confirmed.  Two limitations attach to the affine matching and should be stated with it: the identif...

