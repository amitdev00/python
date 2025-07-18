# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return f"The seating capacity of the bus is {self.capacity} "

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def bus_details(self):
        return f"Name: {self.name}\nMaximum Speed: {self.max_speed}\nMileage: {self.mileage}"
    
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity = 50)

obj_bus = Bus("Volvo", 250, 56)
detail = obj_bus.seating_capacity()
details = obj_bus.bus_details()
print(detail)
print(details)