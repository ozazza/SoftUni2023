from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

        return f'This pokemon is already caught'

    def release_pokemon(self, name):
        try:
            pokemon = [x for x in self.pokemons if x.name == name][0]
        except IndexError:
            return 'Pokemon is not caught'

        self.pokemons.remove(pokemon)
        return f'You have released {name}'

    def trainer_data(self):
        pokemons_data = '\n'.join(f'- {p.pokemon_details()}' for p in self.pokemons)

        return f'Pokemon Trainer {self.name}\n' \
               f'Pokemon count {len(self.pokemons)}\n ' \
               f'{pokemons_data}'
