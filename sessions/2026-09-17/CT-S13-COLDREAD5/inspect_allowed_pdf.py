from pathlib import Path
import fitz
pdf = Path('sessions/2026-09-17/CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf')
doc = fitz.open(pdf)
print('pages', doc.page_count)
# find pages whose visible page text contains 2634/Classification maybe using text layer as navigation, not final table quote
for i, page in enumerate(doc):
    text=page.get_text()
    if 'Classification of Families' in text or 'r(0)' in text or '2634' in text or '2635' in text:
        print('--- pdf_index', i, '---')
        print(text[:4000])
