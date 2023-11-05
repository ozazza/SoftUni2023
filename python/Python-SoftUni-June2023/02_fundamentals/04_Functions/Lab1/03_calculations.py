def calculate(operator: str, num1: int, num2: int):
    result = 0
    if operator == 'multiply':
        result = num1 * num2
    elif operator == 'divide':
        result = num1 / num2
    elif operator == 'add':
        result = num1 + num2
    elif operator == 'subtract':
        result = num1 - num2
    return int(result)


type_operation = input()
number1 = int(input())
number2 = int(input())

print(calculate(type_operation, number1, number2))
