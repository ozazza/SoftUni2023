# Input
product = input()
town = input()
qty = float(input())

coffee_sofia = 0.5
coffee_plovdiv = 0.4
coffee_varna = 0.45

water_sofia = 0.8
water_plovdiv = 0.7
water_varna = 0.7

beer_sofia = 1.2
beer_plovdiv = 1.15
beer_varna = 1.1

sweets_sofia = 1.45
sweets_plovdiv = 1.3
sweets_varna = 1.35

peanuts_sofia = 1.6
peanuts_plovdiv = 1.5
peanuts_varna = 1.55

price = 0
result = 0

# Logic
if product == 'coffee':
    if town == 'Sofia':
        price = coffee_sofia
    elif town == 'Plovdiv':
        price = coffee_plovdiv
    elif town == 'Varna':
        price = coffee_varna
elif product == 'water':
    if town == 'Sofia':
        price = water_sofia
    elif town == 'Plovdiv':
        price = water_plovdiv
    elif town == 'Varna':
        price = water_varna
elif product == 'beer':
    if town == 'Sofia':
        price = beer_sofia
    elif town == 'Plovdiv':
        price = beer_plovdiv
    elif town == 'Varna':
        price = beer_varna
elif product == 'sweets':
    if town == 'Sofia':
        price = sweets_sofia
    elif town == 'Plovdiv':
        price = sweets_plovdiv
    elif town == 'Varna':
        price = sweets_varna
elif product == 'peanuts':
    if town == 'Sofia':
        price = peanuts_sofia
    elif town == 'Plovdiv':
        price = peanuts_plovdiv
    elif town == 'Varna':
        price = peanuts_varna

if price > 0:
    result = price * qty

# Output
print(result)