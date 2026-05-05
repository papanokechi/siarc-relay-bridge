"""Smoke test for sweep_b1_5_8_9_10.py helpers."""
import sweep_b1_5_8_9_10 as s

print("Test 1 (b6 k=1 known orbit hit):")
print("  ", s.bauer_orbit_membership((-1, 0, 0, 6, 3)))

print("Test 2 (b6 k=1 negative b1):")
print("  ", s.bauer_orbit_membership((-1, 0, 0, -6, -3)))

print("Test 3 (b1=5 NOT on orbit even with k=1 a2):")
print("  ", s.bauer_orbit_membership((-1, 0, 0, 5, 3)))

print("Test 4 (b7 singular outlier (8,-4,0,7,4) NOT on orbit):")
print("  ", s.bauer_orbit_membership((8, -4, 0, 7, 4)))

print("Test 5 (b1=12 k=2 should be on orbit):")
print("  ", s.bauer_orbit_membership((-4, 0, 0, 12, 6)))

# Test 6: enumeration count
fams = s.enumerate_families()
print(f"Test 6 (total enumerated): {len(fams)} (expect 4*60*1331 = 319,440)")

# Test 7: extract_n_over_log2_v2 on synthetic record
synthetic = {"relation": [-2, 0, 0, 0, 0, 0, 0, 1]}
print("Test 7 (synthetic n=2 relation):", s.extract_n_over_log2_v2(synthetic))

synthetic2 = {"relation": [-3, 0, 0, 0, 0, 0, 0, 1]}
print("Test 8 (synthetic n=3 relation):", s.extract_n_over_log2_v2(synthetic2))

synthetic3 = {"relation": [-2, 0, 1, 0, 0, 0, 0, 1]}
print("Test 9 (rejects pi-using relation):", s.extract_n_over_log2_v2(synthetic3))

print("Test 10 (b6 trans-stratum-proper a2=-8):",
      s.discriminant_identity_class((-8, 0, 0, 6, 0)))

print("Test 11 (b8 brouncker-boundary 4*a2-64=0 => a2=16):",
      s.discriminant_identity_class((16, 0, 0, 8, 0)))

print("Test 12 (b9 trans-stratum-proper 9*a2+162=0 => a2=-18):",
      s.discriminant_identity_class((-18, 0, 0, 9, 0)))

# Test 13: a single Stage A run on known b6 Bauer orbit hit
print("Test 13 (b6 Bauer-orbit (-1,0,0,6,3) Stage A converge_float):")
import time
t0 = time.time()
L = s.stage_a_converge_float((-1, 0, 0, 6, 3))
dt = time.time() - t0
print(f"  L_float = {L}, dt = {dt*1000:.1f} ms")

# Quick speed estimate
print("Test 14 (timing estimate for 1000 Stage A calls on b1=5 random coeffs):")
import random
random.seed(42)
t0 = time.time()
for _ in range(1000):
    a2 = random.choice([a for a in range(-30, 31) if a != 0])
    a1 = random.choice(range(-5, 6))
    a0 = random.choice(range(-5, 6))
    b0 = random.choice(range(-5, 6))
    s.stage_a_converge_float((a2, a1, a0, 5, b0))
dt = time.time() - t0
print(f"  1000 calls, {dt:.2f} s, {dt/1000*1000:.2f} ms/call")
print(f"  Est. total Stage A wall: {dt * 319.44:.0f} s = {dt*319.44/60:.1f} min")

print("ALL SMOKE TESTS DONE")
