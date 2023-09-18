orders = int(input())

total_price = 0
for order in range(0, orders):

    price = float(input())
    days = int(input())
    caps_day = int(input())

    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= caps_day <= 2000:

        order_price = price * days * caps_day
        print(f'The price for the coffee is: ${order_price:.2f}')

        total_price += order_price
    else:
        continue

print(f'Total: ${total_price:.2f}')
