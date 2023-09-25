lines = int(input())

unicode_sum = 0
for i in range(lines):
    line = input()
    unicode_sum += ord(line)

print(f'The sum equals: {unicode_sum}')
