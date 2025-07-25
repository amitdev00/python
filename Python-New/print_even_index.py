# Write a Python code to accept a string from the user and display characters present at an even index number.

string = str(input("Enter a string: "))

for i in range(0, len(string) - 1, 2):
    print(string[i])
