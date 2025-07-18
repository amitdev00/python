# Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria:
# Unit					Price
# First 100 Units 				No charge
# Next 100 Units 				rs 5 per Unit
# After 200 Units 				Rs 10 per Unit

user_units = int(input("Enter the unit you used: "))

if user_units <= 100:
    print("No Charge.")
elif (user_units <= 200 and user_units >100):
    print(f"Your bill is: Rs{user_units * 5}")
else:
    print(f"Your bill is: Rs{user_units * 10} ")