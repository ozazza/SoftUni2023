from math import ceil

# Input
name = input()
budget = float(input())
beer_bottles = int(input())
chips_packs = int(input())

# Logic
beer_price = 1.2 * beer_bottles
chips_price = ceil(beer_price * 0.45 * chips_packs)
total_price = beer_price + chips_price
budget_left = budget - total_price

# Output
if budget_left >= 0:
    print(f'{name} bought a snack and has {budget_left:.2f} leva left.')
else:
    print(f'{name} needs {abs(budget_left):.2f} more leva!')
