# Write a  while loop to find the sum of digits of a number entered by the user.

numbers = int(input("Enter a number: "))
sum = 0

while numbers != 0:
    digit = numbers % 10   #this gives the remainder by which we can get the last digit
    sum += digit         #this adds the digit to the sum
    numbers //= 10      # this one removes the last digit
print(sum)
    




