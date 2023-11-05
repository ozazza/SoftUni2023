def sort_sequence_numbers_asc(sequence):
    sort_asc = sorted(sequence)

    return sort_asc


numbers = input().split(' ')
nums = [int(x) for x in numbers.copy()]

print(sort_sequence_numbers_asc(nums))
