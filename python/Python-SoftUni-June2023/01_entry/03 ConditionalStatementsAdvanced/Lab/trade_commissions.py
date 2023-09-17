# Input
town = input()
sales = float(input())

commission = 0

# Logic
if 0 <= sales <= 500:
    if town == 'Sofia':
        commission = 0.05
    elif town == 'Varna':
        commission = 0.045
    elif town == 'Plovdiv':
        commission = 0.055
elif 500 < sales <= 1000:
    if town == 'Sofia':
        commission = 0.07
    elif town == 'Varna':
        commission = 0.075
    elif town == 'Plovdiv':
        commission = 0.08
elif 1000 < sales <= 10000:
    if town == 'Sofia':
        commission = 0.08
    elif town == 'Varna':
        commission = 0.10
    elif town == 'Plovdiv':
        commission = 0.12
elif sales > 10000:
    if town == 'Sofia':
        commission = 0.12
    elif town == 'Varna':
        commission = 0.13
    elif town == 'Plovdiv':
        commission = 0.145

# Output
if commission > 0:
    commission *= sales
    print(f'{commission:.2f}')
else:
    print('error')
