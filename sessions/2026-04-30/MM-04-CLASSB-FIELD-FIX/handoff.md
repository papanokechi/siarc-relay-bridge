# MM-04-CLASSB-FIELD-FIX — Verdict: **CLEAN** ✅

Both fixes applied, both PDFs rebuilt clean, mini-rerun passes. UMB ↔ T2B are now coherent on the Class B field claim.

## Step 1 — UMB main.tex (MM-04 patch)

Single OLD/NEW substitution at lines 253–256 (formerly 253–254):

```diff
-  \item Class B ($\rho = +1/4$): limits lie in
-        $\mathbb{Q}\cdot\pi^{-1}$ (T2B Theorem~3 + Cor.~classB-pi).
+  \item Class B ($\rho = +1/4$): limits lie in
+        $\mathbb{Q}(\pi)$ (T2B Theorem~3); the Pure-regime
+        subclass satisfies the stronger $\mathbb{Q}\cdot\pi^{-1}$
+        (T2B Cor.~classB-pi).
```

## Step 2 — T2B Cor. classB-pi title

Single OLD/NEW substitution at line 238:

```diff
-\begin{corollary}[Pure-regime Class B is in $\mathbb{Q}(\pi)$]\label{cor:classB-pi}
+\begin{corollary}[Pure-regime Class B limits lie in $\mathbb{Q}\cdot\pi^{-1}$]\label{cor:classB-pi}
```

Title now matches body (line 239) which already said $\mathbb{Q}\cdot\pi^{-1}$.

## Step 3 — Rebuild + grep verification

| File | tex sha (head) | pdf size | pdf sha (head) | build |
|---|---|---|---|---|
| `umbrella_program_paper/main.tex` | 3B8DA616 | 287,047 B | DB1F2560 | clean (no `!`/Error/Fatal) |
| `t2b_paper_draft_v5_withauthor.tex` | CB7A9DCF | 326,377 B | AE6ED078 | clean (no `!`/Error/Fatal) |

Grep checks:

| Check | Result |
|---|---|
| `\mathbb{Q}\cdot\pi^{-1}` in UMB | **1 hit** at line 255 — inside Pure-regime subclass clause only ✅ (universal claim eliminated) |
| Cor. classB-pi title (T2B line 238) | now `\mathbb{Q}\cdot\pi^{-1}` ✅ |
| Cor. classB-pi body (T2B line 239) | already `\mathbb{Q}\cdot\pi^{-1}` ✅ (no change needed) |
| Title and body consistent | ✅ |

## Step 4 — P-10 mini-rerun (scoped to Class B field claim)

UMB main.tex lines 253–256 now read:
```
\item Class B ($\rho = +1/4$): limits lie in
      $\mathbb{Q}(\pi)$ (T2B Theorem~3); the Pure-regime
      subclass satisfies the stronger $\mathbb{Q}\cdot\pi^{-1}$
      (T2B Cor.~classB-pi).
```

Cross-paper consistency:

- **Universal Class B claim** ($\mathbb{Q}(\pi)$): UMB ↔ T2B abstract line 36, T2B `thm:classB-stieltjes` line 219, T2B summary table line 272. ✅ MATCH
- **Pure-regime stronger claim** ($\mathbb{Q}\cdot\pi^{-1}$): UMB ↔ T2B Cor. classB-pi (now both title and body). ✅ MATCH
- **No assertion contradicted by T2B's $-4/(\pi-2)$ example** (T2B line 260): the mixed Class B family with limit $-4/(\pi-2)$ now lives inside $\mathbb{Q}(\pi)$ (the universal claim), not inside $\mathbb{Q}\cdot\pi^{-1}$. ✅ CONSISTENT

T1-NEW-MM03-CLASSB-FIELD is **resolved**.

## Status of all UMB↔T2B coherence items

| Item | Origin | Status |
|---|---|---|
| MM-01 (P06 line 314 (2,2)→(2,1)) | P-10 audit | ✅ APPLIED (MM-PATCH-APPLY) |
| MM-02 (#14 Tier→Obstruction Tier rename + UMB translation remark) | P-10 audit | ✅ APPLIED (MM-PATCH-APPLY) |
| MM-03 (UMB conj:t2b two-class form) | P-10 audit | ✅ APPLIED (MM-PATCH-APPLY) |
| Abstract line 51 update (consistency w/ MM-03) | discovered during MM-PATCH-APPLY | ✅ APPLIED (MM-PATCH-APPLY) |
| T1-NEW-MM03-CLASSB-FIELD (UMB Class B field overstatement) | P10-RERUN-POSTPATCH | ✅ APPLIED (this task) |
| OBS-T2B-INTERNAL-INCONSISTENCY (Cor. classB-pi title/body) | P10-RERUN-POSTPATCH | ✅ APPLIED (this task) |

All P-10 cross-paper mismatches between UMB and T2B (and MM patches' regressions) are now resolved.

## Bridge

Files in this commit:
- `handoff.md` (this file)
- `claims.jsonl` (8 entries)
- `halt_log.json` (empty; verdict CLEAN)
- `discrepancy_log.json` (empty)
- `unexpected_finds.json` (empty)

Three commits pushed together per the relay directive:
1. `MM-PATCH-APPLY -- MM-01/02/03 applied, P06+#14+UMB patched, verification clean`
2. `P10-RERUN-POSTPATCH -- coherence verdict: NEW (1 T1 in UMB conj:t2b Class B field claim)`
3. `MM-04-CLASSB-FIELD-FIX -- Class B field claim corrected in UMB + T2B Cor title fixed; UMB↔T2B coherent`

The three commits form the audit trail: patch → discover regression → fix regression → coherent.
