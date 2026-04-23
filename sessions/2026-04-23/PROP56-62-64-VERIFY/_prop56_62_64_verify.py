"""
Exhaustive verification of Prop 5.6, 6.2, 6.4 for all 24 Trans families in F(2,4).
Uses exact rational arithmetic (fractions.Fraction).
"""
import json
from fractions import Fraction
from pathlib import Path

# Load certificate
cert_path = Path(__file__).parent / "f1_base_certificate.json"
with open(cert_path, "r", encoding="utf-8") as f:
    cert = json.load(f)

# Extract Trans families
trans_families = cert["strata"]["Trans"]["families"]
print(f"Total Trans families loaded: {len(trans_families)}")
assert len(trans_families) == 24, f"Expected 24, got {len(trans_families)}"

# Build table
header = (
    f"{'idx':>6} | {'a2':>3} {'a1':>3} {'a0':>3} | {'b1':>3} {'b0':>3} | "
    f"{'a2/b1^2':>10} | {'disc(a)':>8} | 5.6ok | 6.2class | 6.4ok"
)
print()
print(header)
print("-" * len(header))

target_neg = Fraction(-2, 9)
target_pos = Fraction(1, 4)
disc_allowed = {0, 1, 9, 25}

count_neg29 = 0
count_pos14 = 0
count_neither = 0
neither_list = []

disc_exceptions = []
prop56_exceptions = []

for fam in trans_families:
    idx = fam["index"]
    # Coefficients are [a2, a1, a0] (leading first)
    a2 = Fraction(fam["family"]["a"][0])
    a1 = Fraction(fam["family"]["a"][1])
    a0 = Fraction(fam["family"]["a"][2])
    # b is [b2, b1, b0]; b2=0 for Trans
    b1 = Fraction(fam["family"]["b"][1])
    b0 = Fraction(fam["family"]["b"][2])

    # Prop 5.6 / 6.2: a2/b1^2
    ratio = a2 / (b1 * b1)
    
    matches_neg = (ratio == target_neg)
    matches_pos = (ratio == target_pos)
    
    if matches_neg:
        count_neg29 += 1
        cls = "-2/9"
    elif matches_pos:
        count_pos14 += 1
        cls = " 1/4"
    else:
        count_neither += 1
        neither_list.append((idx, ratio))
        cls = f"OTHER({ratio})"
    
    prop56_ok = matches_neg or matches_pos
    if not prop56_ok:
        prop56_exceptions.append(idx)

    # Prop 6.4: disc(a) = a1^2 - 4*a2*a0
    disc = a1 * a1 - 4 * a2 * a0
    disc_int = int(disc)
    prop64_ok = disc_int in disc_allowed
    if not prop64_ok:
        disc_exceptions.append((idx, disc_int))

    print(
        f"{idx:>6} | {int(a2):>3} {int(a1):>3} {int(a0):>3} | {int(b1):>3} {int(b0):>3} | "
        f"{str(ratio):>10} | {disc_int:>8} | {'  Y  ' if prop56_ok else '**N**'} | "
        f"{cls:>8} | {'  Y  ' if prop64_ok else '**N**'}"
    )

print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

# Prop 5.6
if len(prop56_exceptions) == 0:
    print(f"PROP 5.6: CONFIRMED — all 24 have a2/b1² ∈ {{-2/9, 1/4}}")
else:
    print(f"PROP 5.6: FAILED ({len(prop56_exceptions)} exceptions: {prop56_exceptions})")

# Prop 6.2
if count_neg29 == 22 and count_pos14 == 2 and count_neither == 0:
    print(f"PROP 6.2: CONFIRMED 22+2 — exactly 22 with -2/9, exactly 2 with 1/4")
else:
    print(f"PROP 6.2: FAILED (actual split: {count_neg29}+{count_pos14}+{count_neither})")
    if neither_list:
        for nidx, nratio in neither_list:
            print(f"  Exception: family {nidx} has a2/b1² = {nratio}")

# Prop 6.4
if len(disc_exceptions) == 0:
    print(f"PROP 6.4: CONFIRMED — all 24 disc(a) ∈ {{0, 1, 9, 25}}")
else:
    print(f"PROP 6.4: FAILED ({len(disc_exceptions)} exceptions)")
    for eidx, edisc in disc_exceptions:
        print(f"  Exception: family {eidx} has disc(a) = {edisc}")

# Disc distribution
from collections import Counter
disc_vals = []
for fam in trans_families:
    a2 = Fraction(fam["family"]["a"][0])
    a1 = Fraction(fam["family"]["a"][1])
    a0 = Fraction(fam["family"]["a"][2])
    disc_vals.append(int(a1*a1 - 4*a2*a0))
disc_count = Counter(disc_vals)
print(f"\nDiscriminant distribution: {dict(sorted(disc_count.items()))}")
print(f"  a2/b1² = -2/9 count: {count_neg29}")
print(f"  a2/b1² =  1/4 count: {count_pos14}")
