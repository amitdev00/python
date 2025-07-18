# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area_of_circle(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter_of_circle(self):
        return 2 * 3.14 * self.radius
    
radius = int(input("Enter the radius of the circle: "))

circle = Circle(radius)

area = circle.area_of_circle()
perimeter = circle.perimeter_of_circle()

print(f"Area of the circle is: {area}")
print(f"Perimeter of the cicle is: {perimeter}")

    