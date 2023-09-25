numbers = []
total = 0

for n in range(4):
    numbers.append(int(input()))

sum_num = numbers[0] + numbers[1]
total = int(sum_num / numbers[2]) * numbers[3]

print(total)
