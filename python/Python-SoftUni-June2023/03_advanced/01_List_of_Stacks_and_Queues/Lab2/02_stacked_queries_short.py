numbers = []

# dictionary
map_functions = {
    '1': lambda x: numbers.append(x[1]),
    '2': lambda x: numbers.pop() if numbers else None,
    '3': lambda x: print(max(numbers)) if numbers else None,
    '4': lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    num_data = input().split()
    command = num_data[0]
    map_functions[command](num_data)

numbers.reverse()
print(*numbers, sep=', ')
