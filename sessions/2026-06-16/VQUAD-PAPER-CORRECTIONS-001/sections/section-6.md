\section{Application to Fres\'an--Jossen and conditional transcendence}\label{sec:fj}

We now interpret the verified identity~\eqref{eq:main-again} inside the Fres\'an--Jossen theory of
exponential motives and deduce the conditional transcendence of $\C$. We are deliberately explicit
about \emph{both} layers of conditionality: the Fres\'an--Jossen period conjecture itself, and a
motivic-comparison hypothesis we label G-MOTGALOIS. Sources: \cite{FJ}, and the slot deliverables
\texttt{fj-application.md}, \texttt{galois-LV-verification.md}, \texttt{fresan-jossen-axioms.md}.

\subsection{$\C$ as an exponential period}
\begin{proposition}[$\C$ is a period of an exponential motive]\label{prop:expperiod}
The datum $(X,f,\omega,\gamma)$ with
\[
  X=\mathbb{A}^1_\xi\smallsetminus\{0,-\xizero\}\ \text{over }\Qsqrt,\qquad f=-\xi,\qquad
  \omega=\Bhat(\xi)\,d\xi,\qquad \gamma\ \text{as in Definition~\ref{def:gamma}},
\]
satisfies the Fres\'an--Jossen axioms: $\omega$ is algebraic over the number field $\Qsqrt$
(Theorem~\ref{thm:LV}), $f$ is regular with $df=-d\xi$ nowhere zero (no finite critical point),
and $\gamma$ is a rapid-decay cycle (Proposition~\ref{prop:rapiddecay},
Proposition~\ref{prop:fjclass}). Consequently $\int_\gamma e^{\xi}\Bhat\,d\xi$ is a period of the
exponential motive $H^1\bigl(\mathbb{A}^1\smallsetminus\{0,-\xizero\},\nabla\bigr)$ attached to
$(X,f,\omega)$, and by~\eqref{eq:main-again} so is $\C=(\lvert\Gamma(\beta)\rvert/2\pi)\int_\gamma
e^{\xi}\Bhat\,d\xi$.
\end{proposition}

The auxiliary Fres\'an--Jossen condition most easily overlooked---the structure of the critical
locus of $f$---is here the most favourable possible: $f=-\xi$ is linear, so $X$ carries \emph{no}
interior critical point and the motive is a single $E^{-f}\otimes(\text{rank-}4\ \text{algebraic})$
with no extra vanishing-cycle contributions; the only critical value at infinity is the slope-$1$
irregularity (Proposition~\ref{prop:exponents}).

\subsection{The period conjecture and the Galois input}
To an exponential motive $M$, Fres\'an--Jossen attach a motivic Galois group $G_{\mathrm{mot}}(M)$,
making the period torsor a $G_{\mathrm{mot}}$-torsor; their period conjecture
(\cite{FJ}, Conjecture~1.3.2) is the exponential-motives analogue of Grothendieck's:
\begin{equation}\label{eq:periodconj}
  \operatorname{trdeg}_{\mathbb{Q}}\mathbb{Q}\bigl(\text{periods of }M\bigr)
  =\dim G_{\mathrm{mot}}(M).
\end{equation}
The Fres\'an--Jossen category of exponential motives is Tannakian over $\mathbb{Q}$; an
exponential motive $M$ generates a Tannakian subcategory $\langle M\rangle$ with affine group
scheme $G_{\mathrm{mot}}(M)=\underline{\mathrm{Aut}}^{\otimes}(\omega_M)$, and the comparison
between the Betti (rapid-decay) and de Rham realisations is a torsor under $G_{\mathrm{mot}}(M)$
whose period matrix has the periods of $M$ as entries. Conjecture~\eqref{eq:periodconj} is the
statement that this period torsor is connected---equivalently, that the periods are as
algebraically independent as the Tannakian formalism permits. For the motive $M$ of
Proposition~\ref{prop:expperiod} the relevant realisations are computed by the differential systems
$\Lphi,\LV$.

The differential-Galois data of Sections~\ref{sec:operators}--\ref{sec:verif} compute the de Rham
realisation of (a quotient of) $G_{\mathrm{mot}}(M)$:
\begin{itemize}[leftmargin=1.4em,itemsep=2pt]
  \item $\Lphi$ (order $2$, regular side) has differential Galois group $\SL_2(\mathbb{C})$
        (Theorem~\ref{thm:galois});
  \item $\LV$ (order $4$, Borel dual) has Galois group $G_V$ containing a torus $\Gm$---from the
        irrational branch exponent $-1+\sqrt3/9$ at $-\xizero$, whose monodromy eigenvalue
        $e^{2\pi i\sqrt3/9}$ has infinite order---together with the exponential/Stokes data at
        $\infty$ (formal torus $\times$ nontrivial unipotent Stokes, the $\SL_2$-dual structure);
  \item $\C$ is the Galois-equivariant pairing $\langle[\gamma]_{\mathrm{rd}},[\omega]_{\mathrm{dR}}\rangle$,
        with the exponential period $2\pi i$ of $E^{\xi}$ and the branch normalisation
        $1/\Gamma(1+\beta)$ as the two torus generators (Method~C, \eqref{eq:methodC}).
\end{itemize}
Because $G_V$ carries both a non-abelian $\SL_2$-type part and a transcendental-monodromy torus
$\Gm$ with irrational character, the motivic Galois group is positive-dimensional and acts
nontrivially on the class pairing defining $\C$: there is no $1$-dimensional sub-torsor forcing $\C$
to be algebraic, and no algebraic relation of $\C$ with the base period $1$ is visible.

Concretely, the period pairing between the rapid-decay Betti class $[\gamma]$ and the de Rham class
$[\omega]=[\Bhat\,d\xi]$, together with the unit and the exponential-torus generators, assembles
into the period matrix
\begin{equation}\label{eq:periodmatrix}
  P(M)=\begin{pmatrix} 1 & 0\\[2pt] \dfrac{1}{\Gamma(1+\beta)} & 2\pi i\end{pmatrix},
  \qquad \det P(M)=2\pi i,
\end{equation}
whose entries are exactly the constants appearing in Method~C, \eqref{eq:methodC}: the determinant
$2\pi i$ is the exponential-torus period of $E^{\xi}$, the off-diagonal $1/\Gamma(1+\beta)$ is the
branch normalisation at $-\xizero$, and the connection coefficient
$\C=\lvert\Gamma(\beta)\rvert K=\lvert A\rvert/\lvert\beta\rvert$ is the period pairing assembled
from these entries via the branch amplitude $\lvert A\rvert=K\,\Gamma(1+\beta)$, not itself an
entry of $P(M)$. The transcendence
of $\C$ is the statement that this matrix is not gauge-equivalent over $\Qbar$ to a block-diagonal
(algebraic) one---precisely what the period conjecture controls.

\subsection{The comparison gap G-MOTGALOIS}
The identification of the de Rham realisation $G_V$ with the relevant quotient of
$G_{\mathrm{mot}}(M)$ uses the standard de Rham-realisation comparison; the full Nori/Ayoub
exponential-motive comparison for this \emph{specific} $M$ is \emph{assumed}, not verified here.

\begin{quote}
\textbf{Hypothesis (G-MOTGALOIS).} The de Rham/differential Galois group $G_V$ computed in
Sections~\ref{sec:operators}--\ref{sec:verif} represents the motivic Galois group
$G_{\mathrm{mot}}(M)$ of the exponential motive $M=(X,f,\omega)$ of
Proposition~\ref{prop:expperiod}; in particular $\dim G_{\mathrm{mot}}(M)\ge1$ and $\C$ is not
fixed by $G_{\mathrm{mot}}(M)$.
\end{quote}

This is a conjectural bridge; it affects only the motivic \emph{interpretation}, not any of the
differential or numerical computations above. We flag it explicitly so that the transcendence
corollary is never mistaken for unconditional.

\subsection{Conditional transcendence}
\begin{proof}[Proof of Corollary~\ref{cor:transc}]
By Proposition~\ref{prop:expperiod}, $\C$ is a period of $M$. Assume \emph{(i)} the
Fres\'an--Jossen period conjecture~\eqref{eq:periodconj} and \emph{(ii)} the hypothesis
G-MOTGALOIS. By (ii), $\dim G_{\mathrm{mot}}(M)\ge1$ and $\C$ is not fixed by
$G_{\mathrm{mot}}(M)$, so $\C$ does not lie in the algebraic ($G_{\mathrm{mot}}$-invariant)
part of the period algebra. By (i), every $\mathbb{Q}$-polynomial relation among the periods of
$M$ is of motivic origin, so a non-invariant period satisfies no algebraic relation over
$\Qbar$. Hence $\C$ is transcendental over $\Qbar$.
\end{proof}

\begin{remark}[The conjecture, specialised]\label{rmk:specialised}
Concretely, Proposition~\ref{prop:expperiod} and the Galois input make the period
algebra of $M$ contain $1$, $2\pi i$, $\Gamma(1+\beta)$ and $\C$; the de Rham realisation $G_V$ is
positive-dimensional (it contains the torus $\Gm$ acting through the irrational character
$\sqrt3/9$ and an $\SL_2$-type Stokes part). The period conjecture~\eqref{eq:periodconj} predicts
$\operatorname{trdeg}_{\mathbb{Q}}$ of this algebra equals $\dim G_{\mathrm{mot}}(M)$, which under
G-MOTGALOIS is $\ge1$ with $\C$ outside the invariants; equality at any value $\ge1$ already forces
$\C\notin\Qbar$. The statement is thus robust to the precise value of $\dim G_{\mathrm{mot}}(M)$:
only positivity and non-invariance of $\C$ are used, not the exact dimension.
\end{remark}

\begin{remark}[What is unconditional, and what is not]\label{rmk:uncond}
Independently of Fres\'an--Jossen, $\C=\lvert\Gamma(\beta)\rvert\,K$ with
$\beta=-1/(3\sqrt3)\notin\mathbb{Q}$. The factor $\lvert\Gamma(\beta)\rvert$ is a value of
$\Gamma$ at an algebraic-irrational argument (transcendence of such values is itself only known
conditionally in general; \cite{Nesterenko} settles the classical rational-argument and modular
cases), while the transcendence of $K$ remains conjectural. Thus the \emph{product} $\C$ is only
\emph{expected} transcendental by ad-hoc $\Gamma$-arithmetic. The value of the Fres\'an--Jossen
route is that it upgrades the \emph{whole} of $\C$ to a single structured conditional statement,
tied to the motivic Galois group rather than to $\Gamma$-arithmetic of one factor. We do not
collapse this into an unconditional claim.
\end{remark}
