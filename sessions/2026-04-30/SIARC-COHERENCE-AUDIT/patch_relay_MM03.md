# Relay patch prompt — MM-03 (UMB Conjecture 2.1 omits Class B)
**Source audit:** `sessions/2026-04-30/SIARC-COHERENCE-AUDIT/`

```
╔══════════════════════════════════════════════════════════════════╗
║  SIARC RELAY — UMB-CONJ-T2B-CLASS-B-PATCH                       ║
║  Goal: bring UMB Conjecture 2.1 into agreement with T2B's       ║
║         two-class structure of the degree-(2,1) trans-stratum.  ║
╚══════════════════════════════════════════════════════════════════╝

CONTEXT
  As literally written, UMB `conj:t2b` claims that every
  generic-degree-(2,1) PSL2(Z)-uniformized PCF family in tier T2
  has trans-stratum exponent c = -2/9. T2B Theorem 3 + Cor.~classB-pi
  exhibit 16 Class B families with a_2/b_1^2 = +1/4 and limits in
  Q·π^{-1}, which (by T2B's Completeness Conjecture) belong to the
  same trans-stratum. UMB's literal statement is therefore
  falsified by 16 documented families.

PROPOSED REVISION (UMB main.tex line 228 ff.)

  REPLACE:
    \begin{conjecture}[Trans-Stratum $-2/9$ Conjecture]
    \label{conj:t2b}
    Let $\{K(x)\}$ be a PCF family of generic degree $(2,1)$
    uniformized by $\PSLZ$, satisfying the regularity conditions
    of companion paper~T2B.  Then $K(x)$ lies in tier T2, and its
    trans-stratum exponent satisfies
    \[ c_{\PSLZ,(2,1)} = -\tfrac{2}{9}. \]
    \end{conjecture}

  WITH:
    \begin{conjecture}[Trans-stratum two-class conjecture]
    \label{conj:t2b}
    Let $\{K(x)\}$ be a PCF family of generic degree $(2,1)$
    uniformized by $\PSLZ$, satisfying the regularity conditions
    of companion paper~T2B.  Then $K(x)$ lies in tier T2 and falls
    into exactly one of two classes, distinguished by the
    structural ratio $\rho := a_2/b_1^2$:
    \begin{itemize}
      \item Class A ($\rho = -2/9$): trans-stratum exponent
            $c_{\PSLZ,(2,1),A} = -2/9$ (T2B Theorem~2,
            conditional on $S_{12}\neq 0$);
      \item Class B ($\rho = +1/4$): limits lie in
            $\mathbb{Q}\cdot\pi^{-1}$ (T2B Theorem~3 + Cor.~classB-pi).
    \end{itemize}
    Equivalently (T2B Completeness Conjecture): the degree-$(2,1)$
    Trans-stratum is exactly $\mathcal{T}_A \sqcup \mathcal{T}_B$,
    with no third class.
    \end{conjecture}

    \begin{remark}[Pre-revision form]
    The version of this conjecture in UMB v1 (Zenodo
    10.5281/zenodo.19885550) stated only the Class A clause.
    The current form incorporates the Class B census of
    companion paper~T2B (16 canonical families, height $\le 100$).
    No previously asserted Class A claim is revoked; the change
    is purely additive.
    \end{remark}

DELIVERABLES
  - patched UMB main.tex
  - new pdf
  - claims.jsonl entry referencing T2B Theorem 3, T2B Cor.~classB-pi
  - new Zenodo version of UMB
       * old version DOI: 10.5281/zenodo.19885550
       * concept DOI:     10.5281/zenodo.19885549  (cite this in v2)
       * new version DOI: assigned at upload
  - handoff.md per standing instructions

HALT IF
  - the proposed wording introduces a numerical claim not already
    proved in T2B (e.g., do not assert that Class B exhausts the
    +1/4 locus globally; that is T2B's *Completeness* Conjecture,
    not its Theorem)
  - any reader path "UMB → T2B → UMB" still produces a
    contradiction after the patch (run a fresh coherence audit
    restricted to UMB ∪ T2B before pushing).
```
