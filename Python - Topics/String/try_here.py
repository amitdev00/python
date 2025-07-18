#print string
str = " this is a string. "
str1 = "this is a second string."
a = 1
b = 2
print(str)

#check string
print("string" in str)

#check if not in string
print("this" not in str)

#slicing string
print(str[4:8])

#slice from the start
print(str[:10])

#slice to the end
print(str[2:])

#negative indexing
print(str[-1])
print(str[::-1])
print(str[::-2])

#uppercase
print(str.upper())

#lowercase
print(str.lower())

#remove whitespace
print(str.strip())

#replace string
print(str.replace("string", "flower"))

#split string
print(str.split("this"))

#string concatenation
print(str + str1)

#f strings
print(f"{a}.", str, f"{b}.", str1)

#placeholders and modifiers
print(f"what is this ? {a} {str}")