packs_pens = int(input())
packs_markers = int(input())
liters_chemicals =int(input())
discount_percentile = int(input()) / 100

price_pens = packs_pens * 5.80
price_markers = packs_markers * 7.20
price_chems = liters_chemicals * 1.20

price = price_pens + price_markers + price_chems
discount_amount = price * discount_percentile
total_price = price - discount_amount

print(total_price)