# 1. Create a base class University. Derive Student and Teacher from it. Then create TeachingAssistant that inherits from both Student and Teacher and implements methods for studying, teaching, and assisting.
class University:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"University Name: {self.name}")
class Student(University):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def study(self):
        print(f"Student ID: {self.student_id} is studying.")
class Teacher(University):
    def __init__(self, name, teacher_id):
        super().__init__(name)
        self.teacher_id = teacher_id
    def teach(self):
        print(f"Teacher ID: {self.teacher_id} is teaching.")
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, student_id, teacher_id):
        Student.__init__(self, name, student_id)
        Teacher.__init__(self, name, teacher_id)
    def assist(self):
        print(f"Teaching Assistant with Student ID: {self.student_id} and Teacher ID: {self.teacher_id} is assisting.")

ta = TeachingAssistant("ABC University", "S123", "T456")
ta.info()
ta.study()
ta.teach()
ta.assist()

