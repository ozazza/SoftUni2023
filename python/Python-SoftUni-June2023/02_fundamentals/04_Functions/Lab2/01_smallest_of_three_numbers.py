def smallest_from_three_integers(n1: int, n2: int, n3: int):
    nums = [n1, n2, n3]

    return min(nums)


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_from_three_integers(num1, num2, num3))
