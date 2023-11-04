def check_if_perfect_number(n: int) -> str:
    divisors = list()

    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(check_if_perfect_number(num))