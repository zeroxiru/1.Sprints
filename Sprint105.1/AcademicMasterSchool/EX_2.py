from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @abstractmethod
    def speak(self):
        pass


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        pass

ani = Cat("Fido")
#print(ani.get_name())
ani.speak()