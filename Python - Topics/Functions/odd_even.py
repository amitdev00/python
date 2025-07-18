# Create a function which tells number is odd or even

def odd_even():
    a = int(input("Enter a number: "))
    if a % 2 == 0:
        print(f"{a} is even.")
    elif a % 2 != 0:
        print(f"{a} is odd.")
    else:
        print("Invalid Operation.")
    return a

user = odd_even()
print(user)