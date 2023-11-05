def return_ascii_chars_between(char1: str, char2: str):
    result = list()
    for c in range(ord(char1) + 1, ord(char2)):
        result.append(chr(c))

    return ' '.join(str(x) for x in result)


ch1 = input()
ch2 = input()

print(return_ascii_chars_between(ch1, ch2))
