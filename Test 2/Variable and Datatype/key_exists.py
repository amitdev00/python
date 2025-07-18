# 10 - Write a function to check if a key exists in a dictionary.

dict = {
    "fname" : "Amit",
    "lname" : "Kumar",
    "age"   : 21
 }

user_key = str(input("Enter the key you want to check: "))
if user_key in dict:
    print(f"{dict.get(user_key)} is present in the dictionary")