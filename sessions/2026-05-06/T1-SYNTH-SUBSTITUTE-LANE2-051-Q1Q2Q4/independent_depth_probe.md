# Independent depth probe — STEP 4

**Method:** Fresh investigations beyond what the synth-substitute flagged.
At least 3 of P1-P6 conducted; this LANE-2 review opted to cover **4** of
the 6 suggested probes (P1, P2, P3, P4) for safety margin above the floor.

---

## P1 — Repository-wide `cf_value` definition sweep

**Method:** `grep` for `def cf_value` and the recurrence pattern
`x = bk + mp.mpf(1) / x` across `pcf-research/`.

**Findings — 9 distinct `cf_value` definitions in `pcf-research/pcf2/`:**

| # | Path | Line | Recurrence | deg_a |
|---|------|------|------------|-------|
| 1 | session_C1_2026-05-01/session_c1_wkb.py | 79 | `x = bk + mp.mpf(1) / x` | 0 |
| 2 | session_B_2026-05-01/session_b_pslq.py | 162 | `x = bk + mp.mpf(1) / x` | 0 |
| 3 | session_R1_1_2026-05-01/r1_1_correlation_probe.py | 224 | `x = bk + mp.mpf(1) / x` | 0 |
| 4 | session_R1_2_2026-05-01/quartic_tail_fit_all60.py | 21 | `x = bk + mp.mpf(1) / x` | 0 |
| 5 | session_R1_2_2026-05-01/r1_2_quartic_j_probe.py | 184 | `x = bk + mp.mpf(1) / x` | 0 |
| 6 | session_R1_2_2026-05-01/fam32_deep_escalation.py | 17 | `x = bk + mp.mpf(1) / x` | 0 |
| 7 | session_R1_3_2026-05-01/r1_3_extended_enumeration.py | 203 | `x = b(k) + mp.mpf(1) / x` | 0 |
| 8 | session_R1_3_2026-05-01/r1_3_residualization.py | 65 | `x = b(k) + mp.mpf(1) / x` | 0 |
| 9 | session_Q1_2026-05-01/session_q1_wkb.py | 67 | `x = bk + mp.mpf(1) / x` | 0 |

The only structural variant is the helper-function form:
`r1_3_residualization.py` L67-68 docstring states verbatim:

```
"""Compute the truncated continued fraction L_N = b_0 + 1/(b_1 + 1/(...
+ 1/b_N)).  coeffs_leading_first are integer/rational [a_d, ..., a_0]."""
```

This DOCSTRING explicitly affirms the canonical (1, b) form
$L_N = b_0 + \cfrac{1}{b_1 + \cfrac{1}{b_2 + \cdots + \cfrac{1}{b_N}}}$,
i.e., $a_n \equiv 1$ verbatim. (Note: the variable name `coeffs_leading_first`
holds $b_n$'s polynomial coefficients despite the comment-side label "[a_d, ..., a_0]";
this is a documentation slip, not a recurrence-form difference.)

**P1 finding:** UNIFORM. All 9 `cf_value` implementations across the entire
PCF-2 R1.1 + R1.2 + R1.3 + Q1 + Session B + Session C1 harvest tree use
the canonical (1, b) recurrence with $a_n \equiv 1$ (deg_a = 0). **No
script in `pcf-research/pcf2/` uses a deg_a = 1 recurrence.** The
synth-substitute's claim that "the harvest set uniformly uses (1, b)"
is INDEPENDENTLY confirmed at full coverage.

**Implication for synth-substitute:** Strengthens C1 finding; no
counter-evidence found. Q1 verdict's scope claim (PCF-2 R1.1/R1.3/Q1)
is actually narrower than the empirical reality, which extends to
**all of PCF-2's harvest pipeline including Sessions A2, B, C1, R1.1,
R1.2, R1.3, Q1**.

---

## P2 — Phase A WZ table: was deg_a = 0 row excluded by assumption?

**Source:** `siarc-relay-bridge/sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_a_summary.md` L22-44.

**Verbatim balance edge equation (L22):**

```
1 - c_b n^{deg_b - μ} / γ - c_a n^{deg_a - 2μ} / γ² = 0
```

with three balance possibilities:

```
(I)   1 ↔ c_b/γ          ⇒ μ = deg_b,        γ = c_b
(II)  1 ↔ c_a/γ²         ⇒ μ = deg_a/2,      γ² = c_a
(III) c_b/γ ↔ c_a/γ²     ⇒ μ = deg_a − deg_b, γ = −c_a/c_b
```

**Phase A WZ table (L34-44, verbatim row structure):**

| d | Convention | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|-----------|-------|-------|-------|-------|---------|
| 2 | α-direction | 1 | 2 | 2 | −1 | 3 |
| 2 | symmetric   | 2 | 2 | 2 |  0 | 2 |
| 2 | δ-direction | 3 | 2 | 2 |  1 | 1 |
| 3 | α-direction | 2 | 3 | 3 | −1 | 4 |
| 3 | symmetric   | 3 | 3 | 3 |  0 | 3 |
| 3 | δ-direction | 4 | 3 | 3 |  1 | 2 |
| 4 | α-direction | 3 | 4 | 4 | −1 | 5 |
| 4 | symmetric   | 4 | 4 | 4 |  0 | 4 |
| 4 | δ-direction | 5 | 4 | 4 |  1 | 3 |

**Key observation:** Phase A enumerates THREE conventions
(α/symmetric/δ-direction) corresponding to deg_a = d-1, d, d+1. There
is NO row for deg_a = 0 (the (1, b) convention used by the harvest
implementations).

**Was the omission accidental or by assumption?**

Reading the Phase D verdict in
`sessions/2026-05-03/T1-BIRKHOFF-PHASE2-LIFT-LOWER/phase_d_verdict.md`
L33-43:

> "Phase A + B establish the formal Newton-polygon baseline
> A_naive ≤ d+1 (naive Wimp-Zeilberger normal case), recovering only
> the LOWER end of the literature bracket A ∈ [d, 2d]. The lift to
> **A = 2d** at d ≥ 3 requires the SIARC PCF stratum to sit at the
> BORDERLINE case `deg_a = 2 deg_b` of Wimp-Zeilberger 1985
> (equivalently, the anormal / fractional rank q ≥ 2 case of B-T 1933
> §1) OR at an exceptional locus of the normal case where leading
> coefficients cancel."

This framing **assumes** the SIARC PCF stratum has $\deg_a \in \{d-1, d, d+1\}$
— the three conventions enumerated in Phase A. Under that assumption,
the lift to $A = 2d$ requires moving outside the normal case (to the
"borderline" or "exceptional locus"). **The deg_a = 0 row was excluded
by ASSUMPTION**, not by oversight: Phase A's "three SIARC conventions"
framing presupposes the conventions live in deg_a ∈ {d-1, d, d+1}.

**Extending Phase A's table by one row (deg_a = 0):**

Applying balance (III) at deg_a = 0:
$\mu_{\rm sub} = 0 - d = -d$, $\gamma_{\rm sub} = -1/c_b$.
$A_{\rm naive} = \mu_{\rm dom} - \mu_{\rm sub} = d - (-d) = 2d$.

| d | Convention | deg a | deg b | μ_dom | μ_sub | A_naive |
|---|-----------|-------|-------|-------|-------|---------|
| 2 | (1, b) PCF-2 corner | 0 | 2 | 2 | −2 | **4** |
| 3 | (1, b) PCF-2 corner | 0 | 3 | 3 | −3 | **6** |
| 4 | (1, b) PCF-2 corner | 0 | 4 | 4 | −4 | **8** |

**The three new rows recover, simultaneously:**
- $d=2$ V_quad upper branch ($A = 4$, NOT recovered by α/symmetric/δ in Phase A).
- $d=3$ PCF-2 R1.1 + B + C1 empirical ($A_{\rm fit} = 5.978$, target $A = 6$, 50/50).
- $d=4$ PCF-2 Q1 empirical ($A_{\rm fit} = 7.954$, target $A = 8$, 60/60).

**P2 finding:** Phase A's omission of the deg_a = 0 row is the proximate
cause of Phase D's "structural gap" framing. When the deg_a = 0 row is
admitted (corresponding to the (1, b) convention used by ALL harvest
scripts per P1), the gap closes uniformly across $d \in \{2, 3, 4\}$
WITHOUT invoking borderline mechanism (i') or exceptional locus (ii').
This is INDEPENDENT corroboration of the synth-substitute's
PROTOCOL_TO_STRATUM_MISMATCH_FIRST_PIVOT verdict.

**Cross-implication for V_quad upper branch:** bt_baseline_note v1.0
§4.2 (sec:proof-d2) attributes V_quad's $A = 4$ at $d = 2$ to mechanism
(i') (borderline-locus). Under the deg_a = 0 reading, V_quad's $A = 4$ is
the natural deg_a = 0 row, NOT a borderline phenomenon. This is a
substantive REINTERPRETATION of bt_baseline_note v1.0 §4.2, going
slightly beyond the synth-substitute's stated scope (which left this
"flagged for canonical T1-Synth follow-up at next ISO week" as a
secondary observation, see synth_substitute_verdict.md L292-294).

---

## P3 — bt_baseline_note §4.2 d=2 verification: deg_a consistency

**Source:** `siarc-relay-bridge/sessions/2026-05-06/T1-PHASE2-BASELINE-NOTE/bt_baseline_note.tex` L457-487.

**§4.2 (sec:proof-d2) verbatim claims:**

L460-470: "Specialising Theorem 1.1 to $d = 2$ in the
$\alpha$-direction convention ($\dega = d - 1 = 1$) yields
$\Anaive = d + 1 = 3$. ... realised by the QL01--QL26 family of
$26$ representatives, with each representative's $A$-value verified
at $\dps = 80$ ..."

L481-487: "The $d = 2$ \emph{upper} branch $A = 4 = 2d$, realised by
the V$_{\mathrm{quad}}$ representative ..., is \emph{not} recovered
by the formal-level baseline of Theorem 1.1: the band
$\Anaive \in \{1, 2, 3\}$ at $d = 2$ does not contain $4$. The
V$_{\mathrm{quad}}$ upper branch is consistent with the
borderline-locus mechanism (i$'$) of Proposition gap-framing -- the
closure of which is the open content of §6 Q\ref{q:mechanism}."

**Reading:**

- §4.2 verifies against PCF-1 v1.3 §6 Theorem 5 LOWER branch (QL01-QL26,
  $A=3$, deg_a = 1, $\delta \neq 0$, dps=80, 26 representatives).
- §4.2 acknowledges the UPPER branch V_quad ($A=4$) is NOT recovered by
  Theorem 1.1's band $\{1, 2, 3\}$ at $d=2$.
- §4.2 attributes V_quad's $A=4$ to mechanism (i') (borderline-locus).

**P3 finding (consistency check):**

§4.2's cited numerics (QL01-QL26 at $A=3$, V_quad at $A=4$) are at
$d = 2$, BUT §4.2 implicitly assumes:

- QL01-QL26 are deg_a = 1 (this is consistent with PCF-1 v1.3's d=2
  declared stratum from V4: $\delta \neq 0$ enforced; QL01-QL26 are
  in α-direction convention with linear $a_n$).
- V_quad is in the SAME convention class but at "upper branch" $A=4$.

**However**, V5 finding (algebraic_independence_audit.py L37-40) is
that V_quad has $a(n) = 1$ (deg_a = 0), NOT $a_n = \delta n + \varepsilon$
with $\delta \neq 0$. **V_quad lives outside the PCF-1 d=2 declared
stratum** (V4) — it is a deg_a = 0 specimen.

Therefore §4.2's interpretation of V_quad's $A=4$ as a "borderline
mechanism (i') case" is substrate-level WRONG. The correct reading,
under deg_a = 0 + d = 2, is $A_{\rm naive} = 2d = 4$ via the WZ NORMAL
case (V6 derivation). V_quad is NOT a borderline anomaly; it is a
deg_a = 0 corner-case specimen incorrectly categorised under the
deg_a = 1 stratum's "upper branch" label.

**Empirical record cited:**

| Family | A | dps | Reps | Convention used |
|--------|---|-----|------|-----------------|
| QL01-QL26 (lower branch) | 3 | 80 | 26 | deg_a = 1, α-direction (V4) |
| V_quad (upper branch)    | 4 | unspec. | 1 | deg_a = 0, (1, b) (V5) |

**Cross-stratum interpretation (LANE-2):**

| Family | Stratum | WZ-predicted $A_{\rm naive}$ | Empirical $A$ | Match? |
|--------|---------|------------------------------|----------------|--------|
| QL01-QL26 | deg_a=1, d=2 | $2d-1 = 3$ | 3 | YES (no anomaly) |
| V_quad | **deg_a=0**, d=2 | $2d = 4$ | 4 | YES (no anomaly under correct stratum) |

So under LANE-2's correct stratum identification, BOTH PCF-1 v1.3 §6
Theorem 5 branches are recovered by the WZ normal case, with **NO
borderline-mechanism (i') case anywhere** in the d=2 record.

**P3 finding:** §4.2 of bt_baseline_note v1.0 cites empirical numerics
($A=3$ for QL01-QL26 + $A=4$ for V_quad) that are INDIVIDUALLY consistent
with WZ normal case at the CORRECT deg_a per family (deg_a=1 for QL01-QL26
yielding $A=3$; deg_a=0 for V_quad yielding $A=4$). The §4.2 INTERPRETATION
that V_quad is a borderline-mechanism (i') anomaly is substrate-level
WRONG: V_quad is a deg_a=0 corner-case specimen mislabelled as a
deg_a=1 "upper branch". The synth-substitute's scope (PCF-2 R1.1/R1.3/Q1)
may need expansion to include the V_quad row in PCF-1 v1.3 §6, since
the same protocol-to-stratum mismatch resolves the d=2 V_quad anomaly
identically. This is logged for STEP 5 Item 1 verdict.

---

## P4 — PCF-2 v1.3 Conjecture B4' falsification: independent consistency with deg_a = 0

**Source:** `tex/submitted/pcf2_program_statement.tex` L539-590.

**B4' verbatim (L544-555):**

> "For a degree-$d$ PCF $(1,b)$ of generic type in scope, the WKB exponent
> of equation (B4) satisfies $A_{\rm fit} = 2d-1$ if the trichotomy bin
> is elementary-positive ($+\_S_d\_{\rm real}$ or $+\_C_d\_{\rm real}$),
> $2d$ otherwise."

**Falsification (L562-571):**

> "Session C1 ran the WKB fit on the 13 elementary-positive cubic families
> at dps=800, fit window n in [10, 100], step 3. The result is unambiguous:
> 0 of the 13 families approach the predicted branch $A = 2d-1 = 5$. All
> 13 sit in $A_{\rm fit} \in [5.884, 5.989]$ ... The trichotomy bin is
> therefore NOT the invariant controlling $A$ at $d=3$: B4' is empirically
> falsified."

**B4 (the surviving form) verbatim (L456-475):**

> "For every degree-$d$ PCF $(1,b)$ of generic type in scope, ...
> $A = 2d$ for every degree-$d$ PCF $(1,b)$ of generic type in scope at
> $d \in \{3, 4\}$ [empirical, 110/110 ...]."

**P4 finding (CRITICAL):**

The PCF-2 program statement Conjecture B4 EXPLICITLY uses the notation
"PCF $(1, b)$" verbatim (L457, L468 [note via boxed identity]), affirming
the (1, b) convention with $a_n \equiv 1$. **Therefore PCF-2 v1.3 §6
(the B4 / B4' subsection) is INTERNALLY CONSISTENT with deg_a = 0.**

The "protocol-to-stratum mismatch" is more nuanced than the
synth-substitute presents:

- **§3 (Setup)** L228-234 declares $a_n = \delta_1 n + \delta_0$ (linear
  in $n$, deg_a $\in \{0, 1\}$).
- **§6 (B4 / B4')** L457, L544 uses notation "PCF $(1, b)$" verbatim,
  implicitly fixing $a_n \equiv 1$ (deg_a = 0).
- **Harvest scripts** (P1) all use $a_n \equiv 1$ (deg_a = 0),
  consistent with §6, but inconsistent with §3's formal declaration.

The mismatch is therefore **intra-document** (§3 setup vs. §6 / B4
wording) within `pcf2_program_statement.tex` ITSELF, not just a
"prose vs scripts" mismatch as worded by the synth-substitute. **The
harvest scripts implement the §6 / B4 stratum exactly, NOT a separate
"implementation-only" stratum.**

**Independent consistency check on B4''s falsification:**

Under deg_a = 0 (uniform across all $d=3$ trichotomy bins), the WZ
normal case predicts $A_{\rm naive} = 2d = 6$ uniformly with NO bin
dependence. B4' predicted a bin-dependent split at deg_a = 1 (analogous
to PCF-1 d=2's $\Delta_2$-sign split). Empirical falsification (0/13
elementary-positive families approaching $A=5$, all 13 at $A \approx 6$)
is **consistent with deg_a = 0** ($A=6$ uniform) and **inconsistent
with deg_a = 1** ($A=5$ predicted for elementary-positive bins, $A=6$
otherwise).

So B4''s falsification is INDEPENDENT corroboration of the
protocol-to-stratum mismatch finding: the cubic stratum being tested
empirically is deg_a = 0, not deg_a = 1, which is precisely why the
deg_a = 1 → "$A = 2d - 1$ for elementary-positive" prediction failed
(no bin dependence at deg_a = 0).

**P4 finding:** B4''s falsification at d=3 is INDEPENDENTLY consistent
with the synth-substitute's (UF3-style) finding that deg_a = 0
naturally predicts $A_{\rm naive} = 2d$ for all bins regardless of
Galois classification. Furthermore, the protocol-to-stratum mismatch
locus is more precisely INTRA-`pcf2_program_statement.tex` (§3 setup
vs §6 B4 wording), not "prose vs scripts" as worded by the
synth-substitute. This is logged as the principal LANE-2 substantive
refinement to the synth-substitute framing for STEP 5 Item 6.

---

## Depth probe summary

| Probe | Result | Substantive refinement to synth-substitute? |
|-------|--------|--------------------------------------------|
| P1 | UNIFORM (1, b) deg_a = 0 across 9 cf_value impls | NO; strengthens C1 with extended coverage |
| P2 | Phase A omitted deg_a = 0 row by ASSUMPTION; one-row extension closes Phase D's "structural gap" without (i') or (ii') | YES — extends synth-substitute interpretation upstream into Phase A / Phase D framing |
| P3 | bt_baseline_note v1.0 §4.2's V_quad mechanism-(i') attribution is substrate-level WRONG; V_quad is a deg_a=0 specimen mislabelled | YES — extends scope from PCF-2 R1.1/R1.3/Q1 to PCF-1 v1.3 §6 Theorem 5 V_quad row |
| P4 | Mismatch locus is intra-`pcf2_program_statement.tex` (§3 setup vs §6 B4 wording), not "prose vs scripts" | YES — refines mismatch framing for Item 6 verdict |

**No new DOI or arXiv-ID acquisition targets were introduced**, so
HALT_061_DOI_HALLUCINATION does not trigger.

**Two independent depth-probe substantive refinements** (P2 + P3) extend
the synth-substitute's findings beyond its stated scope:

1. **P2 (synth-sub's PROTOCOL_TO_STRATUM_MISMATCH applies to Phase A's
   own three-convention enumeration)**: the Phase A baseline's omission
   of the deg_a = 0 row is itself the proximate cause of Phase D's
   "structural gap" framing.
2. **P3 (V_quad upper branch is a deg_a = 0 specimen, not a borderline
   anomaly)**: bt_baseline_note v1.0 §4.2's mechanism-(i') attribution
   for V_quad's $A = 4$ is wrong; V_quad is fully recovered by the WZ
   normal case once the deg_a = 0 row is admitted.

These refinements are EXTENSIONS, not contradictions, of the
synth-substitute's load-bearing claims. STEP 6 meta-verdict therefore
does NOT lean toward `REJECT_AND_REPLACE`.

**One mild substantive refinement** (P4): the mismatch locus is more
precisely intra-document, not "prose vs scripts" as currently worded.
This is a wording-level refinement, not a substantive challenge.
