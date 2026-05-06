# Operator dispatch instructions — P-009 M8b caveat

**Branch active:** **(b) — DRAFT_NOT_YET_STARTED**
(no `tex\submitted\p009_*.tex` working copy exists in workspace as of
2026-05-06 directory listing).

The caveat is therefore **pinned for future paste-time**; it is NOT to
be inserted into any current `.tex` file.

---

## What the operator does NOW

1. Copy the active caveat file from the bridge session deliverables
   to the workspace control center:

   ```
   Copy-Item `
     "siarc-relay-bridge\sessions\2026-05-06\P009-M8B-CAVEAT-FINAL\p009_m8b_caveat_active.txt" `
     "tex\submitted\control center\p009_caveat_pinned.txt"
   ```

   Storage path:
   `tex\submitted\control center\p009_caveat_pinned.txt`

   This is a workspace bookkeeping move only — no commit, no push, no
   tex-file edit.

2. Add a one-line marker into `tex\submitted\control center\memo.txt`
   (or equivalent staging memo) noting that `p009_caveat_pinned.txt`
   exists and which variant it carries (v1 NOT_YET_DISPATCHED).
   Example line:

   ```
   2026-05-06  P-009 M8b caveat pinned (v1 NOT_YET_DISPATCHED)
               at p009_caveat_pinned.txt; SHA256 prefix 8EFC6C93;
               re-fire on M8b dispatch (per relay 050).
   ```

   This optional bookkeeping is recommended but not strictly required
   by the relay 050 spec; the bridge handoff already contains all
   provenance.

---

## What the operator does at P-009 PASTE-TIME (future)

When P-009 acquires a `tex\submitted\p009_*.tex` working copy:

1. Re-check **STEP 6 re-fire conditions** in
   `p009_m8b_caveat_all_variants.md` §6. If any condition has fired,
   re-execute relay 050 (or its successor) before paste — the variant
   may have flipped (v1 → v2/v3/v4). Do NOT paste a stale variant.

2. If v1 is still active: paste the contents of
   `tex\submitted\control center\p009_caveat_pinned.txt` verbatim
   into the §discussion section of `p009_*.tex`, immediately AFTER
   the main classification result (or wherever the manuscript chain
   most naturally hosts the M8b enrichment caveat — typical placement
   is the paragraph that introduces "open structural questions" or
   "companion milestones").

3. The active text is one self-contained sentence; place it as a
   single-paragraph `\paragraph{Companion milestone M8b.}` block, e.g.:

   ```latex
   \paragraph{Companion milestone M8b.}
   Stokes-multiplier discrimination (companion milestone M8b)
   will supply an additional independent test of the SIARC
   stratification at $d\geq 3$, conditional on the M8b dispatch
   landing within the relevant binding window and on the
   binding-window result.
   ```

   (Note: `d≥3` Unicode in the pinned `.txt` becomes `$d \geq 3$`
   in LaTeX. This is a tex-conversion convention only; the verb
   chain `will supply ... conditional on ... and on ...` is
   verbatim and must NOT be edited at paste-time.)

4. Cite this bridge session in P-009's acknowledgements / provenance
   block as the caveat-finalisation source:

   ```
   siarc-relay-bridge / sessions / 2026-05-06 / P009-M8B-CAVEAT-FINAL /
   ```

---

## Why branch (b) and not (a)

`tex\submitted\` listing as of 2026-05-06 contains no file matching
`p009_*.tex`. The closest analogues — `pcf2_program_statement.tex`,
`p12_journal_main.tex`, `vquad_resurgence_R1/R2.tex` — are unrelated
manuscripts (PCF-2 program statement, P12, V_quad resurgence). P-009
"AI Discovery / methodology paper" is **on the synth queue but not
yet drafted** (per CMB.txt SYNTH-TRACK 2026-05-05 ~19:35 JST: "P-009
M8b positioning ... provisional caveat ready").

Per the relay 050 STEP 1 spec, this is exactly the branch-(b) case:
"P-009 not yet drafted — the caveat is pinned in
`tex/submitted/control center/p009_caveat_pinned.txt` for future
paste."

---

## Out-of-scope items (do NOT do as part of this dispatch)

- Do **not** create a placeholder `p009_*.tex` file. The caveat is
  paste-ready; the tex skeleton is a separate Synth-altitude task.
- Do **not** push the pinned `p009_caveat_pinned.txt` to any public
  repo. It lives in the local workspace control center only; the
  bridge session push is the audit-trail copy.
- Do **not** edit the verb chain. `will supply ... conditional on the
  M8b dispatch landing within the relevant binding window and on the
  binding-window result` is the verb-checked v1 form. Editing it
  re-opens HALT_050_VERB_CHECK_FAIL exposure.
