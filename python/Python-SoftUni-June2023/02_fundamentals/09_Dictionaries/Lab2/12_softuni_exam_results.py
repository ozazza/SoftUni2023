results = {}
submissions = {}
while True:
    command = input()
    if command == 'exam finished':
        break

    if len(command.split('-')) == 3:
        user, language, exam_points = command.split('-')
        points = int(exam_points)

        if user not in results.keys():
            results[user] = 0
        if results[user] < points:
            results[user] = points

        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

    elif len(command.split('-')) == 2:
        user, status = command.split('-')
        del results[user]

print('Results:')
for name, points in results.items():
    print(f'{name} | {points}')

print('Submissions:')
for lang, sub_count in submissions.items():
    print(f'{lang} - {sub_count}')
