class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 + self.num2

class Subtraction(Addition):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    def calculate(self):
        return self.num1 - self.num2

add = Subtraction(4,7)
print(add.calculate())