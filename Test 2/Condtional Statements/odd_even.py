# Print "odd" or "even" for a given number

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even.")
elif num % 2 != 0:
    print(f"{num} is Odd.")