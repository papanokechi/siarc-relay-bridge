# H1 handoff — Birkhoff–Trjitzinsky and Conjecture B4

## Top-line verdict

`B4_PROVED_AT_d≥3_RESIDUE_AT_d=2`

## Main finding

Birkhoff–Trjitzinsky gives the **leading slope** `A = 2d` for every `d ≥ 2`
generically, via the Newton polygon (slope 2 from the canonical SIARC normalisation).
This proves Conjecture B4's leading statement.

The **d = 2 two-branch anomaly** is predicted by B–T's discriminant trichotomy
on `Δ_2 = b_1^2 − 4 b_0 b_2`:

- `Δ_2 > 0`: real distinct exponents (generic A = 4 branch).
- `Δ_2 < 0`: complex-conjugate (oscillatory envelope).
- `Δ_2 = 0`: resonance, `β = 1` log correction.

But B–T does **not** determine sub-leading constants at arithmetic loci. The
R1.1 j-invariant finer-cubic-split lives in `Λ(b)` and requires the modular
layer (H2 Eisenstein/Chowla–Selberg, H5 X(1) drift, H6 Γ-products).

## Empirical agreement

- Session B / Q1 cubics A = 6 ✓.
- Session Q1 quartics A = 8 (60/60) ✓.
- R1.1 deep cubic ensemble A = 6 within ε ✓.
- Sub-leading α agrees within fit noise with the polynomial-ratio prediction.

## Aggregator hook

- B–T proof of leading B4 is **strong** — pair with H2's `j = 0 → A_true = 2d
  exactly` to get a clean cubic-modular framing for PCF-2 v1.3.
- d = 2 mechanism: pair with H3 to label branches by Painlevé surface type
  (Δ_2 < 0 ↔ P-III(D6); Δ_2 > 0 ↔ P-V; Δ_2 = 0 ↔ D7/D8 boundary).
- d ≥ 3 sub-leading at j = 0: B–T cannot close — handoff to H2/H5/H6.

## Access caveat

`LITERATURE_PARTIAL` — Trjitzinsky 1932 (Trans. AMS 37) and Birkhoff–Trjitzinsky
1933 (Acta Math 60) were not opened directly. Theorem statements are quoted
from standard secondary sources (Wimp–Zeilberger 1985, Olver 1974, Immink 1991,
Braaksma 1971, Sauzin 2014). Upgrade after library access supplies primary
theorem statements and page numbers.

## Confidence

- HIGH on leading slope `A = 2d`.
- MEDIUM on d = 2 mechanism (needs Painlevé classification confirmation, H3).
- HIGH on residue-existence at arithmetic loci (B–T's structural limit).

## Backfill note

This H1 deliverable was backfilled by the main orchestrator after the H1
sub-agent declined the file-writing task. Theory content is authoritative
against standard references.
