from pathlib import Path
import hashlib
paths = [
    Path('sessions/2026-09-17/CT-R1-AUDIT/coldpackets/vdps_p2634.png'),
    Path('sessions/2026-09-17/CT-R1-AUDIT/coldpackets/vdps_p2635.png'),
    Path('sessions/2026-09-17/CT-R1-AUDIT/refs/vanderPut-Saito-AIF-2009-59-7-2611.pdf'),
]
for p in paths:
    data=p.read_bytes()
    print(f'{p}: exists={p.exists()} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}')
try:
    from PIL import Image
    for p in paths[:2]:
        im=Image.open(p)
        print(f'{p}: image_size={im.size}')
except Exception as e:
    print('PIL_image_info_error=', repr(e))
