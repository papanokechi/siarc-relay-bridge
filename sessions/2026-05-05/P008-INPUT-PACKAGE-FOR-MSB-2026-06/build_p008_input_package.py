"""Build P-008 input package markdown by extracting verbatim sections from substrate files.

No commentary, no framing, no recommendations. Pure verbatim substrate.
"""
import hashlib
import json
import os
import datetime as dt

WS = r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat"
SD = os.path.join(WS, "siarc-relay-bridge", "sessions", "2026-05-05",
                  "P008-INPUT-PACKAGE-FOR-MSB-2026-06")

S1 = os.path.join(WS, "tex", "submitted", "umbrella_program_paper", "main.tex")
S2 = os.path.join(WS, "pcf-research", "channel", "cc_pipeline_v13_2026-05-02",
                  "channel_theory_outline.tex")
S3 = os.path.join(WS, "siarc-relay-bridge", "sessions", "2026-05-05",
                  "M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT", "handoff.md")
S4 = os.path.join(WS, "siarc-relay-bridge", "sessions", "2026-05-07",
                  "PCF-2-V2-BIPARTITION-PROMOTION",
                  "t2b_paper_v3.1_bipartition_promotion.tex")
CMB = os.path.join(WS, "tex", "submitted", "CMB.txt")
CLILOG = os.path.join(WS, "cli_log", "2026-05-05.md")
WSB = os.path.join(WS, "cli_log", "2026-W19_wsb.md")
S7 = os.path.join(WS, "tex", "submitted", "control center", "synthesizer_inbox",
                  "STRATEGYZER_HANDOFF_2026-05-08.md")


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def lines(path, a, b):
    """Return lines a..b inclusive (1-indexed)."""
    txt = read(path).splitlines(keepends=True)
    return "".join(txt[a-1:b])


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest().upper()


def size(path):
    return os.path.getsize(path)


def mtime(path):
    t = dt.datetime.fromtimestamp(os.path.getmtime(path), tz=dt.timezone.utc)
    return t.isoformat()


# ---------- Build package ---------- #
out = []

now_utc = dt.datetime.now(dt.timezone.utc).isoformat()
out.append("# P-008 Input Package for Strategyzer Monthly Cycle 2026-06\n")
out.append(f"## Compiled: {now_utc}\n")
out.append("## Compiler: CLI-Tactical-Executer (relay 045)\n")
out.append("## Authority for use: Strategyzer (Tier 1, monthly cadence)\n\n")
out.append("This artefact is a passive substrate. It is verbatim extraction "
           "from named source files. The compiler does not frame, position, "
           "or advocate. Operator pastes this document into a fresh "
           "Strategyzer chat for the 2026-06-01 monthly cycle.\n\n")

# ---------------- §0 grounding ---------------- #
out.append("## §0  rule5 grounding evidence\n\n")
out.append("Status: **COMPLETE** (all three rule5 grounding sources reachable).\n\n")
out.append("| Source | Path | mtime (UTC) | sha256 |\n")
out.append("|---|---|---|---|\n")
out.append(f"| (a) CMB header | `tex/submitted/CMB.txt` | {mtime(CMB)} | "
           f"`{sha(CMB)}` |\n")
out.append("| (b) 30-day bridge listing | `siarc-relay-bridge/sessions/` | "
           "see manifest | n/a (directory) |\n")
out.append(f"| (c) latest cli_log | `cli_log/2026-05-05.md` | "
           f"{mtime(CLILOG)} | `{sha(CLILOG)}` |\n\n")
out.append("30-day bridge listing (date directories under "
           "`siarc-relay-bridge/sessions/`): 2026-04-22, 2026-04-23, "
           "2026-04-24, 2026-04-25, 2026-04-26, 2026-04-27, 2026-04-28, "
           "2026-04-29, 2026-04-30, 2026-05-01, 2026-05-02, 2026-05-03, "
           "2026-05-04, 2026-05-05, 2026-05-07, 2026-05-08, template.\n\n")

# ---------------- §1 manifest ---------------- #
out.append("## §1  Substrate manifest\n\n")
out.append("Per spec STEP 2. Full machine-readable manifest at "
           "`p008_substrate_manifest.json` in this session directory.\n\n")
out.append("| Src | Label | Path | Status | Size (B) | sha256 |\n")
out.append("|---|---|---|---|---|---|\n")

man = [
    ("S1", "Umbrella v2.0 main.tex",
     "tex/submitted/umbrella_program_paper/main.tex", S1, "FOUND"),
    ("S2", "CT v1.3 channel_theory_outline.tex",
     "pcf-research/channel/cc_pipeline_v13_2026-05-02/channel_theory_outline.tex",
     S2, "FOUND"),
    ("S3", "M9 main-theorem dependency audit handoff",
     "siarc-relay-bridge/sessions/2026-05-05/M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md",
     S3, "FOUND"),
    ("S4", "T2B v3.1 bipartition manuscript",
     "siarc-relay-bridge/sessions/2026-05-07/PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_promotion.tex",
     S4, "FOUND"),
    ("S5", "Working M9 main-theorem statement (workspace search)",
     "<grep tex/submitted/**/*.tex>", None, "NOT_FOUND"),
    ("S6/CMB", "CMB.txt (M6 status surface)",
     "tex/submitted/CMB.txt", CMB, "FOUND"),
    ("S6/cli_log", "cli_log/2026-05-05.md (M6 arbitration status)",
     "cli_log/2026-05-05.md", CLILOG, "FOUND"),
    ("S6/WSB", "cli_log/2026-W19_wsb.md (M6 framing in WSB)",
     "cli_log/2026-W19_wsb.md", WSB, "FOUND"),
    ("S7", "Departing-Synthesizer's three standing notes (043 inbox handoff)",
     "tex/submitted/control center/synthesizer_inbox/STRATEGYZER_HANDOFF_2026-05-08.md",
     S7, "FOUND"),
]
for src, lbl, rel, ap, st in man:
    if ap and os.path.exists(ap):
        out.append(f"| {src} | {lbl} | `{rel}` | {st} | {size(ap)} | "
                   f"`{sha(ap)}` |\n")
    else:
        out.append(f"| {src} | {lbl} | `{rel}` | {st} | n/a | n/a |\n")
out.append("\n")
out.append("**Substrate gap (S5 NOT_FOUND):** workspace grep over "
           "`tex/submitted/**/*.tex` for the patterns "
           "`thm:main|main_theorem|Main Theorem|Theorem 1.1|theorem M9|"
           "theorem:M9` returned 6 hits, NONE of which is a SIARC Master "
           "Conjecture / MASTER-V0 / Phi formal statement (matches: "
           "`umbrella main.tex` L194 forward-ref to companion paper #14; "
           "`paper14-ratio-universality-SUBMISSION.tex` §Main Theorem = "
           "Ratio Universality, not Phi; `pcf_rational_contamination_2026.tex` "
           "`thm:main` = Trivial rational limit observation; "
           "`pcf_unified_expmath_submission.tex` abstract 'two main theorems' "
           "= Logarithmic Ladder + 4/π Casoratian).\n\n")
out.append("**Substrate path correction (S1, S2):** prompt 045 gave the "
           "umbrella v2.0 location as `tex\\submitted\\<umbrella v2.0 .tex>` "
           "and CT v1.3 as `tex\\submitted\\<CT v1.3 .tex>`. Resolved paths "
           "are `tex/submitted/umbrella_program_paper/main.tex` and "
           "`pcf-research/channel/cc_pipeline_v13_2026-05-02/"
           "channel_theory_outline.tex`. The CT v1.3 working source lives "
           "in the `pcf-research` workspace, not under `tex/submitted/`.\n\n")
out.append("**Section-number note (S1):** prompt 045 §2 calls for "
           "\"Umbrella v2.0 §4 (Phi-triple)\" verbatim. In the resolved "
           "`main.tex`, the Phi-triple substrate is §3 (\"Cross-Degree "
           "Framing: the Invariant Triple\", L212–L403); §4 is "
           "\"Logical Structure of the Program\" (L404–L502). §2 below "
           "extracts the Phi-triple section as resolved. The compiler "
           "made no semantic substitution beyond honouring the "
           "parenthetical \"(Phi-triple)\" label.\n\n")

# ---------------- §2 umbrella v2.0 §3 (Phi-triple) ---------------- #
out.append("## §2  Umbrella v2.0 §3 \"Cross-Degree Framing: the Invariant "
           "Triple\" (Phi-triple) — verbatim\n\n")
out.append("Source: `tex/submitted/umbrella_program_paper/main.tex` "
           "L212–L403 inclusive. Extracted as raw TeX inside a fenced "
           "block.\n\n")
out.append("```tex\n")
out.append(lines(S1, 212, 403))
out.append("```\n\n")

# ---------------- §3 CT v1.3 Implications ---------------- #
out.append("## §3  CT v1.3 §\"Implications for the Master Conjecture\" — "
           "verbatim\n\n")
out.append("Source: `pcf-research/channel/cc_pipeline_v13_2026-05-02/"
           "channel_theory_outline.tex` L1336–L1355 inclusive (full "
           "section body up to but not including the next `\\section`).\n\n")
out.append("```tex\n")
out.append(lines(S2, 1336, 1355))
out.append("```\n\n")

# ---------------- §4 M9 audit verdict ---------------- #
out.append("## §4  M9 main-theorem dependency audit verdict — verbatim "
           "(commit 4ffcc8c)\n\n")
out.append("Source: `siarc-relay-bridge/sessions/2026-05-05/"
           "M9-MAIN-THEOREM-S2-DEPENDENCY-AUDIT/handoff.md`. Verdict + "
           "summary block extracted (L1–L26 of the handoff). Full handoff "
           "is preserved alongside this document at `S3_M9_audit_handoff.md` "
           "in this session directory.\n\n")
out.append("```\n")
out.append(lines(S3, 1, 26))
out.append("```\n\n")

# ---------------- §5 T2B v3.1 framing ---------------- #
out.append("## §5  T2B v3.1 bipartition framing — verbatim (commit 5d83797)\n\n")
out.append("Source: `siarc-relay-bridge/sessions/2026-05-07/"
           "PCF-2-V2-BIPARTITION-PROMOTION/t2b_paper_v3.1_bipartition_"
           "promotion.tex`. §1 (Introduction, L39–L95 inclusive) and the "
           "three bipartition-defining theorem statements (§3 \"Theorem 1: "
           "the resonance family\" L122–L160, §4 \"Theorem 2: Class A and "
           "the Stokes mechanism\" L160–L221, §5 \"Theorem 3: Class B and "
           "the Gauss continued fraction\" L222–L280) are extracted "
           "verbatim. Full source preserved at `S4_t2b_v3.1.tex` in this "
           "session directory.\n\n")
out.append("### §5.1  T2B v3.1 §1 Introduction (L39–L95)\n\n")
out.append("```tex\n")
out.append(lines(S4, 39, 95))
out.append("```\n\n")
out.append("### §5.2  T2B v3.1 §3 Theorem 1: the resonance family (L122–L160)\n\n")
out.append("```tex\n")
out.append(lines(S4, 122, 160))
out.append("```\n\n")
out.append("### §5.3  T2B v3.1 §4 Theorem 2: Class A and the Stokes mechanism (L160–L221)\n\n")
out.append("```tex\n")
out.append(lines(S4, 160, 221))
out.append("```\n\n")
out.append("### §5.4  T2B v3.1 §5 Theorem 3: Class B and the Gauss continued fraction (L222–L280)\n\n")
out.append("```tex\n")
out.append(lines(S4, 222, 280))
out.append("```\n\n")

# ---------------- §6 working main-theorem ---------------- #
out.append("## §6  Working M9 main-theorem statement (S5)\n\n")
out.append("**NO WORKING M9 MAIN-THEOREM STATEMENT IN CORPUS AS OF "
           "2026-05-05 (last grounded date).**\n\n")
out.append("Workspace grep over `tex/submitted/**/*.tex` for "
           "`thm:main|main_theorem|Main Theorem|Theorem 1.1|theorem M9|"
           "theorem:M9` returned 6 hits, none of which is a SIARC Master "
           "Conjecture / MASTER-V0 / Phi formal statement. Verbatim hit "
           "list:\n\n")
out.append("- `tex/submitted/umbrella_program_paper/main.tex:194`: "
           "`--- is the main theorem of companion paper \\#14. We do not "
           "reproduce`\n")
out.append("- `tex/submitted/paper14-ratio-universality-SUBMISSION.tex:97`: "
           "`\\section{Main Theorem: Ratio Universality}\\label{sec:main}`\n")
out.append("- `tex/submitted/pcf_rational_contamination_2026.tex:80`: "
           "`\\begin{observation}[Trivial rational limit]\\label{thm:main}`\n")
out.append("- `tex/submitted/pcf_rational_contamination_2026.tex:115`: "
           "`Together, Observation~\\ref{thm:main} and "
           "Proposition~\\ref{prop:finite}`\n")
out.append("- `tex/submitted/pcf_rational_contamination_2026.tex:220`: "
           "`Trivial zero (Obs.~\\ref{thm:main}) & $a(1)=0$ & 34 & "
           "$K=b(0)$ \\\\`\n")
out.append("- `tex/submitted/pcf_unified_expmath_submission.tex:40`: "
           "`We study polynomial continued fractions and prove two main "
           "theorems`\n\n")
out.append("This independently corroborates the §4 audit verdict "
           "`INDETERMINATE_NO_FORMAL_STATEMENT`.\n\n")

# ---------------- §7 M6 status ---------------- #
out.append("## §7  M6 ✅-vs-Phase-A/B.5 status — verbatim\n\n")
out.append("Surfaces from CMB.txt, cli_log/2026-05-05.md, and "
           "cli_log/2026-W19_wsb.md. As of compile time, no formal "
           "CLI-Synthesizer arbitration verdict has been written to "
           "cli_log. Marker:\n\n")
out.append("> **PENDING SYNTHESIZER ARBITRATION (in-tier, expected by "
           "2026-W20).**\n\n")
out.append("### §7.1  CMB.txt M9 caveat profile (L401–L410, M6 marked ✅)\n\n")
out.append("```\n")
out.append(lines(CMB, 401, 410))
out.append("```\n\n")
out.append("### §7.2  CMB.txt M9 gating + arbitration tracker (L1517–L1528)\n\n")
out.append("```\n")
out.append(lines(CMB, 1517, 1528))
out.append("```\n\n")
out.append("### §7.3  cli_log/2026-05-05.md CLI in-tier upcoming (L1230–L1245)\n\n")
out.append("```\n")
out.append(lines(CLILOG, 1230, 1245))
out.append("```\n\n")
out.append("### §7.4  cli_log/2026-W19_wsb.md M6 framing (verbatim hit lines)\n\n")
out.append("```\n")
out.append(lines(WSB, 14, 18))
out.append("\n")
out.append(lines(WSB, 28, 30))
out.append("\n")
out.append(lines(WSB, 49, 53))
out.append("\n")
out.append(lines(WSB, 78, 78))
out.append("\n")
out.append(lines(WSB, 88, 88))
out.append("```\n\n")

# ---------------- §8 standing notes ---------------- #
out.append("## §8  Departing-Synthesizer's three standing notes — verbatim\n\n")
out.append("Source: `tex/submitted/control center/synthesizer_inbox/"
           "STRATEGYZER_HANDOFF_2026-05-08.md` §E (\"Standing notes from "
           "departing Weekly Synthesizer\"). Anchored at the inbox path "
           "produced by 043 (commit ae37e5a). Full file preserved at "
           "`S7_strategyzer_handoff.md` in this session directory.\n\n")
out.append("```\n")
# §E "Standing notes" runs from header line near 209 to before §F
s7txt = read(S7).splitlines()
# find §E and §F
e_idx = next(i for i, ln in enumerate(s7txt) if ln.startswith("## E."))
f_idx = next(i for i, ln in enumerate(s7txt) if ln.startswith("## F."))
out.append("\n".join(s7txt[e_idx:f_idx]))
out.append("\n```\n\n")

# ---------------- §9 AEAL provenance ---------------- #
out.append("## §9  AEAL provenance\n\n")
out.append("Substrate manifest: `p008_substrate_manifest.json` in this "
           "session directory.\n\n")
build_script = os.path.join(SD, "build_p008_input_package.py")
out.append(f"Extraction script: `build_p008_input_package.py` (this file).\n\n")
out.append("AEAL claim entries: `claims.jsonl` in this session directory "
           "(C1 substrate_manifest sha256, C2 input_package_md sha256, "
           "C3 not_found_count, C4 grounding_status).\n\n")
out.append("All extractions are line-bounded verbatim from the named "
           "sources listed in §1 manifest. No paraphrase, no editorial "
           "framing, no recommendations.\n")

# ---------- write ---------- #
md_path = os.path.join(SD, "p008_input_package_for_msb_2026-06.md")
with open(md_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("".join(out))

print("Wrote:", md_path)
print("Size:", os.path.getsize(md_path))
print("SHA256:", hashlib.sha256(open(md_path, "rb").read()).hexdigest().upper())
