statistics = dict()

while True:
    command = input()
    if command == "statistics":
        break

    pairs_input = command.split(": ")
    key = pairs_input[0]
    value = pairs_input[1]

    if key in statistics:
        statistics[key] += int(value)
    else:
        statistics[key] = int(value)

print("Products in stock:")

total_products = 0
total_qty = 0
for k, v in statistics.items():
    print(f"- {k}: {v}")
    total_products += 1
    total_qty += v

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_qty}")
