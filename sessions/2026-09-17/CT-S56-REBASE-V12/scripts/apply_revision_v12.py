#!/usr/bin/env python
r"""CT-S56 Stage 3: apply CT-S52's four items plus item 5 to a COPY of the v1.2
source (the file LMP holds).

Design rules, each of them the residue of a defect found earlier in this run:

* CT-S52's 19 replacements are IMPORTED from its own apply_revision.py, never
  transcribed, so they cannot drift from what that session applies.
* Every replacement must match EXACTLY ONCE. A pattern matching zero times is a
  silent no-op and a pattern matching twice edits the wrong place.
* The whole buffer is validated BEFORE anything is written. A post-write check
  leaves the corrupt artefact on disk.
* The v1.2 source is re-read after writing and required to be byte-unchanged.

Exit codes: 0 clean / 1 finding / 2 refusal / 3 crash.
"""
import hashlib
import importlib.util
import io
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SESS = HERE.parent
REFS = SESS / "refs"
OUT = SESS / "outputs" / "apply_revision_v12.out.txt"
ROOT = SESS.parents[2]

SRC = REFS / "src-v1.2" / "vquad-periodrep-paper.tex"
DSTDIR = SESS / "revision"
DST = DSTDIR / "vquad-periodrep-paper.tex"
S52 = ROOT / "sessions/2026-09-17/CT-S52-XI0-LOGS-REVISION/scripts/apply_revision.py"

BUF = io.StringIO()


def say(s=""):
    print(s)
    BUF.write(s + "\n")


class Refuse(Exception):
    pass


# =====================================================================
# ITEM 5 -- Methods B and C are not independent as printed.
# Substance from CT-S54 (claims S54-01..S54-06); figures 8.84482e-46,
# 9.31344e-46 and 3.68728e-46 are that session's measured values.
# =====================================================================
EXTRA4 = []


def rep4(tag, old, new):
    EXTRA4.append(("4", tag, old, new))


# --------------------------------------------------------------------------
# Operator ruling, 2026-09-21: L455 belongs to item 4, not to a sixth item.
#
# Proposition 2.4 closes "Both statements are obtained twice, by a
# falling-factorial indicial computation and by direct solution of the
# Frobenius recurrence AT -xi0". The second route was run only at -xi0. The two
# statements are (i) the exponents at xi=0 with apparency there and (ii) the
# branch at -xi0. So the apparency statement at 0 was obtained ONCE, by an
# inference CT-S52 has since shown to be false: the sentence claims two
# confirmations for a result that had zero valid ones.
#
# In the revision it is additionally self-contradictory: item 4's new text,
# three sentences earlier in the SAME proposition, states that xi=0 does carry
# a logarithm, while "(no logarithms)" still sweeps both points in.
#
# The replacement says what each route actually covered.
# --------------------------------------------------------------------------
rep4("Prop 2.4 closing: 'Both statements are obtained twice' "
     "(operator ruling: same shape as item 3, inside item 4's scope)",
     "$A$. Both statements are obtained twice, by a falling-factorial indicial "
     "computation and by direct\nsolution of the Frobenius recurrence at "
     "$-\\xizero$ (residuals $1.6\\times10^{-46}$, no\nlogarithms); see "
     "Appendix~\\ref{app:numlogs}.",
     "$A$. The exponents at both points come from a falling-factorial indicial\n"
     "computation. Direct solution of the Frobenius recurrence was carried out at "
     "each\npoint separately, and the two runs do not say the same thing: at "
     "$-\\xizero$ it\nconfirms the absence of logarithms (residuals "
     "$1.6\\times10^{-46}$), while at $\\xi=0$ it\nproduces the obstruction "
     "recorded above and a logarithmic fourth solution. The\napparency previously "
     "asserted at $\\xi=0$ rested on the indicial computation alone;\nno second "
     "route confirmed it, and the inference from consecutive integer exponents\n"
     "to apparency is invalid. See Appendix~\\ref{app:numlogs}.")


FIVE = []


def rep5(tag, old, new):
    FIVE.append(("5", tag, old, new))


rep5("abstract: 'three structurally independent methods'",
     r"""The identity is verified by
three structurally independent methods---differential-equation/operator duality, Borel--Laplace
contour deformation, and Stokes-data---agreeing to $46$ digits.""",
     r"""The identity is verified
three ways---differential-equation/operator duality, Borel--Laplace
contour deformation, and Stokes-data---agreeing to $46$ digits; the latter two share the branch
amplitude $A$ and are not mutually independent (\S\ref{sub:cross}).""")

rep5("1.3 main results: 'three independent ways'",
     r"""We exhibit $\C$ as an explicit exponential-period integral and verify the identity three
independent ways.""",
     r"""We exhibit $\C$ as an explicit exponential-period integral and verify the identity three
ways.""")

rep5("Theorem 1.1: 'three structurally independent methods'",
     r"""The identity is
verified by three structurally independent methods---differential-equation/operator duality,
Borel--Laplace/Hankel, and Stokes-data---which agree to $46$ significant digits
(Section~\ref{sec:verif}).""",
     r"""The identity is
verified by three computations---differential-equation/operator duality,
Borel--Laplace/Hankel, and Stokes-data---which agree to $46$ significant digits
(Section~\ref{sec:verif}); Methods~B and~C share the branch amplitude $A$, so the three are not
mutually independent (Section~\ref{sub:cross}).""")

rep5("5 preamble: 'three structurally independent ways' / 'disjoint inputs'",
     r"""We verify~\eqref{eq:main-again} three structurally independent ways: an exact
differential-equation/operator computation (Method~A, \S\ref{sub:methodA}), a contour evaluation
producing the $\Gamma$-factor in closed form (Method~B, \S\ref{sub:methodB}), and a Stokes-data
computation that never touches $\gamma$ (Method~C, \S\ref{sub:methodC}). The three use disjoint
inputs and agree to $46$ digits (\S\ref{sub:cross}).""",
     r"""We verify~\eqref{eq:main-again} three ways: an exact
differential-equation/operator computation (Method~A, \S\ref{sub:methodA}), a contour evaluation
producing the $\Gamma$-factor in closed form (Method~B, \S\ref{sub:methodB}), and a Stokes-data
computation that never touches $\gamma$ (Method~C, \S\ref{sub:methodC}). Method~A is exact and
symbolic; Methods~B and~C are numerical and agree to $46$ digits. They do \emph{not} use disjoint
inputs: both require the branch amplitude $A$, and what each is and is not independent of is
stated in \S\ref{sub:strategy} and summarised in Table~\ref{tab:methods}.""")

rep5("5.1 strategy: heading and the 'disjoint inputs' premise",
     r"""\subsection{Strategy: why three methods, and why they are independent}\label{sub:strategy}
A single numerical coincidence to $46$ digits is suggestive but not a proof; what upgrades it is
that the three checks draw on \emph{disjoint} mathematical inputs, so a hidden error in any one
construction cannot be common to all three.""",
     r"""\subsection{Strategy: why three methods, and what each is independent of}\label{sub:strategy}
A single numerical coincidence to $46$ digits is suggestive but not a proof; what upgrades it is
the extent to which the checks draw on different mathematical inputs. That extent is not total,
and we state it precisely rather than assert disjointness: Methods~B and~C both require the
branch amplitude $A$. If $A$ is taken from the Stokes datum $S$, as the displayed derivation
in~\eqref{eq:methodB-chain} does, then B and C are two readings of one quantity and their
agreement is not evidence of two determinations. Method~B is therefore quoted below on the
amplitude extracted from the large-order coefficient data, which does not use $S$.""")

rep5("5.1 Method A bullet: independence inferred, not measured",
     r"""value of $\C$; it certifies that the parameter-deformed integral $I_\gamma(z)$ \emph{solves
$\Lphi$}, fixing the differential structure of the period.""",
     r"""value of $\C$; it certifies that the parameter-deformed integral $I_\gamma(z)$ \emph{solves
$\Lphi$}, fixing the differential structure of the period. Its independence from B and C is
\emph{inferred} from its being exact and symbolic over $\Qsqrt$---it consumes no numerical
quantity that B or C could contaminate---and has not been established by a perturbation test, as
the relation between B and C has.""")

rep5("5.1 Method B bullet: name the amplitude dependence",
     r"""produces the closed-form leading period $S\,e^{-\xizero}$ analytically, using the analytic
structure of $\Bhat$ but \emph{not} the operators.""",
     r"""produces the closed-form leading period $S\,e^{-\xizero}$ analytically, using the analytic
structure of $\Bhat$ but \emph{not} the operators. It does, however, require the branch amplitude
$A$: taken from the large-order coefficient data this is independent of $S$, taken from $S$ it is
not.""")

rep5("5.3 methodB chain: name where S enters",
     r"""The cancellation that produces~\eqref{eq:methodB-period} is worth displaying, since it is the heart
of the $\Gamma$-factor mechanism. Substituting $A=(S/2\pi i)\,\Gamma(1+\beta)$ and using
\eqref{eq:hankel-gamma},""",
     r"""The cancellation that produces~\eqref{eq:methodB-period} is worth displaying, since it is the heart
of the $\Gamma$-factor mechanism. Substituting $A=(S/2\pi i)\,\Gamma(1+\beta)$---the step at which
the Stokes datum enters Method~B, and the reason the closed form alone does not constitute a check
independent of $S$---and using \eqref{eq:hankel-gamma},""")

rep5("5.3 methodB: the error figure and the independence sentence",
     r"""by~\eqref{eq:C-from-A}. Numerically (script \texttt{stage4\_methods.py}, Method~B block,
$\to$ \texttt{stage4\_methods\_results.json}, \texttt{mpmath}) the closed form
matches the directly summed Borel data with relative error
\begin{equation}\label{eq:methodB-err}
  \text{rel.\ err}=8.84\times10^{-46}.
\end{equation}
Method~B is independent of the Stokes datum: it \emph{derives} $S\,e^{-\xizero}$ from the cycle and
the branch exponent, rather than assuming $S$.""",
     r"""by~\eqref{eq:C-from-A}.

Two distinct numerical statements must be separated here, because earlier versions of this paper
conflated them. \emph{First}, if $A$ is substituted from $S$ as above, the resulting comparison
reduces algebraically to the identity $\lvert S_{\mathrm{mult}}\rvert=2\pi K$ of
Method~C---the factor $e^{-\xizero}$ cancels from both sides---and returns that method's figure,
$8.84\times10^{-46}$. It is the same quantity as Method~C's, not a second measurement of it.
\emph{Second}, the amplitude can instead be extracted from the coefficient
stream~\eqref{eq:coeffstream} with no reference to $S$, by Neville acceleration of
$A_m=b_m(-1)^m\Gamma(1+\beta)\,m!\,\xizero^{\,m+1+\beta}/\Gamma(m+1+\beta)$ on a window near order
$820$ (\texttt{PERIOD-REP-VQUAD-003}, Stage~1.4, \texttt{numerical-integral.md}~\S2), which
self-converges to $85.96$ digits. Rebuilt on that amplitude, Method~B reconstructs the deposited
Stokes constant to
\begin{equation}\label{eq:methodB-err}
  \text{rel.\ err}=3.69\times10^{-46},
\end{equation}
and \emph{this} is the check that is independent of $S$. It is the figure quoted for Method~B in
Table~\ref{tab:methods}. What Method~B establishes, then, is that the cycle and the branch
exponent together with an amplitude read off the large-order coefficients reproduce $S$; it does
not, by itself, determine $S$ without an amplitude.""")

rep5("5.5 prop:cross: 'disjoint inputs'",
     r"""Methods~A, B, C all confirm the single identity~\eqref{eq:main-again}; none contradicts. They use
disjoint inputs---exact operators over $\Qsqrt$ (A), the rapid-decay contour and branch exponent
(B), the Stokes constant and large-order amplitude (C)---yet land on the same branch datum $A$ and
the same $\Gamma$-factor $\Gamma(1+\beta)$. The numerical agreement is to $46$ digits, with worst
relative error $9.31\times10^{-46}$.""",
     r"""Methods~A, B, C all confirm the single identity~\eqref{eq:main-again}; none contradicts. Their
inputs are not disjoint: Method~A uses the exact operators over $\Qsqrt$ and no numerical
quantity, but Methods~B and~C both require the branch amplitude $A$ and the $\Gamma$-factor
$\Gamma(1+\beta)$. What the numerics establish is therefore two distinct facts rather than three
independent confirmations: the identity $\lvert S_{\mathrm{mult}}\rvert=2\pi K$, to
$8.84\times10^{-46}$ (reported by Method~C, and recovered by Method~B when its amplitude is taken
from $S$); and $\C=\lvert\Gamma(\beta)\rvert K$, to $9.31\times10^{-46}$, which is insensitive to
$S$. Independently of both, Method~B on the large-order amplitude reconstructs $S$ to
$3.69\times10^{-46}$ without using it. Method~A's agreement is exact and symbolic.""")

rep5("Table 2: row B 'Independent of' and its figure",
     r"""B (Borel--Laplace) & Hankel $\Rightarrow$ leading period $S e^{-\xizero}$ & the Stokes datum & $8.84\times10^{-46}$ \\""",
     r"""B (Borel--Laplace) & Hankel $\Rightarrow$ leading period $S e^{-\xizero}$ & the operators & $3.69\times10^{-46}$ \\""")

rep5("Table 2 caption: record the shared amplitude",
     r"""\caption{The three verifications of~\eqref{eq:main-again}. Source:
\texttt{cross-verification.md}, \texttt{PERIOD-REP-VQUAD-003}.}""",
     r"""\caption{The three verifications of~\eqref{eq:main-again}. Methods~B and~C both require the
branch amplitude $A$ and are not mutually independent; the figure quoted for~B is the
reconstruction of $S$ from the large-order amplitude, which does not use $S$. Source:
\texttt{cross-verification.md}, \texttt{PERIOD-REP-VQUAD-003}.}""")

rep5("5.5 closing: 'spurious triple coincidence'",
     r"""Borel--Laplace duality, not a contradiction: B fixes the value, A fixes the ODE. The probability of
a spurious triple coincidence at $46$ digits, with the unique correct operator-sign convention of
four, is negligible; we record the result as \textbf{verified}.""",
     r"""Borel--Laplace duality, not a contradiction: B fixes the value, A fixes the ODE. The probability of
a spurious coincidence at $46$ digits between the exact symbolic computation of Method~A and the
two numerical determinations above, with the unique correct operator-sign convention of four, is
negligible; we record the result as \textbf{verified}.""")


def import_s52():
    if not S52.exists():
        raise Refuse(f"CT-S52 apply_revision.py not found: {S52}")
    spec = importlib.util.spec_from_file_location("s52_apply2", S52)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["s52_apply2"] = mod
    spec.loader.exec_module(mod)
    R = getattr(mod, "R", None)
    if not R:
        raise Refuse("CT-S52 exposed no replacement list R")
    return [(i, t, o.replace("\r\n", "\n"), n.replace("\r\n", "\n")) for i, t, o, n in R]


def all_replacements():
    """The single source of truth for what this revision changes.

    make_docs.py, render_diff.py and emit_claims_s56.py all need this list.
    It is a function rather than three separate reconstructions because the
    L455 item-4 edit was added to main()'s `allreps` and NOT to make_docs.py's
    own `s52 + FIVE`, so the two disagreed by exactly one and the documents
    reported 32 replacements where 33 had been applied. One list, one count.
    """
    return import_s52() + EXTRA4 + FIVE


def main():
    say("=" * 78)
    say("CT-S56 STAGE 3 -- apply items 1-4 (CT-S52) and item 5 to the v1.2 source")
    say("=" * 78)
    say("")

    if not SRC.exists():
        raise Refuse(f"v1.2 source not staged: {SRC}")
    before = SRC.read_bytes()
    say(f"base source   : refs/src-v1.2/vquad-periodrep-paper.tex")
    say(f"base sha256   : {hashlib.sha256(before).hexdigest()}")
    text = before.decode("utf-8")
    crlf = "\r\n" in text
    body = text.replace("\r\n", "\n")
    say(f"line endings  : {'CRLF' if crlf else 'LF'}")
    say("")

    s52 = import_s52()
    say(f"CT-S52 replacements imported : {len(s52)}")
    say(f"item 5 replacements defined  : {len(FIVE)}")
    say(f"item 4 additions (L455)      : {len(EXTRA4)}")
    say("")

    allreps = all_replacements()

    # ---- validate EVERY pattern against the ORIGINAL buffer before writing ----
    say("[1] PRE-APPLICATION VALIDATION (all patterns, before anything is written)")
    bad = 0
    for item, tag, old, new in allreps:
        n = body.count(old)
        mark = "ok" if n == 1 else "REFUSE"
        say(f"    item {item:<2} [{mark:^6}] matches={n}  {tag[:56]}")
        if n != 1:
            bad += 1
    if bad:
        say("")
        say(f"REFUSED: {bad} pattern(s) did not match exactly once. Nothing written.")
        return 2
    say("")
    say(f"    all {len(allreps)} patterns match exactly once.")
    say("")

    # ---------------------------------------------------------- apply in order
    say("[2] APPLYING")
    out = body
    for item, tag, old, new in allreps:
        if out.count(old) != 1:
            raise Refuse(
                f"item {item} ({tag}): pattern no longer matches exactly once after "
                "earlier edits -- two replacements overlap")
        out = out.replace(old, new, 1)
    say(f"    {len(allreps)} replacements applied.")
    say("")

    # ------------------------------------------------- post-condition on buffer
    say("[3] BUFFER CHECKS (still before writing)")
    if out == body:
        raise Refuse("revised buffer is identical to the base -- no edit took effect")
    for item, tag, old, new in allreps:
        if new not in out:
            raise Refuse(f"item {item} ({tag}): replacement text absent from the buffer")
    say("    revised buffer differs from base            : yes")
    say("    every replacement's new text present        : yes")
    nb = out.count(r"\bibitem{")
    ob = body.count(r"\bibitem{")
    say(f"    bibitems base={ob}  revised={nb}  (expected +1)")
    if nb != ob + 1:
        raise Refuse(f"bibliography changed by {nb-ob}, expected exactly +1")
    # the new entry must be the LAST one, so v1.2's numbering is untouched
    tail = out[out.rfind(r"\bibitem{"):]
    if "VquadV13" not in tail:
        raise Refuse("the added bibitem is not the final entry; v1.2 numbering would shift")
    say("    new bibitem is the final entry              : yes (numbering preserved)")
    say("")

    # ------------------------------------------------------------------ write
    DSTDIR.mkdir(parents=True, exist_ok=True)
    for extra in ("preamble.tex", "build.py"):
        s = REFS / "src-v1.2" / extra
        if s.exists():
            (DSTDIR / extra).write_bytes(s.read_bytes())
    outtext = out.replace("\n", "\r\n") if crlf else out
    DST.write_bytes(outtext.encode("utf-8"))
    say("[4] WRITTEN")
    say(f"    {DST.relative_to(SESS)}")
    say(f"    sha256 {hashlib.sha256(outtext.encode('utf-8')).hexdigest()}")
    say(f"    {len(outtext.encode('utf-8'))} bytes")
    say("")

    after = SRC.read_bytes()
    say("[5] BASE UNCHANGED")
    same = after == before
    say(f"    v1.2 source byte-identical after the run: {'YES' if same else 'NO -- REFUSE'}")
    if not same:
        return 2
    say("")
    say("=" * 78)
    say("STAGE 3 CLEAN")
    say("=" * 78)
    return 0


if __name__ == "__main__":
    try:
        rc = main()
    except Refuse as e:
        say("")
        say(f"REFUSED: {e}")
        rc = 2
    except Exception:
        import traceback
        say("")
        say("CRASH:")
        say(traceback.format_exc())
        rc = 3
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(BUF.getvalue(), encoding="utf-8")
    print(f"\n[written] {OUT}")
    print(f"[sha256]  {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
    sys.exit(rc)
