# make caluculator which take input then operation and then again input and when result is shown
# then it will ask the user do you wish to continue or not
# making a simple caluculator that perform all arithmatic operations

oper_ator = ["+", "-", "*", "/", "%", "//"]

num1 = int(input("Enter the first number: "))
user_input = input("Enter the operation you want to perform:")
num2 = int(input("Enter the second number:"))

while True:

    if user_input == oper_ator[0]:
        res = num1 + num2 
        print(f"{num1} {user_input} {num2} = {res}")
    elif user_input == oper_ator[1]:
        res = num1 - num2
        print(f"{num1} {user_input} {num2} = {res}")
    elif user_input == oper_ator[2]:
        res = num1 * num2
        print(f"{num1} {user_input} {num2} = {res}")
    elif user_input == oper_ator[-3]:
        if num2 == 0:
            print("Can't divide by zero.")
        else:
            res = num1 / num2
            print(f"{num1} {user_input} {num2} = {res}")
    elif user_input == oper_ator[-2]:
        res = num1 % num2
        print(f"{num1} {user_input} {num2} = {res}")
    elif user_input == oper_ator[-1]:
        res = num1 // num2
        print(f"{num1} {user_input} {num2} = {res}")
    else:
        print("May Be! You have entered a wrong operation.")
    

    continue_input = str(input("Do you wish to continue(y for yes/ n for no)?"))
    user_ans = "y", "n"
    
    if continue_input == "y":
        num1 = int(input("Enter the first number: "))
        user_input = input("Enter the operation you want to perform:")
        num2 = int(input("Enter the second number:"))  
    elif continue_input == "n":
        print("You choose to terminate the loop.")
        break
