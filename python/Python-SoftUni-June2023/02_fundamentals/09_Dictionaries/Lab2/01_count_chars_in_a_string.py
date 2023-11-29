text_input = input()

text = [x for x in text_input if x != ' ']
chars = {}

for ch in text:
    if ch != ' ':
        if ch not in chars.keys():
            chars[ch] = 1
        else:
            chars[ch] += 1

for k, v in chars.items():
    print(f'{k} -> {v}')
