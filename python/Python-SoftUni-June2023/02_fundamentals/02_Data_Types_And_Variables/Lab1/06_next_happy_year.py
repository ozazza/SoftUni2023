digit_year = int(input())

while True:
    digit_year += 1
    year = str(digit_year)
    digits_list = []

    for y in year:
        if y not in digits_list:
            digits_list.append(y)

    if len(year) == len(digits_list):
        print(year)
        break
