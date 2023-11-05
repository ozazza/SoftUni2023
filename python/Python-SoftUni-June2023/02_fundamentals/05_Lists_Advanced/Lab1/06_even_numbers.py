nums = input().split(', ')

even_nums = [x for x in range(len(nums)) if int(nums[x]) % 2 == 0]

print(even_nums)