class Cat:
    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purr")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow")




