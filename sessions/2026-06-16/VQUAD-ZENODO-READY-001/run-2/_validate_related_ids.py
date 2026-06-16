"""Gate-1 (related-identifiers) + Gate-2.2 (wrong-venue) pre-checks for the V_quad
deposit re-run (VQUAD-ZENODO-READY-001 / run-2). No network; static validation
mirroring what run_production_draft.py enforces at deposit time.
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
RID = os.path.join(HERE, "related_identifiers.md")
PDF = os.path.normpath(os.path.join(
    HERE, "..", "..", "VQUAD-REPRO-BUNDLE-002",
    "vquad-periodrep-bundle", "paper", "vquad-periodrep-paper.pdf"))

BLOCKLIST = {"20455090", "20481592", "20694841", "19885550",
             "20569724", "20571232", "20624814"}

# ---- Gate 1: parse the wired array from related_identifiers.md ----
txt = open(RID, encoding="utf-8").read()
m = re.search(r"```json\s*(\{.*?\})\s*```", txt, re.S)
arr = json.loads(m.group(1))["related_identifiers"]

c = sum(1 for r in arr if r["relation"] == "continues")
ip = sum(1 for r in arr if r["relation"] == "isPartOf")
rf = sum(1 for r in arr if r["relation"] == "references")
sp = sum(1 for r in arr if r["relation"] == "isSupplementTo")

print("=== GATE 1 (related identifiers, Scenario B) ===")
print(f"len={len(arr)} continues={c} isPartOf={ip} references={rf} isSupplementTo={sp}")
gate1_count = (len(arr) == 11 and c == 2 and ip == 1 and rf == 8 and sp == 0)
print("count assertion 11 (2+1+8+0):", gate1_count)

ids = [r["identifier"] for r in arr]
placeholder = [i for i in ids if "{{" in i or "}}" in i]
leak = [i for i in ids for b in BLOCKLIST if b in i]
print("placeholders remaining:", placeholder)
print("BLOCKLIST version-DOI leak:", leak)
print("retracted 20455090 present:", any("20455090" in i for i in ids))
print("concept 20455089 present:", any("20455089" in i for i in ids))
all_doi_scheme = all(r["scheme"] == "doi" for r in arr)
print("all scheme=doi:", all_doi_scheme)
gate1 = (gate1_count and not placeholder and not leak
         and not any("20455090" in i for i in ids)
         and any("20455089" in i for i in ids) and all_doi_scheme)
print("GATE 1:", "PASS" if gate1 else "FAIL")

# ---- Gate 2.2: wrong-venue token absent in the corrections-final PDF ----
print("\n=== GATE 2.2 (wrong-venue, vs 4ca12a35 PDF) ===")
from pypdf import PdfReader
t = "".join((p.extract_text() or "") for p in PdfReader(PDF).pages)
print("PDF chars:", len(t))
checks = {}
for tok in ["Compositio", "AAECC", "ETNA"]:
    checks[tok] = tok in t
    print(f"{tok:12} present: {checks[tok]}")
# JSC citation collision sanity (legitimate 'Symbolic Comput' must be present, not a halt token)
print("'Symbolic Comput' (legit Kovacic cite) present:", "Symbolic Comput" in t)
gate22 = not any(checks.values())
print("GATE 2.2:", "PASS" if gate22 else "FAIL")

print("\n=== SUMMARY ===")
print("GATE 1 (DOI completeness/no-leak):", "PASS" if gate1 else "FAIL")
print("GATE 2.2 (wrong-venue absent):", "PASS" if gate22 else "FAIL")
