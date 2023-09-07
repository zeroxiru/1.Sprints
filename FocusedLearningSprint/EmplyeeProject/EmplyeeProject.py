class Employee:
    def __init__(self, name, id_number, job_title, department ):
        self._name = name
        self._id_number = id_number
        self._job_title = job_title
        self._department = department

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_id_number(self):
        return self._id_number

    def set_id_number(self, value):
        self._id_number = value

    def get_job_title(self):
        return self._job_title

    def set_job_title(self, value):
        self._job_title = value

    def get_department(self):
        return self._department

    def set_department(self, value):
        self._department = value

    def __str__(self):
        return f'{self.get_id_number()}, {self.get_name()},{self.get_department()}, {self.get_job_title()}'

class Company:
    def __init__(self):
        self._employees = {}

    def add_employee(self):
        name = input(" Enter the name")
        id_number = input(" Enter the ID")
        department = input(" Enter the department")
        job_title = input(" Enter the Job title")
        employee = Employee(name, id_number, department, job_title)
        self._employees[id_number] = employee
        print(" Employee added..........")

    def search_employee(self):
        id_number = input(" Please enter the Identification NUmber to search : ")
        if id_number in self._employees:
            print(self._employees[id_number])
        else:
            print("Id not found")

    def delete_employee(self):
        id_number = input(int(" Please enter the Identification NUmber to search : "))
        if id_number in self._employees:
            del self._employees[id_number]
            print("Employee deleted")
        else:
            print("not found")

  #  def print_all_employees(self):

    def display_menu(self):
        print("Menu:")
        print("1. Look up an employee")
        print("2. Add a new employee")
        print("3. Change an existing employee's details")
        print("4. Delete an employee")
        print("5. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice(1-5): ")
            if choice == "1":
                self.search_employee()
            elif choice == "2":
                self.add_employee()
            #elif choice == "3":
            # self.change_details()
            #elif choice == "4":
            elif self.choice == '4':
                self.delete_employee()

            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again")
def main ():
    #e1 = Employee("John Doe", 13, 'IT', 'Network Engineer')
    # print(e1)
    company = Company()
    company.run()

if __name__ == "__main__":
    main()