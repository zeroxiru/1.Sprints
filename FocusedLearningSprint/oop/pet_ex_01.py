class Pet:
    def __init__(self, name, animal_type, age):
        self._name = name
        self._anima_type = animal_type
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_animal_type(self):
        return self._anima_type

    def set_animal_type(self, value):
        self._anima_type = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value
