register = {}
while True:
    command = input()
    if command == 'End':
        break

    company, id = command.split(' -> ')

    if company not in register.keys():
        register[company] = []
        register[company].append(id)

    elif company in register.keys() and id not in register[company]:
        register[company].append(id)

for c, e in register.items():
    print(f'{c}')
    for emp in e:
        print(f'-- {emp}')
