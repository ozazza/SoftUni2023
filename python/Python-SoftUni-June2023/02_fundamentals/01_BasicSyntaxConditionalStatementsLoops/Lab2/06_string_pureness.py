n = int(input())
comma = ','
period = '.'
underscore = '_'

for i in range(0, n):
    word = input()

    if comma in word or period in word or underscore in word:
        print(f'{word} is not pure!')

    else:
        print(f'{word} is pure.')
