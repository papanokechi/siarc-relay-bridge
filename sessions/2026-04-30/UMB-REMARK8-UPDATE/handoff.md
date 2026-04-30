# UMB-REMARK8-UPDATE — Handoff

**Task ID:** UMB-REMARK8-UPDATE
**AEAL class:** manuscript-update
**Depends on:** UMB-RES-EXTEND-PROJ CONFIRMED-BY-EXAMPLE ✅
**Verdict:** **CLEAN** — UMB §4 updated; PDF builds 0 errors.
**Pushed:** No (relay says do not push until papanokechi confirms).

## 1. Interpretation note (Edit 1 / Edit 2)

UMB main.tex shares one counter across `conjecture`, `definition`,
and `remark` environments. By literal counter order, the 8th
theorem-counter item in the file is `\begin{remark}[Pre-revision
form]` at line 263. That remark is about the v1→v3 conjecture
change, not a projective-coordinate claim, so appending the
projective-confirmation paragraph there would be thematically
incoherent and produce a self-referential "Remark 8 confirms
Remark 8" sentence.

The empirical claim verified by UMB-RES-EXTEND-PROJ is the
**Class A clause of Conjecture~\ref{conj:t2b}** (trans-stratum at
$a_2/b_1^2 = -2/9$ for $\PSLZ$). This clause is the natural target
of the projective sweep. Accordingly, Edit 1 was implemented as a
**new remark** placed at the end of §4, with the inserted text
referring to "the Class A clause of Conjecture~\ref{conj:t2b}"
in place of "Remark~8". The new remark carries the label
`rem:projective-verify`.

Edit 2 was a no-op: a grep for "open" / "unverified" / "verified"
near §4 returned only references to the rigorous monodromy
derivation as "the central open problem" (line 295), which is
*not* the empirical claim and is correctly preserved as open.
No sentence in §4 currently describes the empirical Class A
claim as open or unverified, so there was nothing to update.

Edit 3 (claims.jsonl) is recorded in this session folder; UMB
itself does not carry an in-tree claims.jsonl.

## 2. Edit 1 — new remark inserted

**File:** `tex/submitted/umbrella_program_paper/main.tex`
**Location:** end of §4 (`The Trans-Stratum Conjecture`),
inserted between Remark 10 ("Why $-2/9$?") and `\section{Open
Problems}`.

**Inserted block (label `rem:projective-verify`):**

```
\begin{remark}[Projective verification of Conjecture~\ref{conj:t2b}, Class A]
\label{rem:projective-verify}
A targeted projective-coordinate sweep
($H = 8$, $b_1 \in \{3, 6, \ldots, 30\}$ subject to $3 \mid b_1$,
$48{,}552$ primitive 5-tuples
$(a_2, a_1, a_0, b_1, b_0)$ satisfying $9 a_2 + 2 b_1^2 = 0$,
$\gcd = 1$, $b_1 > 0$; $43{,}915$ distinct-$L$ families;
stratified random sample of $400$ groups, $40$ per $b_1$ bucket)
confirms the Class A clause of Conjecture~\ref{conj:t2b}
empirically: $387/400$ sampled families are Trans, with
$0$ Log, $0$ Alg, $13$ rational, and $0$ phantom hits ...
The smallest witness is
$(a_2, a_1, a_0, b_1, b_0) = (-2, 0, 1, 3, -1)$ with
$L \approx 0.26057$. ...
Every $3 \mid b_1$ bucket in the sample contains at least
$32$ Trans families. Full numerics ... in
\texttt{sessions/2026-04-30/UMB-RES-EXTEND-PROJ/} of the
SIARC relay bridge repository.
\end{remark}
```

(Counter index of the new remark: 11.)

## 3. Verification

| Check                                              | Result          |
|----------------------------------------------------|-----------------|
| `(-2,0,1,3,-1)` in main.tex                        | 1 hit ✅         |
| "projective" / "Projective" in main.tex            | 4 hits ✅        |
| "open" / "unverified" describing Class A claim     | 0 hits ✅ (none) |
| `pdflatex -halt-on-error main.tex` (×2 passes)     | 0 errors ✅      |
| Output                                             | 7 pages, 307,113 B |

## 4. File hashes (post-edit)

| File          | sha256                                                              |
|---------------|---------------------------------------------------------------------|
| `main.tex`    | `0C630DE2524F809DC56F4DB099325779CB54897CF5C7D90EC7C435432711F407` |
| `main.pdf`    | `EB4335FCA5807D27DFB5EC85CF59C23157AFC4B7B7EDD605DBFBA2C10598B3D5` |

## 5. Pending push queue

After papanokechi confirmation, three commits are now ready
to push together:

1. `9a8dc28` — UMB-T2B-CITE-UPDATE (T2B citation → v3.0 DOI)
2. `5e67cab` — UMB-RES-EXTEND-PROJ (Remark 8 projective rerun)
3. (this) — UMB-REMARK8-UPDATE (UMB §4 records the verification)
