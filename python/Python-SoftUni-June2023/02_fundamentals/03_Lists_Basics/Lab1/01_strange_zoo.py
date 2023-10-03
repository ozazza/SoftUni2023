my_list = []

for i in range(3):
    my_list.append(input())

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)