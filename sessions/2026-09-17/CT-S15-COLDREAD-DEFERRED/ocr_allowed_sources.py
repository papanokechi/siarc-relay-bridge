from pathlib import Path
from rapidocr_onnxruntime import RapidOCR

paths = [
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2634.png",
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2635.png",
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\jimbo_p1152.png",
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p2.png",
    r"C:\LocalWork\siarc-relay-bridge\sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p3.png",
]
ocr = RapidOCR()
for path in paths:
    print(f"==== {path} ====")
    result, _ = ocr(path)
    if not result:
        print("<no text>")
        continue
    for box, text, score in result:
        print(f"{score:.3f}\t{text}")
