class First:
    def printMethod(self):
        print("First")

class Second:
    def printMethod(self):
        print("Second")

class Third(First, Second):
    def printMethod(self):
        First.printMethod(self)
        Second.printMethod(self)
        
    
obj_third = Third()
print(obj_third.printMethod())