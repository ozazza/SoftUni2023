chicken = int(input())
fish = int(input())
vegetarian = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.4
veg_price = vegetarian * 8.15

price = chicken_price + fish_price + veg_price
dessert = price * 0.2
delivery = 2.5

total_price = price + dessert + delivery

print(total_price)