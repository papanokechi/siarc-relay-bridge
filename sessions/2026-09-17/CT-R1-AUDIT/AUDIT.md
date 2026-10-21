# AUDIT.md — audit of the 13 PROVEN labels

Session: `sessions/2026-09-17/CT-R1-AUDIT/`
Round: **R1**, triggered by the operator review of the P1–P5 deliverables.
Scope: read-only inspection plus independent symbolic re-derivation. No repo
file outside `sessions/2026-09-17/` was touched. Nothing was committed.

Amendment script: `apply_audit.py` → `apply_audit.log`.
Every amended claim now carries `audit_r1`, `amended_in`, and — where the label
moved — `label_before`, so each change is reversible and auditable.

---

## 0. Headline

Of the 13 claims labelled PROVEN:

| outcome | count | claims |
|---|---|---|
| **upheld as-is** | 6 | S3B-01, S3B-03, S4-04, S4-05, S4-06, S4-07 |
| **upheld, but only after repair** | 1 | S1-03 |
| **upheld, basis restated** | 3 | S1-01, S1-02, S4-03 |
| **downgraded → STRUCTURAL** | 3 | S2-05, S3A-03, S3A-06 |

Separately, one claim was **upgraded** STRUCTURAL → PROVEN (S1-04), because
Gap G1 was closed during this round.

Corpus after R1: **47 claims — 16 PROVEN, 21 STRUCTURAL, 10 VERIFIED.**
(47 rather than 37 because session `CT-S5B-COVER` added 10.)

**Nothing in this corpus is machine-checked.** `lean/XiZero/Basic.lean` still
has 7 `sorry`s. PROVEN here means "complete human-written proof", per P0.

---

## 1. The load-bearing defect: theorem.tex, Theorem `thm:radius`, Step 3

The operator asked for the multinomial-sandwich argument to be read cold. I did.
**The idea is sound and the sandwich is correct, but the first draft contained an
unproved assertion that the argument depends on.**

The draft said, without proof:

> "$\binom{dn}{n,\dots,n}=(dn)!/(n!)^d$ is the largest of the
> $\binom{dn}{k_1,\dots,k_d}$ over compositions of $dn$ into $d$ parts"

This is **load-bearing**. The upper bound `(dn)!/(n!)^d ≤ d^{dn}` needs only that
the balanced coefficient is *one term* of the multinomial expansion. But the
**lower** bound `d^{dn}/(dn+1)^{d-1} ≤ (dn)!/(n!)^d` is obtained as
*max ≥ average*, and that step is valid only if the balanced coefficient really
is the maximum. Without maximality the lower bound does not follow, and the
sandwich collapses to a one-sided estimate — which is not enough for the limit.

The assertion is **true**, and elementary. It is now proved in `theorem.tex` by
an exchange argument: if `k_i ≥ k_j + 2`, moving one unit from part `i` to part
`j` multiplies the coefficient by `k_i/(k_j+1) ≥ (k_j+2)/(k_j+1) > 1`, so any
maximiser over the (finite) set of compositions has `|k_i − k_j| ≤ 1` for all
`i,j`; with `Σk_i = dn` that forces `k_1 = … = k_d = n`.

I also re-checked the counting bound: a composition is determined by
`(k_1,…,k_{d−1}) ∈ {0,…,dn}^{d−1}`, so `N_{d,n} ≤ (dn+1)^{d−1}`. Correct.

**Verdict on the rest of the proof:** Steps 1, 2, 4, 5 are correct as written.
Step 1's use of (H) is genuine and correctly flagged as essential — if
`r_∞ = 0` then `|r_n|^{1/n}` need not → 1. Step 2 uses only `log(1+x) = O(x)`
and `Σ_{k≤n} 1/k = O(log n)`; `u_k ≠ 0` is secured by (A1). Step 4's combination
of three limits is legitimate because each exists, is finite, and the
denominator limit is nonzero. Step 5 is Cauchy–Hadamard plus a disc image.

**No Stirling or Gamma asymptotics is used anywhere in part (i)**, as the prompt
required. That constraint is genuinely met.

`S1-03` therefore **keeps PROVEN**, but the record now states that it did so
only after the repair.

---

## 2. Gap G1 closed (S1-04: STRUCTURAL → PROVEN)

G1 was: `Γ(n+1−r)/Γ(n+1) = n^{−r}(1+O(1/n))` quoted rather than proved.

It is now **mostly proved in session**, and the residual import is named
precisely. Put `h(n) := Γ(n+1−r)·n^r/Γ(n+1)`. From `Γ(x+1) = xΓ(x)` alone,

```
h(n)/h(n−1) = (1 − r/n)·(1 − 1/n)^(−r) = (1 − r/n)(1 + r/n + O(1/n²)) = 1 + O(1/n²)
```

Since `Σ O(1/n²) < ∞`, the telescoping product converges to a finite nonzero
`h_∞`, and the tail of a convergent `Σ O(1/m²)` is `O(1/n)`, giving
`h(n) = h_∞(1 + O(1/n))`. **The entire `O(1/n)` error bookkeeping — which is
what part (ii) actually needs — is now self-contained.**

The one remaining imported ingredient is the *constant* `h_∞ = 1`. That is cited
to **DLMF (5.11.12)**, §5.11(iii) "Ratios":
`Γ(z+a)/Γ(z+b) ∼ z^(a−b) Σ_{k≥0} G_k(a,b) z^(−k)` for `|ph z| ≤ π − δ`, with
`G_0(a,b) = 1`; take `a = 1−r`, `b = 1`, `z = n`. I verified this equation
number and its statement against `https://dlmf.nist.gov/5.11` directly rather
than from memory. A `thebibliography` entry was added and the document now
compiles with **no undefined references or citations**.

Citing a classical special-function asymptotic at a named equation number is
normal practice, not a gap. `S1-04` is therefore **PROVEN, modulo one explicitly
named classical citation** — and the qualifier is stated in the abstract, at the
point of use, and in §`sec:gaps`, so no reader can miss it.

`theorem.pdf` is now **7 pages** (was 6).

---

## 3. The three downgrades

The operator's suspicion was right: several PROVEN labels were attached to
**file inspections**, which cannot be proofs.

* **S2-05** — "PCF2-SESSION-Q1 stores no `rho` at d=4". This is a **negative
  search result**. A null grep is only as strong as its search terms; it cannot
  establish absence. → **STRUCTURAL**.
* **S3A-03** — locating and interpreting the explicit halving in
  `CC-PIPELINE-G/vquad_recovery.py` L70–79. Accurate, but interpreting a
  self-contradictory source comment is an interpretive act. → **STRUCTURAL**.
* **S3A-06** — "Proposition 3.3.A does not exist in v1.3.1; the object is
  Conjecture 3.3.A★". File inspection, and partly a negative result.
  → **STRUCTURAL**.

### A taxonomy gap the operator should rule on

P0's four labels have **no slot for "a verified fact about repository
contents"**. PROVEN overstates it; VERIFIED is defined as *numerically checked
at stated dps with a stated residual*, which does not apply; CONJECTURED badly
understates a direct quotation from a file. I have used **STRUCTURAL** for all
`file_inspection` claims, which at least makes the corpus **internally
consistent** — previously S3A-03/S3A-06 carried PROVEN while S4-01/S4-02 carried
STRUCTURAL on *identical* evidence type. That inconsistency is now removed, but
the underlying taxonomy gap is a real defect in P0 and is reported, not patched.

---

## 4. The seven upheld PROVEN labels, with their true basis

* **S1-01, S1-02** (existence of `r_∞`; `b>0 ⇒ (H)`) — genuine proofs, all
  sub-steps complete. Upheld.
* **S3B-01** (the `1e-3000` threshold is ill-posed) — this one *looks* like a
  numerical finding but is a rigorous elementary estimate: tail terms `~1/(9k⁴)`,
  tail sum `~1/(27N³)`, so `1/(27N³) = 1e-3000` gives `N ~ 10^999.5`. Upheld.
* **S3B-03** (no root of `3n²+n+1` is a positive integer) — `disc = 1 − 12 =
  −11 < 0`, so both roots are non-real. Complete proof. Upheld.
* **S4-03** (System A's ODE) — **basis restated.** The proof is the *symbolic*
  derivation `[1 − z·b(θ+1) − z²]f = 1`, exact at all orders. The vanishing
  residual at `z⁰…z³⁸` is **corroboration**; a finite check alone would not
  warrant PROVEN. The claim text previously led with the finite check.
* **S4-04** (System B transcription) — two independent exact CAS identity
  checks. Upheld.
* **S4-05, S4-06, S4-07** (formal types, action differences) — exact arithmetic
  on integers, no tolerance anywhere. Upheld, **with a dependency now named**:
  the step from *pole order* to *{ramified, Katz invariant}* invokes the
  standard classification of second-order formal singularities, which is cited
  rather than proved in session. The pole orders themselves are proved.

---

## 5. Independent re-derivation of the new P5b results

Session `CT-S5B-COVER` (run this round) reports 5 PROVEN claims. I re-derived
its two central computations by hand rather than accepting them:

**Pullback rule.** For `u'' = r(z)u` and `z = φ(s)`, `v(s) = u(φ(s))` gives
`v'' − (φ''/φ')v' − (φ')²r(φ)v = 0`; removing the first-derivative term via
`¼a² + ½a' − b` yields `R = (φ')²r(φ) − ½{φ,s}`. For `φ = w²`:
`{φ,w} = −(3/2)(2/2w)² = −3/(2w²)`, so the correction is `+3/(4w²)`. **Correct.**

**System A pullback.** With `r_A = (−3z²−5z+3)/(9z³)`:

```
R(w) = 4w²·(−3w⁴−5w²+3)/(9w⁶) + 3/(4w²)
     = [16(−3w⁴−5w²+3) + 27w²]/(36w⁴)
     = (−48w⁴ − 53w² + 48)/(36w⁴)
```

matching the agent's output exactly. Numerator at `w=0` is `48 ≠ 0` ⇒ pole
order **4**, even ⇒ **unramified**, Katz `4/2 − 1 = 1`. At infinity I get
`(48t⁴ − 80t² − 48)/(36t⁴)`, numerator `−48 ≠ 0` ⇒ pole order 4, Katz 1. **Both
confirmed.**

**System B inversion.** `φ = 1/x` has `{φ,x} = 6/x² − (3/2)(4/x²) = 0`, so
`R(x) = r_B(1/x)/x⁴ = (12x⁴+4x³+4x²+11)/(4(3x²+x+1)²)`, matching. Roots of
`3x²+x+1` are `(−1 ± i√11)/6`; `R(0) = 11/4` finite ⇒ `x=0` ordinary. **All
confirmed.**

One note the other way: **S5B-C2 is labelled STRUCTURAL but is arguably
PROVEN** — the Schwarzian pullback rule is a complete derivation and I verified
it independently. I left the conservative label in place; erring low is the
right direction.

---

## 6. What the audit did *not* establish

* **Nothing is machine-checked.** 7 `sorry`s remain in
  `lean/XiZero/Basic.lean`. The Lean file states only part (i).
* I reviewed the part (i) proof **myself**, not via an independent cold session.
  The operator asked for "either". If a truly independent read is wanted, the
  repaired Step 3 is the passage to hand over.
* The 2317.8 digits of `r_∞` remain **VERIFIED, not rigorous** — they come from
  agreement between extrapolation levels. Unchanged, and adequate for the
  dps-2000 PSLQ null.
* I did not re-audit the 10 VERIFIED labels; the operator did not ask, and the
  numerical claims all trace to a script and a hashed output.

---

# R2 — operator review #2 (same session, CT-R1-AUDIT)

Round 2 responds to the operator's four rulings. No commit, no deposit, HEAD
unchanged.

## R2.1 Ruling 2 executed: the companion paper, from Zenodo

Concept DOI `10.5281/zenodo.20455089` resolved; **three** versions exist, all
titled *"A non-classical Painlevé V transcendent from a quadratic polynomial
continued fraction: surface classification and resurgent Stokes data"* (note:
this differs from the title carried in the repo's bibliography entry). All three
were downloaded into `CT-R1-AUDIT/refs/` with sha256 recorded:

| version | version DOI | date | pp | sha256 (prefix) | object 4.1 |
|---|---|---|---|---|---|
| v1.0 | `10.5281/zenodo.20455090` | 2026-05-30 | 10 | `C07C97D6…` | **Theorem 4.1** |
| v1.1 | `10.5281/zenodo.20480603` | 2026-06-01 | 12 | `E07C1DDA…` | **Theorem 4.1** |
| v1.2 | `10.5281/zenodo.20481592` | 2026-06-01 | 12 | `A5D9E264…` | **Conjecture 4.1** (7 occurrences) |

**The operator's hypothesis is confirmed exactly.** Conjecture 4.1 first appears
at v1.2. The repo's `\bibitem{Vquad}` cites version DOI `…20455090`, which is
**v1.0** — where the object numbered 4.1 is a *theorem*. Anyone reading the cited
version would therefore fail to find "Conjecture 4.1", which is precisely the
R1 finding.

**Finding S4-F1 is closed** and the R1 wording of it is superseded. The halt
recorded as claim S4-08 is lifted. Claim label: INSPECTED (per ruling 1) —
established by inspection of named files with stated hashes, valid for those
files only.

## R2.2 Ruling 1 adopted: the INSPECTED provenance label

`INSPECTED` is now in use across all session `claims.jsonl` files, with the
operator's two rules:

* **1(a)** every `evidence_type: file_inspection` claim carries INSPECTED and can
  never be PROVEN. Enforced programmatically; `apply_audit_r2.py` asserts the
  invariant and it holds across the corpus.
* **1(b)** absence claims are phrased **"NOT FOUND in ⟨scope⟩ by ⟨method⟩"**,
  never "does not exist". Claims S2-05 and S3A-06 were rewritten accordingly.

Post-amendment corpus (63 claims): PROVEN 19, INSPECTED 20, STRUCTURAL 13,
VERIFIED 10, CONJECTURED 1.

### R2.2.1 A schema question for the operator (claim R1-16)

Applying rule 1(a) *literally* would have demoted twelve genuine mathematical
results — `S1-01…S1-05`, `S3A-02`, `S3B-04`, `S3B-07`, `R1-02`, `R1-03`,
`R1-08`, `R1-09` — whose only connection to "file inspection" is that the proof
text happens to live in a `.tex` or `.md` file. That is an **evidence_type
error, not a label error**: their evidence is a proof, read and checked, not the
presence of a file.

I retagged those twelve to a **new `evidence_type: "proof"`**, outside the
original `file_inspection|computation|build` set, and left their labels intact.
**This extends the AEAL schema and needs the operator's confirmation or
replacement.** If rejected, the alternative is to keep `file_inspection` and
carve an explicit exception into rule 1(a); I did not do that, because an
invariant with an exception is not enforceable.

## R2.3 Ruling 3 executed: CT-S6-APPARENCY launched

Delegated with the operator's five-step scope verbatim, plus two additions made
after launch, when the v1.2 PDF arrived:

* **System C** (companion §2.2, eq. (6)–(7)) — the ODE Conjecture 4.1 is
  *actually* about, which is neither System A nor System B. Its finite singular
  points `(−1 ± i√11)/6` coincide exactly with those of the *inverted* System B.
* **Companion Remark 2.2**, which asserts as a general principle that the finite
  singularities of any PCF-derived ODE of this shape "are always apparent". That
  is a testable claim and is now in scope.

## R2.4 Ruling 4 honoured

`op:cc-median-resurgence-execute` is left as a **flag only**. No restatement was
written; that is an authoring decision reserved to the operator. The substantive
content for a future restatement is recorded in `CT-S3B-RINF/REPORT.md` and in
R1 §5: the problem concerns the exponential-sector series `e^{c±/u}·(…)`, whose
Borel singularities sit at the action difference `ζ* = 2ξ₀`, and the ξ₀-level
amplitude `K` is now in closed form and is therefore **not** what it targets.

## R2.5 The operator's caveats on the classification result

Recorded in `CLASSIFICATION-TABLE.md` §5, as binding constraints on any use of
§3: (i) a matching Katz multiset is necessary, not sufficient; (ii) the cover
lands on a **special** PIII(D6) family; (iii) the `−` slot in `(1/2, −, 1/2)`
is an unjustified premise until CT-S6 step 5 returns.

## R2.6 On the repaired sub-lemma

The operator's independent reconstruction of the exchange argument matches the
text written into `theorem.tex` step 3 exactly, including the ratio
`k_i/(k_j+1) > 1` and the three-step lower bound (max ≥ average; total `d^{dn}`;
composition count `C(dn+d−1, d−1) ≤ (dn+1)^{d−1}`). A cold read of the written
passage by an independent session remains desirable but is, per the operator,
lower value than attacking the seven Lean `sorry`s. Neither was done here.

## R2.7 `CT-S6-APPARENCY` returned — spot-check and one correction

Ruling 3's session completed. As with P5b, I re-derived its load-bearing results
independently rather than accepting them (`verify_s6.py`, `VERIFY-S6.md`).

**Confirmed exactly**, by script and by hand: System C's exactness `b = a'`;
exponents `[0,0]` at `s± = (−1 ± i√11)/6` with normal-form residue `−1/4`;
System C's normal form identical to the inverted System B's; Katz 1 unramified
at `x = ∞`.

**Strengthened.** CT-S6 refuted companion Remark 2.2 with two counterexamples.
The refutation is in fact general: the indicial polynomial at any simple root of
`χ` with `c(s) ≠ 0` is `λ²` for *every* `χ` and `c`, so such a point is **never**
apparent. The exactness identity `b = a'` the companion relies on is precisely
what forces this. PROVEN, claim R1-18.

**Corrected.** CT-S6's claim S6-C7 (System B multiset `(1,0,0,0)`, no matching
row) contradicts its own PROVEN equivalence of System B with System C, whose
multiset is `(0,0,1)`. The defect: its apparency test rejected `z = ∞` because
the exponents are non-integers, but they differ by exactly `1` and the rank-1
twist implicit in the normal-form reduction makes the point **ordinary**
(`R = 11/4` finite at `x = 0`). Effective multiset is `(0,0,1)`. S6-C7 is
superseded — recorded as claim R1-20, not edited in the CT-S6 session folder.

**Consequence for Conjecture 4.1: right row, wrong reason.** Its `D5^(1)`
conclusion is consistent with van der Put–Saito for System C, but its stated
argument — `β = γ = 0` because the finite singularities are apparent — rests on
a premise now refuted. Membership remains open under caveat 5.1 either way.

Five claims appended: R1-17 … R1-21. CT-R1-AUDIT now carries 21 claims;
rule 1(a) invariant re-asserted and holds.

---

# R3 — operator review #3

Four rulings plus two corrections. Nothing committed; HEAD unchanged.

## R3.1 Corrections accepted

* **The Remark 2.2 lemma is more general than we stated.** The hypothesis
  `c(s) ≠ 0` is unnecessary and has been **dropped**: once `p = χ'/χ` has residue
  `1` and `q` has at most a simple pole, the indicial polynomial is `λ²` whatever
  `c(s)` is, and equal exponents then force the log term. Claim R1-18 rewritten;
  `VERIFY-S6.md` §2 amended.
* **"Ordinary after twist" needed the qualification.** It is equivalence **up to
  a rank-1 twist**, not equivalence of the operators themselves — valid for
  Table 2.1 precisely because that table classifies trace-free rank-2
  connections. Claim R1-20 rewritten; `VERIFY-S6.md` §3 amended.

## R3.2 Ruling 1 — `evidence_type: "proof"` accepted, with a `review` field

Every `proof` claim now carries `review ∈ {self, cold, lean}`:
`self` = checked only by the authoring agent; `cold` = read by an independent
session without its derivation history; `lean` = machine-checked with no `sorry`
on the claim's path. PROVEN may stand on a `self` claim, but **anything entering
a deposit needs `cold` or `lean`.**

State after gate 1 returned: **17 `self`, 1 `cold`, 0 `lean`.** The single
`cold` is S1-03 (part (i) Step 3).

## R3.3 Ruling 2 — the stale bibitem, located and already fixed

It is in the **period-rep paper**, not Channel Theory — and the operator's first
hypothesis was right: *the repo source is older than the deposit*.

| copy | title | DOI cited | state |
|---|---|---|---|
| `2026-06-15/VQUAD-PERIODREP-PAPER-001` | old title | **version** `…20455090` | **stale**, superseded |
| `2026-06-16/VQUAD-REPRO-BUNDLE-001` | old title | **version** `…20455090` | **stale**, superseded |
| `2026-06-16/VQUAD-PAPER-CORRECTIONS-001` | Zenodo title | **concept** `…20455089` | correct |
| `2026-06-16/VQUAD-PAPER-LAYOUTFIX-001` | Zenodo title | **concept** `…20455089` | correct |
| `2026-06-16/VQUAD-REPRO-BUNDLE-002` (slot-root and `run-2`) | Zenodo title | **concept** `…20455089` | correct |

The deposit-ready path is `VQUAD-REPRO-BUNDLE-002/run-2` (per that session's own
`stale-pin-inventory.md`), and it is **correct**. CT-S4 read the superseded
2026-06-15 draft. **No fix is required**; recorded as claims R1-22/R1-23.

One residual, for that paper's next version only: the corrected bibitem gives
concept DOI and title but names the **version read** only in section-8 prose
("with the `S = 2πK` calibration in version 1.2"), not in the bibitem itself.

## R3.4 Ruling 3 — correction-note scope

Written to `CORRECTION-NOTE-SCOPE.md`, with all four required points. Note in
particular that the earlier reading in this session — that the old PIII(D₆)
label "may have been closer to right" — is **withdrawn**: it presumed the old
label was about System A, which has not been shown.

## R3.5 Ruling 5 — deposit route

Standalone note; plan and gates in `DEPOSIT-PLAN.md`.

## R3.6 Gate 1 returned (`CT-S7-COLDREAD`) — and found a real defect

* `thm:radius` Step 3 — **SOUND**.
* `thm:growth` Step 3 / G1 — **ERROR**: DLMF (5.11.12) misquoted as the full
  `G_k` expansion. Confirmed independently against dlmf.nist.gov: (5.11.12) is
  the plain ratio, (5.11.13) is the expansion, (5.11.15) gives `G_0 = 1`.
  Repaired at five sites; recompiles clean at 7 pages. The mathematics is
  unaffected, because (5.11.12) alone is what the proof needs.

Gate 1 is **not closed**: the repair has not itself been cold-read.

Two successive independent reads of this document have each found a defect. That
pattern is itself evidence about how much weight a `self` review can carry.

---

# R5 — CT-S9 verification and the closure of deposit gate 1

## R5.1 Ruling 4 (PV parameters) — verified, and extended

`VERIFY-S9.md` records the independent check. CT-S9 did not halt; it found a
quotable Jimbo convention and reported a contradiction. Both were re-derived
from scratch (`verify_s9.py`), and the dictionary was verified against the
primary source by reading the page image, not by trusting the agent.

Outcome: **CT-S9 is correct**, and three things are added.

1. **The contradiction is genuine, not conventional.** Under `z -> cz` PV maps
   `(a,b,g,d) -> (a,b,cg,c^2 d)`, so holding `d = -1/2` forces `c = +/-1`.
   `gamma = 1` cannot be rescaled to `gamma = 0`.
2. **Jimbo's (A1)_PV (`theta_0, theta_t not in Z`) is violated** by
   `theta_0 = theta_t = 0`. The dictionary precedes (A1) and survives; the rest
   of Jimbo's machinery does not apply to this case. This coheres: integer theta
   is the resonant case, and resonance is when logarithms appear — which is what
   CT-S6 independently found.
3. **The PV time is fixed, not free**: `t = -/+ 2i sqrt(33)/9`. This answers the
   operator's question directly. It also states exactly what a membership claim
   would have to produce: an isomonodromic *family* whose fibre at that `t` is
   System C. Not found.

## R5.2 Gate 1 — CLOSED

| passage | cold reader | verdict | defect found |
|---|---|---|---|
| `thm:radius` Step 3 (multinomial sandwich) | CT-S7-COLDREAD | SOUND | none |
| `thm:growth` Step 3 / G1 | CT-S7-COLDREAD | **ERROR** | DLMF (5.11.12) misquoted as (5.11.13)'s content |
| `thm:growth` Step 3 / G1, after repair | CT-S10-COLDREAD2 | SOUND | stale release string `1.2.4` vs actual `1.2.8` |

Both defects were citation defects; neither touched the mathematics. Both were
independently confirmed against the live DLMF source before being acted on, and
both are now fixed. `theorem.tex` recompiles clean at 7 pages. `S1-03` and
`S1-04` both carry `review: cold`.

**The pattern is worth stating plainly for the operator.** Three successive
independent reads of `theorem.tex` found three defects, all in citation
metadata and none in the argument. That is mildly reassuring about the
mathematics and quite unflattering about the bibliography discipline. The
standing recommendation is that every external citation in anything deposited be
re-fetched and hashed at deposit time rather than carried forward from an
earlier draft — which is the same failure mode as the stale `\bibitem{Vquad}`
from ruling 2.

## R5.3 Gate status

| gate | status |
|---|---|
| 1. Cold review of part (i) Step 3 and G1 | **CLOSED** |
| 2. No machine-checked claim asserted | **OPEN BY DESIGN** — 7 `sorry`s remain; binding on wording |
| 3. Literature check | **PENDING** — CT-S8-LITCHECK not returned |

Gate 3 remains the largest risk, exactly as the operator judged.

---

# R6 — deposit gate 3 returned: the radius theorem is prior art

`CT-S8-LITCHECK` returned. Full detail in `VERIFY-S8.md`; gate consequences in
`DEPOSIT-PLAN.md` §§4–6. Headline:

* **Result 1 (radius) is PRIOR ART** — a corollary of Perron–Kreuser
  (Gautschi, *SIAM Review* 9(1) 1967, Thm 2.3(a), p. 35) plus Pincherle
  (ibid. Thm 1.1, p. 31). Independently re-derived here and **confirmed**.
* **Result 2 (explicit `s`) is BLOCKED** on Wong & Li (1992a), paywalled and not
  obtained. Recorded as NOT FOUND, never as new. Needs operator access.
* **Result 3 (`K`) strengthens** — CT-S8 independently reproduced the closed form
  at 60 dps without access to P3's derivation.

## R6.1 The OCR trap, and why the page was re-rendered

CT-S8's quote of Theorem 2.3 was exact. But the *hypotheses* (2.8) were only
available through a lossy OCR layer that produced `"ab 0; a, real"` — readable
either as "the coefficient `a` is real" (which would **exclude** our complex
`β_d` and void the whole finding) or as "the exponents `α, β` are real".

Journal p. 34 was re-rendered from the PDF at 3× to settle it. The true text is
`ab ≠ 0; α, β real` — **the exponents**. Perron–Kreuser therefore does cover
complex `β_d`, and the finding stands at full generality.

This is the fourth citation-level defect handled in this run, and the second
where an OCR or transcription artefact could have flipped a conclusion. The
standing recommendation in `DEPOSIT-PLAN.md` — re-fetch and hash every external
citation at deposit time, and read page images rather than OCR for anything
load-bearing — is reinforced.

## R6.2 Labels versus priority

`S1-03` is PROVEN and `review: cold`, and **both stand**. Being classical does
not make a proof wrong. Priority is a different axis from correctness, and the
taxonomy has no rung for it, so it is recorded in a separate `audit_r6` field on
the claim rather than by moving the label. This mirrors the operator's own
reasoning in ruling 1 for INSPECTED: different kinds of claim need different
fields, not more rungs.

## R6.3 Position

Gate 1 CLOSED, gate 2 open by design, **gate 3 returned but NOT closed**.
**Recommendation: do not deposit.** The blocker is narrow and concrete — one
paywalled 1992 paper — and it is load-bearing for the contribution claim.

---

# R7 — operator review #4: route change, two cold reads, P0 rule

## R7.1 Both scheduled cold reads returned, and both paid off

| packet | reader | verdict | what it added |
|---|---|---|---|
| A — the Remark 2.2 lemma | `CT-S11-COLDREAD3` | **SOUND** | **improved the proof** |
| B — the PV parameter contradiction | `CT-S12-COLDREAD4` | **SOUND WITH CAVEAT** | independently re-derived the load-bearing step |

Both read from self-contained packets in `coldpackets/`, with explicit
instructions not to open any other file in the session tree.

**Cold read A improved the lemma.** Where the packet appealed generically to
Frobenius theory for the logarithm, the reader supplied the explicit
reduction-of-order argument: since `p = χ'/χ`, `exp(−∫p) = 1/χ`, so the second
solution is `y₂ = y₁ ∫ dx/(χ y₁²)` and the integrand has a **simple pole at `s`
with residue `1/(h(s)y₁(s)²) ≠ 0`**. This exhibits the log coefficient
explicitly and nonzero, closing the only soft step in the argument. Verified by
hand and adopted into `DRAFT-COMPANION-v1.3-NOTICE.md` §C1.

**Cold read B re-derived the step that mattered.** The packet deliberately
instructed the reader not to take the PV rescaling law on trust. It derived
`(α,β,γ,δ) → (α,β,cγ,c²δ)` from the Painlevé V equation by direct substitution,
**and** checked the opposite convention, where the law reads `(α,β,γ/c,δ/c²)`.
The conclusion survives either way: fixing `δ = −1/2` forces `c² = 1`.

It also **independently rediscovered (A1)_PV** on the Jimbo page, without being
told to look. Two independent parties have now found the assumption that
`CT-S9-PVPARAMS` — which produced the original result — missed.

Its two caveats are not new defects. One is an artefact of my own packet design
(the published tuple was withheld to preserve isolation, so the reader could not
verify it); the other is the `(A1)` point already recorded as `R1-32`.

## R7.2 Wong–Li: the citation is confirmed, and a trap was found

`CT-S8-LITCHECK`'s identification is **correct**, verified against
`https://dlmf.nist.gov/bib/W`. But the DLMF suffix ordering invites error:

| DLMF key | Paper | Cited for |
|---|---|---|
| **1992a** | *…difference equations.* **II**, *Stud. Appl. Math.* **87**(4), 289–324 | **eq. (2.9.14) — our case** |
| 1992b | *…difference equations*, *J. Comput. Appl. Math.* **41**(1–2), 65–94 | bounded case — not ours |

**"1992a" is the paper titled "II".** An access request quoting only the DLMF
key would plausibly retrieve the wrong paper. Full citation recorded in
`DRAFT-CT-v1.7-NOTICE.md` §5.

The paper remains **NOT OBTAINED**. Paywalled at Wiley; no mirror used. The
companion 1992b DOI resolves only to a ScienceDirect stub (`anon_guest`), which
is not evidence of open access and is the wrong paper anyway. This needs the
operator.

## R7.3 Route change recorded

The standalone note is **dropped**; `DEPOSIT-PLAN.md` now carries a superseding
header. Two drafts prepared, neither applied to any source file:

* `DRAFT-CT-v1.7-NOTICE.md` — N1 attribution and retirement of the conjecture
  label; N2 supersession of the EBR positivity grounding; N3 `K` and the `r_∞`
  series; N4 the one-line vacuity explanation. `[WONG-LI]`-flagged passages
  carry two alternative phrasings each.
* `DRAFT-COMPANION-v1.3-NOTICE.md` — C1 the lemma; C2 the refuted derivation and
  the genuine contradiction; C3 the well-posedness restatement; C4 the
  per-object label table.

## R7.4 P0 citation rule adopted

`P0-CITATION-RULE.md`. The evidence base is four citation defects in one run,
**none** in any mathematical argument, **one** of which — the Gautschi (2.8) OCR
artefact — would have flipped the prior-art conclusion. That one sat in a
**hypothesis**, which is why the rule names hypotheses explicitly.

## R7.5 A note on the `review` field's scope

Ruling 1 defined `review` for `evidence_type: "proof"`. It has been applied here
to three non-proof claims (`R1-31`, `R1-32`, `R1-33`) as well, because the
question it answers — *has an independent party checked this?* — is just as
meaningful for a computation or a file inspection. Flagging the extension rather
than assuming it: the operator may prefer to restrict it.

---

# R8 — Operator review #5

Three rulings: Wong-Li access with an author request; a refined `review`
taxonomy for computations; publish the companion v1.3 correction first, behind
three gates.

## R8.1 Ruling 1 — the author request, and a title defect

The draft was not in review #5 (that message ended at the instruction to check
the title); it arrived separately. **The check the operator asked for fired.**

The drafted title read *"Asymptotic expansions for second-order difference
equations, II"*. Both the publisher record (Crossref, the registrant for
DOI `10.1002/sapm1992874289`) and the stored DLMF bibliography give
*"second-order **linear** difference equations"*. The word **linear** was
missing from the subject line and from the body citation, and was restored in
both.

This is not pedantry. DLMF's **1992b** is a different paper, in a different
journal, carrying the same title **minus the trailing "II"** — and it covers the
bounded-coefficient case, which is not ours. A degraded title sent to an author
who wrote both papers is a request that can be answered with the wrong one. The
corrected draft quotes journal, volume, pages **and DOI**, so the identification
does not rest on the title at all.

The signature block was verified character by character, and the ORCID digit by
digit, against the 2026-06-16 deposit metadata. It matches; nothing was invented.

Deliverable: `AUTHOR-REQUEST-WONGLI.md`. **Nothing has been sent.**

## R8.2 Ruling 2 — `review` now has a type-dependent definition

`cold` is no longer a single notion:

| Claim type | `cold` requires |
|---|---|
| Proof | an independent party read the argument **without its derivation history** |
| Computation | an independent party reproduced the value by **different code**, ideally a different method, **without access to the original script or output** |

Re-executing the original script is **`self`**, not `cold`. Every review value
now carries a **`review_note`** recording the method, so the distinction is
auditable after the fact rather than taken on trust.

Retro-applied across the corpus by `apply_audit_r8.py`: **8 cold, 28 self, 0
lacking a `review_note`**. One promotion: **R1-40**, CT-S8's independent
derivation of `K` from the Gauss multiplication formula and its 60-dps
verification in its own script, which meets the computational bar. No
downgrades were required — the existing `cold` values all survived scrutiny
under the stricter definition, which is a reassuring result rather than a
foregone one.

## R8.3 Gate 1 — PASS, and two findings that strengthen C2

Every tuple, equation number and remark number in the draft notice was checked
against companion v1.2 (sha256 `a5d9e264…`), reading 3×-rendered **page images**
per the P0 rule. **All 11 checked items match**, including Remark 2.2's number
and its verbatim apparency wording, Conjecture 4.1's number, and the tuple
`(1/6, 0, 0, −1/2)`. No defect.

The gate also turned up two things that make the correction more robust, both
folded into **C2**:

* **F1 — the convention objection is closed by the companion's own text.**
  v1.2 p. 6 states and applies the very law we used,
  `(α, β, γ, δ) ↦ (α, β, cγ, c²δ)` with `c = √3`. Its claim that this "leaves
  `γ = 0` invariant" holds only *because* `γ` was assumed `0`; the correct
  `γ = 1` maps to `√3`.
* **F2 — the `γ` error does not depend on C1.** The companion's `θ₁ = θ₂ = 0`
  is *correct* as a statement about local exponents, and Jimbo's dictionary then
  forces `γ = 1`. So `γ = 0` fails on the companion's own data, whatever one
  concludes about apparency. C2 now rests on two independent grounds, and the
  weaker one does not rely on any lemma proved in this run.

A third result: a full-text pass located every passage in v1.2 depending on
apparency, now section **C5**. The substantive casualty is **§7.1 item 1**,
which offers apparency as the first of four components of a "complete
explanation" for the identification obstruction. The other three survive.

Deliverable: `GATE1-VERIFY.md`.

## R8.4 Gate 3 — one wording defect, fixed

* "Necessary condition" language on every row match: **present. PASS.**
* C3 verbatim as drafted: **FAILED, now fixed.** The notice read *"The operator
  has the local formal type…"* where the drafted text names the object:
  *"System C has the local formal type…"*. That is precisely the per-object
  ambiguity C4 exists to forbid, and "operator" is additionally overloaded in
  this repository, where it denotes the human principal. Corrected.

## R8.5 Gate 2 — cold read of C4

`CT-S13-COLDREAD5` initially **halted correctly**: it was dispatched before its
packet existed, and it refused to read named evidence it could not find rather
than improvising. That ordering error was mine. The packet
(`coldpackets/PACKET-C-surface-labels.md`) was then written and the session
resumed under the same isolation rule.

*(Outcome recorded below once the session returns.)*

### R8.5 (cont.) Gate 2 — PASS with a defect found

`CT-S13-COLDREAD5` returned. Katz data and both table lookups were independently
reproduced in its own code, with Table 2.1 read from the page images. It
returned **ERROR** on (A6), the family-membership inference — which was already
the operator's stated position — and, more valuably, it found something this run
did not have.

**The new finding, independently re-verified by me from the PDF.** On p. 2634,
immediately before the table, van der Put–Saito write that the strong
Riemann–Hilbert problem has a positive answer for every type **"except possibly
for `(1/2, −, 1/2)` and `(−, −, 5/2)`"**, and that for those two types they
consider only the modules for which it *does* hold. **`(1/2, −, 1/2)` is object
A's type.** Of ten families, object A sits in one of the two exceptional rows.
The PIII(D₈) row is thus restricted by a condition nobody has checked for object
A. This is now C4 point 5.

The reader also raised the scalar-operator-to-rank-2-connection gap (point 6)
and `dim P = 0` for the PIII(D₈) row (point 7), the latter bearing directly on
C3's single-fibre objection.

**One caveat declined, on evidence.** The reader flagged the three-entry
notation `(1/2, −, 1/2)` as a contraction of a four-column table. Its
ordered-column point is right and was adopted; its premise is not. The same page
reads *"We will not number these ten families, but indicate them by their Katz
invariants, e.g., (0, 0, 0, 0), (0, 0, 1), …, (−, −, 5/2)"* — the three-entry
form is **the authors' own**. An isolated reader could not have resolved this;
it needed the running text.

C4's review status moves `self` → **cold**. Gate 2 **CLOSED**. This is the
second time a cold read has caught a load-bearing gap under a confident label.

---

# R9 — Operator review #6 (C4 wording, C2 order, §7.1 scope)

## R9.1 `dim P = 0` — a conflation, corrected

The operator caught a defect in C4 point 7 that I had adopted from CT-S13
without challenge. `P` is the **parameter** space; `dim P = 0` means PIII(D₈)
has **no free parameters**, which is expected and is not a defect. It says
nothing about the isomonodromic **time**, which still gives a one-dimensional
deformation.

CT-S13 linked `dim P = 0` to C3's single-fibre concern, and I carried that link
into the notice. It is a conflation: **C3 concerns the absence of a written
deformation, not the absence of parameters.** Point 7 now states only that the
family has no free parameters, and whether object A lies in a deformation is
kept as a separate open question.

A lesson for this run's method: a cold read catching a real defect (the strong
Riemann–Hilbert restriction) does not make its *surrounding* reasoning safe to
adopt wholesale. The correct finding and the conflation arrived in the same
paragraph, and I checked only the former.

## R9.2 The quadratic cover as a possible route — CONJECTURED, no weight

Object A's cover lands in `(1, −, 1)`, which is **not** one of the two types
exempted from the strong Riemann–Hilbert guarantee. Whether that helps decide
the condition for object A itself is **unverified**. Recorded in the notice as a
possible approach only, labelled **CONJECTURED**.

## R9.3 C2 reordered to lead with the published-sources-only ground

Ruled: **yes.** C2 now opens with `γ = 1 − θ₀ − θ_t = 1`, which uses only the
companion's own `θ₁ = θ₂ = 0`, the companion's own stated scaling law, and
Jimbo's published dictionary — all verifiable by a reader from published sources,
with no lemma proved in this run. The apparency ground via **C1** follows as
explicitly labelled independent corroboration.

## R9.4 §7.1 — record, do not rebuild

Ruled: **do not re-argue.** C5 now states that item 1 is refuted, withdraws the
"complete explanation" characterisation, and says items 2–4 do not depend on
apparency **and that their correctness is not re-examined in this notice**.

The words *survive*, *stand* and *unaffected* are avoided deliberately: nothing
in this work has independently checked items 2–4, and those words read as
endorsement. My own R8 text had used "survive", which was the error. The same
scope statement now attaches to §2.2's untouched conclusions.

## R9.5 Deposit-day checklist added, deliberately not executed

Four external citations listed for the P0 re-fetch-and-hash pass, to be run
**immediately before uploading** so the hashes match what is cited on the day.
The checklist records that **hypotheses as well as theorem statements** are in
scope — the Gautschi (2.8) lesson.

Claims `R1-56`–`R1-60` appended, all `self`: these are authoring changes to the
draft, and no independent party has read the revised wording.

---

# R10 — Operator review #7

## R10.1 Author request finalised

Both authorised edits applied: **§2.9 → §2.9(ii)**, and "your paper" → **"your
paper in *Studies in Applied Mathematics*"** (journal named in full rather than
by nickname). The DOI remains. The draft is ready to send; finding an address
and sending are operator actions and have not been done.

## R10.2 The method lesson added to P0

> Findings from a review are adopted claim by claim. A correct finding does not
> certify the reasoning around it; each adopted statement is verified on its own.

Recorded in `P0-CITATION-RULE.md` with its evidence, and with the observation
that this rule and the citation rule address the same failure from opposite
directions: one says do not trust a *rendering* of a source, the other says do
not trust a *verdict* on one.

## R10.3 A defect in this session's own AEAL record

The R8 batch was numbered `R1-44`–`R1-51`, but `R1-44`–`R1-49` were **already in
use** by R7. Six duplicate `claim_id`s — which breaks exactly the traceability
the record exists to provide. Found while building the dependency list, not by
looking for it.

Repaired by `repair_claim_ids.py`: the six R8 occurrences renumbered to
`R1-61`–`R1-66`, each carrying `renumbered_from` and a `renumber_note`; no claim
content altered; prose cross-references updated. **All 210 `claim_id`s are now
unique**, and the check is cheap enough to run every round from here.

## R10.4 Deposit dependency audit — five gaps, one material

The operator's count was right at the level of each item's *headline* claim.
Beneath them, 47 supporting claims feed C1–C5. **42 clear**, by one of four
routes: `cold`; INSPECTED; **is** a cold session's output; or independently
recomputed by a named cold session.

The fourth and third routes matter. A cold session's own claims are marked
`self` — correctly, since a session cannot cold-read itself — **yet those claims
are the independent work**. Scoring them as unreviewed would double-count the
isolation rule against itself.

**Five gaps. The material one is object B:** `S4-06` and `S5B-C6` have never had
a cold read. CT-S13 covered System A and its cover only. Row B is also the row
carrying the delicate *"up to inversion and twist"* qualification, whose wording
already needed one correction — and it is the row bearing the `D̃₅` label whose
misattribution is the entire subject of C4.

Recommendation: a short cold packet for object B before deposit. The other three
gaps (`CT-S9-PVPARAMS-C014`, `R1-56`, `R1-57`) do not warrant delay.
→ `DEPOSIT-DEPENDENCIES.md`

## R10.5 The citation rule caught me, not a source

`R1-53` and `R1-54` are load-bearing and were originally re-verified from the
**PDF text layer**, not a page image — contrary to the rule this session
authored. Both have now been read from `vdps_p2634.png` and are confirmed
verbatim, along with the sentence establishing that `P` is the space of
*parameters*, which is the textual basis for the operator's `dim P` ruling.

First time the rule has caught this session rather than an external source.

## R10.6 Backup made; licences reviewed; Lean deprioritised

**Backup:** `C:\LocalWork\_siarc-session-backups\sessions-2026-09-17_20260917-202213.zip`,
30.9 MB, sha256 `9CE442A4…DD5202`, excluding `lean/.lake/` and `__pycache__`,
stored **outside the repository** so a `git clean` cannot reach it.

**Licences** (`REFS-LICENCE-REVIEW.md`): do **not** commit `refs/` wholesale.
`gautschi_p34_bot.png` is a page image of a SIAM-copyright article and must not
be committed; the DLMF HTML captures should be cited by URL and release version
instead. The AIF licence string and the Zenodo deposit licence are both **NOT
CHECKED**, and were not guessed; both fold into the deposit-day pass. The
recommended arrangement is to commit a **manifest** — URL/DOI, sha256, retrieval
date, licence — which is what the P0 rule needs anyway.

**Lean deprioritised.** With the radius theorem now known to be a corollary of
Perron–Kreuser, the 7 `sorry`s in `XiZero.lean` support no novelty claim and
block nothing. They remain of interest only as a Mathlib contribution or as
formalisation practice.

---

# R11 — operator review #8: route-4 provenance, invariants, object-B cold read

## Items ruled on

| # | Ruling | Status |
|---|---|---|
| 1 | Route 4 must record the `claim_id` it was recomputed against | done; the audit now verifies each named claim exists and reports **BROKEN LINK** otherwise. None found |
| 2 | Add the duplicate-ID check to the per-round invariants, beside Rule 1(a) | done; five invariants, scripted as `check_invariants.py` |
| 3 | Authorise the CT-S14 object-B cold packet | done; packet written **first**, session run, findings adopted claim by claim |
| 4 | Show the remaining gaps as `self` in the notice's support list | done; and two of the five were then cleared by CT-S14, leaving the three deferred by decision |

Housekeeping: backup hash now stored beside the archive rather than only in a
document; archive refreshed; the licence question recorded as one for the
publisher's terms, not for an agent.

## The substantive result

CT-S14 was commissioned to test the weakest support in the notice — the `D̃₅`
row for object **B**, which rested on `R1-20`, a STRUCTURAL claim that had never
been reviewed. It returned more than a confirmation.

**Objects B and C are the same object.** Under `z ↦ 1/x` their trace-free normal
forms are *identically equal*, both being
`(12x⁴+4x³+4x²+11)/(4(3x²+x+1)²)`. Re-derived here independently from the
primary printed data (`verify_s14.py`); the symbolic difference is exactly zero.

Two consequences:

* The `/2` vs `/6` root discrepancy that had sat unexplained in the record —
  **B**'s singular points at `(−1±i√11)/2`, the companion's at `(−1±i√11)/6` —
  is simply the inversion. It was never a discrepancy.
* The twist is not part of **B**'s classification. The `2/x` term produced by the
  pullback contributes nothing to the normal potential, so **inversion alone**
  reaches the trace-free form. The twist by `A^(−1/2)` only converts that form
  into the companion's *printed* scalar operator.

## The operator's question, answered

*"Does the twist that makes B's normal form match System C take B into the class
van der Put–Saito classify?"*

**No — and it does not need to.** The twist alters the trace by
`−dlog A = −(6x+1)/(3x²+x+1) ≠ 0`, and p. 2634 requires `trace 0`, so a
trace-altering twist does leave the classified class. But **B** reaches its
trace-free normal form by inversion alone, and that is where the row is read. The
row stands; the drafted phrase "up to inversion and twist" was both unnecessary
and inaccurate, and has been removed.

## Two corrections made during adoption

The claim-by-claim rule earned its place twice in this round.

1. **CT-S14's task 3 called the integer-difference points "apparent".** Its
   substantive conclusion — *not ordinary* — is correct and is adopted. The word
   "apparent" is not: at each root, `residue(P) = 1` and `lim (x−β)²Q = 0`, which
   are exactly the hypotheses of our own C1 lemma, whose conclusion is that a log
   term is **forced**. The points are regular singular and *non*-apparent.
   CT-S14 was isolated from C1 by design and could not have known this, so the
   defect is in the adoption, not in the reviewer. Recorded as `R1-78`.
2. **CT-S14's task 4 is correct but phrased as though the row were at risk.**
   Its own task 5 says the opposite (re-normalising restores the trace-free
   form). Adopted with the qualification stated above.

A third item was a false alarm worth recording: my verification script's set
comparison of the inverted roots printed `False` on values that are visibly
equal. It was a SymPy hashing artefact on unevaluated radicals; an elementwise
check confirms the match. Had it been taken at face value it would have read as a
refutation of the central result.

## A defect in this session's own tooling

`append_r11_claims.py` deduplicated by `claim_id` and **silently skipped** three
of eleven claims whose IDs had already been used in round R10 — and the three
dropped were the ones carrying the central CT-S14 result. Nothing failed; the
script printed `appended 8 new claims (3 already present)` and exited zero.

This is the same class of defect as the six duplicate IDs found in R9, and it
shows the R9 fix was incomplete: the invariant detects duplicates *after* the
fact, but the append path was still free to lose data quietly. Repaired by
`append_r11b_claims.py`, which **aborts** on collision instead of skipping, and
which also repaired a cross-reference left dangling by the renumbering. Recorded
openly as `R1-85`.

The general lesson matches the one already in P0: a step that cannot fail cannot
be trusted to report failure. Deduplication is not error handling.

## Record state at the end of R11

| | |
|---|---|
| Claims | **234**, all IDs unique, across 16 files |
| Labels | INSPECTED 86 · PROVEN 82 · STRUCTURAL 40 · VERIFIED 24 · CONJECTURED 2 |
| Review | `cold` 19 · `self` 61 · none 154 |
| Invariants | all five pass (`check_invariants.log`) |
| Deposit dependencies | **44 of 47 cleared**; 3 gaps, all deferred by operator decision |
| HEAD | `08aa0e2381b3dc37ee54a3200b7272755ca11d59`, unchanged; nothing committed |

---

# R12-R13 - operator review #9: wording, symbolic-equality rule, load-bearing test

## Rulings applied

| # | Ruling | Status |
|---|---|---|
| A | P0 method note: symbolic equality by simplify-to-zero **plus** a high-precision numeric check, never `==` on unevaluated radicals | done; and applied retroactively to the B-C identity itself (`verify_s14_numeric.py`, dps 60, worst relative residual 1.5558e-61) |
| B | "Same object" is too strong; use **projectively equivalent under z -> 1/z** | done in the notice and in the claim text (`R1-82` patched, `R1-87`) |
| C | Keep B and C as separate rows; add the equivalence beneath; reframe as **two classes**, A vs {B,C} | done (`R1-88`) |
| D | Record the deformation-transport observation and the time-consistency check as a **future problem, not a claim** | done, CONJECTURED (`R1-89`) |
| E | Decide `R1-56` and `CT-S9-PVPARAMS-C014` by load-bearingness | done (`LOADBEARING-TEST.md`, `R1-90`); `R1-56` load-bearing, the other two corroborating only |

## The load-bearing test, and what it caught

`R1-56` is load-bearing: C4 point 7 exists only to state it, and no other content
in the notice supplies it. `CT-S9-PVPARAMS-C014` is corroborating only, because
the notice asserts **openness** - a later positive result would not falsify it -
and C3's fixed-time sentence rests on the separately cold affine computation.
`R1-57` is CONJECTURED on the face of the notice.

Per the ruling that if either needs a cold read both should travel together,
`PACKET-E` carried both as `CT-S15-COLDREAD-DEFERRED`. `R1-57` was not sent: no
cold read could change a sentence that already says "open question, not a claim".

CT-S15 returned **CORRECT WITH WORDING CHANGE** on statement 1 and **CORRECT** on
statement 2. More valuably, it found a sentence on p. 2635 -

> "We will also describe the corresponding one-dimensional families of
> differential modules M(t)."

- which supports point 7 **directly** rather than by inference. `R1-56` no longer
rests on an inference from the definition of `P`.

## The OCR defect - the Gautschi lesson repeating one review later

CT-S15 was supplied with page images and **ran OCR on them**, reporting that the
OCR "retained the line imperfectly". Two transcriptions were wrong:

| Printed | CT-S15 | Severity |
|---|---|---|
| Jimbo (3.1) constant matrix `diag(1,0)` | `(1/2) sigma_3 = diag(1/2,-1/2)` | different matrices |
| `(A1)_PV`: `theta_0, theta_t not in Z` | adds `theta_inf` | **load-bearing hypothesis**; C2 turns on it |

Neither reached the notice - its `(A1)` line and PV dictionary were verified
earlier by direct reading and are correct - but the second is precisely the
Gautschi (2.8) near-miss recurring, on a hypothesis rather than a theorem
statement, one review after that lesson was written into P0.

The rule has been amended: **a load-bearing statement is read by looking at the
rendered page**; OCR is a text layer and does not satisfy it; an agent that
cannot view an image must **halt and say so**. Packets must state that halt
condition explicitly, because listing image files evidently does not convey it.

## A smaller self-caught defect

When wiring the two newly cleared claims into `deposit_deps2.py` I added route-D
entries naming CT-S15 claim_ids I had **not verified existed**. Route A (the
claim's own `review: cold`) takes precedence, so the link check would never have
examined them and the invented ids would have sat in the record unchallenged.
They were removed rather than corrected: the correct route was already A.

## Record state

| | |
|---|---|
| Claims | **259**, all ids unique, 16 files |
| Labels | INSPECTED 97 - PROVEN 82 - STRUCTURAL 51 - VERIFIED 26 - CONJECTURED 3 |
| Review | `cold` 25 - `self` 68 - none 166 |
| Invariants | all five pass |
| Deposit dependencies | **46 of 47 cleared**; the one gap is `R1-57`, CONJECTURED |
| HEAD | `08aa0e2381b3dc37ee54a3200b7272755ca11d59`, unchanged |

---

## R14 — inversion notation normalised to `z ↦ 1/x`

Operator review #10 wrote the map as `z ↦ 1/x` (as review #9 had). The notice and
claims `R1-82`, `R1-87`, `R1-89` carried `z ↦ 1/z`. Since **B**'s coordinate is
`z` and **C**'s is `x`, the form naming both coordinates is the accurate one, and
`R1-82` was internally inconsistent — its own derivation line already read
"pulled back by `z = 1/x`".

Rewritten: notice lines 159, 165, 182; `REPORT.md` R12–R13; claims `R1-82`,
`R1-87`, `R1-89` via `patch_map_notation.py` (in 98 / out 98, all three
confirmed rewritten, aborts if any target is missed).

**Not rewritten**, deliberately: `1/z` inside Zenodo DOIs (`5281/zenodo` contains
the substring), and the earlier `CT-S5B-COVER` uses at `REPORT.md:106,230`, which
concern **object A**'s quadratic cover in the `w`-plane and are a different map.

---

## R15 — CT-S16-MEMBERSHIP-C (operator review #12)

Analysis-only session; **no notice or conjecture file was edited**. Full write-up
in `sessions/2026-09-17/CT-S16-MEMBERSHIP-C/REPORT.md`; 17 claims appended there.

Recorded here because three items affect the standing record:

1. **P0 second amendment adopted** — *confirm the page image actually rendered.*
   `view` takes one image per message; two in one message returns a limit notice
   and displays nothing, and reasoning had begun from unseen page content.
   Caught and stopped. Appended to `P0-CITATION-RULE.md` under the review-#9
   amendment.

2. **A suspected typo in van der Put–Saito p.2655** (family (4.1), entry `b(z)`:
   a missing `t` in the first term), discriminated by the paper's own
   `det A(1) = −θ₁²/4` constraint. Flagged, used for computation, **not adopted
   silently**. Claim `S16-05`. Whether to write to the authors is the operator's.

3. **The C3 "single fibre" concern is, on vdPS's framework, presentational**
   (claim `S16-16`): `t` is an invariant of the configuration, not a free
   parameter, and every point of the moduli space already lies on an isomonodromy
   leaf. **Deliberately not applied to the companion v1.3 notice.** If the
   operator wants C3 reworded, that is a separate instruction; the notice text is
   unchanged by this round.

Corpus after R15: **276 claims**, all IDs unique, all five invariants passing.

---

## R16 — review #13: the twist caveat, the typo, and the C3 rewrite

### CT-S17-TRACEFREE-NORM (new session, 8 claims)

The operator's **conclusion** on the "up to rank-1 twist" caveat is adopted; the
operator's **reasoning** for it is rejected.

* **T1 PROVEN** — the trace-free member of a single twist orbit is unique
  (`λ = −tr(A)/2`). This much of the argument is correct.
* **T2 PROVEN FALSE** — trace-freeness *alone* does not single out a
  representative of a projective class. Counterexample `L = d − 1/(2z)`:
  `L⊗L` trivial (witness `w = z`), `L` non-trivial (residue `−1/2 ∉ Z`).
  Pre-registered as doubted **before** computing.
* **T3 PROVEN** — decisive. Comparing the **pair** `(P,Q)`, not just the
  projective invariant `R`, System C's operator in `z` **equals** the family's
  scalar operator at the located point, coefficient for coefficient. The modules
  are isomorphic, not merely projectively isomorphic. Both vacuity controls fired.
* Membership label **unchanged at STRUCTURAL** — the operator tied any raise to
  step 3(b), still unrun. The *statement* strengthened, not the label.
* One defect caught in this session's own first run: a printed line
  (`L⊗L trivial? False`) that contradicted its own conclusion. Test replaced with
  a residue-based one, self-checked in both directions.

### CT-S16 follow-up (5 claims appended, `S16-18` … `S16-22`)

* **Typo re-verified by looking**, as required: journal **p. 2655** confirmed from
  the running head, and the same error is present in **arXiv:0902.1702v5 p. 34** —
  the authors' own most recent corrected version. No published erratum found.
* Residual carries the factor `(t−1)`, vanishing exactly where the two readings
  agree — the signature of a dropped `t`. Bogus-variant control rejected.
* **Page-offset audit**: journal = 0-based index + 2610 = 1-based page + 2609.
  `render_pages.py` used the 1-based convention correctly, so **every page
  citation in the CT-S16 claims stands**; two ad-hoc crops written this round used
  the wrong convention and were deleted. Caught because a rendered header did not
  match its filename.
* `TYPO-EVIDENCE.md` prepared for the operator's author letter. **Not sent.**

### Notice edits (operator-authorised, review #13)

`DRAFT-COMPANION-v1.3-NOTICE.md`:

1. **C3 body replaced** with the operator's drafted wording, verbatim.
2. Heading changed to *"C3. Conjecture 4.1 mis-states the significance of the
   fixed Painlevé V time"* — **flagged for operator review**, as the old heading
   ("not yet well-posed") contradicted the new body.
3. Two downstream passages made consistent: the "Scope of the open question"
   paragraph (what is open is now *verification*, not the existence of a
   deformation) and the `dim P = 0` note in C4.
4. **Disclosure block added** to C3, as the operator required: a corrected form of
   a published formula is load-bearing.
5. **Support table**: two new rows, `C3 moduli-space membership` and
   `C3 corrected b(z)`, both recorded openly as **`self`, no cold read**.

> **Deposit gate changed.** The dependency audit previously stood at 46 of 47
> cleared, with `R1-57` the only gap. C3 now carries **two further `self`
> supports**. This is an operator decision, not an agent one.

Corpus after R16: **289 claims**, all ids unique, all five invariants passing.

---

## R17 — operator reviews #14 and #15; CT-S18 cold read adjudicated

**Round outcome: the cold read returned ERROR on C3, and the ERROR was overruled
on a point the packet had not thought to name.**

### CT-S18-COLDREAD-C3

Issued verbatim from the operator's packet, with two recorded deviations: p. 2637
added (the `det A(1)` constraint is printed in §3.2, which the stated range
missed), and the drafted C3 **sealed** behind a hash of the stage-1 write-up,
because it states the answers to tasks 1-3. Both deviations were approved at
review #15, and the sealing was adopted as P0's third amendment.

| Task | Outcome |
|---|---|
| 1 — the typo | **ADOPTED IN FULL.** Independently read off p. 2655, same residual factorisation derived in the reader's own code, corrected square shown to satisfy the constraint identically, own bogus-variant control. The `C3 corrected b(z)` row moves `self` -> **`cold`**. |
| 2 — hypotheses | **ADOPTED**, except its last bullet, which inherits task 3's error and misstates it besides. |
| 3 — the chart | **Computation adopted; inference REJECTED.** |
| 4 — verdict ERROR | **REJECTED**, as resting entirely on task 3. |

### The substance

A rank-2 system has **two** scalar reductions - the ODEs satisfied by its two
components - differing by `d/dz log(c/b)`. CT-S17 compared System C against the
`b`-route; CT-S18 against the `c`-route. Both computations are correct; they are
not the same computation. `adjudicate_s18.py` derives both generically by
elimination with no formula assumed, then settles which is System C by a control
that depends on neither prior session: solve the **system** at an ordinary point
and test which ODE its `y1` component satisfies. Route 1 residuals `4.8e-61`,
`6.9e-62`; route 2 residuals `9.0`, `4.0`, over two seeds. System C is route 1,
exactly, and `P - P_C = Q - Q_C = 0` there.

There is a structural reason as well, and it is the paper's own: vdPS define `q`
as the unique zero of `c(z)`, so the `c`-route equation has an apparent
singularity at `z = q`. System C has no third finite singular point, so it cannot
be the `c`-route for **any** point of the chart.

### Two defects in the cold read, recorded

1. Its `P` control was `assert simplify(Pfam - Pfam) == 0` - identically zero for
   any `Pfam`, so it could not fail, and it sat directly beneath the assertion
   that drove the ERROR verdict. The recurring defect family again, in a session
   explicitly instructed against it.
2. Its mismatch was evaluated only at a **generic** sample, never at the located
   point. Since the route-2 mismatch `-1/(z-q)` has no zero in `z`, the test could
   only ever return "mismatch".

Neither touches task 1, which was derived and controlled independently.

### A defect of mine, caught by the invariants

The adjudication claims were first appended as `S17-08...S17-13`, colliding with
an existing `S17-08`. The **duplicate-ID invariant added at review #12 fired**
and the append was rolled back from `claims.jsonl.bak-r17` and redone with
collision-safe allocation. This is the first time that invariant has caught a
real defect.

### Other work this round

* Notice **opening summary** added: two corrections (C1, C2), one clarification
  (C3), one label question (C4), one scope tabulation (C5), stating plainly that
  C3 is the one item that comes out in the companion's favour.
* **C3 heading** settled by reading Conjecture 4.1 verbatim from a page image: it
  makes **no assertion about `t` at all**, so the accusatory heading is not
  supportable and the neutral one stands.
* **Licence correction**, wider than review #14 asked: the AIF title page reads
  *"tous droits réservés"*; free-to-read was conflated with
  free-to-redistribute. Standing hold added - everything under any `refs/` stays
  local until its own row is checked - plus P0's fourth amendment, including that
  arXiv licences are per-submission and the default grants third parties nothing.
* **Letter to van der Put and Saito** finalised with the bracketed entry filled,
  and **held**; sending and address confirmation remain the operator's.

### Deposit position

`C3 corrected b(z)` is now **cold**. `C3 moduli-space membership` stays **`self`**
- a challenge raised and survived is not an independent confirmation, and the
resolution was performed by me adjudicating a session of my own. Of 49 supporting
claims, 47 cleared; the two open are `R1-57` (CONJECTURED, no weight) and the
membership row.

Backup `sessions-2026-09-17_20260918-104714.zip`, 386 files, 40.4 MB, sha256
`27cdc28a11d7fb6aba6b8f552956a367ca316f5e4e703e0d913602dcee1ae51e`, sidecar
stored outside the archive.

---

## R18 — CT-S19 reissued packet; the last substantive gap clears

### CT-S19-COLDREAD-MEMBERSHIP

Commissioned on my own initiative after R17, because the membership row was the
notice's one substantive `self` claim and R17 had identified exactly why the
previous reader failed: it silently chose a component. The reissued packet named
that as **task 1**, without saying what the previous reader had chosen or what
came of it.

**Verdict: CORRECT WITH WORDING CHANGE. The row moves `self` -> `cold`.**

The packet worked better than intended. The reader answered task 1 **from the
source**, quoting p. 2655:

> *"The first basis vector is chosen as cyclic vector and following Subsection
> 4.1, `q` is the unique zero of `c(z)` and `p = a(q)`."*

I rendered and looked at the page: the quotation is verbatim. This settles the
component question by the authors' own stated convention and **supersedes** the
structural argument in `VERIFY-S18` while confirming its conclusion. The reader
also noticed unprompted that `q`, being read off `c(z)`, bears on the *second*
component - the precise trap CT-S18 fell into.

### A corroboration nobody designed

CT-S19 derived its own point of `U₀` from scratch and landed on the **opposite
branch** to CT-S17:

| | `t` | `θ∞` | `√33` term of `q` |
|---|---|---|---|
| CT-S17 | `−2i√33/9` | `−2 − √3/9` | `+281700i/122408` |
| CT-S19 | `+2i√33/9` | `−2 + √3/9` | `−281700i/122408` |

Re-verified in independent code (`adjudicate_s19.py`): both give `db/dz = 0`,
`q ∉ {0,1}`, `P − P_C = Q − Q_C = 0` exactly, `t² = −44/27`; `t₁₉ = −t₁₇` exactly;
controls fired on 3/3 perturbations. Two isolated sessions between them exhibit
**both signs** of the companion's printed `t = ∓2i√33/9`.

### One part of the wording change declined, and recorded as a judgement

The reader wanted *"Membership on a single isomonodromic leaf follows from the
framework"* dropped, because **it** had not computed monodromy/Stokes data. That
is a statement about the scope of its own check: the sentence attributes the leaf
to vdPS' framework, which the reader was not asked to verify and could not have
(its packet contained no monodromy data), and the sentence already marks the
computation as not done and **open**. The sharper locution *"exhibited explicitly
in the chart `U₀`"* **is** adopted. The reader's full alternative is preserved
verbatim in its `VERDICT-5.md` for the operator, who drafted the original.

### The letter changes — a stronger argument found on the page

While checking the CT-S19 quotation I looked at p. 2655 in full and saw that the
bracket whose `t` is missing in `b(z)` **appears a second time on the same page**,
in `B₁` of the display `B = zB₀ + (1/t)B₁`, where its `(1,2)` entry prints
`(p + ½(q−1)q t)²` **with** the `t`. The same asymmetry is in arXiv v5 p. 34.
Verified symbolically: under the corrected reading `b(z)`'s first term is exactly
`z · B₁[1,2]`; under the printed reading it is not, and three bogus variants are
rejected. The difference between readings factors as
`−z(q−1)(t−1)(4p + q²t + q² − qt − q)/4` — the **same** factor as the `det A(1)`
residual, so two independent tests agree term for term.

This is the stronger argument, because it appeals only to the authors' own page
rather than to the correctness of a constraint, and it evidences a **transcription
slip** rather than an inconsistency. The letter has been redrafted to lead with it.
It remains **unsent**.

### A defect of mine, caught and fixed

The R18 entry and the `DEPOSIT-DEPENDENCIES` update were first written with
shell-style escaped apostrophes inside a PowerShell literal here-string, where
everything is taken verbatim. Eight mangled apostrophe sequences were written
into the record, then repaired by a scripted replace that reported its count (8)
and verified none remained.

A second, better one: the first attempt to insert *this very note* used
`python - @"..."@`, which opened an interactive interpreter, consumed the script
as terminal input, did nothing, and **exited zero**. It was caught only because
the result was checked rather than assumed. That is the recurring defect family
again — a step that cannot announce its own failure — and it is worth recording
that it caught me while I was writing the paragraph about catching it.

Both are cosmetic. They are recorded because the rule is that the trail shows
what happened, not only the tidied result. The backup was re-taken afterwards.

### Deposit position

**48 of 49 supporting claims clear.** The sole remainder is `R1-57`, CONJECTURED
on the face of the notice and carrying no weight. `C3 corrected b(z)` is now
**cold ×2**.

Corpus 330 claims in 21 files, all five invariants pass.

---

## R19 — operator review #16: the open item re-framed, and a P0 rule against silent writes

### The open mathematical item was mis-framed, and the operator corrected it

I had been carrying the forward item as *"whether the B/C class embeds in an
isomonodromic PV deformation"*. The operator ruled that this understates what
the run established, and that a future session reading it could redo work
already done. The ruling, and it is correct:

> CT-S16 and CT-S17 answered that. C's trace-free connection is a point of the
> moduli space, the vector field is regular there, so a unique leaf passes
> through it, and B follows by projective equivalence under z to 1/x. The result
> is STRUCTURAL, resting on the framework rather than on an independent
> computation.

**The open item, stated correctly from here on:**

> Independent confirmation of leaf membership by computing the monodromy and
> Stokes data of System C and of the PV-transported system at a nearby time, to
> the pre-registered 30-digit threshold (step 3(b), gap `S16-15`).

Existence of the leaf is settled at STRUCTURAL; what is open is the
**verification**, not the existence. This matches what the notice already says
at C3 and what claim `S16-15` already says — the defective phrasing was in my
round summaries only, which is where the correction was needed. No claim text
changed, because no claim carried the bad framing.

### On the CT-S18 verdict — correcting an inference, not a record

The operator read the "48 of 49" line as implying CT-S18 returned clean. It did
not. **CT-S18 returned ERROR**, and I overruled its verdict while adopting its
task-1 finding. Both halves matter and the summary should have said so plainly:

* Its **task 1** independently reproduced the `b(z)` typo, including the same
  residual factorisation. That is what moved the `corrected b(z)` row to `cold`.
* Its **tasks 3 and 4** compared the wrong component of a rank-2 system — the
  `c`-route rather than the `b`-route — and the ERROR verdict rests on that.
  `adjudicate_s18.py` settled the component question by a control depending on
  neither prior session.

The deposit gate was cleared by **CT-S19**, the reissued packet that named the
component question explicitly, not by CT-S18.

### P0 fifth amendment — a write is not done until it is read back

Adopted from the operator's observation that the append path dropping three
claims and `python - @"..."@` exiting zero after doing nothing are *the same
failure with different surfaces*. See `P0-CITATION-RULE.md`, fifth amendment.
The rule: any script that writes must read back what it wrote and fail loudly if
the effect is absent; an exit code is never evidence that a write happened.

### Deposit position

Unchanged: **48 of 49**, sole remainder `R1-57`. Corpus 330 claims in 21 files.
Nothing in this round altered a claim.

---

## R20 — the contested gate closed; a claim amended for the first time

*Operator review #18.*

### CT-S20B-COMPONENT returned CORRECT

The isolated cold check of the adjudication — commissioned at review #17 because
a gate on a deposit-supporting claim had been contested by a cold reader and
overruled by the same agent that wrote the claim — returned **CORRECT**, on all
four tasks. Adjudicated task by task in `CT-S20B-COMPONENT/VERIFY-S20B.md`;
adopted as `S17-20` … `S17-25`.

Two results in it are load-bearing beyond the agreement.

**The c-route residual came back as `-1/(z-q)` unprompted.** That is the simple
zero of `c(z) = -(z-q)/(q-1)` at `q`, exactly what the route difference
`d/dz log(c/b)` predicts when `b` is constant at the point. Since `-1/(z-q)` has
no zero in `z`, a comparison against the c-route mismatches at every sample
point and every parameter value. So CT-S18's test **could not have returned a
match under any circumstance** — a stronger and more useful statement than "it
made a mistake", now on the record as `S17-22`.

**The `θ∞` check was genuinely at risk of returning the wrong answer.** Its
second attempt reported *inconsistent* and the value `thi = √3/9` — wrong by
exactly the branch shift, 2. What caught it was an arithmetic control that could
fire and did: the two scalar exponents must sum to `-P1`, and they summed to
`-1` against System C's `-2`. The operator's reading, which I adopt: *a check
that nearly failed for a real reason is worth more than six that pass.*

This is the **converse** instance of the recurring family in this record. Every
prior instance was a step that could not fail and therefore certified nothing —
`assert simplify(Pfam - Pfam) == 0`, the generic-sample test that could only
return "mismatch", `python - @"..."@` exiting zero, the regex scan that flagged
71 of 74. This one is a control that fired, inside a check that would otherwise
have returned a confident wrong answer. Recorded as `S17-25`.

### What CT-S20B is not

It was not independent of `inputs.md`, which I wrote, and it was handed the
point rather than locating its own. It is **not** a second independent location
of a point of `U₀`; `CT-S19` is that. It tested the disputed step and nothing
else, which is what it was commissioned to do. Stated in `S17-24` and in the
support table, so that the row is not read as stronger than it is.

### `S17-09` amended in place — and why that needed saying out loud

The operator's point: CT-S20B reported the **orientation** of the sign and
flagged that identifying `n21/n12` with `c/b` relies on `§1`'s common
denominator. Neither changes the claim, but the claim text should carry the sign
convention so that a future reader does not rederive it backwards.

This is the first time in this run that a claim's text has been changed rather
than superseded. The prior text is preserved verbatim in
`CT-S17-TRACEFREE-NORM/claims.jsonl.bak-r20`, quoted here, and the amendment is
itself a claim, `S17-26`.

> **`S17-09`, as it stood:** "A rank-2 first-order system Y' = N Y admits TWO
> scalar reductions, the ODEs satisfied by its two components. Derived
> generically by elimination with no formula assumed: route 1 (for y1) has
> P = -tr N - n12'/n12, route 2 (for y2) has P = -tr N - n21'/n21. **They differ
> by d/dz log(c/b)** and are both correct. Neither is "the" scalar equation of
> the connection."

The amended text keeps every word of the mathematics and adds two sentences: the
orientation (route 1 minus route 2 equals `+d/dz log(c/b)`, i.e. `c'/c - b'/b`),
and the proviso that the general statement is `d/dz log(n21/n12)`, which reduces
to `d/dz log(c/b)` only because `N = -A/D` divides both off-diagonal entries by
the same `D`. The label is unchanged at PROVEN.

The bracketed provenance note is inside the claim text itself, so the amendment
cannot be read as the original.

### One correction to the operator's summary

The review says "P0 has five amendments". It has **six**: the sixth, *name the
component or the cyclic vector*, was added at review #17 and is at
`P0-CITATION-RULE.md` l.364. It is the amendment that this very round
vindicated, since CT-S18 failed for want of exactly that instruction. Recording
the discrepancy rather than silently agreeing.

### Deposit position

**48 of 49**, sole remainder `R1-57`, unchanged — but the `C3 moduli-space
membership` row now rests on an independent resolution rather than an in-house
one. Corpus **337 claims in 21 files**: seven appended, one amended, none
removed.

### Queue

Items 3, 4 and 5 of the operator's list — the deposit-day citation pass and
deposit, the vdPS letter, the Wong–Li purchase — are **operator actions** and
were not performed. Nothing was committed, deposited, sent or bought.


## R21 — the seventh amendment, and the manifest that did not exist

*Operator review #19 asked for one thing: that S17-22 be lifted out of the sixth
amendment's consequence clause and written into P0 as its own line. Doing that
was half an hour. Checking the round's own commit-readiness claim, which was the
other half of #19, took the rest and produced two findings that were not on
anyone's list.*

### The seventh amendment

Written at `P0-CITATION-RULE.md` §Seventh amendment. The operator's framing is
the one adopted: the earlier family was **steps that could not fail**, and this
is a **step that could not succeed**. Both certify nothing, and the second is
worse, because it arrives as a confident negative verdict that looks like a
finding. CT-S18's ERROR read as a real defect for two rounds and cost two
further cold packets to clear.

The diagnostic, in one line: *what would this test have returned had the claim
been true?* If the answer is the same thing, the test has not been run.

Claim `R1-102`, STRUCTURAL.

### A false claim in this round's own record — `R1-103`

`R1-103` was written to close #19's commit-readiness item. It said:

> *"`refs/` is excluded mandatorily under the licence hold (fourth amendment)
> and `lean/.lake/` for size; both exclusions were re-verified at this round's
> backup, which included 454 files and skipped 124116 excluded paths."*

**The first half is false.** `make_backup.py` carries
`EXCLUDE_DIRS = {".lake", "__pycache__", ".git"}` and no `refs` entry; the
archive holds **34** `refs/` paths. The clause *"both exclusions were
re-verified"* describes a verification that never happened — and it is the
seventh amendment's own failure mode in miniature, an assertion about a check
whose result was assumed from its plausibility.

What makes it worth recording rather than quietly fixing is *why* it was caught:
the sentence **named a mechanism**, and naming a mechanism invites reading it.
Had it said only "the backups are safe", nothing would have prompted opening the
script.

The error is a conflation of two holds that had been running under one word:

| hold | what it governs | is it in force? |
|---|---|---|
| retain locally | the backup archive | `refs/` **is** included — correct and intended |
| do not redistribute | commit, deposit | was **not** mechanised at all |

A backup that omitted the reference bytes would defeat its own purpose. The hold
is about redistribution. So the claim was not merely unverified — it named the
wrong side of the distinction. Amended in place under the R20 precedent (backup
to `.bak-r21b`, prior text quoted above, provenance note inside the claim text,
label unchanged, amendment itself claimed as `R1-104`). No downstream claim had
cited it.

### The finding underneath: the manifest route was a decision, not an artefact

Checking the redistribution side turned up something larger.
`REFS-LICENCE-REVIEW.md` recommended committing **a manifest of hashes** instead
of the reference bytes. The recommendation was adopted in prose, cited in later
rounds as though in force, and described to the operator as one of the two
things standing between the record and a bad `git clean`. In fact:

- **no manifest file existed** anywhere under `sessions/2026-09-17/`;
- the repository has **no root `.gitignore`**;
- the only mechanical exclusion in the tree was `CT-S1-THEOREM/lean/.gitignore`,
  covering the Lean build directory, for size and not for licence.

So a `git add sessions/` on the morning of R21b would have staged **all 69**
files under `refs/` and `pages/` — including the whole-page *Annales de
l'Institut Fourier* renders and the Gautschi page image, the two items the
review names explicitly as DO NOT COMMIT. The hold was carried entirely by the
intention of whoever next typed the command.

`REFS-MANIFEST.md` now exists: path, byte length and full sha256 for all 69, the
artefact the route had only ever named. Claim `R1-105`.

### And a gap in the inventory the deposit gate reads

Building it exposed a second gap. **40 of the 69** third-party files have **no
row** in `REFS-LICENCE-REVIEW.md`. The whole of `CT-S8-LITCHECK/refs/` and
`CT-S9-PVPARAMS/refs/` had never been enumerated — among them seven *complete
third-party articles* rather than page regions (Gautschi 1967, Perron 1913,
Nemes 2025, Wang JAT 2014, `polycf`, `bt1933`, Jimbo 1982 PRIMS), their
extracted-text derivatives, and fifteen page images under
`CT-S16-MEMBERSHIP-C/pages/`.

Nothing was exposed: the hold's wording reads *"everything under any `refs/`
directory"*, which covers them. What failed is that **the wording and the
inventory diverged, and only the inventory is machine-readable**. Every one of
the 40 is recorded **NOT CHECKED**. No licence determination was made for any
file this round, and none will be made except by reading the licence on the item
itself. Claim `R1-106`.

### The mechanism, verified by effect

`sessions/2026-09-17/.gitignore`, written at R21b. Patterns exclude directory
*contents* rather than the directories (`**/refs/*`, `**/pages/*`) precisely so
that a negation can re-admit session-produced scripts (`!**/refs/*.py`) — git
cannot re-include a file whose parent directory is excluded.

Verified by `git add --dry-run`, which stages nothing and is reversible:
**391** paths would be added, of which **exactly one** lies under `refs/` or
`pages/` — `CT-R1-AUDIT/refs/parse_dlmf.py`, written in this run and re-admitted
by the negation. `git ls-files --others --ignored` reports **97** ignored paths.
Zero third-party bytes would be staged. Claim `R1-107`, VERIFIED.

This is preparatory and reversible. **Nothing was committed.**

### Two counting failures, and an extension to the fifth amendment

`git check-ignore -v` printed the *negation* pattern for `parse_dlmf.py` while
still **exiting 0** — which reads as IGNORED and is the reverse of the truth. A
tool's exit status is not its answer; the dry run settled it.

Worse, a PowerShell statement that invoked `git add -n` twice in one line and
counted the second reported **7** stageable paths against a true **391**. It
exited zero. Seven is *plausible*, and it would have supported the conclusion
that almost nothing was stageable — the exact opposite of `R1-105`. It was
caught only by re-running the enumeration alone. Two counts given to the
operator earlier in the round (*71 files*) were also wrong; the figure is **69**.

The fifth amendment is extended accordingly: **the readback rule covers counts,
not only writes.** A quantity that will be reasoned from is re-derived in a
separate invocation, and a plausible number is the dangerous case — an
implausible one gets checked. Claim `R1-108`.

### Position

Claims **344 in 21 files**, all identifiers unique, all five invariants pass.
Deposit position unchanged at **48 of 49**, `R1-57` the sole remainder. The R21b
findings are about the *record's own handling*, not about any deposited claim,
so no support row moves.

### Queue

Items 3, 4 and 5 — the deposit-day citation pass and the companion v1.3 deposit,
the vdPS letter, the Wong–Li purchase — remain **operator actions** and were not
performed. Nothing was committed, deposited, sent or bought. Committing the
session tree is now *safe to attempt*, in the narrow sense that the held bytes
can no longer be staged by accident; whether to commit remains the operator's
call.

## R23 — CT-S21 deposit preparation

Packet `CT-S21-DEPOSIT-PREP`, then the operator ruling on M1. Output
`CT-S21-DEPOSIT-PREP/DEPOSIT-READY.md`; claims `S21-01` .. `S21-23`.

**Round 1 — the gate.** Re-fetched all five cited sources (four byte-identical
to the local copies), read ten page images one per message, recorded licence
strings as printed, and ran the consistency scan. Verdict: **not ready**, six
items. The largest was not an error in the notice: **C5's tabulation was
incomplete**, and incomplete in the companion's favour.

**The Theorem 3.1 finding.** v1.2's own §3 already proves C1's local analysis —
`p₀ = 1`, `q₀ = 0`, `I(ρ) = ρ² = 0`, the logarithm in `y₂` only — and Step 4
**displays the monodromy as `[[1, 2πi], [0, 1]]`**, unipotent and not the
identity. Theorem 3.1(ii)'s claim is about the *effective* monodromy on `M₁₁`,
which is weaker than and independent of apparency. The notice as drafted would
have read as though §3 fell with Remark 2.2.

**Round 2 — the ruling applied.** C1 gained a scope limitation; C5 gained the
`Remark 3.2` row and a statement of three deliberate exclusions:

| passage | rests on | in C5? |
|---|---|---|
| Remark 3.2 | apparency, stated flatly without the `M₁₁` qualifier | **yes**, dependency only |
| Remark 4.2 | `θ₁ = θ₂ = 0`, which **survives C1** | no |
| Remark 6.7 | Theorem 3.1(ii), unadjudicated | no |
| Theorem 3.1 | — it is the *source* of the correct computation | no; under C1 |

`θ₁ = θ₂ = 0` survives because it is the difference of the local exponents,
both `0` by the double root C1 establishes; `θ = 0` is exactly the resonant case
in which logarithms occur. **C2 is therefore safe**, resting on those values.

**Three defects in the gate itself**, all found by reading output rather than
exit codes, and all now controlled by `scripts/control_item4.py`:

1. a **false negative from hard wrapping** — a hedge reported missing that was
   present, wrapped across a blockquote line;
2. a **check that could no longer fail** — the C4 test hardcoded `"Four
   points"`, so correcting the notice to `"Seven"` left it matching nothing and
   passing silently. The seventh amendment's failure mode, inside the gate built
   to catch it;
3. a **substring search with no polarity** — `author-confirmed` matched the
   notice's own `"nothing here is author-confirmed"`.

**Corrections to my own record.** `R1-107` ("zero third-party bytes would be
staged") was **false** and is amended in place: nine third-party files were
still stageable. `.gitignore` now default-denies media, verified by effect,
17 → 0. An earlier draft of `DEPOSIT-READY.md` also mislisted the CT-S18/S19
packet images as exposed; re-deriving the count corrected it.

**Result: the notice is ready**, subject to two deposit-day confirmations.

## R24 - references for v1.7, and three corrections to my closing summary

Operator review #21 corrected three things I had stated wrongly when closing R23.
Recorded here because two of them would have misdirected a future session.

1. **The letter that was sent was the vdPS typo report.** I listed a *Wong-Li
   letter* as outstanding. There is none: the correspondence route is dropped -
   R. Wong retired in 2019 and is emeritus - and the plan is purchase.
   AUTHOR-REQUEST-WONGLI.md is now marked **SUPERSEDED - do not send** at its
   head, retained only for the title trap it caught (R1-61).
2. **The Springer-contents check is done**, not pending. Wong & Zhao 2022
   confirms at section 3 that Wong-Li II covers the equation class; the growth
   law is **NOT FOUND in section 3 by full-text read** (CT-S21, pp. 12-20,
   six positive controls fired; outputs/wz_sec3_absence.json). Stated as an
   absence claim, not as "the survey does not state it". The purchase is
   warranted.
3. **Two free references pulled into `refs/`.**

All three identifiers were verified before being recorded, none transcribed:

| identifier | resolves to | licence as printed |
|---|---|---|
| DOI 10.1002/sapm1992874289 | Wong & Li, *Asymptotic Expansions for Second-Order Linear Difference Equations, II*, Stud. Appl. Math. **87**(4), 289-324, 1992-11 | n/a - paywalled, **NOT OBTAINED** |
| arXiv:2204.09305 | Wong & Zhao, *Recent Advances in Asymptotic Analysis*, Anal. Appl. 20 (2022) 1103-1146 | **CC-BY-4.0** |
| arXiv:2306.05930 | Ibrahim & Salvy, *Positivity certificates for linear recurrences*, SODA 2024 | **CC-BY-4.0** |

The DOI record matches P0-CITATION-RULE.md exactly, **II** and *linear*
included. Both arXiv items print CC-BY-4.0 and so carry a redistribution right,
unlike arXiv:0902.1702 - they are the first third-party files in `refs/` cleared
on evidence rather than left NOT CHECKED. `acquire_refs.py` refuses to download
unless the licence check passes.

**One flag, S21-26, labelled CONJECTURED.** arXiv:2306.05930 is real and the
identifier is verified, but its title is about positivity certificates and does
not obviously name the result attributed to it (that a dominant solution leading
coefficient is not exactly computable in general). That content claim, and the
Wong-Zhao section 3 reading, are both the operator's and are **not** independently
checked here. They must be located and quoted before framing the contribution for
K and r_infinity in v1.7.

## R25 — the two attributions checked against the PDFs (CT-S21, cont.)

Both items §R24 recorded as the operator's own readings, one of them flagged
CONJECTURED, were checkable here: both PDFs are in `refs/` under CC-BY-4.0. So
they were checked rather than left attributed. Full detail in
`CT-S21-DEPOSIT-PREP/outputs/refs_attribution.md`.

**1. arXiv:2306.05930 — located; the paraphrase overstated it.** The passage is
on printed **p. 5**, §2.3 "Asymptotics", read from a rendered page image. The
certified interval, the inability to exclude 0, and the name *connexion problem*
are all as described. Two corrections:

- The paper says *"we do not know how to compute the leading coefficient exactly
  in general"* — a statement about the **state of the art**. It does **not** say
  the coefficient *is not computable*, which is a statement about the world.
  For the v1.7 framing of K and r_infinity this cuts both ways and must be
  quoted in the weaker, printed form.
- It is **background**, confirmed structurally: §2.3 is in the preliminaries,
  and the authors' contribution begins at §3, printed p. 6. Cite as the standard
  situation, not as their theorem.

`S21-26` is amended in place to **INSPECTED**, superseded by `S21-28`; the
`.bak-s21refs` copy is retained.

**2. Wong & Zhao §3 — class confirmed, growth law NOT FOUND.** §3 spans PDF
pp. 12–20, fixed from the PDF outline and asserted in the script. It **does**
cover this project's class, equation (3.2)
`y(n+2) + n^p a(n) y(n+1) + n^q b(n) y(n) = 0`, via Wong & Li [100] — the
operator's reading confirmed (`S21-30`).

The growth law is recorded as an **absence claim in the INSPECTED form the
operator requires** — "NOT FOUND in §3 by full-text read", with scope and
method, not "the survey does not state it" (`S21-31`).

**The absence test was built so it could fail.** A bare absence test cannot: an
empty or mis-scoped extraction would make every pattern "absent" and the verdict
would read as a finding — S17-22's failure mode exactly, a test that fails
uniformly. Six **positive controls** therefore run first over the same extracted
string (§3 heading, "Wong and Li", equation (3.2), "turning point",
Theorem 3.3, and the `K_{n+1}/K_{n-1} = c_n` normalisation). All six fired;
had any not, the script emits VOID and no absence verdict.

**Better than the absence, a structural reason for it** (`S21-32`). §3
normalises the growth away before it starts: at (3.23) it sets `x_n = y_n/K_n`
with `K_{n+1}/K_{n-1} = c_n`, so `K_n` absorbs precisely the product growth, and
Theorems 3.1–3.3 then give uniform Airy/Bessel expansions for `x_n` near
transition points. It is a turning-point theory in a parameter, and `K_0, K_1`
are left "depending on the particular sequence". The growth constant is not
merely missing from §3 — it is normalised out of view. That corroborates
Ibrahim–Salvy: the constant is the part tied to the initial conditions, and the
part nobody computes. **The purchase stays warranted**, and the two references
together sharpen why.

**3. Licence determinations are now version-pinned** (`S21-33`). arXiv licences
are per-submission **and per-version**, so the manifest now records that the
licence was read from the **abstract page, never the PDF**, and pins it to the
bytes held: page-1 stamps give `2204.09305v1` and `2306.05930v2`, and the
**versioned** abstract pages for those exact versions both print CC-BY-4.0. The
version came from each PDF's own margin stamp rather than an API answer about
the current version.

### A new failure mode for P0 — readback does not check intent

Repairing §R24 turned up four sites where a Python source literal had
interpreted escapes: `\refs/` and `\r_infinity` became CR, `\acquire_refs.py`
became BEL. A later text-mode read-modify-write then promoted each lone CR to a
full CRLF, so the damage presented as a spurious line break rather than a
control character (`S21-34`).

**The P0 readback rule did not catch this, and could not.** The script read back
the same already-mangled string it had written, and the comparison passed. The
rule establishes that *a write happened*; it does not establish that *the text
written was the text intended*. The mangling was upstream of the write.

Proposed **eighth amendment**: a write whose content is composed in source must
be verified against a property the source literal cannot vouch for — e.g. scan
the result for control characters, or compose the text in a separate file and
append it byte-wise rather than through a string literal. This round's §R25 was
written the second way.

The tree was scanned; `AUDIT.md` is now clean, and the remaining stray control
characters live only in raw PDF text extractions under `CT-S9-PVPARAMS/outputs/`,
where they are artefacts of the sources.

## R26 — a mangled macro in the deposit object, found on the way to the walkthrough

Preparing the deposit runbook meant reading the notice's final section, which
turned out to print `heta_inf`, `heta_0`, `heta_t` in the methodology note at
lines 524–525: four `\theta` where a Python source literal had interpreted
`\t` as a TAB. A fifth site, `\b` as BACKSPACE, had eaten a `beta` in
`CT-S21-DEPOSIT-PREP/outputs/item2_quotes.md` — in the Borel-normalisation
quote, which is the lead carried forward to the `S_{ζ*}` work. All five
repaired (`S21-35`); both scanners now return zero.

**This is in the object that was about to be deposited.** The R25 scanner,
written one section earlier *for this exact defect class*, did not catch it:
it tested `\r`, `\a`, `\v`, `\f` and omitted `\t` and `\b` — precisely the two
escapes that consume the commonest macros in a Painlevé document (`\theta`,
`\tau`, `\times`, `\beta`).

**And the first fix under-reported 4 as 2** (`S21-36`). A guard added to stop
TAB indentation being flagged suppressed every hit at the start of a line, and
the mangled thetas sit at the start of two wrapped prose lines. That is the
S17-22 shape once more — a test that could not fire — this time *inside the
detector written in response to S17-22*, one round after the eighth amendment
was proposed for the same family. The guard now flags decisive tails regardless
of position.

The honest reading: the escape-mangling family has now produced three findings
in two rounds (§R25, §R26), each one caught by widening a detector that the
previous round had just written. The detectors are converging, but the sequence
is a reminder that a scanner's *coverage list* is itself an unchecked
assumption — the same defect as a hardcoded count word, one level up.

### Deposit walkthrough prepared

`CT-S21-DEPOSIT-PREP/DEPOSIT-WALKTHROUGH.md` (`S21-37`) collects what the
deposit needs into one runbook: pre-flight commands including the control that
must fire, the two deposit-day confirmations, the four-row citation pass with
p. 2637 added, the `refs/` non-upload rule stated per file with its licence
basis, Zenodo new-version mechanics against concept DOI `10.5281/zenodo.20455089`
and v1.2 version DOI `10.5281/zenodo.20481592`, the DataCite and
`metadata.rights` fallbacks, five abort conditions, and the post-publish record
steps.

Part B sets out the Wong–Li decision. The material point is that it has got
cheaper: with Ibrahim–Salvy now quoted in its weaker printed form and `S21-32`
supplying a structural reason the growth law is absent from Wong–Zhao §3, there
is a contribution statement resting on a page already held — `r_∞` is the
constant the classical method sets aside to reach turning-point behaviour, made
explicit. That survives either outcome. The recommendation is still to buy,
weakly held, on the one ground that the paper is the last unread source that
could bear on whether the connection constant is given in closed form.

**Nothing executed.** No deposit, no purchase, no commit, no upload.

---

## R27 — the deposit-day pass, and a packet that was labelled by index

Part A of the walkthrough, run. Nothing published, uploaded, committed or sent.

**The pass is clean.** All four citation rows re-fetched: van der Put-Saito and
Jimbo byte-identical to the held copies and to the manifest; Zenodo 20481592
still version 1.2, conceptdoi 10.5281/zenodo.20455089 read from the API and
still distinct from the version DOI; DLMF section 32.2 at Version 1.2.8,
2026-09-15, unchanged from what the notice cites. All four load-bearing pages
re-read from images and all four match. A0 passes with all three of
`control_item4.py`'s controls firing. Claims `S21-38`..`S21-44`.

Two things worth keeping.

**My renderer was off by one, and the automated check could not tell me.** It
used printed = index + 2611 for van der Put-Saito, and index 16 for Jimbo; the
true offsets are +2610 and index 15. So the file written as `p2635` showed
printed 2634. The scripted check for "is the expected page number present in the
text layer?" returned **false for all four pages** — the running heads did not
survive extraction — and a uniform false across every case reads as a property
of the tool rather than a finding about any page. That is the seventh
amendment's shape again: a check that returns the same answer whatever the truth
is has not been run. What caught it was reading the images.

**The stored cold packet has the same defect, and it is older.**
`coldpackets/jimbo_p1152.png` is byte-identical to a render of PDF index 16 and
shows printed **1153**. CT-S9 named its renders by index; the packet inherited
the name and the name became the claim. The van der Put-Saito packet images were
checked against this and are correctly labelled, so this is the Jimbo file only.

The consequence is not a wrong claim but a wrong explanation. Every Jimbo quote
in the notice matches the true printed 1152, verified this round: (3.1) prints
the constant matrix as `diag(1,0)`, (A1)_PV reads `theta_0, theta_t not in Z`,
and the dictionary's `gamma = 1 - theta_0 - theta_t` gives C2 its `gamma = 1`
directly. But the notice's methodology note attributes CT-S15's two rejected
transcriptions to OCR, and they follow substantially from the packet instead:
printed 1153 carries **(A3)_PV**, which *does* constrain `theta_inf`, and does
not carry (3.1) at all. CT-S15 read the assumption line on the page it was
handed and labelled it by the filename it was given.

Left unedited. Re-characterising a cold read inside the deposit object is a
substantive wording change and the operator's call; a replacement paragraph is
proposed in `CT-S21-DEPOSIT-PREP/DEPOSIT-DAY-PASS.md`.

Two smaller notes. Rows 1 and 2 were first recorded NOT RE-FETCHED on the
assumption that a paywall left no route — but the manifest records working URLs,
and *paywalled to redistribute* is not *unreachable to fetch*; corrected in the
same round. And P0 gains the two detector-hygiene lines: a detector's coverage
list is itself an unchecked assumption, and a guard added to suppress false
positives can suppress exactly the hits that matter.

---

## R28 — the OCR attribution withdrawn, and the checklist made true

Operator ruled: adopt the replacement paragraph. Two edits to the deposit object,
both spliced byte-wise from composed files.

**The CT-S15 paragraph.** The notice attributed that reader's two rejected
transcriptions to OCR. Withdrawn. The image it was handed as Jimbo p. 1152 is
printed p. 1153, which carries (A3)_PV — constraining `theta_inf` — and does not
carry (3.1) at all. Both transcriptions were faithful readings of the page it was
given. The paragraph now says the packet was wrong, that the reader was not, and
that every Jimbo passage relied on was re-read from the true printed 1152 on
deposit day.

The operator's reason for the ruling is worth recording, because it is not the
accuracy argument: the notice's methodological credibility rests on the claim
that its checks catch defects, and blaming OCR for a defect that was ours inverts
that. It was the one place in the notice where the record flattered itself.

**The checklist section.** It still read *NOT YET DONE, and deliberately so*, and
closed with "Only the deposit-day citation pass above remains." Both were true
when written and false at the moment of deposit — a stale status line that would
have shipped inside the object asserting the very pass this round completed. Now
dated, with the four results and the hashes, and carrying one sentence on the
packet defect the pass found in our own materials.

That second edit was not in the ruling. It followed from it: once the pass is
run, a notice that says it has not been is wrong about itself.

**P0** gains the third line — identify a rendered page by the number printed on
it, never by the arithmetic that produced it. Where the running head does not
survive extraction, the check is an eye read, not a script.

Gates re-run against the new bytes: `item4_consistency` clean, C4 count word 7
vs 7, F7 0 asserting / 1 negated, both hedges present; all three controls fire;
the notice restores to sha256 `d070fab1…`; macro scan 0.

Still not done, and not mine: the author-reply check, and the upload itself.

---

## R29 — A1.1 confirmed, and a note-to-self caught on the way out

Operator checked the inbox: **no reply** from van der Put or Saito. A1.1 clears,
and C3's letter-status sentence stands exactly as written — *"the authors were
notified of this by email; no reply had been received when this notice was
finalised, and nothing here is author-confirmed."* `item4_consistency`
independently confirms the hedge survives (`hedges present: letter=True`), which
is the gate that would have fired had the sentence been softened or dropped.

Reading that sentence to verify it caught something else. It carried a trailing
**`*[Deposit-day: confirm that sentence still holds.]*`** — an instruction to
ourselves, written into the deposit object, which had served its purpose the
moment the inbox was checked and would otherwise have been published. Removed.
A scan for the other editorial markers (`[TODO`, `[FIXME`, `XXX`) found none.

Same class as the stale checklist header in §R28, and the third instance this
round: **text that was true and useful when written, and wrong at the moment of
deposit.** A draft accumulates instructions addressed to its own author, and
nothing in the gates looks for them, because they are not claims — they are
scaffolding. The pass caught all three only because the walkthrough required
re-reading the object end to end on the day rather than trusting that the last
round left it finished.

Notice now at sha256 `a9a938f7…`. Gates re-run: consistency clean, all three
controls fire, no control characters, no editorial markers. On this record the
notice is cleared for upload; the upload itself is the operator's.

---

## R30 — the form sheet, and the word DRAFT still in the title

Operator asked for a walkthrough of the Zenodo form. Wrote
`CT-S21-DEPOSIT-PREP/DEPOSIT-FORM.md`, field by field, every *keep* value read
from the live v1.2 record this round rather than from memory, and then diffed
the sheet back against that record: affiliation, ORCID, name, licence, all nine
keywords, the companion title and the existing related-identifier row all verify
verbatim.

Writing it surfaced the last blocker. **The notice's H1 still reads
`# DRAFT — V_quad companion paper v1.3 correction notice`, and the
`**STATUS: DRAFT FOR THE OPERATOR. Nothing has been deposited...**` block is
still under it.** Both would have published. The status block is worse than
merely stale: deposited, it would assert that nothing has been deposited.

Same class as §R28's checklist header and §R29's `*[Deposit-day: …]*` marker,
and the fifth instance in two rounds — scaffolding addressed to the author,
inside the object, true when written and false at deposit. It survived three
end-to-end passes over the same file because it is at the very top, where a
reader checking mathematics does not look, and because the filename itself
begins `DRAFT-`, which makes the word unremarkable in context.

Not applied. The H1 depends on a title choice that is the operator's, and every
wording change in this object has been ruled on first. `scripts/apply_title.py`
takes `A` or `B`, refuses without one, strips the status block, asserts no
`DRAFT` survives, reads back its own bytes and prints the new sha256. Verified
inert: run with no argument it exits 1 and the notice still hashes
`a9a938f7…`.

Two further findings recorded in the sheet rather than here, because they are
decisions rather than defects. **A rendered PDF has its own hash**, so
`a9a938f7…` stops being the number to verify the moment the format changes —
the stale-hash defect one file-format wide. And because A3 makes this a *new
version* while A2 deposits *the notice only*, the concept DOI will resolve to a
record whose sole file is a correction notice rather than the paper; defensible,
irreversible, and worth choosing deliberately rather than by default.

---

## R31 — the paper stays in the record

Operator reconsidered the deposit shape and overruled A2's *notice only*. A new
version whose sole file is an erratum makes the concept DOI
`10.5281/zenodo.20455089` resolve to a record where the paper itself is absent,
so a reader following a citation to the companion lands on a correction with
nothing to correct. The record keeps both.

Checking how to do that produced a better answer than re-uploading. On Zenodo
**New version** the previous files are **carried over by default**, so keeping
the paper is the default and the notice-only shape would have required actively
**deleting** `vquad_resurgence.pdf` from the draft. A2 now says: do not delete
it, add the notice beside it. Belt and braces, the held copy
`refs/vquad_resurgence_v1.2_zenodo-20481592.pdf` was checked against the live
record and is byte-identical — 612 719 bytes, md5 `4d1e4d59…`, matching the
record's own checksum field — so a hand re-upload could not alter the paper.

The ruling had two consequences the form sheet had not accounted for.

**The record title should probably now stay unchanged.** Options A and B were
written for a notice-only record, where the title had to announce the erratum or
the record would misdescribe itself. With the paper retained, the companion's
title still describes the record accurately, and leaving it byte-identical to
v1.2 means citations resolve to a record titled as cited. Added as **Option C**
and recommended; A remains defensible if the erratum should be visible in search.

This also exposed a conflation in the sheet's own pre-publish table, which
required the form title to match the notice's H1. The **record** title and the
**document** H1 are different objects. The notice's H1 reads as a correction
notice whichever record title is chosen. Row corrected.

**The notice's filename begins `DRAFT-`, and Zenodo publishes the filename you
upload.** Sixth instance of author-addressed scaffolding inside the deposited
object, and the first that is not text at all — no scan over file *contents*
could have found it, because the defect is in the name. A copy renamed
`vquad_resurgence_v1.3_correction_notice.md` is staged under `upload/` and
verified byte-identical to the notice, `c936662f…`.

---

## R32 — the related-identifier row that should not be added

Operator's instruction for the form said to add `10.5281/zenodo.20481592` as
*is supplemented by*; this sheet said *is supplement to*. Checking the direction
showed the row should not be added at all, and that the disagreement about which
way it points was the symptom rather than the problem.

Read back from the live v1.2 record:

- `related_identifiers` holds exactly one row, `10.5281/zenodo.20173773` /
  *references*. It contains **no** row for v1.1 (`20480603`), v1.0
  (`20455090`) or the concept DOI. The existing versions do not hand-link each
  other.
- Version linkage is maintained by Zenodo elsewhere:
  `metadata.relations.version = [{"index": 2, "is_last": true, "parent":
  {"pid_value": "20455089"}}]`.

So with the paper retained (§R31), v1.3 is a **version** of the work, not a
supplement to its own predecessor. Adding either direction would mislabel the
lineage in exchange for something Zenodo already records. DataCite has no
`corrects` relation, so there is no honest row to add even if one were wanted;
the correction is carried by the version string, the description and the notice
file.

This supersedes my own earlier advice in `DEPOSIT-FORM.md`, which was written
for the notice-only shape and not revisited when §R31 changed that shape —
guidance that was correct under an assumption and not re-derived when the
assumption moved. Two dependent spots were stale with it: the sheet's
pre-publish diff row ("the two DOIs in A3") and A3's own paragraph in the
walkthrough. Both corrected.

That makes three documents in two rounds carrying a consequence of a superseded
decision — the same shape as the stale hash and the stale status header, but at
the level of *reasoning* rather than a value: when a decision is overruled, what
was derived from it does not update itself.

## R33 - The upload walkthrough, and a checker that can fail

The operator asked for a screen-by-screen upload guide. Three documents now
describe one deposit, which is one more than is comfortable, so
`UPLOAD-SCREENS.md` quotes **no field value at all**: values stay in
`DEPOSIT-FORM.md`, mechanics in walkthrough A3, abort conditions in A4,
recording in A5. This is the same decision as declining a second recording slot
for the version DOI. Every duplicate this round has drifted - the hash, the
status line, the title - and a fourth copy of the title would have been a
fourth chance to drift (S21-63).

Two scripts were added because the guide referred to them, and referring to a
script that does not exist is inventing a path.

`verify_upload_file.py` prints the **md5** as well as the sha256, because md5
is what Zenodo displays beside an uploaded file. A sha256 the operator cannot
compare in the dialog is not a verification, it is a reassurance (S21-60).

`postpublish_readback.py` is the more interesting one. A checker written after
the event can always be made to agree with the event, so its expected values
were fixed before publication and it was control-tested against the **v1.1**
record, where it returned 5 of 10 and failed exactly the five checks that
depend on v1.3 having happened. It discriminates. That is the property the
uniformly-failing test of S17-22 lacked in the other direction, and it is
cheapest to establish before the thing being checked exists (S21-61).

The control also paid for itself substantively. v1.1 carries **the same single
`references` row** as v1.2, so that row is inherited and the work has never
hand-linked a predecessor version. The add-nothing ruling of R32 now rests on
two versions rather than one. v1.1's PDF md5 differs from v1.2's, so the
carry-over is a real file that changed, not a fixed artefact (S21-62).

Abort condition 3 was re-checked live today and is clear: record 20481592 is
still version 1.2, parent 20455089, PDF md5 unchanged.

### R33.1 - The backtick is PowerShell's escape character (S21-64)

Writing this very section produced the defect it describes. The block was first
written through `python -c "..."` inside a **double-quoted PowerShell string**,
where the backtick is the escape character. The markdown code span for
`verify_upload_file.py` therefore entered the file as a vertical tab, 0x0b,
followed by `erify_upload_file.py`. The backtick before `references` survived,
because the letter after it is not one PowerShell recognises.

This is the eighth amendment's class - a tool retyping what it should derive -
at one more level down, and it has a property the earlier instances did not:
**it is selective**. Only backticks followed by a, b, e, f, n, r, t, v or 0 are
consumed, so a document can pass an eye-read and a line count while carrying
one mangled identifier, and the surviving backticks are evidence that nothing
is wrong. In a document full of code spans, that is most of them.

It was caught only because `append_block.py` refuses control characters before
writing, and because the block was routed through that appender rather than
written directly. The first two attempts to run the appender did **not** catch
it: importing the older appender to reuse one function executed that module's
body instead of only its helper, and both the control and the real run then
failed identically with a NameError. A control that fails for the same reason
as the run it is controlling is the S17-22 shape again, and it was visible only
because the two were run side by side and their outputs compared. Fixed by
extracting the helper with `ast` rather than importing it, and by making the
control two-sided: one block that must be refused, one that must be accepted.

Consequence, added to P0: **never pass markdown through a double-quoted
PowerShell string.** Write the text in a file. The rule is not "escape the
backticks" - that is the coverage-list mistake again.

### R33.2 - The damage is older than today, and it is in the record (S21-65)

Having identified the backtick as the cause, the session tree was scanned for
the residue rather than for the cause: any control character in a markdown,
json or text file, with raw PDF extractions excluded by path.

213 files scanned, 10 carrying control characters. Nine are raw pdftotext or
OCR output under `CT-S8-LITCHECK/refs/`, `CT-S15-COLDREAD-DEFERRED/`,
`CT-S16-MEMBERSHIP-C/outputs/` and `CT-S21-DEPOSIT-PREP/outputs/`, where
control bytes are the normal residue of extracting mathematics from a PDF and
carry no meaning. Those are expected and were already the known exception.

The tenth is not. `CT-S1-THEOREM/REPORT.md` carries two TAB bytes, and reading
them in context shows the same defect, from the R1 round:

    > **AMENDED IN AUDIT ROUND R1** (see \../CT-R1-AUDIT/AUDIT.md\).
    > (1) Theorem \<TAB>hm:radius\ Step 3 contained ...

Two markdown code spans have been destroyed. Every backtick became a backslash,
and where the backtick preceded a `t` the pair collapsed to a TAB, so
`` `thm:radius` `` reads as a backslash, a tab, and `hm:radius`. The label is
unrecoverable from the text alone; it is legible only because the surrounding
sentence still names Theorem and Step 3.

So this class is not a defect of today's round. It has been latent in the
record since R1, it survived every gate built since, and it was found only
after an unrelated write was routed through an appender that refuses control
characters. The five invariants do not look at bytes. That is the same finding
as "gates that check claims do not check bytes", one level further down: the
byte check that exists was pointed at the deposit object, and the record around
it was never in scope.

**Not repaired.** `CT-S1-THEOREM/` is an earlier session folder and P0 forbids
modifying it. The damage is recorded here and the file left as it is. Anyone
reading that report should know the two mangled spans are `` `../CT-R1-AUDIT/AUDIT.md` ``
and `` `thm:radius` ``, on the evidence of the surrounding sentence rather than
of the bytes.

**The deposit object is clean.** `DRAFT-COMPANION-v1.3-NOTICE.md` and the
staged `upload/` copy both remain 35918 bytes at
`c936662f61be8625d69b7f8efce8a8684b33569c6a033e88f510a3050b89948c`, carry no
control characters, and were not touched by any of this. Nothing here changes
the deposit (S21-66).

### R33.3 - A count that changed meaning, and a damaged file with a future (S21-67, S21-68)

Two closing items, both raised by the operator at the boundary.

**The claim count.** This round reported "66 claims" where every previous round
reported the corpus figure, which stood at 406. The operator flagged the drop
and was right to: a checker reporting a smaller number as OK is exactly this
round's defect class. It was not that. 66 is the size of
`CT-S21-DEPOSIT-PREP/claims.jsonl` alone; the corpus is **413 claims in 22
files**, which is 406 plus the seven appended since, with no duplicate id.
`check_invariants.py` prints its own scope on the first line and was never
narrowed. The defect was in the prose: a number was reused with a different
referent and without saying so. That is the same drift class as the stale hash,
one level up from the bytes, and it is worth recording precisely because the
gate was sound and the sentence was not (S21-67).

**`CT-S1-THEOREM/REPORT.md` has a future, not only a past.** R33.2 recorded the
R1-era backtick damage and left the file alone, correctly, since P0 forbids
modifying an earlier session folder. But that file reports on the theorem that
part (i) is headed for. Two destroyed code spans surviving every gate built
since means the gates were never scanning it, and the remedy at publication is
not to repair the file in place but to **regenerate the report** from its
sources and cite the regenerated one. Citing a known-damaged file because it is
the historical artefact would carry the damage forward into a deposit. Recorded
here so that whoever scopes part (i) meets this before choosing a source
(S21-68).

## R34. The companion v1.3 deposit, published

Published 2026-09-18 as a **new version** of record `20481592`, not a new
upload: version DOI `10.5281/zenodo.22831933`, record `22831933`, concept DOI
`10.5281/zenodo.20455089` unchanged. Version `1.3`. Licence `cc-by-4.0`.
Title byte-identical to v1.2. Creators: Papanokechi (Independent Researcher). 11 keywords: the nine
carried over in their stored order plus `correction notice` and
`isomonodromic deformation`. Exactly one related identifier, unchanged from
v1.2: `10.5281/zenodo.20173773`, relation `references`. No
row was added for the v1.2 record, because Zenodo carries version lineage in
`metadata.relations.version`, outside `related_identifiers`, and DataCite has
no `corrects` relation.

Two files. The correction notice, and the v1.2 paper retained unchanged --- the
ruling of R31, taken because a concept DOI that resolves to an erratum with no
paper strands every reader following a citation. `default_preview` is
`vquad_resurgence.pdf`, so the landing page shows the manuscript and the erratum is read
as the description. Both files were verified after publication against the
bytes on disk, and the paper additionally against the v1.2 record's own stored
file entry, so the manuscript in the new version is byte-identical to the one
already cited.

**The last defect caught was in a filename, again.** The paper was first
uploaded from `CT-R1-AUDIT/refs/`, where it is stored under the descriptive
name `vquad_resurgence_v1.2_zenodo-20481592.pdf`. That name embeds record
`20481592` in a file published on record `22831933`, and Zenodo publishes the
filename it is given and freezes the file set at publish. No content scan could
reach it: the bytes were correct and the label was on the outside. This is the
third instance of the class this round, after the `DRAFT-` prefix and the Jimbo
packet mislabel, and it is the reason the staged copy carries the v1.2 record's
own published file key rather than a name chosen for the shelf it sat on
(S21-71, S21-72).

The whole round's defect class, stated once: **true when written, wrong at
deposit.** A stale checklist header, a self-addressed instruction, a stale hash,
a `DRAFT` H1, a `DRAFT-` filename, a stale upload-target line, a count reused
with a changed referent, a mis-named file, and an abstract whose refuted claims
sit four paragraphs below the correction that overturns them. Every one is a
duplicate drifting from the thing it describes. The countermeasure that held was
not a better checker but a rule about authorship: `FORM-VALUES.md` derives its
values from the record JSON instead of retyping them, and `UPLOAD-SCREENS.md`
quotes no field value at all.


## R35. The Wong-Li line, written rather than bought

The decision framed in `CT-S21-DEPOSIT-PREP/DEPOSIT-WALKTHROUGH.md` Part B was
between buying the article and writing the NOT OBTAINED line. The line is
written. What follows is why that is not a concession.

The recommendation in B4 was, weakly, to buy, and it rested on B2's second
question: whether the connection constant is given there in closed form. That
question is not answered by this decision and is not claimed to be. What changed
is which claim depends on it. The exponent

    s = beta_(d-1)/beta_d + (d-1)/2

is derived and numerically verified in this corpus independently of any source,
so if Wong-Li states it, the exponent was never the contribution. And the
contribution actually made - that `r_infinity` is the constant classical method
sets aside in order to reach turning-point behaviour, made explicit - rests on
`Wong-Zhao section 3`, a page that is held, CC-BY, and hashed in the manifest
(`S21-32`): the substitution x_n = y_n/K_n with K_(n+1)/K_(n-1) = c_n absorbs
the product growth by construction, leaving K_0, K_1 "depending on the
particular sequence". Ibrahim-Salvy is quoted in its printed form as a statement
about the state of the art, not about the world.

So the unread source could still bear on the closed form of `K`. It cannot
reach `s`, and it cannot reach the framing. That asymmetry is the whole of the
argument, and it is why the honest line costs the record nothing.

**What must not happen is the quiet version.** An unstated gap reads as a
novelty claim, which is why the status is written into `REFS-MANIFEST.md` as a
table row per question rather than as a sentence in a report someone may not
reach. If the article is obtained later, this section is superseded, not
deleted: the two questions are already stated in the form an answer would take.
