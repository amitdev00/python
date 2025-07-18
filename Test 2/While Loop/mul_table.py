# Print the multiplication table of a given number.

intial_value = 1
number = int(input("Enter a number: "))

while intial_value <= 10:
    
    output = number * intial_value
    print(f"{number} * {intial_value} = {output} " )
    intial_value += 1
