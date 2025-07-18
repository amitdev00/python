# Calculate factorial of a number using a loop.
factorial = 1
user_input = int(input("Enter a number: "))

while user_input >= 1:
    factorial = factorial * user_input
    user_input -= 1
print(f" Factorial of the given number is {factorial}.")
   