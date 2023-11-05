time_line = input().split(' ')

middle = int(len(time_line) / 2)
left_time = time_line[:middle]
right_time = time_line[middle + 1:]

left_sum = 0
right_sum = 0
for i in range(len(left_time)):
    left_sum += int(left_time[i])
    if int(left_time[i]) == 0:
        left_sum *= 0.8

for r in range(len(right_time) - 1, -1, -1):
    right_sum += int(right_time[r])
    if int(right_time[r]) == 0:
        right_sum *= 0.8

if left_sum < right_sum:
    winner = 'left'
    total = left_sum
else:
    winner = 'right'
    total = right_sum

print(f'The winner is {winner} with total time: {total:.1f}')
