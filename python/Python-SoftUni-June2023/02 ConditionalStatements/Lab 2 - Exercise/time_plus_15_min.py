# Input
num_hour = int(input())
num_minutes = int(input())

min_15 = 15

# Logic
hour = num_hour
minutes = num_minutes + min_15

if num_minutes >= 45:
    min_left = 60 - num_minutes
    min_add = min_15 - min_left
    minutes = min_add
    hour = num_hour + 1

    if hour > 23:
        hours_after_midnight = hour - 24
        hour = hours_after_midnight

# Output
print(f'{hour}:{minutes:02}')
