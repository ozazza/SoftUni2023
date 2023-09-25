char_num = int(input())

start_char = 97

for col1 in range(start_char, start_char + char_num):

    for col2 in range(start_char, start_char + char_num):

        for col3 in range(start_char, start_char + char_num):

            print(f'{chr(col1)}{chr(col2)}{chr(col3)}')
