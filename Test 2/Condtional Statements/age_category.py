# Categorize age group based on user input (child, adult, senior)

age = int(input("Enter age of the person: "))

if 18 > age > 0:
    print("Child.")
elif 60 > age >= 18:
    print("Adult.")
elif  age >= 60:
    print('Senior.')