# create program in python which prints the pyramid using star symbol

# n = 5
# for i in range(n):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()

lines = int(input("Enter number of lines of stars you want to print: "))

for i in range(lines):
    for j in range(lines - i):
        print(" ", end = "")
    for k in range(2 * i + 1):
        print("*", end = "")
    print()