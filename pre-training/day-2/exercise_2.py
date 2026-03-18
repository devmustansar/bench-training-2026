# =============================================================
# Exercise 2 — Grade Book System
# =============================================================

students = [
    {"name": "Mustansar", "scores": [88, 92, 79, 95, 85], "subject": "Python"},
    {"name": "Ayesha",    "scores": [72, 68, 74, 70, 76], "subject": "Data Science"},
    {"name": "Bilal",     "scores": [55, 60, 52, 58, 63], "subject": "Web Dev"},
    {"name": "Sana",      "scores": [91, 95, 98, 93, 97], "subject": "ML"},
    {"name": "Hamza",     "scores": [80, 83, 78, 82, 81], "subject": "DevOps"},
]

def calculate_average(scores: list[int | float]) -> float:
    return sum(scores) / len(scores)

def get_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def class_topper(students: list[dict]) -> dict:
    return max(students, key=lambda s: calculate_average(s["scores"]))


topper = class_topper(students)
sorted_students = sorted(
    students,
    key=lambda s: calculate_average(s["scores"]),
    reverse=True,
)

col_name    = 12
col_subject = 14
col_avg     = 9
col_grade   = 7

header = (
    f"{'Name':<{col_name}} {'Subject':<{col_subject}} "
    f"{'Average':>{col_avg}} {'Grade':>{col_grade}}"
)
divider = "─" * len(header)

print(divider)
print(header)
print(divider)

for student in sorted_students:
    avg   = calculate_average(student["scores"])
    grade = get_grade(avg)
    tag   = "  ★ TOP" if student["name"] == topper["name"] else ""
    row   = (
        f"{student['name']:<{col_name}} {student['subject']:<{col_subject}} "
        f"{avg:>{col_avg}.2f} {grade:>{col_grade}}{tag}"
    )
    print(row)

print(divider)
