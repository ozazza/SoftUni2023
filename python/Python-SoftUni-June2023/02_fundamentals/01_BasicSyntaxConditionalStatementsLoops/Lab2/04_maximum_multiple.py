divisor = int(input())
boundary = int(input())
# largest_n = 0

n = boundary

while 0 < n <= boundary:

    if n % divisor == 0:

        print(n)
        break

    n -= 1
