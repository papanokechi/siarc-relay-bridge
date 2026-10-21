# CT-S32-LD2-ORDINARY-LOCUS — REPORT

**Object.** `L_2 = z·b(θ+1) + z²·a(θ+2) − 1`, `θ = z d/dz`,
`b = β₂n² + β₁n + β₀` (`β₂ ≠ 0`), `a = α₂n² + α₁n + α₀`.

**Deliverables.**
`scripts/locus.py` → `outputs/locus.out.txt`, sha256
`f0a14395901cf1e6cf98f4334318290f5be3196bd11b906130a69871f0a727f2`, **19/19
controls PASS**. `scripts/emit_claims.py` → `claims.jsonl`, sha256
`b996b45ccfae509b87c919e5a81af79c6a68c39c2a1204ae3a671531682c4277`, 12 claims
`S32-01`…`S32-12`. `scripts/mutants.py` → **7/7 arms CAUGHT**.
Corpus check after this session: **551 claims in 30 files, INVARIANTS OK**.

**Review label.** Every claim carries `review: self` with
`review_note: "contaminated re-derivation; prior treatment of the same
operator was in context"`. The computation here was written and run in this
repository from the operator's definition and reproduces the finding
independently — but the earlier treatment was in context throughout, so no arm
of this session is a cold read and none should be counted as independent
confirmation of the earlier work.

## 1. The finding, adopted claim by claim

`S32-01` **PROVEN** — A singular point of `L_2` can *disappear*. The point at
infinity is an **ordinary** point exactly on the locus `a(1) = a(2) = 0` **and**
`b(1) = 0`. Exhibited at `b = n²+n−2`, `a = (n−1)(n−2)`: in `t = 1/z`, after
removing content, the operator is `(1+t)Y″ − 2Y′ − Y`, whose leading
coefficient at `t = 0` is `1 ≠ 0`. Then `S = {0, z*}`, of size 2 not 3.

`S32-02` **PROVEN** — The resulting Katz multiset is `(1/2, −, 0)` and matches
**no row** of Table 2.1. This is not a pathology: Table 2.1 lists the families
whose Riemann–Hilbert fibres have dimension one, not every rank-two connection
on `P¹`. Both Katz readings by two differently implemented methods — Newton
polygon of the Euler-operator coefficients, and pole order of the normal-form
potential `r = p²/4 + p′/2 − q` — agreeing at every point of every case (nine
`C-M` arms).

`S32-03` **PROVEN** — Both conditions are needed; the locus is codimension 3.
With `a(1)=a(2)=0` but `b(1) = 5 ≠ 0`, the exponents at ∞ are `{0,1}` yet the
`t⁰` equation is `b(1)·c₀ = 5c₀ = 0`, forcing `c₀ = 0`: a logarithm is forced,
∞ survives, and the row is `D̃6 / PVdeg = PIII(D6)`. The obstructing
coefficient *is* `b(1)`.

`S32-04` **PROVEN**, `supersedes: S28-10` — *"The row depends only on
`(α₂, α₁)`"* is **true generically and false on the locus**. S28-10 asserted
it without restriction and recorded it as *stricter than the
pre-registration*, which had allowed dependence on the vanishing of `a(2)`.
The generic statement stands. The unrestricted one does not: holding the
numerator **fixed** at `a = (n−1)(n−2)` — `(α₂,α₁,α₀) = (1,−3,2)` unchanged —
and moving `β₀` alone from `−2` to `−1`, i.e. `b(1)` from 0 to 1, moves the
answer from **no row** to `D̃6 / PVdeg`. So `b(1) = β₂+β₁+β₀` does enter,
through that locus alone.

`S32-05` **PROVEN**, `supersedes: S28-09` — The *"reached iff `deg a = 2`"*
direction of S28-09 fails: `deg a = 2` does not imply the row is reached. The
rest of S28-09 is unaffected — three rows reachable, seven excluded — because
the exclusions rest on `Katz(0) = 1/2` and `Katz(∞) ≤ 1`, neither of which the
locus disturbs (`z = 0` keeps Katz 1/2 there).

**CT-S28 was not edited.** The supersession is recorded only here, in the
`supersedes` field and in the claim text, which names the superseded id
explicitly (the emitter refuses to write a `supersedes` whose target is not
named in the prose — mutant arm M5).

## 2. The defect behind it

`S32-06` **VERIFIED** — The ordinary-point predicate tested only whether a
holomorphic solution with `c₀ = 1` exists. It did **not** require the exponents
to be `{0,1}` — a criterion written in the predicate's own docstring and in the
surrounding prose, and simply never coded. Exhibited exactly: at
`b = 3n²+n+1`, `a = (n−1)(n−2)` the point `z* = −3` has exponents `{0, 7/3}`; a
holomorphic solution with `c₀ = 1` does exist, so the defective predicate calls
`z*` ordinary and discards it — returning `S = {0, ∞}` and no row, *the right
verdict class for the wrong point and the wrong reason*. Control **C5** runs
the same case under both predicates and requires them to **disagree**; it would
have fired had they agreed, which would have shown the requirement decorative.

`S32-07` **STRUCTURAL** — Why `{0,1}` is the right criterion. For exponents
`{0,m}` with `m ≥ 2` the Wronskian behaves as `w^{m−1}` and vanishes, so two
holomorphic solutions are not a basis; for non-integer `m` the second solution
is not holomorphic at all. Existence of *one* holomorphic solution is
necessary, not sufficient — exactly the gap the defect fell into.

`S32-12` **VERIFIED** — A second, independent instance of the same *class* was
found in this session's own emitter. Arm **M6** of `scripts/mutants.py`
reported MISSED: the emitter refused a wrong `output_hash`, but only in its
post-write read-back, so the bad value had already reached disk — CT-S28 defect
6.3 again. Repaired by moving the artefact-hash assertion into the pre-write
validation block; all seven arms then CAUGHT, with `claims.jsonl`
byte-identical throughout and a clean re-run reproducing it byte-for-byte.
Every anchor string is asserted present before its arm runs, so no arm can pass
vacuously by failing to apply.

## 3. Controls

| arm | would have fired if |
|---|---|
| C1 generic `deg a = 2` → 3 points, row PVdeg | the generic case producing any other row, or fewer than three points |
| C2 on the locus: ∞ ordinary, `#S = 2`, no row | ∞ staying singular, or the two-point multiset matching some row |
| C3 **sharp**: `β₀` by 1, `b(1): 0→1`, restores ∞ and the row | the classifier being blind to `b(1)` — C2 would then be uninterpretable |
| C4 `a(1)=a(2)=0` alone does not drop ∞ | the locus being codimension 2 rather than 3 |
| C5 defective predicate changes the answer | the two predicates agreeing, showing the defect harmless |
| C6 `(α₂,α₁)` fixed, `β₀` alone moves the answer | the multiset unchanged by `β₀`, leaving S28-10 intact |
| C-M ×9 | any disagreement between the polygon and potential readings |
| M1–M7 emitter arms | the emitter accepting a fault, refusing for the wrong reason, or leaving a modified `claims.jsonl` |

The artefact is read back from disk, CRLF asserted absent, and a known-present
non-ASCII sentinel asserted **present** *and* asserted **destroyed by a latin-1
read** before any absence is evaluated.

## 4. Does `check_invariants.py` reach `C:\LocalWork\SCOPE\`?

**No** — and it reaches less of this repository than its docstring claims.

`sessions/2026-09-17/CT-R1-AUDIT/check_invariants.py` sets
`ROOT = pathlib.Path(__file__).resolve().parents[1]`, which is
`sessions/2026-09-17`, then `rglob`s `claims.jsonl` beneath it. Measured today:

* `C:\LocalWork\SCOPE` is outside this repository entirely and is **not**
  reached — confirming **S30-08**. The CT-S28, CT-S29 and CT-S31 claim material
  there is outside the corpus checker.
* The docstring says *"over the whole session corpus"*, but the repository
  holds **443** `claims.jsonl` files of which only **29** lie under
  `sessions/2026-09-17`. **414 are never examined.** The checker's own line
  `corpus: 551 claims in 30 files` is the honest measure of its coverage.
  (Separately, 46 lines elsewhere in the repository are unparseable as JSON —
  a UTF-8 BOM among them — which the checker never sees.)

### What it would take — and why nothing was done unilaterally (`S32-10`)

1. **Re-point `ROOT`** to the repository root. *Cost:* 414 previously
   unchecked files enter the invariant set at once, and any legacy violation
   becomes a hard failure of every future round. That must be a deliberate,
   staged decision, not a side effect.
2. **Give the checker an explicit roots list**, including `C:\LocalWork\SCOPE`,
   so out-of-tree session folders are checked *in place*. *Cost:* the corpus
   acquires a dependency on an absolute path outside version control, and "the
   corpus" stops meaning "what is in the repository".
3. **Move the SCOPE session folders into `sessions/`.** *Cost:* a
   provenance-bearing relocation of deposited-adjacent records — and one of
   those folders, `CT-S31-COLDREAD-ROWS`, is an input packet being assembled
   for a different, uncontaminated process, from which this session has been
   stood down.

Moving files to satisfy a checker is precisely the unilateral act that was
ruled out, so **nothing was moved and no path was rewritten**. The decision is
the operator's. This session was placed under `sessions/2026-09-17/` so that
its own twelve claims are reached by the existing checker **with no change to
it at all** — confirmed: 551 claims in 30 files, INVARIANTS OK.

## 5. Scope limit, binding (`S32-11`)

A matching Katz multiset is **necessary, not sufficient**. Nothing in
`S32-01`…`S32-05` asserts that any specialisation of `L_2` *is* a member of any
van der Put–Saito family; no membership, isomonodromy or surface-type claim is
made. Conversely — and this is the content of `S32-02` — failure to match is
not a pathology, because Table 2.1 is not a classification of all rank-two
connections.

## 6. What could not be established

* Whether the multiset `(1/2, −, 0)` corresponds to any classified object.
* Whether the logarithm is forced at `z*` and at ∞ for *all* coefficient values
  on the near-miss loci, or only for the exhibited representatives — each was
  settled at one explicit, exactly-computed point, not symbolically across the
  locus.
* Anything about `d ≥ 3`.
* Whether the 414 unchecked `claims.jsonl` files satisfy the invariants. They
  were counted, not validated; the 46 unparseable lines are a symptom, not a
  survey.

## 7. Stand-down note

`C:\LocalWork\SCOPE\CT-S31-COLDREAD-ROWS\` was **not** read, written, listed or
deleted during this session. `CT-S28-LD-ORDER/claims.jsonl` was read — to quote
`S28-09` and `S28-10` accurately for the supersession — and **not modified**.
