# Input
budget = int(input())
season = input()
fisherman = int(input())

spring_boat = 3000
summer_autumn_boat = 4200
winter_boat = 2600

group_6 = 10 / 100
group_7_11 = 15 / 100
group_12_above = 25 / 100
discount_even_not_autumn = 5 / 100

discount = 0
price = 0
total_amount = 0
amount_left = 0

# Logic
if season == 'Spring':
    price = spring_boat
elif season == 'Summer' or season == 'Autumn':
    price = summer_autumn_boat
elif season == 'Winter':
    price = winter_boat

if 0 < fisherman <= 6:
    discount = group_6
elif 6 < fisherman <= 11:
    discount = group_7_11
elif fisherman >= 12:
    discount = group_12_above

discount *= price
total_amount = price - discount

if fisherman % 2 == 0 and season != 'Autumn':
    discount_even_not_autumn *= total_amount
    total_amount -= discount_even_not_autumn

amount_left = budget - total_amount

# Output
if amount_left >= 0:
    print(f'Yes! You have {amount_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(amount_left):.2f} leva.')
