# Open-items decision pack — VQUAD-PERIODREP-PAPER-001

Consolidated, pre-committed operator decisions on the 6 open items from
`VQUAD-PERIODREP-PAPER-001/self-review.md` (items 3–8). This is the clean
reference for the downstream correction-pass agent (VQUAD-PAPER-CORRECTIONS-001),
so the decisions are **not re-litigated**. The two HIGH items from self-review
were already fixed during drafting and are not listed here.

| ID | Self-review item | Severity | Pre-committed decision | Who acts | When |
|----|------------------|----------|------------------------|----------|------|
| MED-1 | Sakai concept DOI placeholder (§9 bibitem `Sakai`) | MED | Reference **CURRENT** Sakai state (Part (ii)(a) STRUCTURAL); insert the current Sakai Stratification deposit's concept DOI. Do **not** anticipate the planned Sakai upgrade — the upgrade lands AFTER the Direction-2 deposit, and this paper cites current state. | Operator supplies DOI; corrections agent substitutes. | Corrections slot, before deposit. |
| MED-2 | 23pp at low end of 25–30 band | MED | Do **not** pre-expand. 23pp is acceptable (all content genuine/sourced; gap is amsart density, not missing material). Revisit **only** if the cold read names *specifically undeveloped* material. No padding (AEAL/no-pad discipline). | Operator (during read); corrections agent only if a specific section is named. | Conditional on cold-read finding. |
| MED-3 | G-MOTGALOIS evidence heuristic (§6) | MED | **STRENGTHEN.** Compositio is the primary venue; preemptively address the likely-strongest referee concern (motives referee may want Nori/Ayoub specifics for G_V ≅ relevant quotient of G_mot(M)). Keep it honest — it stays a *conjectural bridge*; strengthen the *evidence/exposition*, do not overclaim it as proven. | Corrections agent (with operator steer on §6 vs appendix vs both). | Corrections slot. |
| LOW-1 | Pseudonym/affiliation (author block) | LOW | **Defer to VENUE-RELAY.** No action during cold read or corrections. Do not anonymize or alter the author block in this draft. | VENUE-RELAY chain. | Out of scope here. |
| LOW-2 | b_m coefficient table (§2 eq:coeffstream) | LOW | **Review during the cold read.** Current form (exact ℚ(√3), b_2 inline, reproducible) makes its point; tabulating b_m fully is optional. Decide as-is vs. expand based on the read. | Operator (during read). | Cold-read judgement. |
| LOW-3 | §5.3 Method C numerical amplitude A | LOW | **Spot-check during the cold read.** A is a Borel–Padé-accelerated 46-digit numerical extraction (not exact); confirm the displayed figure matches the parent-slot data (`PERIOD-REP-VQUAD-002/scripts/borel_pade_results.json` and §5.3). Keep the numerical hedge. | Operator (during read). | Cold-read spot-check. |

## Decision-status summary (for the corrections agent)

- **Settled, no read needed:** LOW-1 (defer).
- **Settled, conservative, read may override:** MED-1 (current DOI), MED-2 (no expand unless specific finding).
- **Settled to STRENGTHEN, read sets the depth:** MED-3.
- **Read-dependent:** LOW-2 (as-is vs. expand), LOW-3 (figure spot-check).

## Guardrails carried from the paper task (do not violate in corrections)

- Transcendence stays **doubly conditional** (Fresán–Jossen period conjecture +
  G-MOTGALOIS hypothesis); never collapse to unconditional.
- G-MOTGALOIS remains a displayed, named, *conjectural* hypothesis in §6.
- Keep ≤ 30 pp; do not anonymize; no autonomous deposit/submission; no edits to
  the parent (PERIOD-REP-VQUAD-00x) corpus.
