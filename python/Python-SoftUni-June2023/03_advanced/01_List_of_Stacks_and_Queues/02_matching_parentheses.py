text = input()

open_parentheses = []
for i in range(len(text)):
    if text[i] == '(':
        open_parentheses.append(i)
    elif text[i] == ')':
        start_i = open_parentheses.pop()
        end_i = i + 1

        print(text[start_i:end_i])
