# Write a program to count the number of vowels in a string.
vowels = ["a","e", "i", "o", "u"]
string = "hello"
count = 0 
index = 0 

while index < len(string):
    char = string[index]
    if string[index] in vowels:
        count += 1
    index += 1
print(count)