from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id: str, emp_name: str, emp_mail: str):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._emp_mail = emp_mail


    def get_emp_id(self):
        return self._emp_id

    def set_emp_id(self, value):
        self._emp_id = value

    def get_emp_name(self):
        return self._emp_name


    def set_emp_name(self, value):
        self._emp_name = value

    def get_emp_mail(self):
        return self._emp_mail

    def set_emp_mail(self, value):
        self._emp_mail = value

    @abstractmethod
    def calculate_pay(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, monthly_salary: float, tax_rate: float, emp_id: str, emp_name: str, emp_mail: str):
        super().__init__(emp_id, emp_name, emp_mail)
        self._monthly_salary = monthly_salary
        self._tax_rate =  tax_rate


    def get_monthly_salary(self):
        return  self._monthly_salary

    def set_monthly_salary(self, value):
        self._monthly_salary = value


    def get_tax_rate(self):
        return self._tax_rate


    def set_tax_rate(self, value):
        self._tax_rate = value


    def calculate_pay(self):
        salary = self._monthly_salary -(self._monthly_salary * (self._tax_rate + 100))
        return salary


class CommissionEmployee(Employee):

    def __init__(self, sales_amount: float, commission_rate: float, emp_id: str, emp_name: str, emp_mail: str):
        super().__init__(emp_id, emp_name, emp_mail)
        self._sales_amount = sales_amount
        self._commission_rate = commission_rate


  #write the setters and getters letter

    def get_sales_amount(self):
        return self._sales_amount

    def set_sales_amount(self, value):
        self._sales_amount = value

    def get_commission_rate(self):
        return  self._commission_rate

    def set_commission_rate(self, value):
        self._commission_rate = value
    def calculate_pay(self):
        salary = self._sales_amount * (self._commission_rate / 100)
        return  salary




class HourlyEmployee(Employee):

    def __init__(self, hourly_rate: float, hours_worked: float, emp_id: str, emp_name: str, emp_mail: str):
        super().__init__(emp_id, emp_name, emp_mail)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, value):
        self._hourly_rate = value


    def get_hours_worked(self):
        return  self._hours_worked

    def set_hours_worked(self, value):
        self._hours_worked = value


    def calculate_pay(self):
        salary = (self._hourly_rate * self._hours_worked)
        return  salary



if __name__ == "__main__":
    salaried_employee = SalariedEmployee(5000, 25, 1, "John Doe", "erer@gmail.com", )
    comm_employee = CommissionEmployee(5000, 25, 1, " Michal", "erer@gmail.com" )
    hourly_employee = HourlyEmployee(5000, 25, 1, "Max", "erer@gmail.com")

    lst_Emp = [salaried_employee, comm_employee, hourly_employee]

    for emp in lst_Emp:
        net_pay = emp.calculate_pay()
        print(f"Employee ID: {emp._emp_id}")
        print(f"Employee Name: {emp._emp_name}")
        print(f"Net Salary: ${net_pay:.2f}")
