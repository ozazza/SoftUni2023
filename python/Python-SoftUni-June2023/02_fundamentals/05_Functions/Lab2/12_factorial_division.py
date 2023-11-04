def calculate_factorial_division(n1: int, n2: int) -> str:
    import math

    fact_n1 = math.factorial(n1)
    fact_n2 = math.factorial(n2)
    result = fact_n1 / fact_n2

    return f'{result:.2f}'


num1 = int(input())
num2 = int(input())

print(calculate_factorial_division(num1, num2))
