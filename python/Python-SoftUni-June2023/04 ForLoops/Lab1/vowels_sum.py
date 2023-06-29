# гласни

user_input = input()

result = 0
a = 1
e = 2
i = 3
o = 4
u = 5

for char in user_input:
    if char == 'a':
        result += a
    elif char == 'e':
        result += e
    elif char == 'i':
        result += i
    elif char == 'o':
        result += o
    elif char == 'u':
        result += u

print(result)
