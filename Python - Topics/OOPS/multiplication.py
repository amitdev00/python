# Program to multiply two numbers

class Multiplication:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiply(self):
        return self.num1 * self.num2
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

multiply_num = Multiplication(num1, num2)

peform_multiplication = multiply_num.multiply()
print(f"Multiplication of {num1} and {num2} is: {peform_multiplication}")