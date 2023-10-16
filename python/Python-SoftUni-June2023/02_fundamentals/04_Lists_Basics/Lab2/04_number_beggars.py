str_numbers = input().split(', ')
count_beggars = int(input())

sums_beggars = list()
for b in range(count_beggars):

    sum_nums = 0
    for i in range(b, len(str_numbers), count_beggars):
        sum_nums += int(str_numbers[i])

    sums_beggars.append(sum_nums)

print(sums_beggars)
