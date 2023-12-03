sequence = input()
digits = ''
letters = ''
other = ''
for c in sequence:
    if c.isdigit():
        digits += c
    elif c.isalpha():
        letters += c
    else:
        other += c

print(digits)
print(letters)
print(other)