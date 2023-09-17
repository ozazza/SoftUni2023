# Input
food_kg = int(input())

# Logic
food_gr = food_kg * 1000
food_need = 0

while True:
    feed = input()

    if feed == 'Adopted':
        break

    food_need += int(feed)

food_left = food_gr - food_need

# Output
if food_left >= 0:
    print(f'Food is enough! Leftovers: {food_left} grams.')
else:
    print(f'Food is not enough. You need {abs(food_left)} grams more.')
