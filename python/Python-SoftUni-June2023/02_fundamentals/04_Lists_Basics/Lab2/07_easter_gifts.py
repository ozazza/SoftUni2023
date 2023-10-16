gifts = input().split()

while True:
    command_str = input()

    if command_str != 'No Money':
        command = command_str.split()

        if 'OutOfStock' in command:
            while command[1] in gifts:
                gifts_index = gifts.index(command[1])
                gifts[gifts_index] = 'None'

        elif 'Required' in command:
            idx = int(command[2])
            if 0 < idx < len(gifts):
                gifts[idx] = command[1]

        elif 'JustInCase' in command:
            gifts[len(gifts) - 1] = command[1]

    else:
        break

for g in gifts:
    if g != 'None':
        print(g, end=' ')
