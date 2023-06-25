pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_reading = pages / pages_per_hour

hours_per_day = round(hours_reading / days)

print(hours_per_day)