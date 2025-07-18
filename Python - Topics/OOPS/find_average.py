# Program to find the average of three numbers

class Average:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def find_average(self):
        return (self.num1 + self.num2 + self.num3) / 3
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

obj_average = Average(num1, num2, num3)

method_average = obj_average.find_average()
print(f"the average of {num1} and {num2} and {num3} is: {method_average}")