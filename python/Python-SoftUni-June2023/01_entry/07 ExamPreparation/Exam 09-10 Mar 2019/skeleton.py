# https://judge.softuni.bg/Contests/Practice/Index/1538#3

# Input
best_quota_min = int(input())
best_quota_sec = int(input())
chute_len_meters = float(input())
sec_100_meters = int(input())

# Logic
quota_sec = best_quota_min * 60 + best_quota_sec
person_time = chute_len_meters/100 * sec_100_meters
delay = chute_len_meters/120 * 2.5
total_person_time = person_time - delay

# Output
if total_person_time <= quota_sec:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {total_person_time:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(quota_sec - total_person_time):.3f} second slower.')
