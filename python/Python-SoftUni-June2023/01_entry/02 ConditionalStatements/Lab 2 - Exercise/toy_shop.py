# Input
trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_price = 2.6 * puzzles
dolls_price = 3 * dolls
bears_price = 4.1 * bears
minions_price = 8.2 * minions
trucks_price = 2 * trucks

# Logic
toys_count = puzzles + dolls + bears + minions + trucks
toys_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price
discount = toys_price * 25 / 100

if toys_count >= 50:
    toys_price -= discount

rent = toys_price * 10 / 100
profit = toys_price - rent
money_left = abs(profit - trip_price)

# Output
if profit >= trip_price:
    print(f'Yes! {money_left:.2f} lv left.')
else:
    print(f'Not enough money! {money_left:.2f} lv needed.')
