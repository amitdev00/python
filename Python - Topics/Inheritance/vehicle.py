# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, name,  max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


car = Vehicle("Audi", "360", 78)
print(car.name)
print(car.max_speed)
print(car.mileage)
