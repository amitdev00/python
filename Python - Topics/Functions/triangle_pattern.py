# create a function which is used to print star pattern in triangle shape

def triangle():
    lines = int(input("Enter number of lines: "))

    for i in range(1, lines + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    return f" The {lines} number of triangle has been created."


tri_angle = triangle()
print(tri_angle)
