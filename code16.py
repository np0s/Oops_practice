# 5. Create an Employee class where salary is private and can be increased.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Salary increased by: {amount}")
        else:
            print("Increase amount must be positive.")

    def get_salary(self):
        return self.__salary
employee = Employee("Eve", 50000)
employee.increase_salary(5000)
print(f"Employee Name: {employee.name}")
print(f"Employee Salary: {employee.get_salary()}")