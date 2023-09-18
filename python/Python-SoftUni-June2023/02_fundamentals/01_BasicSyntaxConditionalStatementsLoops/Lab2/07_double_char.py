while True:
    txt = input()

    if txt == 'End':
        break
    elif txt == 'SoftUni':
        continue

    for ch in txt:
        print(ch * 2, end='')

    print()
