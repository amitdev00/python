# 5 - Write a program to convert a tuple into a dictionary.

cars = (("Mercedes","S-Class"), ("BMW","R8"), ("Audi", "A6"), ("Rolls Royce", "Phantom"), ("Land Rover", "Range Rover"))

cars_list  = list(cars)
print(cars_list)

dict_cars = dict(cars_list)
print(dict_cars)