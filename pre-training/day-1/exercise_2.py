# =============================================================
# Exercise 2 — Control Flow That Does Something Real
# =============================================================

def grade_classifier(score: int | float) -> str:
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

print("── Manual test cases ──────────────────────────────")
test_values = [100, 90, 89, 60, 59]
for val in test_values:
    print(f"  score={val:>3}  →  {grade_classifier(val)}")

scores = [45, 72, 91, 60, 38, 85]

print("\n── Batch results ──────────────────────────────────")
for score in scores:
    result = grade_classifier(score)
    print(f"  score={score:>3}  →  {result}")
