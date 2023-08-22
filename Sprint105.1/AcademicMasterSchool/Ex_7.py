# Complete the following code to include a method named
# update_attacks(attack) which appends the attack to the list of attacks.

class Pokemon:

    def __init__(self, name, kind):
        self.name = name
        self.type = kind
        self.attacks = []

    def show(self):
        return f"Pokemon name is {self.name} and type is {self.type}. Attacks include: {str(self.attacks)}"

bulbasaur = Pokemon('Bulbasaur', 'Grass')
bulbasaur.update_attacks('Vine Whip')
bulbasaur.update_attacks('Tackle')

