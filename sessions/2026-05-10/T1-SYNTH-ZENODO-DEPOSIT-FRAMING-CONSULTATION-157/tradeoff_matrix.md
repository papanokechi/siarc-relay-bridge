# Tradeoff Matrix — Slot 157 Zenodo Deposit Framing

Source: slot 157 verdict (claude-opus-4.7-anthropic-2026-05-10) Section Q3.
Bridge prompt: claude-chat commit `8dcff49`.
Verdict label: FRAMING_AMEND @ MEDIUM-HIGH (recommends Framing C).

---

## Framing key

- **A** — Consolidated single manuscript (1 deposit; new concept-DOI; orphans PCF-2 19936297)
- **B** — Cascade-132 Option α (3 deposits; PCF-2 v1.4 + Umbrella v2.2 + Picture-chain v1.20+; status quo)
- **C** — Drop/fold picture-chain (2 deposits; PCF-2 v1.4 + Umbrella v2.3 with Appendix C absorbing picture-chain) **← RECOMMENDED**
- **D** — Tiered (3 deposits + 1 anchor; new M1–M12 closure paper anchors PCF-2 + Umb; picture folded into anchor)
- **E** — Zenodo Community + per-deposit (composes with B or C)
- **F** — Atomic-axis (≥6 deposits: program papers + per-axis V0 records)
- **G** — arXiv-first (RULE-1-blocked via M11 endorsement)
- **H** — H1 bibliographic-record-only / H2 journal-primary (H2 RULE-1-blocked)

## Scoring matrix

| Axis | A | B | **C** | D | E | F |
|------|---|---|---|---|---|---|
| Discoverability                | HIGH (1 record)  | MED (3 fragmented) | **MED-HIGH (2 focused)** | HIGH (anchor) | HIGH (Community page) | LOW (fragmented) |
| Citation friction              | LOW (single)     | MED (which to cite?) | **LOW-MED (Umb=program)** | LOW (cite anchor) | LOW (cite Community) | HIGH (which axis?) |
| Composition workload           | 2.5–3.5×         | 1.0× baseline       | **1.1–1.3×** | 1.8–2.3× | base × 1.05 | 2.0–2.8× |
| Versioning flexibility         | LOW (monolithic) | HIGH (per-paper)    | **HIGH (per-paper)** | HIGH (per-supp) | HIGH | HIGH |
| Audit-trail clarity            | MED (merged)     | HIGH (per-paper)    | **HIGH (per-paper)** | HIGH | HIGH | HIGHEST |
| Existing-artefact reuse        | ~30%             | ~85%                | **~80%** | ~70% | inherits | ~50% |
| Concept-DOI lineage            | BREAKS PCF-2     | PRESERVES           | **PRESERVES** | PRESERVES | PRESERVES | PRESERVES |
| D-154-1 resolution             | YES (absorbed)   | NO (still open)     | **YES (folded)** | YES (folded into anchor) | inherits | partial |

## Pareto analysis

- **C ⪰ B**: C dominates B on Discoverability, Citation friction, D-154-1 resolution; loses 0.1–0.3× on Composition workload; ties on the rest. **Strict domination on the 3 most strategically important axes**.
- **C ⪰? A**: C does not dominate A on Discoverability (A is HIGH), Citation friction (A is LOW), or coherence; A does not dominate C on Concept-DOI lineage (A BREAKS PCF-2), Composition workload (2.5–3.5× vs 1.1–1.3×), Existing reuse (~30% vs ~80%). **Mutually non-dominated**, but A is risk-asymmetric (large cost for marginal coherence gain over C+E).
- **C ⪰? D**: D ties C on most axes; loses 0.7–1.0× on Composition workload (1.8–2.3× vs 1.1–1.3×). **C dominates D on workload alone**; coherence parity.
- **F is dominated**: F loses on Discoverability (LOW vs MED-HIGH), Citation friction (HIGH vs LOW-MED), Composition workload (2.0–2.8× vs 1.1–1.3×); only wins on Audit-trail clarity, which is already provided by bridge cascade records. **F is Pareto-dominated by C**.
- **C+E**: C+E composes the SIARC Zenodo Community on top of C base. **C+E weakly Pareto-dominates plain C** if program-level Community discoverability is valued; admin overhead is marginal.

## Implicit axis (RULE 1 fire-eligibility)

| Axis | A | B | **C** | D | E | F | G | H1 | H2 |
|------|---|---|---|---|---|---|---|---|---|
| RULE 1 fire-eligibility | YES | YES | **YES** | YES | YES (advisory) | YES | NO (M11) | YES | NO (M11) |

G and H2 are gated on M11 endorsement workflow lift; not fire-eligible under RULE 1. Held for post-lift menu.

## Conclusion

**Recommended: Framing C** (drop/fold picture-chain into Umbrella v2.3 Appendix C). Pareto-dominates B on the 3 most strategically important axes at ~1.1–1.3× composition cost. C+E upgrade (add SIARC Zenodo Community) is weakly Pareto-superior post-RULE-1-lift; defer.
