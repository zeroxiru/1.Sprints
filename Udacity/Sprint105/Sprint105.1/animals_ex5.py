class Dog:
    scientific_name = "Canis lupus familiaris"
    def __init__(self, name):
        self.name = name
        self.woof = 0

    def speak(self):
        print("Woof!!")

    def hear(self, words):
        if self.name in words:
            self.speak()

    def count(self):
        self.woof += 1
        for bark in range(self.woof):
            self.speak()
class Chihuahua(Dog):
    origin = "Mexico"
    def speak(self):
        print("Yipp")


class Husky(Dog):
    origin = "Serbia"

    def speak(self):
        print("Auurora")


class Labrador(Dog):
    origin = "Germany"

    def speak(self):
        print("bahuu")



