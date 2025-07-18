# Create a program that checks if a given character
# is a vowel (a, e, i, o, u) using a single if statement with or operators.

vowels = ["a", "e", "i", "o", "u"]
user_input = str(input("Enter a alphabet:"))
print("You have entered", user_input)

if user_input in vowels:
    print(f"{user_input} is a vowel.")
else:
    print(f"{user_input} is not a vowel.")
