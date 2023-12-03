command = input().split()
new_word = ''
for word in command:
    result = word * len(word)
    new_word += result

print(new_word)
