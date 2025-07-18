# create a calculator using python

def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1  / num2

def modulus(num1, num2):
    return num1 % num2

def floor_division(num1, num2):
    return num1 // num2

num1 = int(input("Enter the number: "))
operation = input("Enter the operation you want to perform: ")
num2 = int(input("Enter the number: "))

if operation == '+':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == '-':
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
elif operation == '*':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
elif operation == '/':
    print(f"{num1} / {num2} = {division(num1, num2)}")
elif operation == '//':
    print(f"{num1} // {num2} = {floor_division(num1, num2)}")
else:
    print("Invalid Operation.")