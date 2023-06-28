# Input
budget = float(input())
season = input()

destination = ''
stay_in = 'Hotel'
amount = 0

# Logic
if season == 'summer':
    stay_in = 'Camp'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        amount = budget * 0.3
    elif season == 'winter':
        amount = budget * 0.7

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        amount = budget * 0.4
    elif season == 'winter':
        amount = budget * 0.8

elif budget > 1000:
    destination = 'Europe'
    stay_in = 'Hotel'
    amount = budget * 0.9

# Output
print(f'Somewhere in {destination}')
print(f'{stay_in} - {amount:.2f}')
