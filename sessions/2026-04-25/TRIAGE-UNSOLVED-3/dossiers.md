# Unsolved Problems Triage — Dossiers

**Relay class:** Epistemic Mapping + Computational Scouting
**Date:** 2026-04-25
**Task ID:** TRIAGE-UNSOLVED-3
**AEAL vocabulary:** near_miss | numerical_identity | independently_verified | formalized

All "frontier" citations below are tagged `independently_verified`
(published, peer-reviewed or community-vetted preprints). No new
sweeps were launched in this relay; no `near_miss` or
`numerical_identity` tags are issued, by design.

---

## P1 — Collatz Conjecture

**Statement.** For every positive integer $n$, the iteration
$T(n) = n/2$ if even, $3n+1$ if odd, eventually reaches $1$.

**CURRENT FRONTIER** (`independently_verified`):
- Barina (2020/21): exhaustive verification that every $n < 2^{68}$
  reaches $1$ under $T$ (GPU-distributed convergence test).
- Tao (2019, "Almost all orbits of the Collatz map attain almost
  bounded values"): for any $f(n) \to \infty$, the set
  $\{n : \min_k T^k(n) < f(n)\}$ has logarithmic density $1$.
- Krasikov–Lagarias inequalities: density bounds on stopping times.
- Conze–Kac / Sinai-style ergodic reformulations exist but yield
  no quantitative reduction.

**AI-RELAY SURFACE.**
- *Enumerable now:* stopping-time histograms, $3$-adic / $2$-adic
  congruence statistics, glide-record holders, total-stopping-time
  $\sigma_\infty(n)$ for $n$ up to ~$10^{12}$ on a workstation.
  None of these advance the frontier (Barina's bound dominates).
- *PSLQ surface:* essentially **empty**. The Collatz dynamic is
  not period-like; there is no analytic constant to identify.
  The only numerical scalars of interest (e.g. average
  contraction $\log_2 3 \cdot \tfrac12 \approx 0.792$) are
  already trivially identified.
- *Lean 4 ≤ 500 lines:* feasible targets:
  (a) formalize the $T$-map and define total-stopping-time;
  (b) prove that no nontrivial cycle of length $\le L_0$ exists
      for some explicit $L_0$ (cycle-length lower bounds via
      Eliahou-style $2$-adic / $3$-adic arguments);
  (c) port Krasikov's density inequality for one specific
      exponent. (a)+(b) for $L_0 \le 17$ is the most plausible
      $\le 500$-line target — Eliahou's bound is $\ge 17{,}087{,}915$
      but the *short* cases admit a clean self-contained proof.

**OBSTRUCTION CLASS.**
- Hard obstruction: Conway-style undecidability for generalized
  Collatz maps — no purely combinatorial invariant has resisted
  attempts. The conjecture is widely viewed as requiring genuinely
  new ergodic / Diophantine input. AI-relay computation cannot
  cross this.

**RELAY ENTRY POINT** (narrow, falsifiable):
> *"In Lean 4, define the Collatz map $T : \mathbb{N}_{\ge 1} \to
> \mathbb{N}_{\ge 1}$ and prove: there is no cycle of length
> exactly $\ell$ for $1 \le \ell \le 10$ other than the trivial
> $1 \to 4 \to 2 \to 1$."*
> Falsifiable: either Lean accepts the proof or the script
> exhibits a counter-cycle (none exist; Barina's bound makes
> this a formalization exercise, not a search).

**ESTIMATED RELAY DEPTH:** 2 cycles (A1 enumerate cycle equations
mod $2^k 3^m$ → A2 Lean port → A3 critique → A4 evidence). No
path to the full conjecture in any finite relay depth.

---

## P2 — Goldbach's Conjecture (strong form)

**Statement.** Every even integer $n \ge 4$ is a sum of two primes.

**CURRENT FRONTIER** (`independently_verified`):
- Oliveira e Silva, Herzog, Pardi (2014): verified for all even
  $n \le 4 \cdot 10^{18}$.
- Helfgott (2013, accepted 2014): **ternary** Goldbach proven
  unconditionally (every odd $n \ge 7$ is a sum of three primes).
- Chen's theorem (1973): every sufficiently large even $n$ is
  $p + P_2$ ($P_2$ = product of at most two primes).
- Pintz, Ruzsa, Matomäki et al.: exceptional set bounds — the
  number of even $n \le N$ violating Goldbach is $O(N^{1-\delta})$
  for explicit small $\delta$.

**AI-RELAY SURFACE.**
- *Enumerable now:* Goldbach partition counts $r_2(n)$ (number
  of representations) for $n$ up to ~$10^{10}$ on a workstation;
  Goldbach's comet plot; minimum-prime-witness statistics. The
  $4 \cdot 10^{18}$ frontier requires distributed compute and is
  out of reach for a single-machine relay.
- *PSLQ surface:* genuine, but indirect. Hardy–Littlewood
  predicts $r_2(n) \sim 2 C_2 \, n / (\log n)^2 \prod_{p \mid n,\,
  p>2} \tfrac{p-1}{p-2}$ with $C_2 = \prod_{p>2}\bigl(1 -
  \tfrac{1}{(p-1)^2}\bigr) \approx 0.6601618...$ (twin-prime
  constant). PSLQ-style fits of the residual
  $r_2(n) - \text{HL}(n)$ vs. arithmetic correction terms is a
  legitimate exploratory target — but every leading correction
  is already known.
- *Lean 4 ≤ 500 lines:* very feasible — formalize the statement,
  the ternary form, the *Vinogradov-type* identity at small
  height, and verify Goldbach for $n \le 10^6$ by **certificate**
  (precomputed witness pair $(p, n-p)$, checked in Lean's kernel
  with a primality witness). 500 lines is comfortable for a
  certified-witness verifier; the full $4 \cdot 10^{18}$ is not.

**OBSTRUCTION CLASS.**
- Soft (computational): exceeding $4 \cdot 10^{18}$ requires
  major engineering, not new mathematics. No payoff.
- Hard (theoretical): closing the gap from Chen's $p + P_2$ to
  $p + p$ requires breaking the parity barrier — the canonical
  obstruction in sieve theory (Selberg). AI-relay cannot cross
  this either.

**RELAY ENTRY POINT** (narrow, falsifiable):
> *"In Lean 4, formalize the strong Goldbach predicate and
> produce a certified verifier that, given a precomputed table
> of Goldbach witnesses for $4 \le n \le 10^6$ (n even), kernel-
> checks every entry. Output: a Lean term of type
> `∀ n, 4 ≤ n → Even n → n ≤ 10^6 → ∃ p q, p.Prime ∧ q.Prime ∧
> p + q = n`."*
> Falsifiable: the verifier either type-checks or fails on a
> specific $n$ (none will fail; this is formalization, not search).

**ESTIMATED RELAY DEPTH:** 2–3 cycles. Cycle 1: witness table +
primality certificate format. Cycle 2: Lean verifier. Cycle 3
(optional): extend to $10^8$ if certificate compression works.
No relay path to the full conjecture.

---

## P3 — Birch–Swinnerton-Dyer Conjecture

**Statement** (rank part). For an elliptic curve $E/\mathbb{Q}$,
$\operatorname{ord}_{s=1} L(E, s) = \operatorname{rank}\, E(\mathbb{Q})$.
The full BSD also predicts the leading Taylor coefficient via the
BSD formula involving $\#\Sha(E)$, regulator, real period,
Tamagawa numbers, and torsion.

**CURRENT FRONTIER** (`independently_verified`):
- Gross–Zagier (1986) + Kolyvagin (1989): for $E/\mathbb{Q}$
  modular with analytic rank $\le 1$, the rank part of BSD holds
  and $\#\Sha$ is finite.
- Modularity theorem (Wiles–Taylor–Breuil–Conrad–Diamond, 2001):
  every $E/\mathbb{Q}$ is modular — analytic continuation of
  $L(E,s)$ to $s=1$ is unconditional.
- Skinner–Urban, Bhargava–Skinner–Zhang, Kim, et al.: positive-
  proportion results — a positive proportion of $E/\mathbb{Q}$
  by height satisfy BSD.
- LMFDB: BSD numerically verified (to high precision, modulo
  $\#\Sha$ heuristics) for all curves of conductor $\le 500{,}000$.
- Higher ranks: $p$-adic BSD (Mazur–Tate–Teitelbaum, Bertolini–
  Darmon, Bertolini–Darmon–Prasanna) gives partial results in
  rank 1, very partial in rank $\ge 2$.

**AI-RELAY SURFACE.**
- *Enumerable now:* this is the strongest of the three.
  $L(E,s)$ at $s=1$ via Dokchitser's algorithm to thousands of
  digits is routine in PARI/Sage (we already use this — see
  `_heegner_163_*` files in this workspace). The BSD formula
  components — real period $\Omega_E$, regulator $\operatorname{Reg}(E)$,
  Tamagawa product $\prod c_p$, torsion order, conjectural $\#\Sha$
  — are all individually computable to high precision for
  conductors ranging into the millions on a workstation.
- *PSLQ surface:* **direct and powerful.** The BSD ratio
  $$ \mathcal{R}(E) = \frac{L^{(r)}(E,1) / r!}
       {\Omega_E \cdot \operatorname{Reg}(E) \cdot \prod_p c_p \cdot
        \#E(\mathbb{Q})_{\text{tors}}^{-2}} $$
  is conjecturally $\#\Sha(E)$, an integer. PSLQ-style
  identification of $\mathcal{R}(E)$ as a rational with small
  denominator (or as a perfect square integer) is the canonical
  numerical test of BSD. Anomaly-hunting: does $\mathcal{R}(E)$
  ever PSLQ-identify as something *other* than an integer
  square? (No counterexample known; finding one would falsify
  BSD.) This is precisely the kind of `near_miss` /
  `numerical_identity` workflow this lab is built for.
- *Lean 4 ≤ 500 lines:* feasible targets:
  (a) state the BSD conjecture rigorously using `mathlib`'s
      elliptic curves and L-functions (the latter is
      partially formalized — currently the binding constraint);
  (b) formalize the Tamagawa-number computation for a curve
      of good or multiplicative reduction at one prime;
  (c) **certificate verifier**: given an $E/\mathbb{Q}$ and
      claimed rank $r$ with explicit generators, verify
      independence-of-points (height pairing nondegeneracy)
      to fixed precision in Lean. (c) is the most plausible
      $\le 500$-line target.

**OBSTRUCTION CLASS.**
- Hard: rank $\ge 2$ is essentially open. Kolyvagin's method
  needs a non-vanishing $L'$ or related Heegner input. The
  parity / $p$-adic methods cannot currently prove $\#\Sha$
  finite outside rank $\le 1$.
- Computation cannot prove BSD, but can **falsify** it (a
  rational ratio that fails to be a positive integer square) or
  **stress-test** it on rank-$2$ and rank-$3$ curves where
  theory is silent.

**RELAY ENTRY POINT** (narrow, falsifiable):
> *"For every rank-2 elliptic curve $E/\mathbb{Q}$ in LMFDB with
> conductor $N \le 10000$ (~ a few hundred curves), compute the
> BSD ratio
> $\mathcal{R}(E) = L''(E,1)/(2 \Omega_E \operatorname{Reg}(E)
> \prod c_p \cdot \#E_{\text{tors}}^{-2})$
> to 200 digits via Dokchitser, and PSLQ-identify it. Tag each
> result with $\{near\_miss, numerical\_identity\}$ per AEAL.
> Falsifiable claim: every $\mathcal{R}(E)$ in this set is a
> positive integer square within $\le 10^{-150}$."*

**ESTIMATED RELAY DEPTH:** 3–4 cycles. Cycle 1: enumerate +
compute. Cycle 2: AEAL-tag. Cycle 3: adversarial critique
(precision audit, $L$-function convergence). Cycle 4: Lean
formalization of the certificate format for one example.
Possible deliverable: a published "BSD compatibility table"
analogous to LMFDB but with AEAL provenance.

---

## RANKED RECOMMENDATION

| Rank | Problem | Score | Justification |
|------|---------|-------|---------------|
| **1** | **P3 — BSD** | **best fit** | Only target with a *rich PSLQ surface*, mature numerical infrastructure (Dokchitser, LMFDB) already used in this workspace, multiple Lean 4 sub-targets, and an AEAL-natural workflow (`near_miss` → `numerical_identity` → `independently_verified`). Cannot prove BSD but can produce *new* numerical evidence in higher rank, where theory is silent. |
| 2 | P2 — Goldbach | medium | Lean 4 certificate-verifier is clean and self-contained, but yields no mathematical novelty — verification at $10^6$ is far below the $4 \cdot 10^{18}$ frontier. Pedagogical / infrastructure value only. |
| 3 | P1 — Collatz | poor | No PSLQ surface. No analytic structure to identify. Lean targets exist but are exercises far from the conjecture. Computation cannot help; this is a genuine ergodic-theoretic obstruction. |

**Commit Relay Cycle 1 to P3 — BSD.**

Recommended Cycle 1 task (verbatim, ready to dispatch):
> *"BSD-RATIO-RANK2-N10000: enumerate all rank-2 elliptic curves
> in LMFDB with conductor $N \le 10000$. For each, compute
> $L''(E,1)$ via Dokchitser to 200 dps, the regulator from the
> stored Mordell–Weil generators, $\Omega_E$, $\prod c_p$, and
> $\#E_{\text{tors}}$. Form $\mathcal{R}(E)$ and PSLQ-identify
> as a rational. AEAL-tag each entry. Halt and log if any
> $\mathcal{R}(E)$ fails to identify as a perfect square integer
> within $10^{-150}$."*

This is narrow, falsifiable, uses tools already validated in this
workspace (`_heegner_163_dokchitser.py`, etc.), and its negative
outcome (everything is a square) is itself a publishable
AEAL-tagged compatibility table.
