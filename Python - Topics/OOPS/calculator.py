# make a calculator that perform basic arithmatic operations

class Calculator:
    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2

    def calculate_num(self):
        if self.operation == "+":
            return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
        elif self.operation == "-":
            return f"{num1} - {num2} = {self.num1 - self.num2}"
        elif self.operation == "*":
            return f"{num1} * {num2} = {self.num1 * self.num2}"
        elif self.operation == "/":
            if self.num2 == 0:
                return "Number can't be divide by zero."
            else:
                return f"{num1} / {num2} = {self.num1 / self.num2}"
        elif self.operation == "//":
            return f" {num1} // {num2} = {self.num1 // self.num2}"


num1 = int(input("Enter the first number: "))
operation = input("Enter the operation you want to perform: ")
num2 = int(input("Enter the second number: "))

obj_calculator = Calculator(num1, operation, num2)

calculate_numbers = obj_calculator.calculate_num()
print(calculate_numbers)






