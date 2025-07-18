# Compare two numbers and print the larger one.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is greater than {num1}.")
else:
    print("You have done something worng.")