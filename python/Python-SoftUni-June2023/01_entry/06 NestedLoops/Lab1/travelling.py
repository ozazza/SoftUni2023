
# Logic
destination = ''
end = 'End'
trip_budget = 0

while destination != end:
    destination = input()

    if destination == end:
        break

    budget_min = float(input())

    savings = 0
    while savings < budget_min:
        saved = input()

        if not saved.isalpha():
            savings += float(saved)

            if savings >= budget_min:
                print(f'Going to {destination}!')
                break
        else:
            destination = saved
            break

