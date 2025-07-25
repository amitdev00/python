# Write a Python code to display numbers from a list divisible by 5

def divisible_by_5():
    list = []
    user_input = int(input("Enter how many elements you want to add in the list: "))

    for  i in range(user_input):
        list_numbers = int(input("Enter the numbers you want to add in the list: "))

        list.append(list_numbers)
    print(list)

    for number in list:
        if number % 5 == 0:
            print(f"The number divisible by 5 is: {number}")
        else:
            print(f"The number not divisible by 5 is: {number}")

    
    return list

y = divisible_by_5()
print(y)