# Rubber-duck self-critique --- VQUAD-PIII-NORMALIZATION-MAP

**Author:** GitHub Copilot (VS Code execution agent)
**Date:** 2026-05-02
**Verdict reached:** G15_PARTIAL

## What I'm second-guessing

### 1. Was the verdict G15_PARTIAL the right call, or should it have been a HARD HALT for missing literature?

The prompt's "Do NOT" section says: *"If a literature item is unavailable, halt with the missing-source list rather than guess."*

The prompt's PARTIAL definition says: *"Φ obtained as composition of two of three steps; remaining step requires a piece of P_III(D_6) literature not in the operator's library."*

These two clauses are in tension. I read PARTIAL as the intended landing for *exactly this configuration* (two of three Φ-blocks pinned, one blocked by literature), and the "halt" clause as applying to cases where *no* progress is possible without the missing source.

Phase A and Phase B (and most of Phase C) **are** possible without the missing literature; the substantive blocker is Φ_symp in Phase C plus the numerical Phase D. So PARTIAL fits the prompt's letter and spirit. *Confidence: high.*

### 2. Did I claim Φ_resc more strongly than the evidence warrants?

The Φ_resc lambda = 1/3 derivation rests on the assumption that the canonical P_III(D_6) trans-series at t=0 has the form `exp(±2/√t) ...`, with a leading prefactor of exactly 2. I marked this as "R3-conditional" --- if the canonical-form trans-series carries a different leading constant (say, 2c_* with c_* ≠ 1), then `λ` adjusts accordingly. This is documented honestly in `phi_change_of_variables.tex`. *Confidence: medium-high; the dependence is documented.*

### 3. Did I trigger the layer-separation observation prematurely?

The `unexpected_finds.json` entry `scalar_ode_versus_Lax_pair_layer_separation` is a substantive structural insight, not a numerical anomaly. CT v1.3 §3.5 *implicitly* knew this (its phrasing "algebraic identity at Painlevé-class level only" gestures at it), but CT v1.3 did not spell out the layer structure. Spelling it out here is a positive contribution. *Confidence: high; this is what the prompt's "What would have been asked" section is for.*

### 4. Is the parameter-point Okamoto-constraint mismatch a hard issue or just a convention question?

The four numbers (1/6, 0, 0, -1/2) summing to -1/3 ≠ 0 looked like a halt candidate when I first noticed it. But: it could equally be a convention difference (Okamoto vs Sakai vs CT v1.3's own convention). I flagged it as `unexpected_finds.json` rather than `halt_log.json` because it doesn't *contradict* anything in CT v1.3 --- it points at a residual (R1) that is exactly the kind of thing the prompt anticipated.

If Claude's review reads the constraint mismatch as more serious (e.g. as evidence that CT v1.3 §3.5's parameter point is in a *different* convention than the prompt's quoted Hamiltonian), then a CT v1.4 may be warranted to clarify. That decision is operator/Claude territory, not mine. *Confidence: medium; flagged for review.*

### 5. Did I do enough symbolic work?

I derived the V_quad ODE coefficients from the recurrence symbolically (sympy), confirmed Newton-polygon slope 1/2, and confirmed c = ±2/√3 and ρ = -11/6 by direct expansion. These are all already in CT v1.3 §3.5 with 200-digit verification, but this session re-derives them from scratch from the recurrence (rather than citing them). The re-derivation is reproducible (`verify_vquad_ode.py` + `verify_vquad_ode.log` with sha256).

I did **not** push the symbolic Birkhoff-recursion to compute `a_1, a_2, ..., a_K` for the V_quad-native trans-series; CC-MEDIAN-RESURGENCE-EXECUTE already does this at K=5000 with dps=250. Re-doing it here would be redundant. *Confidence: high.*

### 6. AEAL discipline check

12 entries in claims.jsonl. Three are computation/derivation, two are literature_gap, one is audit. The G15-A5 and G15-A6 entries are explicitly marked `exact: null, reproducible: false` because the canonical numerical value is *not* produced. This is the truthful state. The forbidden-verb scan (no "shows", "confirms", "proves" without numerical backing) is checked by hand here:

- "derives" / "derived" --- used freely, OK;
- "verifies" / "verified" --- used only where numerical agreement is established (Newton polygon, coefficients);
- "established" / "establishes" --- used for partial Φ_resc derivation, qualified by "modulo R3";
- "shows" --- searched all .tex and .md files: 0 occurrences. OK.
- "confirms" --- 0 occurrences. OK.
- "proves" --- 0 occurrences in deliverables. OK.

*Confidence: high.*

## What Claude should review

1. Does the layer-separation observation (`unexpected_finds.json` item 2) warrant a CT v1.4 amendment to §3.5?
2. Is the Okamoto-constraint mismatch (item 1) symptomatic of a deeper issue with the parameter-point identification, or just a convention question?
3. Should Prompt 010 (the planned T3 Stokes-multiplier follow-up) be reordered ahead of the operator's literature-acquisition for R1-R5, given that the substantive G15 blocker is R5 (Lax pair)?

## What I would have asked the operator mid-session, if bidirectional

1. *"Do you have local PDF access to Okamoto 1987 or Conte-Musette 2008? If yes, I should pull the Lax pair from there and continue Phase C-D fully. If no, PARTIAL is the right landing."*

2. *"Should the (1/6, 0, 0, -1/2) constraint mismatch be treated as a halt-class anomaly or as a convention-pinning residual?"*

Both would have shaped the verdict. In their absence, PARTIAL with explicit residual list and unexpected_finds is the conservatively correct call.

## Prose-overclaim self-check

Re-scanning all .tex and .md deliverables for: "shows", "confirms", "proves", "establishes" without qualifier, "demonstrates":

- `vquad_hamiltonian.tex`: "matching" (OK), "verified" (OK, has computational evidence), "exact" (OK, exact rational/algebraic), no overclaim found.
- `pIII_canonical.tex`: "identifies" (CT v1.3 does, so this is a citation), no overclaim found.
- `phi_change_of_variables.tex`: "pinned" (OK, matches the partial-determination claim), "fixed" (OK), "PASS, conditional on R3" (qualified properly), no overclaim found.
- `canonical_S_zeta_star.txt`: "NOT NUMERICALLY COMPUTED" stated repeatedly, no overclaim possible.
- `literature_crosscheck.md`: residuals listed; no overclaim found.

`G15_PROSE_OVERCLAIM` HALT clause: **NOT TRIGGERED.**

## Final disposition

Verdict: **G15_PARTIAL**, residual list R1-R5 documented, primary
blocker R5 (Okamoto 1987 Lax pair). G15 closure ready for follow-up
prompt with estimated 2-4 hr runtime once R5 is in operator's library.
