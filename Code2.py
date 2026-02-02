# 2. Create a base class Vehicle. Derive Car and Boat from it. Then create AmphibiousVehicle that inherits from both Car and Boat and shows land and water transportation.
class Vehicle:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"Vehicle Name: {self.name}")
class Car(Vehicle):
    def __init__(self, name, wheels):
        super().__init__(name)
        self.wheels = wheels
    def drive(self):
        print(f"{self.name} is driving on {self.wheels} wheels.")
class Boat(Vehicle):
    def __init__(self, name, propellers):
        super().__init__(name)
        self.propellers = propellers
    def sail(self):
        print(f"{self.name} is sailing with {self.propellers} propellers.")
class AmphibiousVehicle(Car, Boat):
    def __init__(self, name, wheels, propellers):
        Car.__init__(self, name, wheels)
        Boat.__init__(self, name, propellers)
    def transport(self):
        print(f"{self.name} can transport on land and water.")
  
amphibious = AmphibiousVehicle("AmphiCar", 4, 2)
amphibious.info()
amphibious.drive()
amphibious.sail()
amphibious.transport()