numbers = list()
notes = list()
tasks = list()

while True:
    command = input()

    if command == 'End':
        numbers.sort()

        for num in numbers:
            for n in notes:
                cmnd = n.split('-')
                imp = int(cmnd[0])

                if num == imp:
                    task = cmnd[1]
                    tasks.append(task)
                    break

        break

    note = command.split('-')
    importance = int(note[0])

    numbers.append(importance)
    notes.append(command)

print(tasks)
