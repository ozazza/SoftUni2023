nums_string = input().split()
n = int(input())

nums = list()
for k in range(len(nums_string)):
    nums.append(int(nums_string[k]))

for i in range(n):
    index_min = nums.index(min(nums))
    nums.pop(index_min)

for p in range(len(nums)):
    if p != len(nums) - 1:
        print(f'{nums[p]}', end=', ')
    else:
        print(nums[p])


