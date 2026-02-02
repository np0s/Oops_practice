# 3. Create a base class Device. Derive Camera and Phone from it. Then create SmartGadget that inherits from both Camera and Phone and performs multitasking operations.
class Device:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        print(f"Device Brand: {self.brand}")
class Camera(Device):
    def __init__(self, brand, megapixels):
        super().__init__(brand)
        self.megapixels = megapixels
    def take_photo(self):
        print(f"{self.brand} Camera with {self.megapixels}MP is taking a photo.")
class Phone(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def make_call(self, number):
        print(f"{self.brand} Phone model {self.model} is making a call to {number}.")
class SmartGadget(Camera, Phone):
    def __init__(self, brand, megapixels, model):
        Camera.__init__(self, brand, megapixels)
        Phone.__init__(self, brand, model)
    def multitask(self):
        print(f"{self.brand} SmartGadget is multitasking.")

gadget = SmartGadget("TechBrand", 48, "X1000")
gadget.info()
gadget.take_photo()
gadget.make_call("123-456-7890")
gadget.multitask()  