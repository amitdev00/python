# 6 - Create a program to merge two dictionaries.

dict1 = {
    "fname" : "Amit Kumar",
    "lname" : "Kumar"
}

dict2 = {
    "age" : 21,
    "course" : "Python"
}

# list1 = list(dict1.items())
# list2 = list(dict2.items())
# print(list1)
# print(list2)

# list1.extend(list2)
# print(list1)

# dict1 = dict(list1)
# print(dict1)

# dict1.update(dict2)
# print(dict1)

# result = dict1 | dict2
# print(result)

dict3 = {**dict1, **dict2}
print(dict3)