# cover_letter.md — Zenodo deposit description body (Q7a)

## Status

**The LIVE deposit description body at 10.5281/zenodo.20114315 is well-structured and is NOT recommended for Edit.** Re-deposit or major re-write of the description would not improve archival fidelity (the 'forthcoming' temporal language for Umbrella v2.2 and Picture-chain v1.20+ is a snapshot at deposit time and is provenance-faithful — see UF-155-4 in `unexpected_finds.json`).

## Live description body — verified clean (no Edit)

The live description body for 10.5281/zenodo.20114315 includes:

1. **Opening paragraph** introducing v1.4 as a minor amendment to v1.3 recording the resolution of one forward-pointed Open Problem.
2. **Version changelog blockquote** detailing the v1.4 amendment narrative + Prompt 014 PASS_A_EQ_6_ONLY anchor + bridge SHA references.
3. **Numerical content of the closure** verbatim from M7 V0 cascade 7f93b9e (max |δ_lin| = 3.09 × 10⁻²³, dps = 25,000, N ≤ 1200, 11-parameter LIN refit, K_FIT = 7, PSLQ on 17-member deduplicated H6 basis B19+ at maxcoeff = 10⁵⁰ tolerance = 10⁻⁴⁰, no Γ(1/3) relation).
4. **Q23 PSLQ basis hygiene note** (17-member dedup vs. 18-element literal).
5. **Cascade-132 deposit-ordering note** (PCF-2 v1.4 deposited FIRST per Option α).
6. **Companion documents block** (PCF-1 v1.3, Umbrella v2.2 'forthcoming', Picture-chain v1.20+ 'forthcoming').
7. **M1-M12 program-axis coverage table** (slot 160 schema v1 compliant; status vocabulary normative; bridge cascade SHAs as content-addressed identifiers).
8. **Bridge-SHA persistence statement** (URLs may decay; SHAs remain recoverable from any clone).

## Template for FUTURE deposits (v1.5+) — structural reference

Future deposit description bodies should follow this 8-section structure. Word budget target: ~600-900 words (matches live 20114315).

```
[Opening paragraph: 1-2 sentences naming the version, the amendment scope,
 and whether v1.5 is a status update or content revision.]

Version changelog (v1.5):

> [Blockquote: detailed amendment narrative; cite Prompt N PASS_X verdict
> name; cite bridge SHA(s); preserve any (SOFT-BRANCH; HARD-BRANCH-PENDING)
> or other annotations verbatim from cascade record.]

Numerical content of the closure (inherited from M{axis} V0 cascade `{SHA}`):
[Anchor values; substrate-frozen; cite verbatim.]

[Optional: PSLQ basis hygiene note if any new PSLQ closure recorded.]

[Optional: cascade-N deposit-ordering note if cascade chain re-opens.]

Companion documents:
- [PCF-1, Umbrella, possibly CT / T2B if mathematically relevant; cite
  concept-DOIs, not version-DOIs.]

M1-M12 program-axis coverage (snapshot at v1.5 deposit time):
[Table per slot 160 schema v1; status vocabulary normative.]

[Final paragraph: SIARC schema attribution; bridge SHA persistence note.]
```

## Submission notes (NOT for Zenodo description — for the operator's records)

The PCF-2 v1.4 deposit is **cascade-132 Option α' Step 1** (Step 2 = Umbrella v2.2 LANDED 2026-05-11 at 10.5281/zenodo.20114861; Step 3 = Picture-chain v1.20+ NOT YET DEPOSITED, blocked on M10 V0 + RULE 1 lift).

The deposit-time Zenodo metadata has 3 known defects (D-PCF2-V14-1/2/3); see `zenodo_metadata.json` for the Edit-form runbook. Edit is metadata-only; no DOI bump expected per slot 167 P4 precedent.

## Journal cover letter (DIFFERENT from this; M11/M12 work-stream)

The "cover letter" referenced in slot 155 §Q7a is the **Zenodo deposit description body** (above). A separate **journal cover letter** is needed if/when the operator submits PCF-2 v1.4 to a journal (arXiv mirror → journal pipeline; M11/M12 work-stream covered in slot 154 §Q3 ACTION_LADDER). The journal cover letter is OUT OF SCOPE for this slot 155 fire; it should be drafted as a separate consultation when the journal submission target is selected.
