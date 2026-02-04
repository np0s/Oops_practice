# 6. Create a Car class with private speed and methods accelerate and brake without init simple code
class Car:
    def __init__(self):
        self.__speed = 0  

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            print(f"Car accelerated by: {amount} km/h")
        else:
            print("Acceleration amount must be positive.")

    def brake(self, amount):
        if amount > 0:
            self.__speed = max(0, self.__speed - amount)
            print(f"Car slowed down by: {amount} km/h")
        else:
            print("Brake amount must be positive.")

    def get_speed(self):
        return self.__speed
car = Car()
car.accelerate(50)
car.brake(20)
print(f"Current Speed: {car.get_speed()} km/h")
