class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def print_name(self):
        print(self._first_name, self._last_name)

class Student(Person):
    def __init__(self, first_name, last_name, reg_no):
        super().__init__(first_name, last_name,)
        self._reg_no = reg_no

    def welcome(self):
        print(f'Welcome {self._first_name} {self._last_name}, Your university registration number is {self._reg_no}')


if __name__ == "__main__":
    student = Student("Mohammad", "Zohan", 1230)
    student.print_name()
    student.welcome()

