class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def show(self):
        print("Name:", self._name, ", Salary:", int(self._salary))
        #print("Name:", self._name, ", Salary:", int(self._salary))

class TopEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self._salary = self.get_percent(salary)

    @staticmethod
    def get_percent( salary):
        return salary * 1.10


topemployee = TopEmployee("Ibrahim", 5000)
topemployee.show()







