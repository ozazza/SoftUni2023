from collections import deque
from datetime import datetime, time, timedelta

robots = {}
for r in input().split(';'):
    name, work_duration = r.split('-')
    robots[name] = [int(work_duration), 0]

time_start_producing = datetime.strptime(input(), '%H:%M:%S')
product_line = deque()

command = ''
while True:
    command = input()
    if command == 'End':
        break

    product_line.append(command)

# this while counts the seconds and manage robots
while product_line:
    time_start_producing += timedelta(0, 1)
    product = product_line.popleft()

    free_robots = []
    for name, value in robots.items():
        if value[1] != 0:
            value[1] -= 1   # {'ROB': [15, 15 - 1]}

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        product_line.append(product)
        continue

    robot_name, robot_times = free_robots[0]    # {'ROB': [15, 0]}
    robots[robot_name][1] = robot_times[0]  # {'ROB': [15, 15]} robot starts producing

    print(f'{robot_name} - {product} [{time_start_producing.strftime("%H:%M:%S")}]')
