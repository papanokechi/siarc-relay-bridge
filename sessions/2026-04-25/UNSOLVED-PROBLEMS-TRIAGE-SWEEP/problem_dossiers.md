# Unsolved Problems Triage Sweep

Task ID: UNSOLVED-PROBLEMS-TRIAGE-SWEEP  
Date: 2026-04-25  
Relay class: Epistemic Mapping + Computational Scouting  
AEAL vocabulary: near_miss | numerical_identity | independently_verified | formalized

Scope note: this is a mapping dossier only. No new computational sweep was launched, and no unresolved target statement is asserted as true.

## Problem Dossiers

### PROBLEM: Collatz Conjecture

**CURRENT FRONTIER:**

- [independently_verified] Tao (2019; revised 2022) proved that almost all Collatz orbits, in logarithmic density, attain values below any divergent comparison function.
- [independently_verified] Barina (2020) reported convergence verification for all starting values below 2^68.
- [independently_verified] The global universal statement remains open; the frontier consists of density theorems plus finite-prefix verification rather than a proof for every positive integer.

**AI-RELAY SURFACE:**

- [near_miss] Computable now: bounded total-stopping verification for finite intervals, residue-class certificates for parity words, stopping-time histograms, maximum excursion records, and independent rechecking of selected published verification windows at much smaller bounds.
- [near_miss] PSLQ or pattern-search surface: affine parity-word maps of the form T^k(n) = (3^a n + b)/2^k, empirical stopping-time distributions, drift estimates for Syracuse blocks, and residue-class coverage ratios. This is pattern-search rather than a direct numerical-identity channel.
- [near_miss] Lean 4 target in <= 500 lines: formalize a parity-word affine-iterate lemma plus a certificate checker proving that every residue class in a finite modulus either reaches 1 or drops below its initial representative bound.

**OBSTRUCTION CLASS:**

- [independently_verified] Finite verification cannot cover the unbounded state space, and empirical drift does not supply an induction principle over all residue classes.
- [near_miss] A purely computational relay stalls unless it produces either a finitely checkable descent certificate schema closed under all residues, or a formal obstruction showing why the chosen certificate language cannot close.

**RELAY ENTRY POINT:**

- [near_miss] A1 task: produce a machine-checkable certificate for the claim "for every 1 <= n < 2^20, the Collatz orbit reaches 1," using residue blocks rather than raw orbit logs; the falsifier is any n in the interval whose certificate path fails to decrease or reaches an unchecked residue.

**ESTIMATED RELAY DEPTH:**

- [near_miss] 2 A1->A4 cycles to a meaningful formalized bounded certificate; 3-4 cycles to characterize whether the residue-certificate format scales or provably stalls.

### PROBLEM: Goldbach's Conjecture, Strong Form

**CURRENT FRONTIER:**

- [independently_verified] Oliveira e Silva, Herzog, and Pardi (2014) verified the strong Goldbach conjecture for every even integer up to 4 * 10^18.
- [independently_verified] Helfgott (2013) proved the ternary or weak Goldbach conjecture: every odd integer greater than 5 is a sum of three primes.
- [independently_verified] Chen (1973) proved that every sufficiently large even integer is a sum of a prime and an integer with at most two prime factors.

**AI-RELAY SURFACE:**

- [near_miss] Computable now: bounded even-number witness tables, independent primality certificates for each summand, gap-aware verification windows, and audit scripts that recheck published-style finite intervals at modest bounds.
- [near_miss] PSLQ or pattern-search surface: Goldbach representation counts G(2n), ratios to the Hardy-Littlewood singular-series prediction, local residue biases, and prime-gap stress cases. These are statistical structure probes, not proof-grade numerical identities by themselves.
- [near_miss] Lean 4 target in <= 500 lines: formalize a finite witness-certificate checker proving "every even N in [4,B] has listed primes p,q with p+q=N," assuming or including primality certificates for the finite prime table.

**OBSTRUCTION CLASS:**

- [independently_verified] Finite verification plus the ternary theorem does not imply the binary theorem.
- [near_miss] A computational approach stops at the missing uniform analytic lower bound for binary representation counts beyond the verified range.

**RELAY ENTRY POINT:**

- [near_miss] A1 task: build an independently rerunnable witness certificate for every even N <= 10^6, with two primality checks for each p,q pair and a compact file format suitable for a Lean checker; the falsifier is any even N in the interval without a certified pair.

**ESTIMATED RELAY DEPTH:**

- [near_miss] 1-2 A1->A4 cycles to a formalized bounded result; 3-4 cycles to map the analytic obstruction by comparing certified representation counts with explicit Hardy-Littlewood lower-bound requirements.

### PROBLEM: Birch-Swinnerton-Dyer Conjecture

**CURRENT FRONTIER:**

- [independently_verified] Wiles, Taylor-Wiles, and the Breuil-Conrad-Diamond-Taylor completion of modularity (1995-2001) established modularity for elliptic curves over Q, giving the analytic L-function framework used in rank-0 and rank-1 BSD results.
- [independently_verified] Gross-Zagier (1986) and Kolyvagin (1989) established the rank part and finiteness of the Tate-Shafarevich group for modular elliptic curves over Q when the analytic rank is 0 or 1.
- [independently_verified] The full BSD conjecture, including all ranks and the exact leading-coefficient formula in general, remains open.

**AI-RELAY SURFACE:**

- [near_miss] Computable now: small-conductor elliptic curve invariants, point counts a_p over finite fields, numerical L-values or leading coefficients, Mordell-Weil rank data from existing algorithms, Tamagawa factors, torsion orders, real periods, regulators, and BSD quotient audits for selected curves.
- [near_miss] PSLQ or pattern-search surface: rational reconstruction of BSD quotients, square detection for predicted Sha order, period-normalized L-values, regulator-normalized rank-1 derivatives, and anomaly detection across conductor strata. Escalation to numerical_identity requires independent L-function and arithmetic-invariant verification.
- [near_miss] Lean 4 target in <= 500 lines: formalize nonsingularity and finite-field point counting for one explicit Weierstrass curve over F_p for a finite list of primes, yielding certified a_p values used by the computational audit.

**OBSTRUCTION CLASS:**

- [independently_verified] Numerical BSD checks depend on analytic continuation, exact rank information, descent/Selmer computations, and Tate-Shafarevich finiteness; finite arithmetic data alone cannot prove the global conjecture.
- [near_miss] A relay can certify local Euler-factor data and selected numerical quotient checks, but it cannot bridge to general Sha finiteness or all-rank leading-coefficient formulas without importing deep theorems far outside a four-cycle computational scaffold.

**RELAY ENTRY POINT:**

- [near_miss] A1 task: select one named rank-0 curve, e.g. Cremona 11a1, and produce a two-backend numerical audit of its rank-0 BSD quotient at >= 80 decimal digits plus a Lean-checkable finite-field point-count certificate for a_p at all primes p <= 97; the falsifier is disagreement between backends, nonintegral reconstructed quotient, or a failed local point-count certificate.

**ESTIMATED RELAY DEPTH:**

- [near_miss] 3-4 A1->A4 cycles to a meaningful micro-dossier with independent numerical checks and a formalized local-data component; 4 cycles are likely insufficient for a proof-relevant global advance.

## Ranked Recommendation for Relay Cycle 1

1. **Goldbach strong form**
   - [near_miss] Best Cycle-1 target because the first deliverable can be narrow, falsifiable, independently rerunnable, and formally checkable: a bounded witness certificate with primality evidence.
   - [independently_verified] The published computational frontier is already very high, so a relay can focus on certificate discipline, negative-result reporting, and Lean checker design rather than trying to beat the frontier.
   - [near_miss] Expected payoff in <= 2 cycles: a clean formalized finite theorem plus a reusable certificate format for later intervals.

2. **Collatz**
   - [near_miss] Worth second priority because residue-class certificates are formalization-friendly and can expose whether the relay's certificate language scales.
   - [independently_verified] The best known theory is density-based rather than universal, so a bounded certificate is useful but farther from the unresolved core than Goldbach witness checking.

3. **Birch-Swinnerton-Dyer**
   - [near_miss] Richest numerical surface, but weakest Cycle-1 fit: the computations require heavier infrastructure, the Lean target is mostly local/peripheral, and proof-relevant global claims depend on deep external theorems.
   - [near_miss] Recommended only after the relay has a mature independent-verification protocol for numerical identities and arithmetic-invariant provenance.

## References Used

- [independently_verified] Tao, "Almost all orbits of the Collatz map attain almost bounded values," submitted 2019, revised 2022.
- [independently_verified] Barina, "Convergence verification of the Collatz problem," 2020.
- [independently_verified] Oliveira e Silva, Herzog, and Pardi, "Empirical verification of the even Goldbach conjecture and computation of prime gaps up to 4 * 10^18," 2014.
- [independently_verified] Helfgott, "The ternary Goldbach conjecture is true," 2013.
- [independently_verified] Chen, "On the representation of a large even integer as the sum of a prime and the product of at most two primes," 1973.
- [independently_verified] Gross and Zagier, "Heegner points and derivatives of L-series," 1986.
- [independently_verified] Kolyvagin, Euler-system work on modular elliptic curves and finiteness results for Sha, 1989.
- [independently_verified] Wiles/Taylor-Wiles and Breuil-Conrad-Diamond-Taylor modularity results for elliptic curves over Q, 1995-2001.
