key = int(input())
n = int(input())

message_word = ''
for i in range(1, n + 1):
    ch = input()
    message_word += chr(ord(ch) + key)

print(message_word)
