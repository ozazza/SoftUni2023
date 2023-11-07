text = input().split()

while True:
    user_input = input()

    if user_input == '3:1':
        break

    command = user_input.split()
    
    new_text = []
    if command[0] == 'merge':
        start_i = int(command[1])
        end_i = int(command[2])

        if end_i > len(text):
            end_i = len(text) - 1

        new_text = []
        new_word = ''
        for word in text:
            if start_i <= text.index(word) <= end_i:
                new_word += word
            else:
                new_text.append(word)

        new_text.insert(start_i, new_word)
        text = new_text.copy()

    elif command[0] == 'divide':
        i = int(command[1])
        partitions = int(command[2])

        sub_str_list = []

        diff = 0
        for part in text:

            if text.index(part) == i:
                text.pop(i)

                # Calculate the step (the len of the part)
                diff = len(part) % partitions
                chars_in_partition = int(len(part) / partitions)
                
                if diff > 0:
                    list_with_chars_in = [chars_in_partition] * (partitions - 1)
                    list_with_chars_in.append(chars_in_partition + diff)

                    step = ((len(part) - diff) / partitions) - 1
                else:
                    list_with_chars_in = [chars_in_partition] * partitions
                    step = (int(len(part) / partitions)) - 1

                sub_string = ''
                for chars_count in list_with_chars_in:

                    for n in range(chars_count):
                        sub_string += part[n]


                    sub_str_list.append(sub_string)


                # start = 0
                # end = start + step
                # sub_s = ''
                # for sub_part_i in range(len(part)):
                #
                #     if part.index(part[start]) <= part.index(part[sub_part_i]) <= part.index(part[end]):
                #         sub_s += part[sub_part_i]
                #
                #         if part.index(part[sub_part_i]) == part.index(part[end]):
                #             text.append(sub_s)
                #             start = sub_part_i + 1
                #             end = start + step
                #
                #             if diff > 0 and sub_part_i + step > len(part) - 1:
                #                 end = start + step + diff
                #
                #             sub_s = ''

print(' '.join(text))
