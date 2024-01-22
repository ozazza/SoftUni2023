n = int(input())

longest_intersection = set()
for _ in range(n):
    first, second = [x.split(',') for x in input().split('-')]
    first_set = set(range(int(first[0]), int(first[1]) + 1))
    second_set = set(range(int(second[0]), int(second[1]) + 1))

    intersection = first_set.intersection(second_set)  # first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f'Longest intersection is '
    f'[{", ".join(str(x) for x in longest_intersection)}] with length '
    f'{len(longest_intersection)}'
)
