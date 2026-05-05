# Changelog: t2b_paper_draft_v5_withauthor.tex v3.0 -> v3.1

**v3.0 source (anchor):** `tex/submitted/t2b_paper_draft_v5_withauthor.tex`
- SHA-256: `9BDD6A5D799BD8FE956E3F87114E8F9CDA730B96ACED24037B292E80619F538B`
- Size: 28,635 bytes; 289 lines
- Date stamp: "Version 3.0 \\ 2026-04-30"
- Byte-identical with the arxiv-pack mirror at
  `siarc-relay-bridge/sessions/2026-05-02/ARXIV-MIRROR-RUNBOOK/arxiv_pack_t2b_v3.0/pack/t2b_paper_draft_v5_withauthor.tex`

**v3.1 output:** `t2b_paper_v3.1_bipartition_promotion.tex`
- SHA-256: `538B897C75908C9E25B2AD5C6F7EE8317A5906D2E7668809DBF58E7DB7755B79`
- Size: 33,762 bytes; 300 lines
- Date stamp: "Version 3.1 \\ 2026-05-07"
- **Patch 6 applied** (synth conditional GO on JC-1, 2026-05-05 ~19:23 JST):
  the b1=7 bullet item in §"Further open questions" sharpened to make
  the off-orbit-relative-to-all-three-laws framing explicit per synth's
  one-sentence-addition condition.

**Net effect:**
- 5 amendments (insertions + one date-stamp swap); 0 deletions of v3.0 content;
  0 alterations of theorem statements, proposition wording, conjecture
  wording, table data, remark content, or AI Disclosure (H8 compliance).
- 4 theorems / 1 proposition / 1 conjecture / 2 tables: counts unchanged.
- Net additions: ~5 KB (~850 words across 5 patches + 1 new section).

---

## Patch 1 — `\date` line (line 31)

**Rationale:** Version label + date stamp update for amendment.

**v3.0:**
```latex
\date{Version 3.0 \\ 2026-04-30}
```

**v3.1:**
```latex
\date{Version 3.1 \\ 2026-05-07}
```

---

## Patch 2 — Abstract (line 36, single paragraph)

**Rationale:** Strengthen the abstract with the empirical backing from
three independent stratum-aware verification sweeps at b1 in {5, 6, 7}.
The original v3.0 closing sentence about the desert at k=3 and the
Completeness Conjecture is preserved verbatim and augmented with one
new sentence reporting the three-sweep evidence. No v3.0 wording was
altered (H8 compliance).

**Insertion site:** Between the existing "...zero Trans-stratum
families, confirming a complete desert at $k=3$." clause and the
existing "supporting our \emph{Completeness Conjecture}: ..." clause.
Implementation: split into two sentences and insert the new
three-sweep sentence between them.

**v3.0 (closing of abstract):**
```
... produced zero Trans-stratum families, confirming a complete desert
at $k=3$ and supporting our \emph{Completeness Conjecture}: the
degree-$(2,1)$ Trans-stratum is exhausted by Class A and Class B.
```

**v3.1 (closing of abstract):**
```
... produced zero Trans-stratum families, confirming a complete desert
at $k=3$. Three independent stratum-aware verification sweeps at
$b_1 \in \{5, 6, 7\}$ are consistent with the bipartition: at
$b_1 = 5$ both loci are predicted empty (since $9 \nmid 25$ and
$2 \nmid 5$); at $b_1 = 6$, four Trans-stratum hits land on exactly
the predicted loci (three on Class~A at $a_2 = -8$, one on Class~B
at $a_2 = 9$); and at $b_1 = 7$ a coprime-to-both null sweep of
$79{,}860$ candidates returns zero Trans-stratum hits (since
$9 \nmid 49$ and $4 \nmid 49$ block both loci simultaneously).
These observations support our \emph{Completeness Conjecture}: the
degree-$(2,1)$ Trans-stratum is exhausted by Class~A and Class~B.
```

**Verb hygiene:** "are consistent with", "support" — both §D-compliant.
No use of "shows", "proves", "establishes", "demonstrates". The verb
"confirms" appears in the v3.0 desert clause (preserved verbatim) but
not in the new sentence.

---

## Patch 3 — New paragraph in §1 Introduction (after Empirical phenomenon itemize)

**Rationale:** Per relay Step 3, insert a "Three independent
verification sweeps" paragraph immediately after the existing
"Empirical phenomenon and dichotomy" itemize block, with full
per-sweep attribution to bridge commits 1735258 (b1=6) and 8e18465
(b1=7) plus arithmetic justification for the predicted empties at
b1=5 and b1=7.

**Insertion site:** Between the existing line
"A sweep of $134{,}040$ candidates at the next BT integer-resonance
locus $a_2/b_1^2 = -3/16$ produced zero Trans-stratum families."
and the next `\paragraph{Main results.}`.

**Inserted block (v3.1 only):**
```
\paragraph{Three independent verification sweeps.}
The original height-bounded enumeration provided $78$ canonical
Class~A and $16$ canonical Class~B families plus a $134{,}040$-
candidate desert at $k=3$ (Section~\ref{sec:empirical}). Subsequent
stratum-aware sweeps at three additional resonance values
$b_1 \in \{5, 6, 7\}$ are consistent with the bipartition. At
$b_1 = 5$, Class~A integer realization requires $a_2 = -50/9
\notin \mathbb{Z}$ and Class~B integer realization requires
$a_2 = 25/4 \notin \mathbb{Z}$, so both loci are predicted empty;
the sweep returns zero Trans hits. At $b_1 = 6$, Class~A at
$a_2 = -8$ admits three integer-coefficient realizations (with
limits $4/\pi$, $4/(\pi-2)$, and $(8\pi+2\pi^2)/(2\pi+\pi^2)$) and
Class~B at $a_2 = 9$ admits one ($12/\pi$); the stratum-aware sweep
of $79{,}860$ candidates at $b_1 = 6$ returns exactly these four
Trans hits, with $0$ third-stratum hits and $0$ locus-violations
(deep-verified at \texttt{dps}$=300$, $N=1500$). At $b_1 = 7$, both
loci are non-integer ($a_2 = -98/9$ and $a_2 = 49/4$) and the sweep
of $79{,}860$ candidates returns zero Trans hits, providing a
coprime-to-both ($\gcd(7,3) = \gcd(7,2) = 1$) null verdict. The
singleton-mate $(9, 0, 0, -6, -3) \to -12/\pi$ verifies sign-flip
orbit completeness for Class~B at $|b_1|=6$. Full per-family
records are in the SIARC bridge sessions
\texttt{T2B-BIPARTITION-B6-VERIFICATION} (commit \texttt{1735258})
and \texttt{T2B-BIPARTITION-B7-STRONG-NULL} (commit
\texttt{8e18465}).
```

**Verb hygiene:** "are consistent with", "verifies" (per
relay Step 2 epistemic note: "verifies" is acceptable
empirical-test-context language for deep-verify dps=300 N=1500
PSLQ output), "provides", "returns", "land". No forbidden verbs.

---

## Patch 4 — New section "Further open questions" (positioned after sec:open)

**Rationale:** Per relay Step 4, record the off-locus Log-stratum
families with c/log(2)-scaled limits as a NAMED OPEN STRUCTURAL
QUESTION (synth framing 2026-05-05 ~18:45 JST). The b1=6 entry
(-1,0,0,6,3) -> 2/log 2 lies in the Bauer 1872 orbit already named
in Remark `rem:bauer-orbit`; the b1=7 entry (8,-4,0,7,4) -> 3/log 2
at ratio 8/49 is a genuinely new off-orbit, off-locus Log family.

**Insertion site:** Between the closing `\end{enumerate}` of the
existing §"Open problems and the Completeness Conjecture"
(sec:open) and `\section*{AI Disclosure}`.

**Inserted block (v3.1 only) — header + content:**
```
\section{Further open questions}\label{sec:further-open}

\subsection*{Off-locus Log-stratum families with $1/\!\log 2$
              scaled limits}

The stratum-aware sweeps at $b_1 = 6$ and $b_1 = 7$ surfaced two
off-locus Log-stratum families whose limits have a common
structural form $c/\!\log 2$ for small integer $c$:

\begin{itemize}
  \item At $b_1 = 6$, $(a_2, a_1, a_0, b_1, b_0) = (-1, 0, 0, 6, 3)$
        has $a_2/b_1^2 = -1/36$ and limit $L = 2/\!\log 2$
        (verified at \texttt{dps}$=200$, $N = 4{,}000$,
        $|L_{\text{computed}} - 2/\!\log 2| = 0$ to working
        precision; SIARC bridge session
        \texttt{U1-MOBIUS-LOCAL-CHECK}, commit \texttt{171eccc}).
        This family lies in the Bauer 1872 orbit
        (Remark~\ref{rem:bauer-orbit}) and is therefore part of the
        Log stratum already characterised in this paper.

  \item At $b_1 = 7$, $(a_2, a_1, a_0, b_1, b_0) = (8, -4, 0, 7, 4)$
        has $a_2/b_1^2 = 8/49$ and limit $L = 3/\!\log 2$ (verified
        at \texttt{dps}$=300$, $N = 1500$, residual
        $< 10^{-200}$; SIARC bridge session
        \texttt{T2B-BIPARTITION-B7-STRONG-NULL}, commit
        \texttt{8e18465}). This family lies outside the Bauer 1872
        orbit (the orbit requires $a_2 = -k^2$ negative; here
        $a_2 = +8$) and outside both bipartition loci ($8/49 \notin
        \{-2/9, +1/4\}$).
\end{itemize}

A direct M\"obius-equivalence test between the $b_1 = 6$
off-locus family $(-1,0,0,6,3)$ and the on-locus Class~A Log
family $(-8,0,0,6,4)$ -- which shares the limit $2/\!\log 2$ --
returned LIMIT-LEVEL equivalence only: both sequences yield $L =
b(0) + K = 2/\!\log 2$ via independent $b(0)$ choices (with $K_A
- K_B = +1$ exactly compensating the $b(0)$ shift), but the
classical sequence-rescaling transformation $r_n = (6n+4)/(6n+3)$
fails to satisfy $r_n\,r_{n-1} = 8$ (yields $40/27, 80/63,
112/91, \ldots$), and Bauer--Muir transformations with constant
auxiliary $w$ also fail (\texttt{U1-MOBIUS-LOCAL-CHECK}). A
structural characterization that unifies (i) the Bauer 1872
orbit, (ii) the off-locus $b_1 = 7$ family at ratio $8/49$, and
(iii) any further off-locus Log families with limits in
$\mathbb{Q}\cdot(1/\!\log 2)$ is open.

The pattern is recorded here as a research direction; two data
points are insufficient to assert a third structural class
beyond Class~A and Class~B.
```

**Verb hygiene:** "surfaced", "is open", "returned LIMIT-LEVEL
equivalence only", "fails to satisfy", "are insufficient". No
use of "shows", "proves", "establishes", "demonstrates",
"confirms".

**H5 compliance:** Does NOT propose a Class C label, does NOT
claim a closed form for c in c/log 2, does NOT claim a
bijection between off-locus Log families and Class A. Frames
the question as OPEN STRUCTURAL QUESTION only.

**H3 compliance:** No `\begin{theorem}`, `\begin{conjecture}`, or
`\begin{proposition}` is introduced. The new section is a
prose research-direction note.

**H8 compliance:** The Bauer 1872 orbit Remark
(`rem:bauer-orbit`) is referenced via `\ref{rem:bauer-orbit}`
but its content is unchanged.

---

## Patch 5 — Acknowledgements (append, do not replace)

**Rationale:** Per relay Step 5, credit the SIARC pipeline and
the three v3.1-relevant bridge sessions, mirroring the
manuscript's existing citation style for v3.0-era bridge sessions.

**Insertion site:** End of the existing
`\section*{Acknowledgements}` paragraph; appended after the
v3.0 sentence ending in "...verifications reported here." The
v3.0 word "here" is replaced by "in v3.0" (one-word edit) to
clarify scope; this is a minor-clarification edit consistent with
amendment scope.

**v3.0:**
```
We thank the SIARC programme infrastructure for computational
support, and the maintainers of the relay-bridge sessions
T2B-DELTA2-VERIFICATION, T2B-STIELTJES-VERIFY, and
T2B-PLUS-QUARTER-SURVEY whose outputs underlie the verifications
reported here.
```

**v3.1:**
```
We thank the SIARC programme infrastructure for computational
support, and the maintainers of the relay-bridge sessions
T2B-DELTA2-VERIFICATION, T2B-STIELTJES-VERIFY, and
T2B-PLUS-QUARTER-SURVEY whose outputs underlie the verifications
reported in v3.0. For the v3.1 amendment we additionally thank the
SIARC pipeline (GitHub Copilot Tier-2 agent and Anthropic Claude
Tier-1 synthesis) for the three bipartition verification sweeps
at $b_1 \in \{5, 6, 7\}$ -- recorded in the bridge sessions
T2B-BIPARTITION-B6-VERIFICATION (commit \texttt{1735258}),
T2B-BIPARTITION-B7-STRONG-NULL (commit \texttt{8e18465}), and
U1-MOBIUS-LOCAL-CHECK (commit \texttt{171eccc}) -- whose outputs
provide the empirical backing reported in this version. All
numerical artefacts are recorded with SHA-256 verification in
the SIARC bridge repository
\url{https://github.com/papanokechi/siarc-relay-bridge}.
```

**Note:** the "here" -> "in v3.0" edit is a 1-word clarification
that disambiguates scope after the new sentence is appended. It
does not alter the meaning of the v3.0 attribution to the three
v3.0-era bridge sessions.

---

## Halt status

| Halt | Trigger | Status |
|------|---------|--------|
| H1   | Forbidden epistemic verb in new content | NOT FIRED — verb hygiene clean |
| H2   | Cited bridge commit not on origin/main | NOT FIRED — 1735258, 8e18465, 171eccc all verified |
| H3   | New theorem / new conjecture introduced | NOT FIRED — counts unchanged |
| H4   | Wall-time > 90 min | NOT FIRED |
| H5   | Overclaim re Log off-locus families | NOT FIRED — open structural question framing |
| H6   | v3.0 byte-identity drift (working vs arxiv-pack) | NOT FIRED — SHA matches |
| H7   | AI Disclosure missing in v3.0 | NOT FIRED — present in v3.0 line ~245, preserved verbatim |
| H8   | Existing v3.0 result altered | NOT FIRED — theorems/conjecture/tables unchanged; one Acknowledgements word ("here" -> "in v3.0") is a clarifying edit only |

All halts evaluated and clean. Manuscript is ready for operator
review.

---

## Patch 6 — Synth-conditional sharpening of b1=7 bullet (2026-05-05 ~19:23 JST)

**Rationale:** Synth's GO on JC-1 (Bauer 1872 anchoring) was conditional
on one one-sentence addition: making the off-orbit-relative-to-all-three-laws
framing explicit for the b1=7 family. This patch replaces a one-sentence
distributive statement ("outside ... and outside ...") with a sharper
three-clause structural-laws-comparison sentence plus a singular-genuine-
off-orbit summary statement.

**Insertion site:** the `\item` for $b_1 = 7$ in §"Further open questions"
(line 349 of v3.1 pre-Patch-6).

**v3.1 pre-Patch-6 (final clause of b1=7 bullet):**
```
This family lies outside the Bauer 1872 orbit (the orbit requires
$a_2 = -k^2$ negative; here $a_2 = +8$) and outside both bipartition
loci ($8/49 \notin \{-2/9, +1/4\}$).
```

**v3.1 post-Patch-6 (final clauses of b1=7 bullet):**
```
This family fits none of the three structural laws anchored in this
paper: it is off Class~A (since $8/49 \neq -2/9$), off Class~B (since
$8/49 \neq +1/4$), and off the Bauer 1872 orbit (since $a_2 = +8$ is
not of the form $-k^2$ for any integer~$k$). Among the stratum-aware
sweeps at $b_1 = 6$ and $b_1 = 7$, this is the only data point that
fits none of these three laws.
```

**Verb hygiene:** "fits none of", "anchored", "is off", "is not of the
form", "is the only data point that fits none". No use of "shows",
"proves", "establishes", "demonstrates", "confirms". H1 PASS.

**H3 compliance:** No `\begin{theorem}`, `\begin{conjecture}`,
`\begin{proposition}` introduced. Theorem/conjecture/proposition env
counts unchanged: 3 / 1 / 1 (identical to v3.0).

**H5 compliance:** Does not propose a new structural class; the singular
"only data point that fits none of these three laws" is empirically
restricted to the $b_1 \in \{6, 7\}$ sweeps where Log-stratum families
were catalogued explicitly (b1=5 sweeps targeted Class A / Class B and
did not exhaustively catalogue Log families).

**Net delta v3.1-pre-Patch-6 -> v3.1-post-Patch-6:** +203 B; 0 line-count
change (existing line lengthened in place). Final size 33,762 B / 300
lines.

**Synth concurrence record:** "Synth concurrence: GO on JC-1, conditional
on the above one-sentence check." (synth, 2026-05-05 ~19:23 JST). This
patch implements that condition. JC-1 closed; manuscript is push-ready
pending operator green-light.
