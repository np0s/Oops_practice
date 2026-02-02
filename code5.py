# 5. Create a base class Company. Derive Programmer and Tester from it. Then create SoftwareEngineer that inherits from both Programmer and Tester and handles complete software development.
class Company:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"Company Name: {self.name}")
class Programmer(Company):
    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language
    def code(self):
        print(f"{self.name} is coding in {self.programming_language}.")
class Tester(Company):
    def __init__(self, name, testing_tool):
        super().__init__(name)
        self.testing_tool = testing_tool
    def test(self):
        print(f"{self.name} is testing using {self.testing_tool}.")
class SoftwareEngineer(Programmer, Tester):
    def __init__(self, name, programming_language, testing_tool):
        Programmer.__init__(self, name, programming_language)
        Tester.__init__(self, name, testing_tool)
    def develop(self):
        print(f"{self.name} is handling complete software development.")

engineer = SoftwareEngineer("TechCorp", "Python", "Selenium")
engineer.info()
engineer.code()
engineer.test()
engineer.develop()

