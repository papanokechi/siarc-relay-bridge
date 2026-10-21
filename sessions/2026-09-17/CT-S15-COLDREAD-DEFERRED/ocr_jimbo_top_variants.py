from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance
from rapidocr_onnxruntime import RapidOCR
src = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\jimbo_p1152.png")
outdir = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S15-COLDREAD-DEFERRED")
img = Image.open(src).convert('RGB')
print('image_size', img.size)
# crop upper 45%, where system and parameter dictionary are located
w,h = img.size
crops = {
    'top_full': (0,0,w,int(h*0.48)),
    'system_area': (0,int(h*0.02),w,int(h*0.22)),
    'params_area': (0,int(h*0.16),w,int(h*0.40)),
    'assumption_area': (0,int(h*0.36),w,int(h*0.50)),
}
ocr = RapidOCR()
for name, box in crops.items():
    crop = img.crop(box)
    # enlarge and sharpen for OCR
    crop = crop.resize((crop.width*2, crop.height*2))
    crop = ImageEnhance.Contrast(crop).enhance(1.5)
    path = outdir / f'{name}.png'
    crop.save(path)
    print(f'==== {name} {box} saved={path} ====')
    result, _ = ocr(str(path))
    if not result:
        print('<no text>')
        continue
    for pts,text,score in result:
        xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
        print(f'{score:.3f}\t({min(xs):.0f},{min(ys):.0f})-({max(xs):.0f},{max(ys):.0f})\t{text}')
