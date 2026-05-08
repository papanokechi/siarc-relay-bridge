# QD-5 Audit Verdict
**Audit performed:** 2026-05-08 ~14:35 JST
**Agent:** GitHub Copilot (VS Code)
**Substrates audited:**

  - 058R Section B.3: `siarc-relay-bridge/sessions/2026-05-06/CC-VQUAD-PIII-NORMALIZATION-MAP-RERE-FIRE/phase_b_canonical_map.md` lines 72-158
  - p12_journal sec:vquad: `tex/submitted/p12_journal_main.tex` lines 958-1090 (whole section)
  - LIT dict cross-check: `pcf-research/channel/cc_pipeline_2026-05-01/vquad_p3d6_recovery.py` lines 43-50

---

## Phase A findings (058R B.3)

### Q-A1: raw Hamiltonian parameters?

**Answer: YES.** 058R Section B.3 frames the output domain of
$M = \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}$
as the canonical $(q, p, t)$ Hamiltonian system of Okamoto 1987 §1.1
+ KNY 2017 §8.5.17 with raw parameters $(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$
on the Okamoto side and $(a_0, a_1, a_2)$ on the KNY side.

Cited line numbers (`phase_b_canonical_map.md`):

- **L24-30** — section B.1 introduces the Okamoto Hamiltonian
  $H_{III}(q, p, t; \theta_0, \theta_\infty)$ with parameters
  $\mathbf{v} = (v_1, v_2) = (\theta_0, \theta_\infty) \in \mathbb{C}^2$
  per Okamoto eq. (0.5).
- **L99-114** — section B.3 names KNY 2017 eq. (8.237) Hamiltonian
  $H_{D_6}^{\mathrm{KNY}}$ in $(q, p, t; a_1, a_2)$.
- **L118-127** — Φ_symp construction at the level of the canonical
  $(q, p) \leftrightarrow (q, p)$ gauge transformation between
  $H_{III}$ and $H_{D_6}^{\mathrm{KNY}}$.

Verbatim quote (`phase_b_canonical_map.md` L121-123, 30 words):

> "$\Phi_{\mathrm{symp}}$ is the canonical $(q, p) \leftrightarrow (q, p)$
> gauge transformation that identifies Okamoto 1987's $H_{III}$ (B.1)
> with KNY 2017's $H_{D_6}^{\mathrm{KNY}}$ above."

Verbatim quote (`phase_b_canonical_map.md` L125-126, 10 words):

> "$(\theta_0, \theta_\infty)_{\mathrm{Okamoto}} \leftrightarrow (a_1, a_2)_{\mathrm{KNY}}$
> $(\bmod \text{ convention shift})$"

### Q-A2: projected/transformed quantities?

**Answer: NO** as the *primary* output. The output of $M$ at the
parameter-space level is raw Hamiltonian per Q-A1. No ratio,
$D_6$-root projection, or homothety appears in the parameter slot
of the Section B.3 output description.

**Caveat:** there is a *Hamiltonian-coordinate* gauge transform on
$(q, p)$ inside Φ_symp (L121-127), but this acts on the phase-space
coordinates, not on the four parameter entries themselves. The
parameter four-tuple stays raw across the gauge.

### Q-A3: output-domain ambiguous?

**Answer: NO at the structural level; PARTIAL at the arithmetic level.**

058R B.3 pins the output-domain structurally as Okamoto/KNY
Hamiltonian-parameter space (L24-30, L99-114, L118-127). The
*explicit numerical conversion* of the V_quad input tuple
$(1/6, 0, 0, -1/2)$ into KNY $(a_0, a_1, a_2)$ is logged as
"residual R1 partially closed" at L138-141.

Verbatim quote (`phase_b_canonical_map.md` L138-141, 38 words):

> "(i) explicit conversion of the V_quad's CT v1.3 §3.5 4-tuple
> $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0) = (1/6, 0, 0, -1/2)$
> to KNY $(a_0, a_1, a_2)$ — this is residual R1 partially
> closed; the 4-tuple does NOT satisfy Okamoto's
> $\alpha_\infty + \alpha_0 + \beta_\infty + \beta_0 = 0$ constraint
> (sums to $-1/3$)"

The structural domain (raw Hamiltonian) is clear; only the explicit
numerical mapping arithmetic is open.

---

## Phase B findings (p12 sec:vquad)

### Q-B1: classical-ODE labeling?

**Answer: YES.** p12 sec:vquad uses unsubscripted
$(\alpha, \beta, \gamma, \delta)$ — the Painlevé-III standard
classical-ODE form notation per Okamoto eq. (0.1) / (1.1).

Cited line numbers (`p12_journal_main.tex`):

- **L975** — `\subsection{Painlev\'e III$(D_{6})$ parameters}`
- **L982-984** — the four-tuple labeling

Verbatim quote (`p12_journal_main.tex` L982-984, 13 words):

```latex
(\alpha, \beta, \gamma, \delta) \;=\;
\big(\tfrac{1}{6}, 0, 0, -\tfrac{1}{2}\big).
```

Verbatim quote (`p12_journal_main.tex` L985, 11 words):

> "These values are taken verbatim from~\cite[\S 2]{Papanokechi2026Vquad}."

A second occurrence of the same labeling appears in the Introduction
"Contributions" item at **L232-233**:

```latex
$(\alpha,\beta,\gamma,\delta) = (1/6, 0, 0, -1/2)$
```

Both p12 occurrences use the unsubscripted-Greek classical-ODE
notation.

### Q-B2: Hamiltonian-parameter labeling?

**Answer: NO** at p12 sec:vquad. The "Painlevé III$(D_6)$ parameters"
subsec at L975-985 carries no $(\eta, \theta)$ symbols and no
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ subscripted form.

(The Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$
notation appears at CT v1.3 §3.5 + 058R B.3 + 105 §3.5.1 — different
substrates — and creates a labeling-convention divergence with
sec:vquad. Surfaced as anomaly A-115-1 below.)

### Q-B3: projected/transformed labeling?

**Answer: NO.** sec:vquad attaches no projection / ratio / root-system
annotation to the tuple. The four entries appear as bare numerical
values inside the unsubscripted-Greek tuple.

### Q-B4: labeling-convention ambiguous?

**Answer: NO formally; YES across project documents.**

Within sec:vquad alone, the labeling reads classical-ODE per the
standard Painlevé-III convention. Read across project documents,
the same numerical tuple $(1/6, 0, 0, -1/2)$ carries TWO labels:

- p12 sec:vquad L982-984 + p12 Intro L232-233 + LIT dict L48: classical-ODE $(\alpha, \beta, \gamma, \delta)$.
- 058R B.3 L138-141 + CT v1.3 §3.5 + 105 §3.5.1 (3.5.1a)-(3.5.1d): Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$.

Surfaced as anomaly A-115-1.

### Q-B5: LIT dict source-string accurate vs sec:vquad?

**Answer: PARTIAL_AGREE.** The LIT dict labeling AGREES with sec:vquad's
labeling (both classical-ODE). The LIT dict *source-string subsec
attribution* MISATTRIBUTES the subsec name.

Cited line numbers (`vquad_p3d6_recovery.py`):

- **L48** — `"P_III_D6_params": "(alpha,beta,gamma,delta) = (1/6, 0, 0, -1/2)"` — labels classical-ODE.
- **L49-50** — `"source": ("p12_journal_main.tex sec:vquad subsec Stokes data, citing Papanokechi2026Vquad.")` — names "subsec Stokes data".

Verbatim quote (`vquad_p3d6_recovery.py` L48-50, 22 words):

```python
"P_III_D6_params": "(alpha,beta,gamma,delta) = (1/6, 0, 0, -1/2)",
"source": ("p12_journal_main.tex sec:vquad subsec Stokes data, "
           "citing Papanokechi2026Vquad."),
```

Cross-check against `p12_journal_main.tex`:

- The subsec "Stokes data" at L1046-1067 carries the Stokes constant
  $\Stokes \approx 0.43770528\ldots$, the branch point
  $\xi_0 = 2/\sqrt{3}$, and the branch exponent $-1/(3\sqrt{3})$
  — but does **not** carry the $(1/6, 0, 0, -1/2)$ four-tuple.
- The four-tuple sits at the subsec "Painlevé III$(D_6)$ parameters"
  L975-985.

**Conclusion on Q-B5:** the labeling-claim half of the source-string
matches sec:vquad (both classical-ODE → labeling agreement).
The subsec-attribution half misnames the subsec ("Stokes data"
vs "Painlevé III$(D_6)$ parameters"). HALT-107-5 not triggered;
LIT dict source-string subsec name flagged as anomaly A-115-2 for
follow-up edit.

---

## Verdict

**Bin: R1.**
**Confidence: MEDIUM-HIGH.**

### Reasoning narrative

The QD-5 task asks whether the canonical-form normalisation map
$M = \Phi_{\mathrm{symp}} \circ \Phi_{\mathrm{shift}} \circ \Phi_{\mathrm{resc}}$
constructed in 058R Section B.3 produces *raw* Hamiltonian parameters
of P_III(D_6) at its output (R1) or *projected / transformed* quantities
(R2).

Phase A reads 058R B.3 directly. The output domain is named at three
distinct levels of B.3 prose: the Okamoto §1.1 Hamiltonian
$H_{III}(q, p, t; \theta_0, \theta_\infty)$ is the canonical target
(L24-30); the KNY 2017 §8.5.17 Hamiltonian
$H_{D_6}^{\mathrm{KNY}}(q, p, t; a_1, a_2)$ is the equivalent Lax-pair
target (L99-114); Φ_symp is named as the canonical $(q, p)$-gauge
transform between them (L118-127). All three frame the output as
*raw* Hamiltonian parameters in $(q, p, t) \oplus$ parameter space.
No projection, ratio, or root-system map appears at the parameter
slot.

Phase B reads p12 sec:vquad. The (1/6, 0, 0, -1/2) four-tuple appears
at L982-984 under unsubscripted classical-ODE notation
$(\alpha, \beta, \gamma, \delta)$. p12 sec:vquad does NOT annotate
the tuple as a projection or transform.

Phase B also notes a labeling-convention divergence between p12
sec:vquad (classical-ODE) and 058R B.3 / CT v1.3 §3.5 / 105 §3.5.1
(Hamiltonian). This divergence does NOT change M's output domain
— M's output is anchored on 058R B.3, which uses the Hamiltonian
labeling per CT v1.3 §3.5. Surfaced as anomaly A-115-1 for
reconciliation.

The MEDIUM-HIGH (rather than HIGH) confidence reflects three
non-blocking caveats logged in the discrepancy / unexpected-finds
files: (a) 058R residual R1 leaves the explicit
$(1/6, 0, 0, -1/2) \to (a_0, a_1, a_2)_{\mathrm{KNY}}$ arithmetic
partially closed; (b) the V_quad input tuple violates the Okamoto
null-sum constraint (sums to $-1/3$, not 0) and places the fibre
at a parameter-degeneracy locus; (c) p12 sec:vquad's classical-ODE
notation creates the cross-document labeling divergence noted
above.

Verdict R2 has no support in 058R B.3 substrate. Verdict
R1+R2_BLEND has no support either (the four parameter entries
all live in the same Hamiltonian slot). Verdict UNDECIDABLE
would require the substrate to be silent on the structural
output domain, but B.3 is explicit at L24-30, L99-114, L118-127.
R1 is the verdict.

---

## Recommended Section 3.5.1 amendment scope

**R1, sub-form R1a (small).**

CT v1.3 §3.5.1 (105 deposit) declarations (3.5.1a)-(3.5.1d):

- $(3.5.1a)$ $\alpha_\infty := \eta_\infty$
- $(3.5.1b)$ $\alpha_0 := \eta_0$
- $(3.5.1c)$ $\beta_\infty := \theta_\infty$
- $(3.5.1d)$ $\beta_0 := \theta_0$

These declarations remain structurally right at the symbol-assignment
level: the rename moves V_quad-native CT v1.3 §3.5 names
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ onto Okamoto §1.1
Hamiltonian names $(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$.
058R B.3's reading of M's output as raw Hamiltonian aligns with
this rename.

The amendment scope is a SMALL caveat insertion to address the
$\eta_0 = 0$ admissibility issue at the V_quad parameter point
(Okamoto §1 standing assumption $\eta_\Delta \neq 0$ violated).
Specific edit:

> Insert a sentence after (3.5.1d) noting that at the V_quad image
> point $(\eta_\infty, \eta_0, \theta_\infty, \theta_0) = (1/6, 0, 0, -1/2)$
> the entry $\eta_0 = 0$ places the fibre at a degeneration locus
> of P_III(D_6) (the standing assumption $\eta_\Delta \neq 0$ from
> Okamoto §1 is at boundary). Forward-pointer to 058R B.3 residual R1
> partial closure (`phase_b_canonical_map.md` L138-141) and to the
> three candidate mechanisms (a) / (b) / (c) for the $-1/3$
> null-sum offset already named in the 105 deposit prose. Footnote
> the 069r2 QD-5 audit verdict (this prompt) for governance trail.

Estimated diff size: 3-6 lines of LaTeX prose + 1 footnote.

**QE re-bin recommendation: ROUTE_E_TRIVIAL retained.** The trivial
relabel framing of 105 §3.5.1 stands; the audit substrate gives no
support to a ROUTE_E_NONTRIVIAL_REQUIRED upgrade.

---

## Anomalies surfaced

### A-115-1 (PRIMARY) — labeling-convention divergence across project documents

The numerical tuple $(1/6, 0, 0, -1/2)$ carries TWO labels across
project artefacts:

| Substrate | File:line | Labeling |
|---|---|---|
| p12 Intro | `p12_journal_main.tex` L232-233 | classical-ODE $(\alpha, \beta, \gamma, \delta)$ |
| p12 sec:vquad | `p12_journal_main.tex` L982-984 | classical-ODE $(\alpha, \beta, \gamma, \delta)$ |
| LIT dict | `vquad_p3d6_recovery.py` L48 | classical-ODE $(\alpha, \beta, \gamma, \delta)$ |
| 058R B.3 | `phase_b_canonical_map.md` L138-141 | Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ |
| CT v1.3 §3.5 | (cited by 058R B.3) | Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ |
| CT v1.3 §3.5.1 (105 deposit) | `tex/submitted/section_3_5_1_okamoto_rename.tex` | Hamiltonian → Okamoto $(\eta, \theta)$ trivial relabel |

Three artefacts read classical-ODE, three read Hamiltonian. Under
classical-ODE reading, $\gamma = 0$ violates Okamoto §1 standing
assumption $\gamma \delta \neq 0$ for P_III(D_6) and would place
the fibre at a P_III(D_7) sector (not (D_6)). Under Hamiltonian
reading, $\eta_0 = 0$ violates $\eta_\Delta \neq 0$ and places
the fibre at an Okamoto-degeneration locus inside the (D_6) family.

**Recommended follow-up:** dedicated reconciliation prompt that
either (i) updates p12 sec:vquad + p12 Intro + LIT dict to
Hamiltonian notation for consistency with 058R / CT v1.3 / 105;
or (ii) adds an explicit cross-walk footnote at sec:vquad noting
that the unsubscripted-Greek notation is shorthand for
Hamiltonian $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$,
not classical-ODE.

This anomaly is **independent of QD-5 verdict R1**: Section 3.5.1's
amendment scope (R1 small caveat) does not depend on which
notation p12 sec:vquad ultimately uses.

### A-115-2 (SECONDARY) — LIT dict source-string subsec misattribution

`vquad_p3d6_recovery.py` L49-50 source-string names
"subsec Stokes data" but the (1/6, 0, 0, -1/2) labeling lives
in subsec "Painlevé III$(D_6)$ parameters" at p12_journal_main.tex
L975-985. The subsec "Stokes data" at L1046-1067 carries the
Stokes constant numerics (0.43770528...) and does not carry the
parameter four-tuple.

**Recommended follow-up:** small one-line edit to the recovery
script's LIT dict, pointing the source-string at
"subsec Painlevé III$(D_6)$ parameters" or simply
"sec:vquad" without the misattributed subsec qualifier.

### A-115-3 — Okamoto-degeneracy locus at V_quad image

Under either labeling reading, the V_quad tuple $(1/6, 0, 0, -1/2)$
lies at an Okamoto §1 standing-assumption boundary
($\gamma \delta = 0$ classical-ODE; or $\eta_\Delta = 0$
Hamiltonian). 058R B.3 L138-141 already logs the
$-1/3$ null-sum offset as discrepancy D2 carry-forward.

**Recommended follow-up:** the Section 3.5.1 R1a small caveat
sentence (above) is the immediate handling. A separate structural
prompt may diagnose whether V_quad genuinely sits at a
P_III(D_6) → P_III(D_7) degeneration limit (case for elevating
to a Sakai-classification refinement).

---

## Forward-pointers for downstream prompts

- **Prompt 108 scope:** `small` (R1a, ~3-6 LaTeX lines + 1 footnote).
- **Prompt 109 (069r3-B FW pull-back) parameter entry format:**
  Hamiltonian $(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$ per
  Okamoto §1.1 / 105 §3.5.1 trivial relabel. Per-coordinate
  $\geq 3$-digit cross-validation criterion (UF-113-3) at each
  of the four entries of $(1/6, 0, 0, -1/2)$.
- **Prompt 110 (069r3-D V_quad numerical) extraction target format:**
  same as Prompt 109 — Hamiltonian $(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$.

---

## AEAL claim count

7 entries written to `claims.jsonl` this audit.
