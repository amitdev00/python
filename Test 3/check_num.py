# Count how many times a digit  occurs in a number

number = int(input("Enter a number: "))
count_check = int(input("Enter the digit you want to count: "))
convert_to_str = str(number)
convert_to_str = str(count_check)

count = 0

for num in convert_to_str:
    if int(num) == int(count_check):
        count += 1
print(count)
    



    

