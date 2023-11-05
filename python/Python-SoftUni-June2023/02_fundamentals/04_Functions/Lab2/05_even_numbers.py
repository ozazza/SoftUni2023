def filter_even_numbers(sequence: list):

    even_s = filter(is_even, sequence)
    result = list()
    for i in even_s:
        result.append(i)

    return result


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


numbers = input().split(' ')
nums = [int(x) for x in numbers.copy()]

print(filter_even_numbers(nums))
