pair_rows = int(input())

journal = {}
grades = 'grades'
avg = 'avg_grade'

for pair in range(pair_rows):
    name = input()
    grade = float(input())

    if name not in journal:
        journal[name] = {grades: [], avg: 0.0}

    journal[name][grades].append(grade)
    journal[name][avg] = sum(journal[name][grades]) / len(journal[name][grades])

for st_name, details in journal.items():
    student_avg = details[avg]

    if student_avg >= 4.5:
        print(f'{st_name} -> {student_avg:.2f}')
