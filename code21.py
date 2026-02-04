# 10. Create a Result class where marks list is private and modified using methods.
class Result:
    def __init__(self):
        self.__marks = []  

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
            print(f"Added mark: {mark}")
        else:
            print("Mark must be between 0 and 100.")

    def get_marks(self):
        return self.__marks
result = Result()
result.add_mark(85)
result.add_mark(110)
print(f"Marks: {result.get_marks()}") 