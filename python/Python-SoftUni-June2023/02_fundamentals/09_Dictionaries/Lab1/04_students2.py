students = []
course_search = ""

while True:

    user_input = input()
    if ":" not in user_input:
        course_search = user_input
        break

    name, student_id, student_course = user_input.split(":")
    student_id = int(student_id)

    students.append({'name': name, 'id': student_id, 'course': student_course})

for student in students:
    if course_search.split("_")[0] in student['course']:
        print(f"{student['name']} - {student['id']}")
