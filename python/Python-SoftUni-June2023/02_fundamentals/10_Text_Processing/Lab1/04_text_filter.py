banned = input().split(', ')
text = input()

new_text = ''
for word in banned:
    while word in text:
        text = text.replace(word, '*' * len(word))

print(text)
