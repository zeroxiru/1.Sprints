class Dog:
    scientific_name = "Canis lupus familiaris"
    def speak(self):
        print("Bowow!!!")

    def eat(self, food):
        if food == "buscuit":
            print("Yummy!")
        else:
            print("It is not food")
    def learn_name(self, name):
        self.name = name

    def learn_name2(self, foo):
        self.name = foo


    def hear(self, words):
        if self.name in words:
            self.speak()