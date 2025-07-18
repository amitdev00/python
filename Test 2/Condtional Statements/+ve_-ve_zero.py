# Write a program to check if a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num == 0:
    print(f"{num} is zero.")
elif num > 0:
    print(f"{num} is positive number.")
elif num < 0:
    print(f"{num} is negative number.")
else:
    print("Invalid input.")