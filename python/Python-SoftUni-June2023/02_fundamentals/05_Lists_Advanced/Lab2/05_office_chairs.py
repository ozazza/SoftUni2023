total_rooms = int(input())

rooms = []
chairs = []
visitors = []
left_chairs = []

for r in range(total_rooms):
    info = input().split()
    i_chairs = len(info[0])
    i_visitors = int(info[1])

    rooms.append(r)
    left_chairs.append(i_chairs - i_visitors)

free_chairs = sum(left_chairs)

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')
else:
    for room in range(len(rooms)):
        if left_chairs[room] < 0:
            needed_chairs = abs(left_chairs[room])

            print(f'{needed_chairs} more chairs needed in room {room + 1}')
