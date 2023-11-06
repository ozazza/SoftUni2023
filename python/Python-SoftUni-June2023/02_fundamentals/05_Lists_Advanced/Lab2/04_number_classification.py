nums = input().split(', ')

print(f'Positive: {", ".join([x for x in nums if int(x) >= 0])}')
print(f'Negative: {", ".join([x for x in nums if int(x) < 0])}')
print(f'Even: {", ".join([x for x in nums if int(x) % 2 == 0])}')
print(f'Odd: {", ".join([x for x in nums if int(x) % 2 != 0])}')
