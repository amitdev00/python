#  Program to subtract two numbers

class Subtract:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def subtraction(self):
        return self.num1 - self.num2
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

subtract_number = Subtract(num1, num2)

subtraction_number = subtract_number.subtraction()
print(f"The subtraction of {num1} and {num2} is {subtraction_number}")