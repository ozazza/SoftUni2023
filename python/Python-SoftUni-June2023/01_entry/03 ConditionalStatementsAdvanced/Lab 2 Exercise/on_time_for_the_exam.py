# Input
exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())

# Logic
status = ''
hours = 0
minutes = 0

# Convert times to minutes
arrive_time_mm = (arrive_h * 60) + arrive_m
exam_time_max_mm = (exam_h * 60) + exam_m
exam_time_min_to_mm = exam_time_max_mm - 30

# Calculate Difference
diff_minutes = arrive_time_mm - exam_time_max_mm

# Determine the Statuses
if diff_minutes > 0:
    status = 'Late'
elif exam_time_min_to_mm <= arrive_time_mm <= exam_time_max_mm:
    status = 'On time'
elif exam_time_min_to_mm > arrive_time_mm:
    status = 'Early'

# Calculate hours and minutes
hours_decimal = abs(diff_minutes / 60)
hours = int(hours_decimal)

minutes_decimal = (hours_decimal - hours) * 60
minutes = round(minutes_decimal)

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
