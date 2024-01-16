from collections import deque

pumps = int(input())

path = deque()
tank = 0
for pump_nr in range(pumps):
    data = [int(x) for x in input().split()]
    petrol = data[0]
    distance = data[1]

    if petrol >= distance or tank + petrol >= distance:
        data.append(pump_nr)
        path.append(data)
        tank += petrol - distance
    else:
        # restart the path of the truck
        path = deque()
        tank = 0

truck_start = path.popleft()
print(truck_start[2])
