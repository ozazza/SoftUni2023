# Input
exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())

status = ''
diff_minutes = 0
hours = 0
minutes = 0

# Logic
# Convert times to minutes
arrive_to_min = (arrive_h * 60) + arrive_m
exam_maximum_to_min = (exam_h * 60) + exam_m
exam_minimum_to_min = exam_maximum_to_min - 30

# Calculate Difference
diff_minutes = arrive_to_min - exam_maximum_to_min

# Determine the Statuses
if diff_minutes > 0:
    status = 'Late'
elif exam_minimum_to_min <= arrive_to_min <= exam_maximum_to_min:
    status = 'On time'
elif exam_minimum_to_min > arrive_to_min:
    status = 'Early'

# Calculate hours and minutes
hours = abs(int(diff_minutes / 60))
# hours2 = abs(diff_minutes / 60)

minutes = abs(diff_minutes / 60) + abs(diff_minutes % 60)

# Output
print(status)

if diff_minutes != 0:

    if abs(diff_minutes) < 60:
        print(f'{abs(diff_minutes)} minutes', end=' ')

    elif abs(diff_minutes) >= 60:
        print(f'{hours}:{minutes:02d} hours', end=' ')

    if diff_minutes < 0:
        print(f'before the start')
    elif diff_minutes > 0:
        print(f'after the start')
