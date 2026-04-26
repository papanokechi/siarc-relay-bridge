"""Step 1: enumerate achievable a2/b1^2 ratios at D=5, filter to negative
Worpitzky interior (-1/4, 0)."""
from fractions import Fraction

D = 5
A2 = [a for a in range(-D, D+1) if a != 0]
B1 = [b for b in range(-D, D+1) if b != 0]
ratios = sorted({Fraction(a, b*b) for a in A2 for b in B1})

neg_int = [r for r in ratios if Fraction(-1, 4) < r < 0]
print(f"D={D}: {len(ratios)} distinct ratios overall")
print(f"D={D}: {len(neg_int)} distinct negative Worpitzky-interior ratios (-1/4 < r < 0):")
for r in neg_int:
    print(f"  {r} = {float(r):+.6f}")

# D=4 baseline
D2 = 4
A2_4 = [a for a in range(-D2, D2+1) if a != 0]
B1_4 = [b for b in range(-D2, D2+1) if b != 0]
ratios_4 = sorted({Fraction(a, b*b) for a in A2_4 for b in B1_4})
neg_int_4 = [r for r in ratios_4 if Fraction(-1,4) < r < 0]
print(f"\nD={D2}: {len(neg_int_4)} negative Worpitzky-interior ratios:")
for r in neg_int_4:
    print(f"  {r} = {float(r):+.6f}")

new_at_5 = sorted(set(neg_int) - set(neg_int_4))
print(f"\nNEW at D=5 (not present at D=4): {len(new_at_5)}")
for r in new_at_5:
    print(f"  {r} = {float(r):+.6f}")
