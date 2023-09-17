# Input
n1 = input()
n2 = input()

# Logic
for num in range(int(n1), int(n2) + 1):
    sum_even = 0
    sum_odd = 0
    string_num = str(num)

    for char_index in range(len(string_num)):

        char = string_num[char_index]
        n = int(char)

        position = char_index + 1
        if position % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

    if sum_even == sum_odd:
        print(num, end=' ')
