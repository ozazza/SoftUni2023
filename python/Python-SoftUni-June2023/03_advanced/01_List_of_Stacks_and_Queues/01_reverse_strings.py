# text = input()
#
# print(text[::-1])

text = list(input())

while text:
    print(text.pop(), end='')
