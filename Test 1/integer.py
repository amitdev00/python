# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and not in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

user_input = int(input("Enter any integer: "))

if (user_input % 2 != 0):
    print("Weird.")
elif (user_input % 2 == 0 and range(0, user_input)):
    print("Not Weird.")
elif(user_input % 2 == 0 and user_input > range(0, user_input)):
    print("Not Weird.")