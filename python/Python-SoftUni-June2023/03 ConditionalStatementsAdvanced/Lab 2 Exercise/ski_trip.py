# Input
trip_days = int(input())
place = input()
review = input()

room = 18
apartment = 25
apartment_lux = 35
nights = trip_days - 1

discount = 0
review_discount = 0
trip_price = 0

# Logic
if place == 'room for one person':
    trip_price = nights * room

elif place == 'apartment':
    trip_price = nights * apartment

    if nights < 10:
        discount = 0.3
    if 10 < nights <= 15:
        discount = 0.35
    if nights > 15:
        discount = 0.5

if place == 'president apartment':
    trip_price = nights * apartment_lux

    if nights < 10:
        discount = 0.1
    if 10 < nights <= 15:
        discount = 0.15
    if nights > 15:
        discount = 0.2

discount *= trip_price
trip_price -= discount

if review == 'positive':
    review_discount = trip_price * 0.25
    trip_price += review_discount
else:
    review_discount = trip_price * 0.1
    trip_price -= review_discount

# Output
print(f'{trip_price:.2f}')
