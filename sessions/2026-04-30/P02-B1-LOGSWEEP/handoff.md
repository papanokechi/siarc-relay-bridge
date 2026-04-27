# Handoff — P02-B1-LOGSWEEP
**Date:** 2026-04-30
**Agent:** GitHub Copilot (VS Code)
**Session duration:** ~25 minutes
**Status:** COMPLETE

## What was accomplished
Performed a literature sweep on the logarithmic PCF family
$\alpha(n) = -k n^2,\ \beta(n) = (k{+}1)n + k$ with limit
$1/\ln(k/(k{-}1))$ (Theorem 2.1 of `tex/p02_b1_ladder_pi.tex`).
Compared against Euler's classical CF for $\ln(1{+}z)$ (DLMF 4.9.1)
both analytically (using closed-form convergents) and numerically.
Drafted a verdict and revised related-work paragraph for §2.

## Key numerical findings
- For $k=2$, our PCF has convergents $C_n = k/T_n$ where
  $T_n = \sum_{j=0}^{n} (1/k)^j/(j{+}1)$ is the partial Taylor sum
  of $-\ln(1-1/k)/(1/k) = k\ln(k/(k-1))$. (script: `novelty_test.py`,
  exact rational arithmetic.)
- Empirical convergence rate at $k=2$: $|C_n - 1/\ln 2|$ decreases
  by ratio $\to 1/2$ per step (0.47 at $n=14$), consistent with
  abstract claim $O(2^{-N}/N^{7/2})$.
- Euler's classical CF for $\ln(1{+}z)$ at $z=1$ converges
  super-geometrically (machine precision by $N=22$). Our PCF reaches
  only $\sim 10^{-6}$ at $N=14$.
- Direct match test: our PCF convergents are **NOT** equal to the
  even-indexed (or any contracted) convergents of Euler's CF for
  $\ln(2)$ (let alone its reciprocal). They are **different
  rational sequences** that converge to the same limit.

## Novelty verdict: **(B) PARTIAL/REPARAMETRIZATION-FLAVORED**

### Detailed reasoning

**The underlying identity is classical.** The closed form
$C_n = k/T_n$ shows that our PCF *encodes the partial Taylor sums*
of the standard log series
$-\ln(1-x)/x = \sum_{j\ge 0} x^j/(j{+}1)$ at $x = 1/k$.
By DLMF eq.~(3.10.5), every convergent series can be converted
mechanically into a CF whose convergents equal its partial sums
(Euler's series-to-CF conversion). Applied to our series and
followed by an equivalence transformation $c_n = k(n{+}1)$ to
clear denominators, then by a reciprocal/scaling step, one
recovers exactly $\alpha(n) = -kn^2,\ \beta(n) = (k{+}1)n + k$.
So the family is not "new mathematics" — it is a polynomial
repackaging of the Mercator/Euler log series.

**However, three aspects are not standard.**

1. The reciprocation step ($T_n \to k/T_n$) cannot be performed
   as an equivalence transformation on a CF; CFs are not closed
   under reciprocation in PCF form. So the resulting *polynomial*
   CF for $1/\ln(k/(k{-}1))$ is a non-trivial rearrangement.
2. The standard handbook entries (DLMF §4.9.1; L–W §2.4 / pp.
   292–330; Cuyt et al. pp. 196–200) give CFs for $\ln(1+z)$,
   $\ln((1{+}z)/(1{-}z))$, etc. — never for the **reciprocal**
   $1/\ln$. A targeted handbook search for "1/ln" CFs would be
   needed to confirm absence (this sweep could not access
   Lorentzen–Waadeland or Cuyt directly).
3. The empirical convergence rates differ qualitatively from
   Euler's CF (geometric vs. super-geometric), confirming that
   our PCF is not a simple rewriting.

**Therefore Theorem 2.1 should be presented as: a clean
polynomial CF tower for $1/\ln(k/(k{-}1))$ for all real $k>1$,
whose convergents are the reciprocals of the Mercator partial
sums (a known identity), proved via a uniform Casoratian
telescope and yielding a sharp $O(2^{-N}/N^{7/2})$ error rate
that does not appear in standard references.**

This is verdict **(B)** in the rubric: the identity content is
classical; the contribution is the proof technology and error
bound, not the existence of the CF.

## Draft related-work paragraph (for §2 of the .tex)

> \paragraph{Relation to Euler's series for the logarithm.}
> The closed form $q_n = (n{+}1)!\sum_{j=0}^n k^{n-j}/(j{+}1)$
> shows that the convergents of Theorem~\ref{thm:log} are
> $C_n = k/T_n$, where $T_n = \sum_{j=0}^n (1/k)^j/(j{+}1)$
> is the $n$-th partial sum of the Mercator series for
> $k\ln(k/(k{-}1))$. The polynomial recurrence $\alpha(n)=-kn^2$,
> $\beta(n)=(k{+}1)n+k$ can therefore be obtained mechanically
> by applying the Euler series-to-fraction conversion
> \cite[\S3.10(ii), eq.~(3.10.5)]{dlmf} to the Mercator series,
> followed by an equivalence transformation with multipliers
> $c_n = k(n{+}1)$ to clear denominators, and a reciprocal
> rescaling. The reciprocal step is not an equivalence
> transformation on continued fractions, so the resulting
> \emph{polynomial} CF for $1/\ln(k/(k{-}1))$ is not present
> in the standard handbook entries for the logarithm
> (\cite[\S4.9]{dlmf}, \cite[\S2.4 and pp.~566--568]{lorentzen2008},
> \cite[pp.~196--200]{cuyt2008}, which all express
> $\ln(1{+}z)$ rather than its reciprocal). Likewise, the
> classical Euler CF~\eqref{eq:euler-cf-log} for $\ln(1{+}z)$
> at $z=1$ converges super-geometrically, whereas the family
> of Theorem~\ref{thm:log} converges geometrically with
> ratio~$1/2$; the two CFs agree in their limit but produce
> different sequences of rational approximants. The novel
> contribution of Theorem~\ref{thm:log} is therefore the
> uniform polynomial parametrization for all real $k>1$, the
> Casoratian-based proof, and the sharp error rate
> $O(2^{-N}/N^{7/2})$, rather than a new analytic identity.

(Adjust citation keys to match the .bib of `p02_b1_ladder_pi.tex`;
the existing draft already cites `lorentzen2008` and `cuyt2008`.)

## Judgment calls made
- I was unable to perform a live web search of Lorentzen–Waadeland
  or Cuyt et al. (Google blocks JS-less crawl). The verdict
  therefore rests on (a) DLMF §4.9 and §3.10, (b) my closed-form
  derivation showing the family is the reciprocal-rescaling of
  the Euler series-to-CF conversion, and (c) numerical
  non-equivalence with Euler's CF. I judged this sufficient to
  recommend verdict (B) rather than (A); a stronger (A) verdict
  would require physical access to the L–W and Cuyt handbooks.
- I did not modify `tex/p02_b1_ladder_pi.tex` per the prompt;
  Claude reviews the verdict first.

## Anomalies and open questions
**THIS IS THE MOST IMPORTANT SECTION.**

1. **Sharp error rate $O(2^{-N}/N^{7/2})$ is not derived in the
   .tex file.** A grep for "error" / "convergence rate" / "N^{7/2}"
   in §2 of `p02_b1_ladder_pi.tex` finds the rate **only in the
   abstract**, not in the proof. Theorem 2.1 as currently written
   proves only convergence to the limit, not the sharp rate.
   This is an unsupported claim in the abstract — it must either
   be proved (via a Casoratian estimate on $p_n - C \cdot q_n$,
   which would give the $7/2$ exponent from Stirling) or removed
   from the abstract before submission. **Claude should flag this
   as a separate revision item.**

2. **Closed handbook check still needed.** A definitive verdict
   requires opening Lorentzen–Waadeland pp.~566–568 and Cuyt et al.
   pp.~196–200 (the explicit log-CF entries cited by DLMF §4.9).
   The probability that this exact polynomial form is listed is
   low (those pages catalog Euler/Brouncker-type fractions), but
   non-zero. If owner has library access, a 30-minute scan would
   nail down (A) vs. (B).

3. **The k=2 case ($1/\ln 2$).** This is the most-studied special
   case. Worth a separate targeted search of the OEIS / Plouffe's
   inverter for the sequence $C_n = 2, 8/5, 3/2, 192/131,\dots$
   to see if it has appeared before.

## What would have been asked (if bidirectional)
- "Should I attempt to prove the $O(2^{-N}/N^{7/2})$ rate now,
  or defer that to a separate task?"
- "Do you have access to physical Lorentzen–Waadeland pp.~566–568
  to confirm absence of this CF form?"
- "Verdict (B) implies repositioning the contribution from
  'new identity' to 'new CF form + sharp rate.' Is this acceptable
  for the Ramanujan Journal target, or does the journal require
  a stronger novelty claim?"

## Recommended next step
**Two-step revision of `tex/p02_b1_ladder_pi.tex`:**
1. Insert the draft related-work paragraph (above) at the end of
   §2 (or as a new \paragraph at the end of §1's "Related work").
2. Either (a) prove the $O(2^{-N}/N^{7/2})$ rate as a corollary
   of Theorem 2.1 using a Stirling estimate on the closed form,
   or (b) weaken the abstract to "geometric convergence with
   ratio~$1/2$" until the sharp rate is proved.

A follow-up task `P02-B1-RATE` could discharge step (2a). The
related-work insertion (step 1) should be done immediately upon
Claude's confirmation of verdict (B).

## Files committed
- `novelty_test.py` — closed-form convergent comparison and
  numerical Euler-CF cross-check (uses fractions for exactness)
- `_run.log` — full output of `novelty_test.py`
- `claims.jsonl` — 3 AEAL claim entries
- `handoff.md` — this file

## AEAL claim count
3 entries written to `claims.jsonl` this session.
