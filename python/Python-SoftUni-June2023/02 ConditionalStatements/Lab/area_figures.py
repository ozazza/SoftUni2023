from math import pi

figure = input()

result = 0

if figure == 'square':
    x = float(input())
    result = x * x
elif figure == 'rectangle':
    x = float(input())
    y = float(input())
    result = x * y
elif figure == 'circle':
    r = float(input())
    result = pi * r * r
if figure == 'triangle':
    a = float(input())
    h = float(input())
    result = a * h / 2

print(f'{result:.3f}')

