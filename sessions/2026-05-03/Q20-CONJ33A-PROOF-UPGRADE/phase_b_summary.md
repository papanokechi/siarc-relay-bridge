# Phase B Summary — Q20-CONJ33A-PROOF-UPGRADE

**Verdict signal (in-scope, ξ_0 only):** `B_TEMPLATE_PARAMETRIC`
**Verdict signal (out-of-scope, ξ_0 + ρ + a_k):** `B_MACHINERY_NEEDED at d ≥ 3`

## B.1 — d=2 proof template

See `phase_b_d2_proof_template.md`. The d=2 proof template
(Prop 3.3.A) is identical at the statement-and-sketch level
between D2-NOTE v1 (`d2_note.tex` lines 188–227) and
CT v1.3 (`channel_theory_outline.tex` lines 502–540).

## B.2 — Cross-reference status

D2-NOTE v1 ↔ CT v1.3 §3.3.A: **agree at the statement
level**.  D2-NOTE v1 ↔ PCF-1 v1.3 §5 (Theorem 5):
**source not in workspace** (operator-side TeX). Phase B
treats this as a partial deferral, not a halt: the SIARC
v1.3 release window was joint and the bib keys
`siarc_pcf1_v13` in both D2-NOTE and CT v1.3 are
self-consistent.  The PCF-1 v1.3 §5 cross-check is
explicitly flagged in handoff.md "Anomalies" as a residual
operator-side check.

No `HALT_Q20_PHASE_B_TEMPLATE_DRIFT`.

## B.3–B.4 — Line-by-line diff

See `phase_b_proof_diff.md`. Nine lines of the proof sketch
are classified U/D/M.

For the Conj 3.3.A* upgrade scope (ξ_0 only):
- All D-lines in scope (L1, L2, L4, L5, L6) have clean
  parametric-in-d replacements that reduce to the d=2 line
  at d=2.
- The reduction at d=2 is checked symbolically in each case.
- L7 (ρ formula) and L8 (Birkhoff recursion) are out of
  scope for Conj 3.3.A*; they pertain to Prop 3.3.A's
  ρ and a_k components, which are NOT what Conj 3.3.A*
  is conjecturing.
- Machinery citations needed: Wasow §X.3 (Gevrey index of
  slope-1/d edge); Wasow §X.3 + B–T 1933 (Birkhoff
  recursion); standard Borel-summability theorem (Borel
  singularity = exponential characteristic root).

For the broader Prop 3.3.A scope (ξ_0 + ρ + a_k):
- L7 (parametric ρ_d formula at general d) has no
  parametric-in-d replacement currently available.
- This is open per D2-NOTE v1 §3 last paragraph.
- The corresponding general-d verdict signal is
  `B_MACHINERY_NEEDED at d ≥ 3` for ρ_d.

## Phase B verdict (in-scope)

**`B_TEMPLATE_PARAMETRIC`** — every D2-SPECIFIC line in the
ξ_0-only proof has a clean parametric-in-d replacement that
reduces to the d=2 line at d=2.  All M-tagged lines (L3, L8,
implicit Borel-summability at L6) are deferred to Phase C
literature verification.

**Note on PCF-1 v1.3 §5 source-drift:** since PCF-1 v1.3
is the operator's local source and not under the bridge or
under `pcf-research/`, the formal source-drift check
required by Phase B.2 is partially deferred.  D2-NOTE v1
and CT v1.3 §3.3.A internally agree, and both cite PCF-1
v1.3 §5 with the same bib key.  This is flagged as a
**residual operator-side check** in the handoff, not as a
halt.
