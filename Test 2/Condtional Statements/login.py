# Create a simple login system using if-else.

name = str(input("Enter your name: "))
create_user = input("Create a username: ")
create_pass = input("Create Password: ")

login = str(input("Do you want to login to you i'd('y' - yes / 'n' - no): "))

if login == 'y':
    print("Enter your login details.")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_name == create_user and password == create_pass:
        print("Login Successful.")
    elif user_name != create_user:
        print("Wrong username.")
    elif password != create_pass:
        print("Wrong password.")
elif login == 'n':
    print("Your account has been removed.")
    print("You have to enter the details one more time.")

