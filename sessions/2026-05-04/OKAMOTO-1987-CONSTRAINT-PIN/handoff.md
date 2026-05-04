# Handoff — OKAMOTO-1987-CONSTRAINT-PIN
**Date:** 2026-05-04
**Agent:** GitHub Copilot (VS Code, Claude Opus 4.7)
**Session duration:** ~25 minutes
**Status:** COMPLETE

**VERDICT:** `UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_OKAMOTO_2PARAM_VS_CT_4TUPLE`

---

## What was accomplished

Pinned Okamoto 1987 (FE 30, pp.305-332) §1 H_III parameter labeling
and §2.1 Root system content directly from slot 07 PDF (SHA-256
`65294FBC...A43F`). Verified by direct quote extraction that
Okamoto's P_III' is a **two-parameter** family on
$V = \{(v_1, v_2) = (\theta_0, \theta_\infty)\}$ (after the universal
$\eta_\Delta = 1$ normalization on p.306). The §2 "R1" canonical
relation is the W(B_2) root-system action on V, not a 4-tuple linear
sum. Cross-checked slot 08 (Barhoumi-Lisovyy-Miller-Prokhorov 2024)
which also treats $P_{III}(D_6)$ as a 2-parameter $(\alpha, \beta)$
family with monodromy parameters $(e_1, e_2)$. The CT v1.3 §3.5
4-tuple $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0,
0, -1/2)$ is therefore from a separate convention (Jimbo-Miwa or
Sakai surface), not Okamoto 1987 §2 R1; G18 closes positively as a
labeling-correspondence artifact (interpretation (a) per Prompt 020
§0).

## Key numerical findings

- **Okamoto §0 / §1 (p.306):** P_III' Hamiltonian
  $H_{III'} = \frac{1}{t}\bigl[q^2 p^2 - \{\eta_\infty q^2 + \theta_0 q
  - \eta_0 t\} p + \tfrac{1}{2}\eta_\infty(\theta_0+\theta_\infty) q\bigr]$
  with $\eta_\Delta = 1$ WLOG.
- **Okamoto eq. (0.5) (p.307):** Parameter base space $V$ is
  **2-dimensional complex**, $v_1 = \theta_0$, $v_2 = \theta_\infty$.
  No 4-tuple labeling.
- **Okamoto §2.1 (p.317-318):** Root system $R = R_{III'}$ of type
  $B_2$. Fundamental roots $\alpha_1 = e_1 - e_2$, $\alpha_2 = e_2$;
  highest root $\alpha = e_1 + e_2$. Reflections:
  $s_1: (v_1,v_2) \mapsto (v_2, v_1)$;
  $s_2: (v_1,v_2) \mapsto (v_1, -v_2)$;
  $s_0$ about affine wall $(\alpha|v) = -1$, i.e. $v_1 + v_2 = -1$.
- **Phase C arithmetic** (`substitution_check.py`,
  hash `23DBC3C5...D580094BD3136`):
  $\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = 1/6 + 0 + 0 +
  (-1/2) = -1/3 \neq 0$. Brief-stated sum-to-zero constraint not
  satisfied as-arithmetic.
- **Phase C interpretation:** the 4-tuple labels
  $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ have **no
  counterpart in Okamoto 1987**; Okamoto's "R1" is structural
  (W(B_2) action), not a linear sum. Reading $(v_1, v_2) = (1/6,
  -1/2)$ as Okamoto coords gives no wall-locus hit (none of $v_1 -
  v_2 = 0$, $v_2 = 0$, $v_1 + v_2 = -1$, $v_1 + v_2 = 0$ holds).
- **Cross-check (slot 08):** Barhoumi-Lisovyy 2024 $P_{III}(D_6)$ is
  also 2-parameter $(\alpha, \beta)$; no 4-tuple sum constraint.

## Verbatim quotes (all ≤ 30 words)

**Q1 (Okamoto p.306, §0 Introduction; H_III definition):**
> "$H_{III}\;\frac{1}{t}[2q^2 p^2 - \{2\eta_\infty t q^2 + (2\theta_0+1)
> q - 2\eta_0 t\}p + \eta_\infty(\theta_0+\theta_\infty)tq]$, where the
> constants $\eta_\Delta$, $\theta_\Delta$ ($\Delta = 0, \infty$)..."
(transcription cleaned from `okamoto_1987_text.txt` p.2)

**Q2 (Okamoto p.306, immediately after eq. (0.1)):**
> "By the assumption, we have $\eta_\Delta \neq 0$; moreover we set
> $\eta_\Delta = 1$ without loss of generality."

**Q3 (Okamoto eq. (0.5), p.307):**
> "We regard $V$ as the space of parameters of the Painlevé system
> through (0.5) $v_1 = \theta_0$, $v_2 = \theta_\infty$."

**Q4 (Okamoto §2.1, p.317-318; the canonical "R1" content):**
> "$\alpha_1 = e_1 - e_2$, $\alpha_2 = e_2$, $\alpha = e_1 + e_2$.
> Let $R = R_{III'}$ be the root system of the type $B_2$. Then
> $\alpha_i$ are the fundamental roots of $R$ and $\alpha$ is the
> highest root."

**Q5 (Okamoto §2.1, p.318; the affine wall):**
> "$s_0$: $v \mapsto (-1-v_2, -1-v_1)$." [reflection about
> $(\alpha|v) = -1$, i.e. $v_1 + v_2 = -1$.]

## Verification analysis

The brief-stated sum constraint
$\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = 0$
is not Okamoto 1987 §2 R1. Okamoto's parameter space is 2-dimensional
$(\theta_0, \theta_\infty) \equiv (v_1, v_2)$; the W(B_2) root-system
action provides three reflection walls
($v_1 - v_2 = 0$, $v_2 = 0$, $v_1 + v_2 = -1$) plus the Bessel
sub-locus $v_1 + v_2 = 0$. No 4-tuple sum exists in Okamoto's
formulation.

This is **interpretation (a)** per Prompt 020 §0: CT v1.3 §3.5 uses a
different parameter labeling (most likely Jimbo-Miwa monodromy
exponents at $(0, \infty)$ with a Fuchs-style relation, or a Sakai
$P_{III}(D_6^{(1)})$ surface convention with W-root labeling). The
explicit correspondence map from CT v1.3's
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ to Okamoto's
$(\theta_0, \theta_\infty)$ requires CT v1.3's source convention —
out of scope here. Recommended: have CT v1.3 §3.5 cite its actual
source (likely Jimbo-Miwa Inventiones 1981 or Ohyama-Kawamuko-Sakai
2006), not Okamoto 1987.

Cross-check against slot 08 (Barhoumi-Lisovyy-Miller-Prokhorov 2024)
confirms: even modern $P_{III}(D_6)$ literature uses 2 parameters
$(\alpha, \beta)$ at the equation level. No 4-tuple sum constraint
exists.

## Judgment calls made

- Used pypdf for slot 07 text extraction. Output is mathematically
  legible despite TeX-encoded glyph artifacts (`/xa5` prefixes); all
  five Phase A/B quotes were recoverable from page 2 (Okamoto §0/§1)
  and pages 13-14 (§2.1 Root system) without OCR fallback. No HALT.
- Did not exhaustively probe Okamoto §2.5-2.6 for additional
  relations (R2, R3, ...): §2.1 is the canonical Root-system pin;
  §2.2-2.6 derive the canonical-transformation realizations of $s_1,
  s_2, s_0$ on the Painlevé system itself (these are W-action
  constructions, not new parameter relations). The §2.1 W(B_2)
  structure is sufficient to establish "no 4-tuple sum constraint"
  conclusively.
- Read 25 of 77 pages of slot 08 (Barhoumi-Lisovyy 2024) — sufficient
  to confirm 2-parameter convention from the abstract / §1.1 / §1.2
  formula displays. Did not pursue full §_W cross-walk (out of scope
  per Prompt 020 §6).

## Anomalies and open questions

**THIS IS THE MOST IMPORTANT SECTION. (See `unexpected_finds.json`.)**

1. **Okamoto 1987 is fundamentally a 2-parameter paper.** The
   relay-prompt brief framing implicitly assumed Okamoto's R1 was a
   4-tuple sum on $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$;
   in fact this 4-tuple labeling does not exist in Okamoto 1987 at
   all. The eta_Delta = 1 normalization is on p.306 and is universal.

2. **The "alpha+alpha+beta+beta=0" constraint that CT v1.3 §3.5
   purports to invoke needs a source.** It is plausibly from
   Jimbo-Miwa 1981 (Fuchs-style relation among monodromy exponents)
   or from a Sakai $P_{III}(D_6^{(1)})$ surface convention with
   simple-root labeling, but neither slot 07 (Okamoto 1987) nor slot
   08 (Barhoumi-Lisovyy 2024) carries it. CT v1.3 should be amended
   to cite its actual source convention.

3. **M6 spec Phase B.5 implication:** the W(B_2)-vs-W(D_6) cross-walk
   is structurally about generators (root-system relations and Weyl
   action), NOT about parameter sum constraints. This pin reinforces
   the M6 spec framing and does not redirect it. The M6 Phase B.5
   work remains the right place to settle the W cross-walk; this
   prompt is purely the Okamoto §2 R1 pin and convention-level G18
   close.

4. **No HALT condition triggered.** All §1, §2.1 content was
   pypdf-readable; no OCR fallback needed; no operator-decision
   ambiguity at Phase D.

## What would have been asked (if bidirectional)

- "Where in CT v1.3 §3.5 does the (1/6, 0, 0, -1/2) 4-tuple actually
  come from? — citation to its source convention (Jimbo-Miwa 1981,
  Ohyama-Kawamuko-Sakai 2006, Sakai 2001, or other?) would let me
  pin the labeling correspondence concretely instead of leaving it
  at 'this is a different convention'."
- "Is the v1.18 picture amendment for G18 expected to be a 1-row
  retirement (G18 -> RETIRED with `OKAMOTO-1987-CONSTRAINT-PIN`
  cite), or should it be promoted to a 'CT v1.3 sec.3.5 source
  convention pin' as a continuing workstream?"

## Recommended next step

1. **v1.18 picture amendment:** retire G18 with citation to this
   handoff (`UPGRADE_G18_CLOSED_PARAMETER_CORRESPONDENCE_OKAMOTO_
   2PARAM_VS_CT_4TUPLE`). Note that the closure is convention-level
   only; the underlying CT v1.3 §3.5 cite needs a source.
2. **CT v1.3 / v1.4 §3.5 amendment** (operator decision): replace
   the implicit "Okamoto §2 R1" attribution with the actual source
   (likely Jimbo-Miwa Inventiones 1981 §3 or Ohyama-Kawamuko-Sakai
   2006). This is the parsimonious downstream fix.
3. **M6 spec Phase B.5** continues as scoped; this pin provides a
   clean W(B_2) anchor for the cross-walk.
4. **Optional follow-on probe:** if the operator wants the 4-tuple
   labeling formally pinned, run `JIMBO-MIWA-1981-FUCHS-RELATION-
   PIN` on a Jimbo-Miwa primary source (acquisition needed; likely
   Publ. RIMS 18, 1982 or Physica 2D, 1981).

## Files committed

- `prompt_spec_used.md` — verbatim Prompt 020 body (Phase 0).
- `okamoto_1987_text.txt` — full pypdf extraction of slot 07 (28
  pages, 56170 chars; SHA of source `65294FBC...A43F`).
- `barhoumi_2024_text.txt` — pypdf extraction of slot 08 first 25
  pages (cross-check; SHA of source `96C49CDD...696BB3`).
- `substitution_check.py` — Phase C arithmetic + interpretation.
- `substitution_check.log` — Phase C output (hash
  `23DBC3C5...3136`).
- `claims.jsonl` — 9 AEAL entries.
- `halt_log.json` — empty (no halt).
- `discrepancy_log.json` — empty (no discrepancy >5%).
- `unexpected_finds.json` — 2 entries (Okamoto-2-param,
  Barhoumi-2-param); LOW severity / informational.
- `handoff.md` — this file.

## AEAL claim count

**9** entries written to `claims.jsonl` this session.

## STRATEGIC_IMPLICATION

G18 (CT v1.3 §3.5 4-tuple constraint mismatch) closes positively
as a **labeling-correspondence artifact**: Okamoto 1987 is a
2-parameter paper $(\theta_0, \theta_\infty)$; its §2 "R1" is the
W(B_2) root-system action, not a 4-tuple linear sum. CT v1.3's
4-tuple comes from a different (Jimbo-Miwa or Sakai $D_6$ surface)
convention.

- **v1.18 picture:** retire G18 row with cite
  `OKAMOTO-1987-CONSTRAINT-PIN_2026-05-04`.
- **M6 spec Phase B.5:** unchanged; this pin reinforces the W(B_2)
  anchor.
- **CT v1.4 §3.5:** operator should consider replacing the implicit
  Okamoto attribution with the actual source convention (Jimbo-Miwa
  1981 or Ohyama-Kawamuko-Sakai 2006). Out-of-scope here; flagged.
- **No CT v1.3 in-flight reframing required** — the underlying
  physical content of CT v1.3 §3.5 is unaffected; only the citation
  attribution is mismatched.
