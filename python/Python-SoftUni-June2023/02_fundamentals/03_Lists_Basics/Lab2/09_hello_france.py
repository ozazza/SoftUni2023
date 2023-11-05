items = input().split('|')
budget = float(input())

train_ticket = 150.0
clothes_max_price = 50.0
shoes_max_price = 35.0
acces_max_price = 20.5

sold_prices = list()
profit = 0.0

for i in items:
    item = i.split('->')
    type_i = item[0]
    price_i = float(item[1])

    if budget >= price_i:
        cloth_is_valid = type_i == 'Clothes' and price_i <= clothes_max_price
        shoes_is_valid = type_i == 'Shoes' and price_i <= shoes_max_price
        acces_is_valid = type_i == 'Accessories' and price_i <= acces_max_price

        if cloth_is_valid or shoes_is_valid or acces_is_valid:
            budget -= price_i
            sold_prices.append(price_i * 1.4)
            profit += price_i * 0.4

print(' '.join([str(f'{price:.2f}') for price in sold_prices]))
print(f'Profit: {profit:.2f}')

if budget + sum(sold_prices) >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
