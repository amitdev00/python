#  Program to check if a number is divisible by both 3 and 5.

user_input = int(input("Enter a number: "))

if user_input % 3 == 0 and user_input % 5 == 0:
    print(f"{user_input} is divisible by both 3 and 5.")
else:
    print(f"{user_input} is not divisible by both 3 and 5.")