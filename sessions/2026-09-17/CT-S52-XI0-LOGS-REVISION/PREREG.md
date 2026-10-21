# PREREG — CT-S52-XI0-LOGS-REVISION

Written before any computation in this session. Thresholds fixed here are not
revised after seeing results; if a threshold proves ill-posed that is reported as
a finding (P0, and the CT-S51 precedent for `C2`).

Two parts. Part A is a computation; Part B is an edit to a copy of a manuscript
source, gated on Part A's verdict.

---

## Part A — is ξ = 0 log-free for L_V?

### Hypothesis

H-A. The point ξ = 0 of the Borel operator

    L_V = Σ_{k=0}^{4} p_k(ξ) D^k ,   p_0 ≡ 1,   p_k ∈ ℚ(√3)[ξ],

as printed in Appendix A.1 of the submitted manuscript, is an **apparent**
singularity: its four local exponents are the consecutive integers {−1, 0, 1, 2}
and a full basis of four formal solutions exists **without logarithms**.

The manuscript asserts apparency (Prop. 2.4 `prop:exponents`) with the stated
reason *"the four exponents are consecutive integers, so the point is apparent"*.
That implication is false in general — consecutive integer exponents are exactly
the resonant case in which logarithms may be **forced**. H-A is therefore under
test, not assumed, and the manuscript's stated justification is not used as
evidence for it.

### Observables

O-A0 (transcription). The coefficient tuples of p_1…p_4 read out of the
manuscript `.tex` by a parser, compared entry-by-entry against an independently
hand-typed table in the script.

O-A1 (residual). res(N) = coefficient of ξ^N in L_V B̂, computed in **exact**
ℚ(√3) arithmetic (Fraction pairs; no floating point anywhere), for
N = 0, 1, …, 129, with b_m = a_{m+1}/m! and a_n the exact ℚ(√3) V_quad series
coefficients.

O-A2 (exponents). The roots of the indicial polynomial
I(s) = Σ_{(k,i): k−i = L} p_{k,i} (s)_k at ξ = 0, where L = max(k − i) over
nonzero p_{k,i} and (s)_k is the falling factorial.

O-A3 (logs). Running the Frobenius recursion from the **lowest** exponent
s = −1 with each coefficient c_n carried as an exact ℚ(√3)-linear form in the
free parameters introduced so far: at every n with I(s+n) = 0 (the resonant
steps, expected n ∈ {1, 2, 3}), the obstruction vector `rest`. `rest` = 0 ⇒ the
recursion is consistent and a new free parameter enters; `rest` ≠ 0 ⇒ a
logarithm is forced at exponent s+n.

### Falsifiers, with thresholds

F-A0. Any disagreement between parser and hand-typed table in any one of the 12
coefficient entries ⇒ HALT; the transcription is not established.

F-A1. Any N ≤ 129 with res(N) ≠ 0 **exactly** (threshold: exact zero in ℚ(√3),
not a tolerance) ⇒ HALT. Either the transcription or the corpus B̂ is wrong, and
nothing downstream may be believed.

F-A2. The root multiset of I is anything other than {−1, 0, 1, 2} ⇒ HALT; the
manuscript's Prop. 2.4 exponent statement is itself wrong and Part B item 4
changes scope.

F-A3. Fewer than 4 free parameters at the end of the run, i.e. some resonant
step has `rest` ≠ 0 ⇒ verdict **LOGARITHMS FOUND**, naming the exponent. This is
not a halt: it is the other branch of the task, and Part B item 4 takes its
alternative wording.

### Controls that must be able to fail

Both controls run through the **same** Frobenius routine as the observable, with
no special-casing.

C-LOG. L_log = (ξ³ − 2ξ)D² + (2 − 3ξ²)D + 4ξ. Exponents {0, 2}; basis
{ξ², 1 + ξ² log ξ}. The routine **must** report a forced logarithm at exponent 2
(resonant step n = 2 from s = 0). If it reports log-free, the routine cannot see
a logarithm and the whole of Part A is void.

C-NOLOG. L_hyp = ξ(1 − ξ)D² + (2 − 3ξ)D − 1. Exponents {−1, 0}; basis
{ξ^{-1}, −log(1−ξ)/ξ}, both log-free at ξ = 0 despite the integer-difference
resonance at n = 1. The routine **must** report log-free. If it reports a
logarithm, the routine flags resonance as such and its verdict on L_V would be
uninformative.

Two controls are required because either one alone is passed by a degenerate
routine: a routine that always says "log" passes C-LOG, one that always says
"log-free" passes C-NOLOG.

### Ordering (CT-S47 rule)

The observable is evaluated **first** and printed before the controls run. A
control arm may not gate, overwrite or suppress the observable's result; if a
control fails, the observable's value still stands in the output and the verdict
is reported as VOID rather than replaced. This is the repair adopted after
CT-S47 §3.8, where a vacuity pre-check guarding a PASS turned a real finding
into a refusal.

### Vacuity pre-check for O-A1

The residual check must be able to see a wrong operator. Perturb one printed
coefficient of p_2 by +1/418501 and re-run res(0..20): at least one N must
become nonzero. If none does, the residual check is vacuous at this order and
O-A1 carries no weight.

### Label rule

Part A is exact rational arithmetic in ℚ(√3) end to end. If it completes with no
floating-point step anywhere, the verdict may be labelled **PROVEN** — but only
as a statement about the **formal** solution basis of the printed operator at
ξ = 0. Apparency of the singularity in the analytic sense additionally needs the
local solutions to be single-valued, which follows here only because all four
exponents are integers *and* no logarithm occurs; that combination is what is
being tested, so the label attaches to the conjunction and to nothing more.

---

## Part B — the revision

### Sweep first (P0 Amendment H)

Before any edit, grep the located source for every occurrence of: `D_5`,
`Sakai`, `Painlev` near `transcendent`, `completes`, `twice`, `independent`,
`structural argument`, `apparent`. The **full** hit list with line numbers is
part of the output, including hits not edited and the reason each was left. An
empty sweep and an absent sweep must not be distinguishable in the report
(Amendment H, clause added on adoption).

### Identification of the source

H-B. Exactly one `.tex` in the tree rebuilds to the submitted PDF. Observable:
page count, and the text layer of the rebuild compared against the text layer of
the submitted PDF. Falsifier: if no candidate matches, or more than one does,
report that and do not guess by filename. The submitted PDF is identified by its
own digest, recorded in the report; filename is evidence of nothing.

### Checks after editing

K1. `pdflatex` on the revised copy: 0 undefined references, 0 undefined
citations.
K2. Rendered diff (text layer, submitted vs revised) shows only intended edits;
every differing line is accounted for in the changes list.
K3. The sweep is re-run on the revised source and every remaining hit is
accounted for, edited or not.
K4. The submitted source is **byte-identical** before and after this session
(digest recorded both times). Work happens on a copy.

### Out of scope, explicitly

The cover letter is not in the source. Its sentence is listed as a correction for
the editor, separately from the edit list, and is not edited here.

Nothing is uploaded, submitted, deposited, committed, pushed or tagged.
