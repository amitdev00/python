#checking if numbers are equal or not
num1 = 10
num2 = 20
num3 = 30

#syntax of if elif  statement
if ((num1 > num2) & (num1 > num3)):
    print("num1 is greater than num2, num3")
elif((num2 > num1)and(num2 > num3)):
    print("num2 is greater than num1, num3")
else:
    print("num3 is greater.")
