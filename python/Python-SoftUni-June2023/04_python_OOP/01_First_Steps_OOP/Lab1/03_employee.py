class Employee:
    def __init__(self, _id: int, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return self.first_name + self.last_name

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        new_salary = self.salary + amount
        return


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
