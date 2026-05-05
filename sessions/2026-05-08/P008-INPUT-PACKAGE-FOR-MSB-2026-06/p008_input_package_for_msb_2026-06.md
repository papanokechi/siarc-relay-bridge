# P-008 Input Package for Strategyzer Monthly Cycle 2026-06
## Compiled: 2026-05-05T12:39:28.191955+00:00
## Compiler: CLI-Tactical-Executer (relay 045, sweep 044 in flight)
## Authority for use: Strategyzer (Tier 1, monthly cadence)
## RACI anchor: v2026-05-08 (bridge commit 177bfd7, RACI-V2026-05-08-INSTALL re-fire)

## §0  rule5 grounding evidence (captured 2026-05-05T12:39:29.020068+00:00)

- CMB header: FOUND mtime_utc=2026-05-05T11:20:28.318074+00:00 sha256=b89a1c1b6aab2a49286e44216535febd93c0b3dda9d3b41ecbd900335fe656ed
- cli_log/2026-05-05.md: FOUND mtime_utc=2026-05-05T11:20:28.306641+00:00 sha256=6fd1a1a14c9f13bd415a19056d2dbfb1a5e6ee0e4bf3f08d0af14db4ba0fa672
- Bridge 30-day file count: 2667 files modified in last 30 days
- Status: **COMPLETE**

CMB header content (first 4 lines, verbatim):
```
['# SIARC MORNING BRIEFING', '## Claude Morning Briefing — CMD.txt', '## Last updated: 2026-05-04', '## Goal: ONE ACCEPTED PAPER']
```


## §1  Substrate manifest

| ID | Label | Path | Size (B) | SHA-256 (16) | Status |
|----|-------|------|----------|--------------|--------|
| S1 | umbrella v2.0 §4 (Phi-triple) source | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\umbrella_program_paper\main.tex` | 44935 | `612f732ebe2d8bab` | FOUND |
| S2 | Channel Theory v1.3 §Implications source | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\pcf-research\channel\cc_pipeline_v13_2026-05-02\channel_theory_outline.tex` | 70178 | `59c5352795f8d63d` | FOUND |
| S3 | M9 main-theorem dependency audit verdict (commit 4ffcc8c) | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-05\M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT\handoff.md` | 21099 | `4c8c9c22570591cc` | FOUND |
| S4 | T2B v3.1 bipartition framing (commit 5d83797) | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\siarc-relay-bridge\sessions\2026-05-07\PCF-2-V2-BIPARTITION-PROMOTION\t2b_paper_v3.1_bipartition_promotion.tex` | 33762 | `538b897c75908c9e` | FOUND |
| S5 | Working main-theorem statement (if any) | `n/a` | n/a | `n/a` | NOT_FOUND |
| S6 | M6 ✅-vs-Phase-A/B.5 inconsistency status | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\CMB.txt` | 69288 | `b89a1c1b6aab2a49` | FOUND |
| S7 | Departing-Synthesizer's three standing notes (Strategyzer→CLI handoff §E) | `C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\control center\synthesizer_inbox\STRATEGYZER_HANDOFF_2026-05-08.md` | 12323 | `f6fc35af0f7ebfeb` | FOUND |

## §2  Umbrella v2.0 §4 Cross-Degree Framing: the Invariant Triple (verbatim)

```latex
\section{Cross-Degree Framing: the Invariant Triple}
\label{sec:triple}

This section is new in v2.0. It records the cross-degree
organisational principle that emerged from the SIARC stack between
April and May 2026. \emph{No new theorems are stated here}; every
quantitative claim is either empirical (with citation to the responsible
companion paper's session deliverables) or conjectural.

\subsection{Definitions}
\label{sec:triple-defs}

Throughout this section, fix a PCF family of the form
$\PCF(1, b) = 1/(b_1 + 1/(b_2 + \cdots))$ with $b_n = b(n)$ for a fixed
polynomial $b \in \Q[x]$ of degree $d$. Write
$b(x) = \beta_d x^d + \beta_{d-1} x^{d-1} + \cdots + \beta_0$.

\begin{definition}[Discriminant axis]
\label{def:disc-axis}
The \emph{discriminant} of $b$ is $\Delta_d(b) := \mathrm{disc}(b)$, the
ordinary polynomial discriminant of the squarefree-part-stripped
denominator polynomial. By convention $\Delta_d(b) \in \Q^\times$ when
$b$ is squarefree, and the sign $\mathrm{sgn}(\Delta_d) \in \{\pm 1\}$
is the discrete invariant on which PCF-1 v1.3 stratifies the sharp
WKB exponent at $d=2$.
\end{definition}

\begin{definition}[Modular-discriminant axis]
\label{def:moddisc-axis}
For $d=3$ with $b$ irreducible non-singular, the curve $E_b: y^2 = b(x)$
is an elliptic curve over $\Q$; let $\tau_b \in \HH/\mathrm{SL}_2(\Z)$
be its period in the standard fundamental domain. The
\emph{Petersson-normalised modular discriminant} at $\tau_b$ is
\begin{equation}
  \label{eq:petersson-norm}
  \PetN{\Delta}(\tau_b) \;:=\; |\Delta(\tau_b)| \cdot (\mathrm{Im}\,\tau_b)^{6},
\end{equation}
where $\Delta(\tau) = (2\pi)^{12} \eta(\tau)^{24}$ is the modular
discriminant cusp form of weight $12$. For general $d \geq 3$ the
analogous construction uses the period of the hyperelliptic curve
$y^2 = b(x)$ on the corresponding period domain; we restrict the
quantitative claims of this section to $d=3$.
\end{definition}

\begin{definition}[Borel-radius axis]
\label{def:borel-axis}
The \emph{Borel radius} of the PCF asymptotic series associated to
$\PCF(1,b)$ is
\begin{equation}
  \label{eq:borel-radius}
  \xi_0(b) \;:=\; \frac{d}{\beta_d^{1/d}},
\end{equation}
the Newton-polygon root extracted from the dominant balance of the
characteristic equation of the three-term recurrence at infinity
(\cite{PCF2}, Q1-B Proposition; \cite{CT}, V$_{\mathrm{quad}}$
recovery).
\end{definition}

The map
\begin{equation}
  \label{eq:Phi-functor}
  \Phi : \PCF(1,b) \;\longmapsto\; \bigl(\Delta_d(b),\ \PetN{\Delta}(\tau_b),\ \xi_0(b)\bigr)
\end{equation}
is the \emph{bridge functor} of v2.0; the rest of this section reviews
what each axis carries.

\subsection{The discriminant axis \texorpdfstring{$\Delta_d$}{Delta\_d}}
\label{sec:triple-disc}

At $d=2$, PCF-1 v1.3 Theorem~5 establishes the sharp WKB exponent
identity for $\PCF(1,b)$ with $\deg b = 2$, with the exponent split by
$\mathrm{sgn}(\Delta_2)$: $A = 4$ for $\Delta_2 > 0$ and $A = 3$ for
$\Delta_2 < 0$ (six $\Delta_2 < 0$ families verified at $\geq 200$
digits; see PCF-1 v1.3 \cite{PCF1}). At $d \geq 3$, PCF-2 v1.3
\cite{PCF2} verifies the unsplit \emph{sharp} Conjecture B4
\begin{equation}
  \label{eq:b4-conjecture}
  \log|\delta_n| \;\sim\; -A\, n \log n + \alpha\, n - \beta \log n + \gamma,
  \qquad A = 2d
\end{equation}
on the joint $d \in \{3,4\}$ catalogue (110/110 families at the
relevant tail-window precision). The strong-form upgrade
\textsf{op:b4-degree-d} (\S\ref{sec:open}, \textsf{prob:b4-allD})
extends $A = 2d$ to all $d$ via the Birkhoff--Trjitzinsky
asymptotic theory of irregular linear difference equations
\cite{Birkhoff1930,BirkhoffTrjitzinsky1933}; this remains open and is
the gating move toward the \emph{SIARC Master Conjecture v0}
(MASTER-V0, \S\ref{sec:companions}).

\subsection{The modular-discriminant axis \texorpdfstring{$\PetN{\Delta}$}{Pet-norm Delta}}
\label{sec:triple-moddisc}

The defining empirical content of v2.0 is the post-T2 finding
(\cite{PCF2}, Session T2; bridge mirror at
\href{https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-02/PCF2-SESSION-T2/}{PCF2-SESSION-T2})
that, on the deep R1.3 cubic catalogue ($n=50$ cubic families,
$\mathrm{dps} = 4000$, $N_{\max} = 480$), the Petersson-normalised
modular discriminant correlates with the residual $\delta = A_{\mathrm{fit}} - 6$
with Spearman
\[
   \rho\bigl(\log \PetN{\Delta}(\tau_b),\ \delta_{\mathrm{deep}}\bigr)
       \;=\; +0.638,
   \qquad p_{\mathrm{Bonf}}(K{=}14) \;=\; 8.6 \times 10^{-6},
\]
\emph{beating} the bare-$\log|j|$ baseline
$\rho = -0.568,\ p_{\mathrm{Bonf}} = 2.34 \times 10^{-4}$ by a factor of
\(\sim 30\) in Bonferroni $p$. Bare $\log|E_4(\tau_b)|$ alone
\emph{underperforms} $\log|j|$ ($\rho = -0.459$,
$p_{\mathrm{Bonf}} = 1.12 \times 10^{-2}$). This pattern is exactly the
prediction of Fleet-A H2: the local mechanism at the equianharmonic
($j=0$) cell is the simple zero $E_4(\rho)=0$, so $\log|E_4|$ is locally
pinned while $\log\PetN{\Delta} = 6 \log\mathrm{Im}\,\tau + \log|\Delta|$
remains well-conditioned globally via the modular identity
$1728\,\Delta = E_4^3 - E_6^2$. Compactly:

\begin{conjecture}[Cubic-modular split, $d=3$]
\label{conj:b5-b6-d3}
For $\PCF(1,b)$ with $b \in \Q[x]$ irreducible non-singular cubic:
\begin{itemize}[leftmargin=2em]
  \item \textbf{B5 ($d=3$ form):} $j(E_b) = 0$ implies
    $A_{\mathrm{PCF}}(b) = 2d = 6$ exactly, with subleading
    amplitude conjecturally in the Chowla--Selberg
    $\Gamma(1/3)$ basis \cite{ChowlaSelberg1967}.
  \item \textbf{B6 ($d=3$ form):}
    $\rho_{\mathrm{Spearman}}\bigl(\log\PetN{\Delta}(\tau_b),
    A_{\mathrm{fit}}(b) - 6\bigr) > 0$ on the $n=50$ cubic catalogue,
    with $p_{\mathrm{Bonf}} \leq 10^{-5}$ at $K=14$.
\end{itemize}
\end{conjecture}

The d=3 restriction is the verdict of Session R1.3
(\href{https://github.com/papanokechi/siarc-relay-bridge/tree/main/sessions/2026-05-01/PCF2-SESSION-R1.3/}{PCF2-SESSION-R1.3},
\textsf{CASE B with C-caveat}): the deep-WKB null at $d=4$
(family 32 deep $\delta = -4.55\times 10^{-4}$ vs family 1 baseline
deep $\delta = -4.60\times 10^{-4}$, $|\mathrm{diff}|$ at $0.24$
pooled stderr units) shows that the sharp/deep-WKB form of B5/B6 is
$d=3$-specific. A residual shallow-N $j=0$-cell shift at $d=4$
exists but does not survive to deep-N; this is logged as
\textsf{op:shallow-j-effect-d4} (\S\ref{sec:open}). The Phase~D
finite-$N$ tail-window artefact at the four $j=0$ cubic families
($|\delta| \sim 1.5\times 10^{-5}$, shrinking $\geq 50\times$ from
the R1.1 $N \leq 67$ window to the T2-D $N \leq 480$ window) is the
content of \textsf{op:j-zero-amplitude-h6}: a closed-form
Chowla--Selberg amplitude is conjectured but requires a redesigned
five-parameter WKB ansatz to extract.

\subsection{The Borel-radius axis \texorpdfstring{$\xi_0$}{xi\_0}}
\label{sec:triple-borel}

The identity $\xi_0(b) = d/\beta_d^{1/d}$ is the master Newton-polygon
characteristic-root identity (PCF-2 v1.3 Q1-B Proposition; \cite{PCF2}).
At $d=4$ it is verified to spread $0$ across $8$ Q1 representatives;
at $d=3$ it is the same identity used in PCF-1 v1.3's exponent split.
The Channel Theory companion (\cite{CT}, V$_{\mathrm{quad}}$ recovery)
extends this to a functor on the Borel plane: the V$_{\mathrm{quad}}$
CC-channel branch-point structure is recovered to $200$ digits via
Newton-polygon $+$ Birkhoff--Trjitzinsky resurgence, and Fleet-A H4
confirms that median resurgence delivers $\geq 30$-digit accuracy on
the V$_{\mathrm{quad}}$ stratum. The extension of median resurgence
beyond V$_{\mathrm{quad}}$ to the cubic CC channels is open
(\textsf{prob:median-resurgence-extension}).

\subsection{The \texorpdfstring{$E/P_k/B$}{E / P\_k / B} cell decomposition}
\label{sec:triple-cells}

The triple $(\Delta_d, \PetN{\Delta}, \xi_0)$ partitions PCF families
into three structural cells:
\begin{itemize}[leftmargin=2em]
  \item \textbf{Cell $E$ (generic / elliptic):} $\Delta_d \neq 0$,
        $\PetN{\Delta}(\tau_b)$ generic, $\xi_0$ on the principal
        Newton-polygon branch. The bulk of the cubic catalogue lives
        here.
  \item \textbf{Cell $P_k$ (Painlev\'e reduction at level $k$):}
        $\xi_0$ degenerates to a Painlev\'e-VI special-parameter
        substratum at level $k$, in the sense of P08
        \cite{P08}. The $D=2$ Painlev\'e reduction at degree pair
        $(2,1)$ is the historical entry point; higher $k$ is open
        (\textsf{prob:Pk-cells-structure}; Fleet-A H3 status:
        \textsf{D=2\_REDUCTION\_AMBIGUOUS}).
  \item \textbf{Cell $B$ (Borel-channel-anomalous):} the
        V$_{\mathrm{quad}}$ stratum and its conjectural
        cubic-CC-channel extensions; characterised by the channel
        functor $\chi$ of \cite{CT}.
\end{itemize}

The bridge functor $\Phi$ of \eqref{eq:Phi-functor} factors through
the channel functor $\chi$ in a way conjectured to be compatible with
the cell decomposition (\textsf{op:chi-Phi-compatibility};
\textsf{prob:Pk-cells-structure}). A worked example pairing $\chi$
and $\Phi$ on a single $E$-cell representative is deferred to D2-NOTE
(\S\ref{sec:companions}); v2.0 only fixes the notation.
```

## §3  Channel Theory v1.3 §Implications for the Master Conjecture (verbatim)

```latex
\section{Implications for the Master Conjecture}
\label{sec:implications}

A rigorous announcement of the Master Conjecture requires:
\begin{enumerate}
\item Pipeline closure for the five non-$\Vquad$ families
(\textsf{op:cc-monodromy-RH}). \Cref{prop:xi0,tab:cc-channel-v2}
provide the formal-solution data for all six families;
the missing piece is the full Stokes-matrix datum.
\item No-go proof or refutation (\textsf{op:no-go-proof})
of \Cref{conj:nogo}.
\item Bridge identity tier discrimination
(\textsf{op:bridge-witness-tier}) for at least one family
beyond $\Vquad$.
\item Cubic extension along
\cite{siarc_pcf2_v11, siarc_pcf2_program}
(\textsf{op:xi0-degree-d}).
\end{enumerate}

% =====================================================================
```

## §4  M9 main-theorem dependency audit verdict (commit 4ffcc8c, 2026-05-05)

### §4.A Verdict (verbatim)

```markdown
## Verdict (operator escalation gate)

**Primary verdict:** `INDETERMINATE_NO_FORMAL_STATEMENT`

**One-sentence summary:** No formal `Theorem`/`Conjecture` environment for
the SIARC Master Conjecture v0 (Phi) exists in any TeX source on disk or on
Zenodo; the umbrella v2.0 companion table records MASTER-V0 explicitly as
"Planned (post-T1 / Birkhoff--Trjitzinsky)", so the dependency question
cannot be answered against a statement-of-record because no such statement
yet exists.

**Secondary observation (non-speculative; pre-rendering only):** every
schema-level fragment that does exist in workspace (umbrella v2.0
`eq:Phi-functor`, picture v1.18 M9 block, Channel Theory v1.3
§"Implications for the Master Conjecture") references Stokes data only
through type-(b) structural-existence language ("Stokes-matrix datum",
"channel functor", "monodromy data") — never invoking closed-form S_2 by
symbol or by value. This supports an *expected* `NO_DEPENDENCY` /
`SOFT_DEPENDENCY` resolution once P-008 produces a draft Phi statement,
but is recorded here only as observation, not verdict, per Step 4.4 of
the spec.

**Recommended next action:** retry the audit after P-008 produces a draft
Phi statement; until then, P-009 caveat-language drafting should proceed
on the working assumption that closed-form S_2 is *not* a gating
condition (justified by all four schema-level fragments and by the v1.15
gating amendment {M4, M6} which excludes M8b unconditionally).

---
```

### §4.B Step 1 statement-of-record (verbatim)

```markdown
## Step 1 — Statement-of-record

Per the precedence rule (umbrella formal Theorem/Conjecture env →
PCF-1/CT/PCF-2 → picture schema → Zenodo description → NONE):

- **Rule 1 (formal Theorem env):** FAILS. No `\begin{theorem}` or
  `\begin{conjecture}` environment in `umbrella_program_paper/main.tex`
  is labelled "Master Conjecture v0", "MASTER-V0", or "Phi". The
  closest is `Conjecture[Cubic-modular split, $d=3$]` (`conj:b5-b6-d3`,
  L327–339) which is a downstream conjecture about the
  `‖Δ‖_Pet`-axis, not the Phi master statement; and
  `Problem[Compatibility of $\chi$ and $\Phi$]`
  (`prob:chi-Phi-compatibility`, L759–763) which is an open-problem
  entry, not a theorem.
- **Rule 2 (PCF-1/CT/PCF-2 master classification):** FAILS for PCF-1
  v1.3 (only Logarithmic Ladder + Casoratian) and PCF-2 v1.3 (0 hits);
  CT v1.3 §"Implications for the Master Conjecture" only **discusses
  preconditions for** a future announcement, not the announcement
  itself.
- **Rule 3 (picture v1.18 schema):** treated as SCHEMA per spec —
  not a formal theorem. Verbatim L973–975: *"M9: SIARC-MASTER-V0
  announcement — Phi formally stated and the master classification
  result conditional on P-NP + P-B4 + P-CC"*.
- **Rule 4 (Zenodo umbrella v2.0 description):** Phi triple-invariant
  schema only. No formal statement of MASTER-V0; the description
  itself says "v2.0 is the substrate that the program-level publication
  ladder (D1 results paper, D2-NOTE, MASTER-V0, D7-AEAL methodology)
  rests on; it is intended to be cited as '[SIARC v2.0, §X]' by
  downstream papers" — i.e. Phi is the *substrate* on which MASTER-V0
  will be stated.
- **Rule 5 (NONE):** TRIGGERED → verdict `INDETERMINATE_NO_FORMAL_STATEMENT`.
```

### §4.C Step 4 verdict + provisional caveat (verbatim)

```markdown
## Step 4 — Verdict + caveat-language recommendation

### 4.1 Verdict label

`INDETERMINATE_NO_FORMAL_STATEMENT`

### 4.4 Recommendation (per Step 4.4)

Retry this audit after synthesizer P-008 produces a draft Phi statement
in formal text (Theorem / Conjecture environment). Until then, P-009
M8b positioning should NOT speculate on the dependency direction.
However, P-009 may safely use the following **provisional caveat**
template, conditional on the eventual draft Phi statement remaining
within the schema-level fragments audited here (i.e. confined to the
triple-invariant Phi of umbrella v2.0 §4 and the structural Stokes-data
language of CT v1.3 §"Implications"):

> **Provisional caveat (use only if P-008 draft remains within current
> schema; otherwise re-audit):** "Stokes-multiplier discrimination
> (companion milestone M8b) supplies an additional structural axis on
> which the master classification of Φ refines; current numerical
> paths to the second Stokes constant S_2 for the d=2 PCF Painlevé-III
> dichotomy are foreclosed at laptop-feasible precision (cf. SIARC
> bridge sessions T37M, 017c, 017e, 2026-05-03), and a literature-
> direct closed-form expression is not currently available (cf. Costin
> 2008 Theorem 5.26 = first Stokes constant only; Barhoumi--Lisovyy--
> Miller--Prokhorov 2024 = Riemann–Hilbert structural characterisation
> of monodromy data). The classification result of Φ does not depend
> on a closed-form value of S_2; M8b is enrichment, not gate."

Three style notes for synthesizer:

- The phrase *"does not depend on a closed-form value of S_2"* should
  be retained verbatim only if P-008 confirms that no clause in the
  draft Phi statement invokes S_2 by closed-form value. If any such
  invocation appears, the audit must be rerun and the caveat replaced.
- The phrase *"M8b is enrichment, not gate"* aligns with the picture
  v1.18 v1.15 amendment ("M9 gating reduces from {M2, M4, M6} to {M4,
  M6} UNCONDITIONALLY", L981–983) and is true at picture-schema level.
- The caveat avoids the forbidden AEAL verbs (per H6: "shows",
  "confirms", "proves" applied to a non-closed milestone). It does
  use "supplies" and "refines" in conjecture-context, which are
  permitted.

If the schema *does* shift under P-008 drafting (e.g. the Phi statement
acquires an explicit clause like "Phi(b) carries a Stokes-data
component whose closed-form value distinguishes Δ_b > 0 from Δ_b <
0"), this audit should be reopened immediately; that would re-trigger
HARD_DEPENDENCY and re-gate M9 to {M4, M6, M8b}.
```

### §4.D Recommended next step (verbatim)

```markdown
## Recommended next step

1. Synthesizer fires P-008 (M9 V0 announcement draft, Sakai-1999
   template) using the umbrella v2.0 §4 Phi triple as substrate and
   the four CT v1.3 §"Implications" preconditions as the
   announcement's caveat backbone.
2. Once P-008 produces a formal `\begin{conjecture}[SIARC Master
   Conjecture v0]` environment, this audit is rerun in a single relay
   pass against the new statement-of-record. Expected re-verdict:
   SOFT_DEPENDENCY (if Stokes-data clause uses CT v1.3 phrasing) or
   NO_DEPENDENCY (if Phi clause stays at the triple-invariant level).
3. P-009 (M8b positioning) may use the provisional caveat above as a
   parsed starting point, with the explicit understanding that it is
   contingent on the P-008 draft remaining within the audited schema.
```

## §5  T2B v3.1 bipartition framing (commit 5d83797): abstract + introduction (verbatim)

### §5.A Abstract (verbatim)

```latex
\begin{abstract}

We study integer polynomial continued fractions (PCFs) of degree $(2,1)$ — quadratic numerator, linear denominator — and their \emph{Trans-stratum}: the convergent, generic-irrational subclass identified by exhaustive search in the SIARC programme. We show that the Trans-stratum partitions cleanly into exactly two arithmetic classes, distinguished by the value of the structural ratio $a_2/b_1^2$ and by the spectral type of the underlying Birkhoff--Trjitzinsky (BT) characteristic equation $\lambda^2 - b_1\lambda - a_2 = 0$. \emph{Class A} ($a_2/b_1^2 = -2/9$) corresponds to the integer-resonance locus $\lambda_+ /\lambda_- = 2$, supports a generic Stokes phenomenon (Stokes multiplier $S_{12}\ne 0$ on the locus), and yields generic transcendental limits; $\sim\!1.5\times 10^5$ such families are observed and account for all transcendental Trans-stratum data. \emph{Class B} ($a_2/b_1^2 = +1/4$) has irrational characteristic ratio $\lambda_+/\lambda_- = 3+2\sqrt{2}$, no Stokes obstruction, half-integer hypergeometric parameters, and limits in $\mathbb{Q}(\pi)$; we exhibit $16$ minimal Brouncker-shape such families (saturation is open; see Remark~\ref{rem:classB-saturation}) and prove (Theorem~3) that every Pure-regime member is the Stieltjes/Wallis transform of the canonical Gauss continued fraction for $4/\pi$. We give a complete proof of the resonance-family theorem (Theorem~1) and a Stokes-theoretic conditional theorem (Theorem~2) characterising Class~A. A sweep of $134{,}040$ candidates at the next BT integer-resonance locus $a_2/b_1^2 = -3/16$ produced zero Trans-stratum families, confirming a complete desert at $k=3$. Three independent stratum-aware verification sweeps at $b_1 \in \{5, 6, 7\}$ are consistent with the bipartition: at $b_1 = 5$ both loci are predicted empty (since $9 \nmid 25$ and $2 \nmid 5$); at $b_1 = 6$, four Trans-stratum hits land on exactly the predicted loci (three on Class~A at $a_2 = -8$, one on Class~B at $a_2 = 9$); and at $b_1 = 7$ a coprime-to-both null sweep of $79{,}860$ candidates returns zero Trans-stratum hits (since $9 \nmid 49$ and $4 \nmid 49$ block both loci simultaneously). These observations support our \emph{Completeness Conjecture}: the degree-$(2,1)$ Trans-stratum is exhausted by Class~A and Class~B.
\end{abstract}
```

### §5.B Introduction (verbatim)

```latex
\section{Introduction}\label{sec:intro}

The arithmetic of polynomial continued fractions (PCFs) has roots in Brouncker's $4/\pi$, Wallis's product, Gauss's hypergeometric continued fraction \cite{gauss1813}, and Stieltjes' analytic theory of continued fractions \cite{stieltjes1894}. Modern computational searches in the SIARC programme \cite{siarc2024} have produced large datasets of convergent integer-coefficient PCFs whose limits cluster on rigid arithmetic loci. The present paper concerns the lowest non-trivial polynomial degrees: \emph{degree-$(2,1)$}, with quadratic numerator and linear denominator polynomials.

\paragraph{The objects.}
Throughout, let
\begin{equation}\label{eq:pcf-form}
  \mathrm{CF}(a,b) \;=\; b_0 \,+\, \cfrac{a(1)}{b(1) + \cfrac{a(2)}{b(2) + \cfrac{a(3)}{b(3)+\cdots}}},
\end{equation}
where $a(n) = a_2 n^2 + a_1 n + a_0$ and $b(n) = b_1 n + b_0$ with $(a_2, a_1, a_0, b_1, b_0) \in \mathbb{Z}^5$ and $a_2 b_1 \ne 0$. The \emph{Trans-stratum} $\mathcal{T}$ is the set of such tuples for which \eqref{eq:pcf-form} converges in $\widehat{\mathbb{C}}$ and the limit is a generic irrational (Definition~\ref{def:trans-stratum}).

\paragraph{Empirical phenomenon and dichotomy.}
Exhaustive search at primitive heights $|a_i|,|b_j|\le 100$, $1\le b_1 \le 50$, identified $\sim\!1.5\times 10^5$ Trans-stratum families. Inspection of $a_2/b_1^2$ across the full dataset reveals \emph{exactly two} structural values (Section~\ref{sec:empirical}):
\begin{itemize}
  \item \textbf{Class A:} $a_2/b_1^2 = -2/9$, comprising essentially all observed transcendental families ($\sim\!1.5\times 10^5$ at height $\le 100$; $78$ canonical families up to obvious symmetries);
  \item \textbf{Class B:} $a_2/b_1^2 = +1/4$, with $16$ identified canonical families whose limits lie in $\mathbb{Q}(\pi)$ (saturation open; see Remark~\ref{rem:classB-saturation}).
\end{itemize}
A sweep of $134{,}040$ candidates at the next BT integer-resonance locus $a_2/b_1^2 = -3/16$ produced zero Trans-stratum families.

\paragraph{Three independent verification sweeps.}
The original height-bounded enumeration provided $78$ canonical Class~A and $16$ canonical Class~B families plus a $134{,}040$-candidate desert at $k=3$ (Section~\ref{sec:empirical}). Subsequent stratum-aware sweeps at three additional resonance values $b_1 \in \{5, 6, 7\}$ are consistent with the bipartition. At $b_1 = 5$, Class~A integer realization requires $a_2 = -50/9 \notin \mathbb{Z}$ and Class~B integer realization requires $a_2 = 25/4 \notin \mathbb{Z}$, so both loci are predicted empty; the sweep returns zero Trans hits. At $b_1 = 6$, Class~A at $a_2 = -8$ admits three integer-coefficient realizations (with limits $4/\pi$, $4/(\pi-2)$, and $(8\pi+2\pi^2)/(2\pi+\pi^2)$) and Class~B at $a_2 = 9$ admits one ($12/\pi$); the stratum-aware sweep of $79{,}860$ candidates at $b_1 = 6$ returns exactly these four Trans hits, with $0$ third-stratum hits and $0$ locus-violations (deep-verified at \texttt{dps}$=300$, $N=1500$). At $b_1 = 7$, both loci are non-integer ($a_2 = -98/9$ and $a_2 = 49/4$) and the sweep of $79{,}860$ candidates returns zero Trans hits, providing a coprime-to-both ($\gcd(7,3) = \gcd(7,2) = 1$) null verdict. The singleton-mate $(9, 0, 0, -6, -3) \to -12/\pi$ verifies sign-flip orbit completeness for Class~B at $|b_1|=6$. Full per-family records are in the SIARC bridge sessions \texttt{T2B-BIPARTITION-B6-VERIFICATION} (commit \texttt{1735258}) and \texttt{T2B-BIPARTITION-B7-STRONG-NULL} (commit \texttt{8e18465}).

\paragraph{Main results.}

\medskip
\noindent\textbf{Theorem~\ref{thm:resonance-family} (Resonance family; proved, Sec.~\ref{sec:resonance-family}).}
The denominator recurrence of a degree-$(2,1)$ PCF has BT characteristic polynomial $\lambda^2 - b_1\lambda - a_2$. Its two roots satisfy an integer ratio $\lambda_+/\lambda_- = k \in \mathbb{Z}_{\ge 1}$ if and only if
\begin{equation}\label{eq:resonance-loci}
  \frac{a_2}{b_1^2} \;=\; -\frac{k}{(k+1)^2}.
\end{equation}
The values $-1/4, -2/9, -3/16, -4/25, \ldots$ exhaust the integer-resonance loci.

\medskip
\noindent\textbf{Theorem~\ref{thm:k2-stokes} (Class A characterisation; conditional on $S_{12}\ne 0$, Sec.~\ref{sec:k2-stokes}).}
On the resonance locus $\mathcal{R}_2 = \{a_2/b_1^2 = -2/9\}$ the BT formal expansion is regular through depth four and beyond ($\Delta_2 \equiv 0$, verified symbolically); the formal log-free codimension argument therefore does not select $k=2$, and selection is non-formal. Convergence of the PCF on $\mathcal{R}_2$ is equivalent (via Pincherle's theorem) to existence of a minimal solution, which by Immink's analysis of integer-resonance BT systems \cite{immink1984} is governed by a single Stokes multiplier $S_{12}$ given by a Borel residue at $\zeta = -\log 2$. Class A coincides with the locus $\mathcal{R}_2 \cap \{S_{12}\ne 0\}$.

\medskip
\noindent\textbf{Theorem~\ref{thm:classB-stieltjes} (Class B Stieltjes equivalence; proved, Sec.~\ref{sec:classB}).}
Every Pure-regime Class B family (those with $a_1 = a_0 = 0$, $b_0 = b_1/2$, $a_2 = b_1^2/4$) is conjugate, via the Stieltjes equivalence transformation with multiplier $\mu_0 = 1$, $\mu_n = 2/b(n)$, to the canonical Wallis/Gauss continued fraction
\begin{equation}\label{eq:wallis-canonical}
  \mathrm{CF}^*\,:\quad a^*(n)=\frac{(2n)^2}{(2n-1)(2n+1)},\quad b^*(n) = 2,
\end{equation}
with limit $4/\pi$. Consequently every such family has limit $L = (b_1/2)\cdot(4/\pi) = 2b_1/\pi$. The mixed Class B families (with non-zero $a_1$ or $a_0$) have limits in $\mathbb{Q}(\pi)$ via a two-parameter Möbius extension.

\medskip
\noindent\textbf{Completeness Conjecture.}
The degree-$(2,1)$ Trans-stratum is exactly $\mathcal{T} = \mathcal{T}_A \sqcup \mathcal{T}_B$, with $\mathcal{T}_A \subset \mathcal{R}_2$ and $\mathcal{T}_B \subset \{a_2/b_1^2 = 1/4\}$, and no third class.

\paragraph{Why $\pi$ in Class B.}
The Class B condition $a_2 = b_1^2/4$ forces the discriminant $b_1^2 + 4a_2 = 2b_1^2$, hence $\lambda_\pm = b_1(1\pm\sqrt{2})/2$, and reduces the indicial exponents to half-integer hypergeometric parameters. By the Gauss--Kummer summation \cite[\S 13]{andrews-askey-roy} and the reflection formula $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$, the resulting closed forms lie in $\mathbb{Q}(\pi)$. The irrationality of $\lambda_+/\lambda_- = 3+2\sqrt{2}$ removes any integer Stokes obstruction; convergence is automatic and limits are explicit.

\paragraph{Why no Class for $k\ge 3$.}
Heuristically, on $\mathcal{R}_k$ the BT minimal solution is governed by Stokes multipliers of multiplicity $\ge k-1$; for $k\ge 3$ the generic vanishing of these multipliers forces non-existence of a generic-irrational minimal solution, and the surviving locus has codimension $\ge 2$ in the integer lattice. The empirical desert at $k=3$ across $134{,}040$ candidates confirms this picture.

\paragraph{Relation to prior work.}
The asymptotic theory of linear difference equations is due to Birkhoff \cite{birkhoff1911}, Birkhoff \cite{birkhoff1930}, and Birkhoff--Trjitzinsky \cite{bt1932}; the Stokes/multisummability formulation we invoke for Theorem~\ref{thm:k2-stokes} is from Immink \cite{immink1984} and Braaksma--Faber \cite{braaksma-faber1996}. The Pincherle convergence theory appears in Pincherle \cite{pincherle1894} and Lorentzen--Waadeland \cite{lw1992}. Class B is the modern descendant of the Brouncker--Wallis--Gauss family, presented systematically in Wall \cite{wall1948}.
```

## §6  Working main-theorem statement (S5)

**NO WORKING M9 MAIN-THEOREM STATEMENT IN CORPUS AS OF 2026-05-05.**

Per M9 main-theorem dependency audit (commit 4ffcc8c, 2026-05-05),
verdict `INDETERMINATE_NO_FORMAL_STATEMENT`: no formal
`\begin{theorem}` or `\begin{conjecture}` environment labelled
'Master Conjecture v0', 'MASTER-V0', or 'Phi' exists in any TeX
source on disk or on Zenodo as of the audit date. The umbrella
v2.0 companion table records MASTER-V0 explicitly as 'Planned
(post-T1 / Birkhoff--Trjitzinsky)'. The closest formal environments
are downstream conjectures (`conj:b5-b6-d3` cubic-modular split,
d=3-restricted; `prob:chi-Phi-compatibility` open-problem entry).

## §7  M6 ✅-vs-Phase-A/B.5 status

**PENDING SYNTHESIZER ARBITRATION (in-tier under v2026-05-08 RACI;
expected by W20 per W19 master prompt).**

Verbatim grounding from CMB.txt (lines 1517-1518):

```text
L1482-L1484:
  1482:   #3 P-008 M9 V0 announcement draft
  1483:        (substrate ID'd; needs templates + M6 inconsistency resolved)
  1484:   #4 P-009 M8b positioning
L1516-L1518:
  1516: CLI-internal (NOT in queue):
  1517:   - M6 ✅-vs-Phase-A/B.5 arbitration (in-tier; required for
  1518:     045 §7 substrate; pending verdict before 045 fires).
L1527-L1529:
  1527:   W19 (now)        043 -> 044 (+045 parallel) -> in-tier
  1528:                    M6 arbitration + P-009 caveat
  1529:   W20 (May 11-17)  P11 SICF decision + daily loop
```

Verbatim grounding from cli_log/2026-05-05.md (line 1234):

```text
L1233-L1235:
  1233: 
  1234: 1. **M6 ✅-vs-Phase-A/B.5 arbitration verdict** — CLI in-tier;
  1235:    output to cli_log + CMB; required substrate for 045 §7.
L1249-L1251:
  1249: W19 (now)        043 → 044 (+045 parallel) → CLI in-tier
  1250:                  work on M6 arbitration + P-009 caveat
  1251: W20 (May 11-17)  P11 SICF decision; W20 daily relay loop
```

Verbatim grounding from cli_log/2026-W19_master_prompt.md / wsb.md:

```text
L77-L79:
  77: | Thu | 05-08 | P11 blocker #3 | T2B b₁=7 review | Same |
  78: | Fri | 05-09 | M6 Phase A or B.5 | P08 referee-response draft | M6 hits HALT_M6_* → log, do not retry this week |
  79: | Sat | 05-10 | Operator review | Submission decisions if any | — |
```

No verdict issued in cli_log as of compile time.
Status as of 2026-05-05: M6 arbitration is in-tier scope
under v2026-05-08 RACI; expected by W20 per W19 master prompt.

## §8  Departing-Synthesizer's three standing notes (verbatim)

```markdown
## E. Standing notes from departing Weekly Synthesizer

Three observations from W19 that don't fit elsewhere but are worth
keeping in CLI's working memory:

1. **The bipartition promotion (commit 5d83797) is a clean exemplar
   of the AEAL relay protocol.** It's the strongest single reference
   for P09 (AI Discovery, Notices AMS) — the synth-flag → CLI-tighten
   → operator-delegate → synth-concur-with-conditional-sharpening →
   CLI-applies-as-Patch-6 sequence is the methodology-paper headline
   sequence. Preserve the audit trail carefully.

2. **Saturday is genuinely a no-op day under the new RACI.** Under
   the old four-tier model Saturday was Operator review. Under the
   new model Saturday is still Operator review, but the review surface
   shrank because CLI now arbitrates JC-class flags in-tier rather
   than bouncing them to Strategyzer. Don't fill Saturday with new
   work just because there's slack.

3. **The Operator's bandwidth, not Strategyzer's bandwidth, is now
   the binding constraint on the new model.** Before this transition,
   Strategyzer was the constraint (rule3 was about that). After, the
   binding constraint is how many Copilot relay prompts the Operator
   can paste through per day. CLI should optimize WSBs for low
   Operator-touch — batch where possible, run secondaries in parallel
   where Copilot allows it, prefer one large relay over many small
   ones when the work permits.

---
```

## §9  AEAL provenance

Substrate manifest is recorded at `p008_substrate_manifest.json`
(SHA-256 to be computed post-write).
Compile script SHA-256:

```
compile_package.py SHA-256: 241ef5828fa8b40bf2a6c621f8345a68dcf66bd01e8d077af07ffb8a488f329e
```

All seven substrate sources S1..S7 have SHA-256 entries in
`p008_substrate_manifest.json` (S5 marked NOT_FOUND with reason).

