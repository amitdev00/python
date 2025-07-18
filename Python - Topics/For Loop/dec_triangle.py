# Print a pattern of star symbols in the shape of triangle

user_input = int(input("Select the number of rows you want to print: "))

for i in range(user_input):
    for j in range(i, user_input):
        print("*", end = " ")
    print()