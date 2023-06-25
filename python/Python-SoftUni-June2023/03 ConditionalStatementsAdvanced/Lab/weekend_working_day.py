# Input
day_name = input()
result = ''

# Logic
if day_name == 'Monday' or day_name == 'Tuesday' or day_name == 'Wednesday' or day_name == 'Thursday' or day_name == 'Friday':
    result = 'Working day'
elif day_name == 'Saturday' or day_name == 'Sunday':
    result = 'Weekend'
else:
    result = 'Error'

# Output
print(result)