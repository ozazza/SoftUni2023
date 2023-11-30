counter = 0
collector = {}
while True:
    sequence = input()

    if sequence == 'stop':
        break

    counter += 1

    if counter % 2 != 0:
        resource = sequence
    else:
        if resource not in collector.keys():
            collector[resource] = int(sequence)
        else:
            collector[resource] += int(sequence)

for product, qty in collector.items():
    print(f'{product} -> {qty}')

