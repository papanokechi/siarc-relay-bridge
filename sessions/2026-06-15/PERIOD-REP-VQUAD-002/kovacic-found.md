# Stage 2 — G-KOVACIC pre-investigation: CONFIRMED-ABSENT

**Chain:** PERIOD-REP-VQUAD-002 · **Stage:** 2 · **Date:** 2026-06-15
**Verdict:** **G-KOVACIC confirmed-absent** — no execution of the Kovacic
algorithm on the V_quad differential equation exists in the corpus.

> Strengthening Condition 1: a located Kovacic run would already operate on a
> linear ODE with rational-function coefficients over an explicit base field,
> directly answering the algebraicity question. No such V_quad run exists.

## 2.1 Search performed (this probe, fresh)

| # | Scope | Pattern | Result |
|---|-------|---------|--------|
| A | whole repo | `Kovacic\|Kovačič\|Kovacič` | 53 files — **all** in `sectorial/cc_transcendence/` (EBR) + 1 template placeholder |
| B | `sectorial/vquad_stokes_resurgence/` | `Kovacic\|Picard-?Vessiot\|differential Galois\|SL\(?2\|Galois` | **0 matches** |

**Where Kovacic *does* appear (all EBR / D8⁽¹⁾ sibling, NOT V_quad):**
- `sectorial/cc_transcendence/cc3_2_1_h2_classify.py:9` — "**Kovacic** decision via
  the rigorous symmetric-power / Riccati criterion (van der Put–Singer, …)" —
  this is the **EBR (D8⁽¹⁾) order-4 operator** Galois decision, a *different* ODE.
- `zenodo/templates/related_identifiers.template.md:97,112` — only a **placeholder**
  naming Kovacic as an external-author handle.
- The remaining ~50 files are all `cc_transcendence/` EBR/cc3/ebr3/ebr4 artefacts.

**Zero** Kovacic/Picard–Vessiot/differential-Galois hits in
`sectorial/vquad_stokes_resurgence/` or any V_quad-named file.

## 2.2 Corroboration with the parent probe

- `PERIOD-REP-VQUAD-001/data-inventory.json:141–143` (gap `G-KOVACIC`) — "Task
  asserts 'Galois group SL(2) by exact Kovacic'; **NO Kovacic-execution file
  located in the corpus.** … the derivation is not in hand."
- `PERIOD-REP-VQUAD-001/vquad-linear-system.md:59–61` — SL(2) "by Kovacic (task
  assertion; gap G-KOVACIC — not located as a derivation in the corpus)."

## 2.3 Corpus-organisation flag (per task 2.3, not relitigated)

The V_quad/Sakai program asserts an **SL(2)** differential Galois group "by exact
Kovacic" (task prompt; surface-type memory). **The supporting Kovacic execution is
not present in the corpus.** Per the task instruction this is **flagged as a
corpus-organisation/ under-documentation issue** — the SL(2) claim is *consistent*
with a non-Liouvillian rank-2 irregular connection, but its derivation should be
sourced or redone before any paper. **This probe does not relitigate the Galois
claim.**

## 2.4 Disposition impact

- **No located Kovacic run ⇒ no shortcut to algebraicity.** Proceed to Stage 3
  (Borel–Padé + exact holonomic recognition over ℚ(√3)).
- Note the asymmetry with the EBR sibling: EBR *has* an explicit algebraic order-4
  operator and a Kovacic decision (`cc3_2_1_h2_classify.py`); V_quad has **neither**
  a Lax pair (G-LAX) nor a Kovacic run (G-KOVACIC) nor an algebraic Borel operator
  (G-OMEGA). The whole point of Stage 3 is to *construct* the missing operator and
  read its coefficient field.

**Status:** G-KOVACIC = **confirmed-absent** (fresh search + parent corroboration).
Stages 1 & 2 did **not** resolve algebraicity ⇒ run Stage 3.
