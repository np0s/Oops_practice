# 3. Create a Person class where age is private and cannot be negative.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = 0  
        self.set_age(age)  

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    def get_age(self):
        return self.__age
person = Person("Bob", 25)
print(f"Person Name: {person.name}")
print(f"Person Age: {person.get_age()}")