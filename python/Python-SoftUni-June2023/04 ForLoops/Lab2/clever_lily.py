# Input
lily_years = int(input())
machine_price = float(input())
toy_price = int(input())
amount = 0
b_day_amount = 10
brother = 0
toy_count = 0

# Logic
for year in range(1, lily_years + 1):

    if year >= 2 and year % 2 == 0:
        amount += b_day_amount
        b_day_amount += 10
        amount -= 1
        brother += 1

    if year % 2 != 0:
        toy_count += 1

toys_amount = toy_count * toy_price
amount_total = amount + toys_amount
amount_left = amount_total - machine_price

# Output
if amount_left >= 0:
    print(f'Yes! {amount_left:.2f}')

else:
    print(f'No! {abs(amount_left):.2f}')
