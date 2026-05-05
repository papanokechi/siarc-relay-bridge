# P-008 Input Package for Strategyzer Monthly Cycle 2026-06

## Compiled: 2026-05-05T12:24:58.801753+00:00
## Compiler: CLI-Tactical-Executer (relay 045)
## Authority for use: Strategyzer (Tier 1, monthly cadence)

This artefact is a passive substrate. It contains verbatim excerpts
from located workspace and bridge sources. Sections § 2 - § 8 quote
sources without editorial framing.

---

## § 0  rule5 grounding evidence

**(a) CMB header (most-recent timestamp + first 6 lines):**

- mtime (UTC): 2026-05-05T11:20:28.318074+00:00
- first 6 lines verbatim:

~~~~
# SIARC MORNING BRIEFING
## Claude Morning Briefing — CMD.txt
## Last updated: 2026-05-04
## Goal: ONE ACCEPTED PAPER

Paste this file into Claude.ai each morning for
~~~~

**(b) 30-day bridge listing (sessions modified within last 30 days):**

  - 2026-04-22
  - 2026-04-23
  - 2026-04-24
  - 2026-04-25
  - 2026-04-26
  - 2026-04-27
  - 2026-04-28
  - 2026-04-29
  - 2026-04-30
  - 2026-05-01
  - 2026-05-02
  - 2026-05-03
  - 2026-05-04
  - 2026-05-05
  - 2026-05-07
  - 2026-05-08
  - template

**(c) Latest cli_log files (top 3 by mtime):**

  - 2026-05-05.md  (2026-05-05T11:20:28.306641+00:00)
  - 2026-W19_master_prompt.md  (2026-05-04T23:38:12.852871+00:00)
  - 2026-W19_wsb.md  (2026-05-04T23:38:12.852871+00:00)

Status: COMPLETE (all three sources reachable).

---

## § 1  Substrate manifest

Manifest file: p008_substrate_manifest.json (SHA-256 34A60B517475559C3EFC87264C1A3D5724ECD2D892F5FDCC31FF31A5436BB2F9).
Entries verbatim:

~~~~json
﻿{
    "compiler":  "CLI-Tactical-Executer (relay 045)",
    "entries":  [
                    {
                        "size_bytes":  44935,
                        "id":  "S1",
                        "mtime_utc":  "2026-05-02T00:55:25.7456963Z",
                        "label":  "Umbrella v2.0 main.tex",
                        "sha256":  "612F732EBE2D8BABF5EE6582C3D35D6B91F2CF2421D9A7778B3A17810DAC8EF0",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\tex\\submitted\\umbrella_program_paper\\main.tex",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  70178,
                        "id":  "S2",
                        "mtime_utc":  "2026-05-02T03:33:16.8113023Z",
                        "label":  "CT v1.3 channel_theory_outline.tex",
                        "sha256":  "59C5352795F8D63DC59AC6BA11E96F91805D424CD6E20D74F52C9A565846F7E5",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\pcf-research\\channel\\cc_pipeline_v13_2026-05-02\\channel_theory_outline.tex",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  21099,
                        "id":  "S3",
                        "mtime_utc":  "2026-05-05T02:56:27.6391735Z",
                        "label":  "M9 main-theorem dependency audit handoff",
                        "sha256":  "4C8C9C22570591CCE442B62266207731C396D097B0B4B6A611C2CB1282878D19",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\siarc-relay-bridge\\sessions\\2026-05-05\\M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT\\handoff.md",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  33762,
                        "id":  "S4",
                        "mtime_utc":  "2026-05-05T10:26:33.8293686Z",
                        "label":  "T2B v3.1 bipartition manuscript",
                        "sha256":  "538B897C75908C9E25B2AD5C6F7EE8317A5906D2E7668809DBF58E7DB7755B79",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\siarc-relay-bridge\\sessions\\2026-05-07\\PCF-2-V2-BIPARTITION-PROMOTION\\t2b_paper_v3.1_bipartition_promotion.tex",
                        "status":  "FOUND"
                    },
                    {
                        "label":  "Working M9 main-theorem statement (workspace search)",
                        "path":  "\u003cgrep tex/submitted/**/*.tex\u003e",
                        "status":  "NOT_FOUND",
                        "id":  "S5",
                        "reason":  "workspace grep over tex/submitted/**/*.tex for thm:main|main_theorem|Main Theorem|Theorem 1.1|theorem M9|theorem:M9 returned 6 hits, NONE of which is a SIARC Master Conjecture / MASTER-V0 / Phi formal statement (matches: umbrella main.tex L194 forward-ref to companion paper #14; paper14 Â§Main Theorem = Ratio Universality, not Phi; pcf_rational_contamination thm:main = Trivial rational limit observation; pcf_unified_expmath_submission abstract \u0027two main theorems\u0027 = Logarithmic Ladder + 4/pi Casoratian)."
                    },
                    {
                        "size_bytes":  69288,
                        "id":  "S6_CMB",
                        "mtime_utc":  "2026-05-05T11:20:28.3180739Z",
                        "label":  "CMB.txt (M6 status surface)",
                        "sha256":  "B89A1C1B6AAB2A49286E44216535FEBD93C0B3DDA9D3B41ECBD900335FE656ED",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\tex\\submitted\\CMB.txt",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  71620,
                        "id":  "S6_cli_log",
                        "mtime_utc":  "2026-05-05T11:20:28.3066408Z",
                        "label":  "cli_log\\2026-05-05.md (M6 arbitration status)",
                        "sha256":  "6FD1A1A14C9F13BD415A19056D2DBFB1A5E6EE0E4BF3F08D0AF14DB4BA0FA672",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\cli_log\\2026-05-05.md",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  5383,
                        "id":  "S6_W19_wsb",
                        "mtime_utc":  "2026-05-04T23:38:12.8528709Z",
                        "label":  "cli_log\\2026-W19_wsb.md (M6 framing in WSB)",
                        "sha256":  "7AF74267E25B8CDE4B89C5DD6DD8938405BF83FE538E5FEB36F6BE1BA81FED8F",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\cli_log\\2026-W19_wsb.md",
                        "status":  "FOUND"
                    },
                    {
                        "size_bytes":  12323,
                        "id":  "S7",
                        "mtime_utc":  "2026-05-05T11:20:12.9891164Z",
                        "label":  "Departing-Synthesizer\u0027s three standing notes (043 inbox handoff)",
                        "sha256":  "F6FC35AF0F7EBFEB3FD984F3812AFE1B92F5E5F1F0F38786587A01013C78761D",
                        "path":  "C:\\Users\\shkub\\OneDrive\\Documents\\archive\\admin\\VSCode\\claude-chat\\tex\\submitted\\control center\\synthesizer_inbox\\STRATEGYZER_HANDOFF_2026-05-08.md",
                        "status":  "FOUND"
                    }
                ],
    "compiled_utc":  "2026-05-05T11:44:25.0053821Z"
}

~~~~

---

## § 2  Umbrella v2.0 § "Cross-Degree Framing: the Invariant Triple"  (verbatim, L212-502)

Source: tex/submitted/umbrella_program_paper/main.tex  (S1; FOUND)

~~~~tex
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

\section{Logical Structure of the Program}
\label{sec:structure}

\subsection{Companion papers and dependency graph}

Figure~\ref{fig:depgraph} shows the dependency structure of the
program after the post-March 2026 stack. The $\PSLZ$ classification
(\#14) and the Trans-Stratum paper (T2B) remain at the centre;
PCF-1 / PCF-2 / Channel Theory enter as the cross-degree extension
spine; the standalone $j$-invariant note (jSN) is the polished
exposition of the equianharmonic cubic cell of \S\ref{sec:triple-moddisc}.

\begin{figure}[h]
\centering
\begin{tikzpicture}[
  node distance=8mm and 12mm,
  every node/.style={draw, rounded corners, align=center,
                     font=\footnotesize, inner sep=4pt},
  arr/.style={-{Latex[length=2mm]}, thick}
]
\node (p14) {\#14\\ $\PSLZ$ 4-tier};
\node (t2b) [right=of p14] {T2B\\ Trans-stratum $-2/9$};
\node (p08) [right=of t2b] {P08\\ Painlev\'e link};
\node (pcf1)[below=of p14] {PCF-1\\ $d{=}2$ sharp WKB};
\node (pcf2)[right=of pcf1] {PCF-2\\ $d{=}3$ cubic-modular};
\node (ct)  [right=of pcf2] {CT\\ Channel theory};
\node (jsn) [below=of pcf2] {jSN\\ $j$-cell note};
\node (op)  [below=of ct]  {OP\\ Open problems};

\draw[arr] (p14) -- (t2b);
\draw[arr] (t2b) -- (p08);
\draw[arr] (pcf1) -- (pcf2);
\draw[arr] (pcf2) -- (ct);
\draw[arr] (p14)  -- (pcf1);
\draw[arr] (t2b)  -- (pcf2);
\draw[arr] (pcf2) -- (jsn);
\draw[arr] (ct)   -- (op);
\draw[arr] (p08)  -- (op);
\draw[arr] (jsn)  -- (op);
\end{tikzpicture}
\caption{Dependency graph of the SIARC companion papers (v2.0).
Arrows denote ``logical prerequisite''; the umbrella paper (this
document, v2.0) sits above all nodes and provides the unified
notation and the cross-degree invariant triple of
\S\ref{sec:triple}.}
\label{fig:depgraph}
\end{figure}

\subsection{Unified notation}

Across the series we adopt the following conventions. Companion papers
that predate this umbrella may use slightly different notation locally;
the table below is the canonical reference and absorbs the v2.0
additions (the invariant triple, the channel and bridge functors, the
cell decomposition, and the residual notation).

\begin{center}
\begin{tabular}{@{}lll@{}}
\toprule
Symbol & Meaning & Convention \\
\midrule
$x$ & PCF variable & integer, $x \geq 1$ \\
$a_n(x), b_n(x)$ & partial num./denom.\ polynomials & $\Z[x]$ \\
$(d_a, d_b)$ & degree pair & $d_a = \deg a_n$, $d_b = \deg b_n$ \\
$d$ & denominator polynomial degree & $d = \deg b$ (cross-degree label) \\
$\Gamma$ & uniformizing Fuchsian group & subgroup of $\PSLZ$ unless stated \\
$K(x)$ & limit of the PCF at $x$ & in $\R \cup \{\infty\}$ \\
$\mu(\alpha)$ & irrationality measure of $\alpha$ & $\mu \geq 2$ for irrationals \\
$c_{\Gamma,(d_a,d_b)}$ & trans-stratum exponent & rational, depends on $\Gamma$ and degrees \\
T0--T3 & arithmetic tiers & as in \S\ref{sec:tiers} \\
$\Delta_d(b)$ & polynomial discriminant axis & $\mathrm{disc}(b)$, $\S$\ref{sec:triple-disc} \\
$\tau_b$ & period of $E_b: y^2 = b(x)$ & in $\HH/\mathrm{SL}_2(\Z)$ \\
$\PetN{\Delta}(\tau_b)$ & Petersson modular-discriminant axis & $|\Delta(\tau_b)|(\mathrm{Im}\,\tau_b)^6$ \\
$\xi_0(b)$ & Borel-radius axis & $d/\beta_d^{1/d}$, $\S$\ref{sec:triple-borel} \\
$E,\ P_k,\ B$ & cell decomposition & $\S$\ref{sec:triple-cells} \\
$\chi$ & channel functor & \cite{CT} \\
$\Phi$ & bridge functor (umbrella v2.0) & \eqref{eq:Phi-functor} \\
$\delta_n$ & PCF residual (PCF-2 notation) & $\delta_n = \log|p_n - K(x) q_n|$ \\
$A_{\mathrm{fit}}, A_{\mathrm{PCF}}$ & fitted and conjectured WKB exponent & $A_{\mathrm{PCF}} = 2d$ (Conj.~B4) \\
\bottomrule
\end{tabular}
\end{center}

\noindent
\textbf{Degree convention.} Throughout the series, ``degree-$(d_a, d_b)$''
refers to the \emph{generic} polynomial degrees of $a_n$ and $b_n$ as
functions of the index $n$ in the underlying recurrence, not as
functions of $x$. A degree-$(2,1)$ family is therefore one in which
the numerator polynomial grows quadratically in $n$ and the denominator
grows linearly in $n$. The cross-degree label $d = \deg b$ of
\S\ref{sec:triple} matches $d_b$ at $\PCF(1,b)$ where $\deg a = 0$.

\paragraph{Coefficient ordering.} PCF family coefficients
$[a_2, a_1, a_0, b_1, b_0]$ and $[\beta_d, \dots, \beta_0]$ are stored
\emph{leading-coefficient-first} throughout the SIARC stack
(\texttt{f1\_base\_computation.py} convention). This matches the v2.0
notation: $\xi_0(b) = d/\beta_d^{1/d}$ uses $\beta_d$ as the leading
coefficient of $b$.

~~~~

---

## § 3  CT v1.3 § "Implications for the Master Conjecture" (verbatim, L1336-1355)

Source: pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex  (S2; FOUND)

~~~~tex
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
~~~~

---

## § 4  M9 main-theorem dependency audit verdict (verbatim full handoff, commit 4ffcc8c)

Source: siarc-relay-bridge/sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md  (S3; FOUND)

~~~~markdown
# Handoff — M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT
**Date:** 2026-05-05
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

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

## What was accomplished

Read-only audit of all ten upstream sources listed in the spec (Step 0
A–J) plus a workspace-wide grep across `tex/submitted/**/*.tex` for the
canonical strings "Master Conjecture", "MASTER-V0", "Phi formally",
"S_2", "second Stokes", "alien amplitude". Confirmed via verbatim
quotation that:

1. The umbrella v2.0 `main.tex` defines the bridge functor `Phi` at
   `eq:Phi-functor` but does NOT state a Master Conjecture / MASTER-V0
   theorem; the only references to MASTER-V0 in the manuscript are
   forward-looking pointers to the future companion paper.
2. PCF-1 v1.3, PCF-2 v1.3, and Channel Theory v1.3 each contain
   contributions to the SIARC program but no formal Phi statement of
   the master classification.
3. The 2026-05-01 SIARC-MASTER-V0 session was HALTED at Phase MV0-1
   before any draft text was produced (verbatim handoff §"Status:
   HALTED").
4. Picture v1.18 (bridge) and `picture_revised_20260504.md`
   (operator-side mirror) are byte-identical at the M8b and M9 blocks;
   no H5 divergence.
5. Dossier §C confirms no closed-form S_2 for the SIARC d=2 PCF
   dichotomy is available in literature (Costin 2008 = S_1 only; BLMP
   2024 = RH-characterised monodromy data, partial fit).

Step 1 returned NONE under the strict precedence rule (1→2→3→4→5),
escalating to verdict `INDETERMINATE_NO_FORMAL_STATEMENT`.

## Key numerical findings

None. This is a pure manuscript / picture / dossier audit. No
computations performed.

## Step-0 source inventory (verbatim summary table)

| Src | File | M9 main-theorem statement found? | S_2 mention? |
|-----|------|----------------------------------|--------------|
| A | `siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/picture_v1.18.md` (L959–995) | NO formal theorem; SCHEMA only ("Phi formally stated and the master classification result conditional on P-NP + P-B4 + P-CC", L973–975) | YES (L965–973) — type (b)+(c) only ("S_2 PERMANENTLY FORECLOSED via Stage-2-LSQ ... Borel-Padé") in M8b block; M9 block itself has 0 S_2 hits |
| B | `tex/submitted/control center/picture_revised_20260504.md` (L926–960) | byte-identical to A in this block | byte-identical to A in this block |
| C | `tex/submitted/umbrella_program_paper/main.tex` (Phi definition L273; MASTER-V0 forward refs L298–299, L695, L806) | NO formal theorem; bridge functor `Phi : PCF(1,b) → (Δ_d(b), ‖Δ‖_Pet(τ_b), ξ_0(b))` defined as eq:Phi-functor; companion table line 806 records "MASTER-V0 ... Planned (post-T1 / Birkhoff--Trjitzinsky)" | 0 occurrences of "S_2", "Stokes constant", "alien amplitude", "second Stokes" anywhere in main.tex |
| D | `tex/submitted/pcf_unified_expmath_submission.tex` (PCF-1 v1.3) (abstract L40) | "two main theorems" = Logarithmic Ladder + 4/π Casoratian; NO Phi / Master Conjecture / MASTER-V0 statement | 0 occurrences of S_2 / Stokes constant / alien amplitude / second Stokes / S_zeta |
| E | `siarc-relay-bridge/sessions/2026-05-02/CHANNEL-THEORY-V13-RELEASE/channel_theory_outline.tex` (CT v1.3) (§"Implications for the Master Conjecture" L1336–1339; channel functor definition L1026; alien amplitude refs L109, L221, L926, L1379, L1401) | NO formal Phi theorem; section §"Implications" lists 4 preconditions for "A rigorous announcement of the Master Conjecture" | YES — V_quad alien amplitude (S_zeta_*) discussed structurally; "the missing piece is the full Stokes-matrix datum" (L1339 ff., type (b) structural-existence) |
| E' | `tex/submitted/pcf2_program_statement.tex` (PCF-2 v1.3) | NO formal Phi theorem | 0 occurrences of Master Conjecture / MASTER-V0 / S_2 / second Stokes / alien amplitude / Phi formally |
| F | `siarc-relay-bridge/sessions/2026-05-04/MILESTONE-RESIDUAL-GAP-SURVEY-M4-M7-M8B-M9/dossier_milestone_residual_gap_survey_m4_m7_m8b_m9.md` §C (L185–212) §D (L272+) | n/a (dossier is literature pass, not theorem source) | YES — §C verdict: closed-form S_2 NOT in literature for SIARC d=2 PCF dichotomy (Costin 2008 = S_1 only; BLMP 2024 = RH partial) |
| G | `sessions/2026-05-01/SIARC-MASTER-V0/handoff.md` | confirms NO Phi statement drafted; "Status: HALTED" before content | n/a |
| H | `tex/submitted/CMB.txt` (L361–410) | confirms M9 still upstream of MASTER-V0 fire; "Sakai 1999 = recommended template if SIARC-MASTER-V0 announcement fires" (L405–410) | confirms "NO closed-form S_2 alien-amplitude formula for the SIARC d=2 PCF dichotomy" (L389–395) |
| I | `sessions/2026-05-02/SIARC-UMBRELLA-V2-RELEASE/zenodo_description_v2.0.txt` | reaffirms umbrella v2.0 is a "program statement, not a results paper"; Phi mentioned as triple-invariant; MASTER-V0 referenced as future entry in publication ladder | 0 occurrences of S_2 / Stokes / alien |
| J | workspace-wide `tex/submitted/**/*.tex` grep for Master Conjecture / MASTER-V0 / S_2 / second Stokes / alien amplitude | only umbrella `main.tex` lines 298, 299, 695, 806 (forward refs); CT v1.3 (per E); `vquad_resurgence_R1.tex`/`R2.tex` use `s_1, s_2` as PIII apparent-singularity coordinates (NOT Stokes constants) | as above |

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

## Step 2 — Dependency trace (pre-rendering only; non-binding)

Because Step 1 returned NONE, Step 2 is non-binding per the spec; but
for synthesizer benefit it is recorded as a pre-rendering across the
schema-level fragments that *do* exist:

| Fragment | S_2 occurrence(s) | Type | Statement-level dependency |
|----------|-------------------|------|----------------------------|
| Umbrella v2.0 `eq:Phi-functor` and surrounding §4 | none | n/a | NO_DEPENDENCY (Phi triple is `(Δ_d, ‖Δ‖_Pet, ξ_0)`; Stokes data not present) |
| Umbrella v2.0 §"Open Problems" `prob:b4-allD` (L686–696) | none | n/a | references "Birkhoff--Trjitzinsky asymptotic theory of irregular linear difference equations \cite{Birkhoff1930, BirkhoffTrjitzinsky1933}" — no S_2 |
| Picture v1.18 M9 block (L973–989) | none in M9 block; M8b adjacent block (L959–972) carries the S_2 PERMANENTLY FORECLOSED tag | M8b S_2 refs are type (c) numerical-foreclosure; M9 block has 0 S_2 refs | NO_DEPENDENCY at M9 level; M8b is downstream sibling, not gate (per v1.15 gating reduction to {M4, M6}) |
| Channel Theory v1.3 §"Implications for the Master Conjecture" (L1336–1349) | "the missing piece is the full Stokes-matrix datum" (L1339 ff.) | type (b) structural-existence | SOFT_DEPENDENCY: rigorous announcement requires Stokes-matrix *datum* (the full multiplier vector), not closed-form S_2 *value* |
| CT v1.3 channel-functor definition (L1026 ff.) | references "alien amplitude" structurally for V_quad | type (b) | SOFT_DEPENDENCY at most |

Summary: across all four schema-level fragments, every Stokes / S_2
reference is type (b) structural or type (c) numerical-state. None is
type (a) closed-form-value. Per Step 2.3/2.4 pre-rendering: the eventual
formal Phi statement, if drafted faithful to the current schema, would
yield SOFT_DEPENDENCY (CT v1.3 reading) or NO_DEPENDENCY (umbrella v2.0
+ picture v1.18 reading). It would NOT yield HARD_DEPENDENCY unless
P-008 introduces a closed-form-value invocation of S_2 not present in
any of the four schema fragments.

## Step 3 — M8b status cross-check

Verbatim from picture v1.18 M8b block (L959–972):

> M8b: 🆕 Stokes-multiplier discrimination (per-family, with t2c-style
> precision escalation) to resolve the PCF-1 sign-of-Delta dichotomy
> below the Painlevé-class scale
> [PARTIAL+a_1-PARTITION-CLOSED+S_2-PERMANENTLY-FORECLOSED:
>  |S_1| measured (010); a_1 3-stratum partition CLOSED at 60+ digits
>  (017c+017e); G20 third stratum HIGHER-DIM 4-d cylinder over
>  (delta, epsilon) (T37L 2026-05-03); S_2 PERMANENTLY FORECLOSED via
>  Stage-2-LSQ (017c+017e) + Borel-Padé (T37M HALT 2026-05-03 retires
>  final numerical S_2 path); P-PIII alien-amplitude scale closes at
>  degraded resolution (S_1 measured, S_2 structurally open)]

Verbatim from dossier §C row C.P1 (Costin 2008):

> Theorem 5.26 gives the **first** Stokes constant `S₁` in the
> connection formula; the **second** Stokes constant `S₂` would
> correspond to the second singularity at `2λ₁` in the Borel plane;
> Costin 2008 §5 / Theorem 5.11 (eq. 5.12) has a multi-singular
> analytic-structure formula `Y₀±(z + lλⱼ)` with `l ∈ ℕ⁺` covering
> `l ≥ 2`, but **the closed-form for the corresponding `S²ⱼ`-derived
> alien amplitude `S₂`** is not given as a single explicit formula
> [...]; "second Stokes" returns 0 hits; "S_2" (alien-amplitude sense)
> returns 0 hits.

Verbatim from dossier §C row C.P2 (BLMP 2024):

> Closed-form S_2 claim (Y / N / partial / NIA) | partial — Theorems
> 1.1 + 1.4 + 1.7 give explicit Riemann-Hilbert-problem
> characterisations of monodromy data [...]; pinning the second alien
> amplitude `S_2` for a specific normalisation (the SIARC d=2 PCF δ_n
> one) requires the normalisation map step which is the subject of M6
> Phase B and currently INDEX-2 closed (036 verdict, 2026-05-04).

Verbatim from CMB (L389–395):

> Costin Theorem 5.26 + BLMP 2024 RH characterisation of monodromy
> for PIII(D_8) and PIII(D_6) give the structural framework but NO
> closed-form S_2 alien-amplitude formula for the SIARC d=2 PCF
> dichotomy (verbatim search of 9030-line BLMP TXT for SIARC dichotomy
> markers: 0 hits).

**Cross-source concordance** (picture v1.18 ↔ dossier §C ↔ CMB): all
three independent sources agree on:

- Numerical paths to S_2 are PERMANENTLY FORECLOSED at the laptop-feasible
  precision regime (Stage-2-LSQ + Borel-Padé both halted with structural
  failure modes).
- Literature does not supply a closed-form S_2 value for the SIARC d=2
  PCF dichotomy specifically (Costin = S_1 only; BLMP = RH-structural).
- Closure of S_2 at value-level would require either operator-side ILL
  acquisition of further primary sources (Mazzocco, Iwaki et al.,
  Lisovyy-Roussillon, Clavier-Cournod) or a SIARC-primary derivation.

Status label per Step 3.3: **DEFERRED-PENDING-PRIMARY-DERIVATION**
(literature partial; numerical foreclosed; primary derivation not yet
attempted at announcement-grade scope).

No divergence detected between picture v1.18, dossier §C, and CMB on
S_2 status.

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

## Judgment calls made

1. **Step-1 escalation to Rule 5 (NONE):** the spec's precedence rule
   says "any formal `Theorem` or `Conjecture` environment ... labelled
   'Master Conjecture v0' or 'MASTER-V0' or 'Phi'". I checked
   workspace-wide and found NONE. The picture v1.18 schema (Rule 3)
   is explicitly tagged in the spec as "treated as a SCHEMA, not a
   formal theorem", so it cannot serve as a statement-of-record. This
   triggers the NONE clause and verdict
   `INDETERMINATE_NO_FORMAL_STATEMENT`.
2. **Step 2 pre-rendering recorded as observation, not verdict:** per
   Step 4.4, "Do NOT speculate the dependency direction" when verdict
   is INDETERMINATE. I have honoured this by recording the
   pre-rendering as a non-binding table inside Step 2 with explicit
   tag "non-binding"; the operator-escalation gate at the top reports
   only the INDETERMINATE verdict.
3. **Provisional caveat draft:** Step 4.4 only asks for a
   "recommend retry" action. I have additionally drafted a
   provisional caveat for synthesizer P-009 use, conditional on the
   schema not shifting under P-008. This is judgment-call territory
   (the spec does not explicitly request it), but the synthesizer
   originally asked for caveat language; providing a conditional
   draft unblocks P-009 partial work without committing the audit
   verdict. If the operator considers this overreach, the
   provisional caveat can be discarded with no impact on the verdict.
4. **TODAY_DATE = 2026-05-05** rather than the spec's candidate slot
   2026-05-06: the relay prompt explicitly allows "any slot before
   P-008 / P-009 fire", and the system date at session-start was
   2026-05-05. Using 2026-05-05 keeps the bridge folder consistent
   with actual session date.

## Anomalies and open questions

- **None at audit-verdict level.** No HALT triggered (H1–H6 all clear:
  no mutually-inconsistent multiple statements; no HARD_DEPENDENCY; no
  unauthorised post-2026-05-01 Phi draft; all sources A–J readable;
  pictures A and B byte-identical; provisional caveat free of
  forbidden AEAL verbs).
- **Operator-side note (not an anomaly):** the picture v1.18
  M9 gating amendment history records v1.15 as the moment M9 reduced
  unconditionally to {M4, M6} (with M8b excluded). The current verdict
  is consistent with that amendment: closed-form S_2 is not on the
  M9 critical path. If P-008 inadvertently introduces a closed-form
  S_2 dependency, that would *contradict* the v1.15 amendment and
  should trigger an immediate re-audit + picture v1.19 amendment.

## What would have been asked (if bidirectional)

- "If the verdict is `INDETERMINATE_NO_FORMAL_STATEMENT`, does the
  operator want me to draft a *minimal* Phi statement skeleton based
  on the umbrella v2.0 + CT v1.3 schemas as a non-binding starting
  point for P-008, or strictly defer all drafting to synthesizer?"
  Default chosen: defer (per Step 4.4 do-not-speculate clause).

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

## Files committed (this session, local-only — no push)

- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/dependency_trace.md`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/verdict.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/claims.jsonl`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/halt_log.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/discrepancy_log.json`
- `sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/unexpected_finds.json`

## AEAL claim count

5 entries written to claims.jsonl this session (C1–C5).

## Push status

**LOCAL-ONLY.** Not pushed. Per spec Step 6: INDETERMINATE verdict →
"push as informational; flag P-008 as the next-action prerequisite."
Operator gates the actual `git push`.

~~~~

---

## § 5  T2B v3.1 bipartition framing (verbatim, commit 5d83797)

Source: siarc-relay-bridge/sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_promotion.tex  (S4; FOUND)

### § 5.1  Introduction (L36-94)

~~~~tex
We study integer polynomial continued fractions (PCFs) of degree $(2,1)$ — quadratic numerator, linear denominator — and their \emph{Trans-stratum}: the convergent, generic-irrational subclass identified by exhaustive search in the SIARC programme. We show that the Trans-stratum partitions cleanly into exactly two arithmetic classes, distinguished by the value of the structural ratio $a_2/b_1^2$ and by the spectral type of the underlying Birkhoff--Trjitzinsky (BT) characteristic equation $\lambda^2 - b_1\lambda - a_2 = 0$. \emph{Class A} ($a_2/b_1^2 = -2/9$) corresponds to the integer-resonance locus $\lambda_+ /\lambda_- = 2$, supports a generic Stokes phenomenon (Stokes multiplier $S_{12}\ne 0$ on the locus), and yields generic transcendental limits; $\sim\!1.5\times 10^5$ such families are observed and account for all transcendental Trans-stratum data. \emph{Class B} ($a_2/b_1^2 = +1/4$) has irrational characteristic ratio $\lambda_+/\lambda_- = 3+2\sqrt{2}$, no Stokes obstruction, half-integer hypergeometric parameters, and limits in $\mathbb{Q}(\pi)$; we exhibit $16$ minimal Brouncker-shape such families (saturation is open; see Remark~\ref{rem:classB-saturation}) and prove (Theorem~3) that every Pure-regime member is the Stieltjes/Wallis transform of the canonical Gauss continued fraction for $4/\pi$. We give a complete proof of the resonance-family theorem (Theorem~1) and a Stokes-theoretic conditional theorem (Theorem~2) characterising Class~A. A sweep of $134{,}040$ candidates at the next BT integer-resonance locus $a_2/b_1^2 = -3/16$ produced zero Trans-stratum families, confirming a complete desert at $k=3$. Three independent stratum-aware verification sweeps at $b_1 \in \{5, 6, 7\}$ are consistent with the bipartition: at $b_1 = 5$ both loci are predicted empty (since $9 \nmid 25$ and $2 \nmid 5$); at $b_1 = 6$, four Trans-stratum hits land on exactly the predicted loci (three on Class~A at $a_2 = -8$, one on Class~B at $a_2 = 9$); and at $b_1 = 7$ a coprime-to-both null sweep of $79{,}860$ candidates returns zero Trans-stratum hits (since $9 \nmid 49$ and $4 \nmid 49$ block both loci simultaneously). These observations support our \emph{Completeness Conjecture}: the degree-$(2,1)$ Trans-stratum is exhausted by Class~A and Class~B.
\end{abstract}

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
~~~~

### § 5.2  Theorem 1 - the resonance family (L122-165)

~~~~tex
\section{Theorem 1: the resonance family}\label{sec:resonance-family}

\begin{lemma}[BT formal solutions]\label{lem:bt-formal}
For $a_2 \ne 0$ and $b_1^2 + 4a_2 \ne 0$, recurrence \eqref{eq:recurrence} admits two linearly independent formal solutions
\begin{equation}\label{eq:bt-ansatz}
  Q^\pm(n) \;=\; \lambda_\pm^{\,n}\,(n!)\,n^{\rho_\pm}\Bigl(1 + \sum_{j\ge 1} c_j^\pm\,n^{-j}\Bigr),
\end{equation}
with $\lambda_\pm$ the roots of
\begin{equation}\label{eq:characteristic}
  \chi(\lambda) \;=\; \lambda^2 - b_1\lambda - a_2,
\end{equation}
and $\rho_\pm = \big((b_0-b_1)\lambda_\pm + (a_1-a_2)\big)\big/(b_1\lambda_\pm + 2a_2)$.
\end{lemma}

\begin{proof}
Substitute \eqref{eq:bt-ansatz} into \eqref{eq:recurrence}; the leading $n^1$ balance gives \eqref{eq:characteristic}, the $n^0$ balance fixes $\rho_\pm$, and the formal series is then determined inductively by matching successive powers of $n^{-1}$. The recursion is regular as long as $\lambda_+ \ne k\lambda_-$ for any $k\in\mathbb{Z}_{>0}$; see \cite[Thm.~1]{bt1932} or \cite[Ch.~VIII]{wasow1965}.
\end{proof}

\begin{theorem}[Resonance family]\label{thm:resonance-family}
The two roots $\lambda_\pm$ of \eqref{eq:characteristic} satisfy $\lambda_+ = k\,\lambda_-$ for some $k\in\mathbb{Z}_{\ge 1}$ if and only if
\begin{equation}\label{eq:resonance-formula}
  \frac{a_2}{b_1^2} \;=\; -\frac{k}{(k+1)^2}.
\end{equation}
\end{theorem}

\begin{proof}
By Vieta, $\lambda_+ + \lambda_- = b_1$ and $\lambda_+ \lambda_- = -a_2$. Setting $\lambda_+ = k\lambda_-$:
$(k+1)\lambda_- = b_1$, $k\lambda_-^2 = -a_2$, hence $\lambda_- = b_1/(k+1)$ and $-a_2 = k b_1^2/(k+1)^2$, equivalent to \eqref{eq:resonance-formula}. The converse is direct.
\end{proof}

\begin{corollary}\label{cor:k=2}
The identity $a_2/b_1^2 = -2/9$ is exactly $k=2$ in \eqref{eq:resonance-formula}: $\lambda_- = b_1/3$, $\lambda_+ = 2b_1/3$.
\end{corollary}

\begin{remark}\label{rem:k1-and-wallis}
The case $k=1$ forces $\lambda_+ = \lambda_-$, hence the discriminant of \eqref{eq:characteristic} vanishes; this excludes Trans-stratum membership in the integer-resonance family (algebraic limits, log corrections). The Wallis locus $\mathcal{W} = \{a_2/b_1^2 = 1/4\}$ is \emph{not} an integer-resonance locus: the discriminant is $b_1^2+4a_2 = 2b_1^2$, the roots are $\lambda_\pm = b_1(1\pm\sqrt{2})/2$, and the ratio $\lambda_+/\lambda_- = 3+2\sqrt{2}\notin\mathbb{Q}$. This irrationality removes any integer Stokes obstruction (Sec.~\ref{sec:classB}).
\end{remark}

\section{Theorem 2: Class A and the Stokes mechanism}\label{sec:k2-stokes}

\subsection{Pincherle convergence}

\begin{proposition}[Pincherle's theorem]\label{prop:pincherle}
The PCF \eqref{eq:pcf-form} converges in $\widehat{\mathbb{C}}$ if and only if \eqref{eq:recurrence} admits a \emph{minimal} (subdominant) solution $Q^{\min}$. The limit is $-Q^{\min}(-1)/Q^{\min}(0)$ in the standard normalization \cite[Thm.~3.7]{lw1992}.
~~~~

### § 5.3  Theorem 3 - Class B Stieltjes equivalence (L222-290)

~~~~tex
\section{Theorem 3: Class B and the Gauss continued fraction}\label{sec:classB}

\subsection{The Wallis locus}

Set $\mathcal{W} = \{a_2/b_1^2 = 1/4\}$. The discriminant $b_1^2+4a_2 = 2b_1^2$ gives roots $\lambda_\pm = b_1(1\pm\sqrt{2})/2$ with irrational ratio $3+2\sqrt{2}$; no integer Stokes obstruction occurs (Remark~\ref{rem:k1-and-wallis}). The condition $a_2 = b_1^2/4$ identifies the indicial polynomial of the associated $_2F_1$ ratio as having half-integer parameters, which by the reflection formula forces limits in $\mathbb{Q}(\pi)$.

\subsection{The Stieltjes/Wallis equivalence}

Recall the equivalence transformation \cite[\S 2.4]{lw1992}: for any sequence $\mu_n$ with $\mu_0=1$ and $\mu_n\ne 0$, multiplying numerator $a(n)$ by $\mu_{n-1}\mu_n$ and denominator $b(n)$ by $\mu_n$ produces an equivalent CF. We apply it with
\begin{equation}\label{eq:mu}
  \mu_0 = 1, \qquad \mu_n = \frac{2}{b(n)} = \frac{2}{b_1 n + b_0} \quad (n\ge 1).
\end{equation}

\begin{theorem}[Class B Stieltjes equivalence]\label{thm:classB-stieltjes}
Let $(a_2, 0, 0, b_1, b_1/2) \in \mathbb{Z}^5$ be a Pure-regime Class B family ($a_2 = b_1^2/4$, $a_1 = a_0 = 0$, $b_0 = b_1/2$, equivalently $b(n) = (b_1/2)(2n+1)$). Under the equivalence transformation \eqref{eq:mu}, recurrence \eqref{eq:recurrence} maps to the canonical Wallis kernel
\begin{equation}\label{eq:wallis-kernel}
  a^*(n) = \frac{(2n)^2}{(2n-1)(2n+1)}, \qquad b^*(n) = 2,
\end{equation}
whose continued fraction equals $4/\pi$ \cite[\S 92]{wall1948}. Consequently
\begin{equation}\label{eq:classB-limit}
  L\bigl(a_2, 0, 0, b_1, b_1/2\bigr) \;=\; \frac{b_1}{2}\cdot\frac{4}{\pi} \;=\; \frac{2 b_1}{\pi}.
\end{equation}
\end{theorem}

\begin{proof}
Write $b(n) = k(2n+1)$ where $k = b_1/2$. Then $\mu_n = 2/(k(2n+1))$ for $n\ge 1$. The numerator transforms as
\[
  \mu_{n-1}\mu_n\, a(n) \;=\; \frac{2}{k(2n-1)}\cdot\frac{2}{k(2n+1)}\cdot k^2 n^2 \;=\; \frac{(2n)^2}{(2n-1)(2n+1)},
\]
using $a(n) = a_2 n^2 = (b_1^2/4)n^2 = k^2 n^2$ on the Pure-regime locus, with the $n=1$ case using $\mu_0 = 1$ in place of $2/(k\cdot 1)$, which absorbs into the leading constant $b_0 = k$ that survives outside the equivalence (see below). The denominator transforms as $\mu_n b(n) = (2/(k(2n+1)))\cdot k(2n+1) = 2$. Equivalence preserves convergence and value. The leading term $b_0 = k$ sits outside the equivalence and scales the canonical limit by $k$; combined with the canonical value $4/\pi$ this gives \eqref{eq:classB-limit}.
\end{proof}

\begin{remark}[Painlev\'{e}~III($D_6$) reduction]\label{rem:piii-d6}
The monodromy proxy via BT discriminant
$D = 2\cdot b_{\mathrm{top}}^2$ assigns all $16$
Class~B families to Painlev\'{e}~III($D_6$)
uniformly, strengthening this characterization
to a Painlev\'{e}-class reduction.
\end{remark}

\begin{corollary}[Pure-regime Class B limits lie in $\mathbb{Q}\cdot\pi^{-1}$]\label{cor:classB-pi}
For every Pure-regime Class B family the limit lies in $\mathbb{Q}\cdot\pi^{-1}$. The five primitive Pure-regime families found by the SIARC search at height $\le 100$ are listed in Table~\ref{tab:classB-pure}.
\end{corollary}

\begin{table}[h]
\centering
\begin{tabular}{lccccr}
\toprule
$(a_2,a_1,a_0,b_1,b_0)$ & $b_1/2$ & predicted $L$ & numerical residual at dps $150$, depth $4000$ \\
\midrule
$(1, 0, 0, 2, 1)$    & $1$  & $4/\pi$    & $0$ \\
$(1, 0, 0, -2, -1)$  & $-1$ & $-4/\pi$   & $0$ \\
$(4, 0, 0, 4, 2)$    & $2$  & $8/\pi$    & $0$ \\
$(4, 0, 0, -4, -2)$  & $-2$ & $-8/\pi$   & $0$ \\
$(9, 0, 0, 6, 3)$    & $3$  & $12/\pi$   & $3.05\times 10^{-151}$ \\
\bottomrule
\end{tabular}
\caption{Pure-regime Class B families verified numerically (session T2B-STIELTJES-VERIFY).}
\label{tab:classB-pure}
\end{table}

\begin{remark}[Mixed regime]
The remaining $11$ Class B families have $a_1\ne 0$ or $a_0\ne 0$; the same multiplier $\mu_n$ collapses the kernel $a^*(n)/b^*(n)$ but the leading rational shifts produce limits in $\mathbb{Q}(\pi)$ of more general shape, e.g.\ $(1,2,0,-2,-3)\mapsto -4/(\pi-2)$. A two-parameter Möbius extension (in preparation) is expected to map all $16$ Class B families onto a single canonical CF up to a fractional-linear transformation in $\pi$.
\end{remark}

\begin{remark}[Class B saturation status]\label{rem:classB-saturation}
At precision \texttt{dps}$=300$, $K=250$ within
the Worpitzky boundary, $16$ minimal Brouncker-shape
Class~B families were identified. The count is
~~~~

---

## § 6  Working main-theorem statement (status)

NO WORKING M9 / SIARC-MASTER-V0 / Phi MAIN-THEOREM STATEMENT IN
WORKSPACE OR BRIDGE CORPUS AS OF 2026-05-05.

The 2026-05-05 M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT (verdict
INDETERMINATE_NO_FORMAL_STATEMENT, full text quoted verbatim in § 4)
returned Step 1 - Statement-of-record Rule 5 (NONE) under strict
precedence. No formal theorem or conjecture environment labelled
"Master Conjecture v0", "MASTER-V0", or "Phi" exists in any of:

- tex/submitted/umbrella_program_paper/main.tex (umbrella v2.0)
- tex/submitted/pcf_unified_expmath_submission.tex (PCF-1 v1.3)
- tex/submitted/pcf2_program_statement.tex (PCF-2 v1.3)
- pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex (CT v1.3)
- sessions/2026-05-01/SIARC-MASTER-V0/handoff.md (HALTED before content)
- siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/picture_v1.18.md (SCHEMA only, not a formal theorem environment per audit Rule 3)

Workspace grep over tex/submitted/**/*.tex for the patterns
thm:main | main_theorem | Main Theorem | Theorem 1.1 | theorem M9 |
theorem:M9 returned 6 hits, none of which is a Phi master statement
(full breakdown in the manifest entry for S5).

---

## § 7  M6 status (verbatim from CMB, cli_log, and W19 WSB)

Source A: tex/submitted/CMB.txt  (S6_CMB; FOUND).

### § 7.1  CMB synth-track marker block (verbatim, L1480-1535)

~~~~
  #2 P11 SICF four strategic options
       (timing-sensitive; JTNB withdraw-and-resubmit window narrowing)
  #3 P-008 M9 V0 announcement draft
       (substrate ID'd; needs templates + M6 inconsistency resolved)
  #4 P-009 M8b positioning
       (provisional caveat ready; +042-exemplar to cite)

SUNDAY HANDOFF: synth previewed the W19 narrative arc and signaled
readiness for the handoff paste. CLI assembles cli_log/2026-W19.md
on Sunday (new SQL todo: w19-sunday-weekly-handoff-narrative-arc).

Synth: "Standing by."
CLI: standing by; no actions queued for this turn.

================================================================


================================================================
SYNTH-TRACK  2026-05-05 ~20:05 JST  RACI v2026-05-08 ABSORBED
================================================================

Three-AI-tier model now in effect. CLI is Tier 2 Synthesizer
(weekly + daily) plus Tier 3 Executer (daily) under operator's
effective deployment.

First Synthesizer-authored relay queue since cutover:

  043  RACI v2026-05-08 INSTALL              P0 Day-0
       Anchor instructions.txt + handoff doc to bridge.

  044  b(0)-offset Log sweep b1 in {5,8,9,10}  P1 synth #1
       Three-outcome gate; Outcome C => §4 E2 escalation.

  045  P-008 input package for MSB 2026-06   P1 synth #3
       Verbatim substrate; no advocacy.

CLI-internal (NOT in queue):
  - M6 ✅-vs-Phase-A/B.5 arbitration (in-tier; required for
    045 §7 substrate; pending verdict before 045 fires).
  - A.4 P-009 M8b caveat finalization.
  - A.2 P11 SICF four-options decision (timing-sensitive).
  - W19 closing handoff + W20 WSB by Sunday.
  - 2026-05_monthly_handoff.md by 2026-05-31.

Next milestone: M9 V0 substrate-ready for 2026-06-01 monthly
Strategyzer cycle. Roadmap below.

  W19 (now)        043 -> 044 (+045 parallel) -> in-tier
                   M6 arbitration + P-009 caveat
  W20 (May 11-17)  P11 SICF decision + daily loop
  W21 (May 18-24)  contingent on 044 outcome
  W22 (May 25-31)  monthly handoff draft
  2026-06-01       first formal Strategyzer monthly cycle

Bridge state at marker: 5d83797 (v3.1 push); origin/main aligned.
SQL state at marker:    66 pending / 3 in_progress / 142 done /
~~~~

### § 7.2  CMB M9 caveat profile excerpt (verbatim, L395-410)

~~~~
    dichotomy markers: 0 hits). M8b numerical revival
    remains foreclosed per 017d/017m verdicts; this
    finding confirms structural-only path forward.

  M9 (announcement-protocol meta-precedent):
    Sakai 1999 slot 13 verified as STRONG-FIT
    precedent for SIARC M9 announcement format
    (7-section partition with explicit deferrals
    "see § 7; 4"). Structurally closer to the SIARC
    M9 caveat profile (M1/M2/M3/M5/M6/M8 ✅ + M4
    partial + M7 soft + M8b foreclosed) than the
    Langlands 1967 letter to Weil (which is
    aesthetic-justification-only at announcement
    time per IAS author-commentary verbatim).
    Sakai 1999 = recommended template if SIARC-
    MASTER-V0 announcement fires.
~~~~

Source B: cli_log/2026-05-05.md  (S6_cli_log; FOUND).

### § 7.3  cli_log M6 arbitration upcoming-block (verbatim, L1220-1260)

~~~~
  - Goal: determine whether b₁=7 (8,−4,0,7,4)→3/log(2) outlier
    is structural-equivalence-theorem candidate or singular.

**045 P-008 input package for MSB 2026-06** (P1, synth-queue #3)
  - Path: `tex/submitted/control center/prompt/045_p008_input_package_for_msb_2026-06.txt` (12,649 B)
  - AEAL: SUBSTRATE-EXTRACTION
  - Strict verbatim discipline; no advocacy (rule6 guardrail
    via HALT_045_PACKAGE_INCLUDES_FRAMING grep self-check).
  - Substrate manifest of 7 sources (umbrella v2.0 §4, CT v1.3
    §Implications, M9 audit verdict 4ffcc8c, T2B v3.1 5d83797,
    main-thm working statement, M6 status, departing standing notes).

### CLI-Synthesizer in-tier upcoming (NOT relay-queue):

1. **M6 ✅-vs-Phase-A/B.5 arbitration verdict** — CLI in-tier;
   output to cli_log + CMB; required substrate for 045 §7.
2. **A.4 P-009 M8b caveat finalization** — text editing in-tier;
   absorb +042/Patch-6 as AEAL-relay-protocol exemplar citation.
3. **A.2 P11 SICF four-options decision** — synth-queue #2,
   timing-sensitive (JTNB withdraw-and-resubmit window).
4. **W19 closing handoff + W20 WSB** — by Sunday 2026-05-10
   per departing-Synthesizer standing notes.
5. **2026-05_monthly_handoff.md draft** — by 2026-05-31
   working-day; substrate for first monthly Strategyzer
   cycle 2026-06-01.

### Roadmap to next milestone (M9 V0 substrate-ready):

`
W19 (now)        043 → 044 (+045 parallel) → CLI in-tier
                 work on M6 arbitration + P-009 caveat
W20 (May 11-17)  P11 SICF decision; W20 daily relay loop
W21 (May 18-24)  if 044 Outcome B: tightened 044' at extended
                 corridor; otherwise routine cycles
W22 (May 25-31)  monthly handoff draft; final substrate chase
2026-06-01       Operator pastes monthly handoff + 4 weekly
                 handoffs + verdicts received → Strategyzer →
                 first MSB + Synthesizer Master Prompt
`

### rule5 grounding for this entry:
~~~~

Source C: cli_log/2026-W19_wsb.md  (S6_W19_wsb; FOUND, full body).

### § 7.4  W19 WSB (verbatim, full file)

~~~~
# Weekly Strategy Brief (WSB) — Week of 2026-05-05 → 2026-05-11
## SIARC Breakthrough Explorer
## Author: Synthesizer (Claude.ai)
## Cadence: weekly (per revised RACI v2026-05-05)

---

## Context snapshot (from CMB + portfolio map)

- 17 active journal submissions, 2 Zenodo preprints.
- Highest-likelihood active paper: **P08 Painlevé/V_quad at Nonlinearity (radar 8.0)**.
- Strongest theoretical+proved cluster: **P04 (JNT, 7.0), P08 (Nonlinearity, 8.0), P10 (JDE, 6.5)**.
- Mid-tier in MathComp zone: **P11 (Math.Comp, 6.0)** — has active blockers.
- Open computational frontier: **T2B-RESONANCE-B67** (extend Trans-stratum
  falsification to b₁ ∈ {6,7}).
- Open structural task: **CC-VQUAD-PIII-NORMALIZATION-MAP** (M6 leg, gates SIARC-MASTER-V0).
- Project north star: ONE accepted paper. Optimize for that, not for portfolio breadth.

## Strategic posture for this week

The portfolio has been *built out*. The bottleneck is no longer drafts — it
is (a) closing the highest-radar papers' last revision blockers and (b)
keeping the empirical conjecture pipeline producing ammunition for the next
two papers. With Synthesizer on weekly cadence, the week is structured so
that CLI + Copilot can run autonomously Mon–Fri while the Operator only
needs to make submission/withdrawal decisions on Sat.

**One-line strategy:** *Defend P08 and P11; extend T2B; keep M6 moving;
do not start anything new.*

---

## Top priorities (ranked)

1. **P08 (Nonlinearity, Painlevé/V_quad) — protect the asset.**
   Highest radar score in the portfolio. Run a fresh SICF pass this week and
   pre-draft a referee response template, so when the verdict lands we are
   ready within 48h.

2. **P11 (Math.Comp, F(2,4) base case) — close active blockers.**
   Mid-radar (6.0) but has the longest revision tail. Each open blocker is
   a known item; CLI should knock them down one per day Mon–Thu.

3. **T2B-RESONANCE-B67 — keep the empirical engine running.**
   Extend falsification test to b₁ ∈ {6,7}. This feeds the Transcendental
   Ratio Identity preprint and is the most likely source of the next
   genuinely novel result. Background-runnable; CLI dispatches to Copilot.

4. **CC-VQUAD-PIII-NORMALIZATION-MAP (M6 leg) — advance one phase.**
   Per `prompt_spec.md`, this gates SIARC-MASTER-V0. Not on the critical
   path for this week's paper outcomes, but one phase of progress per week
   keeps the M9 deadline reachable. Target: finish Phase A or Phase B.5
   this week.

5. **P10 (JDE) and P04 (JNT) — monitor only.**
   No action unless a verdict arrives. If a verdict does arrive, CLI
   triggers a same-day SICF pass and queues a Synthesizer escalation.

## Explicit non-goals this week

- Do NOT start a new paper draft.
- Do NOT submit anything new (P08/P11 already in flight; nothing else is
  SICF-ready).
- Do NOT touch P09 (AI Discovery, Notices AMS) unless a verdict arrives.
- Do NOT engage Claude in Chrome on submission portals (rule2).
- Do NOT generate any artifact requiring API keys (rule1).

---

## Daily slot allocation

| Day | Date | Primary | Secondary | Halt-if |
|---|---|---|---|---|
| Mon | 05-05 | P11 blocker #1 | T2B b₁=6 dispatch | P11 blocker requires math decision → escalate to Operator |
| Tue | 05-06 | P11 blocker #2 | T2B b₁=6 review | T2B finds counterexample → freeze, escalate |
| Wed | 05-07 | P08 SICF pass | T2B b₁=7 dispatch | SICF verdict ≠ PUBLISH-READY → log, continue |
| Thu | 05-08 | P11 blocker #3 | T2B b₁=7 review | Same |
| Fri | 05-09 | M6 Phase A or B.5 | P08 referee-response draft | M6 hits HALT_M6_* → log, do not retry this week |
| Sat | 05-10 | Operator review | Submission decisions if any | — |
| Sun | 05-11 | CLI weekly log → Synthesizer | — | — |

## End-of-week deliverables (CLI → Synthesizer for next WSB)

1. `cli_log/2026-W19.md` summarizing the 7 days.
2. P11 blocker tracker: how many of the 3 closed.
3. T2B-RESONANCE-B67 result for b₁ ∈ {6,7} (passes/fails, claim count).
4. P08 SICF report (4 radar scores + verdict).
5. M6 phase status update (which phase advanced; any halts).
6. Any verdicts received this week, transcribed into VERDICTS RECEIVED.
7. Recommended changes to next week's WSB (CLI's view of what to add/drop).

## Halt-and-escalate conditions (CLI → Operator → Synthesizer out-of-band)

- A T2B counterexample is found (would be paper-altering).
- An accept/major-revision verdict arrives on any P0x paper.
- SICF on P08 returns HOLD or MAJOR-REVISION (re-framing needed).
- Bridge repo SHA mismatch or AEAL claims minimum violated on any task.

---

## Notes for the Operator

- This week's load is mostly defensive (revisions, SICF, response drafts) +
  one empirical extension (T2B). It is engineered to need ~30 minutes/day
  of your time: paste CLI's relay prompt into Copilot, paste Copilot's
  output back into CLI, glance at the daily log.
- Saturday is the only day you actively decide anything. If no verdicts
  arrived, Saturday is a no-op.
- If at any point this plan feels wrong, re-engage Synthesizer
  out-of-band — but the design assumption is that a re-engagement before
  Sunday is a sign something genuinely changed (verdict, counterexample,
  halt) rather than a routine course-correction.

~~~~

### § 7.5  M6 arbitration verdict status

A CLI-Synthesizer arbitration verdict for the M6 (checkmark)-vs-Phase-A/B.5
inconsistency between the 038 caveat profile and the W19 WSB has NOT been
written to cli_log/2026-05-05.md or cli_log/2026-W19_wsb.md as of the
compile timestamp recorded above (grep for "arbitration verdict" /
"M6 verdict" / "Phase A" / "Phase B.5" within those two files returns
only forward-references to the pending in-tier work; cf. cli_log L1234
verbatim: "M6 (checkmark)-vs-Phase-A/B.5 arbitration verdict - CLI in-tier;
output to cli_log + CMB; required substrate for 045 § 7.").

PENDING SYNTHESIZER ARBITRATION (in-tier, expected by 2026-W20).

---

## § 8  Departing-Synthesizer's three standing notes (verbatim, S7 § E)

Source: tex/submitted/control center/synthesizer_inbox/STRATEGYZER_HANDOFF_2026-05-08.md  (S7; FOUND).

~~~~markdown
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

~~~~

---

## § 9  AEAL provenance

- Substrate manifest SHA-256: 34A60B517475559C3EFC87264C1A3D5724ECD2D892F5FDCC31FF31A5436BB2F9
- Compile script (build_package.py) SHA-256: FB68744B04E6D2905A1EC824D12B6114D87BDE9444D981502923D254F46CE38E
- Per-source SHA-256, size, and mtime: see § 1 manifest.
- Claim entries: claims.jsonl in this session directory.

---

End of P-008 input package.
