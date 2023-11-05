nums = input().split(' ')
message = input()

indexes = list()
message_list = list()
sent_message = ''

for n in nums:
    sum_d = 0
    for d in n:
        sum_d += int(d)

    indexes.append(sum_d)

for c in message:
    message_list.append(c)

for i in range(len(indexes)):
    ch_index = indexes[i]

    if ch_index >= len(message_list):
        actual_index = ch_index - len(message_list)
    else:
        actual_index = ch_index

    sent_message += message_list[actual_index]
    message_list.pop(actual_index)

print(sent_message)
