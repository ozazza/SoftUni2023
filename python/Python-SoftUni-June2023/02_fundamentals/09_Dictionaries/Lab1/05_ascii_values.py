chars = input().split(', ')

chars_to_ascii = {ch: ord(ch) for ch in chars}
print(chars_to_ascii)