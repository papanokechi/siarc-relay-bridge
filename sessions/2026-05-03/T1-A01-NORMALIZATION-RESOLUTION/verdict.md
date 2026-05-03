# D8 — Verdict (one of the five labels)

**Task:** T1-A01-NORMALIZATION-RESOLUTION — STEP 7
**Date:** 2026-05-03

---

## Verdict label

```
A01_WASOW_READING_CONFIRMED
```

## Justification (concise)

The triangulation in [D5](normalization_triangulation.md) supports
the reading that Birkhoff 1930 (Acta Math 54) and
Birkhoff–Trjitzinsky 1933 (Acta Math 60) — both with OCR layers —
use a **single shared normalisation** for the formal-solution
exponent at $\infty$:

* Birkhoff 1930 §1 (page 6, formula (6)) defines $s(x) = x^{\nu x}\,
  e^{P(x)}\,x^\mu(\cdots)$, with $\nu$ as the $x\log x$ coefficient and
  $\mu$ as the Newton-polygon slope $(j_l - j_m)/(l-m)$.
* B–T 1933 §1 (page 4, formula (7) and the "normal" definition on
  the same page) writes $Q_j(x) = \mu_j\,x\log x + \gamma_j\,x$ for
  the canonical normal-case exponent ($p=1$), explicitly extending
  Birkhoff's notation.
* Both papers explicitly cite Adams 1928 (Trans. AMS **30**, 507–541)
  in footnote 2 and characterise Adams's formal series as "of the
  same kind as appear in the regular case" (Birkhoff 1930 page 2),
  i.e., **same μ-units**.
* PCF-1 v1.3 §6 (Theorem 5, TeX line 525) writes
  $\log|\delta_n| = -A\,n\log n + \alpha n - \beta_w\log n + \gamma_w
  + o(1)$, with $-A$ as the coefficient of $n\log n$ — **directly
  matching** the difference $\mu_{\mathrm{sub}} - \mu_{\mathrm{dom}}$
  of the two B–T exponents (since $\delta_n$ is sub/dom at leading
  order).

There is therefore **no factor of 2** between SIARC's $A$ and
Birkhoff/B–T's μ at the normalisation level. The Phase-1 worry
"$\sigma_{\mathrm{Adams}} = \tfrac{1}{2}\sigma_{\mathrm{Wasow}}$" is
identified as a **paraphrase artefact** and is falsified by the direct
on-disk evidence (Birkhoff 1930 page 2 + B–T 1933 page 5).

The Phase-1 literature-derivable bracket

$$
   A \in [d,\ 2d]
   \quad \text{for } d \ge 3, \text{ literature-derivable}
$$

with B4 = 2d at the upper end **holds under the Wasow-normalisation
reading**. Phase 2 may launch with target B4 = 2d (the present
upper-bound vertex of the bracket); Phase 2's task is the
lower-bound lift from $d$ to $2d$ via a non-resonance / non-degeneracy
argument on the SIARC PCF stratum.

The alternative branch — `A01_ADAMS_READING_CONFIRMED`, in which the
bracket would shift to $[d/2, d]$ and B4 = 2d would be **outside**
the literature bracket (a major-halt branch) — is **not supported**
by the on-disk evidence and is **falsified** to the extent that
B–T 1933 and Birkhoff 1930 both characterise Adams's normalisation as
identical to their own.

## Caveats logged in `discrepancy_log.json`

1. **Wasow 1965 §X.2–§X.3 not primary-quoted.** The Dover-reprint
   PDF on disk is image-only with no OCR layer (see
   [D2](wasow_section_X_normalization.md)). The agent triangulated
   through B–T 1933 + Birkhoff 1930 directly; this resolves the
   **normalisation-match** question (the A-01 ambiguity) but does
   **not** verbatim-verify the Wasow §X.3 polynomial-coefficient
   slope bound that supplies the **upper end** of the bracket.

2. **Adams 1928 not primary-accessed (per H-3).** All Adams-related
   claims are sourced from Birkhoff 1930 footnote 2 + B–T 1933
   footnote 2 + Birkhoff 1930 page 2 textual characterisation of
   Adams's formal-series form. This is the maximum the on-disk
   literature permits without primary Adams access; primary Adams
   1928 access would tighten the verdict from
   "WASOW_READING_CONFIRMED via transitive Birkhoff/B–T evidence"
   to "WASOW_READING_CONFIRMED via direct Adams + Birkhoff/B–T
   triangulation".

3. **The bracket derivation itself (the upper bound $\mu \le 2d$ in
   terms of polynomial degree $d$) inherits Phase-1's paraphrase
   from Wasow §X.3 and Birkhoff 1911.** The present verdict resolves
   the **normalisation-match** half of A-01; the **bracket-tightness**
   half of the Phase-1 claim remains paraphrase-grade. This is an
   acknowledged residual that does not prevent Phase 2 launch under
   the Wasow reading, but should be tightened by a separate
   literature pass or by Phase 2's own internal argument.

These three caveats do not block the present verdict; they are
documented for synthesizer arbitration and for subsequent literature
passes.

---

## Effect on H1 (Theory-Fleet) label

See [`h1_label_disposition_advisory.md`](h1_label_disposition_advisory.md).
The agent recommends **HOLD-FOR-SYNTHESIZER-ARBITRATION** rather than
either keep-as-is or downgrade, because the present verdict is
WASOW_READING_CONFIRMED with explicit caveats (1)–(3) above and the
synthesizer is best placed to weigh the residual paraphrase against
the umbrella v2.0 phrasing that H1 anchors on.

---

## Out of scope (do NOT execute as part of this verdict)

* Phase 2 lower-bound lift (separate relay
  `T1-BIRKHOFF-PHASE2-LIFT-LOWER`).
* Modifying H1, umbrella v2.0 main.tex, or PCF-1 v1.3 (operator-side
  after synthesizer arbitration).
* Re-deriving the [d, 2d] bracket (cited from Phase-1; out of scope).
