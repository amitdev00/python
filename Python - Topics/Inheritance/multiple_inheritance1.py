# create a base and adn derived class which shows the multiple inhereitance

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B:
    def __init__(self, c, d):
        self.c = c
        self.d = d

class C(A, B):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        B.__init__(self, c, d)
    
    def numbers(self):
        print(f"a = {self.a}\nb = {self.b}\nc = {self.c}\nd = {self.d} ")


obj_c = C(1, 2, 3, 4)
print(obj_c.numbers())


