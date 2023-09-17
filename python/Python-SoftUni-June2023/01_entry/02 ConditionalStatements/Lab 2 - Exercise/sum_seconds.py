# Read user input
first_racer = int(input())
second_racer = int(input())
third_racer = int(input())

# Logic
seconds = first_racer + second_racer + third_racer
minutes = seconds // 60
left_seconds = seconds % 60

# Print output
# print(minutes)
# print(left_seconds)

# print(f'{minutes:02d}:{left_seconds:02d}')

# minutes_str = str(minutes)
# if 0 <= minutes < 10:
#     minutes_str = '0' + str(minutes)
#
# print(f'{minutes_str}:{left_seconds:02}')

# if left_seconds <= 9:
#     print(f'{minutes}:{left_seconds:02d}')
# else:
#     print(f'{minutes}:{left_seconds}')

print(f'{minutes}:{left_seconds:02}')
