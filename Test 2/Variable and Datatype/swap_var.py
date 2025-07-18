# Swap two numbers  without using a temporary variable.

num1 = int(input("Enter the number: "))
num2 = int(input(" Enter the numeber: "))

print(f"Value of num1 before swapping is: {num1}")
print(f"Value of num2 before swapping is: {num2}")

num1, num2 = num2, num1

print(f"Value of num1 after swapping is: {num1}")
print(f"Value of num2 after swapping is: {num2}")