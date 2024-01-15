from collections import deque

# nums = deque(input().split())
#
# for _ in range(len(nums)):
#     print(nums.pop(), end=' ')

nums = deque(input().split())
nums.reverse()

# * means unpack
print(*nums)
