# Calculate factorial of a number using a loop
factorial = 1
number = int(input("Enter a number: "))

for number in range(1, number + 1):
    factorial *= number
print(f"The factorial of the numeber is: {factorial}")