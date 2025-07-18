# You have given a Shape class and subclasses Circle  and Square. 
# The parent class (Shape) has a area() method.
# Now, Write a OOP code to calculate the area of each shapes 

from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Radius of Circle :- {self.radius}\nArea of Circle :- {3.14 * self.radius * self.radius}\n"
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return f"Side of Square :- {self.side}\nArea of Square :- {self.side * self.side}"
    
shapes = [Circle(45), Square(10), Circle(20), Square(67)]

for shape in shapes:
    print(shape.area())

