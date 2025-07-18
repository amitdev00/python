# 4 - Count how many times each character appears in a string.

count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
str = "hello! India is a beautiful country."

for char in str:
    if char in vowels:
        count += 1
print(f" there are {count} vowels in the string.")