class Dog:

    is_trained = False
    def __init__(self, name):
        self.name = name
        self.woof = 0
        self.hunger_level = 100

    def speak(self):
        print("Woof!!")

    def hear(self, words):
        if self.name in words:
            self.speak()
            self.is_trained = True

    def feed(self, amount):
        if amount >= self.hunger_level:
            self.hunger_level = 0
        else:
            self.hunger_level -= amount
        if self.hunger_level < 0:
            self.hunger_level = 0




    def count(self):
        self.woof += 2
        for bark in range(self.woof ):
            self.speak()

