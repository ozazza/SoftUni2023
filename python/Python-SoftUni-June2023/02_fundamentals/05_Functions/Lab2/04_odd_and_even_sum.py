def sum_odd_even_numbers(a: str):
    # list_a = a.split('')
    sum_even = 0
    sum_odd = 0

    for i in a:
        n = int(i)

        if n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


num = input()
print(sum_odd_even_numbers(num))
