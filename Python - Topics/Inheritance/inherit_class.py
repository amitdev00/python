# Create a electric car class that inherits from the Car class and
#  has an additional attribute battery_size


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)

    def details(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nBattery Size: {self.battery_size}"

car = ElectricCar("Mahindra", "Thar", "Large")
car_details = car.details()
print(car_details)

        

        





