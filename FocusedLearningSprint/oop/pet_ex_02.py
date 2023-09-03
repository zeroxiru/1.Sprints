from abc import abstractmethod


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, value):
        self._last_name = value

    @abstractmethod
    def speak_language(self):
        pass

class Bengali(Person):
    def speak_language(self):
        print(f" {self.get_first_name()} {self.get_last_name()}  speak in bengali mother tongue")

class British(Person):
    def speak_language(self):
        print(f" {self.get_first_name()} {self.get_last_name()} speak in English mother tongue")

class Arabic(Person):
    def speak_language(self):
        print(f" {self.get_first_name()} {self.get_last_name()}  speak in arabic mother tongue")

bengali = Bengali("Mohammad", "Zohan")
bengali.speak_language()

english = British("Imran", "Kibria")
english.speak_language()

arabic = Arabic("Mohammad", "Amirul")
arabic.speak_language()


