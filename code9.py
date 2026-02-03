# 4. Create an abstract class Vehicle with abstract method speed() and implement it in Car class.
from abc import ABC, abstractmethod 
class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
class Car(Vehicle):
    def __init__(self, max_speed):
        self.max_speed = max_speed
    def speed(self):
        return f"The car's maximum speed is {self.max_speed} km/h."
car = Car(220)
print(car.speed())

