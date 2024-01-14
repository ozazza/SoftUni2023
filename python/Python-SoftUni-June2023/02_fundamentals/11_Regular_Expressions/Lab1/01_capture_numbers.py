import re


command = input()
while len(command) > 1:

    command = input()
    pattern = r"d+"
    r = re.findall(pattern, command)

    if r:
        print(r)


