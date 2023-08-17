
class Dogs:

    def __init__(self, name):
        self.name = name


    def speak(self):
        print("Wooof!!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!!!")
        else:
            print("It is not a food")


    def hear(self, words):
        if self.name in words:
            self.speak()




