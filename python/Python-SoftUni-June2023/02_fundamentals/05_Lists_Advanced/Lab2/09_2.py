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
        
        if start_i < 0:
            start_i = 0
        if end_i > len(text) - 1:
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
    
        if i < 0:
            i = 0
            
        sub_str_list = []
        diff = 0
        for part in text:

            if text.index(part) == i:
                text.pop(i)

                # Calculate the step (the len of the part)
                diff = int(len(part) % partitions)
                chars_in_partition = int(len(part) // partitions)

                if diff > 0:
                    list_steps_count = [chars_in_partition] * (partitions - 1)
                    list_steps_count.append(chars_in_partition + diff)

                    step = int((len(part) - diff) / partitions) - 1
                else:
                    list_steps_count = [chars_in_partition] * partitions

                    step = int((len(part) / partitions)) - 1

                part_list = list(part)
                for steps_count in list_steps_count:

                    sub_string = ''
                    for n in range(steps_count):
                        sub_string += part_list[n]

                    text.append(sub_string)

                    new_part = part_list[steps_count:]
                    part_list = new_part

print(' '.join(text))
