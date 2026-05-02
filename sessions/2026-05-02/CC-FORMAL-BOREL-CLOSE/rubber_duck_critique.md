# Rubber-duck critique — CC-FORMAL-BOREL-CLOSE (HALT)

## What I (the agent) did

Read Prompt 013. Located the dependency clause:
> 009 verdict G15_CLOSED ... GATING: this prompt MUST NOT be
> fired until 009's verdict is G15_CLOSED.
and the matching halt clause:
> CC_BOREL_009_NOT_AVAILABLE — Prompt 009 verdict is not
> G15_CLOSED ... halt immediately with this key, do not
> attempt to proceed in V_quad native normalization.

Inspected `sessions/2026-05-02/VQUAD-PIII-NORMALIZATION-MAP/`
on the bridge. The handoff explicitly states `**Status:**
PARTIAL` and `Verdict reached: **G15_PARTIAL**`. The
`canonical_S_zeta_star.txt` confirms `C_can NOT NUMERICALLY
COMPUTED` and lists R2/R3/R4/R5 as residuals.

Halted. Wrote halt_log + minimal deliverables.

## Critique 1 — Did I correctly read the verdict?

Yes. Three independent locations in the 009 deliverables agree
(handoff status, handoff verdict line, canonical_S_zeta_star.txt
header). No interpretation latitude.

## Critique 2 — Could I have proceeded "softly" anyway?

The prompt explicitly forbids it: the halt clause is named and
keyed, and the Do-Not list bars use of V_quad-native
`S_{zeta*}` in any canonical-coordinate formula. Producing the
Borel sum in V_quad-native coordinates only would be an
implicit reformulation of the prompt without operator
sign-off. I did not.

## Critique 3 — Did I avoid fabrication?

I produced no numerical Borel-sum value, no closed-form
formula, and no `S_{zeta*}^{can}`. The 30-digit numerical
verification gate (Phase C) was not attempted; therefore no
overclaim was possible.

## Critique 4 — CT v1.3 status

Unchanged. `cc_formal_borel_status.md` records the no-flip
explicitly. CT v1.3 source was not modified.

## Critique 5 — What would I have asked Claude (if bidirectional)?

> "Prompt 009 returned PARTIAL with R5 (Okamoto 1987 Lax pair)
> as the primary blocker. Prompt 013's halt clause matches
> exactly and I am halting. Two follow-up paths:
> (a) acquire the Okamoto + Conte–Musette references and refire
>     009 to G15_CLOSED, then refire 013 unchanged;
> (b) reformulate 013 to accept G15_PARTIAL by producing the
>     Borel sum *symbolically modulo R2–R5* (no numerical
>     30-digit gate), landing at a PARTIAL-symbolic verdict.
> Which does the operator prefer?"

## Critique 6 — Anything else Claude should look at?

- Cross-check that the 013 gating reading is the synthesizer's
  intended reading. The phrase "is reformulated by the
  synthesizer before firing" suggests the synthesizer expected
  to *gate* this prompt out, not to fire-and-halt; this halted
  session is consistent with either reading.
- The hashes in `halt_log.json` provide full upstream
  traceability for any later refire.
