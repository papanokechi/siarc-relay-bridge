# Phase C.3 — Aggregate Literature Verdict

**Dispatch 3 timestamp:** 2026-05-03 (re-fire 3)
**Verdict signal:** `C_LITERATURE_BLOCKED_AT_C1`

## Per-source results

| Source           | Phase    | Result                          | d-range / status                                  |
|------------------|----------|---------------------------------|---------------------------------------------------|
| Wasow 1965 §X.3  | C.1      | HALT (PDF image-only, no text)  | d_W* — undetermined; cannot read theorems         |
| Birkhoff 1930 §2 | C.2 (i)  | PASS, uniform                   | d_B*(formal-existence) = ∞                        |
| Birkhoff 1930 §3 | C.2      | PASS (converse, uniform)        | d_B*(converse) = ∞                                |
| (Borel-singular  | C.2 (ii) | NOT IN §§2-3                    | content lives in B–T 1933 / Wasow X.3, both       |
|  radius claim)   |          |                                 | unread per C.1 / not yet acquired                 |

## Aggregate proof d-range

Per Prompt 018 §2 step 6:
proof's d-range = min(d_W*, d_B*, ∞ if both UNIFORM).

- d_B*(formal existence) = ∞ ✓ (Birkhoff 1930 §2)
- d_W* = **unknown** (Wasow §X.3 unreadable)
- The Borel-singularity radius theorem — needed to identify
  ξ = 1/c with the Phase A* `xi_0 = d / β_d^{1/d}` value — is
  **not in Birkhoff 1930 §§2-3** and has not been verified from
  any landed source.

The minimum over `{∞, undetermined, undetermined}` is
**undetermined**. Phase C.3 cannot output a finite or "uniform"
d-range for the full Q20a proof template at this dispatch.

## Verdict

`C_LITERATURE_BLOCKED_AT_C1` (new code, distinct from
Prompt 018 §2 step 6 ladder).

This differs from `HALT_Q20A_LITERATURE_NOT_LANDED` (Phase C.0
halt of dispatches 1/2): the literature **is** landed. It
differs from `C_LITERATURE_BOUNDED_AT_d*`: no finite d* has
been established. It differs from `C_LITERATURE_UNIFORM`: only
the formal half (Birkhoff §§2-3 (i)) is uniform; the Borel
half is unverified.

## What is now closed and what remains open

**Closed (this dispatch):**
- Phase A* sanity sweep d ∈ {2..10}, all PASS, no regression
  (carry-forward from dispatches 1/2; SHA-cache verified).
- Phase C.0 gate hash check (4/4 PDFs match SHA256SUMS.txt).
- Phase C.2 (i) — Birkhoff §2 formal-series existence,
  uniform in n = d.

**Open (this dispatch):**
- Phase C.1 — Wasow §X.3 theorems (i), (ii), (iii) — blocked
  by image-only PDF.
- Phase C.2 (ii) — Borel-singularity-radius identification
  ξ = 1/c — not in Birkhoff §§2-3; needs B–T 1933 or Wasow
  X.3 (the latter via OCR / re-acquisition).

**Recommendation for downstream:**
- Synthesizer receives `UPGRADE_PARTIAL_FORMAL_ONLY` (formal
  half closes uniformly in d; analytic / Borel half blocked
  on lit). The PCF-2 v1.3 `xi_0(d) = d / β_d^{1/d}` upgrade
  cannot use this dispatch's evidence to land as a *theorem*;
  the formal direction (existence and uniqueness of
  characteristic equation at slope p/q) is theorem-grade
  citable to Birkhoff 1930 §§2-3 uniformly in d ≥ 1.
