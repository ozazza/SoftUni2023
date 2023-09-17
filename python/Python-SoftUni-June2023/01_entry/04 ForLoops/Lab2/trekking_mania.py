# Input
groups = int(input())

total_people = 0
musala = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

# Logic
for i in range(groups):
    people = int(input())

    if people <= 5:
        musala += people
    elif people <= 12:
        monblanc += people
    elif people <= 25:
        kilimandjaro += people
    elif people <= 40:
        k2 += people
    elif people >= 41:
        everest += people

    total_people += people

# Output
print(f'{musala / (total_people/100):.2f}%')
print(f'{monblanc / (total_people/100):.2f}%')
print(f'{kilimandjaro / (total_people/100):.2f}%')
print(f'{k2 / (total_people/100):.2f}%')
print(f'{everest / (total_people/100):.2f}%')
