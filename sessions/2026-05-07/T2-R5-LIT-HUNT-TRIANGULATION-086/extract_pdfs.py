"""Extract text + per-page hashes from V1, V2 PDFs for substrate AEAL.

Outputs:
  v1_full.txt  -- full text of V1 PDF
  v2_full.txt  -- full text of V2 PDF
  v1_pages.json, v2_pages.json -- per-page char counts (audit aid)
"""
import json
from pathlib import Path

import pypdf

HERE = Path(__file__).parent


def extract(pdf_path: Path, out_txt: Path, out_pages: Path) -> dict:
    reader = pypdf.PdfReader(str(pdf_path))
    pages = []
    full_text = []
    for i, p in enumerate(reader.pages):
        try:
            t = p.extract_text() or ""
        except Exception as e:
            t = f"[EXTRACTION ERROR PAGE {i + 1}: {e}]"
        pages.append({"page": i + 1, "n_chars": len(t)})
        full_text.append(f"=== PAGE {i + 1} ===\n{t}\n")
    out_txt.write_text("".join(full_text), encoding="utf-8")
    out_pages.write_text(json.dumps(pages, indent=2), encoding="utf-8")
    return {
        "n_pages": len(pages),
        "total_chars": sum(p["n_chars"] for p in pages),
        "out_txt": str(out_txt),
    }


def main() -> None:
    summary = {}
    for tag, pdf_name in [("v1", "v1_arxiv_2307_11217.pdf"),
                          ("v2", "v2_arxiv_1604_03082.pdf")]:
        pdf = HERE / pdf_name
        out_txt = HERE / f"{tag}_full.txt"
        out_pages = HERE / f"{tag}_pages.json"
        summary[tag] = extract(pdf, out_txt, out_pages)
        print(f"{tag}: {summary[tag]}")
    (HERE / "extract_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
