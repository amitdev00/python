# program for area of square

class Area:
    def __init__(self, side):
        self.side = side
        
    
    def area_sqaure(self):
        return self.side * self.side
    
side = int(input("Enter side of sqaure: "))


obj_square = Area(side)

method_areasquare = obj_square.area_sqaure()
print(f"Area of square: {method_areasquare}")

        