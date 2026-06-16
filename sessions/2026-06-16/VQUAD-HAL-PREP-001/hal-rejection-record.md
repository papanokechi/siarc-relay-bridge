# HAL Rejection Record — hal-05624243v1

**Slot:** VQUAD-HAL-PREP-001 · **Authored:** 2026-06-16 · **Status:** DEFERRED (HAL
pathway closed pending credential change)

---

## ⚠️ SCOPE CORRECTION (read first)

The task brief framed this slot as documenting *"the HAL deposit attempt for
VQUAD-PERIODREP … rejected on [today's date]."* The authoritative durable record
(`submission_log.txt` §HAL, L1257–1349) contradicts two specifics of that framing.
This record uses the **sourced** facts, not the brief's assumptions:

| Brief assumption | Sourced reality (submission_log.txt) | Cite |
|---|---|---|
| hal-05624243 = the **V_quad** paper | hal-05624243v1 = the **PCF Logarithmic Ladder / 482 constants** paper (`pcf_unified_arxiv.pdf`) | L1261–1262 |
| Rejected **today** (2026-06-16) | Rejected **2026-05-21** (submitted 2026-05-16) | L1265–1267 |
| Cross-ref to V_quad Zenodo | Cross-ref to PCF-ladder Zenodo `10.5281/zenodo.19491767` | L1280 |
| Overlay = (none stated) | Overlay journal = Hardy-Ramanujan Journal (Episciences) | L1269 |

**V_quad has never been submitted to HAL.** The V_quad paper is still a working
draft ("not yet submitted") and its Zenodo deposit is itself gated behind cold-read
+ corrections. What the brief *correctly* captures is the **strategic consequence**:
the credentialing barrier that rejected hal-05624243v1 is **institutional**, so it
applies to *every* Papanokechi-pseudonym deposit — including the future V_quad one.
This slot therefore documents the HAL pathway as **deferred for the V_quad pipeline
and the broader pseudonymous program**, grounded in the actual hal-05624243v1
precedent rather than a non-existent V_quad HAL deposit. Flags: **F-PAPER-IDENTITY**,
**F-DATE** (see `ledger.json`).

---

## 1. Deposit identification (sourced: submission_log.txt L1259–1284)

| Field | Value | Cite |
|---|---|---|
| HAL deposit ID | `hal-05624243v1` (assigned at submit) | L1259 |
| HAL URL | https://hal.science/hal-05624243 | L1260 |
| Filename | `pcf_unified_arxiv.pdf` | L1261 |
| Title | *Polynomial Continued Fractions: a Proved Logarithmic Ladder, a 4/π Casoratian Identity, and 482 Irrational Constants* | L1262 |
| Author | Papanokechi (idHAL `papanokechi`; ORCID 0009-0000-6192-8273; HAL mononym workaround renders "Papanokechi Papanokechi") | L1263 |
| Affiliation (HAL form) | "Independent researcher, Yokohama, Japan" | L1264 |
| Deposited on | 2026-05-16T22:35:55+09:00 JST (operator clicked *Soumettre*) | L1265 |
| License | CC BY 4.0 | L1273 |
| MSC (HAL field) | 11J70 (primary), 11Y60, 33C20 | L1275 |
| Domain | math.NT primary + math.GM secondary | L1276 |
| Zenodo cross-ref | `10.5281/zenodo.19491767` (concept DOI; relation IsVersionOf) | L1280 |
| Overlay journal | Hardy-Ramanujan Journal (Episciences route) | L1269 |

## 2. Rejection (sourced: submission_log.txt L1266–1267, L1283–1284)

- **Submission date:** 2026-05-16 22:35 JST (L1265).
- **Rejection date:** **2026-05-21** (L1266–1267). Moderation latency ~3 business
  days / 5 calendar days (L1268).
- **Status transition:** `Awaiting moderation` → `REJECTED (credentialing, not
  scientific) 2026-05-21` (L1284).
- **Basis — explicitly non-scientific.** Per the HAL/CCSD letter the scientific
  quality was *"not in question"*; the decision cited an **institutional
  credentialing gate** (L1266, L1283).

## 3. HAL acceptance criterion (sourced: L1266, L1283, L1295–1296)

HAL/CCSD requires the depositor to satisfy **at least one** of:

  (a) **PhD program enrollment**, OR
  (b) **PhD degree** from an internationally recognized institution, OR
  (c) a **substantial list of publications** in internationally recognized
      peer-reviewed journals.

**Additional criterion (brief Stage 1.1, standard HAL practice; not separately
quoted in the log excerpt):** the submission must align with the author's documented
field of research / academic expertise as evidenced by academic background or prior
publications.

The Papanokechi pseudonymous identity meets **none** of (a)–(c) at present.

## 4. Reconsideration pathway (sourced: L1321–1324, L1348–1349; address per brief)

- **Trigger condition (sourced):** ≥ 1 peer-reviewed journal acceptance from the
  active queue satisfies prong (c); after that, a HAL reconsideration request is
  appropriate (L1322–1324). Tracked as task **T41** (L1348–1349). The brief's
  "2–3 peer-reviewed publications" is a more conservative reading of the same prong;
  the sourced threshold is ≥ 1.
- **Contact (brief Stage 1.1):** `hal.support@ccsd.cnrs.fr` with proof of status.
  CCSD (Centre pour la Communication Scientifique Directe, CNRS) operates HAL.
- **Supporting document:** the HAL rejection email is **preserved by the operator**
  for a future appeal (L1321, L1349).

**Verbatim email text is NOT reproduced here.** The full rejection email is held by
the operator outside the bridge; only the institutional summary above is in the
durable record (`submission_log.txt`). Per AEAL discipline the verbatim wording is
not reconstructed (no fabrication). No HAL-support staff name appears in the
accessible record, so no anonymization is required; the institutional identifier is
**HAL / CCSD (CNRS)**.

## 5. Public-docs-vs-practice gap (operational knowledge worth preserving)

HAL's public-facing documentation reads as broadly open to any researcher and does
**not** prominently surface a PhD-or-publication credentialing gate; the actual
moderation practice applies that gate at review time (the rejection here was
purely on credentials, with scientific quality explicitly *"not in question"*,
L1266/L1283). Future preprint-pathway inquiries for the pseudonym should treat HAL
as **credential-gated regardless of the open tone of its public docs**. The related
second-order finding from this deposit — that HAL's DataCite relation vocabulary is
a 15-relation subset of the ~35-relation full schema (missing `IsNewVersionOf`
etc., L1284) — is preserved in `HAL_RISK_REGISTER_v1.md` (operator-side) and is
orthogonal to the credentialing barrier.

## 6. AEAL classification (sourced: L1283–1284, L1317–1320)

Institutional **access-constraint** event: structural, not epistemic; outcome
externally imposed; **no** Searcher's-Fatigue pattern; **no** fabrication pattern.
AEAL claim `deposit-hal-001-rejected-credentialing` appended to the operator-side
`claims.jsonl`; predecessor `deposit-hal-001-pcf-log-ladder` transitioned
verified=null → verified=false with failure-mode = credentialing/identity gate (not
scientific, not fabrication).
