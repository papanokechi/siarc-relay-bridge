# Handoff — VQUAD-PERIODREP-PAPER-001

**Task:** Draft a research paper exhibiting the V_quad connection coefficient C
as an explicit exponential-period integral, with three independent verifications
and a conditional transcendence corollary.

**Status:** `DRAFT-WITH-OPEN-ITEMS` — complete, referee-reviewed draft; clean
build; 6 MED/LOW items deferred to operator. Ready-state git **HELD** per the
standing meta-rule (no commit/push).

---

## What was produced

A 23-page `amsart` paper draft, `latex/vquad-periodrep-paper.pdf`, compiling with
**0 errors, 0 undefined references, 19/19 bibitems cited**, byte-reproducible.

**Main theorem (verified):**
> C = (|Γ(β)|/2π) ∫_γ e^ξ B̂(ξ) dξ = |Γ(β)|·K,  β = −1/(3√3),
> γ = Hankel thimble on (−∞, −2/√3].

Verified three structurally independent ways (operator duality, exact over ℚ(√3);
Borel–Laplace/Hankel; Stokes-data), agreeing to ~46 digits. Bonus: a finite
resurgence corollary (holonomic Borel transform ⇒ finite singular locus, no
infinite alien tower). Conditional on the Fresán–Jossen period conjecture **and**
a stated motivic-comparison hypothesis (G-MOTGALOIS), C is transcendental over ℚ̄.

## Section map

| § | Title | pp (approx) |
|---|-------|-------------|
| 1 | Introduction (+ Notation) | ~3 |
| 2 | The operators L_φ and L_V (+ finite resurgence) | ~6 |
| 3 | The rapid-decay cycle γ (with TikZ figure) | ~3 |
| 4 | The main theorem | ~2.5 |
| 5 | Three verifications (+ strategy/independence) | ~5 |
| 6 | Fresán–Jossen + conditional transcendence (G-MOTGALOIS boxed) | ~3.5 |
| 7 | Discussion (Sakai place, d≥3, Ramanujan/CMF, period comparison, CAS) | ~3 |
| 8 | Appendices A.1–A.5 (coeffs, Kovacic, logs, 4-convention table, repro) | ~3.5 |
| 9 | References (19 bibitems) | ~1 |

## Metrics

- Pages **23**; body sections **8** (+ references); subsections **38**.
- Labelled equations **30**; theorems **5**, propositions **6**, lemmas **1**,
  corollaries **2**, definitions **1**, remarks **7**; distinct labels **72**.

## Self-review (Stage 4) outcome

All four Lecerf criteria PASS (readable / objects-defined-before-use /
significance-beyond-program / CAS-SOTA-context). Two HIGH-severity issues found
and **fixed**:
1. §4 "only transcendental constant" → "only non-algebraic factor" (Γ(β)
   transcendence is only conditionally known; was inconsistent with §6).
2. Four relevant bibitems were uncited (Hien, SakaiClass, Écalle,
   Loday-Richaud) → now cited at their natural places.

Conditionality audit: transcendence is **doubly-conditional everywhere**;
G-MOTGALOIS is an explicit boxed hypothesis in §6. Not collapsed to unconditional.

## Open items for operator (6) — see `self-review.md` / `ledger.json`

- **MED 3** Insert the real Sakai-stratification Zenodo **concept DOI** (bibitem
  `Sakai` is a placeholder).
- **MED 4** Page count 23 = lower end of the 25–30 band (above the 22 floor);
  accept or specify additional in-body content (not auto-padded, per AEAL).
- **MED 5** G-MOTGALOIS evidence is heuristic; a motives referee may want
  Nori/Ayoub specifics. Honest state — do not overclaim.
- **LOW 6** Pseudonym / no affiliation → VENUE-RELAY concern (do not alter here).
- **LOW 7** §2 b_m table could be fully tabulated.
- **LOW 8** §5.3 amplitude A is a labelled 46-digit numerical extraction.

## Files in this slot

```
outline-final.md
sections/section-1.md … section-8.md, section-9-references.md
latex/preamble.tex, latex/build.py
latex/vquad-periodrep-paper.tex, latex/vquad-periodrep-paper.pdf
vquad-periodrep-paper.md          (concatenated markdown view)
self-review.md
reproducibility-statement.md
ledger.json
claims.jsonl                      (20 claims)
handoff.md                        (this file)
```

## How to rebuild

```powershell
cd latex
$env:PYTHONIOENCODING="utf-8"
python build.py        # prints PAGES / ERRORS / PDF_EXISTS
```

## Governance / DO-NOT (honored)

No Zenodo deposit · no journal submission · no parent-corpus edits (V_quad
20455090, Sakai paper untouched) · transcendence kept conditional · G-MOTGALOIS
present in §6 · ≤ 30 pages · Stage-4 Lecerf review done · not anonymized.
Ready-state git **HELD**: staged for operator, no commit/push.

## Downstream

Operator review of this draft → VENUE-RELAY-VQUAD-PAPER chain (venue selection,
journal-class swap, per-venue blinding). Zenodo deposit and submission are
separate operator-gated slots.
