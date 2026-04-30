# Relay patch prompt — MM-02 (UMB / #14 tier-label collision)
**Source audit:** `sessions/2026-04-30/SIARC-COHERENCE-AUDIT/`

```
╔══════════════════════════════════════════════════════════════════╗
║  SIARC RELAY — UMB-14-TIER-LABEL-DISAMBIGUATION                 ║
║  Goal: end the T0/T1/T2/T3 label collision between UMB and #14. ║
╚══════════════════════════════════════════════════════════════════╝

CONTEXT
  UMB defines T0..T3 as an arithmetic-classification hierarchy:
     T0 algebraic / T1 transcendental(Mahler-Nesterenko) /
     T2 trans-stratum (μ-asymptotic) / T3 barrier (Fuchsian).
  #14 (paper4_takeuchi_outline.tex) defines Tier 0..3 as an
     obstruction hierarchy:
     0 modular non-CM / 1 cuspidal arithmetic /
     2 non-arithmetic Fuchsian / 3 d=2 irregular confluent-Heun.
  These are not translations of each other.

PROPOSED FIX (lowest blast radius)
  Keep UMB's T0..T3.  Rename #14's tiers to "Obstruction Tiers
  O0..O3" everywhere in paper4_takeuchi_outline.tex.  Then add a
  one-paragraph translation table to UMB §1.2 explicitly mapping
  the obstruction tiers into UMB's arithmetic tiers (where the
  inclusion is partial, say so).

FILES TO EDIT
  tex/submitted/paper4_takeuchi_outline.tex   (rename Tier→Obstruction Tier O)
  tex/submitted/umbrella_program_paper/main.tex (add translation paragraph
                                                 + bib-entry rename if needed)
  f1_mathcomp_submission/references.bib       (no math change; only update
                                                 the title string of @article{spectral}
                                                 if the renamed file's title changes)

STEPS
  1. In paper4_takeuchi_outline.tex, search/replace
        "Tier~0"|"Tier 0"|"Tier-0"  → "Obstruction Tier O0"
        "Tier~1"|"Tier 1"           → "Obstruction Tier O1"
        ... (for 2 and 3)
     leaving narrative phrases like "four-tier hierarchy" intact;
     prefer "four-tier obstruction hierarchy" for clarity.
  2. In UMB main.tex §1.2, after the four T0..T3 definitions, insert:

       \begin{remark}[Translation to the obstruction hierarchy of \#14]
       The companion paper~\#14 introduces a parallel four-tier
       \emph{obstruction} hierarchy $O_0,\dots,O_3$ measuring the
       distance from the modular sector $X(1)$. The two
       hierarchies do not coincide. We have the inclusions
       $O_0 \subseteq T_0 \cup T_2$, $O_1 \subseteq T_2$,
       $O_2 \subseteq T_2$, $O_3 \subseteq T_3$, but in general
       neither family of tiers refines the other.
       \end{remark}

  3. Re-render UMB and #14 PDFs; do a global grep for "Tier"
     in each to ensure no orphaned old labels remain.
  4. AEAL claims:
       - "UMB T0..T3 are arithmetic; #14 O0..O3 are obstruction"
       - "Inclusions O_0⊆T_0∪T_2, O_1⊆T_2, O_2⊆T_2, O_3⊆T_3"
       (label both as evidence_type=documentary; the inclusions
        are derived from comparing definitions, not new theorems).

DELIVERABLES
  - patched .tex files (UMB main.tex, paper4_takeuchi_outline.tex)
  - re-rendered PDFs
  - claims.jsonl entries
  - handoff.md per standing instructions

HALT IF
  - the proposed inclusions O_i ⊆ T_j cannot be supported by the
    existing definitions (in that case, escalate to Claude for a
    revised translation table — do not invent inclusions).
```
