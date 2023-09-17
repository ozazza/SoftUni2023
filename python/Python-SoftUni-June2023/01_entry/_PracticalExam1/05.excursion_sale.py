# Input
sea = int(input())
mountain = int(input())

# Logic
sea_left = sea
mountain_left = mountain

sold_packages = 0
profit = 0

command = ''
while command != 'Stop':
    command = input()
    if command == 'Stop':
        break

    package = command
    price = 0
    if package == 'sea':
        if sea_left > 0:
            sea_left -= 1
            price = 680
            sold_packages += 1
        else:
            price = 0
    elif package == 'mountain':
        if mountain_left > 0:
            mountain_left -= 1
            price = 499
            sold_packages += 1
        else:
            price = 0

    profit += price
    if sea_left + mountain_left == 0:
        break

# Output
if sold_packages == (sea + mountain):
    print(f'Good job! Everything is sold.')

print(f'Profit: {profit} leva.')
