version = input()

num = int(version.replace('.', ''))
num_str = str(num + 1)

print(f'{num_str[0]}.{num_str[1]}.{num_str[2]}')
