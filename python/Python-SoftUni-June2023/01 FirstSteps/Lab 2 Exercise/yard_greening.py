square_meters = float(input())

price_per_meter = 7.61
discount = 0.18

price = square_meters * price_per_meter
price_discounted = price * discount
price_final = price - price_discounted

print(f'The final price is: {price_final} lv.')
print(f'The discount is: {price_discounted} lv.')