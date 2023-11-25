class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    usr = input()

    if usr == "End":
        break

    party.people.append(usr)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
