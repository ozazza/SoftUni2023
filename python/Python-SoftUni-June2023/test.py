def check_balance(str1):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]

    stack = []
    for i in str1:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


str2 = check_balance('{[(])}')
print(str2)
