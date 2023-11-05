nums = int(input())

my_nums = []
for i in range(nums):
    my_nums.append(int(input()))

command = input()

for n in range(len(my_nums) - 1, -1, -1):
    if command == 'even' and int(my_nums[n]) % 2 != 0:
        my_nums.remove(my_nums[n])
    elif command == 'odd' and int(my_nums[n]) % 2 == 0:
        my_nums.remove(my_nums[n])
    elif command == 'negative' and int(my_nums[n]) >= 0:
        my_nums.remove(my_nums[n])
    elif command == 'positive' and int(my_nums[n]) < 0:
        my_nums.remove(my_nums[n])

print(my_nums)
