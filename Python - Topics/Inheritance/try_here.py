class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Makes a sound.")

class Dog(Animal):
    def  __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Bark")

buddy = Dog("Buddy")
buddy.speak()

anim = Animal("Generic Animal")
anim.speak()