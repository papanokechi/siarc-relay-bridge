# Handoff — T2A-WRITEUP
**Date:** 2026-04-28
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Drafted the T2A computational observation paper as `t2a_paper_draft.tex`,
an `amsart` LaTeX manuscript reporting the degree-(4,2) findings at
both CMAX=1 and CMAX=2.  Compiled cleanly (pdflatex, twice) to an
8-page PDF with no undefined references and no errors.

## Paper title
"A Computational Investigation of the 2k-Degree Conjecture at k=2:
the Degree-(4,2) Stratum and a Novel Transcendental Constant"

## Abstract (one-line)
Two enumerations (CMAX=1: 1,162/1,162 Trans-hard at dps=300; CMAX=2:
1,000/1,000 sampled Trans-hard at dps=150 from 108,762/125,000
candidates) confirm the existential claim of the 2k-degree conjecture
at k=2, refute the natural ratio sub-hypothesis (Trans-hard rate
85.8/89.1/86.0/89.0% across rho=1/4,1/2,1,2), and isolate a novel
transcendental candidate R_1 = -0.10123520070804963... unidentified
against all standard bases at dps=300.

## Compile status
- pdflatex twice: CLEAN
- 8 pages, 421,374 bytes
- 0 undefined references
- 0 errors
- Only cosmetic hyperref bookmark warnings (math in titles)

## Recommended venue (NOT in the paper itself)
- Primary: **Integers** (open access, computational results welcome,
  no Exp.Math affiliation)
- Fallback: **Journal of Integer Sequences** (open access)
- Do NOT submit to: Experimental Mathematics (BLACKLISTED), NNTDM

## Key numerical findings (all from BACKGROUND, no fabrication)
- F(2,4) baseline: 24/531,441 Trans (cited from companion [PCF24])
- (4,2) CMAX=1: 1,162/1,162 Trans-hard at dps=300
- (4,2) CMAX=2: 108,762 candidates / 125,000 (~87.0%);
  1,000/1,000 deep-validated at dps=150
- Ratio rho = a_4/b_2^2 in {1/4, 1/2, 1, 2} ~25% each;
  Trans-hard rate 85.8/89.1/86.0/89.0% (3.3pp spread) — REFUTED
- 28 phantom hits caught at CMAX=2 Stage C, +6 in pick-identify
- R_1 = -0.10123520070804963... (30 sig digits)
  - 0/35 PSLQ hits at dps=300
  - RIES: 8-digit coincidence, diff=0.389
  - OEIS: no match on 17-digit prefix
  - LMFDB: no match within 10^-12

## Phantom traps documented (formal Remark)
1. zeta(2) = pi^2/6: relation [..,-6,1] with L-coef=0
2. phi = (1+sqrt(5))/2: relation [2,-1,-1] with L-coef=0
   when both phi and sqrt(5) are in basis
Defense: mandatory `int(rel[L_index]) != 0`

## Bridge commits referenced in paper
- 84f91bf  T2A-DEGREE42-SEARCH
- fa259b0  T2A-DEGREE42-DEEP-VALIDATE
- 45fe389  T2A-BASIS-IDENTIFY
- 3a5bb2b  T2A-LMFDB-LOOKUP
- ce25196  T2A-CMAX2-RATIO

## Open items before submission
1. Cover letter (Integers): emphasise computational-observation
   framing; cite [PCF24] explicitly; flag the negative ratio
   result as the key methodological point.
2. Decide whether to expand Section 5 (R_1) with a precision-
   escalation residual plot before submitting.
3. Confirm Integers' formatting requirements (they may prefer
   their own .cls file).
4. Add ORCID and a "Code availability" statement linking to the
   GitHub bridge.
5. Consider a short appendix listing the 5 representative limits
   used in the basis-identification table (currently summarised
   as "0/35").

## Judgment calls made
- Used `lmodern` package after `microtype` rejected default fonts
  for expansion. Standard fix.
- Set table label "$\\dagger$" footnote on the CMAX=2 enumeration
  size to clarify the sign-symmetric reduction (not in BACKGROUND
  but follows directly from the WLOG a_4>0 step).
- Bibliography hand-built (no .bib): 6 entries, the canonical
  ones (PCF24, AEAL, Apery, BBP, Ferguson-Bailey, Lindemann).
- Did NOT cite the contamination paper from main_R1.tex's bbl
  because it is an Exp.Math submission and the present paper
  should not advertise that venue.

## Anomalies and open questions
None detected.  All numerical claims trace to the BACKGROUND
section provided in the task prompt; no values were invented.

## What would have been asked (if bidirectional)
- Should the Integers submission go out today, or after Claude
  reviews the draft?
- Confirm: the R_1-bearing CMAX=1 family coefficients are not
  recorded in this paper (the paper only quotes the limit value).
  Should the family be named explicitly in an appendix?

## Recommended next step
Have Claude review the abstract and §1 framing.  If approved, run
SICF (Self-Improving Compositional Feedback) once over the paper
to flag any remaining phrasing risks, then prepare the Integers
submission package.

## Files committed
- t2a_paper_draft.tex
- t2a_paper_draft.pdf
- handoff.md

## AEAL claim count
0 new claims this session (the paper restates claims already
logged under sessions T2A-DEGREE42-SEARCH, T2A-DEGREE42-DEEP-VALIDATE,
T2A-BASIS-IDENTIFY, T2A-LMFDB-LOOKUP, and T2A-CMAX2-RATIO).
The compile-success of the LaTeX source is itself recorded by the
.log file checksum, but no novel numerical claim is introduced.
