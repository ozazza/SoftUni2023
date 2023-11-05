wagons = [0] * int(input())

while True:
    command = input().split()

    if command[0] == 'End':
        print(wagons)
        break

    if command[0] == 'add':
        wagons[-1] += int(command[1])
    else:
        index = int(command[1])
        people = int(command[2])

        if command[0] == 'insert':
            wagons[index] += people

        elif command[0] == 'leave':
            wagons[index] -= people
