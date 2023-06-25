# Input
day_week = input()

price_mon_tue_fri = 12
price_wed_thu = 14
price_sat_sun = 16
price = 0

# Logic
if day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Friday':
    price = price_mon_tue_fri
elif day_week == 'Wednesday' or day_week == 'Thursday':
    price = price_wed_thu
else:
    price = price_sat_sun

# Output
print(price)
