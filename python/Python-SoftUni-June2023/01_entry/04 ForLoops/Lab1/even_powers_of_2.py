from math import pow

n = int(input())

for i in range(0, n + 1, 2):
    if i % 2 == 0:
        print(int(pow(2, i)))
