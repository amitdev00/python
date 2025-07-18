# caluculate the sum of numbers from 1 to given number

i = 1
sum = 0
user_input = int(input("Enter a number: "))
while i <= user_input:
    sum = sum + i
    i += 1
print (f"The sum of the first {user_input} is: {sum} ")

