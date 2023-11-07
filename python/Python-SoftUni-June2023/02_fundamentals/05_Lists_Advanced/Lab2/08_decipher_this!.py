message = input().split()

deciphered = []
for word in message:
    str_digit = ''
    str_char = ''

    for char in word:

        if char.isdigit():
            str_digit += char
        else:
            str_char += char

    ascii_char = chr(int(str_digit))
    new_word_list = list(ascii_char + str_char)
    new_word_list[1], new_word_list[-1] = new_word_list[-1], new_word_list[1]

    deciphered.append(''.join(new_word_list))

print(' '.join(deciphered))
