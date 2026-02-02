# 4. Create a base class Person. Derive Dancer and Singer from it. Then create Performer that inherits from both Dancer and Singer and performs on stage.
class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"Person Name: {self.name}")
class Dancer(Person):
    def __init__(self, name, dance_style):
        super().__init__(name)
        self.dance_style = dance_style
    def dance(self):
        print(f"{self.name} is dancing in {self.dance_style} style.")
class Singer(Person):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre
    def sing(self):
        print(f"{self.name} is singing {self.genre} music.")
class Performer(Dancer, Singer):
    def __init__(self, name, dance_style, genre):
        Dancer.__init__(self, name, dance_style)
        Singer.__init__(self, name, genre)
    def perform(self):
        print(f"{self.name} is performing on stage.")

performer = Performer("John Doe", "Hip-Hop", "Pop")
performer.info()
performer.dance()
performer.sing()
performer.perform() 
