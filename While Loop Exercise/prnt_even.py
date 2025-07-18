# Write a program to print all even numbers that fall between two numbers (exclusively both numbers) 
# entered from the user using while loop

even_numbers = 0 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
even_numbers = num1
print(f"Even numbers in the range of {num1} and {num2} are:")

while even_numbers <= num2:
    if even_numbers % 2 == 0:
        even_numbers = even_numbers + 2
        print(even_numbers, end = " ")
    elif even_numbers % 2 != 0:
        even_numbers = even_numbers + 1
        print(even_numbers, end = " ")