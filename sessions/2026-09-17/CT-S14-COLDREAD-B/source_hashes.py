from pathlib import Path
import hashlib

root = Path(r'C:\LocalWork\siarc-relay-bridge')
files = [
    r'sessions\2026-09-17\CT-R1-AUDIT\coldpackets\PACKET-D-objectB.md',
    r'sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2634.png',
    r'sessions\2026-09-17\CT-R1-AUDIT\coldpackets\vdps_p2635.png',
    r'sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p2.png',
    r'sessions\2026-09-17\CT-R1-AUDIT\coldpackets\companion_v12_p3.png',
]
for rel in files:
    data = (root / rel).read_bytes()
    print(f'{hashlib.sha256(data).hexdigest()}  {rel}')
