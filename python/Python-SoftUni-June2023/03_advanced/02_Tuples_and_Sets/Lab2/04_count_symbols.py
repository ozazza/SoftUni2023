text = input()

for l in sorted(set(text)):
    print(f'{l}: {text.count(l)} time/s')


# times = {}
#
# for s in input():
#     times[s] = times.get(s,0)+1
#
# for symbol, val in sorted(times.items()):
#     print(f'{symbol}: {val} time/s')
