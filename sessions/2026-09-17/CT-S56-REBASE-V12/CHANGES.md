# CHANGES — revision of MATH-D-26-00523, rebased onto v1.2

**Base.** v1.2, Zenodo record 21412469, `md5 792107efab6317e8ae21e2ca20f092ff` — the file
Editorial Manager holds. Established in CT-S55 by downloading the manuscript
item itself through the link embedded in EM's stamped build, not by filename.

**Status.** Draft. Nothing has been uploaded, submitted or deposited.

| | base v1.2 | revision |
|---|---|---|
| pages | 25 | 27 |
| PDF | `md5 792107efab6317e8ae21e2ca20f092ff` | `sha256 4ffcc94f8698f515172d4b8b8cc4b427` |
| source | `sha256 2529da49e377b9dd…` | `sha256 973145689699bdb79a2b67d314ea821e` |

**33 replacements**, each required to match the v1.2 source exactly once,
all validated against the buffer before anything was written:

- **Item 1** — 4 edits
- **Item 2** — 1 edit
- **Item 3** — 5 edits
- **Item 4** — 9 edits
- **Item 5** — 13 edits
- **Item R** — 1 edit

Of these, 19 are CT-S52's edits, **imported from its own module** rather than
retyped, 1 is a further item-4 correction found in this session (the
"obtained twice" sentence in Proposition 2.4, L455 of the v1.2 source),
and 13 are new for item 5.

---

## Why the base changed

CT-S52 prepared this revision against **v1.0**. CT-S55 established that LMP holds
**v1.2**. The revision was therefore rebuilt from v1.2's source.

The re-basing cost less than feared: the v1.0 → v1.2 source diff is **3 hunks,
+21/−3 lines**, and is entirely journal boilerplate — *Funding*, *Data
availability*, *Conflict of interest*, *Declaration on the use of AI tools*, and
the removal of the *References* heading. **No mathematical text differs between
v1.0 and v1.2.** That is why all 19 of CT-S52's replacements matched v1.2
exactly once, with none broken and none ambiguous.

---

## Item 1 — the D₅⁽¹⁾ identification stated as conjectural

  1. abstract: D5 stated as fact
  2. 1.1: identification + v1.3 notice on the Painleve parameters
  3. 7.1: the representative described as a D5 representative
  4. 4.x algebraicity: accessory parameter asserted as fact (found by the sweep, not on the reported list)

Each now attributes the surface identification to the companion's Conjecture 4.1
rather than asserting it. §1.1 additionally records that the companion's v1.3
correction notice revises the derivation of the quoted Painlevé parameters.

The fourth edit was **not on the reported list**. It was found by the
Amendment H sweep, which is why the sweep is run before editing and not after.

## Item 2 — the overclaimed completion in §7.1

  1. 7.1: 'completes part (ii)(a) for d=2'

"completes part (ii)(a) for d = 2" is replaced by: an instance of part (ii)(a)
for the representative V_quad, conditional on the conjectured surface
identification, and not established for the stratum.

## Item 3 — "proved twice" and the independence of the structural argument

  1. Theorem 1.2: 'proved twice'
  2. 1.4: 'an independent structural argument'
  3. 2.2 proof: the structural argument restated correctly
  4. Appendix A.2: 'Independent structural confirmation'
  5. A.5: 'case-elimination plus the structural argument'

Theorem 1.2 no longer says the result is proved twice. The structural
argument is restated correctly: a torus together with one root unipotent
generates a **Borel** subgroup, and it is Kovacic Case 1 exclusion of
reducibility that upgrades this to SL₂(ℂ). **Kovacic is the proof**; the
structural route is a consistency check resting on the same Case 1 exclusion,
so it is not independent corroboration.

## Item 4 — apparency at ξ = 0

  1. Prop 2.4: apparency at xi=0
  2. Table 1: '0 (apparent)'
  3. Cor 1.4 proof: 'the point 0 is apparent'
  4. Lemma 2.7 statement and proof
  5. figure: node label '(apparent)'
  6. figure caption: 'xi=0 is apparent and carries no cut'
  7. Remark 3.3: 'the apparent point'
  8. A.3: record the xi=0 log computation
  9. Prop 2.4 closing: 'Both statements are obtained twice' (operator ruling: same shape as item 3, inside item 4's scope)

CT-S52's exact computation over ℚ(√3) found that ξ = 0 **does** force a
logarithm, so "apparent" was wrong. Every occurrence is corrected, and the
main identity is stated to be unaffected: B̂ is holomorphic at 0 on the
principal sheet and the cycle does not approach it. In Table 1 the cell
`0 (apparent)` becomes `0 (reg. sing., logarithmic; B̂ holomorphic there)`.

Affected objects, **in v1.2's numbering**: Proposition 2.4,
Lemma 2.7, Table 1, Remark 3.4, Figure 1 and its
caption, and the proof of Corollary 1.4.

> ⚠️ CT-S52's internal tag for one of these reads "Remark 3.3". **v1.2 has no
> Remark 3.3**; the object is Remark 3.4. The tag is a v1.0 leftover.
> It is the tag that is stale, not the edit — the edit matched v1.2's text
> exactly once, by text and not by number.

## Item 5 — Methods B and C are not independent (new this session)

  1. abstract: 'three structurally independent methods'
  2. 1.3 main results: 'three independent ways'
  3. Theorem 1.1: 'three structurally independent methods'
  4. 5 preamble: 'three structurally independent ways' / 'disjoint inputs'
  5. 5.1 strategy: heading and the 'disjoint inputs' premise
  6. 5.1 Method A bullet: independence inferred, not measured
  7. 5.1 Method B bullet: name the amplitude dependence
  8. 5.3 methodB chain: name where S enters
  9. 5.3 methodB: the error figure and the independence sentence
  10. 5.5 prop:cross: 'disjoint inputs'
  11. Table 2: row B 'Independent of' and its figure
  12. Table 2 caption: record the shared amplitude
  13. 5.5 closing: 'spurious triple coincidence'

CT-S54 established that `eq:methodB-chain` opens by substituting
A = (S/2πi)·Γ(1+β), so Method B's printed derivation **consumes S**, and its
reported 8.84482×10⁻⁴⁶ is algebraically the same quantity as Method C's — the
e^(−ξ₀) cancels. Two numbers printed side by side in the results file since
June were one number printed twice.

The revision:

- removes "three structurally independent methods" from the abstract,
  §1.3 and Theorem 1.1;
- names, at the point where it happens, that S enters Method B through the
  amplitude;
- reports Method B's **independent** check as the reconstruction of S from the
  stream-extracted amplitude, **3.69×10⁻⁴⁶**, which uses no Stokes datum —
  this replaces 8.84×10⁻⁴⁶ in Table 2 row B;
- restates Table 2's caption and the cross-check proposition in §5.5 to
  record the shared amplitude;
- states Method A's independence as **inferred, not measured**, because it was
  never measured.

The identity itself stands. What was wrong was §5's description of it.

## Reference added

new bibitem for the companion's v1.3 correction notice

v1.2's bibliography numbering is **unchanged**: the companion's v1.3 is appended
as the new final entry, [26]. This was checked mechanically — the count must
increase by exactly one and the new entry must be **last**, so that no existing
citation number can shift.

---

## ⚠️ Two different papers each have a version 1.3

This trips readers and it tripped an earlier session, so it is stated plainly:

| | concept DOI | its v1.3 |
|---|---|---|
| **this paper** | `10.5281/zenodo.20719042` | record 22731371, published 2026-09-13 |
| **the companion** | `10.5281/zenodo.20455089` | version DOI `10.5281/zenodo.22831933` |

The new reference cites the **companion's** v1.3. The base of this revision is
**this paper's** v1.2.

## ⚠️ The revision's wording diverges from this paper's published v1.3

This paper's v1.3 already states the D₅⁽¹⁾ identification conjecturally and
already carries a *Correction notice* withdrawing "completes part (ii)(a)" —
i.e. it covers items 1 and 2, but **in different words**, and it does **not**
cover items 3, 4 or 5.

Applying CT-S52's item 1 and 2 text to v1.2 therefore produces wording that does
not match the published v1.3. The cover letter promised that the deposit and the
submission would be identical. **Keeping that promise requires depositing a new
version of concept 20719042 matching whatever the editor accepts** — which is
the standing plan, and is why nothing has been deposited yet.

## Not in the source

The cover-letter sentence is not part of the manuscript. It is listed separately
as a correction for the editor, not as an edit.

---

## Checks that were required to be able to fail

- v1.2's source located by **byte-identical rebuild**, with v1.0 reproduced
  byte-identically as the positive control. Without that control, "nothing here
  builds to v1.2" could not be told from "nothing here builds to anything".
- all 33 replacements matched **exactly once**; the whole buffer was
  validated **before** any write.
- build: 0 errors, **0 undefined references**, read from the `.log` rather than
  trusted from the build script's summary.
- rendered diff v1.2 → revision: every changed block attributable to items 1–5,
  with the reflow test exercised **both ways** — it must collapse hyphenation
  and must **not** collapse a changed figure, or it would hide the 8.84 → 3.69
  edit that is the point of item 5.
- the Amendment H sweep re-run after editing, with every remaining hit read.
- the submitted v1.2 artefacts re-hashed and confirmed **byte-unchanged**.
