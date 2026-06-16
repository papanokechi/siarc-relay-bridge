# H-1 provenance remark — VERIFIED-AND-INSERTED

**STATUS: OPERATOR-VERIFIED (2026-06-16) AND INSERTED.** Operator confirmed claims (a),(b),(c),(e);
and (d) confirmed with refinement — the correction is the companion's *Version 1.1* Remark 6.2, and
record `20481592` is live-verified as companion v1.2 (concept `20455089`). The remark below was
inserted verbatim at `section-4.md` §4.3 (after the bridge sentence); both `\eqref{eq:bridge}` and
`\eqref{eq:C-from-A}` resolve. PDF rebuilt in Stage 4 (SHA `4CA12A35…`). See `build-result.md` and
`verification-pass.md`. The Stage-3 HALT gate is CLEARED.

---

## Why H-1 exists (the finding, restated)

The paper's headline value is `C = |Gamma(beta)|·K = 0.437705286193537221230739749794...`
(`section-1.md` eq:C-skeleton; `section-4.md` eq:constants). The cold-read flagged that these digits
are **numerically identical to the value once published, in the V_quad companion v1.0, as the
*Stokes constant* S** — a value later retracted and corrected to `S = 2*pi*K = 0.45790662316901763...`
in companion v1.1/v1.2. The paper's mathematics is correct and already states C != S and the exact
bridge `S/C = 2*pi/|Gamma(beta)|` (`section-1.md` eq:bridge; `section-4.md` L67-68). What it does
**not** do is warn a corpus-aware reader that `0.43770528...` is the *retracted-as-S* number, here
correctly wearing its true hat as `C`. H-1 adds that one-paragraph provenance note — which doubles as
a showcase of the paper's core contribution (the period framework is exactly what disambiguates the
two constants).

---

## Proposed remark text (LaTeX) — for `section-4.md` §4.3, after the bridge sentence (L68)

```latex
\begin{remark}[Provenance of the value $0.43770528\ldots$]\label{rmk:provenance-C}
A reader familiar with the $\Vquad$ corpus will recognise the digits
$\C=\lvert\Gamma(\beta)\rvert K=0.437705286\ldots$ as numerically identical to a value once
reported---in the first companion version (v1.0)---as the Stokes constant $S$. That identification
was an error of prefactor: the companion was subsequently corrected to $S=2\pi K=0.457906623\ldots$
in v1.1/v1.2~\cite{StokesNote}. The present period representation explains the coincidence rather
than repeating it. The factor $\lvert\Gamma(\beta)\rvert$ is the \emph{correct} prefactor for the
connection coefficient $\C$---it is the branch $\Gamma$-factor manufactured by the Hankel loop,
\eqref{eq:C-from-A}---whereas $2\pi$ is the prefactor for the Stokes constant $S$; the two are tied
by the exact bridge $S/\C=2\pi/\lvert\Gamma(\beta)\rvert$~\eqref{eq:bridge} and are genuinely
distinct constants. In other words, the quantity $\lvert\Gamma(\beta)\rvert K$ is the right number
for $\C$, and the v1.0 slip was precisely that this contribution was made to do double duty and
mislabelled as $S$.
\end{remark}
```

(Alternative, lighter-weight placement: a footnote attached to `eq:bridge` in `section-1.md`
carrying the same three points. The §4.3 remark is preferred because both numerical values appear
there at full precision, side by side, which is exactly where a knowledgeable reader meets the
collision.)

---

## Agent reconstruction of the C-vs-S history  [LABEL: RECONSTRUCTION — operator must verify]

Sourced to (i) this paper and (ii) session memory; **explicitly NOT asserted as established fact**:

- From the paper (exact, in-document):
  - `C = |Gamma(beta)|·K`, eq:C-from-A / eq:constants; `S = 2*pi*K`; bridge `S/C = 2*pi/|Gamma(beta)|`,
    residual 0. `|Gamma(beta)| = 6.00599...`, `K = 0.0728781025518669641294...`,
    `beta = -1/(3*sqrt3)`.
  - Numerically: `C = 0.437705286193537...`, `S = 0.457906623169018...`. Distinct.
- From memory (stored facts on the V_quad Stokes constant; corroborating, to be confirmed):
  - "v1.0/repo scripts wrongly used prefactor Gamma(beta_exp) = -6.00599 giving retracted
    0.43770528"; "Painlevé-V paper v1.1 correction (prefactor 2*pi vs Gamma(beta_exp))";
    "2*pi prefactor -> 0.4579066231690176361190978, matches v1.1".
  - I.e. v1.0 wrote `|Gamma(beta)|·K` and labelled it `S`; v1.1/v1.2 corrected the *label/prefactor*
    so that `S = 2*pi*K`. The number `|Gamma(beta)|·K` itself is not wrong — it is `C`.

This reconstruction is internally consistent (|Gamma(beta)| = 6.00599 is exactly the "wrong
prefactor" memory cites; the corrected S uses 2*pi), but the *history* (what v1.0 said, when the fix
landed) is a provenance claim about prior deposits, so it is gated on operator confirmation.

---

## FIVE factual claims the operator MUST confirm (or correct) before Stage 4

- **(a)** `C` and `S` are **distinct** quantities: `C = |Gamma(beta)|·K = 0.43770528...`,
  `S = 2*pi*K = 0.45790662...`.
- **(b)** `|Gamma(beta)|` is the **correct** prefactor for the connection coefficient `C`.
- **(c)** The v1.0 companion error was **`|Gamma(beta)|` used where `2*pi` belonged** — i.e. the
  product `|Gamma(beta)|·K` was mislabelled as the Stokes constant `S`.
- **(d)** The correction landed in companion **v1.1/v1.2** (`S = 2*pi*K`), cite `\cite{StokesNote}`
  = Zenodo `10.5281/zenodo.20481592`.
- **(e)** `0.43770528... = |Gamma(beta)|·K` is **correct as `C`** (this paper's result), even though
  it was wrong as `S`.

If the operator corrects any of (a)–(e), the remark text above is revised to match the operator's
account **before** insertion.

---

## What Stage 4 will do (post-confirmation only)
1. Insert the (possibly operator-revised) remark at `section-4.md` §4.3 after L68.
2. `python build.py` (pdflatex ×2, SOURCE_DATE_EPOCH set, preamble guards) → new `.tex` + `.pdf`.
3. Compute the corrections-final PDF SHA-256 (supersedes `359d1172…`); confirm reproducibility from a
   pristine temp dir.
4. Wrong-venue check on the final PDF ("Compositio" and other target-venue strings absent).
5. Stage-5 constant re-verification (mpmath): S, C, bridge unchanged.
