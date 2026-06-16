\section{The main identity and its normalisation}\label{sec:main}

We now assemble Sections~\ref{sec:operators}--\ref{sec:cycle} into the main theorem and fix, once
and for all, the normalisation by which the raw thimble integral yields the connection
coefficient. The numerical values quoted are from the deposited V\_quad data~\cite{Vquad,StokesNote}
and the slot \texttt{PERIOD-REP-VQUAD-001} (\texttt{numerical-check.md}).

\subsection{Statement}
\begin{theorem}[Main identity, restated]\label{thm:main-restated}
With $\Bhat$, $\LV$, $\gamma$, $\beta$ and $K$ as above,
\begin{equation}\label{eq:main-again}
  \C\;=\;\frac{\lvert\Gamma(\beta)\rvert}{2\pi}\int_{\gamma}e^{\xi}\,\Bhat(\xi)\,d\xi
  \;=\;\lvert\Gamma(\beta)\rvert\cdot K ,
\end{equation}
where the raw thimble integral equals $S\,e^{-\xizero}$ at leading order, $S=2\pi K$ is the
V\_quad Stokes constant, and $\lvert\Gamma(\beta)\rvert/2\pi$ is the explicit algebraic-$\Gamma$
reweighting. Equivalently, recentring the potential on the singularity
(an admissible $\mathbb{G}_a$-translation $f\mapsto f-\xizero$),
\begin{equation}\label{eq:main-recentred}
  \int_\gamma e^{\xi+\xizero}\,\Bhat(\xi)\,d\xi\;=\;S,\qquad
  \C\;=\;\frac{\lvert\Gamma(\beta)\rvert}{2\pi}\,S .
\end{equation}
\end{theorem}

The two forms~\eqref{eq:main-again} and~\eqref{eq:main-recentred} are equivalent: the constant
$e^{\xizero}$ is the value of the action factor $e^{-f}=e^{\xi}$ at the dominant point $-\xizero$,
and translating the potential $f\mapsto f-\xizero$ (a $\mathbb{G}_a$-shift, admissible in the
Fres\'an--Jossen formalism since it changes $E^{-f}$ by the constant rank-one factor
$E^{\xizero}$) multiplies the integrand by $e^{\xizero}$, absorbing it. We adopt the
recentred~\eqref{eq:main-recentred} as the headline so that the raw period is exactly $S$ and the
connection coefficient is its explicit algebraic-$\Gamma$ reweighting; the un-recentred
form~\eqref{eq:main-again} makes the action $e^{-\xizero}$ visible. Both are recorded so that no
reader mistakes the raw thimble value $S\,e^{-\xizero}$ for $\C$ itself.

\subsection{Where the \texorpdfstring{$\Gamma(\beta)$}{Gamma(beta)} factor comes from}
The factor is not inserted by hand: it is produced by the branch integral around $-\xizero$.
Writing $\eta=\xi+\xizero$ and using the local form~\eqref{eq:branch-local}, the discontinuity
integral~\eqref{eq:disc} is a Hankel loop integral for the reciprocal $\Gamma$-function,
\begin{equation}\label{eq:hankel-gamma}
  \frac{1}{2\pi i}\oint_{H}e^{\eta}\,\eta^{-(1+\beta)}\,d\eta=\frac{1}{\Gamma(1+\beta)}
  \qquad(\text{\cite[\S5.9]{DLMF}, \cite[\S12.22]{WW}}),
\end{equation}
so the amplitude of the period is $A=(S/2\pi i)\,\Gamma(1+\beta)$, i.e.
$\lvert A\rvert=K\,\Gamma(1+\beta)$. The connection coefficient is the branch datum reweighted by
the exponent,
\begin{equation}\label{eq:C-from-A}
  \C=\frac{\lvert A\rvert}{\lvert\beta\rvert}=\frac{K\,\Gamma(1+\beta)}{\lvert\beta\rvert}
   =K\,\lvert\Gamma(\beta)\rvert ,
\end{equation}
the last equality using $\Gamma(1+\beta)=\beta\,\Gamma(\beta)$ together with $\beta<0$ and
$\Gamma(\beta)<0$ on $(-1,0)$, so that $\Gamma(1+\beta)/\lvert\beta\rvert
=\beta\Gamma(\beta)/(-\beta)=-\Gamma(\beta)=\lvert\Gamma(\beta)\rvert$. Thus the only
non-algebraic factor manufactured by the
integral is a single value of the $\Gamma$-function at the algebraic argument
$\beta=-1/(3\sqrt3)\in\Qsqrt$; everything else---$\Bhat$, $\LV$, the cut, the cycle---is algebraic
over $\Qsqrt$. This is exactly the shape an exponential period should take.

\subsection{The constants}
\begin{equation}\label{eq:constants}
\begin{aligned}
  K&=0.0728781025518669641294423633296525128045556892\ldots\quad(\text{58 digits, \cite{Vquad}}),\\
  S&=2\pi K=0.457906623169017636119097842548225837962395135\ldots,\\
  \beta&=-1/(3\sqrt3)=-0.19245008972987525\ldots,\qquad \xizero=2/\sqrt3=1.1547005383792517\ldots,\\
  \C&=\lvert\Gamma(\beta)\rvert\,K=0.437705286193537221230739749794369589981725597\ldots .
\end{aligned}
\end{equation}
The bridge identity $S/\C=2\pi/\lvert\Gamma(\beta)\rvert$ holds with residual $0$ (exact, not
numerical): both sides are $2\pi/\lvert\Gamma(\beta)\rvert$ by~\eqref{eq:main-again}.

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

\subsection{Numerical confirmation}
The identity~\eqref{eq:main-again} is confirmed numerically to $46$ significant digits by the
contour evaluation (Method~B) and the Stokes-data evaluation (Method~C) of
Section~\ref{sec:verif}; the differential-equation route (Method~A) confirms the same identity
\emph{exactly} at the operator level (no numerical integration). The worst relative error across
the numerical methods is $9.31\times10^{-46}$
(\texttt{PERIOD-REP-VQUAD-003}, \texttt{numerical-integral.md} and
\texttt{cross-verification.md}). We turn to the three verifications next.
