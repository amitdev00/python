#Swap two number values and print them
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

temp = num1
num1 = num2
num2 = temp
print("After swapping:", num1, "and", num2)