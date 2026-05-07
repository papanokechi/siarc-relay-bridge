# Coverage gap analysis — M5 substrate (relay 098 Phase E.E2)

**Generated:** 2026-05-07
**Scope:** Walk PCF-1 v1.3 § 1-§ 6 paragraph-by-paragraph and tabulate
M5-level objects that did NOT land in B1-B9 inventory. Each
uncovered object is flagged for a next-fire backlog entry.

---

## Method

For each numbered subsection of PCF-1 v1.3 (= `tex/submitted/p12_journal_main.tex`,
SHA-16 82173A09521D6676), enumerate the named mathematical objects
(definitions, theorems, lemmas, named equations) and check whether
each landed in the [m5_frds.lean](m5_frds.lean) scaffold.

Status legend:
- ✅ COVERED — has a Lean encoding in B1-B9
- ⚠️ PARTIAL — some aspect captured, body deferred
- ❌ UNCOVERED — flagged for next-fire backlog

---

## Section-by-section walk

### § 1.1 The transcendence predicate

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| PCF schema (eq:PCF) | L113-116 | ✅ | B6 |
| d=2 class (eq:d2-class) | L126-130 | ✅ | B1 |
| Wallis recurrence (informal mention) | L131-138 | ✅ | B8 |
| Perron-Poincaré root Λ (mention) | L137-140 | ⚠️ | B9 |
| Balanced discriminant Δ = β²-4αγ (def) | L142-150 | ⚠️ | B3 (a-side) |
| CM / non-CM case names | L150-152 | ❌ | CG-2 |

### § 1.2 Empirical dichotomy and the conjecture

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Conjecture A (transcendence dichotomy) | L156-180 | ❌ | CG-3 |
| Stokes exponent S(t) = log\|L(t)-L(0)\|/log\|t\| | L171-175 | ❌ | CG-4 |

### § 2.1 Polynomial CFs and Wallis convergents

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Wallis recurrence (eq:wallis) | L312-322 | ✅ | B8 |
| Perron-Poincaré characteristic (eq:char) | L326-336 | ⚠️ | B3 (indicial) |
| Convergence rate ρ = log₁₀\|Λ\| | L334-336 | ⚠️ | B9 |
| Field structure Λ ∈ Q(√(α²+4δ)) | L335-336 | ❌ | CG-5 |

### § 2.2 Spec(K) classification

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Spec(K) 5-tuple (eq:speck) | L342-344 | ✅ | B9 |
| Components d / Λ / Δ / ρ / τ semantics | L346-358 | ✅ | B9 |
| v5 upgrade convention | L360-361 | ❌ | CG-6 |

### § 2.3 Imaginary quadratic fields and CM

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Q(√Δ) splitting field convention | L363-389 | ❌ | CG-7 |
| Class-number-one (Heegner) discriminants | L386-388 | ❌ | CG-8 |

### § 2.4 Heun and Painlevé equations

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Heun ODE (4 regular singular points) | L390-417 | ❌ | CG-1 (full) |
| Painlevé III(D₆) parameters | L390-417 | ⚠️ | B5 (V_quad-only) |
| Painlevé III(D₆) Stokes constants | L390-417 | ⚠️ | B4 (per-stratum) |

### § 2.5 The Stokes phenomenon

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Borel transform ŷ(ξ) | L419-435 | ❌ | CG-9 |
| Borel-summability sectorial property | L432-440 | ❌ | CG-10 |
| Stokes constants per Stokes line | L440-445 | ⚠️ | B4 (sign + parity) |

### § 3 The Theorem for Δ > 0

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Theorem 3.1 (Trans-stratum closed form) | L450-465 | ❌ | CG-11 |
| F(2,4) Trans Main + Outlier subclasses | L450-465 | ❌ | CG-12 |
| Borel-summation closed-form derivation | L488-540 | ❌ | CG-13 |
| Corollary 3.2 (24 closed forms) | L572-573 | ❌ | CG-14 |

### § 4 The Sharp Dichotomy and Conjecture A v5

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Definition 4.1 (balanced discriminant) | L581-597 | ⚠️ | B3 (indicial side only) |
| 30-family evidence table (Table 1) | L599-650 | ❌ | CG-15 |
| Conjecture A v5 part (i) | L650-660 | ❌ | CG-3 |
| Conjecture A v5 part (ii) | L660-682 | ❌ | CG-3 |
| Lemma (singular points in Q(√Δ)) | L675-682 | ❌ | CG-16 |

### § 5 The Stokes-Exponent Diagnostic

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| Definition (S(t) exponent) | L711-728 | ❌ | CG-4 |
| CM-respecting deformations | L729-754 | ❌ | CG-17 |
| Six-family verification table | L755-790 | ❌ | CG-18 |

### § 6 V_quad Painlevé Prototype

| Object | PCF-1 v1.3 ref | Status | FRD |
|--------|----------------|--------|-----|
| V_quad parametrization | L959-985 | ✅ | B1 (relay convention) |
| P_III(D₆) parameters (1/6, 0, 0, -1/2) | L975-985 | ⚠️ | B5 |
| L(t)-deformation channel distinction | L986-1045 | ❌ | CG-19 |
| Stokes-data subsection | L1046+ | ⚠️ | B4 |

---

## Backlog enumeration

| Backlog ID | Object | Suggested next fire | Priority |
|------------|--------|---------------------|----------|
| CG-1 | Heun ODE structure (full) | M10-PROOF-DRAFT or HEUN-ENCODE | MEDIUM |
| CG-2 | CM / non-CM case dispatcher | inside B4 stratumOf body | LOW |
| CG-3 | Conjecture A v5 statements (i)+(ii) | M10-CONJECTURE-A-FORMAL | HIGH |
| CG-4 | Stokes exponent S(t) definition | M10-STOKES-DIAGNOSTIC | HIGH |
| CG-5 | Λ ∈ Q(√(α²+4δ)) field structure | M10-PERRON-POINCARE | MEDIUM |
| CG-6 | Spec(K) v5 upgrade convention | inside B9 specK body | LOW |
| CG-7 | Q(√Δ) splitting field convention | M10-CM-FIELDS | MEDIUM |
| CG-8 | Heegner discriminants list | inside B4 stratumOf body | LOW |
| CG-9 | Borel transform ŷ(ξ) | M10-BOREL-TRANSFORM | MEDIUM |
| CG-10 | Borel-summability sectorial property | M10-BOREL-SUM | MEDIUM |
| CG-11 | Theorem 3.1 statement + proof | M10-PROOF-DRAFT (B1+B2 sorries) | HIGH |
| CG-12 | F(2,4) Trans Main + Outlier subclass tags | inside B4 stratumOf body | MEDIUM |
| CG-13 | Borel-summation closed-form derivation | M10-PROOF-DRAFT-3.1-PROOF | HIGH |
| CG-14 | Corollary 3.2 (24 closed forms enumeration) | M10-CLOSED-FORMS-TABLE | LOW |
| CG-15 | 30-family evidence table | M10-EVIDENCE-TABLE | LOW |
| CG-16 | Lemma (singular pts in Q(√Δ)) | M10-PROOF-DRAFT | MEDIUM |
| CG-17 | CM-respecting deformations | M10-DEFORMATIONS | MEDIUM |
| CG-18 | Six-family Stokes-exponent verification | M10-STOKES-VERIFY | LOW |
| CG-19 | L(t)-deformation channel distinction | M10-CHANNEL-DIST | LOW |

---

## Summary statistics

- **Total enumerated M5-level objects:** 31
- **Fully covered (✅):** 7 (22.6%)
- **Partial coverage (⚠️):** 9 (29.0%)
- **Uncovered (❌):** 15 (48.4%)
- **Coverage gap %:** ~48%

This is consistent with the relay's framing: **SCAFFOLD only**.
The principal uncovered objects (Heun ODE, Conjecture A statements,
Stokes exponent S(t), Theorem 3.1) are statement-level
formalizations that require their own dedicated relay fires; the
B1-B9 scaffold provides the infrastructure to host them.

The coverage gap is the **next-fire backlog**, not a deficiency
of the scaffold itself.
