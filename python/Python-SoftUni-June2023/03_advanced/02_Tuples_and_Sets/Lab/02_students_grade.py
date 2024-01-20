n = int(input())

student_grades = {}
for _ in range(n):
    name, grade_str = tuple(input().split())
    grade = float(grade_str)

    if name not in student_grades:
        student_grades[name] = []

    student_grades[name].append(grade)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    grade_formatted = f'{" ".join([f"{x:.2f}" for x in grades])}'

    print(f'{name} -> {grade_formatted} (avg: {avg_grade:.2f})')
