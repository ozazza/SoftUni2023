# Input
n1 = int(input())
n2 = int(input())
operation = input()

result = 0
is_zero = False
even_odd = 'odd'

# Logic
if operation == '+':
    result = n1 + n2
elif operation == '-':
    result = n1 - n2
elif operation == '*':
    result = n1 * n2
elif operation == '%' or operation == '/':
    if n2 != 0:
        if operation == '/':
            result = n1 / n2
        if operation == '%':
            result = n1 % n2
    else:
        is_zero = True

if not is_zero and result % 2 == 0:
    even_odd = 'even'

# Output
if is_zero:
    print(f'Cannot divide {n1} by zero')
else:
    if operation == '+' or operation == '-' or operation == '*':
        print(f'{n1} {operation} {n2} = {result} - {even_odd}')
    elif operation == '/':
        print(f'{n1} / {n2} = {result:.2f}')
    elif operation == '%':
        print(f'{n1} % {n2} = {result}')
