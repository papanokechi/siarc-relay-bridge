from pathlib import Path
p = Path('sessions') / '2026-09-17' / 'CT-S1-THEOREM' / 'theorem.tex'
lines = p.read_text(encoding='utf-8').splitlines()
ranges = [('thm:radius Step 3',187,233),('thm:growth Step 3',302,347),('growth hypotheses',266,276),('A2 assumptions',50,57)]
for title, a, b in ranges:
    print(f'===== {title}: lines {a}-{b} =====')
    for i in range(a, b+1):
        print(f'{i}: {lines[i-1]}')
    print()
