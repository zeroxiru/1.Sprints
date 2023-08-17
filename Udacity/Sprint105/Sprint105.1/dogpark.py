import animals_ex5
class DogPark:
    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("dogs are available in the park")
        for dog in self.dogs:
            print(f"{dog.name}")

    def shout(self, words):
        for dog in self.dogs:
            dog.hear(words)


    def converse(self):
        self.rollcall()
        while True:
            words = input("Talk to doggos!('quit' to quit)>")
            if quit in words:
                print("Bye!")
                break
            else:
                self.shout(words)


if __name__ == "__main__":
    dogs= [animals_ex5 .Husky("Toklat"),
            animals_ex5.Chihuahua("Scrappy"),
            animals_ex5.Labrador("Barrett")]
    park = DogPark(dogs)
    park.converse()