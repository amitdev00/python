# Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.

def bool_check():

    list = []
    user_input = int(input("Enter how many number you want to add in list: "))
    for i in range(user_input):    
        numbers = int(input(f"Enter the numbers you want to add to the list {i + 1}: "))
        list.append(numbers)

    first_index = list[0]
    last_index = list[-1]

    if first_index == last_index:
        return True
    else:
        return False


        return list
y = bool_check()
print(y)
