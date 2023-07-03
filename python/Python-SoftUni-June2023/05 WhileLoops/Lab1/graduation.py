# Input
student = input()

# Logic
next_class = 1
total_grade = 0
average_grade = 0
failed = 0

while True:
    grade = float(input())

    if grade < 4:
        failed += 1

        if failed == 2:
            # suspended = True
            print(f'{student} has been excluded at {next_class} grade')
            break

        continue

    next_class += 1
    total_grade += grade

    if next_class > 12:

        average_grade = total_grade / (next_class - 1)

        print(f'{student} graduated. Average grade: {average_grade:.2f}')
        break

# # Input
# student = input()
#
# # Logic
# next_class_counter = 1
# class_pass = 0
# total_grade = 0
# average_grade = 0
# failed = 0
#
# while True:
#     grade = float(input())
#
#     if grade < 4:
#         failed += 1
#
#         if failed == 2:
#             # suspended = True
#             print(f'{student} has been excluded at {next_class_counter} grade')
#             break
#
#         continue
#
#     class_pass += 1
#     next_class_counter = class_pass + 1
#     total_grade += grade
#
#     if class_pass == 12:
#
#         average_grade = total_grade / 12
#
#         print(f'{student} graduated. Average grade: {average_grade:.2f}')
#         break
