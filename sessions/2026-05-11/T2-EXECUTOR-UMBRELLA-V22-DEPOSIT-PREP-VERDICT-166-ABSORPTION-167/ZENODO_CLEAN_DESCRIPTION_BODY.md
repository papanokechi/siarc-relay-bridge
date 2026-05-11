# Zenodo-Clean Description Body — Umbrella v2.2 (slot 167 addendum)

**Date**: 2026-05-11 09:15 JST
**Parent slot**: 167 (bridge SHA `3f0377a`)
**Trigger**: operator description-block review request
**Status**: paste-ready (Zenodo TinyMCE HTML + plain-prose mirror)

This addendum supersedes the §2 / §2.1 / §2.5 raw-LaTeX content in `amended_description_block_v2.md` for the **Description body paste**. The LaTeX original remains the authoritative version in the slot 162 parent and the slot 167 baseline; this addendum flattens LaTeX commands (`\ref{}`, `$...$` math mode) that Zenodo's TinyMCE does not render, and strips bridge-internal heading labels.

---

## Part A — Plain-prose mirror (paste into Zenodo "Description" field if using plain-text mode)

### Version difference (short form)

> v2.2 (May 2026): Consolidates full M-axis V0 closure series (M4, M7, M8a, M8b) and M6.CC R1; supersedes v2.1 internal staging.

### Expanded variant

The v2.2 revision of the SIARC umbrella program statement extends the v2.0 §Closure Cascade and Bridge Provenance section from 3 milestones to 6 milestones, adding the M-axis V0 ratification cascade triple landed 2026-05-09: M7 V0 (cubic/quartic borderline-anormal A residual; soft-branch ratification at MEDIUM-HIGH; bridge SHA 7f93b9e; SOFT-BRANCH, HARD-BRANCH-PENDING), M8a V0 (catalogue-wide Painlevé-test stratum labeling via the Conte–Musette necessary criterion; 60/60 LABELED uniformly; bridge SHA cb429e1; ALG-TEST-SCALE, STOKES-DICHOTOMY-DELEGATED-TO-M8B), and M8b V0 (numerical foreclosure of the laptop-feasible |S₂| extraction at d=2; cross-provider dual-witness; bridge SHA 74c5630; NUMERICAL-FORECLOSURE, d≥3 caveat carried forward). The v2.0 → v2.2 version sequence skips v2.1 (internal staging only at bridge 883dddf, 2026-05-09) per the operative cascade-132 (fd669d3) PATH_B decision. All mathematical content, conjectures, open problems, and the §Cross-Degree Triple are unchanged from v2.0; v2.2 is a status/provenance addendum, not a content revision.

### §2.1 Deposit-time companion-artefact snapshot

> Companion artefact state at deposit time (2026-05-11 JST): PCF-2 v1.4 (10.5281/zenodo.20114315, deposited 2026-05-11; cascade-132 Option α Step 1 landed), Channel Theory v1.3 (10.5281/zenodo.19972394, deposited 2026-05-02), T2B v3.0 (10.5281/zenodo.19915689, deposited 2026-04-30), PCF-1 v1.3 (10.5281/zenodo.19937196, deposited 2026-05-01). Picture-chain v1.20+ deposit pending (substrate-prep at bridge b9aa881 2026-05-09; concept-DOI not yet minted); cross-link rows to be spliced via post-publish Zenodo Edit upon picture-chain concept-DOI mint (separate work-stream; cascade-132 Option α Step 3).

### §2.5 M1–M12 program-axis coverage (snapshot at Umbrella v2.2 deposit time)

| Axis  | Status                                  | Primary substrate                                                    |
|-------|-----------------------------------------|----------------------------------------------------------------------|
| M1    | external                                | D2-NOTE concept 10.5281/zenodo.19996689                              |
| M2    | tabled (RULE 1)                         | —                                                                    |
| M3    | tabled (RULE 1)                         | —                                                                    |
| M4    | closed (V0; folded)                     | bridge cascade 5f9db69 (cascade 106)                                 |
| M5    | tabled (RULE 1)                         | —                                                                    |
| M6.CC | closed (retired into Channel Theory)    | Channel Theory concept 10.5281/zenodo.19941678                       |
| M7    | closed (V0; folded)                     | bridge cascade 7f93b9e (cascade 123)                                 |
| M8a   | closed (V0; folded)                     | bridge cascade cb429e1 (cascade 127R)                                |
| M8b   | closed (V0; folded)                     | bridge cascade 74c5630 (cascade 130R; d≥3 caveat carried forward to Umbrella v2.3) |
| M9    | partial                                 | bridge cascade b9aa881 (slot 136 picture v1.20+)                     |
| M10   | partial                                 | Lean sorry discharge work-stream                                     |
| M11   | tabled (RULE 1)                         | —                                                                    |
| M12   | tabled (RULE 1)                         | —                                                                    |

The axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (siarc-relay-bridge cascade 012736f); status vocabulary and atomic listing are normative. Bridge cascade SHAs are content-addressed persistent identifiers; URLs may decay if the siarc-relay-bridge repository is renamed but SHAs remain recoverable from any clone.

Per-deposit semantics: Umbrella v2.2 absorbs the V0-closure cascade via the v2.2 §Closure Cascade and Bridge Provenance amendment. The 4 V0-closed axes (M4, M7, M8a, M8b) and the M6.CC retirement are program-tier provenance for the Umbrella program statement, not new mathematical content; this is the semantic distinction between Umbrella v2.2 (provenance-tier amendment) and Umbrella v2.3 (forthcoming; mathematical content amendment).

---

## Part B — HTML-ready mirror (paste into Zenodo TinyMCE editor in HTML / source-view mode)

### Version difference (short form)

```html
<p><strong>v2.2 (May 2026):</strong> Consolidates full M-axis V0 closure series (M4, M7, M8a, M8b) and M6.CC R1; supersedes v2.1 internal staging.</p>
```

### Expanded variant

```html
<p>The v2.2 revision of the SIARC umbrella program statement extends the v2.0 §Closure Cascade and Bridge Provenance section from 3 milestones to 6 milestones, adding the M-axis V0 ratification cascade triple landed 2026-05-09: <strong>M7 V0</strong> (cubic/quartic borderline-anormal <em>A</em> residual; soft-branch ratification at MEDIUM-HIGH; bridge SHA <code>7f93b9e</code>; SOFT-BRANCH, HARD-BRANCH-PENDING), <strong>M8a V0</strong> (catalogue-wide Painlev&eacute;-test stratum labeling via the Conte&ndash;Musette necessary criterion; 60/60 LABELED uniformly; bridge SHA <code>cb429e1</code>; ALG-TEST-SCALE, STOKES-DICHOTOMY-DELEGATED-TO-M8B), and <strong>M8b V0</strong> (numerical foreclosure of the laptop-feasible |<em>S</em><sub>2</sub>| extraction at <em>d</em>=2; cross-provider dual-witness; bridge SHA <code>74c5630</code>; NUMERICAL-FORECLOSURE, <em>d</em>&ge;3 caveat carried forward). The v2.0 &rarr; v2.2 version sequence skips v2.1 (internal staging only at bridge <code>883dddf</code>, 2026-05-09) per the operative cascade-132 (<code>fd669d3</code>) PATH_B decision. All mathematical content, conjectures, open problems, and the &sect;Cross-Degree Triple are unchanged from v2.0; v2.2 is a status/provenance addendum, not a content revision.</p>
```

### §2.1 Deposit-time companion-artefact snapshot

```html
<h3>&sect;2.1 Deposit-time companion-artefact snapshot</h3>
<blockquote>
  <p><strong>Companion artefact state at deposit time (2026-05-11 JST):</strong> PCF-2 v1.4 (<code>10.5281/zenodo.20114315</code>, deposited 2026-05-11; cascade-132 Option &alpha; Step 1 landed), Channel Theory v1.3 (<code>10.5281/zenodo.19972394</code>, deposited 2026-05-02), T2B v3.0 (<code>10.5281/zenodo.19915689</code>, deposited 2026-04-30), PCF-1 v1.3 (<code>10.5281/zenodo.19937196</code>, deposited 2026-05-01). Picture-chain v1.20+ deposit pending (substrate-prep at bridge <code>b9aa881</code> 2026-05-09; concept-DOI not yet minted); cross-link rows to be spliced via post-publish Zenodo Edit upon picture-chain concept-DOI mint (separate work-stream; cascade-132 Option &alpha; Step 3).</p>
</blockquote>
```

### §2.5 M1–M12 program-axis coverage

```html
<h3>&sect;2.5 M1&ndash;M12 program-axis coverage (snapshot at Umbrella v2.2 deposit time)</h3>
<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr><th>Axis</th><th>Status</th><th>Primary substrate</th></tr>
  </thead>
  <tbody>
    <tr><td>M1</td><td>external</td><td>D2-NOTE concept <code>10.5281/zenodo.19996689</code></td></tr>
    <tr><td>M2</td><td>tabled (RULE 1)</td><td>&mdash;</td></tr>
    <tr><td>M3</td><td>tabled (RULE 1)</td><td>&mdash;</td></tr>
    <tr><td>M4</td><td>closed (V0; folded)</td><td>bridge cascade <code>5f9db69</code> (cascade 106)</td></tr>
    <tr><td>M5</td><td>tabled (RULE 1)</td><td>&mdash;</td></tr>
    <tr><td>M6.CC</td><td>closed (retired into Channel Theory)</td><td>Channel Theory concept <code>10.5281/zenodo.19941678</code></td></tr>
    <tr><td>M7</td><td>closed (V0; folded)</td><td>bridge cascade <code>7f93b9e</code> (cascade 123)</td></tr>
    <tr><td>M8a</td><td>closed (V0; folded)</td><td>bridge cascade <code>cb429e1</code> (cascade 127R)</td></tr>
    <tr><td>M8b</td><td>closed (V0; folded)</td><td>bridge cascade <code>74c5630</code> (cascade 130R; <em>d</em>&ge;3 caveat carried forward to Umbrella v2.3)</td></tr>
    <tr><td>M9</td><td>partial</td><td>bridge cascade <code>b9aa881</code> (slot 136 picture v1.20+)</td></tr>
    <tr><td>M10</td><td>partial</td><td>Lean sorry discharge work-stream</td></tr>
    <tr><td>M11</td><td>tabled (RULE 1)</td><td>&mdash;</td></tr>
    <tr><td>M12</td><td>tabled (RULE 1)</td><td>&mdash;</td></tr>
  </tbody>
</table>
<p>The axis-coverage table follows the SIARC v1 schema locked by slot 160 verdict (siarc-relay-bridge cascade <code>012736f</code>); status vocabulary and atomic listing are normative. Bridge cascade SHAs are content-addressed persistent identifiers; URLs may decay if the <code>siarc-relay-bridge</code> repository is renamed but SHAs remain recoverable from any clone.</p>
<p><strong>Per-deposit semantics:</strong> Umbrella v2.2 absorbs the V0-closure cascade via the v2.2 &sect;Closure Cascade and Bridge Provenance amendment. The 4 V0-closed axes (M4, M7, M8a, M8b) and the M6.CC retirement are program-tier provenance for the Umbrella program statement, not new mathematical content; this is the semantic distinction between Umbrella v2.2 (provenance-tier amendment) and Umbrella v2.3 (forthcoming; mathematical content amendment).</p>
```

---

## Part C — Diff log (what changed vs slot 167 `amended_description_block_v2.md`)

| # | Location | Original (LaTeX/bridge-internal) | Zenodo-clean replacement | Rationale |
|---|---|---|---|---|
| 1 | §2 expanded variant | `§\ref{sec:closure-cascade}` | `§Closure Cascade and Bridge Provenance section` | LaTeX `\ref` does not render in TinyMCE |
| 2 | §2 expanded variant | `§\ref{sec:triple}` | `§Cross-Degree Triple` | Same as #1 |
| 3 | §2 expanded variant | `$A$` | `<em>A</em>` (HTML) / `A` (plain) | Math mode does not render |
| 4 | §2 expanded variant | `$|S_2|$` | `\|<em>S</em><sub>2</sub>\|` (HTML) / `|S₂|` (plain) | Math mode + Unicode subscript |
| 5 | §2 expanded variant | `$d=2$` | `<em>d</em>=2` (HTML) / `d=2` (plain) | Math mode does not render |
| 6 | §2 expanded variant | `$d≥3$` | `<em>d</em>≥3` (HTML) / `d≥3` (plain) | Math mode does not render |
| 7 | §2.1 heading | `### §2.1 Deposit-time companion-artefact snapshot (verdict-166-γ2 footnote)` | `<h3>§2.1 Deposit-time companion-artefact snapshot</h3>` | Strip bridge-internal substrate label `(verdict-166-γ2 footnote)` |
| 8 | §2.5 M8b row | `d≥3 caveat in Umbrella v2.3 Appendix C iii` | `d≥3 caveat carried forward to Umbrella v2.3` | Forward-reference to specific Appendix section that does not exist yet; soften to neutral "carried forward to v2.3" |
| 9 | §2.5 M10 row | `Lean sorry discharge work-stream; SAFE phrasing in Umbrella v2.3 Appendix C ii` | `Lean sorry discharge work-stream` | Strip forward-reference to non-existent v2.3 Appendix section |
| 10 | §2.5 per-deposit semantics last paragraph | `cf. §2 "Expanded variant" above` | (removed) | Reads awkwardly in Zenodo flat-doc context |
| 11 | §2.5 per-deposit semantics last paragraph | `Umbrella v2.3 (mathematical content amendment, F6-blocked on D-156-1)` | `Umbrella v2.3 (forthcoming; mathematical content amendment)` | Strip bridge-internal anomaly ID `D-156-1` |

**Unchanged**: all 4 companion-deposit dates (verified live 2026-05-11); all axis-coverage row content except as noted; all bridge SHAs; concept-DOI vs version-DOI assignments; RULE 1 + cascade-132 references retained as machine-resolvable substrate.

---

## Operator paste workflow

Recommended order for Zenodo description body:

1. **§2 expanded variant** (Part B paragraph 2; or Part A plain prose if TinyMCE source-view is awkward)
2. **§2.1 deposit-time companion-artefact snapshot** (Part B blockquote)
3. **§2.5 axis-coverage table + per-deposit semantics** (Part B table + two paragraphs)

Short form §2 ("v2.2 (May 2026): Consolidates ...") goes into the "Version notes" / "What's new" field if Zenodo presents one separately from the main description. If Zenodo presents only a single description field, prepend the short form as the first paragraph.

---

**End of `ZENODO_CLEAN_DESCRIPTION_BODY.md`.**
