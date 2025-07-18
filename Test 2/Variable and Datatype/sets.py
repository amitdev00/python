# Write a program to remove duplicate values from a list using sets

list1 = ['amit', 'kumar', 'abhishek', 'sharma', 'suryansh', 'thakur']
list2 = ['ruplal', 'sharma', 'rajesh', 'mahatre', 'mahavesh', 'sharma']

list1.extend(list2)
print(list1)

sets = set(list1)
print(sets.union())

list1 = list(sets)
print(list1)



