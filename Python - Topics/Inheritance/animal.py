# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, age):
#         self.age = age
#         super().__init__(name)
        

#     def speak(self):
#         print("Dog Barks.")

# class Cat(Dog):
#     def __init__(self, breed):
#         self.breed = breed
#         super().__init__(breed)
        

#     def speak(self):
#         print("Cat Meow.")

# cat = Cat("asds", 34, "fgs")


class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)

    def speak(self):
        print("Dog Barks.")

class Cat(Dog):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name, 67) # Providing a default age for the cat, or better, just remove age here.

    def speak(self):
        print("Cat Meow.")

cat = Cat("asds", "feline") # Corrected instantiation
print(cat.speak())
