# Create a new dictionary 

dict = {
    "Country" : "USA",
    "Capital" : "Washington, D.C.",
    "Population" : 331002651,
    "Area (sq km)" : 9833517,
    "Official Language" : "English",
}

print(dict) 

#Adding a new key-value pair to the dictionary
dict["Currency"] = "US Dollar"
print("After adding currency, the dictionary is:", dict)

#Getting the value of a specific key
capital = dict.get("Capital")
print("The capital of the country",dict.get("Country")," is:", capital)

#Getting the length of the dictionary
print("The length of the dictionary is  ", len(dict))

#Getting the type of dictionary
print(type(dict))
print(type(dict["Population"]))

#Accessing Dictionary Items
print(dict.get("Population"))

#Getting the keys of the dictionary
print(dict.keys())

#Getting the values of the dictionary
print(dict.values())

#Getting items(in key value pairs) of  the dictionary
print(dict.items())

#Change the specific values of keys in the dictionary
dict["Official Language"] = "Hindi"
print("After changing the dictionary", dict)