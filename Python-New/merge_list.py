# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list 
# and even numbers from the second list.

list1 = [12, 35, 68, 80, 78, 65, 66, 20]
list2 = [67, 89, 56, 88, 64, 79, 65, 88]

new_list = []

for number in list1:
    if number % 2 != 0:
        new_list.append(number)
for number in list2:
    if number % 2 == 0:
        new_list.append(number)

print(new_list)
