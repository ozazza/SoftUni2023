nums = input().split(', ')
group = 0

while len(nums) > 0:
    group += 10
    group_list = [x for x in nums if int(x) <= group]

    print(f"Group of {group}'s: {[int(z) for z in group_list.copy()]}")

    for i in group_list:
        nums.remove(i)
