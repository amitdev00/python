# Print the list of fruits using list comprehension method.

fruits = ["apple", "mango", "banana", "kiwi", "papaya"]

new_fruit_list= [fruit for fruit in fruits if fruit in fruits]
print(new_fruit_list)

new_list = [num for num in range(0, 11)]
print(new_list)

new_list = ["hello" for string in fruits]
print(new_list)