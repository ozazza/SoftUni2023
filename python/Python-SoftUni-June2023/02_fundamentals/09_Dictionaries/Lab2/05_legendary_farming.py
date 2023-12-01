legendary_item = ''
possible_items = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}

item_obtained = False
while True:

    materials = input().lower().split()

    for m in range(1, len(materials), 2):
        item = materials[m]
        qty = int(materials[m - 1])

        if item not in possible_items.keys():
            possible_items[item] = 0
        possible_items[item] += qty

        shadowmourne_obtained = possible_items['shards'] >= 250
        valanyr_obtained = possible_items['fragments'] >= 250
        dragonwrath_obtained = possible_items['motes'] >= 250

        if shadowmourne_obtained:
            legendary_item = 'Shadowmourne'
            possible_items['shards'] -= 250
            item_obtained = True
            break
        elif valanyr_obtained:
            legendary_item = 'Valanyr'
            possible_items['fragments'] -= 250
            item_obtained = True
            break
        elif dragonwrath_obtained:
            legendary_item = 'Dragonwrath'
            possible_items['motes'] -= 250
            item_obtained = True
            break

    if item_obtained:
        break

print(f'{legendary_item} obtained!')

for k, v in possible_items.items():
    print(f'{k}: {v}')
