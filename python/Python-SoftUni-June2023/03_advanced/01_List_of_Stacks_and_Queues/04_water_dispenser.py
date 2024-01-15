from collections import deque

water = int(input())

command = ''
second_command = ''
names = deque()

while True:
    command = input()
    if command == 'Start':
        break

    names.append(command)

while True:
    second_command = input()
    if second_command == 'End':
        break

    if 'refill' in second_command:
        litters_to_refill = int(second_command.split()[1])
        water += litters_to_refill
    else:
        litters_for_current_name = int(second_command)
        name = names.popleft()

        if water >= litters_for_current_name:
            water -= litters_for_current_name
            print(f'{name} got water')
        else:
            print(f'{name} must wait')

print(f'{water} liters left')
