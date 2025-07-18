# Write a temperature converter with options (Celsius <-> Fahrenheit)
# F = C(9⁄5) + 32
# C = (F − 32) × 5⁄9

temprature = float(input("Enter the temprature: "))
type_temprature = str(input("Enter the type of the temprature('c' - celcius / 'f' - fahrenheit):")).upper()

print(f"Given temprature is: {temprature}°{type_temprature}")

if type_temprature == 'C':
    fahrenheit = (temprature * (9 / 5)) + 32
    print(f"Temprature in Fahrenheit is {fahrenheit}°F")
elif type_temprature == "F":
    celsius = (temprature - 32) * (5 / 9)
    print(f"Temprature in Celsius is {celsius}°C")
else:
    print("Invalid Input.")
