# Write a program to count vowels in a string

count = 0
vowels = ["a", "e", "i", "o", "u"]
word = str(input("Enter a word to count vowels: "))

for char in word:
    if char in vowels:
        print(count)
        count += 1
print(f"Total words in {word} is {count}")