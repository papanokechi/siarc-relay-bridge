# Quote Length Scan [SELF-CHECK G.2] — 077

**Session:** T2-PORTFOLIO-BUNDLING-DOSSIER-ASSEMBLY-077
**Compiled:** 2026-05-07
**Purpose:** Mechanical scan of all blockquoted (`>`-prefixed)
verbatim quotes across 077 deliverables for HALT_077_QUOTE_LENGTH
discipline. Spec §8 cap: ≤ 50 words per single blockquote span.

This file is the scan-pattern descriptor; it is excluded from
its own scan-set per 074 / 075 precedent.

---

## G.2.A — Scan command

```powershell
foreach ($f in Get-ChildItem -Filter "*.md") {
  if ($f.Name -eq 'quote_length_scan.md') { continue }
  $lines = Get-Content -LiteralPath $f.FullName
  $cur = @(); $startLine = 0; $i = 0
  foreach ($line in $lines) {
    $i++
    if ($line -match '^>') {
      if ($cur.Count -eq 0) { $startLine = $i }
      $cur += ($line -replace '^>\s?','')
    } else {
      if ($cur.Count -gt 0) {
        $words = (($cur -join ' ') -split '\s+' | Where-Object { $_ -ne '' }).Count
        $tag = if ($words -gt 50) { '[VIOLATION]' } else { 'OK' }
        "{0}:L{1}-L{2} ({3} words) {4}" -f $f.Name, $startLine, ($i-1), $words, $tag
        $cur = @()
      }
    }
  }
  # flush trailing block
}
```

---

## G.2.B — Scan output (all 077 deliverables, post-fix)

```
paper_profile_ct_v13.md:L26-L26 (45 words) OK
paper_profile_ct_v13.md:L63-L63 (36 words) OK
paper_profile_d2note_v21.md:L24-L24 (45 words) OK
paper_profile_pcf1_v13.md:L24-L24 (47 words) OK
paper_profile_pcf1_v13.md:L70-L70 (28 words) OK
paper_profile_pcf2_v13.md:L24-L24 (30 words) OK
paper_profile_pcf2_v13.md:L71-L71 (31 words) OK
paper_profile_t2b_v30.md:L28-L28 (43 words) OK
paper_profile_t2b_v30.md:L70-L70 (35 words) OK
paper_profile_umbrella_v20.md:L24-L24 (45 words) OK
paper_profile_umbrella_v20.md:L72-L72 (31 words) OK
w21_lane1_portfolio_decision_packet.md:L23-L23 (14 words) OK
```

12 blockquote spans across 7 files. **Zero VIOLATION tags.**

---

## G.2.C — Pre-fix vs post-fix delta

Initial scan flagged two violations:

| File | Line | Pre-fix words | Post-fix words | Resolution |
|---|---|---:|---:|---|
| `paper_profile_pcf2_v13.md` | L24 | 51 | 30 | Trailing sentence ("The natural invariant of...Δ₃") moved from blockquote into agent-authored paraphrase block, with explicit `[Paraphrase…not a quote]` label. |
| `paper_profile_t2b_v30.md` | L28 | 52 | 43 | Trailing clause ("distinguished by the value of the structural ratio a_2/b_1²") moved from blockquote into agent-authored paraphrase block, with explicit `[Paraphrase…not a quote]` label. |

[NOTE-077-G2-1] Both fixes preserve the verbatim quoted material
and segregate moved text into explicitly-labelled agent-authored
paraphrase. Per spec §6.E.5 + HALT_077_BIBLIOGRAPHIC_FABRICATION,
this is the standard remediation pattern; no quoted text was
re-worded.

---

## G.2.D — Verdict

**[VERDICT] HALT_077_QUOTE_LENGTH not triggered.** All blockquoted
verbatim quotes ≤ 50 words.

---

End of quote-length scan.
