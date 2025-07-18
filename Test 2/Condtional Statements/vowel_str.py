# Check if a character is a vowel or consonant.


vowels = ["a", "e", "i", "o", "u"]
character = str(input("Enter a alphabet: "))

if character in vowels:
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonent.")