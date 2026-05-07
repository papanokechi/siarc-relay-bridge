# Phi assignment-level statement — V0 substrate

**Relay:** 096 T2-M9-V0-SUBSTRATE-PRE-STAGE
**Tier:** TIER-A.1 (assignment-level only; categorical-coherence
deferred to TIER-C / M13)
**Status:** DRAFT_SUBSTRATE (skeleton; not a publishable V0)
**Anchor:** picture v1.19 §3 P-MC row + §4 M9 milestone
(SHA-256 prefix `8BD9043370872F07`; 383 291 B; 4 026 lines;
SIARC-MASTER-V0 working title)

---

## 1. Working terminology pin

Per peer-AI synthesis 4-of-4 Q4 Reviewer A recommendation
(SHA-16 `DF92466E123E16BF`, L59), the V0 substrate uses the
word **correspondence** in the announcement-facing statement,
reserving **functor** for the M13 follow-up where categorical
laws (composition, identity, naturality) will be addressed.
The internal program-language token *"Phi"* (also written `Φ`)
is preserved. Operator may override to "functor" or "map of
moduli" at fire-time of the V0 announcement itself; the
substrate below is wording-agnostic.

A forbidden-verb translation note is recorded in the
audience-framing memo (Phase E) per Reviewer A blind-spot BS-2.

---

## 2. Source category — Source(Phi)

### 2.1 Objects (what Phi accepts)

The source-side objects are **PCF arithmetic-asymptotic
data triples** indexed by a PCF family $\mathcal{F}$:

$$
\mathrm{Obj}(\text{Source}) \ni \mathcal{F}
   \;=\; \{a_i(b)\}_{i \ge 0}
$$

with $a_i \in \mathbb{Z}[b]$, $\deg a_i \le d$, and the
generator $b \in \mathbb{N}$. Per picture v1.19 §3 P-MC row
(L420-440) the working representative for each family is its
**leading-coefficient triple** plus the formal Newton-polygon
slope determining $\xi_0$.

For the cubic case ($d = 3$) the canonical representative is
the 50-row catalogue documented in PCF-2 v1.3 §6.B (Zenodo
version DOI `10.5281/zenodo.19963298`) which the program has
labelled uniformly `PAINLEVE_UNCLASSIFIED` per T3 Conte-Musette
test verdict (Prompt 007). For the quadratic case ($d = 2$),
the canonical representative is `V_quad` per CT v1.3 §3.5
(Zenodo version DOI `10.5281/zenodo.19972394`).

### 2.2 Morphisms (informal description)

V0 describes morphisms in Source informally per Reviewer A
Q4 recommendation L59 ("morphism behavior described
informally"). The substrate-level picture:

* **Rescaling of $b$** ($b \mapsto k b$ for $k \in
  \mathbb{Q}^{\times}$).
* **Integer translates of $a_0$** ($a_0(b) \mapsto a_0(b) +
  m$ for $m \in \mathbb{Z}$).
* **The explicit "obvious equivalences"** listed in picture
  v1.19 §3 P-MC row L440 ("rescaling $b$, integer translates
  of $a_0$, etc.") which the working P-MC statement marks as
  the equivalence relation up to which $\Phi$ is asserted to
  classify.

V0 does **not** state that the listed morphisms generate the
full equivalence groupoid. That delineation is forwarded to
the M13 follow-up (TIER-C).

### 2.3 Substrate-gap flag

The picture v1.19 source-category description is
substrate-anchored at the **object level** (the P-MC row +
the catalogue-level cubic and quadratic representatives) but
is **not formally written out at the categorical level**. G7
(picture v1.19 §5 L1070, "Master functor $\Phi$ (P-MC) not
formally stated") is the standing program-level gap. V0
substrate inherits this gap and forwards it to the V0 fire
itself for closure.

---

## 3. Target category — Target(Phi)

### 3.1 Objects

Per picture v1.19 §3 P-MC row L426 (verbatim quote, 33
words):

> a functor $\Phi : \mathrm{PCF}(1, b) \longrightarrow
> (\Delta_d, \|\Delta\|_{\mathrm{Pet}}, \xi_0)$ mapping
> each PCF family to an arithmetic-asymptotic invariant
> triple

the published target is the **invariant triple**
$(\Delta_d,\, \|\Delta\|_{\mathrm{Pet}},\, \xi_0)$:

* **$\Delta_d$** — modular discriminant of the associated
  curve at degree $d$ (elliptic / hyperelliptic per $d$).
  Picture v1.19 §3 L425.
* **$\|\Delta\|_{\mathrm{Pet}}$** — Petersson $L^2$ norm in
  the appropriate weight space (working level: weight 12,
  $SL_2(\mathbb{Z})$, cubic case). Picture v1.19 §3 L426.
* **$\xi_0$** — Newton-polygon-derived Borel-singularity
  radius of the formal coefficient series; the conjectural
  formula $\xi_0(b) = d / \beta_d^{1/d}$ (where $\beta_d$ is
  the leading-monomial coefficient) was upgraded
  THEOREM-GRADE for all $d \ge 2$ in D2-NOTE v2.1 (Zenodo
  version DOI `10.5281/zenodo.20015923`; G1 row picture
  v1.19 §5 L1064). Picture v1.19 §3 L427-429.

V0 substrate carries the invariant triple **as the V0
target**.

### 3.2 Stokes-data extension (R5 / R8 / G15 / G22 leg)

The Reviewer D Q4 recommendation L294 (verbatim quote, 25
words):

> Add a "V0-pre-flight" task to the agent queue: a 10-digit
> numerical check of the Stokes multipliers against the
> connection formula

points at a **secondary target axis** beyond the published
invariant triple: the **Stokes-data target** carried by the
$V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$ normalization
map (G15 / G22; picture v1.19 §5 L1066, L1080).
$P_{\mathrm{III}}(D_6)$ Stokes data live in the
$(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$
4-tuple per CT v1.3 §3.5 + KNY 2017 §8.5.17 + V1 monodromy
maps. The Stokes-data axis is carried by the M9 announcement
as a **secondary classifier** (per picture v1.19 §8 Q10
L3963 surfacing of "Stokes-data fourth coordinate" question).

Substrate status of the Stokes-data target axis: **PARTIAL**
per 069 (CC-VQUAD-PIII-NORMALIZATION-MAP-PHASE-D-NUMERICAL
2026-05-07; verdict `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`;
$|\det J(\Phi_{\mathrm{symp}})|$ at V_quad parameter point
NOT_COMPUTABLE_R1_GATED). M9 V0 carries the Stokes-data axis
as a **conditional secondary classifier gated on M6.CC R1
closure**; explicit conditional flag is the recommended V0
announcement disposition.

### 3.3 Morphisms (informal description)

Target-side morphisms include the JMU 1-form (Jimbo-Miwa-Ueno
1981 Physica D series; canonical anchor C1 per
`citation_pre_verification_2026-05-07.md`), the Bertola/
Malgrange extension to extended monodromy data (V2
Its-Lisovyy-Prokhorov 2018 Duke MJ 167:7; arXiv:1604.03082),
and the Bäcklund and Schlesinger transformations on
Painlevé-III tau functions (V1 Barhoumi-Lisovyy-Miller-
Prokhorov 2024 SIGMA 20 019; arXiv:2307.11217). V0
references these informally; their categorical role is
forwarded to TIER-C / M13.

---

## 4. Phi assignment rule

### 4.1 On objects (V0 announcement scope)

Given a PCF family $\mathcal{F}$ as above, V0 announces the
assignment

$$
\Phi(\mathcal{F}) \;\longmapsto\;
   \bigl(\Delta_d(\mathcal{F}),\;
         \|\Delta(\mathcal{F})\|_{\mathrm{Pet}},\;
         \xi_0(\mathcal{F})\bigr).
$$

The component constructions are anchored as follows:

* **$\xi_0(\mathcal{F})$** — D2-NOTE v2.1 Theorem 4.1 (THEOREM-
  GRADE for all $d \ge 2$ uniformly; picture v1.19 G1 row).
* **$\Delta_d(\mathcal{F})$** — picture v1.19 §3 P-PET row
  L850-856 (T2 PASSED; $j = 0$ closure A=6-only branch via
  Q22 path-(a) at $|\delta_a| = 3.08904186542 \times
  10^{-23}$ via 014 / Q22 memo SHA-16 substrate).
* **$\|\Delta\|_{\mathrm{Pet}}$** — picture v1.19 §3 P-PET
  row continuation; derived from $\Delta_d$ via the standard
  Petersson inner product at the working weight.

The announcement-level disposition of each component:
**$\xi_0$ THEOREM-GRADE**, **$\Delta_d$ + $\|\Delta\|_\mathrm{Pet}$
$d=3$ $j=0$ branch CLOSED (A=6-only / PSLQ-detection
precision)**, **other $d$ and other CM-points OPEN**.

The V0 announcement-level statement is therefore the
**conditional version**: $\Phi$ is announced on the
sub-domain of the source category where the component
constructions are individually substantiated, with the
remaining sub-domain announced as "in-program-conjecture
(downstream of M2 + M4 + M6.CC closure)".

### 4.2 On morphisms (informally)

V0 announces that $\Phi$ **sends source morphisms to target
morphisms** at the level described informally in §2.2 + §3.3
above. Concretely, V0 lists:

* The two leading source-side equivalence operations from
  picture v1.19 §3 P-MC row L440 ("rescaling $b$, integer
  translates of $a_0$");
* That each lifts to a target-side automorphism of the
  invariant triple (the modular-discriminant axis is invariant
  under the listed source equivalences by construction of
  $\Delta_d$ from the curve attached to $\mathcal{F}$).

V0 does **not** announce a categorical-level statement
(composition, identity, or naturality of the assignment
rule). That is the M13 deliverable.

### 4.3 Three-tier framing pin

Per peer-AI synthesis Q4 4-of-4 row (peer_ai_reviews
file SHA16 `DF92466E123E16BF`, L341 summary table):

> Staged / two-tier announcement: physics-level V0
> (assignment-level Phi + numerical Stokes consistency) +
> full RH-correspondence as M13 follow-up; D adds 10-digit
> numerical RH check as V0-pre-flight

(verbatim quote, 35 words)

V0 substrate adopts the explicit **three-tier framing** of
relay 096 §TASK:

* **TIER-A** (this fire's scope): assignment-level Phi
  statement + numerical Stokes-multiplier consistency
  check (or PRE-FIRE-INPUT flag) + related-work survey +
  audience-framing + venue list.
* **TIER-B** (M9 V0 announcement; future fire post M4 +
  M6.CC): assembles TIER-A substrates into a preprint,
  cites TIER-C as future deliverable.
* **TIER-C** (M13 follow-up; downstream): full Riemann-
  Hilbert correspondence at Stokes-data level +
  categorical-coherence verification.

---

## 5. Skeleton statement — V0 announcement form (substrate)

The following is a **substrate-form** skeleton of the V0
announcement statement. It is **not a publishable V0**; it
is the assignment-level skeleton from which the V0
announcement-fire (post M4 + M6.CC closure) will draw.
Wording and forbidden-verb translations per Phase E.

> **V0 Announcement (substrate form, 2026-05-07).**
> Let $\mathrm{PCF}(1, b)$ denote the category of polynomial
> continued fractions of the form $\alpha(b) = a_0(b) +
> b/(a_1(b) + b/(a_2(b) + \cdots))$ with $a_i \in
> \mathbb{Z}[b]$, $\deg a_i \le d$, taken up to the obvious
> equivalences (rescaling $b$, integer translates of $a_0$).
> Let $\mathrm{Mod}_d^{\mathrm{Pet}, \xi_0}$ denote the
> arithmetic-asymptotic target carrying the invariant triple
> $(\Delta_d, \|\Delta\|_{\mathrm{Pet}}, \xi_0)$ as in
> picture v1.19 §3 P-MC. We announce a correspondence
>
> $$\Phi : \mathrm{PCF}(1, b) \longrightarrow
> \mathrm{Mod}_d^{\mathrm{Pet}, \xi_0}$$
>
> at the **assignment level on objects** (as described in §4.1
> above), with morphism behavior described informally
> (§4.2). The component sub-claims pinning $\Phi$ on its
> announced sub-domain:
>
> 1. (universality of $\xi_0$) For all $d \ge 2$, $\xi_0(\mathcal{F})
>    = d / \beta_d^{1/d}$ where $\beta_d$ is the leading
>    monomial coefficient. **Anchor:** D2-NOTE v2.1 Theorem
>    4.1 (Zenodo `10.5281/zenodo.20015923`).
> 2. (Petersson $j=0$ closure at $d=3$, A=6-only branch)
>    Linear residual $|\delta_a| = 3.08904186542 \times
>    10^{-23}$ at K_FIT=7 / dps=25000 / N=1200; PSLQ on H6
>    B19+ at maxcoeff $10^{50}$ / tol $10^{-40}$ returns no
>    $\Gamma(1/3)$ relation. **Anchor:** Q22 deposit-readiness
>    memo (relay 099, bridge `d388946`).
> 3. (Stokes-data axis, conditional secondary classifier)
>    The $V_{\mathrm{quad}} \to P_{\mathrm{III}}(D_6)$
>    normalization map carries Stokes-data target
>    $(\alpha_\infty, \alpha_0, \beta_\infty, \beta_0)$;
>    canonical-form residual gated on M6.CC R1 closure.
>    **Anchor:** 069 verdict
>    `UPGRADE_V1_0_PARTIAL_NUMERICAL_PERSIST`; relay 075
>    Phase E STRUCTURAL_MISMATCH on chart-map candidate B1.
>
> The **categorical coherence** of $\Phi$ (composition,
> identity, naturality) and the **full Riemann-Hilbert
> correspondence at Stokes-data level** are forwarded as the
> M13 follow-up deliverable.

(end skeleton)

---

## 6. Substrate-gap inventory

Items still required for V0 fire (post M4 + M6.CC closure):

* **GAP-V0-1** — Source-category equivalence groupoid
  delineation. (M9 fire scope; not blocking.)
* **GAP-V0-2** — Target-category Stokes-data axis residual
  (M6.CC R1 closure; relay 086 / 086a / 086c forward
  pointer; W21 LANE-1 jurisdiction).
* **GAP-V0-3** — Numerical Stokes-multiplier consistency
  check at 10 dps (Phase C below; PRE-FIRE-INPUT flag at
  this fire's time).
* **GAP-V0-4** — Forbidden-verb translation table for
  external-facing announcement (Phase E; A BS-2).
* **GAP-V0-5** — Picture v1.19 G7 closure (master functor
  $\Phi$ (P-MC) not formally stated; HIGH severity per
  picture v1.19 §5 G7 row L1070).

---

## 7. AEAL anchor block

* phi_assignment_statement.md SHA-256 (this file): computed
  at fire end in `claims.jsonl` 096-B-1.
* picture v1.19 anchor: SHA-16 prefix `8BD9043370872F07`;
  bridge path
  `sessions/2026-05-06/PICTURE-V19-CONSOLIDATED-DEPOSIT/
  picture_v1.19.md` at line 1019 (M9) and line 422 (P-MC).
* peer-AI synthesis anchor: SHA-16 prefix
  `DF92466E123E16BF`; bridge path
  `tex/submitted/control center/
  peer_ai_reviews_received_2026-05-07.md` at lines 53-59
  (Q4 A) + L294 (Q4 D) + L341 (summary table).
* citation pre-verification anchor: SHA-16 prefix to be
  recorded in claims.jsonl.

---

End phi_assignment_statement.md.
