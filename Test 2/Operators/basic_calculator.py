#making a simple caluculator that perform all arithmatic operations

oper_ator = ["+", "-", "*", "/", "%", "//"]

num1 = int(input("Enter the first number: "))
user_input = input("Enter the operation you want to perform:")
num2 = int(input("Enter the second number:"))

if user_input == oper_ator[0]:
    print(f"{num1} {user_input} {num2} = ", num1 + num2)
elif user_input == oper_ator[1]:
    print(f"{num1} {user_input} {num2} = ", num1 - num2)
elif user_input == oper_ator[2]:
    print(f"{num1} {user_input} {num2} = ", num1 * num2)
elif user_input == oper_ator[-3]:    
    if num2 == 0:
        print("Can't divide by zero.")
    else:
        print(f"{num1} {user_input} {num2} = ", num1 / num2)
elif user_input == oper_ator[-2]:
    print(f"{num1} {user_input} {num2} = ", num1 % num2)
elif user_input == oper_ator[-1]:
    print(f"{num1} {user_input} {num2} = ", num1 // num2)
else:
    print("May Be! You have entered a wrong operation.")