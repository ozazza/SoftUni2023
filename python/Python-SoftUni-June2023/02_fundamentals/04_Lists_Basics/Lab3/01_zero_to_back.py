nums = input().split(', ')
nums_int = list()

for i in nums:
    if i == '0':
        nums.pop(nums.index(i))
        nums.append(i)

for n in nums:
    nums_int.append(int(n))

print(nums_int)
