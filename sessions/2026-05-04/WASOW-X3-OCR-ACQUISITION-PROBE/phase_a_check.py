"""Phase A: verify slot 04 Wasow 1965 PDF is image-only across §X.3 pages.

Strategy: page count + extract_text() length per page; report any pages that
yield > 50 non-whitespace chars (would indicate text layer).
"""
import pypdf
import hashlib
from pathlib import Path

PDF = Path(r"C:\Users\shkub\OneDrive\Documents\archive\admin\VSCode\claude-chat\tex\submitted\control center\literature\g3b_2026-05-03\04_wasow_1965_dover.pdf")

data = PDF.read_bytes()
sha = hashlib.sha256(data).hexdigest()
print("SHA256", sha)
print("BYTES", len(data))

r = pypdf.PdfReader(str(PDF))
n = len(r.pages)
print("NUM_PAGES", n)

text_layer_pages = []
sample_lengths = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception as e:
        t = ""
    stripped = "".join(t.split())
    sample_lengths.append(len(stripped))
    if len(stripped) > 50:
        text_layer_pages.append((i, len(stripped), t[:200].replace("\n", " ")))

print("PAGES_WITH_TEXT_LAYER >50 chars:", len(text_layer_pages), "/", n)
for i, ln, snip in text_layer_pages[:20]:
    print(f"  page {i:4d}  len={ln:6d}  snippet={snip!r}")

# Histogram of text-extraction lengths
import collections
buckets = collections.Counter()
for ln in sample_lengths:
    if ln == 0: buckets["0"] += 1
    elif ln < 10: buckets["1-9"] += 1
    elif ln < 50: buckets["10-49"] += 1
    elif ln < 200: buckets["50-199"] += 1
    else: buckets["200+"] += 1
print("LENGTH_HISTOGRAM", dict(buckets))

# Search for "Theorem 11.1" or "11.1" anywhere
hits = []
for i, p in enumerate(r.pages):
    try:
        t = p.extract_text() or ""
    except Exception:
        continue
    if "Theorem 11.1" in t or "11.1" in t or "sectorial" in t.lower():
        hits.append((i, t[:300].replace("\n", " ")))
print("THEOREM_11_1_HITS:", len(hits))
for i, snip in hits[:5]:
    print(f"  page {i}: {snip!r}")
