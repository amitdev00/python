# Reverse a given string using a loop.

original_string = "hello"
reversed_string = ""
index = len(original_string) - 1

while index >= 0:
    reversed_string = reversed_string + original_string[index]
    index -= 1
print(f"Original string is: {original_string}")
print(f"Reversed String is: {reversed_string}")
     
