# P08-CAS-HEUNC Handoff
Date: 2026-04-25
Status: COMPLETE

## What was done
CAS verification of HeunC parameters claimed in rem:heunc of
vquad_resurgence_R1.tex. Three independent checks (Copilot/sympy,
Claude.ai/sympy, SageCell/sympy) returned identical verdict.

## Verdict: PARAMETERS WRONG
Claimed: α=-1/3, β=1/(3√3), γ=0, δ=-1/3, η=1/9
Computed: α=0, β=0, γ=0 (match), δ and η are COMPLEX
Root cause: finite singular points of 3x²+x+1 are complex conjugates;
any affine map to {0,1,∞} forces δ,η complex. Real HeunC parameters
for this ODE do not exist under Ronveaux conventions without an
unstated gauge transformation.

## What is correct
- Poincaré rank-1 at ∞: CONFIRMED (lim q(x) = -1/3 ≠ 0)
- ODE belongs to confluent Heun CLASS: CONFIRMED
- Specific parameter quintuple: WRONG, removed

## Fix applied
rem:heunc replaced in vquad_resurgence_R2.tex (1111 lines):
- Removed: parameter quintuple
- Retained: rank-1 confirmation, confluent Heun class claim,
  JMU framework reference, honest deferral of explicit parameters
- Compile: clean, 9 pages, ronveaux1995 + jimbo1981 both resolve

## Files
- vquad_resurgence_R2.tex (working copy, 1111 lines)
- tex\submitted\vquad_resurgence_R2.tex (submission copy)
- _p08_cas_heunc_verify.py (verification script)

## Open items
None. P08 revision is complete pending Nonlinearity referee report.
Do not reopen until a verdict arrives.

## AEAL class
independently_verified (three agents, same result)

CLAUDE_FETCH: this file
