class Pokemon():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def stringPokemon(self):
        print(f"Pokemon name is {self.name} and type is {self.type}")

class GrassType(Pokemon):

    # overrides the stringPokemon() function on 'Pokemon' class
    def stringPokemon(self):
        print(f"Grass type pokemon name is {self.name}")

poke1 = GrassType('Bulbasaur', 'Grass')
poke1.stringPokemon
poke1.stringPokemon()
poke2 = Pokemon('Charizard', 'Fire')
poke2.stringPokemon
poke2.stringPokemon()