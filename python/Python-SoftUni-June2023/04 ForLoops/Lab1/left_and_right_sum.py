# Input
n = int(input())

# Logic
sum1 = 0
sum2 = 0

for i in range(1, (2 * n) + 1):
    number = int(input())

    if i <= n:
        sum1 += number
    else:
        sum2 += number

# Output
if sum1 == sum2:
    print(f'Yes, sum = {sum1}')
else:
    print(f'No, diff = {abs(sum1 - sum2)}')
