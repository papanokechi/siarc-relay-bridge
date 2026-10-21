from pathlib import Path
from PIL import Image, ImageEnhance
from rapidocr_onnxruntime import RapidOCR
src = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\jimbo_p1152.png")
outdir = Path(r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-S15-COLDREAD-DEFERRED")
img = Image.open(src).convert('RGB')
w,h = img.size
print('image_size', img.size)
crops = {
    'tau_assumption': (0, int(h*0.38), w, int(h*0.68)),
    'assumption_only': (0, int(h*0.52), w, int(h*0.64)),
    'asymptotic': (0, int(h*0.58), w, int(h*0.92)),
}
ocr = RapidOCR()
for name, box in crops.items():
    crop = img.crop(box).resize(((box[2]-box[0])*2, (box[3]-box[1])*2))
    crop = ImageEnhance.Contrast(crop).enhance(1.7)
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
