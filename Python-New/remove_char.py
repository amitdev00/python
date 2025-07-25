# Write a Python code to remove characters from a string from 0 to n and return a new string.

def reomve_char():
    string1 = str(input("Enter a string: "))
    user_input = int(input("Enter the number of character you want to remove from the string: "))
    new_string = []

    print(f"The string enter by the user is: {string1}")
    print(F"Number of character user want to remove from the string is: {user_input}")

    sliced_string = string1[user_input :]

    new_string.append(sliced_string)


    return f"The new string is: {new_string}"

print(reomve_char())