# CMB §OPEN QUESTIONS FOR T1 SYNTH — W20 entries for 051

Substrate file for the W20 (Mon 2026-05-11) T1 Synth weekly
arbitration cycle. Drafted Wed 2026-05-06 ~16:30 JST as
deliverable for operator decision (b) "T2 drafts 3 OQ entries
this week" authorized in same chat round as decisions
(c) OPT_C2 + (d) LATE-FIRE post-W20.

## Source of truth

The 3 OQ entries below paraphrase the verbatim content of
`bt_baseline_note.tex` §6 (Open questions and follow-on phases),
lines 696-768, of the deposit at:

- Bridge folder:
  `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/`
- Zenodo concept DOI: `10.5281/zenodo.20048196`
- Zenodo version DOI: `10.5281/zenodo.20048197` (v1.0)
- PDF SHA-256:
  `23022f0de77ac8388ed584b2196c0ab995cd8cf18b2dd71efbc0488a0f6e5b7c`

## Mapping of note §6 problems to SQL Q-numbering

| Note label   | SQL todo                              | OQ key    |
|--------------|---------------------------------------|-----------|
| `q:mechanism`     | `w20-synth-051-q1-dge3-A2d-gap`            | Q1 |
| `q:borderline-Q`  | `w20-synth-051-q2-borderline-Q-ansatz-gap` | Q2 |
| `q:Afit-def`      | (folded into Q1's (ii') branch; not split) | --  |
| `q:sectorial`     | `w20-synth-051-q4-sectorial-upgrade-gap`   | Q4 |

Note §6 has 4 problems; SQL tracks 3 (Q1/Q2/Q4) because Q3 =
`q:Afit-def` is the (ii') sub-question of `q:mechanism` and is
arbitrated jointly with Q1.

## OQ entry bodies (verbatim for paste into CMB.txt)

Pasted between L1919 (existing entry close
"T1 Synth W20 weekly: select OPT_*.") and L1921 (closing `=====`)
in CMB.txt §OPEN QUESTIONS FOR T1 SYNTH. See companion prompt
`prompt/060_cmb_oq_paste_w20_051_q1q2q4.txt` for the executer
fire spec.

```
[OQ-2026-05-06-051-Q1-MECHANISM-IDENTIFICATION]
051 bt_baseline_note v1.0 (Zenodo concept DOI
10.5281/zenodo.20048196 / version 20048197,
2026-05-06) Proposition 1.2 frames the d>=3
gap A_naive < 2d with two non-mutually-
exclusive mechanisms: (i') borderline-locus
deg a = 2 deg b on a sub-stratum, (ii')
alternative A_fit definition under PCF-2 v1.3
fit-protocol audit. R1.1+R1.3+Q1 record is
consistent with either; closure of either
mechanism (jointly with Q4) lifts A_naive to
2d. Distinguishing them is open.
T1 Synth W20 weekly: arbitrate Q1 -- one of
CLOSURE_VIA_(i'), CLOSURE_VIA_(ii'), BOTH_HOLD,
PARTIAL, PIVOT, ESCALATE.

[OQ-2026-05-06-051-Q2-BORDERLINE-Q-ANSATZ]
051 §6 Problem 2 (q:borderline-Q): under
mechanism (i') of Q1, can the BT 1933 §1
borderline-case algebraic ansatz
Q_j(x) = +/- B x^(1/2) + (lower order) be
made explicit at the SIARC stratum, with B
identified in closed form in c_a, c_b?
Expected closed form is B = sqrt(c_a) at
formal level, by analogy with the d=2 Vquad
upper-branch transition of PCF-1 v1.3 §6.
Explicit derivation is open in the note.
Gated on Q1 = CLOSURE_VIA_(i').
T1 Synth W20 weekly: arbitrate Q2 -- one of
CLOSURE_B_EQ_SQRT_C_A, CLOSURE_OTHER, GATED,
PIVOT, ESCALATE.

[OQ-2026-05-06-051-Q4-SECTORIAL-UPGRADE]
051 §6 Problem 4 (q:sectorial): the Theorem
1.1 baseline produces formal y_dom, y_sub in
Gamma(n)^mu gamma^n n^rho C[[1/n]] without an
analytic-side guarantee of Borel convergence
in a sector of opening > pi/(2d). The formal-
to-analytic sectorial upgrade is the content
of Wasow §X.3 (Thm 11.1) / Adams 1928 /
Turrittin 1955 / Immink 1984 / Costin 2008
ch. 5; at deposit time Wasow §X.3 OCR-PDF
unavailable on disk and Adams 1928 NIA per
A-01 verdict. T1 Phase 3 follow-on territory.
T1 Synth W20 weekly: arbitrate Q4 -- one of
WASOW_PRIMARY, COSTIN_PRIMARY, ADAMS_PRIMARY,
TURRITTIN_PRIMARY, IMMINK_PRIMARY, MULTI,
PIVOT, ESCALATE.
```

## Splice geometry (DRAFT-TIME VERIFIED)

- CMB.txt pre-paste SHA: `723E9C60..C3B0`
- CMB.txt pre-paste line count: 1921
- CMB.txt pre-paste byte count: 87292
- L1919 anchor (verified byte-level via
  `[System.IO.File]::ReadAllBytes`):
  `T1 Synth W20 weekly: select OPT_*.` (length 34, no trailing
  whitespace)
- L1920 anchor (verified byte-level): bare empty line (length 0,
  no whitespace; same as L1899 for 059 — bare empty was the
  spec-defect D2 in 059, now correctly modelled here)
- L1921 anchor (verified byte-level): 64 `=` characters
  (length 64, no trailing whitespace, file ends without newline
  — last 12 bytes all `0x3D`)
- Anchor uniqueness: `grep -c "T1 Synth W20 weekly: select OPT"`
  returns exactly 1 hit at L1919.

## Arithmetic verification (the L1 lesson from 059)

OLD_STR (3 lines):
```
T1 Synth W20 weekly: select OPT_*.

================================================================
```

NEW_STR structure (Python AST count of the embedded NEW_STR
fence in prompt 060 verified at draft time):
- L1: `T1 Synth W20 weekly: select OPT_*.` (preserved)
- L2: blank (preserved)
- L3-17: Q1 entry body (15 lines: 1 header + 11 paragraph
  + 3 arbitrate-OPT lines)
- L18: blank
- L19-33: Q2 entry body (15 lines: 1 header + 11 paragraph
  + 3 arbitrate-OPT lines)
- L34: blank
- L35-50: Q4 entry body (16 lines: 1 header + 11 paragraph
  + 4 arbitrate-OPT lines)
- L51: blank
- L52: `===...===` 64-char close (preserved)

NEW_STR total lines = 1 + 1 + 15 + 1 + 15 + 1 + 16 + 1 + 1 = 52

DRAFT-TIME VERIFY:
- NEW_STR=52
- OLD_STR=3
- delta = NEW_STR - OLD_STR = 52 - 3 = +49
- expected post-LC = pre-LC + delta = 1921 + 49 = 1970

NOTE: initial drafting hit an off-by-2 (Q1 sized as 16 actual 15;
Q4 sized as 17 actual 16); both caught by Python AST count on
the embedded prompt fence BEFORE prompt-fire (L1 lesson worked).

## STEP 1 anchor coverage (the L2 lesson from 059)

The 060 prompt covers all 3 lines of OLD_STR via individual
anchor checks (not just sentinels):

- STEP-1.1: L1919 byte-level inspection — exact-match bytes
  `54 31 20 53 79 6E 74 68 20 57 32 30 20 77 65 65 6B 6C 79 3A
   20 73 65 6C 65 63 74 20 4F 50 54 5F 2A 2E` (length 34)
- STEP-1.2: L1920 byte-level inspection — empty line (length 0)
- STEP-1.3: L1921 byte-level inspection — 64 `=` characters
  (length 64); also confirms file-end-no-newline state via
  last-12-bytes-are-all-0x3D check
- STEP-1.4: anchor uniqueness check — exactly 1 hit of
  "T1 Synth W20 weekly: select OPT" in baseline

## Operator decision history captured in this file's substrate

This deliverable executes operator decision (b) authorized
2026-05-06 ~16:25 JST in the chat round that also authorized
(c) OPT_C2 + (d) LATE-FIRE post-W20. (b) is paraphrased as:
"draft 3 OQ entries for CMB.txt this week + a CMB-paste prompt
analogous to 059, with arithmetic-verification fixes per L1/L2
memory lessons." This file is the substrate; prompt 060 is the
fire spec.

## Downstream: T1 Synth W20 weekly arbitration

Mon 2026-05-11 (or Sun-night ISO 2026-05-10): operator pastes
CMB.txt §OPEN QUESTIONS FOR T1 SYNTH (post-paste state) +
relevant 051 substrate to T1 Synth Claude.ai web/desktop. T1
Synth produces verdict on Q1/Q2/Q4 per the OPT_* enumerations.

T2 absorbs verdicts post-arrival:
- Closes 3 SQL todos `w20-synth-051-q1/q2/q4-...`
- Drafts T1 Phase 3 dispatch prompt (gated on Q1+Q4 verdicts)
- Refreshes picture v1.20 substrate (LATE-FIRE post-W20 trigger
  per decision (d))

## AEAL anchor

This substrate file is itself an AEAL deposit-class deliverable
(additive, not deposit-time-snapshot). It does not generate a
new claims.jsonl entry on its own; the 060 fire will produce
one or more.
