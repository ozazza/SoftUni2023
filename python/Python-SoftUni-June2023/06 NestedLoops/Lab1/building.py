# Input
floors = int(input())
rooms_per_floor = int(input())

# Logic
for floor in range(floors, 0, -1):
    for room in range(rooms_per_floor):

        room_letter = ''
        if floor == floors:
            room_letter = 'L'
        elif floor % 2 != 0:
            room_letter = 'A'
        else:
            room_letter = 'O'

        print(f'{room_letter}{floor}{room}', end=' ')

    print()
