qty = int(input())
days_left = int(input())

ornament_price = 2
tree_skirt_price = 5
tree_garland = 3
tree_lights = 15

total_price = 0
spirit = 0
for day in range(1, days_left + 1):

    if day % 11 == 0:
        qty += 2

    if day % 2 == 0:
        total_price += ornament_price * qty
        spirit += 5

    if day % 3 == 0:
        total_price += (tree_skirt_price + tree_garland) * qty
        spirit += 13

    if day % 5 == 0:
        total_price += tree_lights * qty
        spirit += 17
        if day % 3 == 0:
            spirit += 30

    if day % 10 == 0:
        spirit -= 20
        total_price += tree_skirt_price + tree_garland + tree_lights

        if day == days_left:
            spirit -= 30


print(f'Total cost: {total_price}')
print(f'Total spirit: {spirit}')
