class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        if species == "fish":
            self.fishes.append(name)
        if species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.fishes)}"

        result += f"\nTotal animals: {Zoo.__animals}"

        return result


zoo_name = input()
animals = int(input())

zoo = Zoo(zoo_name)
for i in range(animals):
    species, animal_name = input().split(" ")
    zoo.add_animal(species, animal_name)

info_about = input()
print(zoo.get_info(info_about))
