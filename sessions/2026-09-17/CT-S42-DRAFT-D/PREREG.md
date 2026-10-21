# PREREG — CT-S42-DRAFT-D (Group D: §7 monodromy and Stokes data, §8 leaf transport)

Written before any script in this session ran. Thresholds fixed here are not
revised after seeing results; a threshold that proves ill-posed is reported as
a finding, not edited.

## 0. What this session is

A **drafting** session. It writes `section7.tex` and `section8.tex` as paper
prose from the corpus, and gates the prose against the corpus. It runs **no new
mathematics**: every number in the prose is transcribed from a claim record
that already exists, and no formula is re-derived. See §6 for the scope limit
this leaves open.

## 1. Hypothesis under test

**H.** Sections 7 and 8, as drafted, cite only claim ids that resolve in the
corpus and are not superseded; carry, for every cited id, the label that id
currently holds in the corpus; state no numeric literal that does not appear in
a cited claim's own record; and honour the three pre-declared transcription
hazards of §5.

H is a statement about the **drafted files**, not about the mathematics. It can
be false while the mathematics is right, and true while a formula is wrong.

## 2. Observables

- **O1** — for each `\texttt{Sxx-yy}` in the drafted prose: resolves / does not.
- **O2** — for each resolved id: is any corpus claim's `supersedes` field equal
  to it.
- **O3** — for each id carrying an adjacent `\textbf{LABEL}`: does that label
  equal the corpus label for that id.
- **O4** — for each significant numeric literal in the prose: does it appear in
  the `claim` or `review_note` text of some id cited in the same subsection.
- **O5** — the three hazard markers of §5 are present in the drafted text.

**Normalisation for O4, fixed here.** A *significant literal* is an integer run
of ≥ 3 digits, or a decimal, or `m\times10^{-k}`, or a bare `10^{-k}`.
`m\times10^{-k}` matches the claim form `me-k`; bare `10^{-k}` matches `1e-k`.
The search pool is `claim` **and** `review_note` — CT-S41's C5 reported a false
hit because it read `claim` only, and that repair is inherited here.

## 3. Falsifiers, with thresholds

| id | fires when |
|----|-----------|
| **F1** | any cited id fails to resolve |
| **F2** | any cited id is superseded by a later claim |
| **F3** | any prose label differs from the corpus label |
| **F4** | any significant literal is unaccounted for |
| **F5** | fewer than **20** literals are inspected (non-vacuity floor on O4) |
| **F6** | any hazard marker of §5 is absent |
| **F7** | the assembled build reports any error, undefined reference, or multiply-defined label |
| **F8** | `forwardrefs_E.tex` declares a label for a section that exists |

F5 is the **non-vacuity assertion on the numerator**, in the operator's phrase
from the CT-S41 review: *"a count printed as a fraction with zero numerator and
a nonzero denominator is the signature, and the fix is a non-vacuity assertion
on the numerator before printing."* CT-S41's own confirmation script printed
`0/11` — a count of zero tests rendered as a result. Every counting reader in
this session asserts its numerator before printing it.

## 4. Vacuity pre-check (control arms)

The gate is run against **in-memory mutations** of the drafted files, so no
deliberate defect is ever written to disk. Each arm must be CAUGHT, and each
arm must first assert that **its mutation site exists** — an arm that cannot
reach its site reports MISSED identically to a rule that does not work
(CT-S41 S41-05).

| arm | mutation | must fire |
|-----|----------|-----------|
| D1 | a cited id changed to one absent from the corpus | F1 |
| D2 | a real but superseded id substituted | F2 |
| D3 | **the deliberately wrong label** — `S22-15` relabelled PROVEN | F3 |
| D4 | a digit transposed in a quoted literal | F4 |
| D5 | the literal pool emptied | F5 |
| D6 | a hazard marker deleted | F6 |
| D7 | `forwardrefs_E.tex` re-declares `sec:monodromy` | F8 |
| D8 | `section7.tex` truncated below the byte floor | C1 |

D3 is the control the operator's standing rule requires: *"one deliberately
wrong label inserted as a control must be caught."* `S22-15` is chosen because
its own claim text contains the sentence *"it is not a proof of leaf
membership"* — relabelling it PROVEN is the exact error the paper must not make.

**Reader-integrity uses bounds, never fingerprints** (CT-S36 S36-09): a byte
floor and minimum counts, not an exact hash of the file under test. A
fingerprint fires first and masks the check it precedes.

## 5. Transcription hazards, declared before drafting

1. **`S22-15` is VERIFIED, not PROVEN.** Its own text says the agreement "is
   not a proof of leaf membership". The prose must carry the label and the
   disclaimer together.
2. **`S22-20` remains VERIFIED-numerical.** `S22-24` refutes the simplest
   structural route to it and says so explicitly: *"S22-20 REMAINS
   VERIFIED-NUMERICAL (two independent runs), not STRUCTURAL."* The prose must
   not upgrade it.
3. **The `S25-02` upgrade is about the parameters, not the Stokes data.** The
   outline states the trap directly: the branch relation is "no longer purely
   numerical" but "is not thereby proved at the level of the character variety,
   and the paper must not elide the difference." §8 must state both halves in
   the same paragraph.

## 6. Scope limit, stated in advance

**No displayed formula is re-derived.** The gate checks that citations resolve
and that labels and literals match the corpus. A transposed digit inside a
formula that appears nowhere in a claim text passes every rule here and builds
clean. This is the standing gap recorded at CT-S40 and CT-S41 and scoped by the
operator for a pass after Group E; it is restated here so that this session's
PASS is not read as more than it is.

## 7. Rulings adopted in this session

- **Ruling 1 (census).** The gate prints the corpus census **with a
  fingerprint** — a sha256 over the sorted list of walked file paths — and
  makes **no claim of byte-reproducibility across sessions**. A differing count
  with a differing fingerprint is a different input, not a disagreement.
- **Ruling 2 (preamble).** `preamble.tex` is authoritative; `combined_0to8.tex`
  `\input`s it and declares no package of its own. No per-group wrapper is
  written in this session.

## 8. Budget

≤ 1 day. Halt and report if any falsifier fires, if a convention is ambiguous,
if required data is missing, or if runtime exceeds 3× the budget.
