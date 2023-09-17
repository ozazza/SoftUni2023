# Input
hour = int(input())
day_week = input()

weekday = 'Sunday'
workdays_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
is_work_time = 10 <= hour <= 18
office_status = 'closed'

# Logic
if is_work_time and day_week in workdays_week and day_week != weekday:
    office_status = 'open'

# Output
print(office_status)
