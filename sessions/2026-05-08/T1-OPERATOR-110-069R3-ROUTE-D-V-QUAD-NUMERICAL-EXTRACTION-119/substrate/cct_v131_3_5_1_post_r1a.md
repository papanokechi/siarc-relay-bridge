# Substrate A.4 — CT v1.3.1 §3.5.1 + 117 R1a caveat block

**Source:** `pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex` lines 968–1010.
**Live SHA-256 (Get-FileHash inspected at 110 fire time, G2 PASS):** `1894477036FB6332A18979F7A7204FE0BBC43AB22A6A441A11FBB2FAD5BC9BBA` (80193 B / 1668 LC).
**Loaded for:** prompt 110 Phase A.4 (relay envelope SECTION 3 A.4).

---

## §3.5.1 four displayed equations (3.5.1a)–(3.5.1d) — VERBATIM

```latex
\noindent\textbf{Definition (project rename, trivial form).}
For v1.3 the 4-tuple
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$ is declared
in terms of the Okamoto Hamiltonian parameters
$(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$ by the
trivial relabel
\begin{align}
  \alpha_\infty   &:= \eta_\infty,            (3.5.1a)
  \alpha_0        &:= \eta_0,                 (3.5.1b)
  \beta_\infty    &:= \theta_\infty,          (3.5.1c)
  \beta_0         &:= \theta_0.               (3.5.1d)
\end{align}
Equations (3.5.1a)–(3.5.1d) carry no additive shift;
the v1.3 rename is a pure symbol substitution.
```

(line range 968–982; quote ≤ 50 words per stanza.)

## Standing-assumption boundary at V_quad image

```
α_0 = η_0 = 0  →  fibre at boundary of Okamoto §1 standing
                  assumption η_Δ ≠ 0 for canonical H_III form.
```
(p12 L988–994 in CT v1.3.1; UF-115-3 Okamoto-degeneracy flag.)

## 117 R1a caveat block — VERBATIM (post-108a-EXEC insertion at L987–L1010)

(line range L987–1010; ≤ 50 words per quote block per envelope sect. 5.E.2.)

> *"The −1/3 null-sum offset at the V_quad parameter point. Under (3.5.1a)–(3.5.1d) the V_quad image yields the partial sum α_∞ + α_0 + β_∞ + β_0 = 1/6 + 0 + 0 + (-1/2) = -1/3."*

> *"This differs by -1/3 from the FW null-sum constraint v_1 + v_2 + v_3 + v_4 = 0 (FW §2.1 eq. (2.2)) when applied to the project 4-tuple. The 058R canonical-map record anchors the -1/3 value at the V_quad parameter point."*

> *"Three candidate mechanisms account for the offset: (a) Hamiltonian-expansion residual via FW 2002 Prop 4.1 / eq. (4.3): h = t H + (1/4) v_1² − (1/2) t."*

> *"(b) Additive-shift component of the rename. (c) Sakai surface-type artefact gated to Route F D_6^{(1)} machinery."*

## QD-5 audit footnote (CT v1.3.1 L989–998)

```latex
\footnote{The QD-5 audit verdict at bridge session
T2-OPERATOR-QD5-AUDIT-058R-B3-P12-VQUAD-115 reads
the canonical-form normalisation map's output as raw
Okamoto/KNY parameters
$(\eta_\infty, \eta_0, \theta_\infty, \theta_0)$, with
(3.5.1a)–(3.5.1d) the small-amendment R1a item.}
```

## Wording shifts vs pre-108a-EXEC (CT v1.3 → v1.3.1)

Pre-108a-EXEC (CT v1.3, SHA `64FA0577..C7424E615B0756D339FEADC6ECEDE953AED`):
- §3.5.1 prose ended at L984 (close of -1/3 null-sum offset paragraph).
- No QD-5 audit footnote.
- No "Standing-assumption boundary" sub-block.

Post-108a-EXEC (CT v1.3.1, SHA `1894477036FB6332A18979F7A7204FE0BBC43AB22A6A441A11FBB2FAD5BC9BBA`):
- §3.5.1 extended +23 LC / +1105 B.
- Added "Standing-assumption boundary at the V_quad image" paragraph (L984–L988).
- Added QD-5 audit footnote (L989–L998).
- (3.5.1a)–(3.5.1d) trivial-relabel preserved unchanged.

## Implication for 110 Phase D inversion

The trivial-relabel form (3.5.1a)–(3.5.1d) implies the Hamiltonian-side
extraction `(η_∞, η_0, θ_∞, θ_0)` is computationally identical to the
classical-ODE-side `(α_∞, α_0, β_∞, β_0)` at the V_quad parameter point;
no additive shift has to be inverted.

The −1/3 partial-sum is recorded as STRUCTURAL feature (V_quad image
Okamoto-degenerate at η_0 = 0) NOT a labeling artifact under the
v1.3.1 trivial-relabel reading.

The labeling-convention divergence anomaly A-115-1 (3 artefacts label
classical-ODE: p12 sec:vquad + p12 Intro + LIT dict; 3 artefacts label
Hamiltonian: 058R B.3 + CT v1.3.1 §3.5 + 105 §3.5.1) remains an OPEN
ANOMALY in the project record — it is NOT closed by 117's R1a small
amendment, which only ADDED the boundary-degeneracy caveat.
