

class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = Sum(num1, num2)

addition = add.addition()
print(f"The sum of {num1} and {num2} is: {addition}")





    