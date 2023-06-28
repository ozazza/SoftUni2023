# Input
month = input()
nights = int(input())

studio = 0
apartment = 0
studio_discount = 0
apart_discount = 0
studio_amt = 0
apart_amt = 0

# Logic
if month == 'May' or month == 'October':
    studio = 50
    apartment = 65

    if 7 < nights < 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.3

elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7

    if nights > 14:
        studio_discount = 0.2

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

if nights > 14:
    apart_discount = 0.10

studio_amt = studio * nights
studio_discount *= studio_amt
studio_amt -= studio_discount

apart_amt = apartment * nights
apart_discount *= apart_amt
apart_amt -= apart_discount

# Output
print(f'Apartment: {apart_amt:.2f} lv.')
print(f'Studio: {studio_amt:.2f} lv.')
