def load_the_bar(n: int):
    bar = list()
    for i in range(1, 101, 10):
        if i <= n:
            sign = '%'
        else:
            sign = '.'

        bar.append(sign)

    printed_bar = f'{n}% [{"".join(bar)}]'

    if n < 100:
        printed_message = 'Still loading...'

        return '\n'.join([printed_bar, printed_message])
    else:
        printed_message = '100% Complete!'
        printed_percents = printed_bar.split(' ')
        return '\n'.join([printed_message, printed_percents[1]])


percent = int(input())
print(load_the_bar(percent))
