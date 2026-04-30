"""SIARC-COHERENCE-AUDIT: Extract Conjecture/Theorem/Lemma/Proposition
from the 7 SIARC papers' .tex sources.

Outputs claims.json with per-paper list of {kind, label, name, body_first300}.
Also dumps a flat extracted_claims.md.
"""
from __future__ import annotations
import re, json, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

PAPERS = {
    "UMB":  ROOT / "tex" / "submitted" / "umbrella_program_paper" / "main.tex",
    "P14":  ROOT / "tex" / "submitted" / "paper4_takeuchi_outline.tex",
    "P14alt": ROOT / "tex" / "submitted" / "paper14-ratio-universality-SUBMISSION.tex",
    "T2A":  ROOT / "t2a_paper_draft.tex",
    "T2B":  ROOT / "tex" / "submitted" / "t2b_paper_draft_v5_withauthor.tex",
    "P06":  ROOT / "tex" / "submitted" / "p06_desert_ijnt_submission" / "pcf_desert_negative_result.tex",
    "P08":  ROOT / "tex" / "submitted" / "vquad_resurgence_R2.tex",
    "P11":  ROOT / "f1_mathcomp_submission" / "main_R1.tex",
}

KINDS = ["conjecture", "theorem", "lemma", "proposition", "corollary",
         "observation", "definition", "problem"]

ENV_RE = {k: re.compile(r"\\begin\{"+k+r"\}(\[[^\]]*\])?(.*?)\\end\{"+k+r"\}", re.S | re.I) for k in KINDS}
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")

def extract(path: Path):
    if not path.exists():
        return {"missing": True, "path": str(path)}
    text = path.read_text(encoding="utf-8", errors="replace")
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    out = {"path": str(path.relative_to(ROOT)), "size": len(text), "sha12": sha, "claims": []}
    for kind, rx in ENV_RE.items():
        for m in rx.finditer(text):
            opt = (m.group(1) or "").strip("[]")
            body = m.group(2).strip()
            label_m = LABEL_RE.search(body[:300])
            label = label_m.group(1) if label_m else ""
            # First 400 chars after stripping leading whitespace for fingerprint
            snippet = re.sub(r"\s+", " ", body)[:400]
            out["claims"].append({
                "kind": kind,
                "name": opt,
                "label": label,
                "snippet": snippet,
            })
    return out


def main():
    results = {}
    for tag, p in PAPERS.items():
        results[tag] = extract(p)
        if "claims" in results[tag]:
            print(f"{tag}: {len(results[tag]['claims'])} claims  ({results[tag]['path']}, sha12={results[tag]['sha12']})")
        else:
            print(f"{tag}: MISSING {results[tag]['path']}")

    out_dir = Path(__file__).resolve().parent
    (out_dir / "claims.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

    # Flat dump
    lines = ["# Extracted claims (raw)", ""]
    for tag, res in results.items():
        lines.append(f"## {tag} -- `{res.get('path','?')}` (sha12={res.get('sha12','?')})")
        if res.get("missing"):
            lines.append("MISSING")
            continue
        for c in res["claims"]:
            head = f"- **{c['kind']}** `{c['label'] or '(no label)'}`"
            if c["name"]:
                head += f"  *[{c['name']}]*"
            lines.append(head)
            lines.append(f"  > {c['snippet']}")
        lines.append("")
    (out_dir / "extracted_claims.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_dir/'claims.json'} and extracted_claims.md")

if __name__ == "__main__":
    main()
