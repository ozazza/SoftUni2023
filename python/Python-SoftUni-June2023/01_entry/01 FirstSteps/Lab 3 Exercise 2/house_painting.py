x = float(input())
y = float(input())
h = float(input())

green = 3.4
red = 4.3
door = 1.2 * 2
windows = 1.5 * 1.5 * 2

sides_front_back = x * x * 2
sides_left_right = x * y * 2
sides = sides_front_back + sides_left_right - door - windows
sides_liters = sides / green

roof_sides = x * y * 2
roof_triangle = (x * h / 2) * 2
roof_liters = (roof_sides + roof_triangle) / red

print(f'{sides_liters:.2f}')
print(f'{roof_liters:.2f}')
