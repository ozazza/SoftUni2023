# Input
budget = float(input())
extra_persons = int(input())
clothing_price = float(input())

# Logic
decor = budget * 0.1
total_clothing_price = extra_persons * clothing_price
discount = total_clothing_price * 0.1

if extra_persons > 150:
    total_clothing_price -= discount

money = abs((decor + total_clothing_price) - budget)

# Output
if (decor + total_clothing_price) > budget:

    print('Not enough money!')
    print(f'Wingard needs {money:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money:.2f} leva left.')
