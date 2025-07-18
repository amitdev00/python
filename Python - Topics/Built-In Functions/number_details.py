# Takes a number as input from the user (integer).
# Tells if the number is even or odd.
# Converts it to binary and prints it.
# Converts the number to float and string, and displays their types.
# Calculates and prints the cube of the number.
# Displays the absolute value (to handle if user gives negative).
def number_details():
    number = int(input("Enter the number: "))

    if number % 2 == 0:
        print(f"{number} is even.")
    else: 
        print(f"{number} is odd.")

    binary_number = bin(number)
    print(f"the binary number of {number} is: {binary_number}\nthe type of binary number is: {type(binary_number)}")

    float_number = float(number)
    print(f"The float number of {number} is: {float_number}\nthe type of float number is: {type(float_number)}")

    cube_number = pow(number, 3)
    print(f"the cube of the {number} is: {cube_number}")

    absolute_value = abs(number)
    print(f"the absolute value of the {number} is:  {absolute_value}") 

    return number

y = number_details()
print(y)