# =============================================================
# Exercise 1 — Data Types + Operators
# =============================================================

name          = "Mustansar"
age           = 35
drinks_coffee = True
salary        = 85_000.0      # PKR per month

intro = (
    f"Hi, I'm {name}. "
    f"I'm {age} years old, "
    f"{'a coffee drinker' if drinks_coffee else 'not a coffee drinker'}, "
    f"and my monthly salary is Rs. {salary:,.2f}."
)
print(intro)

retirement_age    = 60
years_to_retire   = retirement_age - age
print(f"\nYears until retirement (at {retirement_age}): {years_to_retire} year(s)")

cups_per_day       = 3
price_per_cup      = 150        # PKR
days_in_a_week     = 7

if drinks_coffee:
    weekly_coffee_budget = cups_per_day * price_per_cup * days_in_a_week
    print(
        f"Weekly coffee budget ({cups_per_day} cups/day × "
        f"Rs. {price_per_cup} each × {days_in_a_week} days): "
        f"Rs. {weekly_coffee_budget:,}"
    )
else:
    print("No coffee budget — you don't drink coffee!")
