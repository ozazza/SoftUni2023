nums = int(input())

positives = []
negatives = []

for i in range(nums):
    n = int(input())

    if n >= 0:
        positives.append(n)
    else:
        negatives.append(n)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')
