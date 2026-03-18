# =============================================================
# Exercise 3 — Loop That Builds Something
# =============================================================

VALID_MIN = 1
VALID_MAX = 12
COL_WIDTH = 4

def print_table(n: int) -> None:
    print(f"\n{'─' * 28}")
    print(f"  Multiplication Table for {n}")
    print(f"{'─' * 28}")
    for i in range(VALID_MIN, VALID_MAX + 1):
        product = n * i
        print(f"  {n:>{COL_WIDTH}} × {i:>{COL_WIDTH}} = {product:>{COL_WIDTH}}")
    print(f"{'─' * 28}")

print("=== Single Table Mode ===")
while True:
    raw = input(f"Enter a number between {VALID_MIN} and {VALID_MAX}: ").strip()

    if not raw.lstrip("-").isdigit():
        print(f"  ✗  '{raw}' is not a whole number. Please try again.\n")
        continue

    number = int(raw)
    if VALID_MIN <= number <= VALID_MAX:
        print_table(number)
        break
    else:
        print(
            f"  ✗  {number} is outside the range {VALID_MIN}–{VALID_MAX}. "
            "Please try again.\n"
        )

print("\n\n=== Bonus: All Tables (1–12) ===")
for n in range(VALID_MIN, VALID_MAX + 1):
    print_table(n)
