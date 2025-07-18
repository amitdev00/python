# Write a function called is_leap() that accepts one parameter i.e. year. 
# The function should check whether the year is a leap year or not.

def leap_year():
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            print(f"{year}: Not a leap year")
        else:
            print(f"{year}: Leap year")
    else:
        print("Invalid Output.")

result = leap_year()
print(result)