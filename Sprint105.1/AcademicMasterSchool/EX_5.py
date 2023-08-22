class Employee:
#fix the error
    def __init__(self, name, salary=0):
        self._name = name
        self._salary = salary

    def display_employee(self):
        print("Name : ", self._name, ", Salary: ", self._salary)

new_emp = Employee("Aharon")
new_emp.display_employee()

