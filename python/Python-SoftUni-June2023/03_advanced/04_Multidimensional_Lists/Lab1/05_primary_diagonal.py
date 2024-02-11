n = int(input())

sum_diagonal = 0
k = 0
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    for j in range(len(row)):
        if j == k:
            sum_diagonal += row[j]

    k += 1

print(sum_diagonal)
