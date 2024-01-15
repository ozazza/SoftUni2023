stack = []

for i in range(int(input())):
    query = input().split()
    query = [int(x) for x in query]

    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if stack:
            stack.pop()
    elif query[0] == 3:
        if stack:
            print(max(stack))
    elif query[0] == 4:
        if stack:
            print(min(stack))

stack.reverse()
print(*stack, sep=', ')
