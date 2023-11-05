numbers = input().split(' ')
nums = list()

for i in range(len(numbers)):
    s = int(numbers[i]) * -1
    nums.append(s)

print(nums)
