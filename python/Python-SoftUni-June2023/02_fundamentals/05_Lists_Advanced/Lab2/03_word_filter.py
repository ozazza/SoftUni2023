text = input().split()
words = [x for x in text if len(x) % 2 == 0]
print('\n'.join(words))
