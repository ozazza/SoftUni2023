electrons = int(input())
n = 1
shells = []

while electrons > 0:

    subtracted_electrons = 2 * n**2

    if subtracted_electrons > electrons:
        subtracted_electrons = electrons

    shells.append(subtracted_electrons)
    electrons -= subtracted_electrons
    n += 1
    
print(shells)
