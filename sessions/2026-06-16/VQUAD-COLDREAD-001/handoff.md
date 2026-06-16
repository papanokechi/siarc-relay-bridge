# VQUAD-COLDREAD-001 — Handoff

## What this slot is
The cold read of the V_quad period-representation paper, with an editorial **Verdict A** and a
prioritized **corrections list**. This is the gating step that unblocks the deposit chain. It is an
editorial assessment, not a research execution and not a deposit.

## Verdict (one line)
**A — publication-ready pending corrections** (1 HIGH, 4 MED, 5 LOW; no substantive revision, no
showstopper). The paper is strong: careful, exactly sourced, honestly doubly-conditional on
transcendence, and it directly applies the EBR-III/AAECC Item-40 CAS-section lesson.

## The corrections, at a glance (full text in `corrections-list.md`)
- **H-1 [HIGH]** Add a provenance remark: `C = 0.43770528…` is numerically the *retracted v1.0
  Stokes-constant value*; the paper is correct (C ≠ S; bridge `C/S = |Γ(β)|/2π = 0.95588`) but must
  say so. Turns a credibility landmine into a showcase of the paper's core contribution.
- **M-1/M-2 [MED]** Fix the "Stokes multiplier = C" wording at L804 (it collides with `|S_mult| = S`
  in §5.3); reserve "Stokes constant/multiplier" for `S = 2πK`, "connection coefficient" for `C`.
- **M-3 [MED]** Add topological-recursion / Marchal SOTA citations (the one Lecerf-3 gap):
  Marchal–Alameddine 2024 CMP `10.1007/s00220-024-05187-0`, Iwaki–Marchal–Saenz 2018 JGP
  `10.1016/j.geomphys.2017.10.009`, Marchal–Orantin 2020 JMP `10.1063/5.0002260` + one §7 sentence.
  **Verify these DOIs against the operator's Marchal confirmation before insertion (Trap 6).**
- **M-4 [MED]** Fill the Sakai concept-DOI placeholder (bibitem{Sakai}, L1254) from the
  authoritative `related_identifiers.md` at submission time.
- **L-1…L-5 [LOW]** Optional sibling-deposit cross-refs (EBR-Ib/II, δ-Fredholm — DOIs from file,
  not memory); tighten eq:periodmatrix phrasing; one-clause abstract polish; update `\thanks`;
  precise cite for the `(1/2)^n` floor remark.

## Operator next steps
1. **Review `coldread-verdict.md` and `corrections-list.md`.** Accept/adjust the verdict and the
   item priorities (especially whether H-1 is HIGH for your venue plan).
2. **Open `VQUAD-PAPER-CORRECTIONS-001`** with `corrections-list.md` as its scope. Work H-1, M-1…M-4
   at minimum; LOW items at discretion. Re-verify all inserted DOIs from authoritative files.
3. After corrections land → **`VQUAD-REPRO-BUNDLE-002`** (corrections-final paper + bundle), then
   **re-run `VQUAD-ZENODO-READY-001`** to re-pin the PDF SHA-256 and the metadata anchor against the
   corrected paper, then **`VQUAD-ZENODO-DEPOSIT-001`**.
4. This Verdict A clears the **first** of the three blocking READY-001 Stage-1 prerequisites;
   CORRECTIONS-001 and BUNDLE-002 are still ABSENT, so READY-001 stays correctly HALTED until they
   exist.

## Re-entry chain (unchanged, now one link satisfied)
~~cold-read → Verdict A~~ ✅ →  **VQUAD-PAPER-CORRECTIONS-001** → VQUAD-REPRO-BUNDLE-002 →
[re-run] VQUAD-ZENODO-READY-001 → VQUAD-ZENODO-DEPOSIT-001.

## Standing rule / git state
Slot is **staged and HELD** — no commit, no push, no deposit. `HEAD` remains `dd1edcf`
(operator hand-commits, as with every prior V_quad slot this session). Suggested honest commit
message when the operator is ready:

> `VQUAD-COLDREAD-001 — cold read complete; Verdict A (publication-ready pending 1 HIGH/4 MED/5 LOW corrections); corrections list scopes VQUAD-PAPER-CORRECTIONS-001`

`EBR3-REVISION-001` remains a pre-existing untracked slot — leave it alone. Prior committed slots
(REPRO-BUNDLE-001, ZENODO-PREP-001, HAL-PREP-001) untouched.
