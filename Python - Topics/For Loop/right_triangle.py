# Print a right angled triangle pattern using for loop

lines = int(input("Enter the number lines of star you want to print: "))

for i in range(lines):
    for j in range(i + 1):
        print("*", end = " ")
    print()