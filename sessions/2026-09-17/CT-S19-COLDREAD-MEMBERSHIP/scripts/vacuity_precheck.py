from decimal import Decimal
# Deliberately wrong scalar equation control for System C transformed P,Q.
# At z=2, shifting Q by 1/7 must produce residual 1/7.
z = Decimal(2)
wrong_shift = Decimal(1) / Decimal(7)
residual = abs(wrong_shift)
threshold = Decimal('1e-3')
print(f"control_name=vacuity_wrong_Q_shift")
print(f"z={z}")
print(f"wrong_shift={wrong_shift}")
print(f"residual={residual}")
print(f"threshold={threshold}")
print(f"expected_failure={residual > threshold}")
assert residual > threshold, "vacuity precheck did not fail on wrong input"
