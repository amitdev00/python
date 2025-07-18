# Write a Python function to find the maximum of three numbers

def max_num():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    return max(num1, num2, num3)

largest_number = max_num()
print(f"{largest_number} is the largest among three numbers.")