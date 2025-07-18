# write a program to print the table of the number entered by the user

initial_value = 1
user_input = int(input("Enter a number: "))
print(f"The table of {user_input} is ")
while initial_value <= 10:
    print(f"{user_input} * {initial_value} = {user_input * initial_value}")
    initial_value += 1