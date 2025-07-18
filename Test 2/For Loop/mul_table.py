# Print the multiplication table of a given number.

num = int(input("Enter a number: "))

for i in range(1,11):
    output = (num * i)
    print(f"{num} *  {i} = {output}")
    i += 1