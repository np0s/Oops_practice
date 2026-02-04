# 1. Create a Student class where marks are private and accessed using getter method.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  

    def get_marks(self):
        return self.__marks 
    

student = Student("Alice", 95)
print(f"Student Name: {student.name}")
print(f"Student Marks: {student.get_marks()}")