# Complete the following code to create an object spot from the Dog class
# with the name “Spot” and update their tricks to include “spin”
# then “sit”. You can use show(spot) to print the string representation of the object.

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def update_tricks(self, trick):
        self.tricks.append(trick)

    def show(self):
        return f'Dog(name = {self.name}, tricks = {str(self.tricks)})'

spot = Dog("Fido")
spot.update_tricks("spin")
spot.update_tricks("sit")

print(spot.show())

