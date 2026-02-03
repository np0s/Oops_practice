# 1. Create an abstract class Animal with abstract method sound() and implement it in Dog class.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof!"
dog = Dog()
print(dog.sound()) 