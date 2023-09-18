str1 = input()
str2 = input()

str_length = len(str1)
last_string = ''

for i in range(str_length):
    new_string = ''

    for char_index in range(str_length):

        if char_index > i:
            new_string += str1[char_index]
        else:
            new_string += str2[char_index]

    if new_string != str1 and new_string != last_string:
        last_string = new_string
        print(new_string)
