num = int(input())
is_prime = True

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
elif num == 1:
    is_prime = False

print(is_prime)

# num = int(input())
# is_prime = True
#
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         is_prime = False
#         break
#
# print(is_prime)
