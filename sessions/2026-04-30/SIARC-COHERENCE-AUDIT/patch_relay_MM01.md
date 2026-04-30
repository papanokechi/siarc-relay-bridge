# Relay patch prompt — MM-01 (P06 degree-profile regression)
**Source audit:** `sessions/2026-04-30/SIARC-COHERENCE-AUDIT/`

```
╔══════════════════════════════════════════════════════════════════╗
║  SIARC RELAY — P06-DEGREE-PROFILE-PATCH                         ║
║  Goal: fix the (2,2) → (2,1) regression in P06's positive       ║
║         control description, without altering numerical claims. ║
╚══════════════════════════════════════════════════════════════════╝

CONTEXT
  Coherence audit P-10 (2026-04-30) found that P06 cites the
  P11 Trans-stratum families as "degree profile (2,2)", whereas
  P11 itself proves they are degree-(2,1) (Proposition `prop:deg21`).
  UMB §1.1 and T2B `def:trans-stratum` already use (2,1).

FILES
  tex/submitted/p06_desert_ijnt_submission/pcf_desert_negative_result.tex
  (read-only baseline; sha12=1c5616e09589 as of audit)

STEPS
  1. Edit line 314 only:
       OLD: "the $24$ Trans-stratum families of the
             $\mathcal{F}(2,4)$ base case~\cite{P11}, which lie at
             degree profile $(2,2)$ with coefficient bound~$4$"
       NEW: "the $24$ Trans-stratum families of the
             $\mathcal{F}(2,4)$ base case~\cite{P11}, which lie at
             degree-$(2,1)$ profile (numerator quadratic, denominator
             linear; \cite[Prop.~prop:deg21]{P11}) inside the
             coefficient-bound-$4$ ambient space"
  2. Re-run pdflatex; check no warnings introduced.
  3. AEAL: append a claim to claims.jsonl with
       claim = "F(2,4) Trans-stratum has degree-(2,1) profile per
                P11 prop:deg21"
       evidence_type = "documentary",
       reproducible = true,
       script = "(none, textual fix)",
       output_hash = sha256 of new pdf.
  4. Bridge commit: "P06-DEGREE-PROFILE-PATCH -- correct (2,2)→(2,1)
       regression in positive-control paragraph"

DELIVERABLES
  - patched .tex
  - new pdf (file size + first 200-byte md5)
  - claims.jsonl entry
  - handoff.md per standing instructions

HALT IF
  - any other change to P06 is needed (out of scope)
  - the patched line still passes a (2,2) regex search (sanity check)
```
