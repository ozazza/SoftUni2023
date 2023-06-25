# Input
num_weekday = int(input())
result = ''

# Logic
if num_weekday == 1:
    result = 'Monday'
elif num_weekday == 2:
    result = 'Tuesday'
elif num_weekday == 3:
    result = 'Wednesday'
elif num_weekday == 4:
    result = 'Thursday'
elif num_weekday == 5:
    result = 'Friday'
elif num_weekday == 6:
    result = 'Saturday'
elif num_weekday == 7:
    result = 'Sunday'
else:
    result = 'Error'

# Output
print(result)
