# 7. Create a Mobile class where battery percentage is private and decreases when used.
class Mobile:
    def __init__(self, brand, battery_percentage):
        self.brand = brand
        self.__battery_percentage = battery_percentage  

    def use_battery(self, amount):
        if 0 < amount <= self.__battery_percentage:
            self.__battery_percentage -= amount
            print(f"Used battery: {amount}%")
        else:
            print("Invalid battery usage amount.")

    def get_battery_percentage(self):
        return self.__battery_percentage
mobile = Mobile("Samsung", 100)
mobile.use_battery(30)
print(f"Current Battery Percentage: {mobile.get_battery_percentage()}%")  