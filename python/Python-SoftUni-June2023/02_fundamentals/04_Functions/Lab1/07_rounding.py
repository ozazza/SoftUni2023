def rounds_numbers(list_n: list):
    nums = list()
    for s in list_n:
        n = float(s)
        nums.append(int(round(n)))

    return nums


num_s = input().split()
print(rounds_numbers(num_s))
