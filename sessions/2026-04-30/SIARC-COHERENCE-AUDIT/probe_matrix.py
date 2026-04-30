"""SIARC-COHERENCE-AUDIT: Automated cross-paper checks.

Runs targeted regex scans for:
- degree conventions (2,1), (2,2), (4,2), (4,3), (5,3)
- Zenodo DOIs and stale submission IDs
- Class A / Class B mentions
- T0/T1/T2/T3 tier mentions
"""
import re, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PAPERS = {
    "UMB":     ROOT / "tex" / "submitted" / "umbrella_program_paper" / "main.tex",
    "P14":     ROOT / "tex" / "submitted" / "paper4_takeuchi_outline.tex",
    "P14alt":  ROOT / "tex" / "submitted" / "paper14-ratio-universality-SUBMISSION.tex",
    "T2A":     ROOT / "t2a_paper_draft.tex",
    "T2B":     ROOT / "tex" / "submitted" / "t2b_paper_draft_v5_withauthor.tex",
    "P06":     ROOT / "tex" / "submitted" / "p06_desert_ijnt_submission" / "pcf_desert_negative_result.tex",
    "P08":     ROOT / "tex" / "submitted" / "vquad_resurgence_R2.tex",
    "P11":     ROOT / "f1_mathcomp_submission" / "main_R1.tex",
    "P11refs": ROOT / "f1_mathcomp_submission" / "references.bib",
}

PROBES = [
    ("deg_2_1",     r"\(\s*2\s*,\s*1\s*\)"),
    ("deg_2_2",     r"\(\s*2\s*,\s*2\s*\)"),
    ("deg_4_2",     r"\(\s*4\s*,\s*2\s*\)"),
    ("deg_4_3",     r"\(\s*4\s*,\s*3\s*\)"),
    ("deg_5_3",     r"\(\s*5\s*,\s*3\s*\)"),
    ("deg_3_1",     r"\(\s*3\s*,\s*1\s*\)"),
    ("F_2_4",       r"\\?(?:mathcal\{F\}|FF)\(2,\s*4\)|\$\\F+\(2\s*,\s*4\s*\)\$"),
    ("ratio_-2/9",  r"-\s*2\s*/\s*9|-\\tfrac\{2\}\{9\}|-\\frac\{2\}\{9\}"),
    ("ratio_+1/4",  r"\+?\s*1/4\b|\\tfrac\{1\}\{4\}"),
    ("class_A",     r"Class[ ~]?A\b"),
    ("class_B",     r"Class[ ~]?B\b"),
    ("tier_T0",     r"\bT0\b|Tier[~ ]?0\b|tier T0"),
    ("tier_T1",     r"\bT1\b|Tier[~ ]?1\b|tier T1"),
    ("tier_T2",     r"\bT2\b|Tier[~ ]?2\b|tier T2"),
    ("tier_T3",     r"\bT3\b|Tier[~ ]?3\b|tier T3"),
    ("doi_19783311", r"19783311"),
    ("doi_19801038", r"19801038"),
    ("doi_19885549", r"19885549"),
    ("doi_19885550", r"19885550"),
    ("doi_19774029", r"19774029"),
    ("doi_19491767", r"19491767"),
    ("Math_Comp_id", r"260422.Papanokechi|Math\.Comp|MathComp|Mathematics of Computation"),
    ("JTNB_id",     r"JTNB.?2400|JTNB"),
    ("painleve_VI", r"Painlev[ée]\s*~?\s*VI|PVI"),
    ("painleve_III_D6", r"Painlev[ée]\s*~?\s*III[\(\$]?D_?6|PIII\(D_?6\)"),
    ("synthesis_cite", r"\\cite\{synthesis\}"),
    ("spectral_cite", r"\\cite\{spectral\}"),
    ("PSLZ",         r"\\PSLZ|PSL_2\(\\?(?:mathbb|mathbf)\{Z\}\)|PSL2\(Z\)"),
    ("Gamma_0_2",    r"\\Gamma_0\(2\)|Γ_0\(2\)|Gamma_0\(2\)"),
]

def scan(path: Path):
    if not path.exists():
        return {"missing": True}
    text = path.read_text(encoding="utf-8", errors="replace")
    out = {"size": len(text), "hits": {}}
    for name, pat in PROBES:
        rx = re.compile(pat, re.I)
        ms = rx.findall(text)
        out["hits"][name] = len(ms)
    return out

def main():
    res = {}
    for tag, p in PAPERS.items():
        res[tag] = scan(p)

    # build matrix
    probe_names = [n for n,_ in PROBES]
    paper_names = list(PAPERS.keys())

    lines = ["# Coherence probe matrix",
             "",
             "Counts of occurrences per paper (case-insensitive regex hits).",
             "",
             "| probe | " + " | ".join(paper_names) + " |",
             "|" + "---|" * (len(paper_names)+1)]
    for n in probe_names:
        row = [n]
        for tag in paper_names:
            v = res[tag].get("hits", {}).get(n, 0) if not res[tag].get("missing") else "-"
            row.append(str(v))
        lines.append("| " + " | ".join(row) + " |")

    out_dir = Path(__file__).resolve().parent
    (out_dir / "probe_matrix.md").write_text("\n".join(lines), encoding="utf-8")
    (out_dir / "probe_matrix.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(open(out_dir/"probe_matrix.md","r",encoding="utf-8").read())

if __name__ == "__main__":
    main()
