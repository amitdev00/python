# Check if a given number is even and greater than 100.

number = float(input("Enter a number: "))

if number % 2 == 0 and number > 100:
    print(f"{number} is even and greater than 100.")
else:
    print("Either number is not even or not greater than 100")