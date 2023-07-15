# Input
jury_count = int(input())
presentation = input()

# Logic
finish = 'Finish'
ave_final = 0
count_assessments = 0

while presentation != finish:
    sum_presentation = 0
    ave_presentation = 0

    for i in range(jury_count):
        assessment = float(input())

        count_assessments += 1
        sum_presentation += assessment

    ave_presentation = sum_presentation / jury_count
    ave_final += sum_presentation
    print(f'{presentation} - {ave_presentation:.2f}.')

    presentation = input()

# Output
ave_final /= count_assessments
print(f"Student's final assessment is {ave_final:.2f}.")
