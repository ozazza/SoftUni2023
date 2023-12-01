products = {}
while True:
    command = input()
    if command == 'buy':
        break

    name, price, qty = command.split()

    if name not in products.keys():
        products[name] = {'price': 0.0, 'qty': 0}

    if products[name]['price'] != float(price):
        products[name]['price'] = float(price)

    products[name]['qty'] += int(qty)

for name, details in products.items():
    total_price = details['price'] * details['qty']
    print(f'{name} -> {total_price:.2f}')
