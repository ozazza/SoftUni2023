# Input
n = int(input())

# Logic
for i in range(1111, 9999 + 1):
    spec_number_str = str(i)
    counter = 0

    for spec_char in spec_number_str:
        digit = int(spec_char)

        if digit == 0 or n % digit != 0:
            break

        counter += 1

    if counter == len(spec_number_str):
        print(spec_number_str, end=' ')
