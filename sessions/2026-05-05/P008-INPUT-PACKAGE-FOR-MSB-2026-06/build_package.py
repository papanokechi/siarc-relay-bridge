"""Build p008_input_package_for_msb_2026-06.md by extracting verbatim
excerpts from located substrate. No editorial framing in non-quoted
sections. Uses 4-tilde fences to avoid backtick conflicts inside the
quoted markdown handoff.
"""
from __future__ import annotations
import datetime as _dt
import hashlib
import json
import os
import re
from pathlib import Path

WS = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat")
SD = WS / "siarc-relay-bridge" / "sessions" / "2026-05-05" / "P008-INPUT-PACKAGE-FOR-MSB-2026-06"
OUT = SD / "p008_input_package_for_msb_2026-06.md"

FENCE = "~~~~"

def read_lines(p: Path) -> list[str]:
    return p.read_text(encoding="utf-8", errors="replace").splitlines()

def read_range(p: Path, start: int, end: int) -> str:
    if not p.exists():
        return f"[NOT FOUND: {p}]"
    lines = read_lines(p)
    end = min(end, len(lines))
    return "\n".join(lines[start - 1:end])

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest().upper()

def utc_iso(p: Path) -> str:
    return _dt.datetime.fromtimestamp(p.stat().st_mtime, _dt.timezone.utc).isoformat()

def fence_block(lang: str, body: str) -> str:
    return f"{FENCE}{lang}\n{body}\n{FENCE}"

# Substrate paths
P_S1 = WS / "tex/submitted/umbrella_program_paper/main.tex"
P_S2 = WS / "pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex"
P_S3 = WS / "siarc-relay-bridge/sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md"
P_S4 = WS / "siarc-relay-bridge/sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_promotion.tex"
P_CMB = WS / "tex/submitted/CMB.txt"
P_CLI = WS / "cli_log/2026-05-05.md"
P_WSB = WS / "cli_log/2026-W19_wsb.md"
P_S7 = WS / "tex/submitted/control center/synthesizer_inbox/STRATEGYZER_HANDOFF_2026-05-08.md"

# Manifest
manifest_text = (SD / "p008_substrate_manifest.json").read_text(encoding="utf-8")
manifest_sha = sha256(SD / "p008_substrate_manifest.json")

# Substrate excerpts
S1_excerpt = read_range(P_S1, 212, 502)
S2_excerpt = read_range(P_S2, 1336, 1355)
S3_excerpt = P_S3.read_text(encoding="utf-8")
S4_intro = read_range(P_S4, 36, 94)
S4_thm1 = read_range(P_S4, 122, 165)
S4_thm3 = read_range(P_S4, 222, 290)
cmb_M6_block = read_range(P_CMB, 1480, 1535)
cmb_M9_caveat = read_range(P_CMB, 395, 410)
cli_M6_lines = read_range(P_CLI, 1220, 1260)
wsb_full = P_WSB.read_text(encoding="utf-8")

# S7 § E (verbatim)
S7_lines = read_lines(P_S7)
e_start = next(i for i, l in enumerate(S7_lines) if l.startswith("## E. Standing notes"))
f_start = next(i for i, l in enumerate(S7_lines) if l.startswith("## F."))
S7_excerpt = "\n".join(S7_lines[e_start:f_start])

# Grounding
cmb_mtime = utc_iso(P_CMB)
cmb_first6 = "\n".join(read_lines(P_CMB)[:6])

bridge_sessions = sorted(
    [d for d in (WS / "siarc-relay-bridge/sessions").iterdir() if d.is_dir()],
    key=lambda d: d.name,
)
now = _dt.datetime.now()
bridge_30d_lines = []
for d in bridge_sessions:
    mt = _dt.datetime.fromtimestamp(d.stat().st_mtime)
    if (now - mt).days <= 30:
        bridge_30d_lines.append(f"  - {d.name}")
bridge_30d = "\n".join(bridge_30d_lines)

cli_files = sorted(
    (WS / "cli_log").glob("*.md"),
    key=lambda p: p.stat().st_mtime,
    reverse=True,
)[:3]
cli_latest = "\n".join(f"  - {p.name}  ({utc_iso(p)})" for p in cli_files)

compiled_utc = _dt.datetime.now(_dt.timezone.utc).isoformat()

script_path = SD / "build_package.py"
script_sha = sha256(script_path)

body = f"""# P-008 Input Package for Strategyzer Monthly Cycle 2026-06

## Compiled: {compiled_utc}
## Compiler: CLI-Tactical-Executer (relay 045)
## Authority for use: Strategyzer (Tier 1, monthly cadence)

This artefact is a passive substrate. It contains verbatim excerpts
from located workspace and bridge sources. Sections § 2 - § 8 quote
sources without editorial framing.

---

## § 0  rule5 grounding evidence

**(a) CMB header (most-recent timestamp + first 6 lines):**

- mtime (UTC): {cmb_mtime}
- first 6 lines verbatim:

{fence_block("", cmb_first6)}

**(b) 30-day bridge listing (sessions modified within last 30 days):**

{bridge_30d}

**(c) Latest cli_log files (top 3 by mtime):**

{cli_latest}

Status: COMPLETE (all three sources reachable).

---

## § 1  Substrate manifest

Manifest file: p008_substrate_manifest.json (SHA-256 {manifest_sha}).
Entries verbatim:

{fence_block("json", manifest_text)}

---

## § 2  Umbrella v2.0 § "Cross-Degree Framing: the Invariant Triple"  (verbatim, L212-502)

Source: tex/submitted/umbrella_program_paper/main.tex  (S1; FOUND)

{fence_block("tex", S1_excerpt)}

---

## § 3  CT v1.3 § "Implications for the Master Conjecture" (verbatim, L1336-1355)

Source: pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex  (S2; FOUND)

{fence_block("tex", S2_excerpt)}

---

## § 4  M9 main-theorem dependency audit verdict (verbatim full handoff, commit 4ffcc8c)

Source: siarc-relay-bridge/sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md  (S3; FOUND)

{fence_block("markdown", S3_excerpt)}

---

## § 5  T2B v3.1 bipartition framing (verbatim, commit 5d83797)

Source: siarc-relay-bridge/sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_promotion.tex  (S4; FOUND)

### § 5.1  Introduction (L36-94)

{fence_block("tex", S4_intro)}

### § 5.2  Theorem 1 - the resonance family (L122-165)

{fence_block("tex", S4_thm1)}

### § 5.3  Theorem 3 - Class B Stieltjes equivalence (L222-290)

{fence_block("tex", S4_thm3)}

---

## § 6  Working main-theorem statement (status)

NO WORKING M9 / SIARC-MASTER-V0 / Phi MAIN-THEOREM STATEMENT IN
WORKSPACE OR BRIDGE CORPUS AS OF 2026-05-05.

The 2026-05-05 M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT (verdict
INDETERMINATE_NO_FORMAL_STATEMENT, full text quoted verbatim in § 4)
returned Step 1 - Statement-of-record Rule 5 (NONE) under strict
precedence. No formal theorem or conjecture environment labelled
"Master Conjecture v0", "MASTER-V0", or "Phi" exists in any of:

- tex/submitted/umbrella_program_paper/main.tex (umbrella v2.0)
- tex/submitted/pcf_unified_expmath_submission.tex (PCF-1 v1.3)
- tex/submitted/pcf2_program_statement.tex (PCF-2 v1.3)
- pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex (CT v1.3)
- sessions/2026-05-01/SIARC-MASTER-V0/handoff.md (HALTED before content)
- siarc-relay-bridge/sessions/2026-05-04/PICTURE-V18-AMENDMENT-DRAFTING/picture_v1.18.md (SCHEMA only, not a formal theorem environment per audit Rule 3)

Workspace grep over tex/submitted/**/*.tex for the patterns
thm:main | main_theorem | Main Theorem | Theorem 1.1 | theorem M9 |
theorem:M9 returned 6 hits, none of which is a Phi master statement
(full breakdown in the manifest entry for S5).

---

## § 7  M6 status (verbatim from CMB, cli_log, and W19 WSB)

Source A: tex/submitted/CMB.txt  (S6_CMB; FOUND).

### § 7.1  CMB synth-track marker block (verbatim, L1480-1535)

{fence_block("", cmb_M6_block)}

### § 7.2  CMB M9 caveat profile excerpt (verbatim, L395-410)

{fence_block("", cmb_M9_caveat)}

Source B: cli_log/2026-05-05.md  (S6_cli_log; FOUND).

### § 7.3  cli_log M6 arbitration upcoming-block (verbatim, L1220-1260)

{fence_block("", cli_M6_lines)}

Source C: cli_log/2026-W19_wsb.md  (S6_W19_wsb; FOUND, full body).

### § 7.4  W19 WSB (verbatim, full file)

{fence_block("", wsb_full)}

### § 7.5  M6 arbitration verdict status

A CLI-Synthesizer arbitration verdict for the M6 (checkmark)-vs-Phase-A/B.5
inconsistency between the 038 caveat profile and the W19 WSB has NOT been
written to cli_log/2026-05-05.md or cli_log/2026-W19_wsb.md as of the
compile timestamp recorded above (grep for "arbitration verdict" /
"M6 verdict" / "Phase A" / "Phase B.5" within those two files returns
only forward-references to the pending in-tier work; cf. cli_log L1234
verbatim: "M6 (checkmark)-vs-Phase-A/B.5 arbitration verdict - CLI in-tier;
output to cli_log + CMB; required substrate for 045 § 7.").

PENDING SYNTHESIZER ARBITRATION (in-tier, expected by 2026-W20).

---

## § 8  Departing-Synthesizer's three standing notes (verbatim, S7 § E)

Source: tex/submitted/control center/synthesizer_inbox/STRATEGYZER_HANDOFF_2026-05-08.md  (S7; FOUND).

{fence_block("markdown", S7_excerpt)}

---

## § 9  AEAL provenance

- Substrate manifest SHA-256: {manifest_sha}
- Compile script (build_package.py) SHA-256: {script_sha}
- Per-source SHA-256, size, and mtime: see § 1 manifest.
- Claim entries: claims.jsonl in this session directory.

---

End of P-008 input package.
"""

OUT.write_text(body, encoding="utf-8", newline="\n")
print(f"Wrote {OUT}")
print(f"Bytes: {OUT.stat().st_size}")
print(f"SHA: {sha256(OUT)}")
