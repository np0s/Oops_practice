# 5. Create an abstract class Employee with abstract method salary() and implement it in Developer class.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class Developer(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def salary(self):
        return f"The developer's monthly salary is ${self.monthly_salary}."
dev = Developer(5000)
print(dev.salary())