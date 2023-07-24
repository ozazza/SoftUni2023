# Input
pastry_name = input()
pastry_count = int(input())
day = int(input())

# Logic
cake = 'Cake'
souffle = 'Souffle'
baklava = 'Baklava'
pastry_price = 0.0
discount = 0.0

if pastry_name == cake:
    if day <= 15:
        pastry_price = 24
    else:
        pastry_price = 28.7
elif pastry_name == souffle:
    if day <= 15:
        pastry_price = 6.66
    else:
        pastry_price = 9.8
elif pastry_name == baklava:
    if day <= 15:
        pastry_price = 12.60
    else:
        pastry_price = 16.98

price = pastry_price * pastry_count

if day <= 22:
    if 100 <= price <= 200:
        discount = 0.15
    elif price > 200:
        discount = 0.25

    discount = discount * price
    price -= discount

if day <= 15:
    extra_discount = 0.1 * price
    price -= extra_discount

# Output
print(f'{price:.2f}')
