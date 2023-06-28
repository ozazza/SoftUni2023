# Input
flowers = input()
number = int(input())
budget = float(input())

discount = 0
amount = 0
total = 0

# Logic
if flowers == 'Roses':
    amount = number * 5
    if number > 80:
        discount = amount * 0.1

    total = amount - discount

elif flowers == 'Tulips':
    amount = number * 2.8
    if number > 80:
        discount = amount * 0.15

    total = amount - discount

elif flowers == 'Dahlias':
    amount = number * 3.8
    if number > 90:
        discount = amount * 0.15

    total = amount - discount

elif flowers == 'Narcissus':
    amount = number * 3
    if number < 120:
        discount = amount * 0.15

    total = amount + discount

elif flowers == 'Gladiolus':
    amount = number * 2.5
    if number < 80:
        discount = amount * 0.2

    total = amount + discount

# Output
if budget >= total:
    print(f'Hey, you have a great garden with {number} {flowers} and {(budget-total):.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(budget-total):.2f} leva more.')
