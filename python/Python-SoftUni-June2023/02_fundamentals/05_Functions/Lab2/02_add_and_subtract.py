def sum_numbers(n1: int, n2: int):
    return n1 + n2


def subtract(n1: int, n2: int):
    return n1 - n2


def add_and_subtract(n1: int, n2: int, n3: int):
    first_two = sum_numbers(n1, n2)

    return subtract(first_two, n3)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))