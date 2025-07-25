# Write a Python code to check if the given number is a palindrome. 
# A palindrome number reads the same forwards and backward. 
# For example, 545 is a palindrome number.

def check_palindrome():
    user_input = int(input("Enter a number: "))
    print(f"Given Integer is: {user_input}")

    convert_to_str = str(user_input)
    print(f"The integer is converted to string format: {user_input}")

    reverse_string = convert_to_str[::-1]
    print(f"The reversed string is: {reverse_string}")

    if reverse_string == convert_to_str:
        print(f"{user_input} is a Palindrome number.")
    else:
        print(f"{user_input} is no a Palindrome number.")
    
    return True

y = check_palindrome()
print(y)


