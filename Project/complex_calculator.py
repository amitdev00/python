# Make a Caluculator which performs arithmetic operaations
# took inputs
num1 = int(input("Enter a number: "))
operation = input("Enter the operation you want to perform: ")
num2 = int(input("Enter a number: "))

# performed operations
if operation == "+":
    res = num1 + num2
elif operation == "-":
    res = num1 - num2
elif operation == "*":
    res = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Can't divide by zero.")
    else:
        res = num1 / num2
elif operation == "%":
    res = num1 % num2
# prints result for first time
print(f"{num1} {operation} {num2} = {res}")

# asks "want to do more operations or not"
user_input = input("Do you want to add more operators(y/n)? ")

# this if statement is when user does not respond
if user_input == "":
    while bool(user_input) == False:
        break
# this else statement is when user responds
else:
    # when user enters some input values becomes true
    while bool(user_input) == True:

        # this if statement is used when user wants to performs more than one operations
        if user_input == "y":
            operation = input("Enter the operation you want to perform: ")
            num2 = int(input("Enter a number: "))
            if operation == "+":
                result = res + num2
            elif operation == "-":
                result = res - num2
            elif operation == "*":
                result = res * num2
            elif operation == "/":
                if num2 == 0:
                    print("Can't divide by zero.")
                else:
                    result = res / num2
            elif operation == "%":
                result = res % num2
            print(f" {res} {operation} {num2} = {result} ")
            user_input = input("Do you want to add more operators(y/n)? ")
            res = result

        # this is used when user does not want to continue performing operations
        elif user_input == "n":
            user_input = input("Do you want to add more operators(y/n)? ")
            print(f"You final result is: {result}")
            break
