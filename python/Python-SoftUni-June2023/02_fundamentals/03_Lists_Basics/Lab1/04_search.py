nums = int(input())
key_word = input()
words = []

for i in range(nums):
    words.append(input())

print(words)

for f in range(len(words) - 1, -1, -1):

    if key_word not in words[f]:
        words.remove(words[f])

print(words)
