str_one = input()
str_two = input()

while str_one in str_two:
    str_two = str_two.replace(str_one, '')

print(str_two)
