from math import ceil

# Input
series_name = input()
series_time = int(input())
all_break_time = int(input())

# Logic
lunch_break = all_break_time / 8
personal_break = all_break_time / 4

left_break_time = all_break_time - lunch_break - personal_break
diff_time = ceil(abs(series_time - left_break_time))

# Output
if left_break_time >= series_time:
    print(f'You have enough time to watch {series_name} and left with {diff_time} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {diff_time} more minutes.")
