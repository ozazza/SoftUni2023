# Input
last_record = float(input())
distance = float(input())
time_per_meter = float(input())

# Logic
time_delays = (distance // 15) * 12.5
time_distance = distance * time_per_meter

time_total = time_distance + time_delays
difference_time = abs(time_total - last_record)

# Output
if time_total < last_record:
    print(f'Yes, he succeeded! The new world record is {time_total:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference_time:.2f} seconds slower.')
