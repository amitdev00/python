# 1) Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

# Expected Output :

# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

temp = float(input("Enter the temprature:"))
temp_type = input("Enter your temprature type(C or F): ").upper()
print(f"The given temprature is: {temp}°{temp_type}")

fahrenheit = temp * 1.8 + 32
celsius = (temp - 32) * (5/9)

if temp_type == "C":
    C = temp
    print(f"the temprature in fahrenheit is: {fahrenheit}°F")
elif temp_type == "F":
    F = temp
    print(f"The temprature in fahrenheit is: {celsius}°C")
else:
    print("Something is wrong.")