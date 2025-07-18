# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def display_details(self):
        print(f"Name: {self.name}\nMaximum Speed: {self.max_speed}\nMileage: {self.mileage}")

bus = Bus("School Volvo", 210, 25)
bus.display_details()