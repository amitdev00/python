# Write a Python code to find how often the substring “Emma” appears in the given string.
# Given:
# str_x = "Emma is good developer. Emma is a writer"

user_input = str(input("Enter the word you want to check how many time it comes: "))
string = "Emma is good developer. Emma is a writer."

count_string = string.count(user_input)
print(count_string)


