# creating new dictionary

country = {
    "India": "Delhi",
    "England": "Washington DC",
    "Pakistan": "Islamabad",
    "Bangladesh": "Dhaka"
}

print(country)

# print dictionary items
print(country["India"])

# getting length of the dictionary
print(len(country))

# geting dictionary items
print(country.get("Bangladesh"))

# getting keys of the dictionary
print(country.keys())

# getting values of the dictionary
print(country.values())

# getting items of the dictionary(in key-value pairs)
print(country.items())

# check if exists
if "England" in country:
    print("Exists")

# change values
country["Pakistan"] = "Empty"
print(country)

# update dictionary
country.update({"Pakistan": "Islamabad"})
print(country)

# removing item from the dictionary
country.pop("England")
print(country)

# removing last item from the dictionary
country.popitem()
print(country)

# deleting item from the dictionary
del country["Pakistan"]
print(country)

# emptying the dictionary
country.clear()
print(country)
