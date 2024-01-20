from collections import deque

cups_capacity = deque([int(x) for x in input().split(' ')])
bottle_capacity = deque([int(x) for x in input().split(' ')])

wasted_water = 0
while cups_capacity:

    current_cup_liters = cups_capacity[0]
    while bottle_capacity:
        filled_cup = 0
        current_bottle_litters = bottle_capacity.pop()

        filled_cup = current_cup_liters - current_bottle_litters
        current_bottle_litters = 0
        if filled_cup == 0:
            cups_capacity.popleft()
            break
        elif filled_cup < 0:
            cups_capacity.popleft()
            wasted_water += abs(filled_cup)
            break
        elif filled_cup > 0:
            current_cup_liters = filled_cup
            continue

    if not bottle_capacity:
        print(f'Cups:', *cups_capacity)
        break
    if not cups_capacity:
        print(f'Bottles:', *bottle_capacity)
        break

print(f'Wasted litters of water: {wasted_water}')
