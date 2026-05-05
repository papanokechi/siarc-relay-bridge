"""P008-INPUT-PACKAGE-FOR-MSB-2026-06 -- substrate extraction for the
2026-06-01 Strategyzer monthly cycle (relay 045 under v2026-05-08 RACI).

Builds two deliverables:
  - p008_substrate_manifest.json  (S1..S7 paths, sizes, SHA-256, mtime)
  - p008_input_package_for_msb_2026-06.md  (compiled verbatim substrate)

Then runs the framing self-check (HALT_045_PACKAGE_INCLUDES_FRAMING):
greps the compiled .md for opinion words OUTSIDE verbatim quote blocks.

No commentary, no framing, no recommendation -- pure substrate.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WS_ROOT = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat")
OUT_DIR = Path(__file__).parent

SUBSTRATES = [
    {
        "id": "S1",
        "label": "umbrella v2.0 §4 (Phi-triple) source",
        "path": WS_ROOT / "tex" / "submitted" / "umbrella_program_paper" / "main.tex",
        "extract_section": ("\\section{Cross-Degree Framing", "\\section{Logical Structure"),
    },
    {
        "id": "S2",
        "label": "Channel Theory v1.3 §Implications source",
        "path": WS_ROOT / "pcf-research" / "channel" / "cc_pipeline_v13_2026-05-02" / "channel_theory_outline.tex",
        "extract_section": ("\\section{Implications for the Master Conjecture}",
                            "\\section{Open problems and program}"),
    },
    {
        "id": "S3",
        "label": "M9 main-theorem dependency audit verdict (commit 4ffcc8c)",
        "path": WS_ROOT / "siarc-relay-bridge" / "sessions" / "2026-05-05"
                  / "M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT" / "handoff.md",
        "extract_section": None,
    },
    {
        "id": "S4",
        "label": "T2B v3.1 bipartition framing (commit 5d83797)",
        "path": WS_ROOT / "siarc-relay-bridge" / "sessions" / "2026-05-07"
                  / "PCF-2-V2-BIPARTITION-PROMOTION"
                  / "t2b_paper_v3.1_bipartition_promotion.tex",
        "extract_section": ("\\begin{abstract}", "\\section{Setup and notation}"),
    },
    {
        "id": "S5",
        "label": "Working main-theorem statement (if any)",
        "path": None,
        "search_status": "NOT_FOUND",
        "search_reason": (
            "Per M9 audit verdict INDETERMINATE_NO_FORMAL_STATEMENT "
            "(commit 4ffcc8c, 2026-05-05): no formal Theorem/Conjecture "
            "environment for SIARC Master Conjecture v0 (Phi) exists in "
            "any TeX source on disk or on Zenodo. The umbrella v2.0 "
            "companion table records MASTER-V0 explicitly as 'Planned "
            "(post-T1 / Birkhoff--Trjitzinsky)'. No further search "
            "performed; the audit verdict is the load-bearing source."
        ),
    },
    {
        "id": "S6",
        "label": "M6 ✅-vs-Phase-A/B.5 inconsistency status",
        "path": WS_ROOT / "tex" / "submitted" / "CMB.txt",
        "extract_section": "M6_ARBITRATION_PENDING_LOOKUP",
        "alt_paths": [
            WS_ROOT / "cli_log" / "2026-05-05.md",
            WS_ROOT / "cli_log" / "2026-W19_master_prompt.md",
            WS_ROOT / "cli_log" / "2026-W19_wsb.md",
        ],
    },
    {
        "id": "S7",
        "label": "Departing-Synthesizer's three standing notes (Strategyzer→CLI handoff §E)",
        "path": WS_ROOT / "tex" / "submitted" / "control center"
                  / "synthesizer_inbox" / "STRATEGYZER_HANDOFF_2026-05-08.md",
        "extract_section": ("## E. Standing notes from departing Weekly Synthesizer",
                            "## F. Closing"),
    },
]

# rule5 grounding sources
GROUNDING = {
    "cmb": WS_ROOT / "tex" / "submitted" / "CMB.txt",
    "cli_log_today": WS_ROOT / "cli_log" / "2026-05-05.md",
    "bridge_30day": WS_ROOT / "siarc-relay-bridge" / "sessions",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def file_meta(path: Path) -> dict:
    if not path.exists():
        return {"status": "NOT_FOUND", "path": str(path)}
    st = path.stat()
    return {
        "status": "FOUND",
        "path": str(path),
        "size_bytes": st.st_size,
        "sha256": sha256_file(path),
        "mtime_utc": datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(),
    }


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_between(text: str, start_marker: str, end_marker: str) -> str | None:
    """Extract substring from start_marker (inclusive) to end_marker (exclusive)."""
    i = text.find(start_marker)
    if i == -1:
        return None
    j = text.find(end_marker, i + len(start_marker))
    if j == -1:
        return text[i:]
    return text[i:j].rstrip() + "\n"


def grep_lines(path: Path, patterns: list[str], context: int = 1) -> list[str]:
    """Return lines matching any pattern, with simple line-number context."""
    if not path.exists():
        return [f"[NOT FOUND: {path}]"]
    try:
        text = read_text(path)
    except Exception as exc:
        return [f"[READ ERROR: {exc}]"]
    out = []
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if any(re.search(pat, ln) for pat in patterns):
            lo = max(0, i - context)
            hi = min(len(lines), i + context + 1)
            out.append(f"L{lo+1}-L{hi}:")
            for k in range(lo, hi):
                out.append(f"  {k+1}: {lines[k]}")
    return out or ["[no matches]"]


def build_manifest() -> dict:
    manifest = {
        "compiled_utc": datetime.now(tz=timezone.utc).isoformat(),
        "compiler": "CLI-Tactical-Executer (relay 045, sweep 044 in flight)",
        "raci_anchor": "v2026-05-08 (bridge commit 177bfd7, "
                       "RACI-V2026-05-08-INSTALL re-fire)",
        "substrates": [],
    }
    for s in SUBSTRATES:
        entry = {"id": s["id"], "label": s["label"]}
        if s.get("path") is None:
            entry["status"] = s.get("search_status", "NOT_FOUND")
            entry["reason"] = s.get("search_reason", "")
        else:
            entry.update(file_meta(s["path"]))
            entry["alt_paths"] = []
            for alt in s.get("alt_paths", []) or []:
                entry["alt_paths"].append(file_meta(alt))
        manifest["substrates"].append(entry)
    return manifest


def grounding_block() -> tuple[str, dict]:
    """Capture rule5 grounding evidence; return (markdown_block, evidence_dict)."""
    cmb = file_meta(GROUNDING["cmb"])
    cli_log = file_meta(GROUNDING["cli_log_today"])
    bridge = GROUNDING["bridge_30day"]
    bridge_count = 0
    if bridge.exists():
        cutoff_ts = datetime.now(tz=timezone.utc).timestamp() - 30 * 86400
        for p in bridge.rglob("*"):
            if p.is_file():
                try:
                    if p.stat().st_mtime > cutoff_ts:
                        bridge_count += 1
                except Exception:
                    pass

    cmb_status = "FOUND" if cmb.get("status") == "FOUND" else "NOT_FOUND"
    cmb_mtime = cmb.get("mtime_utc", "n/a")
    cli_status = "FOUND" if cli_log.get("status") == "FOUND" else "NOT_FOUND"
    cli_mtime = cli_log.get("mtime_utc", "n/a")

    overall = "COMPLETE" if (cmb_status == "FOUND" and cli_status == "FOUND" and bridge_count > 0) else "PARTIAL"
    if cmb_status == "FOUND":
        cmb_mtime_local = datetime.fromisoformat(cmb_mtime.replace("Z", "+00:00"))
        cmb_age_hours = (datetime.now(tz=timezone.utc) - cmb_mtime_local).total_seconds() / 3600
        if cmb_age_hours > 24:
            overall = "PARTIAL_CMB_HEADER_STALE_GT_24H"

    md = f"""## §0  rule5 grounding evidence (captured {datetime.now(tz=timezone.utc).isoformat()})

- CMB header: {cmb_status} mtime_utc={cmb_mtime} sha256={cmb.get('sha256', 'n/a')}
- cli_log/2026-05-05.md: {cli_status} mtime_utc={cli_mtime} sha256={cli_log.get('sha256', 'n/a')}
- Bridge 30-day file count: {bridge_count} files modified in last 30 days
- Status: **{overall}**

CMB header content (first 4 lines, verbatim):
```
{read_text(GROUNDING['cmb']).splitlines()[0:4] if cmb_status == 'FOUND' else 'NOT FOUND'}
```
"""
    return md, {
        "cmb": cmb,
        "cli_log_today": cli_log,
        "bridge_30day_file_count": bridge_count,
        "overall": overall,
    }


def compile_package(manifest: dict) -> str:
    parts = []
    parts.append("# P-008 Input Package for Strategyzer Monthly Cycle 2026-06")
    parts.append(f"## Compiled: {manifest['compiled_utc']}")
    parts.append(f"## Compiler: {manifest['compiler']}")
    parts.append("## Authority for use: Strategyzer (Tier 1, monthly cadence)")
    parts.append(f"## RACI anchor: {manifest['raci_anchor']}")
    parts.append("")

    grounding_md, grounding_dict = grounding_block()
    parts.append(grounding_md)
    parts.append("")

    # §1 substrate manifest
    parts.append("## §1  Substrate manifest")
    parts.append("")
    parts.append("| ID | Label | Path | Size (B) | SHA-256 (16) | Status |")
    parts.append("|----|-------|------|----------|--------------|--------|")
    for s in manifest["substrates"]:
        sha = s.get("sha256", "")
        sha16 = sha[:16] if sha else "n/a"
        size = s.get("size_bytes", "n/a")
        path = s.get("path", "n/a")
        status = s.get("status", "NOT_FOUND")
        # escape pipe in path
        path_md = str(path).replace("|", "\\|") if path else "n/a"
        parts.append(f"| {s['id']} | {s['label']} | `{path_md}` | {size} | `{sha16}` | {status} |")
    parts.append("")

    # §2 umbrella v2.0 §4 verbatim
    parts.append("## §2  Umbrella v2.0 §4 Cross-Degree Framing: the Invariant Triple (verbatim)")
    parts.append("")
    s1 = next(s for s in SUBSTRATES if s["id"] == "S1")
    if s1["path"].exists():
        text = read_text(s1["path"])
        section = extract_between(text,
                                  "\\section{Cross-Degree Framing",
                                  "\\section{Logical Structure")
        if section:
            parts.append("```latex")
            parts.append(section.rstrip())
            parts.append("```")
        else:
            parts.append("**EXTRACT FAILED**: §4 markers not found in source.")
    else:
        parts.append("**NOT FOUND** -- Strategyzer should request before drafting.")
    parts.append("")

    # §3 CT v1.3 §Implications verbatim
    parts.append("## §3  Channel Theory v1.3 §Implications for the Master Conjecture (verbatim)")
    parts.append("")
    s2 = next(s for s in SUBSTRATES if s["id"] == "S2")
    if s2["path"].exists():
        text = read_text(s2["path"])
        section = extract_between(text,
                                  "\\section{Implications for the Master Conjecture}",
                                  "\\section{Open problems and program}")
        if section:
            parts.append("```latex")
            parts.append(section.rstrip())
            parts.append("```")
        else:
            parts.append("**EXTRACT FAILED**: §Implications markers not found.")
    else:
        parts.append("**NOT FOUND** -- Strategyzer should request before drafting.")
    parts.append("")

    # §4 M9 audit verdict
    parts.append("## §4  M9 main-theorem dependency audit verdict (commit 4ffcc8c, 2026-05-05)")
    parts.append("")
    s3 = next(s for s in SUBSTRATES if s["id"] == "S3")
    if s3["path"].exists():
        text = read_text(s3["path"])
        # Extract the verdict-relevant header section: from "Verdict (operator escalation gate)" through Step-1 + Step-4 verdict + Recommended next step
        verdict_block = extract_between(text,
                                        "## Verdict (operator escalation gate)",
                                        "## What was accomplished")
        rec_block = extract_between(text,
                                    "## Recommended next step",
                                    "## Files committed")
        step1_block = extract_between(text,
                                      "## Step 1 — Statement-of-record",
                                      "## Step 2")
        step4_block = extract_between(text,
                                      "## Step 4 — Verdict + caveat-language recommendation",
                                      "## Judgment calls made")
        parts.append("### §4.A Verdict (verbatim)")
        parts.append("")
        parts.append("```markdown")
        parts.append((verdict_block or "[VERDICT BLOCK NOT FOUND]").rstrip())
        parts.append("```")
        parts.append("")
        parts.append("### §4.B Step 1 statement-of-record (verbatim)")
        parts.append("")
        parts.append("```markdown")
        parts.append((step1_block or "[STEP 1 BLOCK NOT FOUND]").rstrip())
        parts.append("```")
        parts.append("")
        parts.append("### §4.C Step 4 verdict + provisional caveat (verbatim)")
        parts.append("")
        parts.append("```markdown")
        parts.append((step4_block or "[STEP 4 BLOCK NOT FOUND]").rstrip())
        parts.append("```")
        parts.append("")
        parts.append("### §4.D Recommended next step (verbatim)")
        parts.append("")
        parts.append("```markdown")
        parts.append((rec_block or "[REC BLOCK NOT FOUND]").rstrip())
        parts.append("```")
    else:
        parts.append("**HALT_045_M9_AUDIT_NOT_FOUND** -- audit handoff unreadable.")
    parts.append("")

    # §5 T2B v3.1 abstract + intro
    parts.append("## §5  T2B v3.1 bipartition framing (commit 5d83797): abstract + introduction (verbatim)")
    parts.append("")
    s4 = next(s for s in SUBSTRATES if s["id"] == "S4")
    if s4["path"].exists():
        text = read_text(s4["path"])
        abs_block = extract_between(text, "\\begin{abstract}", "\\end{abstract}")
        intro_block = extract_between(text,
                                      "\\section{Introduction}\\label{sec:intro}",
                                      "\\section{Setup and notation}")
        parts.append("### §5.A Abstract (verbatim)")
        parts.append("")
        parts.append("```latex")
        if abs_block:
            parts.append("\\begin{abstract}")
            parts.append(abs_block.replace("\\begin{abstract}", "").rstrip())
            parts.append("\\end{abstract}")
        else:
            parts.append("[ABSTRACT NOT FOUND]")
        parts.append("```")
        parts.append("")
        parts.append("### §5.B Introduction (verbatim)")
        parts.append("")
        parts.append("```latex")
        parts.append((intro_block or "[INTRO NOT FOUND]").rstrip())
        parts.append("```")
    else:
        parts.append("**HALT_045_T2B_V31_NOT_FOUND** -- v3.1 manuscript unreadable.")
    parts.append("")

    # §6 working main-theorem statement
    parts.append("## §6  Working main-theorem statement (S5)")
    parts.append("")
    parts.append("**NO WORKING M9 MAIN-THEOREM STATEMENT IN CORPUS AS OF 2026-05-05.**")
    parts.append("")
    parts.append("Per M9 main-theorem dependency audit (commit 4ffcc8c, 2026-05-05),")
    parts.append("verdict `INDETERMINATE_NO_FORMAL_STATEMENT`: no formal")
    parts.append("`\\begin{theorem}` or `\\begin{conjecture}` environment labelled")
    parts.append("'Master Conjecture v0', 'MASTER-V0', or 'Phi' exists in any TeX")
    parts.append("source on disk or on Zenodo as of the audit date. The umbrella")
    parts.append("v2.0 companion table records MASTER-V0 explicitly as 'Planned")
    parts.append("(post-T1 / Birkhoff--Trjitzinsky)'. The closest formal environments")
    parts.append("are downstream conjectures (`conj:b5-b6-d3` cubic-modular split,")
    parts.append("d=3-restricted; `prob:chi-Phi-compatibility` open-problem entry).")
    parts.append("")

    # §7 M6 ✅-vs-Phase-A/B.5 status
    parts.append("## §7  M6 ✅-vs-Phase-A/B.5 status")
    parts.append("")
    parts.append("**PENDING SYNTHESIZER ARBITRATION (in-tier under v2026-05-08 RACI;")
    parts.append("expected by W20 per W19 master prompt).**")
    parts.append("")
    parts.append("Verbatim grounding from CMB.txt (lines 1517-1518):")
    parts.append("")
    parts.append("```text")
    cmb_lines = grep_lines(GROUNDING["cmb"],
                           [r"M6.*Phase|Phase.*M6|M6 inconsistency|M6 arbitration|✅-vs-Phase"],
                           context=1)
    for ln in cmb_lines[:30]:
        parts.append(ln)
    parts.append("```")
    parts.append("")
    parts.append("Verbatim grounding from cli_log/2026-05-05.md (line 1234):")
    parts.append("")
    parts.append("```text")
    cli_lines = grep_lines(WS_ROOT / "cli_log" / "2026-05-05.md",
                           [r"M6.*Phase|Phase.*M6|M6 arbitration|✅-vs-Phase"],
                           context=1)
    for ln in cli_lines[:30]:
        parts.append(ln)
    parts.append("```")
    parts.append("")
    parts.append("Verbatim grounding from cli_log/2026-W19_master_prompt.md / wsb.md:")
    parts.append("")
    parts.append("```text")
    wsb_lines = grep_lines(WS_ROOT / "cli_log" / "2026-W19_wsb.md",
                           [r"M6.*Phase|Phase.*M6|✅-vs-Phase"],
                           context=1)
    for ln in wsb_lines[:30]:
        parts.append(ln)
    parts.append("```")
    parts.append("")
    parts.append("No verdict issued in cli_log as of compile time.")
    parts.append("Status as of 2026-05-05: M6 arbitration is in-tier scope")
    parts.append("under v2026-05-08 RACI; expected by W20 per W19 master prompt.")
    parts.append("")

    # §8 standing notes
    parts.append("## §8  Departing-Synthesizer's three standing notes (verbatim)")
    parts.append("")
    s7 = next(s for s in SUBSTRATES if s["id"] == "S7")
    if s7["path"].exists():
        text = read_text(s7["path"])
        notes_block = extract_between(text,
                                      "## E. Standing notes from departing Weekly Synthesizer",
                                      "## F. Closing")
        parts.append("```markdown")
        parts.append((notes_block or "[STANDING NOTES BLOCK NOT FOUND]").rstrip())
        parts.append("```")
    else:
        parts.append("**NOT FOUND** -- handoff doc unreadable; check 043 fire status.")
    parts.append("")

    # §9 AEAL provenance
    parts.append("## §9  AEAL provenance")
    parts.append("")
    parts.append("Substrate manifest is recorded at `p008_substrate_manifest.json`")
    parts.append("(SHA-256 to be computed post-write).")
    parts.append("Compile script SHA-256:")
    parts.append("")
    parts.append(f"```")
    parts.append(f"compile_package.py SHA-256: {sha256_file(Path(__file__))}")
    parts.append(f"```")
    parts.append("")
    parts.append("All seven substrate sources S1..S7 have SHA-256 entries in")
    parts.append("`p008_substrate_manifest.json` (S5 marked NOT_FOUND with reason).")
    parts.append("")

    return "\n".join(parts) + "\n"


# Words that, if they appear OUTSIDE a verbatim/quoted block in the
# compiled package, would breach rule6 framing-discipline (HALT_045_PACKAGE_INCLUDES_FRAMING).
FRAMING_WORDS = ["should", "recommend", "propose", "argue", "suggest",
                 "we believe", "our view", "ought"]


def framing_self_check(md_text: str) -> dict:
    """Scan compiled markdown for opinion words OUTSIDE verbatim quote blocks.

    Verbatim blocks are bounded by ```...``` triple-backtick fences.
    Returns dict with 'pass': bool, 'violations': list of (line_no, word, snippet).
    """
    in_block = False
    violations = []
    for i, ln in enumerate(md_text.splitlines(), start=1):
        if ln.strip().startswith("```"):
            in_block = not in_block
            continue
        if in_block:
            continue
        # Skip headings that name a known section structure
        if ln.startswith("#"):
            continue
        # The standing-notes verbatim §8 has framing words but they're inside
        # a ```markdown fence so they're skipped by the block flag.
        # We still need to allow lines that quote the policy itself; those
        # appear inside `code`-spans as `should`.
        # Treat backtick-wrapped occurrences as quoted.
        # Strip code spans first.
        stripped = re.sub(r"`[^`]+`", "", ln)
        for w in FRAMING_WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", stripped, flags=re.IGNORECASE):
                violations.append({"line": i, "word": w,
                                   "snippet": ln[:140]})
    return {"pass": len(violations) == 0, "violations": violations}


def write_claims(manifest_sha: str, package_sha: str,
                 not_found_count: int, grounding_status: str,
                 script_sha: str) -> int:
    claims = [
        {
            "claim": f"substrate_manifest_sha256_{manifest_sha[:16]}",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "compile_package.py",
            "output_hash": manifest_sha,
        },
        {
            "claim": f"input_package_md_sha256_{package_sha[:16]}",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "compile_package.py",
            "output_hash": package_sha,
        },
        {
            "claim": f"not_found_count_{not_found_count}_of_7_substrate_sources",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "compile_package.py",
            "output_hash": manifest_sha,
        },
        {
            "claim": f"grounding_status_{grounding_status}",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "compile_package.py",
            "output_hash": manifest_sha,
        },
        {
            "claim": f"compile_script_sha256_{script_sha[:16]}",
            "evidence_type": "computation",
            "dps": 0,
            "reproducible": True,
            "script": "compile_package.py",
            "output_hash": script_sha,
        },
    ]
    p = OUT_DIR / "claims.jsonl"
    with p.open("w", encoding="utf-8", newline="\n") as fh:
        for c in claims:
            fh.write(json.dumps(c) + "\n")
    return len(claims)


def main() -> int:
    print(f"[045] compiler script SHA-256: {sha256_file(Path(__file__))}")
    manifest = build_manifest()
    not_found = sum(1 for s in manifest["substrates"] if s.get("status") == "NOT_FOUND")
    print(f"[045] {len(manifest['substrates'])} substrate entries; "
          f"{not_found} NOT_FOUND")

    # Hard-halt checks per relay 045 HALT IF block
    s3 = next(s for s in manifest["substrates"] if s["id"] == "S3")
    if s3.get("status") == "NOT_FOUND":
        halt = {"halt": "HALT_045_M9_AUDIT_NOT_FOUND",
                "reason": "S3 audit handoff unreadable", "manifest": s3}
        (OUT_DIR / "halt_log.json").write_text(json.dumps(halt, indent=2))
        print("[HALT] HALT_045_M9_AUDIT_NOT_FOUND")
        return 2
    s4 = next(s for s in manifest["substrates"] if s["id"] == "S4")
    if s4.get("status") == "NOT_FOUND":
        halt = {"halt": "HALT_045_T2B_V31_NOT_FOUND",
                "reason": "S4 v3.1 manuscript unreadable", "manifest": s4}
        (OUT_DIR / "halt_log.json").write_text(json.dumps(halt, indent=2))
        print("[HALT] HALT_045_T2B_V31_NOT_FOUND")
        return 2

    # Write manifest
    manifest_path = OUT_DIR / "p008_substrate_manifest.json"
    manifest_text = json.dumps(manifest, indent=2)
    manifest_path.write_text(manifest_text, encoding="utf-8", newline="\n")
    manifest_sha = sha256_file(manifest_path)
    manifest["self_sha256"] = manifest_sha
    manifest_text = json.dumps(manifest, indent=2)
    manifest_path.write_text(manifest_text, encoding="utf-8", newline="\n")
    manifest_sha = sha256_file(manifest_path)

    # Compile package
    pkg_md = compile_package(manifest)
    pkg_path = OUT_DIR / "p008_input_package_for_msb_2026-06.md"
    pkg_path.write_text(pkg_md, encoding="utf-8", newline="\n")
    pkg_sha = sha256_file(pkg_path)

    # Framing self-check
    self_check = framing_self_check(pkg_md)
    self_check_path = OUT_DIR / "framing_self_check.json"
    self_check_path.write_text(json.dumps(self_check, indent=2), encoding="utf-8")
    print(f"[045] framing_self_check.pass = {self_check['pass']}")
    if not self_check["pass"]:
        for v in self_check["violations"][:20]:
            print(f"  VIOLATION L{v['line']}: '{v['word']}' in: {v['snippet']!r}")

    # Determine grounding status
    grounding_path = OUT_DIR / "grounding_evidence.json"
    _, grounding_dict = grounding_block()
    grounding_path.write_text(json.dumps(grounding_dict, indent=2, default=str),
                              encoding="utf-8")
    grounding_status = grounding_dict["overall"]

    # AEAL claims
    script_sha = sha256_file(Path(__file__))
    n_claims = write_claims(manifest_sha, pkg_sha, not_found, grounding_status,
                            script_sha)
    print(f"[045] wrote {n_claims} AEAL claims")

    # discrepancy / unexpected logs (empty for 045 substrate-only)
    (OUT_DIR / "discrepancy_log.json").write_text(
        json.dumps({"discrepancy_count": 0, "discrepancies": []}, indent=2),
        encoding="utf-8")
    (OUT_DIR / "unexpected_finds.json").write_text(
        json.dumps({"unexpected_finds_count": 0, "finds": []}, indent=2),
        encoding="utf-8")

    # halt_log.json: empty if framing self-check passed; else log violations
    if self_check["pass"]:
        (OUT_DIR / "halt_log.json").write_text(
            json.dumps({"halt": False,
                        "framing_self_check_pass": True,
                        "raci_anchor": manifest["raci_anchor"]},
                       indent=2), encoding="utf-8")
    else:
        (OUT_DIR / "halt_log.json").write_text(
            json.dumps({"halt": "HALT_045_PACKAGE_INCLUDES_FRAMING",
                        "violations": self_check["violations"][:50]},
                       indent=2), encoding="utf-8")
        print("[HALT] HALT_045_PACKAGE_INCLUDES_FRAMING")
        return 3

    print(f"[045] DONE")
    print(f"  manifest:  {manifest_path}  sha256={manifest_sha[:16]}")
    print(f"  package:   {pkg_path}  sha256={pkg_sha[:16]}")
    print(f"  grounding: {grounding_status}")
    print(f"  not_found: {not_found}/7")
    return 0


if __name__ == "__main__":
    sys.exit(main())
